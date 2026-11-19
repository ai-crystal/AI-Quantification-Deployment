# -*- coding: utf-8 -*-
"""第 3 章插图：roofline 与分块强度。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import numpy as np

import figstyle
figstyle.use_book("compute")
figstyle.setup()

from figstyle import ACCENT, GRAY, GREEN, INK, RED, WARM, box, canvas, label, save

import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, NullLocator

# ---------------------------------------------------------------- 图 3-1
BW = 2.0e12          # B/s
PEAK = 312.0e12      # FLOP/s
RIDGE = PEAK / BW

fig = plt.figure(figsize=(7.4, 3.9))
ax = fig.add_axes([0.10, 0.15, 0.86, 0.80])

x = np.logspace(-1.3, 3.6, 600)
y = np.minimum(PEAK, x * BW)
ax.plot(x, y / 1e12, color=INK, lw=1.6, zorder=3)

ax.axvline(RIDGE, color=GRAY, lw=0.8, ls=(0, (4, 3)), zorder=1)
ax.text(RIDGE * 1.15, 0.42, "拐点 156", fontsize=7.6, color=GRAY)

pts = [(0.167, "逐元素加法", (-6.0, 5.0), "right", "bottom"),
       (0.5, "LayerNorm", (-6.0, 5.0), "right", "bottom"),
       (1.0, "注意力解码", (7.0, -5.0), "left", "top"),
       (127.0, "1×1 卷积", (9.0, 11.0), "left", "bottom"),
       (683.0, "4096 矩阵乘", (0.0, 7.0), "center", "bottom")]

for i, (ii, name, off, ha, va) in enumerate(pts):
    ax.plot([ii], [min(PEAK, ii * BW) / 1e12], "o", ms=4.6, color=WARM,
            zorder=4, mec="white", mew=0.8)
    ax.annotate(name, (ii, min(PEAK, ii * BW) / 1e12), xytext=off,
                textcoords="offset points", fontsize=7.4, color=WARM,
                ha=ha, va=va)

ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(0.1, 4000)
ax.set_ylim(0.05, 1200)
ax.set_xlabel("算术强度（FLOP / Byte）", fontsize=8.2)
ax.set_ylabel("可达性能（TFLOPS）", fontsize=8.2)
ax.tick_params(labelsize=7.4, length=2.5, colors=GRAY)
ax.grid(True, which="major", color="#dcdcdc", lw=0.6, zorder=0)
ax.set_axisbelow(True)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
for s in ("left", "bottom"):
    ax.spines[s].set_color(GRAY)
    ax.spines[s].set_linewidth(0.8)

ax.text(0.12, 1000, "带宽斜线：性能 = 强度 × 2 TB/s", fontsize=7.4, color=GRAY)
ax.text(1500, 170, "算力平台：312 TFLOPS", fontsize=7.4, color=GRAY, ha="right")

save(fig, "03/fig03_1.png")

# ---------------------------------------------------------------- 图 3-2
fig = plt.figure(figsize=(7.4, 3.2))
ax = fig.add_axes([0.135, 0.17, 0.83, 0.78])

s = np.arange(16, 320, 2)
ax.plot(s, s / 4.0, color=ACCENT, lw=1.6, label="fp32，强度 = s / 4")
ax.plot(s, s / 2.0, color=GREEN, lw=1.6, label="fp16，强度 = s / 2")
ax.axhline(156, color=WARM, lw=0.9, ls=(0, (4, 3)))
ax.axhline(10, color=GRAY, lw=0.9, ls=(0, (4, 3)))
ax.text(196, 160, "fp16 拐点 156", fontsize=7.4, color=WARM, ha="right")
ax.text(95, 1.2, "fp32 拐点 10", fontsize=7.4, color=GRAY, ha="center", va="bottom")

ax.plot([128], [32], "o", ms=4.4, color=ACCENT, mec="white", mew=0.8, zorder=4)
ax.annotate("s = 128，强度 32", (128, 32), xytext=(6, -14), textcoords="offset points",
            fontsize=7.4, color=ACCENT)
ax.annotate("s = 256，强度 64", (256, 64), xytext=(-4, 8), textcoords="offset points",
            fontsize=7.4, color=GREEN, ha="right")

ax.set_xlim(0, 320)
ax.set_ylim(0, 180)
ax.set_xlabel("分块边长 s（Tm = Tn = s）", fontsize=8.2)
ax.set_ylabel("算术强度", fontsize=8.6, labelpad=7)
ax.tick_params(labelsize=7.4, length=2.5, colors=GRAY)
ax.grid(True, color="#dcdcdc", lw=0.6)
ax.set_axisbelow(True)
for sp in ("top", "right"):
    ax.spines[sp].set_visible(False)
for sp in ("left", "bottom"):
    ax.spines[sp].set_color(GRAY)
    ax.spines[sp].set_linewidth(0.8)
ax.legend(frameon=False, fontsize=7.6, loc="lower right", bbox_to_anchor=(1.0, 0.02))

save(fig, "03/fig03_2.png")
