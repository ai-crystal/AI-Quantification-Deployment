# -*- coding: utf-8 -*-
"""第 18 章插图：云、边、端的约束光谱。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      line, save)

fig, ax = canvas(7.2, 3.0, 100)

cols = [
    ("云端", "数据中心 GPU", "吞吐、成本、弹性", ACCENT, ACCENT_L),
    ("边缘", "门店、车载、工控", "功耗、散热、可靠性", WARM, WARM_L),
    ("端侧", "手机、PC、平板", "体积、算子、电池", GREEN, GREEN_L),
]
for i, (name, where, focus, ec, fc) in enumerate(cols):
    x = 3.0 + i * 32.0
    box(ax, x, 18.0, 28.0, 16.0, fc=fc, ec=ec)
    label(ax, x + 14.0, 29.0, name, fs=11.0, bold=True, color=ec)
    label(ax, x + 14.0, 23.6, where, fs=6.8, color=INK)
    label(ax, x + 14.0, 20.2, focus, fs=6.4, color=GRAY)

arrow(ax, (3.0, 12.0), (97.0, 12.0), color=GRAY, lw=1.0)
label(ax, 3.0, 8.0, "算力、带宽、显存更充裕", fs=6.8, ha="left", color=GRAY)
label(ax, 97.0, 8.0, "功耗、体积、算子限制更紧", fs=6.8, ha="right", color=GRAY)
label(ax, 50, 3.2, "不是谁替代谁，而是同一个模型在不同约束下的三种活法", fs=7.2, color=GRAY)
save(fig, "18/fig18_1.png")
