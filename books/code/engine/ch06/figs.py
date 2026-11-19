# -*- coding: utf-8 -*-
"""第 6 章插图：从高层图到机器码的下降路径。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("engine")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      save)

fig, ax = canvas(7.4, 3.6, 100)

layers = [
    ("框架导出的图", "算子、张量、属性", "融合、消除、布局选择", ACCENT_L, ACCENT),
    ("张量层方言", "对整块张量的读写", "分块、数据布局", GREEN_L, GREEN),
    ("循环层方言", "索引、循环、共享内存", "向量化、展开、线程映射", WARM_L, WARM),
    ("LLVM 或 GPU 指令", "寄存器、指令、线程", "寄存器分配、指令选择", GRAY_L, GRAY),
]

label(ax, 3.0, 45.4, "下降路径", fs=8.2, bold=True, ha="left", color=INK)
label(ax, 31.5, 45.4, "这一层表示什么", fs=7.4, ha="left", color=GRAY)

top = 36.4
for i, (name, content, opt, fc, ec) in enumerate(layers):
    yy = top - i * 9.4
    box(ax, 3.0, yy, 25.0, 7.2, name, fc=fc, ec=ec, fs=7.8, bold=True)
    label(ax, 31.5, yy + 4.7, content, fs=7.3, ha="left")
    label(ax, 31.5, yy + 1.8, opt, fs=7.0, ha="left", color=GRAY)
    if i:
        arrow(ax, (15.5, yy + 9.4), (15.5, yy + 7.7), color=INK, lw=1.0)

ax.text(68.0, 22.0, "越往下，形状与语义的信息越少，\n能做的重写也越局部。\n\n每一步只改一层，改完可以单独验证。",
        fontsize=7.2, color=GRAY, ha="left", va="center", linespacing=1.7)
save(fig, "06/fig06_1.png")
