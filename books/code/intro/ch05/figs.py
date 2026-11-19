# -*- coding: utf-8 -*-
"""第 5 章插图：算子家族与 im2col。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, Rectangle, arrow, box, canvas,
                      label, line, save)

# ---------------------------------------------------------------- 图 5-1
fig, ax = canvas(7.2, 2.6, 100)

cards = [
    ("矩阵乘 / 卷积", "GEMM、conv\nmatmul", "计算密集", ACCENT, ACCENT_L),
    ("逐元素", "add、mul\nReLU、cast", "带宽密集", GREEN, GREEN_L),
    ("归约", "sum、mean\nmax", "需要跨线程", WARM, WARM_L),
    ("归一化 / softmax", "LayerNorm\nsoftmax", "复合，常需融合", ACCENT, ACCENT_L),
    ("数据移动", "reshape\ntranspose", "不计算，只搬运", GRAY, GRAY_L),
]
for i, (name, ops, tag, ec, fc) in enumerate(cards):
    x = 2.0 + i * 19.4
    box(ax, x, 14.0, 17.4, 18.0, fc=fc, ec=ec)
    label(ax, x + 8.7, 27.4, name, fs=7.2, bold=True)
    label(ax, x + 8.7, 21.6, ops, fs=6.2, color=INK)
    label(ax, x + 8.7, 16.8, tag, fs=6.2, color=GRAY)

label(ax, 50, 8.2, "前两类是优化的主战场；后三类常常是“看起来不慢、加起来很慢”的部分",
      fs=7.4, color=GRAY)
save(fig, "05/fig05_1.png")

# ---------------------------------------------------------------- 图 5-2
fig, ax = canvas(7.2, 3.2, 100)

# 输入 4x4
ox, oy, cell = 3.0, 6.0, 3.4
label(ax, ox + 2 * cell, 22.2, "输入 4×4", fs=7.6)
for r in range(4):
    for c in range(4):
        hi = (r < 3 and c < 3)
        ax.add_patch(Rectangle((ox + c * cell, oy + (3 - r) * cell), cell, cell,
                               facecolor=ACCENT_L if hi else WHITE,
                               edgecolor=ACCENT if hi else GRAY, lw=0.8, zorder=3))
# 滑窗
ax.add_patch(Rectangle((ox - 0.2, oy + cell - 0.2), 3 * cell + 0.4, 3 * cell + 0.4,
                       fill=False, edgecolor=WARM, lw=1.6, zorder=5))
label(ax, ox + 1.5 * cell, oy - 3.2, "取一个 3×3 窗口", fs=6.6, color=WARM)

arrow(ax, (19.0, 13.5), (24.6, 13.5))
label(ax, 21.8, 15.4, "展开", fs=7.0, color=GRAY)

# im2col 4x9
mx, my = 26.0, 6.5
cw, ch = 2.4, 2.8
label(ax, mx + 4.5 * cw, 22.2, "im2col：4 行 × 9 列", fs=7.6)
for r in range(4):
    for c in range(9):
        ax.add_patch(Rectangle((mx + c * cw, my + (3 - r) * ch), cw, ch,
                               facecolor=ACCENT_L if c < 9 else WHITE,
                               edgecolor=ACCENT, lw=0.5, zorder=3))

arrow(ax, (49.2, 13.5), (54.0, 13.5))
label(ax, 51.6, 15.4, "×", fs=9.0, color=GRAY)

# kernel 9x1
kx, ky = 55.0, 6.5
label(ax, kx + 1.6, 22.2, "卷积核 9×1", fs=7.6)
for r in range(9):
    ax.add_patch(Rectangle((kx, my + (8 - r) * ch * 4 / 9), 3.2, ch * 4 / 9,
                           facecolor=WARM_L, edgecolor=WARM, lw=0.5, zorder=3))

arrow(ax, (59.6, 13.5), (64.4, 13.5))
label(ax, 62.0, 15.4, "=", fs=9.0, color=GRAY)

# 输出 4x1
rx, ry = 65.4, 6.5
label(ax, rx + 2.0, 22.2, "输出 4×1", fs=7.6)
for r in range(4):
    ax.add_patch(Rectangle((rx, my + (3 - r) * ch), 4.0, ch,
                           facecolor=GREEN_L, edgecolor=GREEN, lw=0.6, zorder=3))

label(ax, 50, 2.4, "同一个卷积核在四个位置复用，卷积就变成了一个小矩阵乘", fs=7.4, color=GRAY)
save(fig, "05/fig05_2.png")
