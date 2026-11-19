# -*- coding: utf-8 -*-
"""第 12 章插图：NCHW 与 NHWC 的访存模式。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("compute")

from matplotlib.patches import Rectangle

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK,
                      WARM, WARM_L, WHITE, arrow, box, canvas, label, line,
                      note, save)

# ---------------------------------------------------------------- 图 12-1
fig, ax = canvas(7.4, 3.4, 100)

# 上：NCHW
label(ax, 4.0, 43.4, "NCHW", fs=8.6, bold=True, ha="left")
label(ax, 4.0, 40.4, "同一像素的 8 个通道分散在 8 张特征图上，步长 H × W × 4 字节", fs=7.2, color=GRAY, ha="left")

for c in range(8):
    x = 6.0 + c * 11.2
    box(ax, x, 27.0, 9.4, 9.0, "C%d" % c, fc=GRAY_L, ec=GRAY, fs=6.6, lw=0.6)
    ax.add_patch(Rectangle((x + 1.0, 30.8), 7.4, 1.4, facecolor=ACCENT, edgecolor="none", zorder=4))

label(ax, 6.0, 23.4, "8 个请求，落在 8 条不同的缓存行上", fs=7.2, color=WARM, ha="left")

# 下：NHWC
label(ax, 4.0, 17.6, "NHWC", fs=8.6, bold=True, ha="left")
label(ax, 4.0, 14.6, "同一像素的 8 个通道连续存放，步长 4 字节", fs=7.2, color=GRAY, ha="left")

for c in range(8):
    x = 6.0 + c * 6.8
    box(ax, x, 3.6, 6.0, 8.0, "C%d" % c, fc=GREEN_L, ec=GREEN, fs=6.4, lw=0.6)
line(ax, (6.0, 2.8), (6.0 + 8 * 6.8 - 0.8, 2.8), color=GREEN, lw=1.0)
label(ax, 6.0 + 4 * 6.8, 0.4, "128 字节，一条缓存行，一个请求", fs=7.2, color=GREEN)

save(fig, "12/fig12_1.png")
