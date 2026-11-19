# -*- coding: utf-8 -*-
"""第 14 章插图：蒸馏损失的构成。"""

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

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, WARM,
                      WARM_L, WHITE, arrow, box, canvas, label, line, save)

fig, ax = canvas(7.4, 2.5, 100)

# 教师、学生、标签
box(ax, 2.0, 24.0, 16.0, 7.0, fc=GRAY_L, ec=GRAY, lw=0.9, radius=0.9)
label(ax, 10.0, 27.5, "教师（fp32）", fs=7.4)

box(ax, 2.0, 12.5, 16.0, 7.0, fc=ACCENT_L, ec=ACCENT, lw=0.9, radius=0.9)
label(ax, 10.0, 16.0, "学生（量化后）", fs=7.4, color=ACCENT)

box(ax, 2.0, 1.5, 16.0, 6.5, fc=GREEN_L, ec=GREEN, lw=0.9, radius=0.9)
label(ax, 10.0, 4.8, "真实标签 y", fs=7.4, color=GREEN)

# 两项损失
box(ax, 44.0, 24.0, 18.0, 7.0, fc=WARM_L, ec=WARM, lw=0.9, radius=0.9)
label(ax, 53.0, 27.5, "KL( p_t ‖ p_s )", fs=7.6, color=WARM)

box(ax, 44.0, 12.0, 18.0, 7.0, fc=WARM_L, ec=WARM, lw=0.9, radius=0.9)
label(ax, 53.0, 15.5, "CE( y, p_s )", fs=7.6, color=WARM)

# 箭头
arrow(ax, (18.2, 27.5), (43.6, 27.5), lw=0.9, text="p_t（温度 T）", toff=(0, 1.2), fs=6.4)
arrow(ax, (18.2, 16.0), (43.6, 16.0), lw=0.9, text="p_s", toff=(0, 1.2), fs=6.4)
arrow(ax, (18.2, 8.2), (43.6, 12.8), lw=0.9, color=GREEN, rad=-0.12)

# 合并
box(ax, 74.0, 17.0, 17.0, 8.0, fc=WHITE, ec=INK, lw=1.0, radius=0.9)
label(ax, 82.5, 21.0, "加权求和 L", fs=7.6, bold=True)

arrow(ax, (62.2, 27.5), (73.8, 23.0), lw=0.9, text="α T²", toff=(0.2, 1.0), fs=6.6)
arrow(ax, (62.2, 15.5), (73.8, 19.0), lw=0.9, text="1 − α", toff=(0.4, 1.2), fs=6.6)

save(fig, "14/fig14_1.png")
