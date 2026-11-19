# -*- coding: utf-8 -*-
"""第 6 章插图：融合前后的访存，以及融合的决策条件。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      line, save)

# ---------------------------------------------------------------- 图 6-1
fig, ax = canvas(7.2, 3.1, 100)

label(ax, 3.0, 34.0, "未融合", fs=8.4, ha="left", bold=True, color=GRAY)
ys, h = 24.0, 7.0
for i, (name, fc, ec) in enumerate([("卷积", ACCENT_L, ACCENT),
                                    ("归一化", ACCENT_L, ACCENT),
                                    ("ReLU", GREEN_L, GREEN)]):
    x = 4.0 + i * 21.0
    box(ax, x, ys, 13.0, h, name, fc=fc, ec=ec, fs=8.0)
    box(ax, x + 2.6, ys - 6.2, 7.8, 3.4, "显存", fc=GRAY_L, ec=GRAY, fs=6.2, color=GRAY)
    line(ax, (x + 6.5, ys), (x + 6.5, ys - 2.8), color=GRAY, lw=0.7)
    if i < 2:
        arrow(ax, (x + 13.4, ys + h / 2), (x + 20.6, ys + h / 2), lw=0.9)
        label(ax, x + 17.0, ys + h / 2 + 2.0, "读写", fs=6.2, color=WARM)

label(ax, 3.0, 12.0, "融合后", fs=8.4, ha="left", bold=True, color=GRAY)
box(ax, 4.0, 2.0, 55.0, h, "卷积 + 归一化 + ReLU", fc=ACCENT_L, ec=ACCENT, fs=8.2, bold=True)
box(ax, 6.6, -3.2, 7.8, 3.0, "显存", fc=GRAY_L, ec=GRAY, fs=6.2, color=GRAY)
line(ax, (10.5, 2.0), (10.5, -0.2), color=GRAY, lw=0.7)
label(ax, 63.0, 5.5, "中间结果留在寄存器，只写一次输出", fs=7.2, ha="left", color=GRAY)

label(ax, 50, -4.6, "箭头表示的是一次显存往返；融合把三次往返压成一次", fs=7.2, color=GRAY)
save(fig, "06/fig06_1.png")

# ---------------------------------------------------------------- 图 6-2
fig, ax = canvas(7.2, 2.7, 100)

qs = ["中间结果\n还有别的消费者？", "布局\n一致？", "精度\n一致？", "形状\n可推导？"]
xs = [2.0, 21.5, 41.0, 60.5]
for i, (x, q) in enumerate(zip(xs, qs)):
    box(ax, x, 12.0, 16.0, 10.0, q, fc=WHITE, ec=INK, fs=7.0)
    if i:
        arrow(ax, (xs[i - 1] + 16.4, 17.0), (x - 0.4, 17.0), lw=0.9)
        label(ax, xs[i - 1] + 18.4, 19.0, "是", fs=6.6, color=GREEN)

box(ax, 80.0, 12.0, 17.0, 10.0, "融合", fc=GREEN_L, ec=GREEN, fs=8.0, bold=True)
arrow(ax, (76.9, 17.0), (79.6, 17.0), lw=0.9)
label(ax, 78.2, 19.0, "是", fs=6.6, color=GREEN)

notes = ["否：保留中间张量\n或复制一份", "否：插入布局转换\n或放弃融合",
         "否：插入 cast\n可能退出快速通路", "否：走通用路径\n或按形状重编译"]
for x, note in zip(xs, notes):
    label(ax, x + 8.0, 6.0, note, fs=6.0, color=GRAY)

label(ax, 50, 1.4, "任何一步为“否”，融合都会退化；退化不一定报错，但收益会消失",
      fs=7.2, color=GRAY)
save(fig, "06/fig06_2.png")
