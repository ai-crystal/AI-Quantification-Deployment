# -*- coding: utf-8 -*-
"""第 2 章插图：仿射量化的格点映射与整数累加链路。"""

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

from figstyle import (ACCENT, ACCENT_L, GRAY, GREEN, GREEN_L, INK, RED, RED_L,
                      WARM, WARM_L, WHITE, arrow, box, brace, canvas, label,
                      line, save)

# ---------------------------------------------------------------- 图 2-1
fig, ax = canvas(7.4, 3.3, 100)

X0, X1 = 8.0, 92.0          # 实数轴的范围 -2.4 .. 2.4
VLO, VHI = -2.4, 2.4


def rx(v):
    return X0 + (v - VLO) / (VHI - VLO) * (X1 - X0)


def cx(q):
    return rx(-2.0) + q / 255.0 * (rx(2.0) - rx(-2.0))


Y_REAL = 27.0
Y_CODE = 9.0

# 码点轴
line(ax, (cx(0), Y_CODE), (cx(255), Y_CODE), color=INK, lw=1.0)
for q, txt in ((0, "0"), (64, "64"), (128, "128"), (192, "192"), (255, "255")):
    line(ax, (cx(q), Y_CODE), (cx(q), Y_CODE - 1.2), color=INK, lw=1.0)
    label(ax, cx(q), Y_CODE - 3.4, txt, fs=7.4)
label(ax, cx(255) + 1.4, Y_CODE + 3.0, "int8 码点", fs=7.6, color=GRAY, ha="left")

# 实数轴
line(ax, (X0, Y_REAL), (X1, Y_REAL), color=INK, lw=1.0)
for v in (-2, -1, 0, 1, 2):
    line(ax, (rx(v), Y_REAL), (rx(v), Y_REAL - 1.2), color=INK, lw=1.0)
    label(ax, rx(v), Y_REAL - 3.4, "%d" % v, fs=7.4)
label(ax, X1 + 1.4, Y_REAL + 3.0, "实数 x", fs=7.6, color=GRAY, ha="left")

# 饱和区
for a, b in ((X0, rx(-2.0)), (rx(2.0), X1)):
    box(ax, a, Y_REAL - 1.0, b - a, 2.0, fc=RED_L, ec=RED, lw=0.6, radius=0.3, zorder=1)
label(ax, (X0 + rx(-2.0)) / 2, Y_REAL + 3.4, "饱和", fs=7.2, color=RED)
label(ax, (rx(2.0) + X1) / 2, Y_REAL + 3.4, "饱和", fs=7.2, color=RED)

# 格点位置
for i in range(17):
    v = -2.0 + i * 0.25
    line(ax, (rx(v), Y_REAL + 0.2), (rx(v), Y_REAL + 1.5), color=ACCENT, lw=0.9)

brace(ax, rx(-0.125), rx(0.125), Y_REAL + 2.0, "档距 s", color=ACCENT, fs=7.4, height=1.8)

# 三个关键点的对应
for v, q in ((-2.0, 0), (0.0, 127.5), (2.0, 255)):
    line(ax, (rx(v), Y_REAL - 4.6), (cx(q), Y_CODE + 1.2), color=GRAY, lw=0.7, ls=(0, (3, 3)))

label(ax, 28.0, 21.0, "码点 0 对应 x_min", fs=7.2, color=GRAY, ha="center")
label(ax, 70.0, 21.0, "码点 255 对应 x_max", fs=7.2, color=GRAY, ha="center")
label(ax, 6.0, 3.0, "档距按 256 格点画稀了；实线两端之外的数值被截断到端点，补零要求 0 正好落在格点上",
      fs=7.2, color=GRAY, ha="left")
save(fig, "02/fig02_1.png")

# ---------------------------------------------------------------- 图 2-2
fig, ax = canvas(7.4, 2.05, 100)

BOXES = [
    ("输入", "int8 激活", GRAY, "#eef0f2"),
    ("乘法", "int8 × int8", ACCENT, ACCENT_L),
    ("累加", "int32 加法树", ACCENT, ACCENT_L),
    ("缩放", "× s_x · s_w", GREEN, GREEN_L),
    ("加偏置", "+ b（fp32）", GREEN, GREEN_L),
    ("重量化", "round + clamp", WARM, WARM_L),
]
X = [1.0, 17.2, 33.4, 49.6, 65.0, 80.4]
W = [13.4, 13.4, 13.4, 12.6, 12.6, 18.0]
Y, H = 14.5, 9.0

for (t1, t2, ec, fc), x, w in zip(BOXES, X, W):
    box(ax, x, Y, w, H, fc=fc, ec=ec, lw=0.9, radius=1.0)
    label(ax, x + w / 2, Y + H - 3.0, t1, fs=8.2, bold=True, color=ec)
    label(ax, x + w / 2, Y + 3.0, t2, fs=6.8, color=GRAY)

for i in range(len(BOXES) - 1):
    arrow(ax, (X[i] + W[i] + 0.2, Y + H / 2), (X[i + 1] - 0.2, Y + H / 2), lw=1.0)

label(ax, 40.1, 10.2, "同一通路内不做取整，K 项累加全靠 int32 撑住", fs=7.0, color=GRAY)
label(ax, 73.0, 10.2, "取整只发生最后一次", fs=7.0, color=GRAY)
label(ax, 1.0, 4.2, "int8 乘积上界 127 × 127 = 16129，int32 可容纳约 1.3e5 项最坏情形累加",
      fs=7.0, color=GRAY, ha="left")
save(fig, "02/fig02_2.png")
