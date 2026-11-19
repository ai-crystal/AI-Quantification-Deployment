# -*- coding: utf-8 -*-
"""第 9 章插图：融合链与 epilogue 的位置。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("compute")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK,
                      WARM, WARM_L, WHITE, arrow, box, canvas, label, line,
                      note, save)

# ---------------------------------------------------------------- 图 9-1
fig, ax = canvas(7.4, 3.6, 100)

# 第一组：Conv + BN + ReLU
label(ax, 4.0, 47.4, "原图", fs=7.6, color=GRAY, ha="left")
for k, nm in enumerate(["Conv", "BN", "ReLU"]):
    x = 4.0 + k * 16.0
    box(ax, x, 38.0, 13.0, 6.4, nm, fc=WHITE, ec=GRAY, fs=7.6, lw=0.8)
    if k:
        arrow(ax, (x - 2.6, 41.2), (x - 0.4, 41.2), lw=0.8, color=GRAY)
label(ax, 52.0, 41.2, "三次读写", fs=7.2, color=GRAY, ha="left")

label(ax, 4.0, 33.0, "融合后", fs=7.6, color=GRAY, ha="left")
box(ax, 4.0, 23.4, 45.0, 6.4, "Conv + BN + ReLU（一个 kernel）", fc=ACCENT_L, ec=ACCENT, fs=7.4, lw=0.9)
label(ax, 52.0, 26.6, "一次读写", fs=7.2, color=ACCENT, ha="left")

# 第二组：Gemm + Mul + Add
label(ax, 4.0, 18.4, "Gemm + Mul + Add", fs=7.6, color=GRAY, ha="left")
for k, nm in enumerate(["Gemm", "Mul", "Add"]):
    x = 4.0 + k * 16.0
    box(ax, x, 9.0, 13.0, 6.0, nm, fc=WHITE, ec=GRAY, fs=7.2, lw=0.8)
    if k:
        arrow(ax, (x - 2.6, 12.0), (x - 0.4, 12.0), lw=0.8, color=GRAY)
box(ax, 56.0, 9.0, 41.0, 6.0, "合成一个 GEMM 加 epilogue", fc=GREEN_L, ec=GREEN, fs=7.4, lw=0.9)

label(ax, 50.0, 3.0, "融合省下的是中间张量的读写，不是计算", fs=7.4, color=GRAY)

save(fig, "09/fig09_1.png")

# ---------------------------------------------------------------- 图 9-2
fig, ax = canvas(7.4, 2.8, 100)

box(ax, 2.5, 8.0, 95.0, 26.0, fc=WHITE, ec=GRAY_L, lw=0.9, radius=1.2)

box(ax, 5.0, 20.0, 26.0, 9.0, "搬 A、B 片段\n到共享内存", fc=GRAY_L, ec=GRAY, fs=7.2, lw=0.8)
box(ax, 36.0, 20.0, 24.0, 9.0, "MMA 累加\n（K 方向循环）", fc=ACCENT_L, ec=ACCENT, fs=7.2, lw=0.8)
box(ax, 65.0, 20.0, 28.0, 9.0, "epilogue\n缩放·偏置·激活", fc=WARM_L, ec=WARM, fs=7.2, lw=0.8)

arrow(ax, (31.4, 24.5), (35.6, 24.5), lw=0.9, color=GRAY)
arrow(ax, (60.4, 24.5), (64.6, 24.5), lw=0.9, color=GRAY)

label(ax, 18.0, 17.0, "共享内存", fs=6.8, color=GRAY)
label(ax, 48.0, 17.0, "寄存器", fs=6.8, color=ACCENT)


box(ax, 65.0, 10.0, 28.0, 5.4, "写出到显存", fc=GREEN_L, ec=GREEN, fs=7.2, lw=0.8)
arrow(ax, (79.0, 19.6), (79.0, 15.8), lw=0.9, color=GREEN)

label(ax, 50.0, 3.4, "主循环只搬数据、做乘加；所有逐元素运算集中在最后一段", fs=7.4, color=GRAY)

save(fig, "09/fig09_2.png")
