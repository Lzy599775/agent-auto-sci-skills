#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scipilot-writing-skill :: latex_clean.py
========================================
LaTeX 文本的"纯净 + 转义"安全网。润色英文论文片段时，最容易翻车的是把
`95%` / `model_v1` / `R&D` 直接塞进正文导致编译错误或注释掉整行。本脚本：

  1. escape_latex(text)  —— 自动转义数学跨度**之外**的 % & # _（已转义的跳过），
                            保留 $...$、\\(..\\)、\\[..\\] 内的内容原样。
  2. check_latex(text)   —— 报告未转义特殊字符、`$` 是否配平、是否误用 Markdown、
                            以及擅自添加的强调命令数量。

注意：escape 只动正文里的裸特殊字符；它不会去改 `\\cite{a_b}`、`\\label{sec:x}`
这类命令参数（因为下划线在参数里通常无害）。要严格控制请人工复核 check 的输出。

用法
----
    python latex_clean.py draft.tex --check            # 只体检，不改
    python latex_clean.py draft.tex                     # 转义后输出到 stdout
    python latex_clean.py draft.tex --in-place         # 原地写回（先备份 .bak）
"""
from __future__ import annotations

import argparse
import re
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

SPECIALS = ("%", "&", "#", "_")


def _math_mask(text: str) -> list:
    """标记字符是否在数学跨度内（$..$ / \\(..\\) / \\[..\\]）或属于转义序列。"""
    mask = [False] * len(text)
    i, n, in_inline = 0, len(text), False
    while i < n:
        c = text[i]
        if c == "\\" and i + 1 < n:
            nxt = text[i + 1]
            if nxt == "(":
                j = text.find("\\)", i + 2); j = n if j == -1 else j + 2
                for k in range(i, j):
                    mask[k] = True
                i = j; continue
            if nxt == "[":
                j = text.find("\\]", i + 2); j = n if j == -1 else j + 2
                for k in range(i, j):
                    mask[k] = True
                i = j; continue
            mask[i] = True
            mask[i + 1] = True  # 转义的字符本身视为"已处理"
            i += 2; continue
        if c == "$":
            in_inline = not in_inline
            mask[i] = True
            i += 1; continue
        if in_inline:
            mask[i] = True
        i += 1
    return mask


def escape_latex(text: str) -> str:
    """转义数学外、未转义的 % & # _。"""
    mask = _math_mask(text)
    out = []
    for i, c in enumerate(text):
        if c in SPECIALS and not mask[i]:
            out.append("\\" + c)
        else:
            out.append(c)
    return "".join(out)


def check_latex(text: str) -> list:
    """返回 [(severity, message), ...]。severity ∈ {FAIL, WARN, INFO}。"""
    issues = []
    mask = _math_mask(text)
    # 未转义特殊字符
    sev = {"%": "FAIL", "&": "WARN", "#": "INFO", "_": "INFO"}
    cnt = {k: 0 for k in SPECIALS}
    for i, c in enumerate(text):
        if c in SPECIALS and not mask[i] and (i == 0 or text[i - 1] != "\\"):
            cnt[c] += 1
    for ch in SPECIALS:
        if cnt[ch]:
            issues.append((sev[ch], f"未转义 '{ch}' ×{cnt[ch]} → 应为 '\\{ch}'"))
    # $ 配平
    n_dollar = sum(1 for i, c in enumerate(text) if c == "$" and (i == 0 or text[i - 1] != "\\"))
    if n_dollar % 2:
        issues.append(("FAIL", f"行内数学 '$' ×{n_dollar}（奇数）未配平"))
    # Markdown 误用
    md = re.findall(r"\*\*[^*]+\*\*|(?<!\w)__[^_]+__", text)
    if md:
        issues.append(("WARN", f"疑似 Markdown 加粗 ×{len(md)} → LaTeX 应用 \\textbf{{}}"))
    # 擅自强调（风格提示）
    emph = len(re.findall(r"\\(?:textbf|emph|textit)\{", text))
    if emph:
        issues.append(("INFO", f"强调命令 \\textbf/\\emph/\\textit ×{emph}（顶刊正文倾向少用，确认是否原文已有）"))
    return issues


def _main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="LaTeX 纯净 + 转义工具")
    ap.add_argument("path", help="LaTeX 文件路径；'-' 读 stdin")
    ap.add_argument("--check", action="store_true", help="只体检，不输出转义结果")
    ap.add_argument("--in-place", action="store_true", help="原地写回（生成 .bak 备份）")
    args = ap.parse_args(argv)

    text = sys.stdin.read() if args.path == "-" else open(args.path, encoding="utf-8").read()

    issues = check_latex(text)
    for sev, msg in issues:
        print(f"[{sev}] {msg}", file=sys.stderr)
    has_fail = any(s == "FAIL" for s, _ in issues)

    if args.check:
        print(("FAIL" if has_fail else "OK"), file=sys.stderr)
        return 2 if has_fail else 0

    cleaned = escape_latex(text)
    if args.in_place and args.path != "-":
        open(args.path + ".bak", "w", encoding="utf-8").write(text)
        open(args.path, "w", encoding="utf-8").write(cleaned)
        print(f"written: {args.path}  (backup: {args.path}.bak)", file=sys.stderr)
    else:
        sys.stdout.write(cleaned)
    return 0


if __name__ == "__main__":
    sys.exit(_main())
