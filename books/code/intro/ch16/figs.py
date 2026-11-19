# -*- coding: utf-8 -*-
"""第 16 章插图：静态/连续批处理，分页 KV cache。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, Rectangle, arrow, box, canvas,
                      label, line, save)

# ---------------------------------------------------------------- 图 16-1
fig, ax = canvas(7.2, 4.4, 100)

x0, cw = 20.0, 7.2

# 时间刻度
for t in range(9):
    label(ax, x0 + t * cw + cw / 2, 60.0, str(t), fs=5.6, color=GRAY)

label(ax, 2.0, 54.0, "静态批处理", fs=8.0, ha="left", bold=True, color=GRAY)
rows = [("A", 2), ("B", 3), ("C", 4), ("D", 4)]
for i, (name, end) in enumerate(rows):
    y = 47.0 - i * 4.2
    ax.add_patch(Rectangle((x0, y), (end + 1) * cw, 3.0,
                           facecolor=ACCENT_L, edgecolor=ACCENT, lw=0.6, zorder=3))
    label(ax, x0 + (end + 1) * cw / 2, y + 1.5, name, fs=5.8)
    if end < 4:
        ax.add_patch(Rectangle((x0 + (end + 1) * cw, y), (4 - end) * cw, 3.0,
                               facecolor=GRAY_L, edgecolor=GRAY, lw=0.6, zorder=3))
        label(ax, x0 + (end + 1 + (4 - end) / 2) * cw, y + 1.5, "占位", fs=5.2, color=GRAY)

for i in range(4):
    ax.add_patch(Rectangle((x0 + 5 * cw, 47.0 - i * 4.2), 4 * cw, 3.0,
                           facecolor=WHITE, edgecolor=GRAY, lw=0.6, zorder=2))
line(ax, (x0 + 5 * cw, 29.0), (x0 + 5 * cw, 53.5), color=GRAY, lw=0.8, ls=(0, (3, 2)))
label(ax, x0 + 5 * cw + 0.8, 53.0, "整批结束，下一批才能开始", fs=6.0, color=GRAY, ha="left")

label(ax, 2.0, 28.0, "连续批处理", fs=8.0, ha="left", bold=True, color=GRAY)
cont = [(0, 4, "A", ACCENT, 0), (5, 8, "G", ACCENT, 0), (0, 2, "B", GREEN, 1),
        (2, 5, "E", GREEN, 1), (6, 8, "H", GREEN, 1), (0, 6, "C", WARM, 2),
        (0, 3, "D", ACCENT, 3), (3, 7, "F", WARM, 3)]
for start, end, name, color, row in cont:
    y = 23.0 - row * 4.0
    ax.add_patch(Rectangle((x0 + start * cw, y), (end - start) * cw, 2.8,
                           facecolor=WHITE, edgecolor=color, lw=0.9, zorder=3))
    label(ax, x0 + (start + end) / 2 * cw, y + 1.4, name, fs=5.6, color=color)

label(ax, 50, 5.0, "每一步都可以让完成的请求离开、新到的请求进入，槽位不空等", fs=7.0, color=GRAY)
save(fig, "16/fig16_1.png")

# ---------------------------------------------------------------- 图 16-2
fig, ax = canvas(7.2, 2.7, 100)

label(ax, 2.0, 35.0, "请求 A 的逻辑 token", fs=7.2, ha="left", color=GRAY)
for i in range(12):
    ax.add_patch(Rectangle((2.0 + i * 4.2, 26.0), 3.8, 4.6,
                           facecolor=ACCENT_L, edgecolor=ACCENT, lw=0.6, zorder=3))
    label(ax, 3.9 + i * 4.2, 28.3, str(i), fs=6.4)

blocks = [(2.0, 10.0, "块 3", ACCENT_L, ACCENT), (19.0, 10.0, "块 7", ACCENT_L, ACCENT),
          (36.0, 10.0, "块 1", GREEN_L, GREEN), (53.0, 10.0, "块 5", WARM_L, WARM)]
for x, y, name, fc, ec in blocks:
    box(ax, x, y, 15.0, 8.0, name, fc=fc, ec=ec, fs=7.4)

for i in range(4):
    line(ax, (3.9 + i * 12.6, 25.8), (9.5 + i * 17.0, 18.4), color=GRAY, lw=0.6,
         ls=(0, (2, 2)))

label(ax, 70.0, 14.0, "物理块可以不连续，\n按需分配，写满再申请", fs=6.4, ha="left", color=GRAY)
save(fig, "16/fig16_2.png")
