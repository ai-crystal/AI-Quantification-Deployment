# -*- coding: utf-8 -*-
"""第 10 章插图：KV cache 的显存曲线与量化切分。"""

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
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      line, save)

# ---------------------------------------------------------------- 图 10-1
L, H, D = 32, 32, 128
MB_PER_TOKEN = 2 * L * H * D * 2 / 1e6       # fp16，单位 MB

fig, ax = canvas(7.4, 3.0, 100)
X0, X1 = 16.0, 88.0
Y0, Y1 = 8.0, 32.0
TMAX = 65536.0
GMAX = 40.0


def px(t):
    return X0 + t / TMAX * (X1 - X0)


def py(g):
    return Y0 + g / GMAX * (Y1 - Y0)


line(ax, (X0, Y0), (X1, Y0), color=INK, lw=0.9)
line(ax, (X0, Y0), (X0, Y1 + 1.0), color=INK, lw=0.9)
for t in (0, 16384, 32768, 49152, 65536):
    line(ax, (px(t), Y0), (px(t), Y0 - 0.9), color=INK, lw=0.8)
    label(ax, px(t), Y0 - 2.6, "%dK" % (t // 1024), fs=7.0)
for g in (0, 10, 20, 30, 40):
    line(ax, (X0, py(g)), (X0 - 0.9, py(g)), color=INK, lw=0.8)
    label(ax, X0 - 1.8, py(g), "%d" % g, fs=7.0, ha="right")

label(ax, X1 + 0.8, Y1 + 0.6, "GB", fs=7.0, color=GRAY, ha="left")
label(ax, X1, Y0 - 5.2, "上下文长度", fs=7.0, color=GRAY, ha="right")

SERIES = [
    (MB_PER_TOKEN, ACCENT, "KV　fp16"),
    (MB_PER_TOKEN / 2, GREEN, "KV　int8"),
]
for mb, col, name in SERIES:
    ax.plot([px(0), px(TMAX)], [py(0), py(mb * TMAX / 1000)],
            color=col, lw=1.4, zorder=3)
    label(ax, px(TMAX) - 1.0, py(mb * TMAX / 1000) + 1.4, name, fs=7.0,
          color=col, ha="right")

line(ax, (X0, py(14)), (X1, py(14)), color=GRAY, lw=1.0, ls=(0, (5, 3)))
label(ax, X0 + 2.0, py(14) + 1.3, "权重 fp16　14 GB", fs=7.0, color=GRAY, ha="left")

for t, mb, col in ((32768, MB_PER_TOKEN, ACCENT), (32768, MB_PER_TOKEN / 2, GREEN)):
    ax.plot([px(t)], [py(mb * t / 1000)], marker="o", ms=3.4, color=col, zorder=4)
    label(ax, px(t) - 1.2, py(mb * t / 1000) - 3.4, "%.1f" % (mb * t / 1000),
          fs=6.8, color=col, ha="right")

label(ax, X0, 0.6, "按公式 2 × 层数 × KV 头数 × 头维 × 序列长 × 字节数 计算，7B 模型，32 层、32 头、头维 128",
      fs=6.8, color=GRAY, ha="left")
save(fig, "10/fig10_1.png")

# ---------------------------------------------------------------- 图 10-2
fig, ax = canvas(7.4, 2.9, 100)

CELL = 2.4
ROWS, COLS = 8, 12


def matrix(x0, y0, hot_cols, base, hot):
    for r in range(ROWS):
        for c in range(COLS):
            v = hot if c in hot_cols else base
            box(ax, x0 + c * CELL, y0 + (ROWS - 1 - r) * CELL, CELL, CELL,
                fc=v, ec=ACCENT, lw=0.3, radius=0.15)


# 左：K，按通道切
KX, KY = 6.0, 8.0
matrix(KX, KY, {2, 7}, ACCENT_L, "#9fc2da")
for c in (2, 7):
    box(ax, KX + c * CELL, KY, CELL, ROWS * CELL, fc="none", ec=RED, lw=1.3, radius=0.2)
label(ax, KX + COLS * CELL / 2, KY + ROWS * CELL + 2.2, "K：离群值集中在少数通道", fs=7.2, bold=True)
label(ax, KX + COLS * CELL / 2, KY - 2.6, "按通道切，每列一个 scale", fs=7.0, color=GRAY)

# 右：V，按 token 切
VX, VY = 56.0, 8.0
for r in range(ROWS):
    for c in range(COLS):
        fc = ACCENT_L if r % 2 == 0 else "#cfdfe9"
        ec = GREEN if r in (2, 5) else ACCENT
        box(ax, VX + c * CELL, VY + (ROWS - 1 - r) * CELL, CELL, CELL,
            fc=fc, ec=ec, lw=1.1 if r in (2, 5) else 0.3, radius=0.15)
label(ax, VX + COLS * CELL / 2, VY + ROWS * CELL + 2.2, "V：各 token 幅度差异大", fs=7.2, bold=True)
label(ax, VX + COLS * CELL / 2, VY - 2.6, "按 token 切，每行一个 scale", fs=7.0, color=GRAY)

label(ax, 4.0, 1.6, "矩阵的一行是一个 token、一列是一个头维；红色框是离群通道，绿色框是幅度偏大的 token",
      fs=6.8, color=GRAY, ha="left")
save(fig, "10/fig10_2.png")
