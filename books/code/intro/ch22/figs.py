# -*- coding: utf-8 -*-
"""第 22 章插图：三种并行与 PD 分离。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, Rectangle, arrow, box, canvas,
                      label, line, save)

# ---------------------------------------------------------------- 图 22-1
fig, ax = canvas(7.2, 3.2, 100)

# TP
label(ax, 2.0, 39.0, "张量并行", fs=8.0, bold=True, ha="left")
box(ax, 2.0, 22.0, 13.0, 12.0, "GPU 0\n权重左半", fc=ACCENT_L, ec=ACCENT, fs=6.8)
box(ax, 17.0, 22.0, 13.0, 12.0, "GPU 1\n权重右半", fc=ACCENT_L, ec=ACCENT, fs=6.8)
arrow(ax, (15.4, 28.0), (16.6, 28.0), lw=0.8, style="<|-|>")
label(ax, 9.0, 19.0, "每层 all-reduce", fs=6.0, color=GRAY)

# PP
label(ax, 36.0, 39.0, "流水并行", fs=8.0, bold=True, ha="left")
for i, name in enumerate(["层 1–10", "层 11–20", "层 21–30"]):
    y = 31.0 - i * 6.0
    box(ax, 36.0, y, 16.0, 4.8, name, fc=GREEN_L, ec=GREEN, fs=6.6)
    if i:
        arrow(ax, (44.0, y + 7.8), (44.0, y + 5.2), lw=0.7)

# EP
label(ax, 60.0, 39.0, "专家并行", fs=8.0, bold=True, ha="left")
box(ax, 60.0, 30.0, 12.0, 4.6, "路由器", fc=WARM_L, ec=WARM, fs=6.8)
for i in range(4):
    x = 60.0 + (i % 2) * 14.0
    y = 22.0 - (i // 2) * 7.0
    box(ax, x, y, 12.0, 4.6, "专家 %d" % (i + 1), fc=WHITE, ec=WARM, fs=6.6)
    line(ax, (66.0, 29.8), (x + 6.0, y + 4.8), color=GRAY, lw=0.6)

label(ax, 50, 5.0, "三种切法可以组合：TP 切一层，PP 切层，EP 切专家", fs=7.0, color=GRAY)
save(fig, "22/fig22_1.png")

# ---------------------------------------------------------------- 图 22-2
fig, ax = canvas(7.2, 2.9, 100)

box(ax, 2.0, 18.0, 14.0, 10.0, "请求\n路由", fc=GRAY_L, ec=GRAY, fs=6.8)
box(ax, 22.0, 22.0, 24.0, 12.0, "prefill 池\n算力优先", fc=ACCENT_L, ec=ACCENT, fs=7.2, bold=True)
box(ax, 22.0, 5.0, 24.0, 12.0, "decode 池\n显存优先", fc=GREEN_L, ec=GREEN, fs=7.2, bold=True)

arrow(ax, (16.4, 23.0), (21.6, 26.0), lw=0.9)
label(ax, 18.0, 25.2, "prompt", fs=6.0, color=GRAY)

arrow(ax, (34.0, 21.6), (34.0, 17.4), color=WARM, lw=1.2)
label(ax, 35.0, 19.4, "KV cache", fs=6.2, color=WARM, ha="left")

box(ax, 54.0, 12.0, 20.0, 10.0, "token 流", fc=WHITE, ec=INK, fs=6.8)
arrow(ax, (46.4, 11.0), (53.6, 15.5), lw=0.9)

label(ax, 50, 2.2, "两个池独立扩缩容；KV cache 的传输是分离式服务的主要成本", fs=7.0, color=GRAY)
save(fig, "22/fig22_2.png")
