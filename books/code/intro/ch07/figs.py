# -*- coding: utf-8 -*-
"""第 7 章插图：图清理前后，以及静态化的执行路径。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      line, save)

# ---------------------------------------------------------------- 图 7-1
fig, ax = canvas(7.2, 3.2, 100)

label(ax, 2.0, 40.0, "清理前", fs=8.4, ha="left", bold=True, color=GRAY)
items = [
    (2.0, "卷积", ACCENT_L, ACCENT, "-"),
    (17.0, "归一化", ACCENT_L, ACCENT, "-"),
    (32.0, "ReLU", GREEN_L, GREEN, "-"),
    (47.0, "dropout", WHITE, RED, "--"),
    (62.0, "残差相加", ACCENT_L, ACCENT, "-"),
]
for x, name, fc, ec, ls in items:
    box(ax, x, 29.0, 12.2, 6.2, name, fc=fc, ec=ec, fs=7.4, lw=1.0 if ls == "-" else 1.4)
    if ls == "--":
        label(ax, x + 6.1, 36.8, "推理时恒等", fs=6.2, color=RED)

# drop_path 分支
box(ax, 47.0, 19.0, 12.2, 5.0, "drop_path", fc=WHITE, ec=RED, fs=6.8)
line(ax, (53.1, 29.0), (53.1, 24.0), color=RED, lw=1.0, ls=(0, (3, 2)))
label(ax, 60.2, 21.5, "训练时随机跳过", fs=6.2, color=RED, ha="left")

# 位置编码重复
box(ax, 2.0, 19.0, 17.0, 5.0, "位置编码（每层重算）", fc=WHITE, ec=WARM, fs=6.4)
line(ax, (10.5, 24.0), (10.5, 28.6), color=WARM, lw=0.9, ls=(0, (3, 2)))

for x in (14.6, 29.6, 44.6, 59.6):
    arrow(ax, (x, 32.1), (x + 2.0, 32.1), lw=0.8)

label(ax, 2.0, 13.0, "清理后", fs=8.4, ha="left", bold=True, color=GRAY)
box(ax, 2.0, 2.4, 26.0, 7.0, "卷积 + 归一化 + ReLU", fc=ACCENT_L, ec=ACCENT, fs=7.6, bold=True)
box(ax, 33.0, 2.4, 14.0, 7.0, "残差相加", fc=ACCENT_L, ec=ACCENT, fs=7.2)
box(ax, 52.0, 2.4, 14.0, 7.0, "输出", fc=GRAY_L, ec=GRAY, fs=7.2)
arrow(ax, (28.4, 5.9), (32.6, 5.9), lw=0.9)
arrow(ax, (47.4, 5.9), (51.6, 5.9), lw=0.9)
label(ax, 70.0, 5.9, "位置编码表只算一次，dropout 与 drop_path 删除", fs=6.6, ha="left", color=GRAY)
save(fig, "07/fig07_1.png")

# ---------------------------------------------------------------- 图 7-2
fig, ax = canvas(7.2, 2.9, 100)

label(ax, 2.0, 36.0, "动态形状", fs=8.2, ha="left", bold=True, color=GRAY)
for k in range(3):
    x0 = 2.0 + k * 28.0
    box(ax, x0, 25.0, 7.4, 6.2, "请求", fc=GRAY_L, ec=GRAY, fs=6.4)
    box(ax, x0 + 9.0, 25.0, 7.4, 6.2, "分配", fc=WHITE, ec=INK, fs=6.2)
    box(ax, x0 + 18.0, 25.0, 7.4, 6.2, "选 kernel", fc=WHITE, ec=INK, fs=6.0)
    arrow(ax, (x0 + 7.4, 28.1), (x0 + 8.8, 28.1), lw=0.7)
    arrow(ax, (x0 + 16.4, 28.1), (x0 + 17.8, 28.1), lw=0.7)
label(ax, 90.0, 28.1, "每次重复", fs=6.4, color=GRAY, ha="left")

label(ax, 2.0, 19.0, "静态形状", fs=8.2, ha="left", bold=True, color=GRAY)
box(ax, 2.0, 8.0, 34.0, 7.0, "构建：排内存、选 kernel、录制执行图", fc=ACCENT_L, ec=ACCENT, fs=6.8)
box(ax, 40.0, 8.0, 17.0, 7.0, "运行时重放", fc=GREEN_L, ec=GREEN, fs=7.0, bold=True)
box(ax, 61.0, 8.0, 17.0, 7.0, "运行时重放", fc=GREEN_L, ec=GREEN, fs=7.0, bold=True)
box(ax, 82.0, 8.0, 15.0, 7.0, "运行时重放", fc=GREEN_L, ec=GREEN, fs=7.0, bold=True)
for x in (36.4, 57.4, 78.4):
    arrow(ax, (x, 11.5), (x + 3.2, 11.5), lw=0.8)
label(ax, 2.0, 3.4, "构建一次，之后只按固定形状重放；代价是形状变化时要重建", fs=7.0, color=GRAY)
save(fig, "07/fig07_2.png")
