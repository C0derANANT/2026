from __future__ import annotations

import argparse
import json
from pathlib import Path

import gradio as gr
import requests

from reel_generator.config import settings
from reel_generator.pipeline import Analytics, ReelGenerator
from reel_generator.services import ServiceError


generator = ReelGenerator(settings)
APP_THEME = gr.themes.Soft(primary_hue="blue", secondary_hue="violet", neutral_hue="slate")
APP_CSS = """
.hero {text-align:center; padding: 22px 0 8px;} .hero h1 {font-size: 2.35rem; margin-bottom: 8px;}
.hero p {font-size: 1.05rem; color: #64748b;} #generate {min-height: 54px; font-size: 1.1rem;}
"""


def system_status() -> str:
    checks: list[str] = []
    try:
        reply = requests.get(f"{settings.ollama_url.rstrip('/')}/api/tags", timeout=1.5)
        models = [model.get("name", "") for model in reply.json().get("models", [])]
        checks.append(f"✅ Ollama is running · {', '.join(models) or 'no models pulled yet'}")
    except (requests.RequestException, ValueError):
        checks.append("⚠️ Ollama is not running. Start it with `ollama serve`, then run `ollama pull mistral` and `ollama pull llama2`.")
    checks.append("✅ FFmpeg detected" if settings.ffmpeg_available else "⚠️ FFmpeg is missing. Install it with `brew install ffmpeg`.")
    checks.append("✅ Pexels key loaded" if settings.pexels_api_key else "ℹ️ No Pexels key: the app will use original local storyboard art.")
    checks.append("✅ Unsplash key loaded" if settings.unsplash_api_key else "ℹ️ No Unsplash key: optional free provider is not configured.")
    return "\n\n".join(checks)


def analytics_markdown(analytics: Analytics) -> str:
    tags = " ".join(analytics.hashtags)
    tips = "\n".join(f"- {tip}" for tip in analytics.tips)
    return (
        f"### Viral score: **{analytics.viral_score}/10**\n\n"
        f"**Best posting time:** {analytics.best_posting_time}\n\n"
        f"**Top hashtags:**\n\n{tags}\n\n"
        f"**Make it stronger:**\n\n{tips}\n\n"
        f"_Analysis source: {analytics.source}_"
    )


def info_markdown(result) -> str:
    notes = "\n".join(f"- {note}" for note in result.notes)
    return (
        f"### Ready to post\n\n"
        f"**{result.duration:.1f} seconds · 1080 × 1920 · 24 FPS · target 7.5 Mbps**\n\n"
        f"**Production record**\n\n{notes}\n\n"
        f"Saved locally as `{result.reel_id}`."
    )


def records_table(query: str = "") -> list[list[str]]:
    rows = generator.history.list(query)
    return [[row["reel_id"], row["created_at"].replace("T", " ")[:19], row["topic"], row["style"], f"{row['duration']:.1f}s"] for row in rows]


def selector_update(query: str = ""):
    records = generator.history.list(query)
    choices = [(f"{record['created_at'][:16].replace('T', ' ')} · {record['topic']}", record["reel_id"]) for record in records]
    return gr.Dropdown(choices=choices, value=choices[0][1] if choices else None)


def finish_generation(result, statuses: list[str]):
    return (
        "### Production progress\n\n" + "\n".join(statuses + ["✅ Done · Reel saved locally"]),
        result.script,
        [str(image) for image in result.images],
        str(result.video),
        str(result.video),
        str(result.script_file),
        str(result.bundle),
        info_markdown(result),
        analytics_markdown(result.analytics),
        records_table(),
        selector_update(),
    )


def generate_ui(topic, style, genre, volume, subtitles, image_source, progress=gr.Progress()):
    statuses: list[str] = []

    def report(percent: int, message: str) -> None:
        progress(percent / 100, desc=message)
        statuses.append(f"✅ {message.replace(' · ', ': ')}")

    try:
        result = generator.generate(topic, style, genre, int(volume), subtitles, image_source, progress=report)
        return finish_generation(result, statuses)
    except ServiceError as error:
        raise gr.Error(str(error))
    except Exception as error:  # Surface a friendly UI failure while retaining a useful message.
        raise gr.Error(f"Generation stopped: {error}")


def render_edited_ui(topic, edited_script, style, genre, volume, subtitles, image_source, progress=gr.Progress()):
    if not edited_script or len(edited_script.split()) < 8:
        raise gr.Error("Write at least one short sentence before rendering the edited script.")
    statuses: list[str] = []

    def report(percent: int, message: str) -> None:
        progress(percent / 100, desc=message)
        statuses.append(f"✅ {message.replace(' · ', ': ')}")

    try:
        result = generator.generate(topic, style, genre, int(volume), subtitles, image_source, progress=report, script_override=edited_script)
        return finish_generation(result, statuses)
    except ServiceError as error:
        raise gr.Error(str(error))
    except Exception as error:
        raise gr.Error(f"Rendering stopped: {error}")


def regenerate_script(topic: str, style: str):
    if not topic.strip():
        raise gr.Error("Enter a topic first.")
    result = generator.script_writer.create(topic, style)
    return result.text, f"✅ Script generated with {result.source}. Edit it below, then render when ready."


def batch_ui(topics: str, style, genre, volume, subtitles, image_source, progress=gr.Progress()):
    unique_topics = []
    for item in topics.splitlines():
        clean = item.strip(" -•\t")
        if clean and clean not in unique_topics:
            unique_topics.append(clean)
    if not unique_topics:
        raise gr.Error("Add one topic per line.")
    if len(unique_topics) > 5:
        raise gr.Error("Batch mode is deliberately limited to five Reels at a time.")
    results = []
    for index, topic in enumerate(unique_topics, 1):
        progress((index - 1) / len(unique_topics), desc=f"Batch {index}/{len(unique_topics)} · {topic}")
        result = generator.generate(topic, style, genre, int(volume), subtitles, image_source)
        results.append(result)
    progress(1, desc="Batch complete")
    summary = "\n".join(f"✅ {item.topic} → {item.video.name}" for item in results)
    return f"### Batch complete\n\n{summary}", records_table(), selector_update()


def refresh_history(query: str):
    return records_table(query), selector_update(query)


def load_saved(reel_id: str):
    if not reel_id:
        raise gr.Error("Choose a saved Reel first.")
    record = generator.history.get(reel_id)
    if not record:
        raise gr.Error("That saved Reel no longer exists.")
    analytics = Analytics(**json.loads(record["analytics_json"]))
    images = [path for path in json.loads(record["image_paths"]) if Path(path).exists()]
    video = record["video_path"] if Path(record["video_path"]).exists() else None
    bundle = record["bundle_path"] if Path(record["bundle_path"]).exists() else None
    return (
        record["script"], images, video, video, record["script_path"], bundle,
        f"### Saved Reel\n\n**{record['duration']:.1f} seconds · 1080 × 1920**\n\n" + "\n".join(f"- {item}" for item in json.loads(record["notes_json"])),
        analytics_markdown(analytics),
    )


def delete_saved(reel_id: str, query: str):
    if not reel_id:
        raise gr.Error("Choose a saved Reel first.")
    if not generator.history.delete(reel_id):
        raise gr.Error("That Reel was already removed.")
    return "✅ Saved Reel and its local output folder were deleted.", records_table(query), selector_update(query)


def build_app() -> gr.Blocks:
    with gr.Blocks(title="AI Reel Generator") as app:
        gr.HTML("<div class='hero'><h1>🎬 FREE AI REEL GENERATOR</h1><p>No subscriptions · Local-first models · 1080×1920 social video</p></div>")
        gr.Markdown(system_status())
        with gr.Tabs():
            with gr.Tab("Create Reel"):
                with gr.Row():
                    with gr.Column(scale=1):
                        topic = gr.Textbox(label="Topic", placeholder="e.g. Why on-device AI is changing laptops", lines=3)
                        style = gr.Dropdown(["Professional", "Trendy", "Funny", "Cinematic"], value="Trendy", label="Video Style")
                        genre = gr.Dropdown(["Pop", "Chill", "Hip-Hop", "Indie", "Upbeat"], value="Upbeat", label="Music Genre")
                        volume = gr.Slider(0, 100, value=35, step=1, label="Music Volume")
                        subtitles = gr.Checkbox(value=True, label="Include subtitles")
                        image_source = gr.Dropdown(["Auto", "Pexels", "Unsplash", "Stable Diffusion (local)", "Local storyboard art"], value="Auto", label="Visual source")
                        generate = gr.Button("Generate Reel", variant="primary", elem_id="generate")
                    with gr.Column(scale=1):
                        progress_box = gr.Markdown("### Production progress\n\nWaiting for a topic.")
                        gr.Markdown("**Free stack:** Ollama/Mistral → Pexels or local art → Coqui → FFmpeg → Whisper. Optional providers gracefully fall back to local assets.")
                script_box = gr.Textbox(label="Generated Script", lines=5, interactive=True, placeholder="Your generated narration appears here.")
                with gr.Row():
                    regenerate = gr.Button("Edit & Regenerate Script")
                    render_edited = gr.Button("Render Edited Script", variant="secondary")
                script_status = gr.Markdown()
                gallery = gr.Gallery(label="Storyboard images", columns=3, rows=2, height="auto")
                video = gr.Video(label="Generated Reel", height=620)
                with gr.Row():
                    reel_download = gr.File(label="Download Reel (MP4)")
                    script_download = gr.File(label="Download Script (TXT)")
                    bundle_download = gr.File(label="Download All (ZIP)")
                with gr.Row():
                    info = gr.Markdown()
                    analytics = gr.Markdown()
            with gr.Tab("Batch Processing"):
                batch_topics = gr.Textbox(label="Up to five topics (one per line)", lines=8, placeholder="First Reel topic\nSecond Reel topic")
                batch_button = gr.Button("Generate Batch", variant="primary")
                batch_status = gr.Markdown()
            with gr.Tab("Saved Reels"):
                search = gr.Textbox(label="Search by topic or date", placeholder="e.g. AI or 2026-09")
                refresh = gr.Button("Search / Refresh")
                history = gr.Dataframe(headers=["ID", "Created", "Topic", "Style", "Duration"], value=records_table(), interactive=False, wrap=True)
                saved = gr.Dropdown(label="Choose a saved Reel", choices=[])
                with gr.Row():
                    load = gr.Button("Load Selected")
                    delete = gr.Button("Delete Selected", variant="stop")
                saved_status = gr.Markdown()

        all_outputs = [progress_box, script_box, gallery, video, reel_download, script_download, bundle_download, info, analytics, history, saved]
        inputs = [topic, style, genre, volume, subtitles, image_source]
        generate.click(generate_ui, inputs=inputs, outputs=all_outputs)
        render_edited.click(render_edited_ui, inputs=[topic, script_box, style, genre, volume, subtitles, image_source], outputs=all_outputs)
        regenerate.click(regenerate_script, inputs=[topic, style], outputs=[script_box, script_status])
        batch_button.click(batch_ui, inputs=[batch_topics, style, genre, volume, subtitles, image_source], outputs=[batch_status, history, saved])
        refresh.click(refresh_history, inputs=[search], outputs=[history, saved])
        load.click(load_saved, inputs=[saved], outputs=[script_box, gallery, video, reel_download, script_download, bundle_download, info, analytics])
        delete.click(delete_saved, inputs=[saved, search], outputs=[saved_status, history, saved])
    return app


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Reel Generator")
    parser.add_argument("--check", action="store_true", help="Print local dependency status and exit")
    args = parser.parse_args()
    if args.check:
        print(system_status())
    else:
        build_app().queue(default_concurrency_limit=1).launch(
            server_name="127.0.0.1", server_port=7860, inbrowser=True, theme=APP_THEME, css=APP_CSS
        )
