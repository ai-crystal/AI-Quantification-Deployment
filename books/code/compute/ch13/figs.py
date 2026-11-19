# -*- coding: utf-8 -*-
"""第 13 章插图：算子实现的选型路径。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("compute")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK,
                      WARM, WARM_L, WHITE, arrow, box, canvas, label, line,
                      note, save)

# ---------------------------------------------------------------- 图 13-1
fig, ax = canvas(7.4, 4.0, 100)

layers = [
    ("直接用库", "cuBLAS / cuDNN", "形状覆盖够，不需要自定义融合", ACCENT_L, ACCENT, 40.0),
    ("模板定制", "CUTLASS", "只改 tile 或 epilogue", ACCENT_L, ACCENT, 29.0),
    ("块级编译", "Triton", "缺一个融合，或形状不常见", GREEN_L, GREEN, 18.0),
    ("手写 CUDA", "自己写", "新指令、极端形状、极致调优", WARM_L, WARM, 7.0),
]

label(ax, 62.0, 50.6, "什么情况下选它", fs=7.2, color=GRAY, ha="left")

for name, lib, why, fc, ec, y in layers:
    box(ax, 15.0, y, 26.0, 8.0, name, fc=fc, ec=ec, fs=8.2, bold=True)
    label(ax, 43.0, y + 5.0, lib, fs=7.4, color=GRAY, ha="left")
    label(ax, 62.0, y + 4.0, why, fs=7.2, color=INK, ha="left")

arrow(ax, (12.6, 47.6), (12.6, 7.6), lw=1.0, color=GRAY)
label(ax, 9.0, 30.0, "定制", fs=7.0, color=GRAY, ha="center")
label(ax, 9.0, 26.4, "与成本", fs=7.0, color=GRAY, ha="center")

label(ax, 15.0, 4.0, "先问：库能跑到峰值的几成？七成以上就别动", fs=7.4, ha="left")

save(fig, "13/fig13_1.png")
