# -*- coding: utf-8 -*-
"""第 12 章插图：量化映射与粒度。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      line, save)

# ---------------------------------------------------------------- 图 12-1
fig, ax = canvas(7.2, 2.6, 100)

line(ax, (4, 18), (96, 18), color=GRAY, lw=0.9)
line(ax, (4, 16.4), (4, 19.6), color=GRAY, lw=0.9)
line(ax, (96, 16.4), (96, 19.6), color=GRAY, lw=0.9)
label(ax, 4, 15.2, "-0.8", fs=6.8, color=GRAY)
label(ax, 96, 15.2, "0.7", fs=6.8, color=GRAY)

for i in range(9):
    x = 4 + i * 11.5
    ax.plot([x], [18], "o", ms=2.6, color=ACCENT, zorder=4)
label(ax, 50, 23.4, "浮点区间，按 scale 切成等距格点", fs=7.6, color=INK)

# 量化后的整数
box(ax, 4, 4.0, 92, 6.4, fc=ACCENT_L, ec=ACCENT)
for q in [-128, -96, -64, -32, 0, 32, 64, 96, 127]:
    x = 4 + (q + 128) / 255.0 * 92
    label(ax, x, 7.2, str(q), fs=6.4, color=INK)
label(ax, 50, 1.6, "int8 的 256 个格点，这里只画了 9 个作示意", fs=6.8, color=GRAY)

arrow(ax, (4.6, 16.0), (4.6, 10.8), color=WARM, lw=0.9)
arrow(ax, (95.4, 16.0), (95.4, 10.8), color=WARM, lw=0.9)
label(ax, 50, 13.6, "两端对齐，中间按 scale 等分", fs=6.8, color=WARM)
save(fig, "12/fig12_1.png")

# ---------------------------------------------------------------- 图 12-2
figstyle.setup()
fig = figstyle.plt.figure(figsize=(7.2, 2.8))
ax2 = fig.add_axes([0.09, 0.18, 0.88, 0.66])

names = ["通道 1", "通道 2", "通道 3", "通道 4"]
vals = [0.20, 0.15, 0.10, 8.0]
colors = [ACCENT, ACCENT, ACCENT, RED]
bars = ax2.bar(range(4), vals, width=0.55, color=colors, alpha=0.85)

ax2.axhline(8.0, color=GRAY, lw=1.0, ls=(0, (4, 2)))
ax2.text(0.05, 8.32, "per-tensor：所有通道共用一个 scale", fontsize=6.8, color=GRAY, ha="left")

for i, v in enumerate(vals):
    ax2.plot([i], [v], "o", ms=3.6, color=INK, zorder=5)
ax2.text(1.35, 1.6, "圆点 = per-channel scale", fontsize=6.8, color=INK)

ax2.set_xticks(range(4))
ax2.set_xticklabels(names, fontsize=7)
ax2.set_ylabel("通道内的最大绝对值", fontsize=7, color=GRAY)
ax2.tick_params(labelsize=6.5, colors=GRAY)
ax2.set_ylim(0, 9.2)
for sp in ax2.spines.values():
    sp.set_color(GRAY)
    sp.set_linewidth(0.6)

ax2.annotate("一个异常通道把共用 scale 撑到 8\n其余通道只剩很少的格点",
             xy=(3, 8.0), xytext=(0.55, 6.6), fontsize=6.6, color=RED,
             arrowprops=dict(arrowstyle="-|>", color=RED, lw=0.8))
figstyle.save(fig, "12/fig12_2.png")
