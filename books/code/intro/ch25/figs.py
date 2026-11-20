# -*- coding: utf-8 -*-
"""第 25 章插图：推理与 Agent 请求的生命周期。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      line, save)

fig, ax = canvas(7.2, 2.8, 100)

nodes = [
    (2.0, "请求", GRAY, GRAY_L),
    (20.0, "推理 token", ACCENT, ACCENT_L),
    (40.0, "工具调用", WARM, WARM_L),
    (60.0, "观察结果", GRAY, GRAY_L),
    (80.0, "最终答案", GREEN, GREEN_L),
]
for x, name, ec, fc in nodes:
    box(ax, x, 21.0, 15.0, 9.0, name, fc=fc, ec=ec, fs=7.2, bold=True)
    if x < 80:
        arrow(ax, (x + 15.4, 25.5), (x + 17.6, 25.5), lw=0.8)

# 循环回推理
line(ax, (67.5, 20.8), (67.5, 14.0), color=GRAY, lw=0.8, ls=(0, (3, 2)))
line(ax, (67.5, 14.0), (27.5, 14.0), color=GRAY, lw=0.8, ls=(0, (3, 2)))
arrow(ax, (27.5, 14.0), (27.5, 20.6), color=GRAY, lw=0.8)
label(ax, 47.5, 12.0, "多轮：工具结果回到模型，继续推理或再调工具", fs=6.4, color=GRAY)

label(ax, 50, 5.0, "推理 token 也要 decode、占 KV cache；工具等待期间 GPU 可能空闲", fs=7.0, color=GRAY)
save(fig, "25/fig25_1.png")
