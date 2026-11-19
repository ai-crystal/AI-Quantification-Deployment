# -*- coding: utf-8 -*-
"""第 2 章插图：存储阶梯与合并访问。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("compute")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK,
                      WARM, WARM_L, WHITE, arrow, box, brace, canvas, label,
                      line, note, save)
from matplotlib.patches import Rectangle

# ---------------------------------------------------------------- 图 2-1
fig, ax = canvas(7.4, 3.3, 100)

rows = [
    ("寄存器", "256 KB / SM", "1 到 4 周期", 20.0, GREEN_L, GREEN),
    ("共享内存", "164 KB / SM", "约 25 周期", 22.0, ACCENT_L, ACCENT),
    ("一级缓存", "约 192 KB / SM", "约 30 周期", 22.0, ACCENT_L, ACCENT),
    ("二级缓存", "40 MB", "约 200 周期", 44.0, GRAY_L, GRAY),
    ("显存", "80 GB", "400 到 800 周期", 60.0, WARM_L, WARM),
]

label(ax, 76.0, 40.0, "延迟（量级）", fs=7.2, color=GRAY, ha="left")

for i, (name, cap, lat, w, fc, ec) in enumerate(rows):
    y = 33.0 - i * 6.6
    box(ax, 4.0, y, w, 5.2, name, fc=fc, ec=ec, fs=8.4, bold=True)
    label(ax, 4.0 + w + 2.4, y + 2.6, cap, fs=7.4, color=INK, ha="left")
    label(ax, 76.0, y + 2.6, lat, fs=7.4, color=GRAY, ha="left")

note(ax, 4.0, 0.4,
     "条宽按容量对数缩放，每级大约差 200 到 2000 倍；延迟为量级估计，不是实测值",
     fs=7.2)
save(fig, "02/fig02_1.png")

# ---------------------------------------------------------------- 图 2-2
fig, ax = canvas(7.4, 3.0, 100)

label(ax, 4.0, 38.0, "连续地址", fs=8.6, bold=True, ha="left")
label(ax, 4.0, 35.2, "32 个线程各读 1 个 float，地址相邻", fs=7.4, color=GRAY, ha="left")

for k in range(4):
    x = 6.0 + k * 19.4
    box(ax, x, 27.6, 19.0, 5.2, "32 B", fc=ACCENT_L, ec=ACCENT, fs=6.8, lw=0.8)
    for j in range(1, 8):
        xx = x + j * 19.0 / 8.0
        line(ax, (xx, 27.9), (xx, 32.5), color=ACCENT, lw=0.3, zorder=4)

brace(ax, 6.0, 6.0 + 4 * 19.4 - 0.4, 27.0, "1 条 128 B 缓存行，4 个扇区",
      color=ACCENT, fs=7.2, upward=False)
label(ax, 6.0, 21.6, "取回 128 B，用到 128 B", fs=7.4, ha="left")

label(ax, 4.0, 18.2, "跨步 32 个 float", fs=8.6, bold=True, ha="left")
label(ax, 4.0, 15.4, "每个线程落在不同的缓存行上", fs=7.4, color=GRAY, ha="left")

for k in range(8):
    x = 6.0 + k * 10.6
    box(ax, x, 7.6, 8.0, 5.2, fc=GRAY_L, ec=GRAY, lw=0.7, radius=0.6)
    ax.add_patch(Rectangle((x + 0.9, 7.9), 1.1, 4.6, facecolor=ACCENT,
                           edgecolor="none", zorder=4))

label(ax, 6.0, 1.6, "取回 1024 B，用到 128 B，有效带宽掉到八分之一",
      fs=7.4, color=WARM, ha="left")
label(ax, 96.0, 10.2, "共 32 条" + chr(10) + "每个只用到 4 字节", fs=7.2, color=GRAY, ha="right")

save(fig, "02/fig02_2.png")
