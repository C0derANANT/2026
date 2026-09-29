from __future__ import annotations

import base64
import math
import random
import re
import shutil
import subprocess
import textwrap
import wave
from dataclasses import dataclass
from io import BytesIO
from pathlib import Path
from typing import Any

import requests
from PIL import Image, ImageDraw, ImageFilter, ImageFont

from .config import Settings


class ServiceError(RuntimeError):
    """A recoverable provider or renderer error."""


def slugify(value: str, max_length: int = 42) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return value[:max_length].strip("-") or "reel"


def write_text(path: Path, value: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8")
    return path


def system_font(bold: bool = False) -> str:
    candidates = (
        ["/System/Library/Fonts/Supplemental/Arial Bold.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]
        if bold
        else ["/System/Library/Fonts/Supplemental/Arial.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]
    )
    for candidate in candidates:
        if Path(candidate).exists():
            return candidate
    return ""


def font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    path = system_font(bold)
    return ImageFont.truetype(path, size) if path else ImageFont.load_default()


@dataclass
class ScriptResult:
    text: str
    source: str


class Ollama:
    def __init__(self, settings: Settings):
        self.settings = settings

    def generate(self, prompt: str, model: str, timeout: int = 120) -> str:
        response = requests.post(
            f"{self.settings.ollama_url.rstrip('/')}/api/generate",
            json={"model": model, "prompt": prompt, "stream": False, "options": {"temperature": 0.8}},
            timeout=timeout,
        )
        response.raise_for_status()
        payload = response.json()
        return str(payload.get("response", "")).strip()


class ScriptWriter:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.ollama = Ollama(settings)

    def create(self, topic: str, style: str) -> ScriptResult:
        prompt = (
            f"Write a 2–3 sentence Instagram Reel narration about: {topic}. "
            f"Style: {style}. Start with a bold three-second hook. Keep it factual, natural, "
            "spoken, high-energy, under 75 words, and end with a concise call to action. "
            "Return only the narration—no labels, emojis, hashtags, claims you cannot verify, "
            "or production directions."
        )
        try:
            answer = self.ollama.generate(prompt, self.settings.ollama_model)
            cleaned = " ".join(answer.split())
            if len(cleaned.split()) >= 12:
                return ScriptResult(cleaned, f"Ollama · {self.settings.ollama_model}")
        except (requests.RequestException, ValueError, ServiceError):
            pass
        return ScriptResult(self._fallback(topic, style), "Local template fallback (start Ollama for Mistral)")

    @staticmethod
    def _fallback(topic: str, style: str) -> str:
        subject = topic.strip().rstrip(".?!")
        hooks = {
            "Professional": f"Here is the signal everyone is missing about {subject}.",
            "Trendy": f"Stop scrolling—{subject} is the trend worth watching.",
            "Funny": f"Plot twist: {subject} is about to make your group chat sound smart.",
            "Cinematic": f"Picture this: {subject} is changing the story in real time.",
        }
        return (
            f"{hooks.get(style, hooks['Trendy'])} It matters because the people who understand it early "
            "can turn a headline into a real advantage. Save this Reel, then share it with someone building what comes next."
        )


class ImageFinder:
    def __init__(self, settings: Settings):
        self.settings = settings

    def create_storyboard(self, topic: str, style: str, destination: Path, count: int = 6, source: str = "Auto") -> tuple[list[Path], str]:
        destination.mkdir(parents=True, exist_ok=True)
        if source in {"Auto", "Pexels"} and self.settings.pexels_api_key:
            try:
                return self._pexels(topic, destination, count), "Pexels free API"
            except (requests.RequestException, ValueError, ServiceError):
                pass
        if source in {"Auto", "Unsplash"} and self.settings.unsplash_api_key:
            try:
                return self._unsplash(topic, destination, count), "Unsplash free API"
            except (requests.RequestException, ValueError, ServiceError):
                pass
        if source == "Stable Diffusion (local)":
            try:
                return self._automatic1111(topic, style, destination, count), "Local Stable Diffusion / Automatic1111"
            except (requests.RequestException, ValueError, ServiceError):
                pass
        return self._local_cards(topic, style, destination, count), "Local original storyboard art"

    def _download(self, url: str, target: Path) -> Path:
        response = requests.get(url, timeout=45)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content)).convert("RGB")
        image.save(target, quality=92)
        return target

    def _pexels(self, topic: str, destination: Path, count: int) -> list[Path]:
        response = requests.get(
            "https://api.pexels.com/v1/search",
            params={"query": topic, "per_page": count, "orientation": "portrait"},
            headers={"Authorization": self.settings.pexels_api_key},
            timeout=30,
        )
        response.raise_for_status()
        photos = response.json().get("photos", [])[:count]
        if len(photos) < 3:
            raise ServiceError("Pexels returned too few portrait images")
        return [self._download(photo["src"]["large2x"], destination / f"pexels-{number:02d}.jpg") for number, photo in enumerate(photos, 1)]

    def _unsplash(self, topic: str, destination: Path, count: int) -> list[Path]:
        response = requests.get(
            "https://api.unsplash.com/search/photos",
            params={"query": topic, "per_page": count, "orientation": "portrait", "client_id": self.settings.unsplash_api_key},
            timeout=30,
        )
        response.raise_for_status()
        photos = response.json().get("results", [])[:count]
        if len(photos) < 3:
            raise ServiceError("Unsplash returned too few portrait images")
        return [self._download(photo["urls"]["regular"], destination / f"unsplash-{number:02d}.jpg") for number, photo in enumerate(photos, 1)]

    def _automatic1111(self, topic: str, style: str, destination: Path, count: int) -> list[Path]:
        paths: list[Path] = []
        for number in range(count):
            prompt = f"editorial vertical social video frame, {topic}, {style} style, dynamic composition, no text, no watermark, variation {number + 1}"
            response = requests.post(
                f"{self.settings.automatic1111_url.rstrip('/')}/sdapi/v1/txt2img",
                json={"prompt": prompt, "negative_prompt": "text, watermark, logo, blurry", "width": 768, "height": 1344, "steps": 25},
                timeout=180,
            )
            response.raise_for_status()
            image_data = response.json().get("images", [None])[0]
            if not image_data:
                raise ServiceError("Stable Diffusion did not return an image")
            image = Image.open(BytesIO(base64.b64decode(image_data.split(",")[-1]))).convert("RGB")
            target = destination / f"sdxl-{number + 1:02d}.jpg"
            image.save(target, quality=92)
            paths.append(target)
        return paths

    def _local_cards(self, topic: str, style: str, destination: Path, count: int) -> list[Path]:
        palettes = {
            "Professional": [(11, 25, 51), (21, 69, 91), (44, 158, 167)],
            "Trendy": [(32, 14, 67), (112, 29, 126), (250, 97, 157)],
            "Funny": [(30, 25, 13), (116, 66, 21), (255, 196, 67)],
            "Cinematic": [(14, 14, 28), (43, 23, 70), (12, 87, 105)],
        }
        colours = palettes.get(style, palettes["Trendy"])
        words = re.findall(r"[A-Za-z0-9]+", topic)[:6] or ["YOUR", "STORY"]
        paths: list[Path] = []
        for frame in range(count):
            image = Image.new("RGB", (1080, 1920), colours[0])
            draw = ImageDraw.Draw(image, "RGBA")
            for y in range(1920):
                mix = y / 1919
                fill = tuple(int(colours[0][channel] * (1 - mix) + colours[1][channel] * mix) for channel in range(3))
                draw.line((0, y, 1080, y), fill=fill)
            random.seed(f"{topic}-{style}-{frame}")
            for _ in range(25):
                x, y = random.randint(-100, 1180), random.randint(-100, 2020)
                radius = random.randint(20, 160)
                draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(*colours[2], random.randint(18, 75)))
            cx, cy = 540, 940
            for index, radius in enumerate([430, 310, 205]):
                offset = int(math.sin(frame * 1.15 + index) * 44)
                draw.ellipse((cx - radius + offset, cy - radius, cx + radius + offset, cy + radius), outline=(255, 255, 255, 80 - index * 16), width=10)
            draw.rounded_rectangle((90, 130, 990, 252), radius=61, fill=(255, 255, 255, 28), outline=(255, 255, 255, 110), width=2)
            tag = f"FREE AI REEL · {frame + 1:02d}"
            tag_font = font(35, True)
            tag_box = draw.textbbox((0, 0), tag, font=tag_font)
            draw.text(((1080 - (tag_box[2] - tag_box[0])) // 2, 168), tag, font=tag_font, fill=(255, 255, 255))
            headline = " ".join(words[frame % len(words):] + words[:frame % len(words)])[:28].upper()
            headline_font = font(114, True)
            line_y = 700
            for line in textwrap.wrap(headline, width=13)[:3]:
                box = draw.textbbox((0, 0), line, font=headline_font)
                draw.text(((1080 - (box[2] - box[0])) // 2, line_y), line, font=headline_font, fill=(255, 255, 255))
                line_y += 130
            draw.rounded_rectangle((170, 1390, 910, 1540), radius=42, fill=(*colours[2], 230))
            motif = ["IDEA", "BUILD", "SHIFT", "CREATE", "DISCOVER", "SHARE"][frame]
            motif_font = font(54, True)
            motif_box = draw.textbbox((0, 0), motif, font=motif_font)
            draw.text(((1080 - (motif_box[2] - motif_box[0])) // 2, 1435), motif, font=motif_font, fill=(14, 14, 28))
            target = destination / f"storyboard-{frame + 1:02d}.jpg"
            image.filter(ImageFilter.GaussianBlur(radius=0.1)).save(target, quality=92)
            paths.append(target)
        return paths


class VoiceMaker:
    def __init__(self, settings: Settings):
        self.settings = settings

    def synthesize(self, script: str, destination: Path) -> tuple[Path, str]:
        destination.mkdir(parents=True, exist_ok=True)
        wav_path = destination / "narration.wav"
        try:
            from TTS.api import TTS  # type: ignore[import-not-found]

            engine = TTS(model_name=self.settings.tts_model, progress_bar=False, gpu=False)
            engine.tts_to_file(text=script, file_path=str(wav_path))
            return wav_path, f"Coqui TTS · {self.settings.tts_model}"
        except (ImportError, OSError, RuntimeError, ValueError):
            pass
        if shutil.which("say") and self.settings.ffmpeg_available:
            aiff_path = destination / "narration.aiff"
            subprocess.run(["say", "-o", str(aiff_path), script], check=True, capture_output=True)
            self._convert(aiff_path, wav_path)
            return wav_path, "macOS say fallback (install Coqui TTS for preferred voice)"
        self._silent_wav(wav_path, max(8, min(35, len(script.split()) / 2.2)))
        return wav_path, "Silent local fallback (install Coqui TTS for voiceover)"

    def _convert(self, source: Path, destination: Path) -> None:
        subprocess.run([self.settings.ffmpeg_bin, "-y", "-i", str(source), "-ar", "44100", str(destination)], check=True, capture_output=True)

    @staticmethod
    def _silent_wav(path: Path, duration: float) -> None:
        with wave.open(str(path), "w") as stream:
            stream.setnchannels(1)
            stream.setsampwidth(2)
            stream.setframerate(44100)
            stream.writeframes(b"\x00\x00" * int(44100 * duration))


class MusicMaker:
    def __init__(self, settings: Settings):
        self.settings = settings

    def create(self, genre: str, volume: int, duration: float, destination: Path) -> tuple[Path, str]:
        if not self.settings.ffmpeg_available:
            raise ServiceError("FFmpeg is required to generate the local background track")
        library = Path(self.settings.music_library_dir).expanduser() if self.settings.music_library_dir else None
        if library and library.is_dir():
            tracks = sorted(path for path in library.iterdir() if path.suffix.lower() in {".mp3", ".wav", ".m4a", ".aac"})
            if tracks:
                return self._from_library(tracks[hash(genre) % len(tracks)], volume, duration, destination)
        frequency = {"Pop": "261.63", "Chill": "174.61", "Hip-Hop": "98", "Indie": "220", "Upbeat": "329.63"}.get(genre, "220")
        gain = max(0.0, min(1.0, volume / 100)) * 0.055
        target = destination / "background-music.mp3"
        fade_at = max(0, duration - 1.5)
        filter_graph = f"sine=frequency={frequency}:sample_rate=44100:duration={duration},volume={gain},afade=t=in:st=0:d=1,afade=t=out:st={fade_at}:d=1.5"
        subprocess.run([self.settings.ffmpeg_bin, "-y", "-f", "lavfi", "-i", filter_graph, "-q:a", "5", str(target)], check=True, capture_output=True)
        return target, "Locally generated ambient bed (royalty-free)"

    def _from_library(self, track: Path, volume: int, duration: float, destination: Path) -> tuple[Path, str]:
        target = destination / "background-music.mp3"
        gain = max(0.0, min(1.0, volume / 100)) * 0.45
        fade_at = max(0, duration - 1.5)
        filter_graph = f"volume={gain},afade=t=in:st=0:d=1,afade=t=out:st={fade_at}:d=1.5"
        subprocess.run(
            [self.settings.ffmpeg_bin, "-y", "-stream_loop", "-1", "-i", str(track), "-t", f"{duration:.3f}", "-af", filter_graph, "-q:a", "5", str(target)],
            check=True,
            capture_output=True,
        )
        return target, f"Local licensed music library · {track.name}"


def media_duration(settings: Settings, media_path: Path) -> float:
    if not settings.ffmpeg_available:
        return 28.0
    result = subprocess.run([settings.ffmpeg_bin, "-i", str(media_path)], capture_output=True, text=True, check=False)
    match = re.search(r"Duration: (\d+):(\d+):(\d+\.\d+)", result.stderr)
    if not match:
        return 28.0
    return int(match.group(1)) * 3600 + int(match.group(2)) * 60 + float(match.group(3))


def srt_time(seconds: float) -> str:
    millis = int(max(0, seconds) * 1000)
    hours, millis = divmod(millis, 3_600_000)
    minutes, millis = divmod(millis, 60_000)
    secs, millis = divmod(millis, 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"


class SubtitleMaker:
    def __init__(self, settings: Settings):
        self.settings = settings

    def create(self, audio: Path, script: str, duration: float, destination: Path) -> tuple[Path, str]:
        target = destination / "subtitles.srt"
        try:
            import whisper  # type: ignore[import-not-found]

            model = whisper.load_model(self.settings.whisper_model)
            result: dict[str, Any] = model.transcribe(str(audio), fp16=False)
            segments = result.get("segments", [])
            if segments:
                entries = []
                for number, item in enumerate(segments, 1):
                    entries.append(f"{number}\n{srt_time(item['start'])} --> {srt_time(item['end'])}\n{item['text'].strip()}\n")
                return write_text(target, "\n".join(entries)), f"Whisper · {self.settings.whisper_model}"
        except (ImportError, OSError, RuntimeError, ValueError):
            pass
        chunks = textwrap.wrap(script, width=42)
        step = duration / max(1, len(chunks))
        entries = [f"{number}\n{srt_time((number - 1) * step)} --> {srt_time(number * step)}\n{line}\n" for number, line in enumerate(chunks, 1)]
        return write_text(target, "\n".join(entries)), "Timed script fallback (install Whisper for speech-to-text)"
