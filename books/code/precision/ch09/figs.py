# -*- coding: utf-8 -*-
"""第 9 章插图：SmoothQuant 的通道迁移与三种方法的作用位置。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("precision")

# 印刷时图会按版心缩到 0.83 倍，这里把字号整体放大，保证缩后仍可读
SCALE = 1.16
_orig_label = figstyle.label
_orig_box = figstyle.box


def _label(ax, x, y, text, fs=9.5, **kw):
    _orig_label(ax, x, y, text, fs=fs * SCALE, **kw)


def _box(ax, x, y, w, h, text="", fs=9.5, **kw):
    _orig_box(ax, x, y, w, h, text, fs=fs * SCALE, **kw)


figstyle.label = _label
figstyle.box = _box

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, dot,
                      label, line, save)

# ---------------------------------------------------------------- 图 9-1
N = 32
act_before = [1.0 + 0.25 * ((i * 5) % 3) for i in range(N)]
for i in (5, 13, 21, 29):
    act_before[i] = 20.0
act_after = [1.0 + 0.2 * ((i * 5) % 3) for i in range(N)]
wgt_after = [1.0 + 0.3 * ((i * 7) % 3) for i in range(N)]
for i in (5, 13, 21, 29):
    wgt_after[i] = 19.0

fig, ax = canvas(7.4, 3.2, 100)
X0, X1 = 20.0, 92.0
bw = (X1 - X0) / N * 0.66
ROWS = [(act_before, "迁移前　激活", ACCENT, ACCENT_L),
        (act_after, "迁移后　激活", GREEN, GREEN_L),
        (wgt_after, "迁移后　权重", WARM, WARM_L)]
Y = [31.0, 20.0, 9.0]
HMAX = 8.4
VMAX = 21.0

for (vals, name, ec, fc), y in zip(ROWS, Y):
    for i, v in enumerate(vals):
        x = X0 + (X1 - X0) * i / N + ((X1 - X0) / N - bw) / 2
        box(ax, x, y, bw, max(v / VMAX * HMAX, 0.5), fc=fc, ec=ec, lw=0.6, radius=0.25)
    label(ax, X0 - 1.6, y + 2.0, name, fs=7.2, color=ec, ha="right")
    line(ax, (X0, y), (X1, y), color="#1b1b1b", lw=0.8)

label(ax, 21.0, 2.4, "纵轴为各通道的绝对值最大值（构造数据），横轴为通道；四个尖峰通道在迁移后被压平，同一批权重行被等比放大",
      fs=7.0, color=GRAY, ha="left")
save(fig, "09/fig09_1.png")

# ---------------------------------------------------------------- 图 9-2
import matplotlib.pyplot as plt

fig, ax = canvas(7.4, 2.2, 100)

PANELS = [
    ("SmoothQuant", "act", "输入除以 diag(s)，权重乘上 diag(s)"),
    ("GPTQ", "col", "逐列量化，误差传给其余列"),
    ("AWQ", "sig", "逐通道按激活幅度放大显著列"),
]
PX = [2.0, 35.0, 68.0]
CY = 17.0

for (name, mode, note), x0 in zip(PANELS, PX):
    label(ax, x0, 27.0, name, fs=7.8, bold=True, color=INK, ha="left")
    box(ax, x0, CY - 3.0, 7.6, 6.0, fc=GRAY_L, ec=GRAY, lw=0.8, radius=0.8)
    label(ax, x0 + 3.8, CY, "X", fs=7.6)
    arrow(ax, (x0 + 7.6, CY), (x0 + 13.3, CY), lw=0.8)
    ax.add_patch(plt.Circle((x0 + 16.0, CY), 2.5, fill=False, ec=INK, lw=0.9))
    label(ax, x0 + 16.0, CY, "×", fs=8.4)
    arrow(ax, (x0 + 18.6, CY), (x0 + 29.0, CY), lw=0.8)
    label(ax, x0 + 29.4, CY, "Y", fs=7.6, ha="left")

    box(ax, x0 + 10.0, 5.2, 12.0, 6.4, fc=GRAY_L, ec=GRAY, lw=0.8, radius=0.8)
    label(ax, x0 + 16.0, 3.2, "W", fs=7.6, color=GRAY)
    arrow(ax, (x0 + 16.0, 11.7), (x0 + 16.0, 13.3), lw=0.8)

    if mode == "act":
        box(ax, x0 + 7.9, CY - 1.6, 4.2, 3.2, fc=ACCENT_L, ec=ACCENT, lw=0.8, radius=0.4)
        label(ax, x0 + 10.0, CY, "÷ s", fs=6.4, color=ACCENT)
        box(ax, x0 + 13.9, 11.8, 4.2, 2.2, fc=ACCENT_L, ec=ACCENT, lw=0.8, radius=0.4)
        label(ax, x0 + 16.0, 12.9, "× s", fs=6.4, color=ACCENT)
    elif mode == "col":
        for k in range(4):
            ax.plot([x0 + 12.0 + k * 2.4] * 2, [6.0, 10.9], color=WARM, lw=1.0, zorder=6)
    else:
        for k in range(4):
            ax.plot([x0 + 12.0 + k * 2.4] * 2, [6.0, 10.9], color=GREEN,
                    lw=3.0 if k == 1 else 0.8, zorder=6)

    label(ax, x0, 1.2, note, fs=6.6, color=GRAY, ha="left")

save(fig, "09/fig09_2.png")
