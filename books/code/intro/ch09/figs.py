# -*- coding: utf-8 -*-
"""第 9 章插图：推理引擎的四个阶段。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      line, save)

fig, ax = canvas(7.2, 2.9, 100)

label(ax, 2.0, 39.0, "构建或加载阶段", fs=8.2, ha="left", bold=True, color=GRAY)
names = ["读图", "图优化", "做计划", "生成引擎"]
subs = ["解析节点与张量", "折叠、消除、融合", "选 kernel、排内存", "序列化或缓存"]
for i, (name, sub) in enumerate(zip(names, subs)):
    x = 3.0 + i * 23.0
    box(ax, x, 26.0, 19.0, 9.0, fc=ACCENT_L, ec=ACCENT)
    label(ax, x + 9.5, 32.2, name, fs=8.2, bold=True)
    label(ax, x + 9.5, 28.6, sub, fs=6.2, color=GRAY)
    if i < 3:
        arrow(ax, (x + 19.4, 30.5), (x + 22.6, 30.5), lw=0.9)

label(ax, 2.0, 20.0, "运行阶段", fs=8.2, ha="left", bold=True, color=GRAY)
box(ax, 3.0, 8.0, 14.0, 7.0, "输入", fc=GRAY_L, ec=GRAY, fs=7.4)
box(ax, 21.0, 8.0, 34.0, 7.0, "按计划执行 kernel", fc=GREEN_L, ec=GREEN, fs=7.4, bold=True)
box(ax, 59.0, 8.0, 14.0, 7.0, "输出", fc=GRAY_L, ec=GRAY, fs=7.4)
arrow(ax, (17.4, 11.5), (20.6, 11.5), lw=0.9)
arrow(ax, (55.4, 11.5), (58.6, 11.5), lw=0.9)
arrow(ax, (78.0, 26.0), (78.0, 15.4), color=ACCENT, lw=1.0)
label(ax, 79.6, 19.0, "引擎文件\n或缓存", fs=6.4, ha="left", color=ACCENT)

label(ax, 50, 2.6, "前三个阶段可以放在部署前，也可以推迟到第一次推理；放得越早，运行时越稳，灵活性越差",
      fs=7.2, color=GRAY)
save(fig, "09/fig09_1.png")
