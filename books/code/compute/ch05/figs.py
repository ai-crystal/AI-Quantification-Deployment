# -*- coding: utf-8 -*-
"""第 5 章插图：GEMM 分块与双缓冲时间线。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("compute")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK,
                      WARM, WARM_L, WHITE, arrow, box, canvas, label, line,
                      note, save)

from matplotlib.patches import Rectangle

# ---------------------------------------------------------------- 图 5-1
fig, ax = canvas(7.4, 3.6, 100)

# 左：显存里的 C
label(ax, 14.8, 45.8, "显存里的 C", fs=8.2, bold=True)
for i in range(6):
    for j in range(6):
        hi = (i == 1 and j == 1)
        ax.add_patch(Rectangle((4.0 + j * 3.6, 22.0 + i * 3.6), 3.5, 3.5,
                               facecolor=(WARM_L if hi else WHITE),
                               edgecolor=(WARM if hi else GRAY_L), lw=0.7, zorder=2))
label(ax, 14.8, 19.4, "标出一块 128×128", fs=7.2, color=GRAY)

# 中：A 条带（宽）与 B 条带（高）
label(ax, 43.0, 39.6, "A 条带 128×32", fs=7.4, color=ACCENT, bold=True)
for i in range(3):
    for j in range(12):
        ax.add_patch(Rectangle((34.0 + j * 1.5, 33.4 + i * 1.5), 1.45, 1.45,
                               facecolor=ACCENT_L, edgecolor=ACCENT, lw=0.4, zorder=2))
for i in range(12):
    for j in range(3):
        ax.add_patch(Rectangle((46.0 + j * 1.38, 16.0 + i * 1.38), 1.33, 1.33,
                               facecolor=GREEN_L, edgecolor=GREEN, lw=0.4, zorder=2))
label(ax, 51.4, 25.0, "B 条带" + chr(10) + "32×128", fs=7.4, color=GREEN, bold=True, ha="left")

# 右：寄存器里的累加块
label(ax, 82.0, 45.8, "寄存器里的累加块", fs=8.2, bold=True)
for i in range(6):
    for j in range(6):
        ax.add_patch(Rectangle((72.0 + j * 3.4, 22.0 + i * 3.4), 3.3, 3.3,
                               facecolor=WARM_L, edgecolor=WARM, lw=0.6, zorder=2))
label(ax, 82.0, 19.4, "每线程 8×8 个输出", fs=7.2, color=WARM)

arrow(ax, (27.4, 32.0), (33.2, 34.4), lw=1.0, color=GRAY)
label(ax, 30.2, 35.6, "搬一次", fs=6.8, color=GRAY)
arrow(ax, (60.0, 26.0), (71.2, 30.0), lw=1.0, color=GRAY)
label(ax, 62.0, 31.6, "在寄存器里复用", fs=6.8, color=GRAY)

label(ax, 50.0, 8.2, "共享内存复用一个条带 64 次，寄存器再复用 64 次", fs=7.4, color=GRAY)
label(ax, 50.0, 4.6, "显存只被读一遍，K 方向分段累加，中间结果不写回", fs=7.4, color=GRAY)

save(fig, "05/fig05_1.png")

# ---------------------------------------------------------------- 图 5-2
fig, ax = canvas(7.4, 3.2, 100)

label(ax, 4.0, 40.6, "无重叠", fs=8.6, bold=True, ha="left")
label(ax, 4.0, 37.2, "搬运和计算串行，每一段都要等", fs=7.2, color=GRAY, ha="left")

names = ["载入 1", "计算 1", "载入 2", "计算 2", "载入 3", "计算 3"]
for k, nm in enumerate(names):
    x = 6.0 + k * 15.0
    load = k % 2 == 0
    box(ax, x, 27.0, 14.6, 5.0, nm,
        fc=(GRAY_L if load else ACCENT_L), ec=(GRAY if load else ACCENT), fs=6.8, lw=0.7)

label(ax, 4.0, 21.2, "双缓冲", fs=8.6, bold=True, ha="left")
label(ax, 4.0, 17.8, "搬运放到另一条路径上，和计算同时进行", fs=7.2, color=GRAY, ha="left")

for k in range(4):
    box(ax, 6.0 + k * 15.0, 3.4, 14.6, 4.6, "载入 %d" % (k + 1),
        fc=GRAY_L, ec=GRAY, fs=6.8, lw=0.7)
box(ax, 6.0, 10.0, 14.6, 4.6, "空闲", fc=WHITE, ec=GRAY_L, fs=6.8, lw=0.7, color=GRAY)
for k in range(3):
    box(ax, 21.0 + k * 15.0, 10.0, 14.6, 4.6, "计算 %d" % (k + 1),
        fc=ACCENT_L, ec=ACCENT, fs=6.8, lw=0.7)

label(ax, 69.0, 11.8, "计算", fs=7.0, color=ACCENT, ha="left")
label(ax, 69.0, 5.2, "搬运", fs=7.0, color=GRAY, ha="left")
label(ax, 96.0, 38.6, "时间 →", fs=7.0, color=GRAY, ha="right")

save(fig, "05/fig05_2.png")
