# -*- coding: utf-8 -*-
"""第 6 章插图：PTQ 流程与逐层敏感度。"""

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
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, elb_arrow,
                      label, line, save)

# ---------------------------------------------------------------- 图 6-1
fig, ax = canvas(7.4, 2.6, 100)

STEPS = [("导出", "融合算子\n固定形状", GRAY, GRAY_L),
         ("插观察器", "权重量化参数\n在导出时算出", ACCENT, ACCENT_L),
         ("校准", "统计激活范围", ACCENT, ACCENT_L),
         ("转换", "烧进量化参数", GREEN, GREEN_L),
         ("量化图", "逐层校验误差", WARM, WARM_L)]
X = [1.5, 20.6, 39.7, 58.8, 77.9]
W, H, Y = 15.6, 10.0, 13.0

for (t1, t2, ec, fc), x in zip(STEPS, X):
    box(ax, x, Y, W, H, fc=fc, ec=ec, lw=0.9, radius=1.0)
    label(ax, x + W / 2, Y + H - 3.2, t1, fs=8.4, bold=True, color=ec)
    label(ax, x + W / 2, Y + 3.2, t2, fs=6.8, color=GRAY)

for i in range(len(STEPS) - 1):
    arrow(ax, (X[i] + W + 0.2, Y + H / 2), (X[i + 1] - 0.2, Y + H / 2), lw=1.0)

# 校验回路
box(ax, 44.0, 1.6, 26.0, 6.4, fc=WHITE, ec=WARM, lw=0.9, radius=1.0)
label(ax, 57.0, 4.8, "逐层比对余弦相似度", fs=7.0, color=WARM)
elb_arrow(ax, (85.7, Y - 0.2), (70.2, 4.8), color=WARM, lw=0.9, first="v")
elb_arrow(ax, (44.0, 4.8), (47.4, Y - 0.2), color=WARM, lw=0.9, first="h")
label(ax, 49.8, 9.9, "误差超标只回退这一层，不必重跑整条流程", fs=7.0, color=GRAY, ha="left")
save(fig, "06/fig06_1.png")

# ---------------------------------------------------------------- 图 6-2
SENS = [0.62, 0.08, 0.05, 0.11, 0.07, 0.09, 0.14, 0.06, 0.10, 0.05,
        0.08, 0.41, 0.07, 0.06, 0.09, 0.12, 0.05, 0.08, 0.07, 0.13,
        0.06, 0.09, 0.11, 0.58]

fig, ax = canvas(7.4, 2.5, 100)
X0, X1 = 13.0, 92.0
Y0, TOP = 7.5, 27.0
bw = (X1 - X0) / len(SENS) * 0.66
vmax = 0.65

for i, v in enumerate(SENS):
    x = X0 + (X1 - X0) * i / len(SENS) + ((X1 - X0) / len(SENS) - bw) / 2
    h = v / vmax * (TOP - Y0)
    if v > 0.3:
        fc, ec = RED_L, RED
    elif v > 0.12:
        fc, ec = WARM_L, WARM
    else:
        fc, ec = ACCENT_L, ACCENT
    box(ax, x, Y0, bw, max(h, 0.6), fc=fc, ec=ec, lw=0.7, radius=0.3)

line(ax, (X0, Y0), (X1, Y0), color=INK, lw=0.9)
for i in (0, 5, 11, 17, 23):
    x = X0 + (X1 - X0) * (i + 0.5) / len(SENS)
    label(ax, x, Y0 - 2.4, "%d" % (i + 1), fs=7.0, color=GRAY)
label(ax, X1 + 0.8, Y0 - 2.4, "层", fs=7.0, color=GRAY, ha="left")

label(ax, X0 + (X1 - X0) * 0.5 / len(SENS), TOP + 1.6, "首层", fs=7.0, color=RED)
label(ax, X0 + (X1 - X0) * 11.5 / len(SENS), TOP + 1.6, "中部大通道块", fs=7.0, color=RED)
label(ax, X0 + (X1 - X0) * 23.5 / len(SENS), TOP + 1.6, "分类头", fs=7.0, color=RED, ha="right")

label(ax, 1.5, 2.0, "纵轴为只量化该层时的任务指标下降量（百分点），数值为假设，仅示意排序形状",
      fs=7.0, color=GRAY, ha="left")
save(fig, "06/fig06_2.png")
