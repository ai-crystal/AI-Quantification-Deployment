# -*- coding: utf-8 -*-
"""第 26 章插图：扩散模型推理与步数蒸馏。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      line, save)

fig, ax = canvas(7.2, 2.7, 100)

box(ax, 2.0, 15.0, 12.0, 9.0, "噪声", fc=GRAY_L, ec=GRAY, fs=7.0)
steps = ["去噪 1", "去噪 2", "…", "去噪 N"]
for i, name in enumerate(steps):
    x = 18.0 + i * 12.0
    box(ax, x, 15.0, 9.0, 9.0, name, fc=ACCENT_L, ec=ACCENT, fs=6.8)
    if i:
        arrow(ax, (x - 2.8, 19.5), (x - 0.4, 19.5), lw=0.7)
arrow(ax, (14.4, 19.5), (17.6, 19.5), lw=0.8)

box(ax, 69.0, 15.0, 12.0, 9.0, "VAE 解码", fc=WARM_L, ec=WARM, fs=6.6)
box(ax, 85.0, 15.0, 12.0, 9.0, "图像/视频", fc=GREEN_L, ec=GREEN, fs=6.6)
arrow(ax, (63.4, 19.5), (68.6, 19.5), lw=0.8)
arrow(ax, (81.4, 19.5), (84.6, 19.5), lw=0.8)

label(ax, 50, 8.4, "文本编码只跑一次，VAE 解码只跑一次；时间主要花在去噪循环", fs=7.0, color=GRAY)
label(ax, 50, 4.2, "步数蒸馏把 30 步压到 4 步甚至 1 步，代价是多样性下降", fs=7.0, color=GRAY)
save(fig, "26/fig26_1.png")
