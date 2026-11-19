# -*- coding: utf-8 -*-
"""第 1 章插图：一个 SM 的内部构成。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("compute")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK,
                      WARM, WARM_L, WHITE, arrow, box, canvas, label, note, save)

# ---------------------------------------------------------------- 图 1-1
fig, ax = canvas(7.4, 4.6, 100)

# SM 外框
box(ax, 1.5, 10.0, 97.0, 46.0, fc=WHITE, ec=INK, lw=1.2, radius=1.6)
label(ax, 4.2, 52.4, "一个 SM（A100 共 108 个）", fs=8.6, bold=True, ha="left")
label(ax, 96.2, 52.4, "最多 64 个 warp 驻留", fs=7.2, color=GRAY, ha="right")

rows = [("张量核心", GREEN_L, GREEN),
        ("FP32 × 16", ACCENT_L, ACCENT),
        ("寄存器 16K×32b", GRAY_L, GRAY),
        ("warp 调度器", ACCENT_L, ACCENT)]

for k in range(4):
    x = 3.4 + k * 23.8
    box(ax, x, 21.5, 22.2, 26.0, fc=WHITE, ec=ACCENT, lw=0.9, radius=1.2)
    label(ax, x + 11.1, 44.6, "处理块 %d" % (k + 1), fs=7.4, color=ACCENT, bold=True)
    for j, (txt, fc, ec) in enumerate(rows):
        box(ax, x + 2.1, 23.0 + j * 5.0, 18.0, 4.0, txt, fc=fc, ec=ec,
            fs=6.9, lw=0.8, radius=0.9)

# 共享内存与 L1
box(ax, 3.4, 12.6, 93.2, 6.4,
    "共享内存与 L1 共用约 192 KB，其中共享内存最多 164 KB",
    fc=WARM_L, ec=WARM, fs=7.8)

# 片外存储
box(ax, 3.4, 2.6, 93.2, 5.4,
    "L2 40 MB　→　HBM 80 GB，约 2 TB/s",
    fc=GRAY_L, ec=GRAY, fs=7.8)

arrow(ax, (50.0, 12.4), (50.0, 8.3), lw=1.0, color=GRAY)
label(ax, 52.2, 11.1, "全局访存", fs=7.0, color=GRAY, ha="left")

note(ax, 50.0, 0.2, "寄存器堆共 256 KB，按四个处理块划分，每块 16K×32b" + chr(10) +
     "四个调度器各发各的指令，用切换 warp 隐藏延迟", fs=6.9, ha="center")

save(fig, "01/fig01_1.png")
