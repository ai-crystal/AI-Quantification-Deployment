# -*- coding: utf-8 -*-
"""第 11 章插图：一张简化的 Nsight 时间线。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("compute")

from matplotlib.patches import Rectangle

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK,
                      RED, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      line, note, save)

# ---------------------------------------------------------------- 图 11-1
fig, ax = canvas(7.4, 3.4, 100)

# NVTX 区间
box(ax, 9.0, 41.0, 46.0, 3.0, "preprocess", fc=GREEN_L, ec=GREEN, fs=6.6, lw=0.6)
box(ax, 56.0, 41.0, 41.0, 3.0, "inference", fc=GREEN_L, ec=GREEN, fs=6.6, lw=0.6)

# 行
for nm, y in (("CPU", 35.0), ("GPU", 25.0), ("拷贝", 15.0)):
    label(ax, 8.2, y + 1.7, nm, fs=7.8, bold=True, ha="right")
    line(ax, (9.5, y - 0.6), (97.0, y - 0.6), color=GRAY_L, lw=0.6)

for x, w in [(10.0, 6.0), (17.0, 4.0), (22.0, 5.0), (34.0, 20.0),
             (56.0, 6.0), (63.0, 4.0), (68.0, 26.0)]:
    ax.add_patch(Rectangle((x, 35.0), w, 3.2, facecolor=GRAY_L, edgecolor=GRAY,
                           lw=0.6, zorder=2))
label(ax, 46.0, 31.4, "中间一段没有任何 kernel 调用", fs=6.8, color=RED, ha="center")

for x, w, nm in [(10.0, 7.0, "k1"), (17.4, 3.2, "k2"), (21.0, 8.0, "k3"),
                 (29.4, 4.0, "k4"), (56.2, 14.0, "k5"), (70.6, 22.0, "k6")]:
    ax.add_patch(Rectangle((x, 25.0), w, 3.2, facecolor=ACCENT_L, edgecolor=ACCENT,
                           lw=0.7, zorder=2))
    label(ax, x + w / 2, 26.6, nm, fs=6.2, color=ACCENT)

line(ax, (33.8, 26.6), (55.8, 26.6), color=RED, lw=1.0, ls=(0, (3, 2)))
label(ax, 44.8, 27.6, "GPU 空闲", fs=6.8, color=RED, ha="center")
label(ax, 44.8, 22.6, "CPU 卡在一次同步调用上，GPU 只能等", fs=6.8, color=RED, ha="center")

for x, w, nm in [(10.2, 6.0, "H2D"), (21.2, 7.6, "H2D"), (56.4, 13.4, "D2H")]:
    ax.add_patch(Rectangle((x, 15.0), w, 3.0, facecolor=WARM_L, edgecolor=WARM,
                           lw=0.7, zorder=2))
    label(ax, x + w / 2, 16.5, nm, fs=6.2, color=WARM)

label(ax, 52.0, 9.0, "先看空隙，再看拷贝，最后看 kernel 的排布", fs=7.2, color=GRAY)
label(ax, 52.0, 5.4, "拷贝和空隙都可能占掉可观的时间，kernel 之间还夹着一段长空闲", fs=7.2, color=GRAY)
label(ax, 52.0, 1.8, "示意图，块宽不代表实测数值", fs=7.0, color=GRAY)

save(fig, "11/fig11_1.png")
