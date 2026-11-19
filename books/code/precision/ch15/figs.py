# -*- coding: utf-8 -*-
"""第 15 章插图：从离线评估到线上监控的闭环。"""

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

fig, ax = canvas(7.4, 2.2, 100)

BOXES = [("离线评估", "分层指标　中间指标", GRAY, GRAY_L),
         ("灰度", "1% 流量对照", ACCENT, ACCENT_L),
         ("全量", "版本可切换", GREEN, GREEN_L),
         ("监控", "漂移　抽检　投诉", WARM, WARM_L)]
X = [2.0, 26.0, 50.0, 74.0]
W, H, Y = 18.0, 8.4, 16.0

for (t1, t2, ec, fc), x in zip(BOXES, X):
    box(ax, x, Y, W, H, fc=fc, ec=ec, lw=0.9, radius=1.0)
    label(ax, x + W / 2, Y + H - 2.9, t1, fs=8.0, bold=True, color=ec)
    label(ax, x + W / 2, Y + 2.6, t2, fs=6.2, color=GRAY)

for i, cond in enumerate(["指标达标", "无异常", "平稳"]):
    arrow(ax, (X[i] + W + 0.2, Y + H / 2), (X[i + 1] - 0.2, Y + H / 2), lw=0.9)
    label(ax, (X[i] + W + X[i + 1]) / 2, Y + H / 2 + 1.4, cond, fs=6.0, color=GRAY)

# 回环
ybot = 8.0
x1 = X[3] + W / 2
x2 = X[0] + W / 2
line(ax, (x1, Y - 0.2), (x1, ybot), color=RED, lw=0.9)
line(ax, (x1, ybot), (x2, ybot), color=RED, lw=0.9)
arrow(ax, (x2, ybot), (x2, Y - 0.2), color=RED, lw=0.9)
label(ax, (x1 + x2) / 2, ybot - 2.4, "告警触发回滚，回到上一版并重新评估", fs=6.6, color=RED)

label(ax, 2.0, 1.6, "四个阶段之间都有明确的进入条件；任何一环出问题都要能退回到上一个稳定版本",
      fs=6.8, color=GRAY, ha="left")
save(fig, "15/fig15_1.png")
