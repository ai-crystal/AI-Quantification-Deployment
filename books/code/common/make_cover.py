# -*- coding: utf-8 -*-
"""生成系列封面与封底。

用法：
    python make_cover.py intro
    python make_cover.py all

封面版式固定：系列名、书名、分册名、副标题、作者。各册靠背景图与强调色区分。
背景图从 E:/Study/0-logo 读取，铺满后居中裁切，再压一层深色渐变，保证文字可读。
"""

import json
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
LOGO_DIR = r"E:\Study\0-logo"
W, H = 1240, 1754
FONT_BOLD = r"C:\Windows\Fonts\msyhbd.ttc"
FONT_REG = r"C:\Windows\Fonts\msyh.ttc"

SERIES_EN = "LANDING"
SERIES_CN = "落地"
SERIES_SUB = "AI 推理部署与量化技术"

BOOKS = {
    "intro": {
        "no": "01", "volume": "第一册", "role": "入门",
        "bg": "logo2.png", "accent": (157, 184, 232),
        "blurb": "从一次前向开始，把算子、计算图、数值精度、注意力变体、投机解码、并行与线上服务串成一张地图。不写公式，也不要求 CUDA 经验。",
    },
    "compute": {
        "no": "02", "volume": "第二册", "role": "算力",
        "bg": "logo3.png", "accent": (111, 195, 232),
        "blurb": "从 SM、寄存器与显存层次讲到 GEMM、卷积和 FlashAttention，用 roofline 与 Nsight 判断瓶颈究竟在哪一层。",
    },
    "precision": {
        "no": "03", "volume": "第三册", "role": "精度",
        "bg": "logo6.png", "accent": (195, 168, 224),
        "blurb": "浮点、定点、校准、PTQ 与 QAT，再到 GPTQ、AWQ、剪枝与低秩分解，把精度与速度的交换算清楚。",
    },
    "engine": {
        "no": "04", "volume": "第四册", "role": "引擎",
        "bg": "logo1.png", "accent": (232, 185, 120),
        "blurb": "计算图、融合规则、TensorRT 与 torch.compile，直到批处理、KV cache 管理与线上推理服务。",
    },
}


def cover_crop(im):
    im = im.convert("RGB")
    scale = max(W / float(im.width), H / float(im.height))
    nw, nh = int(im.width * scale + 0.5), int(im.height * scale + 0.5)
    im = im.resize((nw, nh), Image.LANCZOS)
    left = (nw - W) // 2
    top = (nh - H) // 2
    return im.crop((left, top, left + W, top + H))


def shade(im, top_a=150, bottom_a=232):
    """自上而下压深，底部再重一些，文字压得住。"""
    veil = Image.new("RGBA", (W, H))
    d = ImageDraw.Draw(veil)
    for y in range(H):
        t = y / float(H - 1)
        a = int(top_a + (bottom_a - top_a) * (t ** 0.85))
        d.line([(0, y), (W, y)], fill=(6, 10, 18, a))
    return Image.alpha_composite(im.convert("RGBA"), veil)


def spaced(d, xy, text, font, fill, gap=8):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill)
        x += d.textlength(ch, font=font) + gap


def wrap(d, text, font, width):
    lines, cur = [], ""
    for ch in text:
        if d.textlength(cur + ch, font=font) > width:
            lines.append(cur)
            cur = ch
        else:
            cur += ch
    if cur:
        lines.append(cur)

    # 避头尾：标点不能出现在行首，左括号不能留在行尾
    no_start = "，。、；：！？）】》」』”’"
    no_end = "（【《「『“‘"
    for i in range(1, len(lines)):
        while lines[i] and lines[i][0] in no_start:
            lines[i - 1] += lines[i][0]
            lines[i] = lines[i][1:]
    for i in range(len(lines) - 1):
        while lines[i] and lines[i][-1] in no_end:
            lines[i + 1] = lines[i][-1] + lines[i + 1]
            lines[i] = lines[i][:-1]
    return [x for x in lines if x]


def make_front(key):
    cfg = BOOKS[key]
    book = json.load(open(os.path.join(ROOT, "books", key, "book.json"), encoding="utf-8"))
    bg = cover_crop(Image.open(os.path.join(LOGO_DIR, cfg["bg"])))
    im = shade(bg)
    d = ImageDraw.Draw(im)

    accent = cfg["accent"]
    ink = (240, 244, 248)
    soft = (204, 214, 224)

    f_series = ImageFont.truetype(FONT_REG, 30)
    f_title = ImageFont.truetype(FONT_BOLD, 188)
    f_sub = ImageFont.truetype(FONT_REG, 52)
    f_vol = ImageFont.truetype(FONT_BOLD, 40)
    f_role = ImageFont.truetype(FONT_REG, 36)
    f_small = ImageFont.truetype(FONT_REG, 28)
    f_no = ImageFont.truetype(FONT_BOLD, 120)

    spaced(d, (108, 126), SERIES_EN, f_series, accent, gap=10)
    d.text((108, 176), SERIES_SUB, font=f_small, fill=soft)

    d.text((100, 360), book["title"], font=f_title, fill=ink)

    d.line([(112, 620), (112 + 196, 620)], fill=accent, width=3)
    d.text((108, 660), "%s　%s" % (cfg["volume"], cfg["role"]), font=f_vol, fill=accent)
    d.text((108, 760), book["subtitle"], font=f_sub, fill=soft)

    # 右下角大号册号，压得很淡
    d.text((W - 300, H - 470), cfg["no"], font=f_no,
           fill=(accent[0], accent[1], accent[2]))

    d.text((108, H - 220), "Dr. Dezeming", font=f_vol, fill=ink)
    d.text((108, H - 158), "2026", font=f_small, fill=soft)
    d.text((W - 300, H - 158), SERIES_CN, font=f_vol, fill=accent)

    out = os.path.join(ROOT, "books", key, "images", "cover.jpg")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    im.convert("RGB").save(out, "JPEG", quality=90, optimize=True)
    print("cover:", out)


def make_back(key):
    cfg = BOOKS[key]
    bg = cover_crop(Image.open(os.path.join(LOGO_DIR, cfg["bg"])))
    bg = bg.filter(ImageFilter.GaussianBlur(2.4))
    im = shade(bg, top_a=196, bottom_a=220)
    d = ImageDraw.Draw(im)
    accent = cfg["accent"]
    ink = (238, 243, 247)
    soft = (198, 208, 218)

    f_series = ImageFont.truetype(FONT_REG, 30)
    f_body = ImageFont.truetype(FONT_REG, 34)
    f_small = ImageFont.truetype(FONT_REG, 26)
    f_vol = ImageFont.truetype(FONT_BOLD, 36)

    spaced(d, (108, 126), SERIES_EN, f_series, accent, gap=10)
    d.text((108, 178), SERIES_SUB, font=f_small, fill=soft)

    d.line([(112, 300), (112 + 120, 300)], fill=accent, width=2)
    y = 380
    for line in wrap(d, cfg["blurb"], f_body, W - 240):
        d.text((108, y), line, font=f_body, fill=ink)
        y += 62

    d.text((108, H - 240), "%s　%s" % (SERIES_CN, cfg["role"]), font=f_vol, fill=accent)
    d.text((108, H - 180), "Dr. Dezeming　2026", font=f_small, fill=soft)

    out = os.path.join(ROOT, "books", key, "images", "backcover.jpg")
    im.convert("RGB").save(out, "JPEG", quality=90, optimize=True)
    print("backcover:", out)


def main():
    keys = list(BOOKS) if len(sys.argv) < 2 or sys.argv[1] == "all" else [sys.argv[1]]
    for key in keys:
        make_front(key)
        make_back(key)


if __name__ == "__main__":
    main()
