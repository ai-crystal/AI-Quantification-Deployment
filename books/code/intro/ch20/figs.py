# -*- coding: utf-8 -*-
"""第 20 章插图：全书技术地图。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      line, save)

fig, ax = canvas(7.2, 4.0, 100)

bands = [
    ("模型", "可能重训", WARM, WARM_L,
     ["剪枝", "低秩分解", "蒸馏", "结构替换"]),
    ("计算图", "几乎无损", ACCENT, ACCENT_L,
     ["常量折叠", "死代码消除", "算子融合", "布局转换", "静态化"]),
    ("数值", "精度换成本", GREEN, GREEN_L,
     ["fp16 / bf16", "int8", "int4", "fp8", "KV 量化"]),
    ("执行", "工程复杂", GRAY, GRAY_L,
     ["kernel", "显存规划", "批处理", "推理引擎"]),
]

for i, (name, cost, ec, fc, chips) in enumerate(bands):
    y = 37.0 - i * 9.6
    box(ax, 2.0, y, 14.0, 7.8, fc=fc, ec=ec)
    label(ax, 9.0, y + 5.2, name, fs=8.4, bold=True, color=ec)
    label(ax, 9.0, y + 2.4, cost, fs=5.8, color=GRAY)
    n = len(chips)
    cw = (82.0 - (n - 1) * 1.4) / n
    for j, chip in enumerate(chips):
        x = 17.5 + j * (cw + 1.4)
        box(ax, x, y + 0.6, cw, 6.6, chip, fc=WHITE, ec=GRAY, fs=6.0)

label(ax, 50, 2.0, "越往上越动模型本身，越往下越靠近硬件；每层都有对应的代价", fs=7.0, color=GRAY)
save(fig, "20/fig20_1.png")
