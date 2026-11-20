# -*- coding: utf-8 -*-
"""第 20 章插图：四种注意力的 K/V 组织。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, Rectangle, box, canvas, label,
                      line, save)

fig, ax = canvas(7.2, 3.2, 100)

panels = [
    ("MHA", 4, 4, "1×", ACCENT, ACCENT_L),
    ("MQA", 4, 1, "1/4", GREEN, GREEN_L),
    ("GQA", 4, 2, "1/2", WARM, WARM_L),
    ("MLA", 4, 1, "更小", GRAY, GRAY_L),
]

for k, (name, nq, nkv, ratio, ec, fc) in enumerate(panels):
    x0 = 2.0 + k * 24.5
    label(ax, x0 + 10.0, 39.0, name, fs=8.2, bold=True)

    label(ax, x0, 33.4, "查询头", fs=6.4, ha="left", color=GRAY)
    for i in range(nq):
        qx = x0 + 2.0 + i * 4.3
        ax.add_patch(Rectangle((qx, 27.5), 3.4, 3.4, facecolor=fc,
                               edgecolor=ec, lw=0.7, zorder=3))

    label(ax, x0, 23.4, "K / V", fs=6.4, ha="left", color=GRAY)
    if name == "MLA":
        box(ax, x0 + 1.2, 14.5, 15.6, 6.0, "潜向量", fc=fc, ec=ec, fs=6.4)
    else:
        for i in range(nkv):
            kx = x0 + 1.2 + i * 5.6
            ax.add_patch(Rectangle((kx, 15.5), 4.6, 4.6, facecolor=fc,
                                   edgecolor=ec, lw=0.7, zorder=3))
            label(ax, kx + 2.3, 17.8, "K/V", fs=5.6, color=ec)

    label(ax, x0 + 9.0, 9.0, "cache " + ratio, fs=7.0, color=GRAY)

label(ax, 50, 2.4, "四个查询头为例；cache 比例只表示相对大小，实际取决于头数与层数",
      fs=7.0, color=GRAY)
save(fig, "20/fig20_1.png")
