# -*- coding: utf-8 -*-
"""第 5 章插图：TensorRT 构建与运行两个阶段的流程。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("engine")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      save)

fig, ax = canvas(7.4, 3.3, 100)

# ---------------------------------------------------------------- 构建阶段
label(ax, 2.0, 42.6, "构建阶段（分钟级）", fs=8.2, bold=True, ha="left", color=WARM)

build = ["解析 ONNX", "网络定义", "图优化\n折叠 消除 融合", "逐层计时\n选 tactic",
         "序列化"]
bx = [2.0, 21.0, 38.0, 58.0, 79.0]
Bob = [(GRAY_L, GRAY), (ACCENT_L, ACCENT), (ACCENT_L, ACCENT),
       (WARM_L, WARM), (GREEN_L, GREEN)]
BW, BH, Y1 = 16.0, 9.6, 30.0

for i, (t, (fc, ec)) in enumerate(zip(build, Bob)):
    box(ax, bx[i], Y1, BW, BH, t, fc=fc, ec=ec, fs=7.6, radius=1.0)
    if i:
        arrow(ax, (bx[i - 1] + BW, Y1 + BH / 2), (bx[i] - 0.4, Y1 + BH / 2), lw=0.9)

label(ax, 22.0, Y1 - 2.8, "可能在这里失败", fs=7.4, color=GRAY)
label(ax, 66.0, Y1 - 2.8, "时间主要花在这里", fs=7.4, color=WARM)

# engine 文件
box(ax, 79.0, 12.0, 16.0, 8.0, "engine\n文件", fc=WHITE, ec=GREEN, fs=7.6,
    bold=True, radius=0.9)
arrow(ax, (87.0, Y1 - 0.3), (87.0, 20.3), color=GREEN, lw=0.9)
label(ax, 84.6, 26.6, "绑定硬件\n与版本", fs=7.4, color=GREEN,
      ha="right")

# ---------------------------------------------------------------- 运行阶段
label(ax, 2.0, 20.0, "运行阶段（毫秒级）", fs=8.2, bold=True, ha="left", color=GREEN)

run = ["反序列化", "绑地址、设形状", "enqueue"]
rx = [2.0, 22.0, 42.0]
for i, t in enumerate(run):
    box(ax, rx[i], 6.0, 17.0, 8.0, t, fc=ACCENT_L, ec=ACCENT, fs=7.6, radius=0.9)
    if i:
        arrow(ax, (rx[i - 1] + 17.0, 10.0), (rx[i] - 0.4, 10.0), lw=0.9)

arrow(ax, (87.0, 11.7), (59.4, 10.0), color=GRAY, lw=0.9, rad=0.16)

label(ax, 30.0, 2.6, "运行时不编译、不搜索、不重新分配", fs=7.2, color=GRAY)
save(fig, "05/fig05_1.png")
