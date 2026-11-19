# -*- coding: utf-8 -*-
"""第 11 章插图：常见数值格式的位布局。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, Rectangle, canvas, label,
                      line, save)

fig, ax = canvas(7.2, 3.3, 100)

rows = [
    ("fp32", 1, 8, 23),
    ("tf32", 1, 8, 10),
    ("bf16", 1, 8, 7),
    ("fp16", 1, 5, 10),
    ("fp8 e4m3", 1, 4, 3),
    ("fp8 e5m2", 1, 5, 2),
    ("int8", 0, 0, 8),
]

unit = 2.15
x0 = 20.0
y = 38.0
for name, s, e, m in rows:
    label(ax, 18.0, y + 1.6, name, fs=7.4, ha="right")
    x = x0
    if s:
        ax.add_patch(Rectangle((x, y), unit * s, 3.2, facecolor=GRAY_L,
                               edgecolor=GRAY, lw=0.6, zorder=3))
        label(ax, x + unit * s / 2, y + 1.6, "S", fs=5.6, color=GRAY)
        x += unit * s
    if e:
        ax.add_patch(Rectangle((x, y), unit * e, 3.2, facecolor=ACCENT_L,
                               edgecolor=ACCENT, lw=0.6, zorder=3))
        label(ax, x + unit * e / 2, y + 1.6, "E%d" % e, fs=5.8, color=ACCENT)
        x += unit * e
    if m:
        ax.add_patch(Rectangle((x, y), unit * m, 3.2, facecolor=WARM_L,
                               edgecolor=WARM, lw=0.6, zorder=3))
        label(ax, x + unit * m / 2, y + 1.6, "M%d" % m, fs=5.8, color=WARM)
        x += unit * m
    total = s + e + m
    label(ax, x + 1.4, y + 1.6, "%d 位" % total, fs=6.0, ha="left", color=GRAY)
    y -= 5.0

label(ax, 20.0, 42.0, "S 符号　　E 指数（决定范围）　　M 尾数（决定精度）", fs=7.0, ha="left", color=GRAY)
label(ax, 20.0, 2.0, "int8 没有指数，只有 256 个格点，靠 scale 映射到浮点区间", fs=7.2, color=GRAY)
save(fig, "11/fig11_1.png")
