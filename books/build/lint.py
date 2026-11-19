# -*- coding: utf-8 -*-
"""稿件体检：在编译之前找出会让书出错的问题。

检查项：
  1. 图片路径不存在，或图片目录与章号不一致
  2. 代码块内部嵌套了代码围栏，或代码块没有闭合
  3. 标题里出现会干扰排版的字符（< > &，以及未闭合的 *）
  4. 图号、表号是否连续，章号是否与文件一致
  5. 公式块 $$ 是否成对出现
  6. 指向站内其他 Markdown 的链接是否写成了相对路径（docsify 需要仓库绝对路径）

用法：
    python books/build/lint.py --book books/intro
"""

import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BOOK = os.path.join(ROOT, "books", "intro")
if "--book" in sys.argv:
    val = sys.argv[sys.argv.index("--book") + 1]
    BOOK = val if os.path.isabs(val) else os.path.join(ROOT, val)

BAD_HEAD = re.compile(r"[<>&]")
FIG_CAP = re.compile(r"^!\[(图\s*(\d+)-(\d+))")
TAB_CAP = re.compile(r"^表\s*(\d+)-(\d+)")


def files():
    out = []
    for pat in ("chapters/*.md", "front/*.md", "appendix/*.md"):
        out.extend(sorted(glob.glob(os.path.join(BOOK, pat))))
    return out


def check(path):
    errors, warns = [], []
    text = open(path, encoding="utf-8").read()
    lines = text.split("\n")
    rel = os.path.relpath(path, BOOK)
    mch = re.match(r"ch(\d+)\.md$", os.path.basename(path))

    in_code = False
    code_start = 0
    in_math = False
    math_start = 0
    figs, tabs = [], []

    for i, line in enumerate(lines, 1):
        stripped = line.strip()

        # 公式块：单独成段的 $$ 开闭
        if not in_code and stripped.startswith("$$"):
            if stripped == "$$":
                in_math = not in_math
                if in_math:
                    math_start = i
                continue
            if not (stripped.endswith("$$") and len(stripped) > 4):
                errors.append("%s:%d 行内公式块没有在同一行闭合" % (rel, i))
            continue
        if in_math:
            if stripped.endswith("$$"):
                in_math = False
            continue

        if line.startswith("```"):
            if in_code and stripped != "```":
                errors.append("%s:%d 代码块内部又出现围栏行" % (rel, i))
            in_code = not in_code
            if in_code:
                code_start = i
            continue
        if in_code:
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            title = m.group(2)
            if BAD_HEAD.search(title):
                errors.append("%s:%d 标题含 < > & 字符：%s" % (rel, i, title))
            if title.count("*") % 2 == 1:
                errors.append("%s:%d 标题里的粗体标记没有闭合" % (rel, i, title))
            if "$$" in title:
                errors.append("%s:%d 标题里不要放公式" % (rel, i))

        for src in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", line):
            if src.startswith("http"):
                continue
            target = os.path.normpath(os.path.join(os.path.dirname(path), src))
            if not os.path.exists(target):
                errors.append("%s:%d 图片不存在：%s" % (rel, i, src))
            mim = re.search(r"images/(\d{2})/fig(\d{2})_", src)
            if mch and mim:
                n = int(mch.group(1))
                if int(mim.group(1)) != n or int(mim.group(2)) != n:
                    errors.append("%s:%d 图片目录与章号不符：%s" % (rel, i, src))

        cap = FIG_CAP.match(stripped)
        if cap:
            figs.append(int(cap.group(3)))
            if mch and int(cap.group(2)) != int(mch.group(1)):
                errors.append("%s:%d 图号章号与实际章不符：%s" % (rel, i, cap.group(1)))
        cap = TAB_CAP.match(stripped)
        if cap:
            tabs.append(int(cap.group(2)))
            if mch and int(cap.group(1)) != int(mch.group(1)):
                errors.append("%s:%d 表号章号与实际章不符：表 %s"
                              % (rel, i, cap.group(1) + "-" + cap.group(2)))

        for href in re.findall(r"\]\(([^)]+)\)", line):
            if href.startswith("http") or href.startswith("#") or href.startswith("mailto"):
                continue
            if href.endswith(".md") and not href.startswith("/") and not href.startswith("../"):
                warns.append("%s:%d 站内链接建议写仓库绝对路径：%s" % (rel, i, href))

    if in_code:
        errors.append("%s:%d 代码块没有闭合" % (rel, code_start))
    if in_math:
        errors.append("%s:%d 公式块没有闭合" % (rel, math_start))

    for name, seq in (("图", figs), ("表", tabs)):
        uniq = []
        for n in seq:
            if not uniq or uniq[-1] != n:
                uniq.append(n)
        for a, b in zip(uniq, uniq[1:]):
            if b != a + 1:
                warns.append("%s %s编号不连续：%d 之后是 %d" % (rel, name, a, b))

    return errors, warns


def main():
    all_err, all_warn = [], []
    for path in files():
        e, w = check(path)
        all_err.extend(e)
        all_warn.extend(w)

    for m in all_warn:
        print("  [注意] " + m)
    for m in all_err:
        print("  [错误] " + m)

    if all_err:
        print("体检发现 %d 个必须修的问题。" % len(all_err))
        return 1
    print("体检通过，%d 个文件。" % len(files()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
