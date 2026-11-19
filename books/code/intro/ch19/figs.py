# -*- coding: utf-8 -*-
"""第 19 章插图：优化循环。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      line, save)

fig, ax = canvas(7.2, 2.8, 100)

steps = ["基线", "分析", "假设", "改动", "复测"]
for i, s in enumerate(steps):
    x = 2.0 + i * 19.0
    box(ax, x, 20.0, 15.0, 8.0, s, fc=ACCENT_L if i < 4 else GREEN_L,
        ec=ACCENT if i < 4 else GREEN, fs=7.6, bold=True)
    if i < 4:
        arrow(ax, (x + 15.4, 24.0), (x + 18.6, 24.0), lw=0.9)

label(ax, 50, 33.0, "一次只改一个变量，否则不知道是谁的功劳", fs=7.4, color=GRAY)


arrow(ax, (90.0, 19.6), (90.0, 12.0), color=GRAY, lw=0.9)
line(ax, (90.0, 12.0), (29.0, 12.0), color=GRAY, lw=0.9)
arrow(ax, (29.0, 12.0), (29.0, 19.6), color=GRAY, lw=0.9)
label(ax, 60.0, 8.6, "没有达到目标：带着新数据回到分析", fs=6.8, color=GRAY)

label(ax, 90.0, 31.0, "达到目标：灰度上线", fs=6.8, color=GREEN, ha="center")
save(fig, "19/fig19_1.png")
