# -*- coding: utf-8 -*-
"""第 3 章插图：量化误差的形状与离群值对档距的影响。"""

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

from figstyle import (ACCENT, ACCENT_L, GRAY, GREEN, INK, RED, RED_L, WARM,
                      WARM_L, WHITE, arrow, box, canvas, label, line, save)

# ---------------------------------------------------------------- 图 3-1
S = 0.25          # 档距
R = 1.0           # 量化区间 [-1, 1]

fig, ax = canvas(7.4, 2.7, 100)

X0, X1 = 14.0, 90.0
VLO, VHI = -1.5, 1.5
Y0, Y1 = 9.0, 27.0
ELO, EHI = -0.34, 0.34


def px(v):
    return X0 + (v - VLO) / (VHI - VLO) * (X1 - X0)


def py(e):
    return Y0 + (e - ELO) / (EHI - ELO) * (Y1 - Y0)


def rnd(v):
    return round(v / S) * S


def trc(v):
    return int(v / S) * S


xs = [VLO + i * 0.002 for i in range(int((VHI - VLO) / 0.002) + 1)]
for fn, col, lw in ((rnd, ACCENT, 1.1), (trc, WARM, 1.1)):
    pts = []
    for v in xs:
        q = fn(max(min(v, R), -R))
        e = v - q
        pts.append((px(v), py(e)))
    ax.plot([p[0] for p in pts], [p[1] for p in pts], color=col, lw=lw,
            solid_joinstyle="miter", zorder=3)

# 饱和区
for a, b in ((X0, px(-R)), (px(R), X1)):
    box(ax, a, Y0, b - a, Y1 - Y0, fc=RED_L, ec="none", radius=0.0, zorder=1)
for xv in (px(-R), px(R)):
    line(ax, (xv, Y0), (xv, Y1 + 0.6), color=RED, lw=0.8, ls=(0, (3, 2)), zorder=2)

line(ax, (X0, py(0)), (X1, py(0)), color=INK, lw=0.8, zorder=2)
line(ax, (X0, Y0 - 1.4), (X1, Y0 - 1.4), color=INK, lw=0.9)
for v, t in ((-1.0, "-1"), (0.0, "0"), (1.0, "1"), (-1.5, "-1.5"), (1.5, "1.5")):
    line(ax, (px(v), Y0 - 1.4), (px(v), Y0 - 2.3), color=INK, lw=0.9)
    label(ax, px(v), Y0 - 4.2, t, fs=7.2)
label(ax, (X0 + px(-R)) / 2, Y1 - 2.2, "饱和区", fs=7.2, color=RED)
label(ax, (px(R) + X1) / 2, Y1 - 2.2, "饱和区", fs=7.2, color=RED)
label(ax, px(1.22), py(-0.22), "饱和误差\n随超出量线性增长", fs=6.8, color=RED, ha="center")

# 图例
for xa, col, nm in ((X0 + 2, ACCENT, "就近舍入"), (X0 + 36, WARM, "向零截断")):
    line(ax, (xa, 31.4), (xa + 5.0, 31.4), color=col, lw=1.2)
    label(ax, xa + 6.2, 31.4, nm, fs=7.4, color=col, ha="left")
label(ax, X1 + 0.6, Y1 + 0.2, "误差", fs=7.6, color=GRAY, ha="left")
label(ax, 10.0, 2.6, "纵轴为量化误差（以输入为单位），档距取 0.25 以便看清；截断的误差恒为负，均值不是零",
      fs=7.0, color=GRAY, ha="left")
save(fig, "03/fig03_1.png")

# ---------------------------------------------------------------- 图 3-2
N = 32
AMP = [0.075 + 0.010 * ((i * 7) % 3) for i in range(N)]
AMP[16] = 2.0

fig, ax = canvas(7.4, 2.7, 100)
X0, X1 = 12.0, 92.0
Y0, TOP = 8.0, 28.0
MAXV = 2.05
bw = (X1 - X0) / N * 0.72


def hy(v):
    return Y0 + v / MAXV * (TOP - Y0)


for i, v in enumerate(AMP):
    x = X0 + (X1 - X0) * i / N + ((X1 - X0) / N - bw) / 2
    fc, ec = (RED_L, RED) if v > 1.0 else (ACCENT_L, ACCENT)
    box(ax, x, Y0, bw, max(hy(v) - Y0, 0.7), fc=fc, ec=ec, lw=0.8, radius=0.3)

line(ax, (X0, Y0), (X1, Y0), color=INK, lw=0.9)
# 右侧刻度，避免虚线穿过条形
for v, col in ((0.08, WARM), (2.0, RED)):
    line(ax, (X1 + 1.0, hy(v)), (X1 + 3.4, hy(v)), color=col, lw=0.8)
    line(ax, (X1 + 1.0, hy(v) - 0.6), (X1 + 1.0, hy(v) + 0.6), color=col, lw=0.8)
    label(ax, X1 + 4.6, hy(v), "%.2f" % v, fs=6.8, color=col, ha="left")

arrow(ax, (62.0, TOP + 4.2), (53.6, TOP + 0.6), color=RED, lw=0.9, rad=-0.15)
label(ax, 64.0, TOP + 5.0, "离群通道", fs=7.2, color=RED, ha="left")
label(ax, 10.0, 2.4, "per-tensor 档距 = 2.0/127 ≈ 0.0157，其余通道的有效格点只剩十来个；按通道定档距则为 0.00063",
      fs=6.8, color=GRAY, ha="left")
label(ax, 10.0, 0.4, "通道编号 1 到 32，幅度为构造数据，仅用于说明档距被单个通道撑大的机制",
      fs=6.6, color=GRAY, ha="left")
save(fig, "03/fig03_2.png")
