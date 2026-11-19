# -*- coding: utf-8 -*-
"""第 5 章插图：校准区间的三种取法。"""

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

import numpy as np

from figstyle import (ACCENT, ACCENT_L, GRAY, RED, RED_L, WARM, WARM_L, WHITE,
                      arrow, box, canvas, label, line, save)

rng = np.random.default_rng(7)
main = rng.normal(0.0, 0.62, 24000)
tail = 1.6 + rng.exponential(1.9, 300)
tail = tail[tail < 8.0]
data = np.concatenate([main, tail])

XLO, XHI = -3.0, 8.0
YMAX = 26.0

fig, ax = canvas(7.4, 2.9, 100)
X0, X1 = 12.0, 92.0
Y0 = 7.0


def px(v):
    return X0 + (v - XLO) / (XHI - XLO) * (X1 - X0)


counts, edges = np.histogram(data, bins=44, range=(XLO, XHI))
cmax = counts.max()
bw = (X1 - X0) / 44 * 0.86

for i, c in enumerate(counts):
    if c == 0:
        continue
    h = np.log10(c + 1.0) / np.log10(cmax + 1.0) * YMAX
    x = px(edges[i]) + (X1 - X0) / 44 * 0.07
    fc = WARM_L if edges[i] >= 2.6 else ACCENT_L
    ec = WARM if edges[i] >= 2.6 else ACCENT
    box(ax, x, Y0, bw, h, fc=fc, ec=ec, lw=0.6, radius=0.25)

line(ax, (X0, Y0), (X1, Y0), color="#1b1b1b", lw=0.9)
for v, t in ((-3, "-3"), (-1, "-1"), (0, "0"), (1, "1"), (2, "2"), (4, "4"), (6, "6"), (8, "8")):
    line(ax, (px(v), Y0), (px(v), Y0 - 0.9), color="#1b1b1b", lw=0.8)
    label(ax, px(v), Y0 - 2.6, "%d" % v, fs=7.4)

# 三条候选区间
for v, col, txt, ty in ((8.0, RED, "min-max", 33.0),
                        (2.6, WARM, "99.9% 分位", 36.4)):
    line(ax, (px(v), Y0), (px(v), ty - 1.2), color=col, lw=1.0, ls=(0, (4, 3)))
    label(ax, px(v) - 1.2, ty, txt, fs=7.4, color=col, ha="right")

label(ax, px(5.0), Y0 + 16.0, "暖色部分被 99.9% 分位截断", fs=7.2, color=WARM, ha="center")


label(ax, X0, 2.0, "同一份激活分布，横轴为取值，纵轴为样本数（对数）；暖色柱子是被 99.9% 分位截掉的部分",
      fs=7.0, color=GRAY, ha="left")
save(fig, "05/fig05_1.png")
