# -*- coding: utf-8 -*-
"""第 8 章插图：QDQ 图与隐式量化图的对照。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("engine")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      save)

fig, ax = canvas(7.4, 3.4, 100)

BW, BH = 12.6, 7.0

# ---------------------------------------------------------------- QDQ
label(ax, 2.0, 41.4, "显式量化（QDQ 图）", fs=8.2, bold=True, ha="left", color=ACCENT)

q1 = [(2.0, "浮点\n输入", GRAY_L, GRAY), (17.0, "量化", WARM_L, WARM),
      (32.0, "反量化", WARM_L, WARM), (47.0, "卷积", ACCENT_L, ACCENT),
      (62.0, "量化", WARM_L, WARM), (77.0, "反量化", WARM_L, WARM)]
Y1 = 30.0
for i, (x, t, fc, ec) in enumerate(q1):
    box(ax, x, Y1, BW, BH, t, fc=fc, ec=ec, fs=7.2, radius=0.9)
    if i:
        arrow(ax, (q1[i - 1][0] + BW, Y1 + BH / 2), (x - 0.4, Y1 + BH / 2), lw=0.9)

label(ax, 24.0, Y1 - 2.6, "边界显式可见", fs=7.4, color=WARM)
label(ax, 84.0, Y1 - 2.6, "再回到浮点", fs=7.4, color=WARM)

# ---------------------------------------------------------------- 隐式
label(ax, 2.0, 20.4, "隐式量化（属性带缩放因子）", fs=8.2, bold=True, ha="left",
      color=GREEN)

q2 = [(2.0, "浮点\n输入", GRAY_L, GRAY), (24.0, "量化卷积\n缩放写在属性", ACCENT_L, ACCENT),
      (50.0, "量化卷积\n缩放写在属性", ACCENT_L, ACCENT),
      (74.0, "浮点\n输出", GRAY_L, GRAY)]
BW2 = 16.0
Y2 = 8.0
for i, (x, t, fc, ec) in enumerate(q2):
    box(ax, x, Y2, BW2, 9.0, t, fc=fc, ec=ec, fs=7.2, radius=0.9)
    if i:
        arrow(ax, (q2[i - 1][0] + BW2, Y2 + 4.5), (x - 0.4, Y2 + 4.5), lw=0.9)

label(ax, 32.0, Y2 - 2.8, "边界靠属性推断", fs=7.4, color=GRAY)

label(ax, 50, 1.0, "同一段计算的两种画法，节点数差一倍，可移植性也不同", fs=7.0,
      color=GRAY)
save(fig, "08/fig08_1.png")
