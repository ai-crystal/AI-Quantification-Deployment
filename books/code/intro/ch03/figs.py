# -*- coding: utf-8 -*-
"""第 3 章插图：模型目录的内容与权重大小。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      line, save)

# ---------------------------------------------------------------- 图 3-1
fig, ax = canvas(7.2, 3.0, 100)

box(ax, 2.0, 18.0, 18.0, 8.0, "模型目录", fc=INK, ec=INK, color=WHITE, fs=9.0, bold=True)

items = [
    (33.0, "权重", "model.safetensors\n或 model.pth", ACCENT, ACCENT_L),
    (51.0, "配置", "config.json\n层数、维度、头数", GRAY, GRAY_L),
    (69.0, "分词器", "vocab、merges\n特殊 token", GREEN, GREEN_L),
    (87.0, "预处理", "均值、方差\n尺寸、色彩空间", WARM, WARM_L),
]
for x, name, sub, ec, fc in items:
    box(ax, x - 8.0, 18.0, 16.0, 8.0, name, fc=fc, ec=ec, fs=8.4, bold=True)
    label(ax, x, 12.4, sub, fs=6.8, color=GRAY)
    arrow(ax, (20.4, 22.0), (x - 8.4, 22.0), color=GRAY, lw=0.8)

box(ax, 2.0, 2.2, 28.0, 5.6, "图定义（可选）", fc=WHITE, ec=INK, fs=8.0)
label(ax, 32.0, 3.8, ".onnx / TorchScript / .engine，决定计算怎么表达", fs=7.2, ha="left", color=GRAY)
line(ax, (11.0, 17.6), (11.0, 8.2), color=GRAY, lw=0.8, ls=(0, (3, 3)))

label(ax, 50, 28.0, "推理只需要权重、配置和预处理；优化器状态、训练步数都不该带上",
      fs=7.6, color=GRAY)
save(fig, "03/fig03_1.png")

# ---------------------------------------------------------------- 图 3-2
fig, ax = canvas(7.2, 2.4, 100)

rows = [("fp32", 28.0, GRAY, GRAY_L), ("fp16", 14.0, ACCENT, ACCENT_L),
        ("int8", 7.0, GREEN, GREEN_L), ("int4", 3.5, WARM, WARM_L)]
x0 = 18.0
for i, (name, val, ec, fc) in enumerate(rows):
    y = 25.0 - i * 5.6
    label(ax, 15.0, y + 1.7, name, fs=8.0, ha="right", color=INK)
    w = 70.0 * val / 28.0
    box(ax, x0, y, w, 3.4, fc=fc, ec=ec)
    label(ax, x0 + w + 2.2, y + 1.7, "%.1f GB" % val, fs=7.6, ha="left", color=GRAY)

label(ax, 18.0, 2.2, "按 70 亿参数乘每参数字节数估算，不含对齐与额外缓冲", fs=7.4, color=GRAY)
save(fig, "03/fig03_2.png")
