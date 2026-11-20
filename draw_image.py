#!/usr/bin/env python3
"""Draw the entry image for make.fun news-image-20261120.

A newspaper-style front page summing up the world news of Friday
20 November 2026, drawn with Pillow. Output: entry.png, 1024x1024.
All stories are as reported on 20 November 2026 (see SOURCES in README).
Run: python3 draw_image.py
"""
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (26, 26, 26)
NAVY = (22, 35, 63)
GOLD = (201, 162, 39)
RED = (179, 39, 30)
GRAY = (74, 74, 74)
PANEL = (255, 255, 255)
BORDER = (216, 210, 196)
DARKGOLD = (138, 109, 27)


def font(name, size):
    return ImageFont.truetype(
        os.path.join("/usr/share/fonts/truetype", name), size
    )


F_TITLE = font("dejavu/DejaVuSerif-Bold.ttf", 58)
F_DATE = font("dejavu/DejaVuSans-Bold.ttf", 30)
F_TAG = font("dejavu/DejaVuSans-Bold.ttf", 20)
F_HEAD = font("dejavu/DejaVuSans-Bold.ttf", 40)
F_HEAD2 = font("dejavu/DejaVuSans-Bold.ttf", 26)
F_SUB = font("dejavu/DejaVuSans.ttf", 24)
F_SUB2 = font("dejavu/DejaVuSans.ttf", 21)
F_STRIP = font("dejavu/DejaVuSans-Bold.ttf", 19)
F_FOOT = font("dejavu/DejaVuSans.ttf", 16)


def wrap(draw, text, fnt, max_w):
    """Wrap text to fit max_w pixels; return list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def centered(draw, y, text, fnt, fill, x0=0, x1=W):
    w = draw.textlength(text, font=fnt)
    draw.text(((x0 + x1 - w) / 2, y), text, font=fnt, fill=fill)


def star(draw, cx, cy, r_out, r_in, points, fill):
    import math

    pts = []
    for i in range(points * 2):
        r = r_out if i % 2 == 0 else r_in
        a = math.pi * i / points - math.pi / 2
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    draw.polygon(pts, fill=fill)


def icon_scales(draw, cx, cy):
    c = DARKGOLD
    draw.line([(cx, cy - 56), (cx, cy + 56)], fill=c, width=5)
    draw.line([(cx - 54, cy - 42), (cx + 54, cy - 42)], fill=c, width=5)
    draw.ellipse([cx - 7, cy - 66, cx + 7, cy - 52], fill=c)
    for sx in (cx - 54, cx + 54):
        draw.line([(sx, cy - 42), (sx - 20, cy - 6)], fill=c, width=4)
        draw.line([(sx, cy - 42), (sx + 20, cy - 6)], fill=c, width=4)
        draw.arc([sx - 20, cy - 22, sx + 20, cy + 10], 0, 180, fill=c, width=4)


def icon_flags(draw, x, y):
    # Three small flags on poles: China, USA, Russia (compact, top-right).
    def pole(px):
        draw.line([(px, y), (px, y + 44)], fill=INK, width=3)

    def flag(px, fy, colors):
        for i, col in enumerate(colors):
            draw.rectangle(
                [px + 2, fy + i * 6, px + 30, fy + (i + 1) * 6], fill=col
            )

    pole(x)
    draw.rectangle([x + 2, y, x + 30, y + 18], fill=(222, 41, 16))
    draw.ellipse([x + 6, y + 4, x + 11, y + 9], fill=(255, 222, 0))
    pole(x + 38)
    flag(x + 38, y, [(178, 34, 52), (255, 255, 255), (178, 34, 52)])
    draw.rectangle([x + 40, y, x + 52, y + 9], fill=(60, 59, 110))
    pole(x + 76)
    flag(x + 76, y, [(255, 255, 255), (0, 57, 166), (213, 0, 50)])


def icon_chart(draw, x, y):
    draw.line([(x, y + 48), (x + 100, y + 48)], fill=INK, width=4)
    draw.line([(x, y), (x, y + 48)], fill=INK, width=4)
    pts = [(x + 6, y + 13), (x + 30, y + 21), (x + 52, y + 10),
           (x + 74, y + 33), (x + 94, y + 42)]
    draw.line(pts, fill=RED, width=5, joint="curve")
    draw.polygon([(x + 94, y + 42), (x + 84, y + 37), (x + 86, y + 48)],
                 fill=RED)


def icon_tower(draw, cx, y):
    draw.rectangle([cx - 18, y, cx + 18, y + 72], fill=(52, 73, 94))
    for row in range(3):
        for col in range(3):
            wx = cx - 12 + col * 10
            wy = y + 10 + row * 18
            draw.rectangle([wx, wy, wx + 6, wy + 8], fill=(232, 197, 71))
    star(draw, cx, y - 4, 20, 8, 8, (230, 126, 34))


def icon_blast(draw, cx, cy):
    star(draw, cx, cy, 34, 13, 12, (230, 126, 34))
    star(draw, cx, cy, 20, 8, 8, (179, 39, 30))
    draw.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=(247, 243, 234))


def icon_leaf(draw, cx, cy):
    draw.ellipse([cx - 32, cy - 32, cx + 32, cy + 32], fill=(39, 174, 96))
    draw.pieslice([cx - 18, cy - 23, cx + 18, cy + 23], 200, 340,
                  fill=(255, 255, 255))
    draw.pieslice([cx - 18, cy - 23, cx + 18, cy + 23], 20, 160,
                  fill=(255, 255, 255))


def icon_cross(draw, cx, cy):
    draw.ellipse([cx - 32, cy - 32, cx + 32, cy + 32], fill=(39, 174, 96))
    draw.rectangle([cx - 7, cy - 20, cx + 7, cy + 20], fill=(255, 255, 255))
    draw.rectangle([cx - 20, cy - 7, cx + 20, cy + 7], fill=(255, 255, 255))


def panel(draw, x0, y0, x1, y1, tag, head, sub, icon):
    draw.rectangle([x0, y0, x1, y1], fill=PANEL, outline=BORDER, width=2)
    draw.rectangle([x0, y0, x0 + 8, y1], fill=RED)
    draw.text((x0 + 24, y0 + 14), tag, font=F_TAG, fill=RED)
    if icon == "flags":
        icon_flags(draw, x1 - 132, y0 + 12)
    elif icon == "chart":
        icon_chart(draw, x1 - 124, y0 + 14)
    elif icon == "tower":
        icon_tower(draw, x1 - 62, y0 + 28)
    elif icon == "blast":
        icon_blast(draw, x1 - 62, y0 + 44)
    tx = x0 + 24
    tw = x1 - tx - 24
    # Headlines stay clear of the top-right icon; subs run full width.
    lines = wrap(draw, head, F_HEAD2, tw - 132)
    ly = y0 + 48
    for ln in lines:
        draw.text((tx, ly), ln, font=F_HEAD2, fill=INK)
        ly += 33
    for ln in wrap(draw, sub, F_SUB2, tw):
        draw.text((tx, ly + 4), ln, font=F_SUB2, fill=GRAY)
        ly += 28


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Masthead
    d.rectangle([0, 0, W, 150], fill=NAVY)
    centered(d, 26, "THE WORLD TODAY", F_TITLE, (255, 255, 255))
    centered(d, 100, "FRIDAY  ·  20 NOVEMBER 2026", F_DATE, (232, 197, 71))
    d.rectangle([0, 150, W, 156], fill=GOLD)

    # Lead story: ICJ genocide ruling
    x0, y0, x1, y1 = 28, 170, 996, 434
    d.rectangle([x0, y0, x1, y1], fill=PANEL, outline=BORDER, width=2)
    d.rectangle([x0, y0, x0 + 10, y1], fill=RED)
    icon_scales(d, 118, y0 + 132)
    tx = 210
    d.text((tx, y0 + 18), "JUSTICE  ·  THE HAGUE", font=F_TAG, fill=RED)
    head = "WORLD COURT: MYANMAR COMMITTED GENOCIDE"
    lines = wrap(d, head, F_HEAD, x1 - tx - 24)
    ly = y0 + 52
    for ln in lines:
        d.text((tx, ly), ln, font=F_HEAD, fill=INK)
        ly += 50
    subs = wrap(d, "Against the Rohingya — the first such ruling "
                   "against a state, in The Hague.", F_SUB, x1 - tx - 24)
    for ln in subs:
        d.text((tx, ly + 6), ln, font=F_SUB, fill=GRAY)
        ly += 32

    # Row 2
    panel(d, 28, 446, 502, 670, "POLITICS  ·  SHENZHEN",
          "TRUMP, XI & PUTIN MEET IN SHENZHEN",
          "First three-way summit — joint peace declaration signed.",
          "flags")
    panel(d, 522, 446, 996, 670, "ECONOMY  ·  NEW YORK",
          "ANTHROPIC +17% ON DEBUT AS STOCKS SLIDE",
          "S&P 500 −2%, fifth straight fall · Nikkei −4.8%.", "chart")

    # Row 3
    panel(d, 28, 684, 502, 908, "CONFLICT  ·  RIYADH",
          "HOUTHI MISSILE HITS RIYADH TOWER",
          "Windows blown out across eight floors of the PIF tower.",
          "tower")
    panel(d, 522, 684, 996, 908, "CONFLICT  ·  KYIV",
          "RUSSIAN STRIKES HIT KYIV — 8 KILLED",
          "Bridges targeted; Austrian and Dutch embassies damaged.",
          "blast")

    # Bottom strip: two small stories
    y0, y1 = 922, 992
    d.rectangle([28, y0, 996, y1], fill=PANEL, outline=BORDER, width=2)
    d.line([(512, y0 + 10), (512, y1 - 10)], fill=BORDER, width=2)
    icon_leaf(d, 72, (y0 + y1) // 2)
    d.text((118, y0 + 10), "CLIMATE · ANTALYA", font=F_TAG, fill=RED)
    d.text((118, y0 + 36), "COP31 draft drops phase-out call",
           font=F_STRIP, fill=INK)
    icon_cross(d, 566, (y0 + y1) // 2)
    d.text((618, y0 + 10), "HEALTH · KENYA", font=F_TAG, fill=RED)
    d.text((618, y0 + 36), "Last Ebola patient goes home",
           font=F_STRIP, fill=INK)

    # Footer
    centered(d, 1000, "Headlines as reported on 20 November 2026",
             F_FOOT, GRAY)

    img.save(OUT, "PNG")
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
