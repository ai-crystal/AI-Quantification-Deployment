# -*- coding: utf-8 -*-
"""第 9 章插图：四个激活张量的生命周期，复用前后的峰值对比。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("engine")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      save)

fig, ax = canvas(7.4, 3.6, 100)

X0, X1, OPS = 14.0, 96.0, 9.0


def opx(op):
    return X0 + (op - 1) * (X1 - X0) / OPS


def seg(y, h, op0, op1, fc, ec):
    box(ax, opx(op0), y, opx(op1) - opx(op0), h, "", fc=fc, ec=ec, fs=7.0,
        radius=0.5, lw=0.9)


def axis(y):
    ax.plot([X0 - 1, X1 + 1], [y, y], color=GRAY, lw=0.8)
    for op in range(1, 10):
        x = opx(op)
        ax.plot([x, x], [y, y - 0.7], color=GRAY, lw=0.8)
        ax.text(x, y - 1.1, str(op), ha="center", va="top", fontsize=7.2, color=GRAY)


# ---------------------------------------------------------------- 不复用
label(ax, 2.0, 46.0, "不复用", fs=8.2, bold=True, ha="left", color=WARM)
label(ax, 2.0, 43.4, "峰值 256 MB", fs=7.2, ha="left", color=RED)

rows = [(39.4, "A　64"), (36.0, "B　96"), (32.6, "C　96"), (29.2, "D　48")]
spans = [(1, 6, ACCENT_L, ACCENT), (2, 4, GREEN_L, GREEN),
         (4, 8, GREEN_L, GREEN), (6, 9, WARM_L, WARM)]
for (y, name), (a, b, fc, ec) in zip(rows, spans):
    label(ax, 2.0, y + 1.4, name, fs=7.4, ha="left", color=ec)
    seg(y, 2.8, a, b, fc, ec)

ax.plot([opx(4), opx(4)], [28.8, 42.0], color=RED, lw=0.8, ls=(0, (3, 2)))
label(ax, opx(4) + 1.4, 30.6, "A B C 同时活着", fs=7.4, ha="left", color=RED)

axis(26.2)

# ---------------------------------------------------------------- 复用后
label(ax, 2.0, 23.4, "复用后", fs=8.2, bold=True, ha="left", color=GREEN)
label(ax, 2.0, 20.6, "峰值 160 MB", fs=7.2, ha="left", color=GREEN)

label(ax, 2.0, 18.4, "块 1　64", fs=7.4, ha="left", color=GRAY)
seg(17.0, 2.8, 1, 6, ACCENT_L, ACCENT)
seg(17.0, 2.8, 6, 9, WARM_L, WARM)
label(ax, opx(3.0), 15.7, "A", fs=7.4, color=ACCENT)
label(ax, opx(7.4), 15.7, "D 复用同一块", fs=7.4, color=WARM, ha="center")

label(ax, 2.0, 12.8, "块 2　96", fs=7.4, ha="left", color=GRAY)
seg(11.4, 2.8, 2, 4, GREEN_L, GREEN)
seg(11.4, 2.8, 4, 8, GREEN_L, GREEN)
label(ax, opx(3.0), 10.1, "B", fs=7.4, color=GREEN)
label(ax, opx(6.0), 10.1, "C 接着用", fs=7.4, color=GREEN)

ax.plot([opx(4), opx(4)], [9.4, 22.2], color=RED, lw=0.8, ls=(0, (3, 2)))

label(ax, 50, 4.6, "横轴是算子序号，一条横杠是一个张量的存活区间；同一行代表共用同一块显存",
      fs=7.0, color=GRAY)
save(fig, "09/fig09_1.png")
