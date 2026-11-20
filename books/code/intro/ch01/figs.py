# -*- coding: utf-8 -*-
"""第 1 章插图：一次前向与部署的四个层面。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, brace, canvas,
                      label, line, save)

# ---------------------------------------------------------------- 图 1-1
fig, ax = canvas(7.4, 2.5, 100)

xs = [2.0, 16.4, 30.8, 45.2, 59.6, 74.0, 88.4]
names = ["输入", "卷积", "归一化", "激活", "池化", "残差块", "分类头"]
subs = ["224×224×3", "7×7，64", "批归一化", "ReLU", "3×3，步长 2", "四层卷积", "全连接"]
colors = [(GRAY_L, GRAY), (ACCENT_L, ACCENT), (ACCENT_L, ACCENT), (GREEN_L, GREEN),
          (ACCENT_L, ACCENT), (WARM_L, WARM), (GRAY_L, GRAY)]

for i, (x, name, sub, (fc, ec)) in enumerate(zip(xs, names, subs, colors)):
    w = 11.2
    box(ax, x, 10.0, w, 9.2, fc=fc, ec=ec)
    label(ax, x + w / 2, 16.2, name, fs=8.6, bold=True)
    label(ax, x + w / 2, 12.6, sub, fs=6.8, color=GRAY)
    if i:
        arrow(ax, (xs[i - 1] + 11.2, 14.6), (x - 0.4, 14.6), lw=0.9)

brace(ax, 74.2, 85.0, 20.2, "重复 16 次", color=GRAY, fs=7.6)
brace(ax, 88.6, 99.4, 20.2, "输出 1000 类分数", color=GRAY, fs=7.6)

label(ax, 50, 5.2, "推理只走这一条路；训练还要从右往左算梯度，并更新每个卷积核",
      fs=7.8, color=GRAY)
save(fig, "01/fig01_1.png")

# ---------------------------------------------------------------- 图 1-2
fig, ax = canvas(7.4, 4.2, 100)

rows = [
    ("模型", "剪枝　低秩分解　蒸馏", "可能要重新训练", WARM, WARM_L),
    ("计算图", "算子融合　常量折叠　死代码消除", "几乎不损失精度", ACCENT, ACCENT_L),
    ("数值", "fp16　bf16　fp8　int8　int4", "精度换带宽与算力", GREEN, GREEN_L),
    ("执行", "kernel　并行　内存布局　显存", "需要熟悉硬件", GRAY, GRAY_L),
    ("系统", "批处理　调度　缓存　服务", "请求与资源匹配", RED, RED_L),
]

for i, (name, techs, cost, ec, fc) in enumerate(rows):
    yy = 45.0 - i * 8.2
    box(ax, 2.0, yy, 12.0, 5.4, name, fc=fc, ec=ec, fs=9.0, bold=True)
    label(ax, 17.0, yy + 2.7, techs, fs=8.1, ha="left", color=INK)
    label(ax, 62.0, yy + 2.7, cost, fs=7.5, ha="left", color=GRAY)
    if i < 4:
        arrow(ax, (8.0, yy - 0.3), (8.0, yy - 1.8), color=GRAY, lw=0.8)

label(ax, 50, 8.0, "越往上越动模型本身，代价越高；越往下越靠近执行与调度，收益与复杂度一起变",
      fs=7.8, color=GRAY)
save(fig, "01/fig01_2.png")
