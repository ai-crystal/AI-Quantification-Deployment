# -*- coding: utf-8 -*-
"""第 3 章插图：垂直融合、水平融合，以及被旁路消费者挡住的断点。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("engine")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      line, save)

fig, ax = canvas(7.4, 3.6, 100)

BH = 7.0

# ---------------------------------------------------------------- 垂直融合
label(ax, 2.0, 33.6, "垂直融合", fs=8.2, bold=True, ha="left", color=INK)

names = ["输入", "卷积", "批归一化", "激活", "输出"]
cols = [(GRAY_L, GRAY), (GREEN_L, GREEN), (GREEN_L, GREEN),
        (RED_L, RED), (GRAY_L, GRAY)]
xs = [2.0, 18.0, 36.0, 54.0, 72.0]
BW = 13.0
Y1 = 24.0

for i, (n, (fc, ec)) in enumerate(zip(names, cols)):
    box(ax, xs[i], Y1, BW, BH, n, fc=fc, ec=ec, fs=7.8, bold=True, radius=1.0)
    if i:
        arrow(ax, (xs[i - 1] + BW, Y1 + BH / 2), (xs[i] - 0.35, Y1 + BH / 2), lw=0.9)

label(ax, 30.0, Y1 - 2.6, "代数等价，可以合", fs=7.4, color=GREEN)
label(ax, 52.0, Y1 - 2.6, "断点", fs=7.4, color=RED)

ax.plot([50.6, 50.6], [Y1 - 0.6, Y1 + BH + 0.6], color=RED, lw=0.9, ls=(0, (3, 2)))

# 旁路消费者
box(ax, 36.0, 37.0, 18.0, 6.0, "旁路消费者", fc=WHITE, ec=RED, fs=7.4,
    color=RED, radius=0.9, lw=0.9)
arrow(ax, (42.5, Y1 + BH + 0.2), (42.5, 36.7), color=RED, lw=0.9, ls=(0, (3, 2)))
label(ax, 56.0, 40.0, "这里多一个读者，中间张量就得落显存", fs=7.0, color=RED,
      ha="left")

# ---------------------------------------------------------------- 水平融合
label(ax, 2.0, 15.4, "水平融合", fs=8.2, bold=True, ha="left", color=INK)

box(ax, 2.0, 4.0, 13.0, 9.6, "同一份\n输入", fc=GRAY_L, ec=GRAY, fs=7.6, bold=True)
box(ax, 21.0, 9.0, 15.0, 5.4, "逐元素 A", fc=GREEN_L, ec=GREEN, fs=7.4)
box(ax, 21.0, 3.2, 15.0, 5.4, "逐元素 B", fc=GREEN_L, ec=GREEN, fs=7.4)
box(ax, 42.0, 4.0, 13.0, 9.6, "两份\n输出", fc=GRAY_L, ec=GRAY, fs=7.6, bold=True)

arrow(ax, (15.2, 9.6), (20.6, 11.7), lw=0.9)
arrow(ax, (15.2, 8.0), (20.6, 5.9), lw=0.9)
arrow(ax, (36.2, 11.7), (41.6, 9.6), lw=0.9)
arrow(ax, (36.2, 5.9), (41.6, 8.0), lw=0.9)

label(ax, 60.0, 9.0, "同输入、同形状\n一次遍历读完，写两份结果", fs=7.2, color=GRAY,
      ha="left")

label(ax, 50, 0.8, "青绿边框表示可以合成同一个 kernel，红色表示融合必须在这里停下",
      fs=7.0, color=GRAY)
save(fig, "03/fig03_1.png")
