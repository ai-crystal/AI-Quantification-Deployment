# -*- coding: utf-8 -*-
"""第 12 章插图：一个请求从到达到逐 token 返回的生命周期。"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "common"))

import figstyle
figstyle.use_book("engine")

from figstyle import (ACCENT, ACCENT_L, GRAY, GRAY_L, GREEN, GREEN_L, INK, RED,
                      RED_L, WARM, WARM_L, WHITE, arrow, box, canvas, label,
                      msg, save)

fig, ax = canvas(7.4, 3.2, 100)

lanes = [
    ("客户端", 7.5, ACCENT),
    ("接入与队列", 29.0, WARM),
    ("调度器", 50.0, GREEN),
    ("引擎与显存", 71.0, ACCENT),
    ("指标", 90.0, GRAY),
]

for name, x, color in lanes:
    box(ax, x - 7.4, 38.4, 14.8, 4.8, name, fc=WHITE, ec=color, fs=7.0, bold=True)
    ax.plot([x, x], [38.0, 4.4], color=color, lw=0.7, ls=(0, (4, 3)))

msg(ax, 7.5, 29.0, 33.6, "HTTP 请求", fs=7.2)
label(ax, 31.0, 30.6, "解析、鉴权、tokenize", fs=7.0, color=WARM, ha="left")
msg(ax, 29.0, 50.0, 27.4, "入队", fs=7.2)
label(ax, 52.4, 26.2, "在这里排队，等下一个 step", fs=7.0, color=GRAY, ha="left")
msg(ax, 50.0, 29.0, 23.2, "可以进批次", fs=7.0, dash=True)
msg(ax, 50.0, 71.0, 19.6, "prefill", fs=7.2)
msg(ax, 71.0, 50.0, 16.2, "首 token", fs=7.2, dash=True)
msg(ax, 50.0, 29.0, 12.8, "转发 token", fs=7.1, dash=True)
msg(ax, 29.0, 7.5, 10.2, "流式返回", fs=7.1)
msg(ax, 50.0, 71.0, 7.0, "decode 若干步，每步一次", fs=7.2)
msg(ax, 71.0, 90.0, 7.0, "", fs=7.0)
label(ax, 80.5, 8.2, "每步上报", fs=7.0, color=GRAY, ha="center")

label(ax, 50, 1.4, "虚线是控制消息，实线是数据；排队与 prefill 的长度决定首 token 延迟", fs=7.0,
      color=GRAY)
save(fig, "12/fig12_1.png")
