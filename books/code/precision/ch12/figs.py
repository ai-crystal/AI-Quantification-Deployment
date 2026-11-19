# -*- coding: utf-8 -*-
"""第 12 章插图：迭代裁剪的闭环。"""

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

fig, ax = canvas(7.4, 2.0, 100)

BOXES = [("训练", "收敛到基线", GRAY, GRAY_L),
         ("评估通道", "按缩放因子排序", ACCENT, ACCENT_L),
         ("剪枝", "剪掉本轮比例", WARM, WARM_L),
         ("微调", "小学习率恢复", GREEN, GREEN_L),
         ("导出", "重置 BN 统计", GRAY, GRAY_L)]
X = [2.0, 20.6, 39.2, 57.8, 76.4]
W, H, Y = 15.2, 8.4, 10.0

for (t1, t2, ec, fc), x in zip(BOXES, X):
    box(ax, x, Y, W, H, fc=fc, ec=ec, lw=0.9, radius=1.0)
    label(ax, x + W / 2, Y + H - 2.9, t1, fs=7.8, bold=True, color=ec)
    label(ax, x + W / 2, Y + 2.6, t2, fs=6.4, color=GRAY)

for i in range(len(BOXES) - 1):
    arrow(ax, (X[i] + W + 0.2, Y + H / 2), (X[i + 1] - 0.2, Y + H / 2), lw=0.9)

label(ax, (X[3] + W + X[4]) / 2, Y - 1.9, "达标", fs=6.4, color=GRAY)

# 回环：微调 → 评估
ytop = 22.6
x1 = X[3] + W / 2
x2 = X[1] + W / 2
line(ax, (x1, Y + H + 0.2), (x1, ytop), color=WARM, lw=0.9)
line(ax, (x1, ytop), (x2 + 1.0, ytop), color=WARM, lw=0.9)
arrow(ax, (x2 + 1.0, ytop), (x2, Y + H + 0.2), color=WARM, lw=0.9)
label(ax, (x1 + x2) / 2, ytop + 1.4, "未达标，剪下一轮", fs=6.6, color=WARM)

label(ax, 2.0, 2.2, "每一轮都要重新评估通道重要性，剪完立刻微调；回环次数由目标剪枝率决定，每轮剪枝率通常不超过 20%",
      fs=6.8, color=GRAY, ha="left")
save(fig, "12/fig12_1.png")
