# -*- coding: utf-8 -*-
"""第 8 章插图：延迟缩放的窗口与微缩放格式的布局。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("precision")

# 印刷时图会按版心缩到 0.83 倍，这里把字号整体放大，保证缩后仍可读
SCALE = 0.95
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

# ---------------------------------------------------------------- 图 8-1
AMAX = [2.1, 2.4, 2.2, 2.6, 3.1, 5.8, 2.9, 2.5, 2.7, 2.3, 2.6, 3.0]

fig, ax = canvas(7.4, 2.4, 100)
X0, X1 = 14.0, 92.0
Y0 = 11.5
HMAX = 13.0
VMAX = 6.4
n = len(AMAX)
slot = (X1 - X0) / n
bw = slot * 0.55


def hy(v):
    return Y0 + v / VMAX * HMAX


for i, v in enumerate(AMAX):
    x = X0 + i * slot + (slot - bw) / 2
    fc, ec = (WARM_L, WARM) if v > 5 else (ACCENT_L, ACCENT)
    box(ax, x, Y0, bw, hy(v) - Y0, fc=fc, ec=ec, lw=0.7, radius=0.3)
    label(ax, x + bw / 2, Y0 - 2.2, "%d" % (i + 1), fs=6.6, color=GRAY)

line(ax, (X0, Y0), (X1, Y0), color=INK, lw=0.9)

# 窗口：突增之前的那几步
w0 = X0
w1 = X0 + 5 * slot
box(ax, w0, Y0 - 0.2, w1 - w0, 2.4, fc="none", ec=GREEN, lw=0.9, radius=0.6)
label(ax, (w0 + w1) / 2, Y0 - 4.6, "第 6 步的 s 取自这个窗口", fs=7.0, color=GREEN)

label(ax, X0 + 5.4 * slot, hy(5.8) + 1.4, "第 6 步突增，s 要等它进入下一轮窗口才跟上",
      fs=7.0, color=WARM)

label(ax, X0, 27.0, "每步的最大幅度", fs=7.2, color=GRAY, ha="left")
label(ax, X0, 1.8, "横轴为训练或推理的步数；当前步的缩放因子由窗口内的最大值决定，省掉当前步的全量扫描",
      fs=7.0, color=GRAY, ha="left")
save(fig, "08/fig08_1.png")

# ---------------------------------------------------------------- 图 8-2
fig, ax = canvas(7.4, 3.1, 100)

CW = 0.54      # 一个 4 位元素格
CH = 4.4
XSTART = 14.0


def strip(y, x, ncell, fc, ec):
    for i in range(ncell):
        box(ax, x + i * CW, y, CW, CH, fc=fc, ec=ec, lw=0.35, radius=0.1)


def sc(y, x, bits):
    w = bits * CW / 4.0
    box(ax, x, y, w, CH, fc=WARM_L, ec=WARM, lw=0.6, radius=0.2)
    if w > 3.2:
        label(ax, x + w / 2, y + CH / 2, "s", fs=7.0, color=WARM)
    return w


rows = [
    ("int4 分组，128 个元素共用一个 fp16 scale", [("s", 16), ("e", 128)]),
    ("MX，每 32 个元素一个 E8M0 共享指数", [("s", 8), ("e", 32)] * 4),
    ("NVFP4，每 16 个元素一个 E4M3 scale", [("s", 8), ("e", 16)] * 8),
]
Y = [33.6, 23.6, 13.6]
ends = []

for (cap, items), y in zip(rows, Y):
    x = XSTART
    for kind, val in items:
        if kind == "s":
            x += sc(y, x, val)
        else:
            strip(y, x, val, ACCENT_L, ACCENT)
            x += val * CW
    ends.append(x)

for (cap, _), y in zip(rows, Y):
    label(ax, XSTART, y + CH + 1.9, cap, fs=7.0, color=GRAY, ha="left")

label(ax, XSTART - 2.0, 8.4, "每行都是 128 个元素，一格 4 位，暖色格是缩放因子并按位数等宽；行长差就是元数据开销",
      fs=7.0, color=GRAY, ha="left")
label(ax, XSTART - 2.0, 4.4, "int4 与 MX 的行长只差一格，NVFP4 长出约一成，换来块内动态范围宽得多",
      fs=7.0, color=GRAY, ha="left")
save(fig, "08/fig08_2.png")
