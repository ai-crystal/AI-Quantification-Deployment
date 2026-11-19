# -*- coding: utf-8 -*-
"""第 14 章插图：迭代速度与性能要求构成的选型空间。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("engine")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      save)

fig, ax = canvas(7.4, 3.5, 100)

OX, OY = 20.0, 10.0
XM, YM = 94.0, 44.0

# 象限底色
box(ax, OX, OY, 34.0, 15.0, "", fc=GRAY_L, ec=WHITE, radius=0.4, lw=0.6)
box(ax, OX + 34.0, OY, 40.0, 15.0, "", fc=ACCENT_L, ec=WHITE, radius=0.4, lw=0.6)
box(ax, OX, OY + 15.0, 34.0, 19.0, "", fc=WARM_L, ec=WHITE, radius=0.4, lw=0.6)
box(ax, OX + 34.0, OY + 15.0, 40.0, 19.0, "", fc=GREEN_L, ec=WHITE, radius=0.4,
    lw=0.6)

# 坐标轴
ax.plot([OX - 1.5, OX - 1.5], [OY, YM + 1.0], color=GRAY, lw=1.0)
arrow(ax, (OX - 1.5, YM + 1.0), (OX - 1.5, YM + 3.0), color=GRAY, lw=1.0)
ax.plot([OX, XM + 1.0], [OY - 1.5, OY - 1.5], color=GRAY, lw=1.0)
arrow(ax, (XM + 1.0, OY - 1.5), (XM + 3.0, OY - 1.5), color=GRAY, lw=1.0)

ax.text(OX - 4.0, (OY + YM) / 2, "性能要求（低 → 高）", rotation=90, ha="center", va="center",
        fontsize=7.6, color=GRAY)
label(ax, (OX + XM) / 2, OY - 4.4, "迭代速度（慢 → 快）", fs=7.6, color=GRAY)

# 象限内容
label(ax, OX + 17.0, OY + 27.4, "编译式引擎", fs=8.2, bold=True, color=WARM)
label(ax, OX + 17.0, OY + 22.4, "模型稳定，值得\n把 tactic 调到极致", fs=7.4, color=GRAY)

label(ax, OX + 54.0, OY + 27.4, "通用框架加关键模型编译", fs=8.2, bold=True,
      color=GREEN)
label(ax, OX + 54.0, OY + 22.4, "主力走通用，热点走编译", fs=7.4, color=GRAY)

label(ax, OX + 17.0, OY + 10.0, "收益有限", fs=8.2, bold=True, color=GRAY)
label(ax, OX + 17.0, OY + 5.6, "要求不高又改得慢，\n先别投入", fs=7.4, color=GRAY)

label(ax, OX + 54.0, OY + 10.0, "通用框架或 torch.compile", fs=8.2, bold=True,
      color=ACCENT)
label(ax, OX + 54.0, OY + 5.6, "迭代优先，延迟够用就停", fs=7.4, color=GRAY)

label(ax, 50, 2.4, "另一个维度是硬件：只有一种卡时向左上走，多种卡时向右下退", fs=7.0,
      color=GRAY)
save(fig, "14/fig14_1.png")
