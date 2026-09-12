"""Render the animated base video for the NVIDIA PAIR / home AI cluster Short.

The renderer intentionally produces original graphics: a local-network map with
moving request packets, changing states, kinetic caption entrances and a closing
brand card. Run it with Pillow installed; final encoding is handled by FFmpeg.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable
import math
import random

from PIL import Image, ImageDraw, ImageFilter, ImageFont


WIDTH, HEIGHT, FPS, DURATION = 720, 1280, 15, 35
ROOT = Path(__file__).resolve().parents[1]
FRAMES = ROOT / "build" / "pair-reel-frames"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_BLACK = "/System/Library/Fonts/Supplemental/Arial Black.ttf"
FONT_REGULAR = "/System/Library/Fonts/Supplemental/Arial.ttf"
MINT = "#58f0b1"
INK = "#08141d"
TEXT = "#f5fffb"


def typeface(size: int, *, black: bool = False, regular: bool = False) -> ImageFont.FreeTypeFont:
    path = FONT_REGULAR if regular else (FONT_BLACK if black else FONT_BOLD)
    return ImageFont.truetype(path, size)


def clamp(value: float, low: float = 0, high: float = 1) -> float:
    return max(low, min(high, value))


def ease_out(value: float) -> float:
    return 1 - (1 - clamp(value)) ** 3


def wrap(draw: ImageDraw.ImageDraw, value: str, font: ImageFont.FreeTypeFont, width: int) -> list[str]:
    words, lines, active = value.split(), [], ""
    for word in words:
        candidate = (active + " " + word).strip()
        if draw.textbbox((0, 0), candidate, font=font)[2] <= width:
            active = candidate
        else:
            lines.append(active)
            active = word
    if active:
        lines.append(active)
    return lines


def text_block(
    draw: ImageDraw.ImageDraw,
    value: str,
    x: int,
    y: float,
    width: int,
    font: ImageFont.FreeTypeFont,
    *,
    fill: str = TEXT,
    gap: int = 8,
    align: str = "left",
) -> float:
    lines = wrap(draw, value, font, width)
    line_height = draw.textbbox((0, 0), "Ag", font=font)[3] + gap
    for number, line in enumerate(lines):
        box = draw.textbbox((0, 0), line, font=font)
        offset = x if align == "left" else x + (width - box[2]) // 2
        draw.text((offset, int(y + number * line_height)), line, font=font, fill=fill)
    return y + len(lines) * line_height


def gradient(frame_number: int) -> Image.Image:
    palette = [
        ((5, 15, 24), (10, 35, 48)),
        ((7, 17, 32), (20, 31, 65)),
        ((8, 20, 28), (11, 47, 52)),
        ((18, 12, 40), (11, 31, 50)),
    ]
    top, bottom = palette[(frame_number // (FPS * 5)) % len(palette)]
    image = Image.new("RGB", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(image)
    for y in range(HEIGHT):
        mix = y / (HEIGHT - 1)
        colour = tuple(int(top[i] * (1 - mix) + bottom[i] * mix) for i in range(3))
        draw.line((0, y, WIDTH, y), fill=colour)
    return image


def draw_grid(draw: ImageDraw.ImageDraw, now: float) -> None:
    offset = int((now * 48) % 56)
    for x in range(-56, WIDTH + 56, 56):
        draw.line((x + offset, 0, x + offset - 90, HEIGHT), fill=(91, 240, 180, 18), width=1)
    for y in range(140, HEIGHT, 72):
        draw.line((0, y, WIDTH, y), fill=(91, 240, 180, 14), width=1)


def pill(draw: ImageDraw.ImageDraw, text: str, x: int = 46, y: int = 58) -> None:
    font = typeface(19)
    box = draw.textbbox((0, 0), text, font=font)
    width = box[2] + 32
    draw.rounded_rectangle((x, y, x + width, y + 40), radius=20, fill=(88, 240, 177, 255))
    draw.text((x + 16, y + 8), text, font=font, fill=INK)


def animated_title(draw: ImageDraw.ImageDraw, headline: str, subhead: str, local: float) -> None:
    enter = ease_out(local / 0.45)
    y = 164 + (1 - enter) * 42
    pill(draw, "AI × ENGINEERING")
    text_block(draw, headline, 46, y, 625, typeface(57, black=True), gap=0)
    text_block(draw, subhead, 49, y + 245, 600, typeface(25, regular=True), fill="#d8f5e7", gap=7)


def machine(draw: ImageDraw.ImageDraw, x: float, y: float, label: str, state: str, active: bool) -> tuple[float, float]:
    glow = (88, 240, 177, 100 if active else 36)
    draw.ellipse((x - 55, y - 55, x + 55, y + 55), fill=glow)
    draw.rounded_rectangle((x - 85, y - 56, x + 85, y + 66), radius=22, fill=(10, 33, 46, 248), outline=(88, 240, 177, 210 if active else 95), width=3)
    draw.rounded_rectangle((x - 45, y - 27, x + 45, y + 17), radius=7, fill=(27, 76, 86, 255))
    for row in range(3):
        draw.rectangle((x - 29, y + 31 + row * 9, x + 29, y + 35 + row * 9), fill=(88, 240, 177, 140 if active else 55))
    text_block(draw, label, int(x - 92), y + 82, 184, typeface(20, black=True), fill=TEXT, gap=0, align="center")
    text_block(draw, state, int(x - 98), y + 111, 196, typeface(16, regular=True), fill=MINT if active else "#93b1b4", gap=0, align="center")
    return x, y


def connection(draw: ImageDraw.ImageDraw, start: tuple[float, float], end: tuple[float, float], now: float, phase: float, colour: tuple[int, int, int] = (88, 240, 177)) -> None:
    draw.line((*start, *end), fill=(*colour, 90), width=4)
    draw.line((*start, *end), fill=(*colour, 205), width=1)
    progress = (now * 0.65 + phase) % 1
    x = start[0] + (end[0] - start[0]) * progress
    y = start[1] + (end[1] - start[1]) * progress
    draw.ellipse((x - 12, y - 12, x + 12, y + 12), fill=(*colour, 70))
    draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill=(*colour, 255))


def task_chip(draw: ImageDraw.ImageDraw, x: float, y: float, text: str, active: bool) -> None:
    fill = (88, 240, 177, 255) if active else (21, 55, 68, 245)
    fg = INK if active else TEXT
    draw.rounded_rectangle((x - 74, y - 22, x + 74, y + 22), radius=22, fill=fill, outline=(88, 240, 177, 180), width=2)
    text_block(draw, text, int(x - 70), y - 9, 140, typeface(16, black=True), fill=fg, gap=0, align="center")


def network_map(draw: ImageDraw.ImageDraw, now: float, local: float, mode: str) -> None:
    agent = (360.0, 555.0)
    left = (170.0, 830.0)
    right = (550.0, 830.0)
    lower = (360.0, 1040.0)
    draw.ellipse((agent[0] - 108, agent[1] - 108, agent[0] + 108, agent[1] + 108), fill=(88, 240, 177, 48))
    draw.ellipse((agent[0] - 76, agent[1] - 76, agent[0] + 76, agent[1] + 76), fill=(9, 44, 53, 255), outline=(88, 240, 177, 255), width=4)
    text_block(draw, "AI", 280, 520, 160, typeface(42, black=True), fill=MINT, gap=0, align="center")
    text_block(draw, "AGENT", 280, 571, 160, typeface(17, black=True), fill=TEXT, gap=0, align="center")

    nodes = [(left, "PC A", "BUSY", mode != "routing"), (right, "PC B", "READY", True), (lower, "PC C", "READY", mode == "parallel")]
    for number, (point, label, state, active) in enumerate(nodes):
        connection(draw, agent, point, now, number / 3)
        machine(draw, *point, label, state, active)

    if mode == "tasks":
        for number, task in enumerate(["RESEARCH", "CODE", "TEST"]):
            task_chip(draw, 155 + number * 205, 685, task, int(now * 1.6 + number) % 2 == 0)
    if mode == "routing":
        task_chip(draw, 360, 700, "GPU BUSY  →  ROUTE TO PC B", True)
    if mode == "parallel":
        task_chip(draw, 360, 700, "3 JOBS • 3 MACHINES", True)


def full_caption(draw: ImageDraw.ImageDraw, main: str, supporting: str, local: float) -> None:
    scale = 1 + 0.025 * math.sin(local * 6)
    size = int(58 * scale)
    text_block(draw, main, 55, 415, 610, typeface(size, black=True), fill=TEXT, gap=0, align="center")
    text_block(draw, supporting, 72, 680, 575, typeface(27, regular=True), fill="#c9eee0", gap=8, align="center")


def footer(draw: ImageDraw.ImageDraw, frame_number: int) -> None:
    progress = frame_number / (FPS * DURATION)
    draw.rounded_rectangle((46, 1210, 674, 1218), radius=4, fill=(255, 255, 255, 33))
    draw.rounded_rectangle((46, 1210, 46 + int(628 * progress), 1218), radius=4, fill=(88, 240, 177, 255))


def render_frame(frame_number: int) -> Image.Image:
    now = frame_number / FPS
    scene = min(int(now / 3.15), 10)
    local = now - scene * 3.15
    image = gradient(frame_number)
    draw = ImageDraw.Draw(image, "RGBA")
    draw_grid(draw, now)

    if scene == 0:
        animated_title(draw, "YOUR HOME HAS AN AI CLUSTER", "Not one computer. A local network of AI compute.", local)
        network_map(draw, now, local, "tasks")
    elif scene == 1:
        animated_title(draw, "ONE GPU IS A BOTTLENECK", "Your idle PCs could be part of the answer.", local)
        network_map(draw, now, local, "routing")
    elif scene == 2:
        animated_title(draw, "MEET: NVIDIA PAIR", "A Personal AI Router for your local network.", local)
        network_map(draw, now, local, "parallel")
    elif scene == 3:
        animated_title(draw, "IT ROUTES INFERENCE", "Independent requests can move to a PC with capacity.", local)
        network_map(draw, now, local, "routing")
    elif scene == 4:
        animated_title(draw, "THE AGENT SPLITS THE WORK", "Research. Code. Test. Each becomes a separate job.", local)
        network_map(draw, now, local, "tasks")
    elif scene == 5:
        animated_title(draw, "THEN THE NETWORK MOVES IT", "Less waiting on one GPU. More local parallel work.", local)
        network_map(draw, now, local, "parallel")
    elif scene == 6:
        pill(draw, "COMPUTER ENGINEERING")
        full_caption(draw, "AI SKILLS ARE BECOMING SYSTEM SKILLS", "The model is only one piece of the machine.", local)
        network_map(draw, now, local, "routing")
    elif scene == 7:
        pill(draw, "WHAT TO LEARN")
        items = ["VRAM", "LOCAL NETWORKS", "SCHEDULING", "PRIVACY"]
        for number, item in enumerate(items):
            y = 390 + number * 145
            beat = (now * 2 + number * 0.5) % 1
            draw.rounded_rectangle((63, y, 657, y + 105), radius=26, fill=(15, 52, 62, 245), outline=(88, 240, 177, int(110 + beat * 115)), width=2)
            draw.ellipse((92, y + 27, 142, y + 77), fill=(88, 240, 177, 255))
            draw.text((108, y + 37), str(number + 1), font=typeface(18, black=True), fill=INK)
            draw.text((171, y + 29), item, font=typeface(33, black=True), fill=TEXT)
    elif scene == 8:
        pill(draw, "THE TAKEAWAY")
        full_caption(draw, "NOT JUST BIGGER MODELS", "Small AI systems that cooperate may matter just as much.", local)
        network_map(draw, now, local, "parallel")
    elif scene == 9:
        pill(draw, "AI × ENGINEERING")
        full_caption(draw, "THE FUTURE RUNS CLOSER TO YOU", "And increasingly, across the devices around you.", local)
        network_map(draw, now, local, "parallel")
    else:
        draw.rounded_rectangle((48, 350, 672, 930), radius=46, fill=(11, 44, 53, 248), outline=(88, 240, 177, 240), width=3)
        pill(draw, "AI × ENGINEERING", 182, 430)
        text_block(draw, "Follow", 80, 555, 560, typeface(52, black=True), fill=TEXT, gap=0, align="center")
        text_block(draw, "@anant.explores", 72, 635, 580, typeface(50, black=True), fill=MINT, gap=0, align="center")
        text_block(draw, "on Instagram & YouTube", 82, 790, 556, typeface(29, regular=True), fill="#e2f1ea", gap=0, align="center")
        for number in range(8):
            angle = now * 1.8 + number * math.pi / 4
            x, y = 360 + math.cos(angle) * 230, 650 + math.sin(angle) * 165
            draw.ellipse((x - 6, y - 6, x + 6, y + 6), fill=(88, 240, 177, 190))

    footer(draw, frame_number)
    return image.convert("RGB")


def build() -> None:
    FRAMES.mkdir(parents=True, exist_ok=True)
    random.seed(7)
    for frame_number in range(FPS * DURATION):
        render_frame(frame_number).save(FRAMES / f"frame-{frame_number:04d}.jpg", quality=88, optimize=True)
        if frame_number % FPS == 0:
            print(f"rendered {frame_number // FPS:02d}/{DURATION}s")


if __name__ == "__main__":
    build()
