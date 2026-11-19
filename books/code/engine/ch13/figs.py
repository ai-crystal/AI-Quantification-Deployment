# -*- coding: utf-8 -*-
"""第 13 章插图：从训练产物到线上服务的流水线。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("engine")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      save)

fig, ax = canvas(7.4, 3.6, 100)

stages = [
    ("导出", "ONNX 或\n直接导引擎", GRAY_L, GRAY),
    ("优化", "折叠 融合\n形状专用化", ACCENT_L, ACCENT),
    ("量化", "校准 →\nQDQ / 隐式", GREEN_L, GREEN),
    ("构建", "engine\n或编译产物", WARM_L, WARM),
    ("发布", "灰度\n回滚", ACCENT_L, ACCENT),
]

BW, BH, Y = 17.0, 10.0, 26.0
xs = [2.0 + i * 19.4 for i in range(5)]
for i, (name, sub, fc, ec) in enumerate(stages):
    box(ax, xs[i], Y, BW, BH, fc=fc, ec=ec, radius=1.0)
    label(ax, xs[i] + BW / 2, Y + 6.8, name, fs=8.0, bold=True)
    label(ax, xs[i] + BW / 2, Y + 3.0, sub, fs=7.2, color=GRAY)
    if i:
        arrow(ax, (xs[i - 1] + BW, Y + BH / 2), (xs[i] - 0.4, Y + BH / 2), lw=0.9)

# 门禁
gates = [
    ("数值对齐", 1),
    ("任务指标", 2),
    ("性能基线", 3),
]
for text, i in gates:
    gx = xs[i - 1] + BW + 1.2
    ax.plot([gx, gx], [Y - 1.6, Y + BH + 1.6], color=RED, lw=0.8, ls=(0, (2, 2)))
    label(ax, gx, Y - 3.2, text, fs=7.1, color=RED)

label(ax, 2.0, 39.6, "每一道门禁不过就拦住，不往下走", fs=7.0, color=RED, ha="left")

# 底部：制品与版本
box(ax, 2.0, 8.0, 92.0, 6.6, fc=WHITE, ec=ACCENT, radius=0.8, lw=0.9)
label(ax, 4.0, 11.3, "一组制品", fs=7.0, bold=True, ha="left", color=ACCENT)
label(ax, 17.0, 11.3, "权重　engine　配置　预处理代码　服务代码　—— 同一个版本号，一起发布，一起回滚",
      fs=7.4, ha="left")

arrow(ax, (46.0, Y - 0.3), (46.0, 14.9), color=ACCENT, lw=0.9)

label(ax, 60.0, 3.6, "构建产物按“硬件型号 × 模型版本”归档", fs=7.0, color=GRAY)
save(fig, "13/fig13_1.png")
