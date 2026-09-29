from __future__ import annotations

import json
import shutil
import sqlite3
import subprocess
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

import requests

from .config import Settings
from .services import (
    ImageFinder,
    MusicMaker,
    Ollama,
    ScriptResult,
    ScriptWriter,
    ServiceError,
    SubtitleMaker,
    VoiceMaker,
    media_duration,
    slugify,
    write_text,
)


ProgressCallback = Callable[[int, str], None]


@dataclass
class Analytics:
    viral_score: float
    best_posting_time: str
    hashtags: list[str]
    tips: list[str]
    source: str


@dataclass
class ReelResult:
    reel_id: str
    topic: str
    script: str
    video: Path
    script_file: Path
    bundle: Path
    images: list[Path]
    duration: float
    analytics: Analytics
    notes: list[str]


class HistoryStore:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.settings.data_dir.mkdir(parents=True, exist_ok=True)
        self.db_path = self.settings.data_dir / "reels.sqlite3"
        with self._connect() as db:
            db.execute(
                """CREATE TABLE IF NOT EXISTS reels (
                    reel_id TEXT PRIMARY KEY,
                    created_at TEXT NOT NULL,
                    topic TEXT NOT NULL,
                    style TEXT NOT NULL,
                    script TEXT NOT NULL,
                    video_path TEXT NOT NULL,
                    script_path TEXT NOT NULL,
                    bundle_path TEXT NOT NULL,
                    image_paths TEXT NOT NULL,
                    duration REAL NOT NULL,
                    analytics_json TEXT NOT NULL,
                    notes_json TEXT NOT NULL
                )"""
            )

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    def save(self, result: ReelResult, style: str) -> None:
        with self._connect() as db:
            db.execute(
                """INSERT OR REPLACE INTO reels VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    result.reel_id,
                    datetime.now(timezone.utc).isoformat(),
                    result.topic,
                    style,
                    result.script,
                    str(result.video),
                    str(result.script_file),
                    str(result.bundle),
                    json.dumps([str(image) for image in result.images]),
                    result.duration,
                    json.dumps(asdict(result.analytics)),
                    json.dumps(result.notes),
                ),
            )

    def list(self, query: str = "") -> list[dict]:
        needle = f"%{query.strip()}%"
        with self._connect() as db:
            db.row_factory = sqlite3.Row
            rows = db.execute(
                "SELECT * FROM reels WHERE topic LIKE ? OR created_at LIKE ? ORDER BY created_at DESC", (needle, needle)
            ).fetchall()
        return [dict(row) for row in rows]

    def get(self, reel_id: str) -> dict | None:
        with self._connect() as db:
            db.row_factory = sqlite3.Row
            row = db.execute("SELECT * FROM reels WHERE reel_id = ?", (reel_id,)).fetchone()
        return dict(row) if row else None

    def delete(self, reel_id: str) -> bool:
        record = self.get(reel_id)
        if not record:
            return False
        reel_dir = Path(record["video_path"]).parent
        if reel_dir.is_dir() and reel_dir.parent == self.settings.output_dir:
            shutil.rmtree(reel_dir)
        with self._connect() as db:
            db.execute("DELETE FROM reels WHERE reel_id = ?", (reel_id,))
        return True


class AnalyticsEngine:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.ollama = Ollama(settings)

    def analyse(self, topic: str, script: str) -> Analytics:
        prompt = (
            "Return valid JSON only with keys viral_score (number 1-10), best_posting_time (string, IST), "
            "hashtags (array of exactly 10 strings) and tips (array of 3 concise strings). Analyse this Reel topic and narration. "
            f"Topic: {topic}\nNarration: {script}"
        )
        try:
            raw = self.ollama.generate(prompt, self.settings.analytics_model, timeout=90)
            payload = json.loads(raw[raw.find("{") : raw.rfind("}") + 1])
            hashtags = [str(tag).lstrip("#") for tag in payload["hashtags"]][:10]
            tips = [str(tip) for tip in payload["tips"]][:3]
            if len(hashtags) == 10 and len(tips) == 3:
                return Analytics(
                    viral_score=max(1, min(10, float(payload["viral_score"]))),
                    best_posting_time=str(payload["best_posting_time"]),
                    hashtags=[f"#{tag}" for tag in hashtags],
                    tips=tips,
                    source=f"Ollama · {self.settings.analytics_model}",
                )
        except (requests.RequestException, json.JSONDecodeError, KeyError, TypeError, ValueError, OSError):
            pass
        words = [word.lower() for word in slugify(topic).split("-") if len(word) > 2]
        defaults = ["AI", "Tech", "Innovation", "FutureOfWork", "CreatorTools", "Reels", "TechTok", "LearnOnInstagram", "BuildInPublic", "DigitalCreators"]
        tags: list[str] = []
        for candidate in words + defaults:
            tag = "#" + "".join(part.capitalize() for part in candidate.split("-"))
            if tag not in tags:
                tags.append(tag)
        score = 6.0 + (0.8 if script.split() and len(script.split()) <= 75 else 0) + (0.6 if any(mark in script[:70] for mark in "!?") else 0)
        return Analytics(
            viral_score=round(min(9.2, score), 1),
            best_posting_time="7:30–9:00 PM IST (test against your audience insights)",
            hashtags=tags[:10],
            tips=["Put the strongest visual change in the first second.", "Keep the first caption under eight words.", "Invite saves or shares with one clear call to action."],
            source="Local heuristic fallback (start Ollama + llama2 for local AI analysis)",
        )


class VideoRenderer:
    def __init__(self, settings: Settings):
        self.settings = settings

    def render(self, images: list[Path], narration: Path, music: Path, duration: float, subtitles: Path | None, destination: Path) -> Path:
        if not self.settings.ffmpeg_available:
            raise ServiceError("FFmpeg was not found. Install it with `brew install ffmpeg` or set FFMPEG_BIN.")
        slides_dir = destination / "slides"
        slides_dir.mkdir(parents=True, exist_ok=True)
        clip_seconds = max(2.0, duration / len(images))
        clips: list[Path] = []
        for number, image in enumerate(images, 1):
            clip = slides_dir / f"slide-{number:02d}.mp4"
            fade_start = max(0.1, clip_seconds - 0.38)
            filter_graph = (
                "scale=1296:2304:force_original_aspect_ratio=increase,"
                "crop=1080:1920,"
                "zoompan=z='min(zoom+0.00045,1.10)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=24,"
                f"fade=t=in:st=0:d=0.3,fade=t=out:st={fade_start}:d=0.38,setsar=1"
            )
            subprocess.run(
                [self.settings.ffmpeg_bin, "-y", "-loop", "1", "-framerate", "24", "-i", str(image), "-t", f"{clip_seconds:.3f}", "-vf", filter_graph, "-r", "24", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-an", str(clip)],
                check=True,
                capture_output=True,
            )
            clips.append(clip)
        manifest = destination / "concat.txt"
        manifest_lines = []
        for clip in clips:
            safe_path = clip.as_posix().replace("'", r"'\''")
            manifest_lines.append(f"file '{safe_path}'\n")
        manifest.write_text("".join(manifest_lines), encoding="utf-8")
        base_video = destination / "base-video.mp4"
        subprocess.run([self.settings.ffmpeg_bin, "-y", "-f", "concat", "-safe", "0", "-i", str(manifest), "-c", "copy", str(base_video)], check=True, capture_output=True)
        final_video = destination / "reel.mp4"
        command = [
            self.settings.ffmpeg_bin, "-y", "-i", str(base_video), "-i", str(narration), "-i", str(music),
            "-filter_complex", "[1:a]volume=1[narration];[2:a]volume=1[music];[narration][music]amix=inputs=2:duration=first:weights='1 0.65'[audio]",
            "-map", "0:v", "-map", "[audio]", "-r", "24", "-c:v", "libx264", "-b:v", "7500k", "-maxrate", "8000k", "-bufsize", "12000k", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest",
        ]
        if subtitles:
            escaped = str(subtitles).replace("\\", "\\\\").replace(":", "\\:").replace("'", "\\'")
            command.extend(["-vf", f"subtitles='{escaped}':force_style='FontName=Arial,FontSize=22,PrimaryColour=&H00FFFFFF,OutlineColour=&H00101010,BorderStyle=1,Outline=3,Alignment=2,MarginV=120'"])
        command.extend(["-movflags", "+faststart", str(final_video)])
        subprocess.run(command, check=True, capture_output=True)
        return final_video


class ReelGenerator:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.script_writer = ScriptWriter(settings)
        self.images = ImageFinder(settings)
        self.voice = VoiceMaker(settings)
        self.music = MusicMaker(settings)
        self.subtitles = SubtitleMaker(settings)
        self.analytics = AnalyticsEngine(settings)
        self.renderer = VideoRenderer(settings)
        self.history = HistoryStore(settings)

    def generate(
        self,
        topic: str,
        style: str,
        genre: str,
        volume: int,
        include_subtitles: bool,
        image_source: str,
        progress: ProgressCallback | None = None,
        script_override: str = "",
    ) -> ReelResult:
        topic = topic.strip()
        if not topic:
            raise ServiceError("Enter a topic before generating a Reel.")
        if not self.settings.ffmpeg_available:
            raise ServiceError("FFmpeg is required to render 1080×1920 MP4 files. Install it with `brew install ffmpeg`.")
        report = progress or (lambda _percent, _message: None)
        reel_id = f"{datetime.now().strftime('%Y%m%d-%H%M%S')}-{slugify(topic)}"
        reel_dir = self.settings.output_dir / reel_id
        reel_dir.mkdir(parents=True, exist_ok=False)
        notes: list[str] = []
        report(8, "Step 1/6 · Generating a short-form script")
        script_result = ScriptResult(script_override.strip(), "User-edited script") if script_override.strip() else self.script_writer.create(topic, style)
        script_file = write_text(reel_dir / "script.txt", script_result.text)
        notes.append(f"Script: {script_result.source}")
        report(23, "Step 2/6 · Creating the visual storyboard")
        images, image_note = self.images.create_storyboard(topic, style, reel_dir / "images", source=image_source)
        notes.append(f"Images: {image_note}")
        report(40, "Step 3/6 · Creating voiceover")
        narration, voice_note = self.voice.synthesize(script_result.text, reel_dir)
        notes.append(f"Voice: {voice_note}")
        duration = max(12.0, min(45.0, media_duration(self.settings, narration)))
        report(54, "Step 4/6 · Creating a local royalty-free background bed")
        music, music_note = self.music.create(genre, volume, duration, reel_dir)
        notes.append(f"Music: {music_note}")
        subtitles = None
        if include_subtitles:
            report(65, "Step 5/6 · Generating styled subtitles")
            subtitles, subtitle_note = self.subtitles.create(narration, script_result.text, duration, reel_dir)
            notes.append(f"Subtitles: {subtitle_note}")
        else:
            notes.append("Subtitles: disabled")
        report(78, "Step 6/6 · Rendering 1080×1920 MP4 with motion and fades")
        video = self.renderer.render(images, narration, music, duration, subtitles, reel_dir)
        duration = media_duration(self.settings, video)
        analytics = self.analytics.analyse(topic, script_result.text)
        caption = f"{script_result.text}\n\n{' '.join(analytics.hashtags)}"
        write_text(reel_dir / "caption.txt", caption)
        write_text(reel_dir / "production-notes.txt", "\n".join(notes + [f"Analytics: {analytics.source}", "Video: 1080×1920, 24 FPS, target 7.5 Mbps."]))
        # Keep the archive beside its source directory.  Placing it inside
        # `reel_dir` causes the archive writer to include its own growing file.
        bundle = Path(shutil.make_archive(str(reel_dir.parent / f"{reel_id}-bundle"), "zip", root_dir=reel_dir))
        result = ReelResult(reel_id, topic, script_result.text, video, script_file, bundle, images, duration, analytics, notes)
        self.history.save(result, style)
        report(100, "Done · Reel saved locally and ready to download")
        return result
