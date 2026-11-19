# -*- coding: utf-8 -*-
"""第 1 章插图：浮点位布局与可表示范围。"""

import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("precision")

# 印刷时图会按版心缩到 0.83 倍，这里把字号整体放大，保证缩后仍可读
SCALE = 1.16
_orig_label = figstyle.label
_orig_box = figstyle.box


def _label(ax, x, y, text, fs=9.5, **kw):
    _orig_label(ax, x, y, text, fs=fs * SCALE, **kw)


def _box(ax, x, y, w, h, text="", fs=9.5, **kw):
    _orig_box(ax, x, y, w, h, text, fs=fs * SCALE, **kw)


figstyle.label = _label
figstyle.box = _box

from figstyle import (ACCENT, ACCENT_L, GRAY, GREEN, GREEN_L, WARM, WARM_L,
                      WHITE, box, canvas, label, line, save)

# ---------------------------------------------------------------- 图 1-1
# 每种格式：(名称, 指数位, 尾数位)，符号位固定 1 位。
FORMATS = [
    ("fp32", 8, 23),
    ("tf32", 8, 10),
    ("bf16", 8, 7),
    ("fp16", 5, 10),
    ("fp8 e4m3", 4, 3),
    ("fp8 e5m2", 5, 2),
]

fig, ax = canvas(7.4, 3.9, 100)
BW = 1.95            # 每个 bit 的宽度
X0 = 25.0            # 条形起点
Y0 = 7.6             # 最下面一行的下沿
STEP = 7.4
BH = 4.6

for i, (name, ne, nm) in enumerate(FORMATS):
    y = Y0 + (len(FORMATS) - 1 - i) * STEP
    label(ax, 1.2, y + BH / 2, name, fs=8.4, ha="left", bold=True)
    label(ax, 22.4, y + BH / 2, "%d 位" % (1 + ne + nm), fs=6.8, ha="right",
          color=GRAY)
    x = X0
    for nb, fc, ec, txt in ((1, WARM_L, WARM, "1"),
                            (ne, ACCENT_L, ACCENT, str(ne)),
                            (nm, GREEN_L, GREEN, str(nm))):
        w = nb * BW
        box(ax, x, y, w, BH, fc=fc, ec=ec, lw=0.9, radius=0.5)
        if nb == 1:
            label(ax, x + w / 2, y + BH / 2, txt, fs=5.8, color=ec)
        elif w >= 3.2:
            label(ax, x + w / 2, y + BH / 2, txt, fs=7.2, color=ec)
        x += w

# 图例
for tx, fc, ec, nm in ((X0, WARM_L, WARM, "符号位"),
                       (X0 + 14, ACCENT_L, ACCENT, "指数位"),
                       (X0 + 28, GREEN_L, GREEN, "尾数位")):
    box(ax, tx, 2.2, 2.2, 2.2, fc=fc, ec=ec, lw=0.9, radius=0.4)
    label(ax, tx + 3.2, 3.3, nm, fs=7.4, color=GRAY, ha="left")

label(ax, 64.0, 3.3, "每格宽度相同，一格代表一位", fs=7.4, color=GRAY, ha="left")
save(fig, "01/fig01_1.png")

# ---------------------------------------------------------------- 图 1-2
RANGE = [
    ("fp32", 1.18e-38, 3.40e38),
    ("tf32", 1.18e-38, 3.40e38),
    ("bf16", 1.18e-38, 3.39e38),
    ("fp16", 6.10e-5, 6.55e4),
    ("fp8 e4m3", 1.56e-2, 4.48e2),
    ("fp8 e5m2", 6.10e-5, 5.73e4),
]

LO, HI = -40.0, 40.0
XS, XE = 30.0, 88.0


def px(v):
    return XS + (math.log10(v) - LO) / (HI - LO) * (XE - XS)


fig, ax = canvas(7.4, 3.4, 100)

Y0 = 8.4
STEP = 5.9
BH = 2.5

for i, (name, lo, hi) in enumerate(RANGE):
    y = Y0 + (len(RANGE) - 1 - i) * STEP
    label(ax, 1.2, y + BH / 2, name, fs=8.2, ha="left", bold=True)
    label(ax, 28.4, y + BH / 2, "%.2e ~ %.2e" % (lo, hi), fs=6.4, ha="right",
          color=GRAY)
    a, b = px(lo), px(hi)
    box(ax, a, y, b - a, BH, fc=ACCENT_L, ec=ACCENT, lw=0.9, radius=0.5)

# 数量级刻度
line(ax, (XS, 5.8), (XE, 5.8), color=GRAY, lw=0.8)
for dec in (-38, -30, -20, -10, 0, 10, 20, 30, 38):
    x = px(10.0 ** dec)
    line(ax, (x, 5.8), (x, 5.0), color=GRAY, lw=0.8)
    if dec in (-38, -20, 0, 20, 38):
        label(ax, x, 3.2, "1e%d" % dec, fs=7.0, color=GRAY)

label(ax, 1.2, 1.2, "横轴为该数值的十进制数量级，条形两端分别是格式的最小正规数与最大正规数；e5m2 的范围接近 fp16，代价是尾数只剩两位",
      fs=7.0, color=GRAY, ha="left")
save(fig, "01/fig01_2.png")
