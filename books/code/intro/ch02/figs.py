# -*- coding: utf-8 -*-
"""第 2 章插图：延迟与吞吐、显存预算。"""

import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      line, save)

# ---------------------------------------------------------------- 图 2-1
fig, ax = canvas(7.2, 2.9, 100)

x = np.linspace(0, 1, 200)
thr = 1 - np.exp(-3.2 * x)
lat = 0.18 + 0.55 * x ** 2.4 / (1 - 0.55 * x + 1e-6)

ax2 = fig.add_axes(ax.get_position(), frameon=False)
ax2.set_xlim(0, 100)
ax2.set_ylim(0, 48)
ax2.set_axis_off()

ax2.plot(30 + 56 * x, 10 + 32 * thr, color=ACCENT, lw=1.8, label="吞吐")
ax2.plot(30 + 56 * x, 10 + 32 * lat / lat.max(), color=WARM, lw=1.8, ls="--", label="单请求延迟")

ax2.annotate("", xy=(86, 6), xytext=(30, 6),
             arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=0.9))
ax2.text(58, 1.8, "同时处理的请求数（batch）", ha="center", fontsize=8, color=GRAY)

ax2.text(46, 39, "吞吐", color=ACCENT, fontsize=8.6)
ax2.text(66, 30, "单请求延迟", color=WARM, fontsize=8.6)

ax2.plot([70, 70], [9, 44], color=GRAY, lw=0.8, ls=(0, (3, 3)))
ax2.text(71, 43, "算力吃满", fontsize=7.6, color=GRAY, ha="left")

ax2.text(58, 47.5, "示意：batch 变大时吞吐趋近上限，延迟持续上升",
         ha="center", fontsize=7.6, color=GRAY)

save(fig, "02/fig02_1.png")

# ---------------------------------------------------------------- 图 2-2
fig, ax = canvas(7.2, 2.0, 100)

total = 80.0
parts = [("权重 14 GB", 14, ACCENT, ACCENT_L),
         ("KV cache 32 GB", 32, GREEN, GREEN_L),
         ("激活 8 GB", 8, WARM, WARM_L),
         ("余量 26 GB", 26, GRAY, GRAY_L)]
x0 = 2.0
w_total = 96.0
for name, val, ec, fc in parts:
    w = w_total * val / total
    box(ax, x0, 12.0, w, 9.0, fc=fc, ec=ec)
    if w > 8:
        label(ax, x0 + w / 2, 16.5, name, fs=7.6, color=INK)
    x0 += w

label(ax, 2.0, 24.0, "80 GB 显存", fs=8.8, ha="left", bold=True)
label(ax, 98.0, 24.0, "16 路并发，序列 4096", fs=7.6, ha="right", color=GRAY)
label(ax, 50, 7.0, "按 7B 参数、fp16 权重与 KV cache 公式估算，不含碎片与框架开销",
      fs=7.4, color=GRAY)
save(fig, "02/fig02_2.png")
