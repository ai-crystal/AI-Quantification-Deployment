# -*- coding: utf-8 -*-
"""第 7 章插图：BN 折叠与 LayerNorm 的访存路径。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("compute")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK,
                      RED, WARM, WARM_L, WHITE, arrow, box, canvas, label, line,
                      note, save)

# ---------------------------------------------------------------- 图 7-1
fig, ax = canvas(7.4, 2.4, 100)

xs = [4.0, 24.0, 44.0, 64.0]
names = ["卷积", "批归一化", "ReLU", "下一层"]
for i, (x, nm) in enumerate(zip(xs, names)):
    drop = (nm == "批归一化")
    box(ax, x, 17.0, 16.0, 8.4, nm, fc=(WHITE if drop else ACCENT_L),
        ec=(GRAY if drop else ACCENT), fs=8.0, lw=0.9)
    if i:
        arrow(ax, (xs[i - 1] + 16.4, 21.2), (x - 0.6, 21.2), lw=0.9, color=GRAY)

line(ax, (25.2, 18.0), (34.8, 24.4), color=RED, lw=1.1)
line(ax, (34.8, 18.0), (25.2, 24.4), color=RED, lw=1.1)
label(ax, 32.0, 15.0, "折叠掉", fs=7.2, color=RED)

label(ax, 32.0, 29.6, "推理时 BN 是一个仿射变换", fs=7.4, color=INK)
label(ax, 50.0, 10.4, "卷积的权重和偏置改写成 W′ = γW/σ，b′ = γ(b − μ)/σ + β", fs=7.4)
label(ax, 50.0, 6.4, "折叠之后 BN 不再是 kernel，省掉一次 12.8 MB 的读写", fs=7.4, color=GRAY)
label(ax, 50.0, 2.6, "前提是统计量已经固定，训练中不能折叠", fs=7.4, color=GRAY)

save(fig, "07/fig07_1.png")

# ---------------------------------------------------------------- 图 7-2
fig, ax = canvas(7.4, 2.9, 100)

label(ax, 4.0, 37.0, "两遍访存", fs=8.4, bold=True, ha="left")

row1 = [("读 x ①", GRAY_L, GRAY), ("算均值与方差", ACCENT_L, ACCENT),
        ("再读 x，归一化写 y", ACCENT_L, ACCENT)]
for k, (txt, fc, ec) in enumerate(row1):
    x = 6.0 + k * 30.0
    box(ax, x, 27.0, 26.0, 5.6, txt, fc=fc, ec=ec, fs=7.4, lw=0.8)
    if k:
        arrow(ax, (x - 4.2, 29.8), (x - 0.6, 29.8), lw=0.9, color=GRAY)

label(ax, 4.0, 22.4, "读 12.8 MB，写 6.4 MB，合计 19.2 MB", fs=7.4, color=GRAY, ha="left")

label(ax, 4.0, 17.4, "一遍访存", fs=8.4, bold=True, ha="left")

row2 = [("读 x 一次", GRAY_L, GRAY), ("片上求统计并归一化", GREEN_L, GREEN),
        ("写 y", WARM_L, WARM)]
for k, (txt, fc, ec) in enumerate(row2):
    x = 6.0 + k * 30.0
    box(ax, x, 7.4, 26.0, 5.6, txt, fc=fc, ec=ec, fs=7.4, lw=0.8)
    if k:
        arrow(ax, (x - 4.2, 10.2), (x - 0.6, 10.2), lw=0.9, color=GRAY)

label(ax, 4.0, 2.8, "读 6.4 MB，写 6.4 MB，合计 12.8 MB；整行留在片上是前提", fs=7.4, color=GRAY, ha="left")

save(fig, "07/fig07_2.png")
