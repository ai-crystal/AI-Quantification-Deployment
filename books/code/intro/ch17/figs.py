# -*- coding: utf-8 -*-
"""第 17 章插图：请求生命周期与权重分块。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, Rectangle, arrow, box, canvas,
                      label, line, save)

# ---------------------------------------------------------------- 图 17-1
fig, ax = canvas(7.2, 2.9, 100)

nodes = [
    ("接入", "鉴权、限流", GRAY, GRAY_L),
    ("预处理", "分词、解码", ACCENT, ACCENT_L),
    ("队列", "排队、准入", WARM, WARM_L),
    ("调度", "组 batch", ACCENT, ACCENT_L),
    ("执行", "prefill / decode", GREEN, GREEN_L),
    ("返回", "流式输出", GRAY, GRAY_L),
]
for i, (name, sub, ec, fc) in enumerate(nodes):
    x = 2.0 + i * 16.2
    box(ax, x, 18.0, 14.0, 10.0, fc=fc, ec=ec)
    label(ax, x + 7.0, 24.2, name, fs=7.6, bold=True)
    label(ax, x + 7.0, 20.4, sub, fs=6.0, color=GRAY)
    if i < 5:
        arrow(ax, (x + 14.2, 23.0), (x + 15.8, 23.0), lw=0.8)

label(ax, 2.0, 33.0, "用户请求", fs=7.0, ha="left", color=GRAY)
label(ax, 98.0, 33.0, "token 流回用户", fs=7.0, ha="right", color=GRAY)
line(ax, (2.0, 31.0), (98.0, 31.0), color=GRAY, lw=0.6, ls=(0, (3, 3)))

# 资源条
box(ax, 2.0, 5.0, 56.0, 5.0, "CPU：接入、预处理、调度", fc=GRAY_L, ec=GRAY, fs=6.2)
box(ax, 61.0, 5.0, 37.0, 5.0, "GPU：执行与 KV cache", fc=GREEN_L, ec=GREEN, fs=6.2)
label(ax, 50, 12.6, "每一站都有自己的排队和超时；端到端延迟是各段之和，不是 GPU 时间", fs=7.0, color=GRAY)
save(fig, "17/fig17_1.png")

# ---------------------------------------------------------------- 图 17-2
fig, ax = canvas(7.2, 2.8, 100)

box(ax, 2.0, 8.0, 42.0, 26.0, fc="#fbfcfd", ec=GRAY)
label(ax, 23.0, 31.0, "主机内存 / 磁盘：完整权重", fs=7.4, bold=True)
for i in range(8):
    box(ax, 5.0 + i * 4.8, 14.0, 4.0, 5.0, "层\n%d" % (i + 1), fc=GRAY_L, ec=GRAY, fs=5.4)

box(ax, 55.0, 8.0, 42.0, 26.0, fc="#fbfcfd", ec=GRAY)
label(ax, 76.0, 31.0, "显存：只放当前需要的块", fs=7.4, bold=True)
for i in range(4):
    box(ax, 58.0 + i * 9.6, 14.0, 8.0, 8.0, "块 %d" % (i + 1), fc=ACCENT_L, ec=ACCENT, fs=6.0)

arrow(ax, (46.0, 24.0), (53.0, 24.0), color=WARM, lw=1.0)
arrow(ax, (53.0, 19.0), (46.0, 19.0), color=GRAY, lw=0.9)
label(ax, 49.5, 26.0, "换入", fs=6.0, color=WARM)
label(ax, 49.5, 16.8, "换出", fs=6.0, color=GRAY)

label(ax, 50, 3.0, "模型比显存大时，按层或按块换入换出；代价是 PCIe 传输，收益是能跑起来", fs=7.0, color=GRAY)
save(fig, "17/fig17_2.png")
