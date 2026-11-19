# -*- coding: utf-8 -*-
"""第 13 章插图：分组量化与 outlier 迁移。"""

import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, Rectangle, arrow, box, canvas,
                      label, line, save)

# ---------------------------------------------------------------- 图 13-1
fig, ax = canvas(7.2, 2.4, 100)

label(ax, 3.0, 31.0, "权重按 128 个一组切开，每组一个 fp16 scale", fs=7.6, ha="left", color=GRAY)

for g in range(4):
    gx = 3.0 + g * 24.0
    for i in range(8):
        ax.add_patch(Rectangle((gx + i * 2.7, 18.0), 2.2, 4.4,
                               facecolor=ACCENT_L, edgecolor=ACCENT, lw=0.5, zorder=3))
    label(ax, gx + 10.6, 24.8, "第 %d 组" % (g + 1), fs=6.2, color=GRAY)
    box(ax, gx + 3.4, 11.0, 12.0, 4.2, "scale %d" % (g + 1), fc=WARM_L, ec=WARM, fs=6.0)
    line(ax, (gx + 9.4, 18.0), (gx + 9.4, 15.4), color=WARM, lw=0.7)

label(ax, 50, 6.2, "方格为示意，每格代表 16 个权重；组内共用 scale，组间独立", fs=7.0, color=GRAY)
save(fig, "13/fig13_1.png")

# ---------------------------------------------------------------- 图 13-2
fig, ax = canvas(7.2, 2.9, 100)

# 左：原始
label(ax, 3.0, 34.0, "原始", fs=8.0, ha="left", bold=True, color=GRAY)
label(ax, 3.0, 28.0, "激活", fs=6.8, ha="left", color=GRAY)
vals = [0.8, 0.7, 1.0, 0.9, 8.0, 0.75, 0.85, 0.9]
for i, v in enumerate(vals):
    h = v / 8.0 * 10.0
    ax.add_patch(Rectangle((10.0 + i * 3.2, 26.0), 2.4, h,
                           facecolor=WARM_L if v < 2 else RED_L,
                           edgecolor=WARM if v < 2 else RED, lw=0.5, zorder=3))
label(ax, 27.0, 37.0, "一个 outlier", fs=6.2, color=RED)
label(ax, 3.0, 21.0, "权重", fs=6.8, ha="left", color=GRAY)
line(ax, (10.0, 19.0), (35.0, 19.0), color=GRAY, lw=0.7)
for i, v in enumerate([0.5, 0.6, 0.4, 0.55, 0.5, 0.45, 0.6, 0.5]):
    h = v * 8.0
    ax.add_patch(Rectangle((10.0 + i * 3.2, 19.0), 2.4, h,
                           facecolor=ACCENT_L, edgecolor=ACCENT, lw=0.5, zorder=3))

# 右：SmoothQuant
label(ax, 54.0, 34.0, "SmoothQuant 之后", fs=8.0, ha="left", bold=True, color=GRAY)
label(ax, 54.0, 28.0, "激活", fs=6.8, ha="left", color=GRAY)
vals2 = [0.55, 0.6, 0.7, 0.65, 0.8, 0.6, 0.7, 0.65]
for i, v in enumerate(vals2):
    h = v / 8.0 * 10.0
    ax.add_patch(Rectangle((61.0 + i * 3.2, 26.0), 2.4, h,
                           facecolor=GREEN_L, edgecolor=GREEN, lw=0.5, zorder=3))
label(ax, 54.0, 21.0, "权重", fs=6.8, ha="left", color=GRAY)
line(ax, (61.0, 19.0), (86.0, 19.0), color=GRAY, lw=0.7)
for i, v in enumerate([1.1, 1.3, 0.9, 1.2, 1.0, 1.05, 1.25, 1.1]):
    h = v / 2.0 * 9.0
    ax.add_patch(Rectangle((61.0 + i * 3.2, 19.0), 2.4, h,
                           facecolor=ACCENT_L, edgecolor=ACCENT, lw=0.5, zorder=3))

arrow(ax, (38.0, 24.0), (52.0, 24.0), color=GRAY, lw=0.9)
label(ax, 45.0, 25.6, "按通道缩放", fs=6.4, color=GRAY)
label(ax, 45.0, 20.6, "激活 ÷ s，权重 × s", fs=6.4, color=ACCENT)
label(ax, 50, 7.0, "数学上等价，数值上把激活的极端值挪到权重，让两边都好量化", fs=7.0, color=GRAY)
save(fig, "13/fig13_2.png")
