# -*- coding: utf-8 -*-
"""第 14 章插图：稀疏形态与迭代剪枝。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, Rectangle, arrow, box, canvas,
                      label, line, save)

# ---------------------------------------------------------------- 图 14-1
fig, ax = canvas(7.2, 2.9, 100)

patterns = []
# 稠密
patterns.append(([1] * 36, "稠密", "不省计算"))
# 非结构化
pat = [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1,
       0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0]
patterns.append((pat, "非结构化", "要稀疏 kernel"))
# 2:4
pat = []
for i in range(9):
    pat += [1, 0, 1, 0]
patterns.append((pat[:36], "2:4 半结构化", "专用 Tensor Core"))
# 通道
pat = []
for r in range(6):
    for c in range(6):
        pat.append(0 if c in (1, 4) else 1)
patterns.append((pat, "整通道", "形状直接变小"))

for k, (pat, name, note) in enumerate(patterns):
    ox = 2.0 + k * 24.0
    label(ax, ox + 9.0, 38.0, name, fs=7.2, bold=True)
    for r in range(6):
        for c in range(6):
            v = pat[r * 6 + c]
            ax.add_patch(Rectangle((ox + c * 3.0, 20.0 + (5 - r) * 2.6), 2.6, 2.2,
                                   facecolor=ACCENT_L if v else WHITE,
                                   edgecolor=ACCENT if v else GRAY_L, lw=0.4, zorder=3))
    label(ax, ox + 9.0, 16.5, note, fs=6.0, color=GRAY)

label(ax, 50, 7.0, "深色为保留的权重；只有结构化与 2:4 能被硬件直接加速", fs=7.2, color=GRAY)
save(fig, "14/fig14_1.png")

# ---------------------------------------------------------------- 图 14-2
fig, ax = canvas(7.2, 2.5, 100)

steps = ["训练好的模型", "评估重要性", "剪掉一小部分", "微调恢复", "达到目标？"]
for i, s in enumerate(steps):
    x = 2.0 + i * 19.0
    box(ax, x, 12.0, 16.0, 8.0, s, fc=ACCENT_L if i < 4 else GREEN_L,
        ec=ACCENT if i < 4 else GREEN, fs=6.6)
    if i < 4:
        arrow(ax, (x + 16.4, 16.0), (x + 18.6, 16.0), lw=0.8)

arrow(ax, (90.0, 11.6), (90.0, 5.0), color=GRAY, lw=0.9)
line(ax, (90.0, 5.0), (30.0, 5.0), color=GRAY, lw=0.9)
arrow(ax, (30.0, 5.0), (30.0, 11.6), color=GRAY, lw=0.9)
label(ax, 60.0, 2.6, "没有达到目标：再剪一轮", fs=6.6, color=GRAY)

label(ax, 90.0, 23.0, "是：导出并量化", fs=6.6, color=GREEN, ha="center")
save(fig, "14/fig14_2.png")
