# -*- coding: utf-8 -*-
"""第 27 章插图：从 fp16 到 fp4 的数值与缩放粒度。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, Rectangle, box, canvas, label,
                      line, save)

fig, ax = canvas(7.2, 3.0, 100)

rows = [
    ("fp16", 8, "每个数 16 位，无块缩放", GRAY, GRAY_L),
    ("fp8", 8, "每个数 8 位，per-tensor 缩放", ACCENT, ACCENT_L),
    ("MX", 4, "每 32 个数一块，共享 8 位指数", GREEN, GREEN_L),
    ("NVFP4", 4, "每 16 个数一块，fp8 缩放 + 全局 fp32", WARM, WARM_L),
]

for i, (name, n, note, ec, fc) in enumerate(rows):
    y = 34.0 - i * 7.4
    label(ax, 3.0, y + 2.0, name, fs=7.6, ha="left", bold=True, color=ec)
    for j in range(12):
        ax.add_patch(Rectangle((19.0 + j * 3.2, y), 2.6, 4.0,
                               facecolor=fc, edgecolor=ec, lw=0.5, zorder=3))
    if name == "MX":
        box(ax, 60.0, y - 0.4, 8.0, 4.8, "指数", fc=WHITE, ec=ec, fs=5.6)
        line(ax, (58.6, y + 2.0), (59.8, y + 2.0), color=ec, lw=0.6)
    elif name == "NVFP4":
        box(ax, 60.0, y - 0.4, 8.0, 4.8, "fp8", fc=WHITE, ec=ec, fs=5.6)
        line(ax, (58.6, y + 2.0), (59.8, y + 2.0), color=ec, lw=0.6)
    label(ax, 71.0, y + 2.0, note, fs=6.2, color=GRAY, ha="left")

label(ax, 50, 3.2, "位宽下降的同时，缩放粒度变细；硬件支持与精度损失一起变化", fs=7.0, color=GRAY)
save(fig, "27/fig27_1.png")
