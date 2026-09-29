from __future__ import annotations

import os
import shutil
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")


def default_ffmpeg() -> str:
    """Prefer an explicit setting, then PATH, then the bundled free runtime."""
    configured = os.getenv("FFMPEG_BIN")
    if configured:
        return configured
    on_path = shutil.which("ffmpeg")
    if on_path:
        return on_path
    bundled = PROJECT_ROOT / "tools" / "ffmpeg"
    if bundled.exists():
        return str(bundled)
    return "ffmpeg"


@dataclass(frozen=True)
class Settings:
    project_root: Path = PROJECT_ROOT
    ollama_url: str = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434")
    ollama_model: str = os.getenv("OLLAMA_MODEL", "mistral")
    analytics_model: str = os.getenv("ANALYTICS_MODEL", "llama2")
    pexels_api_key: str = os.getenv("PEXELS_API_KEY", "")
    unsplash_api_key: str = os.getenv("UNSPLASH_API_KEY", "")
    automatic1111_url: str = os.getenv("AUTOMATIC1111_URL", "http://127.0.0.1:7861")
    music_library_dir: str = os.getenv("MUSIC_LIBRARY_DIR", "")
    tts_model: str = os.getenv("TTS_MODEL", "tts_models/en/ljspeech/tacotron2-DDC")
    whisper_model: str = os.getenv("WHISPER_MODEL", "base")
    ffmpeg_bin: str = default_ffmpeg()

    @property
    def data_dir(self) -> Path:
        return self.project_root / "data"

    @property
    def output_dir(self) -> Path:
        return self.project_root / "outputs"

    @property
    def ffmpeg_available(self) -> bool:
        configured = Path(self.ffmpeg_bin)
        return configured.exists() if configured.is_absolute() else shutil.which(self.ffmpeg_bin) is not None


settings = Settings()
