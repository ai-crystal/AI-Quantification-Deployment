# -*- coding: utf-8 -*-
"""第 4 章插图：量化粒度与量化算子的放置方式。"""

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

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK,
                      WARM, WARM_L, WHITE, arrow, box, canvas, label, line,
                      save)

# ---------------------------------------------------------------- 图 4-1
N = 8
CELL = 2.75


def draw(ax, x0, y0, mode, title, sub):
    for r in range(N):
        for c in range(N):
            if mode == "tensor":
                fc, ec, lw = ACCENT_L, ACCENT, 0.35
            elif mode == "channel":
                fc, ec, lw = (ACCENT_L if r % 2 == 0 else GREEN_L), ACCENT, 0.35
            else:
                b = r + c // 2
                fc, ec, lw = (ACCENT_L if b % 2 == 0 else GREEN_L), ACCENT, 0.35
            box(ax, x0 + c * CELL, y0 + (N - 1 - r) * CELL, CELL, CELL,
                fc=fc, ec=ec, lw=lw, radius=0.2)

    # 块边界
    if mode == "tensor":
        box(ax, x0, y0, N * CELL, N * CELL, fc="none", ec=ACCENT, lw=1.2, radius=0.3)
    elif mode == "channel":
        for r in range(N):
            box(ax, x0, y0 + (N - 1 - r) * CELL, N * CELL, CELL, fc="none",
                ec=ACCENT, lw=1.0, radius=0.3)
    else:
        for r in range(N):
            for g in range(4):
                box(ax, x0 + g * 2 * CELL, y0 + (N - 1 - r) * CELL, 2 * CELL, CELL,
                    fc="none", ec=ACCENT, lw=1.0, radius=0.3)

    label(ax, x0 + N * CELL / 2, y0 + N * CELL + 2.4, title, fs=8.0, bold=True)
    label(ax, x0 + N * CELL / 2, y0 - 2.6, sub, fs=7.0, color=GRAY)


fig, ax = canvas(7.4, 3.0, 100)

draw(ax, 2.0, 7.0, "tensor", "per-tensor", "一个 scale 管 64 个权重")
draw(ax, 37.5, 7.0, "channel", "per-channel", "一个 scale 管 8 个权重")
draw(ax, 73.0, 7.0, "group", "per-group（组大小 2）", "一个 scale 管 2 个权重")

label(ax, 2.0, 1.2, "每个小格是一个权重，行是输出通道，列是输入通道；框线内共用同一组 scale 与 zero point",
      fs=7.0, color=GRAY, ha="left")
save(fig, "04/fig04_1.png")

# ---------------------------------------------------------------- 图 4-2
fig, ax = canvas(7.4, 2.9, 100)

Y1, Y2, H = 20.5, 4.0, 8.5
BW = 13.0


def chain(y, items, x0=1.5, gap=2.0):
    xs = []
    x = x0
    for t1, t2, ec, fc in items:
        box(ax, x, y, BW, H, fc=fc, ec=ec, lw=0.9, radius=1.0)
        label(ax, x + BW / 2, y + H - 2.9, t1, fs=7.8, bold=True, color=ec)
        label(ax, x + BW / 2, y + 2.9, t2, fs=6.4, color=GRAY)
        xs.append(x)
        x += BW + gap
    for i in range(len(items) - 1):
        arrow(ax, (xs[i] + BW + 0.1, y + H / 2), (xs[i + 1] - 0.1, y + H / 2), lw=0.9)
    return xs, x - gap


label(ax, 1.5, 32.4, "显式 QDQ：量化点写在图上", fs=7.2, color=GRAY, ha="left")
xs, end = chain(Y1, [("输入", "fp32", GRAY, GRAY_L),
                     ("Q", "round + clamp", ACCENT, ACCENT_L),
                     ("卷积", "int8 × int8", ACCENT, ACCENT_L),
                     ("DQ", "× s_x · s_w", GREEN, GREEN_L),
                     ("输出", "fp32", GRAY, GRAY_L)])

box(ax, xs[1] - 1.2, Y1 - 1.5, xs[3] + BW - xs[1] + 2.4, H + 3.0,
    fc="none", ec=WARM, lw=0.8, radius=1.4)
label(ax, xs[1] + BW / 2, 17.2, "引擎把这三步折成一个算子", fs=6.8, color=WARM, ha="center")

label(ax, 1.5, Y2 + H + 2.2, "隐式量化：scale 挂在算子属性上", fs=7.2, color=GRAY, ha="left")
box(ax, 1.5, Y2, BW, H, fc=GRAY_L, ec=GRAY, lw=0.9, radius=1.0)
label(ax, 1.5 + BW / 2, Y2 + H - 2.9, "输入", fs=7.8, bold=True, color=GRAY)
label(ax, 1.5 + BW / 2, Y2 + 2.9, "int8 张量", fs=6.4, color=GRAY)
box(ax, 16.5, Y2, 26.0, H, fc=ACCENT_L, ec=ACCENT, lw=0.9, radius=1.0)
label(ax, 29.5, Y2 + H - 2.9, "卷积（带 scale）", fs=7.8, bold=True, color=ACCENT)
label(ax, 29.5, Y2 + 2.9, "s_x, s_w, z 存在算子属性里", fs=6.4, color=GRAY)
box(ax, 44.5, Y2, BW, H, fc=GRAY_L, ec=GRAY, lw=0.9, radius=1.0)
label(ax, 44.5 + BW / 2, Y2 + H - 2.9, "输出", fs=7.8, bold=True, color=GRAY)
label(ax, 44.5 + BW / 2, Y2 + 2.9, "int8 张量", fs=6.4, color=GRAY)
arrow(ax, (14.7, Y2 + H / 2), (16.3, Y2 + H / 2), lw=0.9)
arrow(ax, (42.7, Y2 + H / 2), (44.3, Y2 + H / 2), lw=0.9)

label(ax, 62.0, Y2 + H / 2, "图上没有额外的量化节点，\n反量化藏在相邻算子的收尾里", fs=6.8, color=GRAY, ha="left")
label(ax, 1.5, 1.0, "上图的 Q 与 DQ 若不被融合，每个都要真的走一遍内存；下图省掉的正是这一步",
      fs=6.8, color=GRAY, ha="left")
save(fig, "04/fig04_2.png")
