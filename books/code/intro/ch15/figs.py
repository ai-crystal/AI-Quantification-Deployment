# -*- coding: utf-8 -*-
"""第 15 章插图：低秩分解与蒸馏。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, Rectangle, arrow, box, canvas,
                      label, line, save)

# ---------------------------------------------------------------- 图 15-1
fig, ax = canvas(7.2, 2.6, 100)

def grid(x, y, rows, cols, w, h, fc=ACCENT_L, ec=ACCENT):
    for r in range(rows):
        for c in range(cols):
            ax.add_patch(Rectangle((x + c * w, y + (rows - 1 - r) * h), w, h,
                                   facecolor=fc, edgecolor=ec, lw=0.5, zorder=3))

grid(4.0, 12.0, 6, 6, 3.0, 2.6)
label(ax, 13.0, 28.2, "W：6×6", fs=7.4)
label(ax, 13.0, 8.6, "36 个参数", fs=6.4, color=GRAY)

arrow(ax, (23.0, 20.0), (30.0, 20.0), lw=0.9)
label(ax, 26.5, 21.8, "分解", fs=6.6, color=GRAY)

grid(32.0, 14.0, 6, 2, 3.4, 2.2)
label(ax, 35.4, 29.6, "A：6×2", fs=7.0)
grid(46.0, 14.0, 2, 6, 2.8, 2.4)
label(ax, 54.4, 29.6, "B：2×6", fs=7.0)

label(ax, 44.0, 10.2, "6×2 + 2×6 = 24 < 36", fs=6.2, color=GRAY)
label(ax, 44.0, 6.4, "秩 r 越小，参数越少；r 太小，误差变大", fs=6.8, color=GRAY)
save(fig, "15/fig15_1.png")

# ---------------------------------------------------------------- 图 15-2
fig, ax = canvas(7.2, 2.5, 100)

box(ax, 2.0, 14.0, 18.0, 12.0, "教师模型\n（大）", fc=WARM_L, ec=WARM, fs=7.6, bold=True)
box(ax, 27.0, 14.0, 18.0, 12.0, "软标签\n概率分布", fc=GRAY_L, ec=GRAY, fs=7.2)
box(ax, 52.0, 14.0, 18.0, 12.0, "学生模型\n（小）", fc=ACCENT_L, ec=ACCENT, fs=7.6, bold=True)
box(ax, 77.0, 14.0, 18.0, 12.0, "损失\nKL + CE", fc=GREEN_L, ec=GREEN, fs=7.0)

arrow(ax, (20.4, 20.0), (26.6, 20.0), lw=0.9)
arrow(ax, (45.4, 20.0), (51.6, 20.0), lw=0.9)
arrow(ax, (70.4, 20.0), (76.6, 20.0), lw=0.9)

# 分布小柱
for i, h in enumerate([6.0, 4.0, 2.0, 1.2]):
    ax.add_patch(Rectangle((29.0 + i * 3.6, 15.2), 2.6, h,
                           facecolor=WARM, edgecolor=WARM, alpha=0.8, zorder=4))
label(ax, 36.0, 12.0, "类别之间的相对关系", fs=6.2, color=GRAY)

label(ax, 50, 6.4, "教师不直接给答案，而是给“每个答案有多像”；学生学的是分布", fs=7.0, color=GRAY)
save(fig, "15/fig15_2.png")
