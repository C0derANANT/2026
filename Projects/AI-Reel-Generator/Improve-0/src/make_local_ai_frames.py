"""Create the static base frames for the first @anant.explores AI Short.

The final editing stage should add motion, captions, voiceover, and a music bed.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math
import random

W, H = 720, 1280
OUT = Path("build/local-ai-frames")
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_BLACK = "/System/Library/Fonts/Supplemental/Arial Black.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"


def font(size, black=False, regular=False):
    return ImageFont.truetype(FONT_REG if regular else (FONT_BLACK if black else FONT_BOLD), size)


def wrap(draw, text, active_font, width):
    words, lines, line = text.split(), [], ""
    for word in words:
        trial = (line + " " + word).strip()
        if draw.textbbox((0, 0), trial, font=active_font)[2] <= width:
            line = trial
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def text_block(draw, text, x, y, width, active_font, fill="white", gap=8, align="left"):
    lines = wrap(draw, text, active_font, width)
    line_h = draw.textbbox((0, 0), "Ag", font=active_font)[3] + gap
    for number, line in enumerate(lines):
        box = draw.textbbox((0, 0), line, font=active_font)
        dx = x if align == "left" else x + (width - (box[2] - box[0])) // 2
        draw.text((dx, y + number * line_h), line, font=active_font, fill=fill)
    return y + len(lines) * line_h


def canvas(seed):
    random.seed(seed)
    image = Image.new("RGB", (W, H), "#07131d")
    pixels = image.load()
    for y in range(H):
        mix = y / H
        red = int(7 * (1 - mix) + 18 * mix)
        green = int(19 * (1 - mix) + 31 * mix)
        blue = int(29 * (1 - mix) + 48 * mix)
        for x in range(W):
            shade = int(7 * math.sin((x / W + y / H) * 4.2))
            pixels[x, y] = (max(0, red + shade), max(0, green + shade), max(0, blue + shade))
    draw = ImageDraw.Draw(image, "RGBA")
    for _ in range(30):
        x, y = random.randint(-50, W + 20), random.randint(0, H)
        draw.line((x, y, min(W, x + random.randint(40, 150)), min(H, y + random.randint(30, 100))), fill=(52, 211, 153, 38), width=1)
        draw.ellipse((x - 4, y - 4, x + 4, y + 4), fill=(52, 211, 153, 65))
    return image, draw


def pill(draw, x, y, text):
    active_font = font(20)
    box = draw.textbbox((0, 0), text, font=active_font)
    width = box[2] - box[0] + 34
    draw.rounded_rectangle((x, y, x + width, y + 42), radius=21, fill=(52, 211, 153, 255))
    draw.text((x + 17, y + 9), text, font=active_font, fill="#07131d")


def title(draw, value, sub=None):
    pill(draw, 52, 70, "AI × ENGINEERING")
    text_block(draw, value, 52, 170, 620, font(60, black=True), gap=0)
    if sub:
        text_block(draw, sub, 52, 435, 600, font(28, regular=True), fill="#d8e6ef", gap=7)


def save(image, number):
    OUT.mkdir(parents=True, exist_ok=True)
    image.save(OUT / f"scene-{number:02}.png", optimize=True)


def build():
    image, draw = canvas(1)
    title(draw, "AI IS LEAVING THE CLOUD", "The next big AI change is not another chatbot.")
    draw.rounded_rectangle((52, 770, 668, 1050), radius=36, fill=(12, 35, 49, 240), outline=(52, 211, 153, 190), width=2)
    draw.text((90, 830), "The shift?", font=font(28), fill="#72f1bd")
    text_block(draw, "Where AI runs.", 90, 890, 530, font(47, black=True), gap=0)
    save(image, 1)

    image, draw = canvas(2)
    title(draw, "FROM DATA CENTRES TO YOUR DESK")
    draw.rounded_rectangle((88, 545, 632, 925), radius=30, fill=(8, 19, 29, 255), outline=(52, 211, 153, 230), width=3)
    draw.rounded_rectangle((140, 603, 580, 820), radius=16, fill=(17, 50, 64, 255))
    for index in range(5):
        draw.rounded_rectangle((175, 646 + index * 30, 505 - index * 32, 659 + index * 30), radius=6, fill=(52, 211, 153, 85))
    draw.polygon(((68, 930), (652, 930), (618, 978), (102, 978)), fill=(31, 60, 76, 255))
    text_block(draw, "Local agents can be faster and more private.", 78, 1060, 570, font(32), fill="#e7f5ef", gap=8, align="center")
    save(image, 2)

    image, draw = canvas(3)
    title(draw, "WHY LOCAL AI MATTERS")
    benefits = [("FASTER", "Less cloud round-trip"), ("PRIVATE", "Sensitive work stays closer"), ("CONNECTED", "Agents can use your local setup")]
    for index, (heading, description) in enumerate(benefits):
        y = 510 + index * 190
        draw.rounded_rectangle((52, y, 668, y + 145), radius=28, fill=(15, 38, 55, 245), outline=(52, 211, 153, 120), width=2)
        draw.text((84, y + 28), heading, font=font(30, black=True), fill="#72f1bd")
        draw.text((84, y + 76), description, font=font(25, regular=True), fill="#edf7f2")
    save(image, 3)

    image, draw = canvas(4)
    title(draw, "FOR ENGINEERS, THIS CHANGES THE SKILL SET")
    draw.rounded_rectangle((52, 575, 668, 1060), radius=34, fill=(11, 29, 42, 245))
    text_block(draw, "Don’t only learn prompts.", 92, 650, 530, font(45, black=True), fill="#ffffff", gap=2, align="center")
    text_block(draw, "Learn how systems behave when intelligence runs closer to the hardware.", 96, 810, 525, font(27, regular=True), fill="#cce6dc", gap=8, align="center")
    save(image, 4)

    image, draw = canvas(5)
    title(draw, "WHAT TO LEARN NEXT")
    for index, item in enumerate(["Local models", "GPU basics", "Optimisation", "Security + verification"]):
        y = 500 + index * 145
        draw.ellipse((54, y, 104, y + 50), fill=(52, 211, 153, 255))
        draw.text((69, y + 6), str(index + 1), font=font(22, black=True), fill="#07131d")
        draw.text((134, y + 5), item, font=font(39), fill="white")
    text_block(draw, "The edge is building reliable AI systems — not just using the newest model.", 66, 1125, 585, font(25, regular=True), fill="#bee7d5", gap=6, align="center")
    save(image, 5)

    image, draw = canvas(6)
    draw.rounded_rectangle((44, 360, 676, 940), radius=44, fill=(13, 38, 53, 250), outline=(52, 211, 153, 220), width=3)
    pill(draw, 187, 450, "AI × ENGINEERING")
    text_block(draw, "Follow", 80, 560, 560, font(50, black=True), gap=0, align="center")
    text_block(draw, "@anant.explores", 72, 635, 580, font(50, black=True), fill="#72f1bd", gap=0, align="center")
    text_block(draw, "on Instagram & YouTube", 80, 790, 560, font(29, regular=True), fill="#e2f1ea", gap=0, align="center")
    save(image, 6)


if __name__ == "__main__":
    build()
