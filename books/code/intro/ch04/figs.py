# -*- coding: utf-8 -*-
"""第 4 章插图：CPU/GPU 构造与 roofline 直觉。"""

import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      line, save)

# ---------------------------------------------------------------- 图 4-1
fig, ax = canvas(7.2, 3.0, 100)

# CPU
box(ax, 2.0, 8.0, 43.0, 32.0, fc="#fbfcfd", ec=GRAY)
label(ax, 23.5, 37.0, "CPU：少量强核心", fs=8.6, bold=True)
box(ax, 6.0, 26.0, 12.0, 6.0, "控制单元", fc=GRAY_L, ec=GRAY, fs=6.8)
for i in range(4):
    box(ax, 5.0 + i * 10.0, 17.0, 8.4, 6.5, "核", fc=ACCENT_L, ec=ACCENT, fs=6.8)
box(ax, 5.0, 11.0, 37.0, 4.2, "大容量缓存 L2 / L3", fc=WHITE, ec=GRAY, fs=6.6)
label(ax, 23.5, 4.6, "分支预测、乱序执行，擅长复杂逻辑", fs=6.8, color=GRAY)

# GPU
box(ax, 52.0, 8.0, 46.0, 32.0, fc="#fbfcfd", ec=GRAY)
label(ax, 75.0, 37.0, "GPU：大量小核心", fs=8.6, bold=True)
for i in range(4):
    box(ax, 55.0 + i * 10.4, 14.0, 9.2, 18.0, fc=WHITE, ec=GRAY, fs=5.8)
    label(ax, 59.6 + i * 10.4, 30.6, "SM", fs=6.0, color=GRAY)
    for r in range(3):
        for c in range(3):
            ax.add_patch(figstyle.Rectangle((56.2 + i * 10.4 + c * 2.6,
                                             17.0 + r * 3.0), 2.0, 2.2,
                                            facecolor=ACCENT_L, edgecolor=ACCENT,
                                            lw=0.4, zorder=3))
label(ax, 75.0, 10.6, "每个 SM 里几十个执行单元，按 warp 调度", fs=6.2, color=GRAY)
label(ax, 75.0, 4.6, "用线程切换隐藏延迟，擅长相同的大批量运算", fs=6.8, color=GRAY)

label(ax, 50, 43.5, "两条不同的路：一个把单件事做快，一个把很多件事一起做完",
      fs=7.6, color=GRAY)
save(fig, "04/fig04_1.png")

# ---------------------------------------------------------------- 图 4-2
fig, ax = canvas(7.2, 3.2, 100)
ax2 = fig.add_axes(ax.get_position(), frameon=False)
ax2.set_xlim(0, 100)
ax2.set_ylim(0, 44)
ax2.set_axis_off()

# 带宽斜线与算力平台
xs = np.linspace(8, 52, 100)
ax2.plot(xs, 4 + (xs - 8) * 0.78, color=ACCENT, lw=1.8)
ax2.plot([52, 94], [4 + 44 * 0.78, 4 + 44 * 0.78], color=ACCENT, lw=1.8)
ax2.plot([8, 8], [4, 40], color=GRAY, lw=0.9)
ax2.annotate("", xy=(94, 4), xytext=(8, 4),
             arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=0.9))

ax2.text(22, 5.4, "带宽限制区", fontsize=7.6, color=GRAY)
ax2.text(72, 33.8, "算力限制区", fontsize=7.6, color=GRAY)
ax2.text(50, 0.6, "算术强度（每读 1 字节做多少次运算）", fontsize=7.4, color=GRAY, ha="center")
ax2.text(2.0, 38.0, "可达性能", fontsize=7.4, color=GRAY, rotation=90, va="top")

pts = [(14, 8.7, "逐元素相加", 1.6, 5.4),
       (20, 13.4, "LayerNorm", 1.6, 5.0),
       (36, 25.8, "卷积", -1.2, 4.8),
       (62, 38.3, "GEMM", 0.0, -4.2)]
for x, y, name, dx, dy in pts:
    ax2.plot([x], [y], "o", ms=4.2, color=WARM, zorder=5)
    ax2.annotate(name, xy=(x, y), xytext=(x + dx, y + dy), fontsize=7.4,
                 color=WARM, ha="left" if dx > 0 else ("right" if dx < 0 else "center"))

save(fig, "04/fig04_2.png")
