# -*- coding: utf-8 -*-
"""第 2 章插图：优化前后同一段前向的图结构对比。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("engine")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      line, save)

fig, ax = canvas(7.4, 3.5, 100)

BW, BH = 10.4, 7.4
Y1, Y2 = 32.0, 6.0

# ---------------------------------------------------------------- 优化前
label(ax, 2.0, 43.4, "优化前", fs=8.4, bold=True, ha="left", color=GRAY)

before = [
    ("输入", GRAY_L, GRAY),
    ("转置", GRAY_L, GRAY),
    ("卷积", ACCENT_L, ACCENT),
    ("转置", GRAY_L, GRAY),
    ("批归一化", ACCENT_L, ACCENT),
    ("Dropout", RED_L, RED),
    ("输出", GRAY_L, GRAY),
]
bx = [2.0 + i * 13.6 for i in range(7)]
for i, (name, fc, ec) in enumerate(before):
    box(ax, bx[i], Y1, BW, BH, name, fc=fc, ec=ec, fs=7.8, bold=True, radius=1.0)
    if i:
        arrow(ax, (bx[i - 1] + BW, Y1 + BH / 2), (bx[i] - 0.35, Y1 + BH / 2), lw=0.9)

notes = {1: "全张量搬运", 3: "又把布局转回来", 4: "可折进权重", 5: "推理时恒等"}
for i, t in notes.items():
    label(ax, bx[i] + BW / 2, Y1 - 2.2, t, fs=7.2, color=GRAY)

# 死支路
arrow(ax, (bx[2] + BW / 2, Y1 - 0.3), (bx[2] + BW / 2, Y1 - 6.7), color=RED,
      lw=0.9, ls=(0, (3, 2)))
box(ax, bx[2] + BW / 2 - 8.6, Y1 - 13.4, 17.2, 6.2, "辅助分类头", fc=WHITE,
    ec=RED, fs=7.4, color=RED, radius=0.9, lw=0.9)
label(ax, bx[2] + BW / 2 + 9.6, Y1 - 10.3, "无消费者，删", fs=7.4, color=RED,
      ha="left")

# ---------------------------------------------------------------- 优化后
label(ax, 2.0, 20.0, "优化后", fs=8.4, bold=True, ha="left", color=GRAY)

after = [("输入", GRAY_L, GRAY), ("卷积", ACCENT_L, ACCENT),
         ("激活", GREEN_L, GREEN), ("输出", GRAY_L, GRAY)]
ax_x = [2.0, 26.0, 50.0, 74.0]
AW = 14.0
for i, (name, fc, ec) in enumerate(after):
    box(ax, ax_x[i], Y2, AW, BH, name, fc=fc, ec=ec, fs=7.8, bold=True, radius=1.0)
    if i:
        arrow(ax, (ax_x[i - 1] + AW, Y2 + BH / 2), (ax_x[i] - 0.35, Y2 + BH / 2), lw=0.9)

label(ax, ax_x[1] + AW / 2, Y2 - 2.4, "权重已预先折好", fs=7.2, color=GRAY)
label(ax, ax_x[2] + AW / 2, Y2 - 2.4, "两次遍历并成一次", fs=7.2, color=GRAY)

label(ax, 50, 0.6, "节点从七个降到四个，两次全张量搬运消失，一条死支路被删掉",
      fs=7.2, color=GRAY)
save(fig, "02/fig02_1.png")
