#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scipilot-writing-skill :: text_stats.py
=======================================
把"读着像不像人写的"量化成几个可解释指标，辅助 writing_lint 与 AI 读稿自审。
只用标准库。

指标
----
  - 句长分布：mean / sd / cv（变异系数）/ min / max。cv 偏低 = 节奏均匀 = 疑似 AI。
  - 被动语态比例：be 动词 + 过去分词的粗略计数 / 句数。
  - 名词化密度：-tion/-ment/-ance/-ence/-ity/-ness 结尾词 / 每百词。过高 = 句子笨重。
  - Hedging / Boosting 计数：学术 epistemic stance 是否得体（两者都要有，且匹配证据）。

用法
----
    python text_stats.py draft.txt --lang en
    python text_stats.py draft.txt --lang en --json
"""
from __future__ import annotations

import argparse
import json
import re
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

HEDGES = {"may", "might", "could", "would", "suggest", "suggests", "indicate", "indicates",
          "appear", "appears", "likely", "possibly", "probably", "perhaps", "seem", "seems",
          "tend", "tends", "relatively", "somewhat", "partly", "potentially", "presumably"}
BOOSTERS = {"clearly", "demonstrate", "demonstrates", "establish", "establishes", "show",
            "shows", "prove", "proves", "evident", "evidently", "substantially", "markedly",
            "definitely", "undoubtedly", "strongly", "conclusively", "significantly"}
NOMINAL_SUFFIX = re.compile(r"\b\w{3,}(?:tion|ment|ance|ence|ity|ness|ization|isation)\b",
                            re.IGNORECASE)
PASSIVE = re.compile(r"\b(?:is|are|was|were|be|been|being)\s+(?:\w+ly\s+)?"
                     r"(?:\w+ed|done|made|shown|found|given|taken|seen|known|built|set|"
                     r"used|based|proposed|trained|tested|observed|reported)\b", re.IGNORECASE)


def split_sentences(text: str, lang: str) -> list:
    if lang == "zh":
        parts = re.split(r"(?<=[。！？；])", text)
    else:
        prot = re.sub(r"\b(e\.g|i\.e|et al|Fig|Eq|cf|vs|Dr|Mr|Ms)\.", r"\1<D>", text)
        parts = re.split(r"(?<=[.!?])\s+", prot)
        parts = [p.replace("<D>", ".") for p in parts]
    return [p.strip() for p in parts if p.strip()]


def words(s: str, lang: str) -> int:
    if lang == "zh":
        return len(re.findall(r"[一-鿿]", s)) + len(re.findall(r"[A-Za-z]+", s))
    return len(re.findall(r"[A-Za-z][A-Za-z'\-]*", s))


def analyze(text: str, lang: str = "en") -> dict:
    sents = split_sentences(text, lang)
    lens = [words(s, lang) for s in sents]
    lens = [x for x in lens if x > 0]
    n = len(lens)
    total_words = sum(lens)
    mean = total_words / n if n else 0
    sd = (sum((x - mean) ** 2 for x in lens) / n) ** 0.5 if n else 0
    cv = sd / mean if mean else 0

    res = {
        "sentences": n,
        "words": total_words,
        "sentence_len": {"mean": round(mean, 1), "sd": round(sd, 1), "cv": round(cv, 2),
                         "min": min(lens) if lens else 0, "max": max(lens) if lens else 0},
        "monotone_flag": bool(n >= 5 and cv < 0.35),
    }
    if lang == "en":
        n_pass = len(PASSIVE.findall(text))
        n_nom = len(NOMINAL_SUFFIX.findall(text))
        toks = re.findall(r"[A-Za-z][A-Za-z'\-]*", text.lower())
        n_hedge = sum(1 for t in toks if t in HEDGES)
        n_boost = sum(1 for t in toks if t in BOOSTERS)
        res.update({
            "passive_per_sentence": round(n_pass / n, 2) if n else 0,
            "nominalization_per_100w": round(100 * n_nom / total_words, 1) if total_words else 0,
            "hedges": n_hedge,
            "boosters": n_boost,
        })
    return res


def _print(res: dict) -> None:
    sl = res["sentence_len"]
    print("==== text_stats ====")
    print(f"句子 {res['sentences']}  词 {res['words']}")
    print(f"句长  mean {sl['mean']}  sd {sl['sd']}  cv {sl['cv']}  (min {sl['min']} / max {sl['max']})")
    if res.get("monotone_flag"):
        print("  ⚠️  cv<0.35：句长过均匀，节奏机械，建议长短句交替")
    if "passive_per_sentence" in res:
        print(f"被动/句  {res['passive_per_sentence']}"
              + ("   ⚠️ 偏高" if res['passive_per_sentence'] > 0.6 else ""))
        print(f"名词化/百词  {res['nominalization_per_100w']}"
              + ("   ⚠️ 偏高，句子可能笨重" if res['nominalization_per_100w'] > 12 else ""))
        print(f"Hedging {res['hedges']}  /  Boosting {res['boosters']}"
              + ("   ⚠️ 几乎无 hedging，注意是否 overclaim" if res['hedges'] == 0 and res['sentences'] > 4 else ""))


def _main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="学术文本量化指标")
    ap.add_argument("path", help="文本路径；'-' 读 stdin")
    ap.add_argument("--lang", choices=["en", "zh"], default="en")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    text = sys.stdin.read() if args.path == "-" else open(args.path, encoding="utf-8").read()
    res = analyze(text, args.lang)
    if args.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        _print(res)
    return 0


if __name__ == "__main__":
    sys.exit(_main())
