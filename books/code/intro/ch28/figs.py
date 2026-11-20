# -*- coding: utf-8 -*-
"""第 28 章插图：全书技术地图（五层）。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, box, canvas, label, save)

fig, ax = canvas(7.2, 4.4, 100)

bands = [
    ("模型", "可能重训", WARM, WARM_L,
     ["剪枝 / 低秩", "蒸馏 / 替换", "注意力变体", "MoE", "扩散模型"]),
    ("计算图", "几乎无损", ACCENT, ACCENT_L,
     ["常量折叠", "死代码", "算子融合", "布局转换", "静态化"]),
    ("数值", "精度换成本", GREEN, GREEN_L,
     ["fp16 / bf16", "int8 / int4", "fp8", "fp4 / MX", "KV 量化"]),
    ("执行", "工程复杂", GRAY, GRAY_L,
     ["kernel", "显存规划", "CUDA Graph", "profiling", "推理引擎"]),
    ("系统", "调度与拓扑", ACCENT, ACCENT_L,
     ["批处理", "投机解码", "并行 / PD", "多 LoRA", "Agent / 长上下文"]),
]

for i, (name, cost, ec, fc, chips) in enumerate(bands):
    y = 50.0 - i * 10.2
    box(ax, 2.0, y, 14.0, 8.6, fc=fc, ec=ec)
    label(ax, 9.0, y + 5.8, name, fs=8.4, bold=True, color=ec)
    label(ax, 9.0, y + 2.6, cost, fs=5.6, color=GRAY)
    n = len(chips)
    cw = (82.0 - (n - 1) * 1.3) / n
    for j, chip in enumerate(chips):
        x = 17.5 + j * (cw + 1.3)
        box(ax, x, y + 0.6, cw, 7.4, chip, fc=WHITE, ec=GRAY, fs=6.2)

label(ax, 50, 2.4, "越往上越动模型本身，越往下越靠近硬件，系统层则决定请求怎么落到资源上",
      fs=7.0, color=GRAY)
save(fig, "28/fig28_1.png")
