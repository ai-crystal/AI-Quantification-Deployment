# -*- coding: utf-8 -*-
"""第 14 章插图：Amdahl 曲线与优化循环。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import numpy as np

import figstyle
figstyle.use_book("compute")
figstyle.setup()

from figstyle import (ACCENT, ACCENT_L, GRAY, GREEN, GREEN_L, INK, WARM, WARM_L,
                      arrow, box, canvas, label, save)

import matplotlib.pyplot as plt

# ---------------------------------------------------------------- 图 14-1
fig = plt.figure(figsize=(7.4, 3.4))
ax = fig.add_axes([0.10, 0.16, 0.86, 0.79])

s = np.linspace(1, 16, 400)
for p, c, lb in ((0.2, GRAY, "p = 20%"), (0.5, GREEN, "p = 50%"), (0.7, ACCENT, "p = 70%")):
    ax.plot(s, 1.0 / ((1 - p) + p / s), color=c, lw=1.6, label=lb)
    ax.axhline(1.0 / (1 - p), color=c, lw=0.8, ls=(0, (3, 3)))

ax.set_xlim(1, 16)
ax.set_ylim(1, 3.6)
ax.set_xlabel("局部加速倍数 s", fontsize=8.2)
ax.set_ylabel("端到端加速比 S", fontsize=8.2)
ax.tick_params(labelsize=7.4, length=2.5, colors=GRAY)
ax.grid(True, color="#dcdcdc", lw=0.6)
ax.set_axisbelow(True)
for sp in ("top", "right"):
    ax.spines[sp].set_visible(False)
for sp in ("left", "bottom"):
    ax.spines[sp].set_color(GRAY)
    ax.spines[sp].set_linewidth(0.8)
ax.legend(frameon=False, fontsize=7.6, loc="lower right")

ax.text(10.0, 3.36, "上限 1/(1−p)", fontsize=7.2, color=ACCENT, va="bottom")
ax.text(6.2, 2.06, "p = 50% 的上限 2.0", fontsize=7.2, color=GREEN)
ax.text(3.6, 1.31, "p = 20% 的上限 1.25", fontsize=7.2, color=GRAY)

save(fig, "14/fig14_1.png")

# ---------------------------------------------------------------- 图 14-2
fig, ax = canvas(7.4, 3.0, 100)

steps = [("定基线", 6.0, 8.0), ("profile", 30.0, 6.3), ("提假设", 54.0, 6.3),
         ("改一处", 78.0, 6.3)]

for nm, x, y in steps:
    box(ax, x, 24.0, 16.0, 7.0, nm, fc=ACCENT_L, ec=ACCENT, fs=7.6, lw=0.9)
    if x < 78.0:
        arrow(ax, (x + 16.4, 27.5), (x + 23.4, 27.5), lw=0.9, color=GRAY)

box(ax, 54.0, 12.0, 40.0, 7.0, "复测并与基线对比", fc=WARM_L, ec=WARM, fs=7.6, lw=0.9)
box(ax, 12.0, 12.0, 34.0, 7.0, "记录改动与结论", fc=GREEN_L, ec=GREEN, fs=7.6, lw=0.9)

arrow(ax, (86.0, 23.6), (86.0, 19.4), lw=0.9, color=GRAY)
arrow(ax, (53.6, 15.5), (46.4, 15.5), lw=0.9, color=GRAY)
arrow(ax, (11.6, 17.0), (11.6, 23.6), lw=0.9, color=GRAY)

label(ax, 13.6, 20.6, "一轮之后回到起点", fs=7.0, color=GRAY, ha="left")
label(ax, 50.0, 6.2, "每次只改一个变量，收益小于噪声的视为无效", fs=7.2, color=GRAY)

save(fig, "14/fig14_2.png")
