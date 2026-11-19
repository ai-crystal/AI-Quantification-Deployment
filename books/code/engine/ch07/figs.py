# -*- coding: utf-8 -*-
"""第 7 章插图：torch.compile 的捕获、编译与缓存流程，以及重编译回路。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("engine")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      line, save)

fig, ax = canvas(7.4, 3.35, 100)

Y = 26.0
H = 8.0
steps = [
    ("第一次调用\n字节码", 2.0, 15.0, GRAY_L, GRAY),
    ("Dynamo\n捕获得 FX 图", 19.5, 17.0, ACCENT_L, ACCENT),
    ("守卫\n形状与类型", 39.0, 15.0, WARM_L, WARM),
    ("Inductor\n生成 kernel", 56.5, 17.0, GREEN_L, GREEN),
    ("缓存", 76.0, 12.0, ACCENT_L, ACCENT),
]

for i, (t, x, w, fc, ec) in enumerate(steps):
    box(ax, x, Y, w, H, t, fc=fc, ec=ec, fs=7.4, radius=1.0)
    if i:
        px = steps[i - 1][1] + steps[i - 1][2]
        arrow(ax, (px, Y + H / 2), (x - 0.4, Y + H / 2), lw=0.9)

label(ax, 41.0, Y - 3.0, "守卫失败就重捕获", fs=7.4, color=WARM)

# 重编译回路：守卫上方绕回 Dynamo
ax.plot([46.5, 46.5], [Y + H + 0.3, Y + H + 4.4], color=WARM, lw=0.9,
        ls=(0, (3, 2)))
ax.plot([46.5, 28.0], [Y + H + 4.4, Y + H + 4.4], color=WARM, lw=0.9,
        ls=(0, (3, 2)))
arrow(ax, (28.0, Y + H + 4.4), (28.0, Y + H + 0.3), color=WARM, lw=0.9,
      ls=(0, (3, 2)))
label(ax, 37.0, Y + H + 6.6, "形状或 dtype 变了，重编译", fs=7.4, color=WARM)

# 二次调用
arrow(ax, (82.0, Y - 0.3), (82.0, Y - 5.6), color=ACCENT, lw=0.9)
box(ax, 72.0, Y - 13.0, 20.0, 7.0, "同一个形状再来\n直接查缓存", fc=WHITE, ec=ACCENT,
    fs=7.2, radius=0.9)

# 首次调用等待
label(ax, 8.8, Y - 3.0, "首次要等编译", fs=7.4, color=GRAY)

label(ax, 50, 7.4, "缓存键包含代码、形状、dtype 与硬件；任意一项变了都要重编", fs=7.0,
      color=GRAY)
save(fig, "07/fig07_1.png")
