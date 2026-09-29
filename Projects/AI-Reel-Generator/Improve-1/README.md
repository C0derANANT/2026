# 🎬 AI Reel Generator

A complete, local-first Gradio app for turning a topic into a vertical social Reel. It prioritises zero subscription cost: local Ollama models for writing and analysis, local Coqui TTS and Whisper when installed, FFmpeg for rendering, and optional free Pexels/Unsplash APIs for professional images.

The app is deliberately honest about what is available. It runs without keys or heavyweight models by using original local storyboard art, a macOS voice fallback, estimated subtitles, and a locally generated royalty-free ambient bed. Add the optional providers for the full pipeline.

## Included features

- 2–3 sentence hook-first scripts from **Ollama + Mistral**, with a local template fallback.
- Local **Llama 2** analytics: viral score, suggested IST posting time, ten hashtags, and engagement improvements, with deterministic offline fallback.
- Five-to-seven visual frames from **Pexels**, **Unsplash**, a local **Automatic1111/SDXL** API, or original local storyboard graphics.
- **Coqui TTS** voiceover, with macOS `say` only as a local fallback when Coqui is unavailable.
- Locally synthesised royalty-free background audio. Point `MUSIC_LIBRARY_DIR` at your own properly licensed Pixabay Music or YouTube Audio Library downloads and the app loops, fades and mixes those tracks automatically.
- **Whisper** transcription into styled burned-in subtitles, with explicitly labelled timed-script fallback.
- FFmpeg rendering at **1080 × 1920, 24 FPS, target 7.5 Mbps**, including Ken Burns motion and fade transitions.
- Script editing and rerendering, five-item batch processing, saved local history/search/load/delete, individual downloads, and a ZIP bundle per Reel.

## Quick start

Use Python **3.10 or 3.11** for the full Coqui/Whisper stack. The interface itself works on newer Python versions, but ML packages often lag behind the newest Python release.

```bash
cd AI-Reel-Generator
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-local-ai.txt
cp .env.example .env
```

Install the system tools:

```bash
# macOS
brew install ffmpeg ollama

# Linux (Debian/Ubuntu)
sudo apt-get install ffmpeg
```

Start Ollama and pull the two free local models:

```bash
ollama serve
ollama pull mistral
ollama pull llama2
```

In a separate terminal, launch the app:

```bash
python main.py
```

It opens at `http://127.0.0.1:7860`. Use `python main.py --check` to see what is configured before generating.

## Optional free image providers

Create free developer keys, then put them in `.env`:

```env
PEXELS_API_KEY=...
UNSPLASH_API_KEY=...
```

Without a key, **Local storyboard art** is the default and no image leaves the computer. If you already run Automatic1111/Stable Diffusion locally, set `AUTOMATIC1111_URL` and choose **Stable Diffusion (local)** in the app.

Pexels and Unsplash accounts are free but their published API terms and rate limits still apply. The Ollama, Coqui, Whisper, FFmpeg, local SD, local storyboard, history, batch and renderer paths do not use a paid API.

## Local storage and privacy

- Generated items live in `outputs/<timestamp>-<topic>/`.
- Saved history is local SQLite data in `data/reels.sqlite3`.
- `.env`, generated media, audio, subtitle files, history, and ZIPs are ignored by Git.
- No paid APIs are used. Pexels/Unsplash are optional free third-party APIs and only receive the visual search topic when selected/configured.

## Notes on quality claims

Quality depends on the hardware, models, prompt, source visuals, and edit choices. This app provides a strong hackathon-ready local workflow but does not promise a fixed percentage score, virality, or a particular social-platform outcome. Always review factual claims, licensing, and the final video before posting.
