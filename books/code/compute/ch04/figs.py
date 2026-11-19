# -*- coding: utf-8 -*-
"""第 4 章插图：MMA 数据流与浮点格式位宽。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("compute")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK,
                      WARM, WARM_L, WHITE, arrow, box, canvas, label, line,
                      note, save)

# ---------------------------------------------------------------- 图 4-1
fig, ax = canvas(7.4, 4.0, 100)

# A 片段 16x16
x0, y0, cw, ch = 5.0, 28.0, 1.25, 1.25
from matplotlib.patches import Rectangle

for i in range(16):
    for j in range(16):
        ax.add_patch(Rectangle((x0 + j * cw, y0 + i * ch), cw, ch,
                               facecolor=ACCENT_L, edgecolor=ACCENT, lw=0.25, zorder=2))
label(ax, x0 + 8 * cw, y0 + 16 * ch + 2.4, "A 片段 16×16", fs=8.0, bold=True)

# B 片段 16x8
bx, by = 15.0, 4.0
for i in range(16):
    for j in range(8):
        ax.add_patch(Rectangle((bx + j * cw, by + i * ch), cw, ch,
                               facecolor=GREEN_L, edgecolor=GREEN, lw=0.25, zorder=2))
label(ax, bx + 4 * cw, by + 16 * ch + 2.4, "B 片段 16×8", fs=8.0, bold=True)

# 中间 warp
box(ax, 34.0, 8.0, 32.0, 32.0, fc=WHITE, ec=INK, lw=1.1, radius=1.4)
label(ax, 50.0, 37.2, "一个 warp，32 个线程", fs=8.2, bold=True)

frags = [("A 片段　每线程 8 个", ACCENT_L, ACCENT),
         ("B 片段　每线程 4 个", GREEN_L, GREEN),
         ("C 累加器　每线程 4 个", WARM_L, WARM)]
for k, (txt, fc, ec) in enumerate(frags):
    box(ax, 36.0, 27.6 - k * 6.4, 28.0, 4.8, txt, fc=fc, ec=ec, fs=7.2, lw=0.8)
label(ax, 50.0, 9.6, "一条指令 2048 次乘加", fs=7.4, color=GRAY)

# C 片段 16x8
cx, cy = 74.0, 14.0
for i in range(16):
    for j in range(8):
        ax.add_patch(Rectangle((cx + j * cw, cy + i * ch), cw, ch,
                               facecolor=WARM_L, edgecolor=WARM, lw=0.25, zorder=2))
label(ax, cx + 4 * cw, cy + 16 * ch + 2.2, "C 16×8，fp32", fs=8.0, bold=True)

arrow(ax, (x0 + 16 * cw + 0.6, y0 + 8 * ch), (33.4, 32.0), lw=1.0, color=ACCENT)
arrow(ax, (bx + 8 * cw + 0.6, by + 8 * ch), (33.4, 13.0), lw=1.0, color=GREEN)
arrow(ax, (66.6, 24.0), (cx - 0.8, 24.0), lw=1.0, color=WARM)
label(ax, 70.4, 26.0, "累加", fs=7.2, color=WARM)

label(ax, 50.0, 1.4, "A 与 B 来自共享内存，C 全程留在寄存器里，K 方向循环累加",
      fs=7.2, color=GRAY)

save(fig, "04/fig04_1.png")

# ---------------------------------------------------------------- 图 4-2
fig, ax = canvas(7.4, 3.0, 100)

rows = [("fp32", 1, 8, 23, 1.55),
        ("tf32", 1, 8, 10, 1.55),
        ("fp16", 1, 5, 10, 1.55),
        ("bf16", 1, 8, 7, 1.55),
        ("fp8 e4m3", 1, 4, 3, 1.55),
        ("fp8 e5m2", 1, 5, 2, 1.55)]

unit = 1.55
x0 = 21.0
colors = {"s": INK, "e": ACCENT, "m": WARM}

for k, (name, s, e, m, u) in enumerate(rows):
    y = 33.2 - k * 5.4
    label(ax, 18.6, y + 2.2, name, fs=7.8, ha="right")
    x = x0
    for width, key, txt in ((s, "s", ""), (e, "e", str(e)), (m, "m", str(m))):
        w = width * unit
        fc = ACCENT_L if key == "e" else (WARM_L if key == "m" else GRAY)
        box(ax, x, y, w, 4.4, txt, fc=fc, ec=colors[key], fs=6.2, lw=0.7, radius=0.3)
        x += w
    label(ax, x + 1.6, y + 2.2, "%d 位" % (s + e + m), fs=6.8, color=GRAY, ha="left")

# 图例
lx = 21.0
for key, txt, fc in (("s", "符号 1 位", GRAY), ("e", "指数", ACCENT_L), ("m", "尾数", WARM_L)):
    box(ax, lx, 1.4, 3.4, 3.0, "", fc=fc, ec=colors[key], lw=0.7, radius=0.3)
    label(ax, lx + 4.4, 2.9, txt, fs=7.0, color=GRAY, ha="left")
    lx += 18.0

save(fig, "04/fig04_2.png")
