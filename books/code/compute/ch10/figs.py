# -*- coding: utf-8 -*-
"""第 10 章插图：单流与双流时间线、逐次启动与图重放。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("compute")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK,
                      WARM, WARM_L, WHITE, arrow, box, canvas, label, line,
                      note, save)

# ---------------------------------------------------------------- 图 10-1
fig, ax = canvas(7.4, 3.0, 100)

label(ax, 4.0, 40.0, "单流", fs=8.4, bold=True, ha="left")
label(ax, 4.0, 36.8, "每个算子串行，中间有空隙", fs=7.2, color=GRAY, ha="left")

y = 27.0
seq = [("卷积", 14.0, ACCENT_L, ACCENT), ("归一化", 8.0, WARM_L, WARM),
       ("激活", 6.0, GREEN_L, GREEN), ("矩阵乘", 14.0, ACCENT_L, ACCENT),
       ("相加", 6.0, WARM_L, WARM)]
x = 8.0
for nm, w, fc, ec in seq:
    box(ax, x, y, w, 5.4, nm, fc=fc, ec=ec, fs=6.6, lw=0.7)
    x += w
    if nm != "相加":
        line(ax, (x, y + 2.7), (x + 1.8, y + 2.7), color=GRAY_L, lw=1.4)
        x += 1.8

label(ax, 4.0, 21.6, "双流", fs=8.4, bold=True, ha="left")
label(ax, 4.0, 19.4, "把没有依赖的算子放到两个流上", fs=7.2, color=GRAY, ha="left")

# 流 A
box(ax, 14.0, 12.2, 22.0, 4.6, "卷积 A", fc=ACCENT_L, ec=ACCENT, fs=6.6, lw=0.7)
box(ax, 38.0, 12.2, 16.0, 4.6, "矩阵乘 A", fc=ACCENT_L, ec=ACCENT, fs=6.6, lw=0.7)
box(ax, 56.0, 12.2, 9.0, 4.6, "相加", fc=WARM_L, ec=WARM, fs=6.6, lw=0.7)

# 流 B
box(ax, 14.0, 4.8, 14.0, 4.6, "卷积 B", fc=GREEN_L, ec=GREEN, fs=6.6, lw=0.7)
box(ax, 30.0, 4.8, 9.0, 4.6, "归一化", fc=GREEN_L, ec=GREEN, fs=6.6, lw=0.7)
box(ax, 41.0, 4.8, 7.0, 4.6, "激活", fc=GREEN_L, ec=GREEN, fs=6.6, lw=0.7)

label(ax, 4.0, 14.5, "流 0", fs=6.8, color=ACCENT, ha="left")
label(ax, 4.0, 7.1, "流 1", fs=6.8, color=GREEN, ha="left")

label(ax, 52.0, 7.1, "重叠只在资源不冲突时才有效", fs=7.0, color=GRAY, ha="left")

save(fig, "10/fig10_1.png")

# ---------------------------------------------------------------- 图 10-2
fig, ax = canvas(7.4, 2.8, 100)

label(ax, 4.0, 37.2, "逐个启动", fs=8.4, bold=True, ha="left")
x = 8.0
for k in range(7):
    box(ax, x, 25.0, 8.0, 5.2, "k%d" % (k + 1), fc=GRAY_L, ec=GRAY, fs=6.6, lw=0.7)
    x += 8.0
    if k < 6:
        line(ax, (x, 27.6), (x + 4.0, 27.6), color=WARM, lw=1.6)
        x += 4.0
label(ax, 8.0, 21.6, "橙色是提交空隙，每个 kernel 之间都有一次", fs=7.2, color=WARM, ha="left")

label(ax, 4.0, 17.2, "图重放", fs=8.4, bold=True, ha="left")
x = 8.0
for k in range(7):
    box(ax, x, 5.0, 12.2, 5.2, "k%d" % (k + 1), fc=ACCENT_L, ec=ACCENT, fs=6.6, lw=0.7)
    x += 13.0
label(ax, 8.0, 1.6, "只提交一次，节点之间的派发由硬件完成", fs=7.2, color=GRAY, ha="left")

save(fig, "10/fig10_2.png")
