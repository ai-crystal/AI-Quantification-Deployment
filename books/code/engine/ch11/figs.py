# -*- coding: utf-8 -*-
"""第 11 章插图：静态批处理与连续批处理的时间线。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("engine")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      save)

fig, ax = canvas(7.4, 3.4, 100)

X0, UNIT = 18.0, 8.0


def t(x):
    return X0 + x * UNIT


# ---------------------------------------------------------------- 静态
label(ax, 2.0, 43.4, "静态批处理", fs=8.2, bold=True, ha="left", color=WARM)

rows_static = [
    ("请求 1", 1.6), ("请求 2", 1.2), ("请求 3", 5.0), ("请求 4", 1.0),
]
for i, (name, dur) in enumerate(rows_static):
    y = 38.0 - i * 4.4
    label(ax, 14.0, y + 1.6, name, fs=7.2, ha="right", color=GRAY)
    box(ax, t(0.0), y, dur * UNIT, 3.2, "", fc=ACCENT_L, ec=ACCENT, radius=0.4, lw=0.8)
    box(ax, t(dur), y, (5.0 - dur) * UNIT, 3.2, "", fc=WHITE, ec=GRAY_L,
        radius=0.4, lw=0.7)

label(ax, t(5.2), 33.0, "空转等最慢的一条", fs=7.4, color=RED, ha="left")
label(ax, t(5.2), 29.0, "下一批要等这里才进", fs=7.4, color=GRAY, ha="left")

ax.plot([t(0.0), t(5.0)], [23.0, 23.0], color=GRAY, lw=0.7)
ax.plot([t(0.0), t(0.0)], [22.4, 23.6], color=GRAY, lw=0.7)
label(ax, t(0.0), 21.6, "批 1", fs=7.2, color=GRAY)

# ---------------------------------------------------------------- 连续
label(ax, 2.0, 17.4, "连续批处理", fs=8.2, bold=True, ha="left", color=GREEN)

rows_cont = [
    ("请求 1", 0.0, 1.6), ("请求 2", 0.0, 1.2), ("请求 3", 0.0, 5.0),
    ("请求 4", 0.0, 1.0), ("请求 5", 1.2, 3.4), ("请求 6", 2.4, 4.6),
]
for i, (name, s, e) in enumerate(rows_cont):
    y = 14.4 - i * 1.9
    label(ax, 14.0, y + 0.7, name, fs=7.0, ha="right", color=GRAY)
    box(ax, t(s), y, (e - s) * UNIT, 1.5, "", fc=GREEN_L, ec=GREEN, radius=0.3, lw=0.7)

label(ax, t(4.75), 8.6, "结束即退出\n槽位立刻被补上", fs=7.2, color=ACCENT, ha="left")

label(ax, 50, 1.6, "横轴是解码步数；静态批处理里空槽会一直占到批结束，连续批处理每步重排",
      fs=7.0, color=GRAY)
save(fig, "11/fig11_1.png")

# ---------------------------------------------------------------- 图 11-2
fig, ax = canvas(7.4, 3.4, 100)

label(ax, 2.0, 43.0, "逻辑块", fs=8.0, bold=True, ha="left", color=ACCENT)
label(ax, 34.0, 43.0, "块表", fs=8.0, bold=True, ha="left", color=WARM)
label(ax, 58.0, 43.0, "物理块", fs=8.0, bold=True, ha="left", color=GREEN)

# 逻辑块：请求 A 与 B
label(ax, 2.0, 37.4, "请求 A", fs=7.0, ha="left", color=GRAY)
for i in range(4):
    box(ax, 2.0 + i * 7.4, 31.0, 6.4, 5.0, "A%d" % i, fc=ACCENT_L, ec=ACCENT,
        fs=7.4, radius=0.6)

label(ax, 2.0, 27.4, "请求 B", fs=7.0, ha="left", color=GRAY)
for i in range(3):
    box(ax, 2.0 + i * 7.4, 21.0, 6.4, 5.0, "B%d" % i, fc=GREEN_L, ec=GREEN,
        fs=7.4, radius=0.6)

# 块表
tbl = [("A0", 1, 21.0), ("A1", 1, None)]
pairs = [("A0", "P7"), ("A1", "P2"), ("A2", "P5"), ("A3", "P9"),
         ("B0", "P7"), ("B1", "P2"), ("B2", "P6")]
y = 37.6
for i, (lg, ph) in enumerate(pairs):
    yy = y - i * 2.9
    label(ax, 34.0, yy, lg, fs=7.2, ha="left", color=GRAY)
    arrow(ax, (37.0, yy), (41.0, yy), color=GRAY, lw=0.6)
    label(ax, 41.6, yy, ph, fs=7.2, ha="left", color=INK)

# 物理块
phys = ["P2", "P5", "P6", "P7", "P9"]
for i, p in enumerate(phys):
    box(ax, 58.0, 34.0 - i * 4.6, 9.0, 3.6, p, fc=WHITE, ec=GREEN, fs=7.4, radius=0.5)

label(ax, 70.0, 34.0, "P7 与 P2 被两条请求\n共享，只在分叉处\n各自分配", fs=7.4, ha="left",
      color=GREEN)

label(ax, 50, 4.0, "逻辑块按需增加，块表把逻辑地址翻译成物理地址", fs=7.0, color=GRAY)
save(fig, "11/fig11_2.png")
