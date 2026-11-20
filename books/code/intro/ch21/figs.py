# -*- coding: utf-8 -*-
"""第 21 章插图：普通解码与投机解码的时间线。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      line, save)

fig, ax = canvas(7.2, 2.9, 100)

label(ax, 2.0, 38.0, "普通解码", fs=8.2, ha="left", bold=True, color=GRAY)
for i in range(4):
    x = 4.0 + i * 12.0
    box(ax, x, 27.0, 8.0, 6.0, "t%d" % (i + 1), fc=ACCENT_L, ec=ACCENT, fs=7.0)
    if i:
        arrow(ax, (x - 3.8, 30.0), (x - 0.4, 30.0), lw=0.8)
label(ax, 52.0, 24.6, "每个 token 一次完整前向，串行等待", fs=6.8, color=GRAY, ha="center")

label(ax, 2.0, 19.0, "投机解码", fs=8.2, ha="left", bold=True, color=GRAY)

# 草稿
label(ax, 4.0, 14.2, "草稿", fs=6.4, ha="left", color=WARM)
for i in range(4):
    x = 8.0 + i * 7.2
    box(ax, x, 11.0, 5.0, 4.2, "d%d" % (i + 1), fc=WARM_L, ec=WARM, fs=6.0)
    if i:
        arrow(ax, (x - 2.0, 13.1), (x - 0.4, 13.1), lw=0.7)
label(ax, 41.0, 15.4, "草稿模型连猜 4 个", fs=6.2, color=GRAY, ha="center")

# 验证
box(ax, 51.0, 8.0, 24.0, 9.0, "目标模型一次验证", fc=GREEN_L, ec=GREEN, fs=7.2, bold=True)
arrow(ax, (39.0, 13.0), (50.6, 13.0), lw=0.9)
label(ax, 63.0, 5.6, "接受 3 个，第 4 个重采样", fs=6.2, color=GREEN, ha="center")

# 下一轮
box(ax, 79.0, 8.0, 15.0, 9.0, "下一轮", fc=GRAY_L, ec=GRAY, fs=6.8)
arrow(ax, (75.4, 12.5), (78.6, 12.5), lw=0.8)

label(ax, 50, 2.2, "验证一次前向可以产出多个 token；接受率越高，加速越明显", fs=7.0, color=GRAY)
save(fig, "21/fig21_1.png")
