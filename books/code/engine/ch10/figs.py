# -*- coding: utf-8 -*-
"""第 10 章插图：单流、双流与 CUDA Graph 三种执行时间线。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("engine")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      save)

fig, ax = canvas(7.4, 3.6, 100)

X0, UNIT = 20.0, 13.0

K, GAP = 0.52, 0.20


def t(x):
    return X0 + x * UNIT


def kern(x0, x1, y, h, fc=ACCENT_L, ec=ACCENT, text="", fs=7.2):
    box(ax, t(x0), y, (x1 - x0) * UNIT, h, text, fc=fc, ec=ec, fs=fs,
        radius=0.4, lw=0.8)


# ---------------------------------------------------------------- 单流
label(ax, 2.0, 45.4, "单流", fs=8.2, bold=True, ha="left", color=INK)
label(ax, 2.0, 40.6, "顺序执行，每个\nkernel 之间有空隙", fs=7.4, ha="left", color=GRAY)

for i in range(6):
    x = i * (K + GAP)
    kern(x, x + K, 38.6, 4.4)
label(ax, t(6 * (K + GAP)) + 1.0, 39.6, "空隙来自启动开销", fs=7.2, color=RED,
      ha="left")

# ---------------------------------------------------------------- 双流
label(ax, 2.0, 32.6, "双流", fs=8.2, bold=True, ha="left", color=INK)
label(ax, 2.0, 27.6, "两个分支各占一条流\n汇合前插一次事件", fs=7.4, ha="left", color=GRAY)

for i in range(3):
    x = i * (K + GAP)
    kern(x, x + K, 28.4, 4.4, GREEN_L, GREEN)
for i in range(2):
    x = i * (K + GAP)
    kern(x, x + K, 22.6, 4.4, ACCENT_L, ACCENT)
kern(3 * (K + GAP) - 0.1, 3 * (K + GAP) + 0.42, 22.6, 4.4, WARM_L, WARM, "相加")

label(ax, 19.0, 30.6, "流 A", fs=7.1, color=GREEN, ha="right")
label(ax, 19.0, 24.8, "流 B", fs=7.1, color=ACCENT, ha="right")


# ---------------------------------------------------------------- CUDA Graph
label(ax, 2.0, 16.6, "CUDA Graph", fs=8.2, bold=True, ha="left", color=INK)
label(ax, 2.0, 11.6, "整段录成一张图\n一次提交，内部无空隙", fs=7.4, ha="left",
      color=GRAY)

kern(0.0, 3.12, 9.6, 5.6, WARM_L, WARM, "一个图对象，重放时整段展开", fs=7.0)

ax.plot([t(0.0), t(4.4)], [5.6, 5.6], color=GRAY, lw=0.7)
arrow(ax, (t(4.4), 5.6), (t(4.8), 5.6), color=GRAY, lw=0.7)
label(ax, t(0.0), 3.8, "时间", fs=7.2, color=GRAY, ha="left")

label(ax, 50, 1.2, "三种排法的计算量相同，差别只在等待与空隙", fs=7.0, color=GRAY)
save(fig, "10/fig10_1.png")
