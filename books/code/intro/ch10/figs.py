# -*- coding: utf-8 -*-
"""第 10 章插图：推理时间线与端到端拆分。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, Rectangle, arrow, box, canvas,
                      label, line, save)

# ---------------------------------------------------------------- 图 10-1
fig, ax = canvas(7.2, 2.9, 100)

rows = [("CPU", 26.0), ("GPU", 12.0)]
for name, y in rows:
    label(ax, 2.0, y + 3.4, name, fs=7.6, ha="left", color=GRAY)

# CPU 侧的小块与空隙
for x, w, name in [(12, 5, "API"), (19, 4, "API"), (31, 5, "API"),
                   (45, 4, "API"), (58, 5, "API"), (72, 4, "API")]:
    box(ax, x, 27.0, w, 5.0, name, fc=GRAY_L, ec=GRAY, fs=5.6)

# GPU 侧
blocks = [(12, 8, "拷贝", WARM, WARM_L), (22, 14, "kernel", ACCENT, ACCENT_L),
          (38, 9, "", WHITE, WHITE), (49, 11, "kernel", ACCENT, ACCENT_L),
          (62, 8, "拷贝", WARM, WARM_L), (72, 16, "kernel", ACCENT, ACCENT_L)]
for x, w, name, ec, fc in blocks:
    if name:
        box(ax, x, 12.0, w, 6.8, name, fc=fc, ec=ec, fs=6.4)
label(ax, 42.5, 15.4, "空隙", fs=6.2, color=RED)

# 同步标记
line(ax, (89.0, 10.0), (89.0, 34.0), color=RED, lw=1.0, ls=(0, (3, 2)))
label(ax, 89.0, 8.2, "同步", fs=6.2, color=RED)

arrow(ax, (10.0, 4.0), (92.0, 4.0), color=GRAY, lw=0.9)
label(ax, 51.0, 1.6, "时间（示意，不按真实比例）", fs=7.0, color=GRAY)
save(fig, "10/fig10_1.png")

# ---------------------------------------------------------------- 图 10-2
fig, ax = canvas(7.2, 2.6, 100)

total = 120.0
segs = [("卷积 30", 30, ACCENT, ACCENT_L), ("其他 kernel 40", 40, GREEN, GREEN_L),
        ("拷贝 25", 25, WARM, WARM_L), ("空隙 25", 25, GRAY, GRAY_L)]
x0, wbar = 3.0, 90.0
for name, val, ec, fc in segs:
    w = wbar * val / total
    box(ax, x0, 14.0, w, 7.0, fc=fc, ec=ec)
    label(ax, x0 + w / 2, 17.5, name, fs=6.6)
    x0 += w

label(ax, 3.0, 25.0, "端到端 120 ms", fs=8.4, ha="left", bold=True)
label(ax, 93.0, 25.0, "按假设数据拆分", fs=6.8, ha="right", color=GRAY)

# 指示可优化项
for x, text in [(12.0, "先看占比"), (66.0, "常被忽略")]:
    line(ax, (x, 21.4), (x, 23.8), color=RED, lw=0.8, ls=(0, (2, 2)))
    label(ax, x, 10.2, text, fs=6.2, color=RED)

label(ax, 50, 4.0, "卷积只占四分之一；拷贝与空隙加起来接近一半", fs=7.2, color=GRAY)
save(fig, "10/fig10_2.png")
