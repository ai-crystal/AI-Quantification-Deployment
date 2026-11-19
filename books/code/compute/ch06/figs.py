# -*- coding: utf-8 -*-
"""第 6 章插图：im2col 展开与 Winograd 乘法次数。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("compute")

from matplotlib.patches import Rectangle

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK,
                      WARM, WARM_L, WHITE, arrow, box, canvas, label, line,
                      note, save)

# ---------------------------------------------------------------- 图 6-1
fig, ax = canvas(7.4, 3.5, 100)

# 输入 4x4
label(ax, 12.0, 45.6, "输入 4×4", fs=8.0, bold=True)
for i in range(4):
    for j in range(4):
        hi = (i < 3 and j < 3)
        ax.add_patch(Rectangle((5.0 + j * 4.4, 26.0 + (3 - i) * 4.4), 4.2, 4.2,
                               facecolor=(ACCENT_L if hi else WHITE),
                               edgecolor=(ACCENT if hi else GRAY_L), lw=0.8, zorder=2))
label(ax, 12.0, 23.4, "第一个 3×3 窗口", fs=7.0, color=ACCENT)

# 展开矩阵 9x4
x0, y0 = 40.0, 14.0
label(ax, 56.0, 45.6, "展开后的矩阵（9 行，每列一个窗口）", fs=8.0, bold=True)
for i in range(9):
    for j in range(4):
        ax.add_patch(Rectangle((x0 + j * 9.4, y0 + (8 - i) * 2.9), 9.2, 2.8,
                               facecolor=(WARM_L if j == 0 else WHITE),
                               edgecolor=GRAY_L, lw=0.6, zorder=2))
label(ax, 38.6, 27.0, "C·R·S", fs=7.2, color=WARM, ha="right")
label(ax, 56.0, 10.0, "N·H·W", fs=7.2, color=WARM)

# 权重
box(ax, 84.0, 26.0, 12.0, 16.0, "核\nK × C·R·S", fc=GREEN_L, ec=GREEN, fs=7.2, lw=0.8)
label(ax, 90.0, 23.0, "K 行", fs=7.0, color=GREEN)

arrow(ax, (25.4, 34.0), (38.6, 34.0), lw=1.0, color=GRAY)
label(ax, 32.0, 36.0, "取窗口", fs=6.8, color=GRAY)
arrow(ax, (78.0, 34.0), (83.2, 34.0), lw=1.0, color=GRAY)

label(ax, 50.0, 4.0, "每个输入元素被复制到 R·S 个位置，3×3 就是九倍，7×7 是四十九倍",
      fs=7.4, color=GRAY)
label(ax, 50.0, 0.8, "implicit GEMM 不生成这张矩阵，按需算地址，省掉这次复制",
      fs=7.4, color=GRAY)

save(fig, "06/fig06_1.png")

# ---------------------------------------------------------------- 图 6-2
fig, ax = canvas(7.4, 3.2, 100)

label(ax, 4.0, 41.0, "直接卷积", fs=8.4, bold=True, ha="left")
label(ax, 4.0, 37.6, "4×4 输入，3×3 核，2×2 输出", fs=7.2, color=GRAY, ha="left")

# 直接：4 个输出各 9 次乘法
for k in range(4):
    x = 6.0 + k * 22.0
    box(ax, x, 25.0, 20.0, 8.6, "9 次乘法\n+ 9 次加法", fc=GRAY_L, ec=GRAY, fs=7.0, lw=0.8)
label(ax, 50.0, 21.6, "合计 36 次乘法，36 次加法", fs=7.4, color=GRAY)

label(ax, 4.0, 18.0, "F(2×2,3×3)", fs=8.4, bold=True, ha="left")
label(ax, 4.0, 14.6, "先变换，再逐点相乘，最后反变换", fs=7.2, color=GRAY, ha="left")

steps = [("输入变换\n4×4 → 4×4", ACCENT_L, ACCENT),
         ("逐点相乘\n16 次", WARM_L, WARM),
         ("输出变换\n4×4 → 2×2", GREEN_L, GREEN)]
for k, (txt, fc, ec) in enumerate(steps):
    x = 6.0 + k * 31.0
    box(ax, x, 4.0, 26.0, 8.0, txt, fc=fc, ec=ec, fs=7.0, lw=0.8)
    if k:
        arrow(ax, (x - 4.4, 8.0), (x - 0.6, 8.0), lw=0.9, color=GRAY)

label(ax, 50.0, 1.0, "乘法 16 次，代价是两轮加法与更大的中间范围", fs=7.4, color=GRAY)

save(fig, "06/fig06_2.png")
