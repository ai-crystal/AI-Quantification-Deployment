# -*- coding: utf-8 -*-
"""第 23 章插图：基础模型与多 LoRA 适配器。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, Rectangle, arrow, box, canvas,
                      label, line, save)

fig, ax = canvas(7.2, 2.5, 100)

box(ax, 2.0, 11.0, 22.0, 13.0, "基础模型\n只加载一份", fc=ACCENT_L, ec=ACCENT, fs=7.6, bold=True)

for i, name in enumerate(["LoRA A", "LoRA B", "LoRA C"]):
    y = 20.5 - i * 4.6
    box(ax, 32.0, y, 14.0, 3.6, name, fc=WARM_L, ec=WARM, fs=6.6)
    arrow(ax, (24.4, 17.5), (31.6, y + 1.8), color=GRAY, lw=0.6)

label(ax, 49.0, 17.5, "适配器按请求挂载\n几十 MB 到几百 MB", fs=6.8, color=GRAY, ha="left")

# 混排 batch
label(ax, 32.0, 8.8, "同一个 batch", fs=6.2, ha="left", color=GRAY)
segs = ["请求 A", "请求 B", "请求 C"]
for i, name in enumerate(segs):
    box(ax, 32.0 + i * 20.0, 3.0, 18.0, 4.4, name, fc=WHITE, ec=GRAY, fs=6.6)


label(ax, 50, 0.8, "基础权重共享，适配器在计算时切换；一个 batch 可以混多个租户", fs=6.8, color=GRAY)
save(fig, "23/fig23_1.png")
