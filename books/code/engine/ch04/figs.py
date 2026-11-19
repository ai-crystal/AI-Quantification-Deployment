# -*- coding: utf-8 -*-
"""第 4 章插图：动态形状与静态形状的执行路径对比。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("engine")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      line, save)

fig, ax = canvas(7.4, 3.5, 100)

# ---------------------------------------------------------------- 动态
label(ax, 2.0, 47.2, "动态形状", fs=8.4, bold=True, ha="left", color=WARM)

dyn = ["收到请求，读实际形状", "推导每个中间张量形状", "按推导结果申请显存",
       "运行时挑一份 kernel", "按上限重算 workspace", "执行，结束后释放"]
for i, t in enumerate(dyn):
    yy = 40.5 - i * 6.6
    box(ax, 2.0, yy, 39.0, 5.2, t, fc=WARM_L, ec=WARM, fs=7.4, radius=0.9)
    if i:
        arrow(ax, (21.5, yy + 6.6), (21.5, yy + 5.5), color=WARM, lw=0.8)

# ---------------------------------------------------------------- 静态
label(ax, 55.0, 47.2, "静态形状", fs=8.4, bold=True, ha="left", color=GREEN)

sta = ["校验形状在范围内", "复用预分配的缓冲", "执行预编译的 kernel", "结束后缓冲归池"]
for i, t in enumerate(sta):
    yy = 40.5 - i * 6.6
    box(ax, 55.0, yy, 39.0, 5.2, t, fc=GREEN_L, ec=GREEN, fs=7.4, radius=0.9)
    if i:
        arrow(ax, (74.5, yy + 6.6), (74.5, yy + 5.5), color=GREEN, lw=0.8)

label(ax, 55.0, 12.6, "构建期做完的部分", fs=7.4, color=GRAY, ha="left")
label(ax, 55.0, 8.6, "形状推导　显存分配\nkernel 选择　workspace 重算", fs=7.4,
      color=GRAY, ha="left")

# 中部划分
ax.plot([48.0, 48.0], [3.0, 46.0], color=GRAY, lw=0.8, ls=(0, (4, 3)))
ax.text(46.0, 24.0, "形状专用化", rotation=90, ha="center", va="center",
        fontsize=7.2, color=GRAY)

label(ax, 50, 0.8, "两端相同，差别在被省掉的中间环节", fs=7.2, color=GRAY)
save(fig, "04/fig04_1.png")
