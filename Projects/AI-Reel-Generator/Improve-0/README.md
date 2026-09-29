# AI Reel Generator

Production source for short-form videos published on **@anant.explores**.

## Editorial focus

30–40 second vertical Shorts/Reels on emerging AI and computer-engineering trends. Every video should have a sharp hook, visual movement, captions, an appropriate AI voiceover, subtle background audio, and the outro:

> Follow @anant.explores on Instagram & YouTube

## Publishing order

1. Publish the final Reel to Instagram.
2. Publish the same vertical Short to YouTube.
3. Commit and push the source, script, caption, and production notes to this repository.

Generated videos, audio, preview images, caches, and credentials are deliberately excluded from Git.

## Project layout

```text
src/                    Reusable frame-generation code
content/YYYY-MM-DD-*/   Script, caption, sources, and production notes per post
```

## Local setup

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

`src/make_local_ai_frames.py` needs Pillow. Rendering the final video additionally requires an FFmpeg binary and an audio-generation step; those stay local because they are build tooling rather than project source.

## Today’s post

The first entry is in `content/2026-09-12-local-ai-edge/`:

- Topic: local AI agents on RTX PCs and the engineering skills they make more valuable.
- Published Short: https://youtube.com/shorts/_SjTcxuI4fA
