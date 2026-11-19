# -*- coding: utf-8 -*-
"""第 8 章插图：注意力的访存路径与 online softmax。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("compute")

from matplotlib.patches import Rectangle

T1 = "片上：" + chr(10) + "S 块 128×128" + chr(10) + "m、l、O" + chr(10) + "归约后写 O"

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK,
                      RED, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      line, note, save)

# ---------------------------------------------------------------- 图 8-1
fig, ax = canvas(7.4, 4.2, 100)

# 左：标准
label(ax, 4.0, 54.0, "标准三步", fs=8.4, bold=True, ha="left")
box(ax, 2.5, 4.0, 44.0, 46.0, fc=WHITE, ec=GRAY_L, lw=0.9, radius=1.4)
label(ax, 24.5, 47.0, "每一步都把中间结果写回显存", fs=7.0, color=GRAY)

steps = [("S = QK^T", 38.0), ("softmax → P", 28.0), ("O = PV", 18.0)]
for nm, y in steps:
    box(ax, 6.0, y, 16.0, 6.4, nm, fc=ACCENT_L, ec=ACCENT, fs=7.2, lw=0.8)
box(ax, 28.0, 18.0, 14.0, 26.4, "S / P\nN×N\nfp16", fc=WARM_L, ec=WARM, fs=7.2, lw=0.9)
for nm, y in steps:
    arrow(ax, (22.4, y + 3.2), (27.6, y + 3.2), lw=0.9, color=GRAY)
arrow(ax, (28.0, 31.0), (22.0, 31.0), lw=0.9, color=GRAY, ls=(0, (3, 2)))
label(ax, 25.0, 33.6, "再读", fs=6.6, color=GRAY)

label(ax, 24.5, 9.0, "搬运量约 33 MB（2048 序列）", fs=7.2, color=GRAY)
label(ax, 24.5, 5.6, "峰值显存 8 MB / 头", fs=7.2, color=GRAY)

# 右：Flash
label(ax, 54.0, 54.0, "FlashAttention", fs=8.4, bold=True, ha="left")
box(ax, 52.5, 4.0, 45.0, 46.0, fc=WHITE, ec=GREEN_L, lw=0.9, radius=1.4)

box(ax, 56.0, 34.0, 16.0, 6.4, "读 Q 块", fc=GRAY_L, ec=GRAY, fs=7.2, lw=0.8)
box(ax, 56.0, 24.0, 16.0, 6.4, "读 K、V 块", fc=GRAY_L, ec=GRAY, fs=7.2, lw=0.8)
box(ax, 76.0, 24.0, 18.0, 16.4, T1, fc=GREEN_L, ec=GREEN, fs=7.0, lw=0.9)
arrow(ax, (72.4, 37.2), (75.6, 37.2), lw=0.9, color=GRAY)
arrow(ax, (72.4, 27.2), (75.6, 27.2), lw=0.9, color=GRAY)

label(ax, 57.0, 14.0, "沿 K 方向循环，S 块不落显存", fs=7.0, color=GRAY, ha="left")
label(ax, 74.5, 9.0, "搬运量约 8 MB，显存占用不到 1 MB", fs=7.2, color=GRAY)
label(ax, 74.5, 5.6, "只多了一次缩放和归约", fs=7.2, color=GRAY)

save(fig, "08/fig08_1.png")

# ---------------------------------------------------------------- 图 8-2
fig, ax = canvas(7.4, 3.2, 100)

label(ax, 4.0, 42.0, "沿 K 方向逐块处理，每块都更新三个量", fs=8.2, bold=True, ha="left")

# 三块
blocks = [("块 1", 6.0), ("块 2", 30.0), ("块 3", 54.0)]
for nm, x in blocks:
    box(ax, x, 27.0, 20.0, 8.4, nm + "\nS 片段", fc=ACCENT_L, ec=ACCENT, fs=7.2, lw=0.8)
    arrow(ax, (x + 20.4, 31.2), (x + 23.4, 31.2), lw=0.9, color=GRAY)

box(ax, 78.0, 27.0, 18.0, 8.4, "S 不写回\n显存", fc=WHITE, ec=GRAY, fs=7.2, lw=0.8, color=GRAY)

# 状态更新
label(ax, 4.0, 21.0, "每块之后", fs=7.4, color=GRAY, ha="left")
states = [("m ← max(m, max s)", 6.0), ("l ← e^(m旧−m新)·l + Σe^(s−m新)", 38.0),
          ("O ← e^(m旧−m新)·O + e^(s−m新)·V", 6.0)]
box(ax, 6.0, 13.4, 30.0, 5.6, "m ← max(m, max s)", fc=WARM_L, ec=WARM, fs=7.0, lw=0.8)
box(ax, 38.0, 13.4, 54.0, 5.6, "l ← e^(m旧 − m新)·l + Σ e^(s − m新)", fc=WARM_L, ec=WARM, fs=7.0, lw=0.8)
box(ax, 6.0, 6.0, 54.0, 5.6, "O ← e^(m旧 − m新)·O + e^(s − m新)·V", fc=WARM_L, ec=WARM, fs=7.0, lw=0.8)
box(ax, 63.0, 6.0, 29.0, 5.6, "最后 O / l", fc=GREEN_L, ec=GREEN, fs=7.2, lw=0.8)

label(ax, 50.0, 1.6, "缩放因子每块不同，靠最后一除归一化", fs=7.2, color=GRAY)

save(fig, "08/fig08_2.png")
