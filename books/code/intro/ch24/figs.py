# -*- coding: utf-8 -*-
"""第 24 章插图：长上下文 KV cache 与多模态输入。"""

import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("intro")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      line, save)

# ---------------------------------------------------------------- 图 24-1
figstyle.setup()
fig = figstyle.plt.figure(figsize=(7.2, 2.8))
ax = fig.add_axes([0.10, 0.18, 0.86, 0.70])

lengths = np.array([4, 16, 32, 64, 128])
gb = lengths * 0.5
ax.plot(lengths, gb, color=ACCENT, lw=1.8, marker="o", ms=4)
for x, y in zip(lengths, gb):
    ax.annotate("%.0f GB" % y, xy=(x, y), xytext=(0, 7), textcoords="offset points",
                fontsize=6.5, color=GRAY, ha="center")

ax.set_xlabel("上下文长度（K token）", fontsize=7, color=GRAY)
ax.set_ylabel("KV cache（GB）", fontsize=7, color=GRAY)
ax.set_xscale("log", base=2)
ax.set_xticks(lengths)
ax.set_xticklabels([str(x) + "K" for x in lengths])
ax.set_ylim(0, 72)
ax.tick_params(labelsize=6.5, colors=GRAY)
for sp in ax.spines.values():
    sp.set_color(GRAY)
    sp.set_linewidth(0.6)

ax.text(6, 60, "7B 模型，32 层、32 头、头维 128、fp16\n每个 token 约 0.5 MB，按公式估算",
        fontsize=6.6, color=GRAY)
figstyle.save(fig, "24/fig24_1.png")

# ---------------------------------------------------------------- 图 24-2
fig, ax = canvas(7.2, 2.5, 100)

box(ax, 2.0, 15.0, 13.0, 10.0, "图像/视频\n音频", fc=GRAY_L, ec=GRAY, fs=6.6)
box(ax, 19.0, 15.0, 16.0, 10.0, "编码器\nViT / 音频", fc=WARM_L, ec=WARM, fs=6.6)
box(ax, 39.0, 15.0, 16.0, 10.0, "token 序列\n几百到几万", fc=ACCENT_L, ec=ACCENT, fs=6.2)
box(ax, 59.0, 15.0, 20.0, 10.0, "语言模型\nprefill + decode", fc=GREEN_L, ec=GREEN, fs=6.8, bold=True)
box(ax, 83.0, 15.0, 14.0, 10.0, "文本输出", fc=GRAY_L, ec=GRAY, fs=6.6)

for x1, x2 in ((15.4, 18.6), (35.4, 38.6), (55.4, 58.6), (79.4, 82.6)):
    arrow(ax, (x1, 20.0), (x2, 20.0), lw=0.9)

label(ax, 50, 8.0, "编码器可以独立部署，按图像/视频流量扩缩容；token 数决定 prefill 成本",
      fs=7.0, color=GRAY)
save(fig, "24/fig24_2.png")
