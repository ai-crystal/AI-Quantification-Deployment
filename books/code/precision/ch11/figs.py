# -*- coding: utf-8 -*-
"""第 11 章插图：四种稀疏形状。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("precision")

# 印刷时图会按版心缩到 0.83 倍，这里把字号整体放大，保证缩后仍可读
SCALE = 1.38
_orig_label = figstyle.label
_orig_box = figstyle.box


def _label(ax, x, y, text, fs=9.5, **kw):
    _orig_label(ax, x, y, text, fs=fs * SCALE, **kw)


def _box(ax, x, y, w, h, text="", fs=9.5, **kw):
    _orig_box(ax, x, y, w, h, text, fs=fs * SCALE, **kw)


figstyle.label = _label
figstyle.box = _box

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, box, canvas, label, line, save)

N = 8
CELL = 2.6
rng = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3,
       2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5,
       0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7,
       5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2]
rnd = [rng[i] / 9.0 for i in range(N * N)]          # 保留比例约六成

fig, ax = canvas(7.4, 2.7, 100)

PANELS = [
    ("稠密", "全部保留", lambda r, c: True),
    ("非结构化", "随机置零，形状无规律", lambda r, c: rnd[r * N + c] > 0.42),
    ("2:4", "每 4 个保留 2 个", lambda r, c: (c % 4) in ((0, 2) if r % 2 == 0 else (1, 3))),
    ("整通道", "两列整体删除", lambda r, c: c not in (2, 5)),
]
PX = [2.5, 28.0, 53.5, 79.0]
GY = 7.6


for (name, sub, keep), x0 in zip(PANELS, PX):
    label(ax, x0 + N * CELL / 2, GY + N * CELL + 2.2, name, fs=7.6, bold=True)
    label(ax, x0 + N * CELL / 2, GY - 2.4, sub, fs=6.6, color=GRAY)
    for r in range(N):
        for c in range(N):
            x = x0 + c * CELL
            y = GY + (N - 1 - r) * CELL
            if keep(r, c):
                box(ax, x, y, CELL, CELL, fc=ACCENT_L, ec=ACCENT, lw=0.35, radius=0.15)
            else:
                box(ax, x, y, CELL, CELL, fc=WHITE, ec="#c9ced4", lw=0.35, radius=0.15)

label(ax, 2.5, 1.6, "每个小格是一个权重，填色格为保留、白色格为剪掉；四种形状的稀疏度接近，能不能加速取决于硬件认不认这种形状",
      fs=6.8, color=GRAY, ha="left")
save(fig, "11/fig11_1.png")
