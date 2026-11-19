# -*- coding: utf-8 -*-
"""第 7 章插图：伪量化的阶梯与直通梯度。"""

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

from figstyle import (ACCENT, ACCENT_L, GRAY, GREEN, INK, RED, RED_L, WARM,
                      WARM_L, WHITE, arrow, box, canvas, label, line, save)

S = 0.5
R = 2.0
X0, X1 = 16.0, 90.0
VLO, VHI = -3.0, 3.0


def px(v):
    return X0 + (v - VLO) / (VHI - VLO) * (X1 - X0)


fig, ax = canvas(7.4, 3.0, 100)

# ---------------- 上：前向阶梯
YQ0, YQ1 = 18.0, 32.0
QLO, QHI = -2.6, 2.6


def py(v):
    return YQ0 + (v - QLO) / (QHI - QLO) * (YQ1 - YQ0)


box(ax, px(-R), YQ0 - 0.6, px(R) - px(-R), YQ1 - YQ0 + 1.2, fc=ACCENT_L,
    ec="none", radius=0.0, zorder=0)
line(ax, (X0, py(0)), (X1, py(0)), color=GRAY, lw=0.7, zorder=1)
line(ax, (px(0), YQ0 - 1.6), (px(0), YQ1 + 1.0), color=GRAY, lw=0.7, zorder=1)

pts = []
v = VLO
step = 0.02
while v <= VHI + 1e-9:
    q = max(min(round(v / S), int(R / S)), -int(R / S))
    pts.append((px(v), py(q * S)))
    v += step
ax.plot([p[0] for p in pts], [p[1] for p in pts], color=ACCENT, lw=1.2, zorder=3)

label(ax, X0 - 2.0, YQ1 + 1.2, "前向", fs=7.4, bold=True, color=ACCENT, ha="right")
label(ax, X1 - 1.0, py(1.55), "截断", fs=7.0, color=RED, ha="right")
label(ax, X1 - 1.0, py(-1.55), "截断", fs=7.0, color=RED, ha="right")
label(ax, px(0.62), py(-1.45), "档距 s", fs=7.0, color=ACCENT, ha="left")

# ---------------- 下：反向梯度
YG0, YG1 = 3.6, 13.0


def gy(g):
    return YG0 + g / 1.25 * (YG1 - YG0)


line(ax, (X0, YG0), (X1, YG0), color=INK, lw=0.8)
line(ax, (X0, gy(1.0)), (X1, gy(1.0)), color=GRAY, lw=0.6, ls=(0, (2, 3)))
label(ax, X0 - 2.0, gy(1.0), "1", fs=7.0, color=GRAY, ha="right")
label(ax, X0 - 2.0, YG0, "0", fs=7.0, color=GRAY, ha="right")
label(ax, X0 - 2.0, YG1 + 1.2, "反向", fs=7.4, bold=True, color=GREEN, ha="right")

line(ax, (px(-R), gy(1.0)), (px(R), gy(1.0)), color=GREEN, lw=1.4)
line(ax, (X0, YG0), (px(-R), YG0), color=GREEN, lw=1.4)
line(ax, (px(R), YG0), (X1, YG0), color=GREEN, lw=1.4)
for xv in (px(-R), px(R)):
    line(ax, (xv, YG0), (xv, gy(1.0)), color=GREEN, lw=1.2, ls=(0, (3, 2)))

label(ax, px(2.45), gy(0.34), "梯度为 0", fs=7.0, color=GREEN, ha="left")
label(ax, px(0.0), gy(0.45), "区间内梯度恒为 1", fs=7.0, color=GREEN)

for v, t in ((-2, "-2"), (0, "0"), (2, "2")):
    label(ax, px(v), YG0 - 1.8, t, fs=7.0, color="#1b1b1b")

label(ax, X0 - 2.2, 0.4, "横轴为浮点输入，浅蓝带是量化区间", fs=7.0, color=GRAY, ha="left")
save(fig, "07/fig07_1.png")
