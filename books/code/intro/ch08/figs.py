# -*- coding: utf-8 -*-
"""第 8 章插图：GELU 近似，以及替换的收益与风险。"""

import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      line, save)

# ---------------------------------------------------------------- 图 8-1
figstyle.setup()
fig = figstyle.plt.figure(figsize=(7.2, 3.4))
ax1 = fig.add_axes([0.085, 0.56, 0.89, 0.38])
ax2 = fig.add_axes([0.085, 0.12, 0.89, 0.30])

x = np.linspace(-4, 4, 400)
from math import erf
exact = np.array([0.5 * v * (1 + erf(v / np.sqrt(2))) for v in x])
approx = 0.5 * x * (1 + np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * x ** 3)))

ax1.plot(x, exact, color=ACCENT, lw=1.8, label="精确 GELU")
ax1.plot(x, approx, color=WARM, lw=1.5, ls=(0, (4, 2)), label="tanh 近似")
ax1.axhline(0, color=GRAY, lw=0.6)
ax1.axvline(0, color=GRAY, lw=0.6)
ax1.set_xlim(-4, 4)
ax1.set_ylim(-0.6, 4.0)
ax1.tick_params(labelsize=6.5, colors=GRAY)
ax1.legend(fontsize=7, frameon=False, loc="upper left")
ax1.set_ylabel("激活值", fontsize=7, color=GRAY)
for sp in ax1.spines.values():
    sp.set_color(GRAY)
    sp.set_linewidth(0.6)

err = (approx - exact) * 1000
ax2.plot(x, err, color=RED, lw=1.4)
ax2.axhline(0, color=GRAY, lw=0.6)
ax2.set_xlim(-4, 4)
ax2.set_ylim(-0.35, 0.80)
ax2.tick_params(labelsize=6.5, colors=GRAY)
ax2.set_ylabel("误差 ×1000", fontsize=7, color=GRAY)
ax2.set_xlabel("x", fontsize=7, color=GRAY)
for sp in ax2.spines.values():
    sp.set_color(GRAY)
    sp.set_linewidth(0.6)

imax = int(np.argmax(np.abs(err)))
ax2.annotate("最大偏差约 %.5f" % abs(err[imax] / 1000.0),
             xy=(x[imax], err[imax]), xytext=(-3.7, 0.66),
             fontsize=6.6, color=RED,
             arrowprops=dict(arrowstyle="-", color=RED, lw=0.7))

figstyle.save(fig, "08/fig08_1.png")

# ---------------------------------------------------------------- 图 8-2
fig, ax = canvas(7.2, 3.4, 100)

box(ax, 8.0, 6.0, 54.0, 40.0, fc=WHITE, ec=GRAY)
line(ax, (35.0, 6.0), (35.0, 46.0), color=GRAY, lw=0.8)
line(ax, (8.0, 26.0), (62.0, 26.0), color=GRAY, lw=0.8)

label(ax, 21.5, 41.0, "收益高、风险低", fs=7.6, bold=True, color=GREEN)
label(ax, 48.5, 41.0, "收益高、风险高", fs=7.6, bold=True, color=WARM)
label(ax, 21.5, 9.0, "收益低、风险低", fs=7.6, bold=True, color=GRAY)
label(ax, 48.5, 9.0, "收益低、风险高", fs=7.6, bold=True, color=RED)

examples = [
    (12.0, 33.0, "删除 dropout", GREEN, GREEN_L),
    (12.0, 28.5, "BN 折叠", GREEN, GREEN_L),
    (38.0, 33.0, "注意力换卷积", WARM, WARM_L),
    (38.0, 28.5, "int4 量化", WARM, WARM_L),
    (12.0, 16.0, "换布局", GRAY, GRAY_L),
    (38.0, 16.0, "极端剪枝", RED, RED_L),
]
for x, y, name, ec, fc in examples:
    box(ax, x, y, 18.0, 3.6, name, fc=fc, ec=ec, fs=6.6)

arrow(ax, (66, 6.0), (66, 46.0), color=GRAY, lw=1.0)
ax.text(68.0, 26.0, "风险", fontsize=7.4, color=GRAY, rotation=90, ha="center", va="center")
arrow(ax, (8.0, 2.4), (62.0, 2.4), color=GRAY, lw=1.0)
label(ax, 35.0, 0.4, "端到端收益", fs=7.4, color=GRAY)
save(fig, "08/fig08_2.png")
