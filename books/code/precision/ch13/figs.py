# -*- coding: utf-8 -*-
"""第 13 章插图：全连接层与卷积层的低秩分解。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("precision")

# 印刷时图会按版心缩到 0.83 倍，这里把字号整体放大，保证缩后仍可读
SCALE = 1.16
_orig_label = figstyle.label
_orig_box = figstyle.box


def _label(ax, x, y, text, fs=9.5, **kw):
    _orig_label(ax, x, y, text, fs=fs * SCALE, **kw)


def _box(ax, x, y, w, h, text="", fs=9.5, **kw):
    _orig_box(ax, x, y, w, h, text, fs=fs * SCALE, **kw)


figstyle.label = _label
figstyle.box = _box

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, WARM,
                      WARM_L, WHITE, arrow, box, canvas, label, line, save)

fig, ax = canvas(7.4, 3.0, 100)

# ---------------- 左：全连接
label(ax, 4.0, 36.4, "全连接层", fs=7.6, bold=True, color=INK, ha="left")

box(ax, 4.0, 17.0, 13.0, 13.0, fc=GRAY_L, ec=GRAY, lw=0.9, radius=1.0)
label(ax, 10.5, 25.2, "W", fs=8.6, bold=True)
label(ax, 10.5, 21.2, "m × n", fs=7.0, color=GRAY)

arrow(ax, (17.4, 23.5), (21.0, 23.5), lw=0.9)
box(ax, 21.4, 19.0, 5.6, 9.0, fc=ACCENT_L, ec=ACCENT, lw=0.9, radius=0.8)
label(ax, 24.2, 24.6, "A", fs=8.2, bold=True, color=ACCENT)
label(ax, 24.2, 21.8, "m×r", fs=6.4, color=GRAY)
arrow(ax, (27.4, 23.5), (30.4, 23.5), lw=0.9)
box(ax, 30.8, 20.4, 9.0, 6.2, fc=ACCENT_L, ec=ACCENT, lw=0.9, radius=0.8)
label(ax, 35.3, 25.0, "B", fs=8.2, bold=True, color=ACCENT)
label(ax, 35.3, 22.2, "r×n", fs=6.4, color=GRAY)

label(ax, 4.0, 13.6, "参数从 m n 降到 r(m + n)，秩 r 要小于 mn/(m+n) 才有收益",
      fs=6.8, color=GRAY, ha="left")

# ---------------- 右：卷积
label(ax, 54.0, 36.4, "卷积层", fs=7.6, bold=True, color=INK, ha="left")

box(ax, 56.0, 25.0, 30.0, 8.0, fc=GRAY_L, ec=GRAY, lw=0.9, radius=1.0)
label(ax, 71.0, 30.6, "k × k 卷积", fs=7.8, bold=True)
label(ax, 71.0, 27.4, "C_in → C_out", fs=6.6, color=GRAY)

arrow(ax, (71.0, 24.8), (71.0, 20.6), lw=0.9)

for x, t1, t2, ec, fc in ((54.0, "1 × 1", "C_in → r", ACCENT, ACCENT_L),
                          (69.0, "k × k", "r → r", WARM, WARM_L),
                          (84.0, "1 × 1", "r → C_out", ACCENT, ACCENT_L)):
    box(ax, x, 13.4, 13.2, 7.2, fc=fc, ec=ec, lw=0.9, radius=0.9)
    label(ax, x + 6.6, 18.4, t1, fs=7.6, bold=True, color=ec)
    label(ax, x + 6.6, 15.2, t2, fs=6.4, color=GRAY)

arrow(ax, (67.4, 17.0), (68.8, 17.0), lw=0.8)
arrow(ax, (82.4, 17.0), (83.8, 17.0), lw=0.8)

label(ax, 54.0, 9.6, "中间通道数 r 是新的瓶颈，选择它要把三步的计算量一起算",
      fs=6.8, color=GRAY, ha="left")

label(ax, 4.0, 3.0, "左图矩形的高宽比表示矩阵形状；右图三个框都是标准卷积，引擎可以直接执行，不需要专用 kernel",
      fs=6.8, color=GRAY, ha="left")
save(fig, "13/fig13_1.png")
