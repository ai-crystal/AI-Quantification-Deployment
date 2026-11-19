# -*- coding: utf-8 -*-
"""第 1 章插图：一个 Transformer block 的图表示，几种中间表示的抽象层级。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("engine")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, brace, canvas,
                      label, line, save)

# ---------------------------------------------------------------- 图 1-1
fig, ax = canvas(7.4, 3.3, 100)

xs = [2.0, 18.7, 35.4, 52.1, 68.8, 85.5]
w, h, y0 = 10.0, 9.5, 28.0
names = ["输入 x", "LayerNorm", "QKV 线性", "注意力", "输出线性", "残差相加"]
subs = ["B×S×D", "", "三份输出", "S×S 打分", "", ""]
colors = [(GRAY_L, GRAY), (ACCENT_L, ACCENT), (ACCENT_L, ACCENT),
          (WARM_L, WARM), (ACCENT_L, ACCENT), (GREEN_L, GREEN)]

for i, (x, name, sub, (fc, ec)) in enumerate(zip(xs, names, subs, colors)):
    box(ax, x, y0, w, h, fc=fc, ec=ec, radius=1.0, lw=1.0)
    if sub:
        label(ax, x + w / 2, y0 + h * 0.66, name, fs=8.2, bold=True)
        label(ax, x + w / 2, y0 + h * 0.26, sub, fs=7.2, color=GRAY)
    else:
        label(ax, x + w / 2, y0 + h / 2, name, fs=8.2, bold=True)

tensors = ["x", "h1", "q k v", "a", "h2"]
for i, t in enumerate(tensors):
    arrow(ax, (xs[i] + w, y0 + h / 2), (xs[i + 1] - 0.3, y0 + h / 2), lw=1.0)
    label(ax, xs[i] + w + (xs[i + 1] - xs[i] - w) / 2, y0 + h / 2 + 1.7, t,
          fs=7.2, color=GRAY)

# 常量权重
box(ax, 35.4, 17.0, 10.0, 6.4, "W 常量", fc=WHITE, ec=WARM, fs=7.4,
    color=WARM, radius=0.9, lw=0.9)
arrow(ax, (40.4, 23.4), (40.4, 27.6), color=WARM, lw=0.9, ls=(0, (3, 2)))

# 残差支路
line(ax, (7.0, y0), (7.0, 8.5), color=GREEN, lw=1.0)
line(ax, (7.0, 8.5), (90.5, 8.5), color=GREEN, lw=1.0)
arrow(ax, (90.5, 8.5), (90.5, y0 - 0.3), color=GREEN, lw=1.0)
label(ax, 30.0, 9.7, "残差支路，张量与输入共享生命周期", fs=7.0, color=GREEN,
      ha="left")

brace(ax, 18.7, 95.5, 38.6, "重复 N 层，每层一套权重", color=GRAY, fs=7.6)

label(ax, 50, 3.0, "权重是常量节点，推理图里没有反向边", fs=7.6, color=GRAY)
save(fig, "01/fig01_1.png")

# ---------------------------------------------------------------- 图 1-2
fig, ax = canvas(7.4, 3.4, 100)

rows = [
    ("Torch FX", "记录 Python 调用序列", "只能做模式匹配", GRAY, GRAY_L),
    ("ONNX", "算子集语义固定", "单算子替换", ACCENT, ACCENT_L),
    ("StableHLO", "纯函数，形状显式", "子图任意重写", GREEN, GREEN_L),
    ("TensorRT", "层加候选 kernel", "按形状挑实现", WARM, WARM_L),
]

for i, (name, unit, free, ec, fc) in enumerate(rows):
    yy = 36.0 - i * 6.4
    box(ax, 8.0, yy, 22.0, 5.4, name, fc=fc, ec=ec, fs=8.6, bold=True)
    label(ax, 33.0, yy + 2.7, unit, fs=7.8, ha="left")
    label(ax, 64.0, yy + 2.7, free, fs=7.4, ha="left", color=GRAY)

arrow(ax, (4.0, 42.0), (4.0, 6.0), color=GRAY, lw=0.9)
ax.text(2.4, 24.0, "绑定硬件", rotation=90, ha="center", va="center",
        fontsize=7.2, color=GRAY)

box(ax, 8.0, 6.0, 88.0, 6.6, fc=WHITE, ec=RED, radius=1.0, lw=0.9)
label(ax, 10.0, 9.3, "MLIR", fs=8.6, bold=True, ha="left", color=RED)
label(ax, 22.0, 9.3, "不固定层级，方言决定这一层表示什么，下降就是换方言",
      fs=7.6, ha="left")

label(ax, 50, 2.4, "越往下能做的优化越具体，能移植的范围越小", fs=7.6,
      color=GRAY)
save(fig, "01/fig01_2.png")
