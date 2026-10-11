#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scipilot-writing-skill :: writing_lint.py
=========================================
学术写作质量的"确定性"linter —— 把"读着像 AI / 不够干净"从感觉变成机器可检的契约。

这是 SciPilot 写作技能的证据链核心：交付前强制运行，命中 FAIL 必须处理。
它只抓**确定性**问题（词表、正则、转义、标点、统计阈值）；感知性与逻辑问题
（是否 overclaim、是否连贯）交给 AI 读稿自审闭环（见 SKILL.md Stage 5）。

检查项
------
通用（中英）：
  - AI 指纹词 / 短语（中英两套词表）
  - 机械连接词扎堆（Moreover/Furthermore/此外/值得注意的是 …）
  - 悬垂 -ing 伪洞见（…, highlighting the importance of …）
  - 否定式平行（not only … but also / 不仅……而且……）
  - 破折号（em dash）密度
  - 空泛归因（Studies show / 专家认为，无具体引用）
  - 模型/方法名所有格（GPT's → the performance of GPT）
  - 句长节奏（burstiness 过低 = 均匀机械，疑似 AI）
  - 被动语态比例（仅提示）
  - NOT_BUT_CONSTRUCTION_CLUSTER / repeated defensive contrast（仅提示）
  - prose manual line breaks（<br>, soft/hard breaks, Unicode separators, vertical tab）
  - table-cell leading/trailing whitespace（Markdown/LaTeX table rows）
  - repeated low-value number and figure/table citation candidates（仅提示）
LaTeX 载体（--mode latex）：
  - 未转义特殊字符 %（FAIL，会注释掉整行）、& 、_ 、#
  - `$` 数学定界符是否配平（FAIL）
  - 误用 Markdown（**bold** 应为 \\textbf）
Word / 纯中文载体（--mode word，或 --lang zh）：
  - 残留 Markdown 标记（Word 端必须零 Markdown → FAIL）
  - 半角标点夹在中文之间（建议全角）

用法
----
    python writing_lint.py draft.tex --mode latex --lang en --report lint_report.json
    python writing_lint.py draft.txt --mode word  --lang zh
    echo "some text" | python writing_lint.py - --mode plain

退出码：0=PASS（无 WARN/FAIL）  1=有 WARN  2=有 FAIL

V2 advisory checks deliberately do not auto-delete text. They surface candidates for the story, evidence,
reproducibility, figure/table, and fact-placement audits; necessary reporting and scientific boundaries remain the
author/model's responsibility.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict, field

# Windows GBK 终端直接 print 中文会 UnicodeEncodeError；用 reconfigure（幂等、不换对象）。
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass


# ──────────────────────────────────────────────────────────────────────────
# 词表（用户可在导入后扩展这些模块级集合）
# ──────────────────────────────────────────────────────────────────────────

# 被过度滥用的"高级"词（英文）。命中不必然是错，但密集出现是强 AI 指纹。
AI_TELL_WORDS_EN = {
    "delve", "delves", "delving", "leverage", "leverages", "leveraging",
    "underscore", "underscores", "underscoring", "pivotal", "crucial",
    "realm", "realms", "landscape", "tapestry", "nuanced", "nuance",
    "intricate", "intricacies", "showcase", "showcases", "showcasing",
    "myriad", "plethora", "paradigm", "paradigms", "harness", "harnesses",
    "harnessing", "seamless", "seamlessly", "robust",  # robust：泛用时才算
    "testament", "beacon", "elevate", "elevates", "boast", "boasts",
    "unveil", "unveils", "unveiling", "embark", "foster", "fosters",
    "encompass", "encompasses", "meticulous", "meticulously",
    "groundbreaking", "revolutionary", "transformative", "unprecedented",
    "cutting-edge", "state-of-the-art",  # CS 中 SOTA 常见，降级为 INFO
}

# 高 AI 味的短语（英文，正则）
AI_TELL_PHRASES_EN = [
    r"plays?\s+an?\s+(?:vital|crucial|pivotal|key|significant|important)\s+role",
    r"stands?\s+as\s+a\s+testament",
    r"a\s+(?:rich\s+)?tapestry\s+of",
    r"in\s+the\s+(?:ever[- ]evolving|rapidly\s+evolving)\s+(?:landscape|world|field)",
    r"paving\s+the\s+way\s+for",
    r"a\s+beacon\s+of",
    r"delve\s+into",
    r"navigat\w*\s+the\s+(?:complex|complexit|landscape)",
    r"at\s+the\s+forefront\s+of",
    r"it\s+is\s+worth\s+noting\s+that",
    r"it\s+is\s+important\s+to\s+note\s+that",
    r"needless\s+to\s+say",
]

# 机械连接词（句首）。出现 1-2 次正常，扎堆才报。
MECH_CONNECTIVES_EN = [
    "moreover", "furthermore", "additionally", "notably", "importantly",
    "consequently", "specifically", "indeed", "essentially", "basically",
]

# promotional / 夸张词（英文）
PROMO_WORDS_EN = {
    "groundbreaking", "revolutionary", "game-changing", "game-changer",
    "seamlessly", "unprecedented", "remarkable", "remarkably", "vast",
    "tremendous", "immense", "profound", "profoundly",
}

# 中文 AI 味 / 空洞渲染词
AI_TELL_WORDS_ZH = [
    "毋庸置疑", "众所周知", "不可磨灭", "范式转移", "范式转变", "颠覆性",
    "赋能", "抓手", "闭环", "深刻地", "切中要害", "本质上", "某种程度上",
    "值得一提的是", "值得注意的是", "综上所述", "总而言之", "不言而喻",
    "至关重要", "极大地", "显著地", "前所未有", "令人惊叹", "强有力地",
    "深远的影响", "划时代", "里程碑式",
]

# 中文机械连接 / 罗列
MECH_CONNECTIVES_ZH = ["此外", "另外", "更重要的是", "首先", "其次", "再次", "再者", "最后", "综上", "综上所述", "进一步而言", "总而言之", "由此可见"]

# 空泛归因（英文正则）
VAGUE_ATTR_EN = [
    r"\b(?:studies|researchers|scientists|experts|prior\s+works?|many\s+works?)\s+"
    r"(?:have\s+)?(?:shown|found|demonstrated|suggested|argued|agree|believe|reported)\b",
    r"\bit\s+is\s+(?:widely\s+)?(?:known|believed|recognized|accepted|understood)\s+that\b",
]
VAGUE_ATTR_ZH = [r"(?:研究|学者|专家|观察者|人们)(?:普遍)?(?:认为|表明|发现|指出|相信)"]

SEV_FAIL, SEV_WARN, SEV_INFO = "FAIL", "WARN", "INFO"


@dataclass
class Issue:
    severity: str
    code: str
    message: str
    line: int = 0
    count: int = 1
    examples: list = field(default_factory=list)


# ──────────────────────────────────────────────────────────────────────────
# 工具
# ──────────────────────────────────────────────────────────────────────────

def _line_of(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def _split_sentences(text: str, lang: str) -> list:
    if lang == "zh":
        parts = re.split(r"(?<=[。！？；])", text)
    else:
        # 在 .!? 后接空白处断句；避免把 e.g./i.e./et al. 误断（粗略）
        protected = re.sub(r"\b(e\.g|i\.e|et al|Fig|Eq|cf|vs|Dr|Mr|Ms)\.", r"\1<DOT>", text)
        parts = re.split(r"(?<=[.!?])\s+", protected)
        parts = [p.replace("<DOT>", ".") for p in parts]
    return [p.strip() for p in parts if p.strip()]


def _math_mask(text: str) -> list:
    """标记每个字符是否处于 LaTeX 数学跨度内（$...$ / $$...$$ / \\[..\\] / \\(..\\)）。"""
    mask = [False] * len(text)
    i, n = 0, len(text)
    in_inline = False
    while i < n:
        c = text[i]
        if c == "\\" and i + 1 < n:
            # 转义字符（含 \$ \( \[ ）整体跳过，不参与定界
            if text[i + 1] == "(" :
                j = text.find("\\)", i + 2)
                j = n if j == -1 else j + 2
                for k in range(i, j):
                    mask[k] = True
                i = j
                continue
            if text[i + 1] == "[":
                j = text.find("\\]", i + 2)
                j = n if j == -1 else j + 2
                for k in range(i, j):
                    mask[k] = True
                i = j
                continue
            i += 2
            continue
        if c == "$":
            # $$ 视作切换显示公式；这里统一按 $ 切换处理足够
            in_inline = not in_inline
            mask[i] = True
            i += 1
            continue
        if in_inline:
            mask[i] = True
        i += 1
    return mask


def _count_words(s: str, lang: str) -> int:
    if lang == "zh":
        return len(re.findall(r"[一-鿿]", s)) + len(re.findall(r"[A-Za-z]+", s))
    return len(re.findall(r"[A-Za-z][A-Za-z'\-]*", s))


# ──────────────────────────────────────────────────────────────────────────
# 各检查
# ──────────────────────────────────────────────────────────────────────────

def _check_wordset(text: str, words, code, sev, msg, ci=True) -> list:
    issues = []
    flags = re.IGNORECASE if ci else 0
    for w in sorted(words):
        pat = re.escape(w)
        # 含连字符/非字母边界的词不强加 \b 右边界
        rx = re.compile(rf"(?<![A-Za-z]){pat}(?![A-Za-z])", flags) if re.match(r"^[\w\-']+$", w) \
            else re.compile(pat, flags)
        hits = list(rx.finditer(text))
        if hits:
            issues.append(Issue(sev, code, f"{msg}：'{w}' ×{len(hits)}",
                                line=_line_of(text, hits[0].start()),
                                count=len(hits),
                                examples=[w]))
    return issues


def _check_patterns(text: str, patterns, code, sev, msg, ci=True) -> list:
    issues = []
    flags = re.IGNORECASE if ci else 0
    for p in patterns:
        rx = re.compile(p, flags)
        hits = list(rx.finditer(text))
        if hits:
            issues.append(Issue(sev, code, f"{msg}：{hits[0].group(0)!r} ×{len(hits)}",
                                line=_line_of(text, hits[0].start()),
                                count=len(hits),
                                examples=[h.group(0) for h in hits[:3]]))
    return issues


def _check_superficial_ing(text: str) -> list:
    rx = re.compile(
        r",\s+(?:high?lighting|underscoring|showcasing|emphasizing|demonstrating|"
        r"illustrating|reflecting|signaling|signalling|paving|reinforcing|"
        r"highlighting)\b[^.,;]*",
        re.IGNORECASE)
    hits = list(rx.finditer(text))
    if hits:
        return [Issue(SEV_WARN, "AI_SUPERFICIAL_ING",
                      f"悬垂 -ing 伪洞见（如 '…, highlighting the …'）×{len(hits)}，建议改为独立陈述句或删除",
                      line=_line_of(text, hits[0].start()), count=len(hits),
                      examples=[h.group(0).strip()[:50] for h in hits[:3]])]
    return []


def _check_negative_parallel(text: str) -> list:
    out = []
    for p, m in [
        (r"\bnot\s+only\b[^.;]{1,60}?\bbut\s+(?:also\s+)?", "not only … but also"),
        (r"\bit'?s\s+not\s+just\b[^.;]{1,40}?\bit'?s\b", "it's not just … it's"),
        (r"不仅[^。；]{1,30}?(?:而且|还|也)", "不仅……而且……"),
    ]:
        hits = list(re.finditer(p, text, re.IGNORECASE))
        if hits:
            out.append(Issue(SEV_WARN, "AI_NEG_PARALLEL",
                             f"否定式平行 '{m}' ×{len(hits)}，AI 高频句式，建议直陈",
                             line=_line_of(text, hits[0].start()), count=len(hits)))
    return out


def _check_emdash(text: str, sentences: int) -> list:
    # em dash (—) U+2014 与 en dash (–) U+2013 作插入语，以及空格连字符 " - "
    n_em = text.count("—") + text.count("–")
    n_sp = len(re.findall(r"\s-\s", text))
    total = n_em + n_sp
    thr = max(2, sentences // 8)
    if total > thr:
        return [Issue(SEV_WARN, "AI_EMDASH",
                      f"破折号/插入语偏多 ×{total}（句数 {sentences}，阈值 {thr}）；建议改逗号、冒号或拆句",
                      count=total)]
    if total:
        return [Issue(SEV_INFO, "AI_EMDASH", f"破折号 ×{total}（在阈值内）", count=total)]
    return []


def _check_mech_connectives(text: str, words, sentences: int, lang: str) -> list:
    total = 0
    first_line = 0
    for w in words:
        if lang == "zh":
            rx = re.compile(re.escape(w))
        else:
            rx = re.compile(rf"(?:^|[.!?]\s+|\n)\s*{re.escape(w)}\b", re.IGNORECASE)
        hits = list(rx.finditer(text))
        if hits and not first_line:
            first_line = _line_of(text, hits[0].start())
        total += len(hits)
    thr = max(2, sentences // 6)
    if total > thr:
        return [Issue(SEV_WARN, "AI_MECH_CONNECTIVE",
                      f"机械连接词扎堆 ×{total}（句数 {sentences}，阈值 {thr}）；多数可删，靠逻辑自然衔接",
                      line=first_line, count=total)]
    return []


def _check_possessive(text: str) -> list:
    # 仅当像"名字/型号"才报：全大写缩写、含数字、或驼峰
    rx = re.compile(r"\b([A-Z][A-Za-z0-9\+\-]*?)['’]s\b")
    bad = []
    for m in rx.finditer(text):
        tok = m.group(1)
        if tok in {"It", "That", "This", "There", "Here", "One", "He", "She", "Who"}:
            continue
        if tok.isupper() and len(tok) >= 2 or any(ch.isdigit() for ch in tok) \
           or re.search(r"[a-z][A-Z]", tok):
            bad.append(m.group(0))
    if bad:
        return [Issue(SEV_WARN, "STYLE_POSSESSIVE",
                      f"方法/模型名所有格 ×{len(bad)}（如 {bad[0]}）；顶刊偏好 'the X of {bad[0][:-2]}' 结构",
                      count=len(bad), examples=bad[:3])]
    return []


def _check_burstiness(sentences_list, lang) -> list:
    lens = [_count_words(s, lang) for s in sentences_list]
    lens = [x for x in lens if x > 0]
    if len(lens) < 5:
        return []
    mean = sum(lens) / len(lens)
    var = sum((x - mean) ** 2 for x in lens) / len(lens)
    sd = var ** 0.5
    cv = sd / mean if mean else 0
    msg = f"句长 mean={mean:.1f} sd={sd:.1f} cv={cv:.2f}（min {min(lens)} / max {max(lens)}）"
    if cv < 0.35:
        return [Issue(SEV_WARN, "AI_MONOTONE",
                      f"句长过于均匀（cv={cv:.2f}<0.35），节奏机械疑似 AI；建议长短句交替。{msg}")]
    return [Issue(SEV_INFO, "AI_MONOTONE", msg)]


def _check_passive(text: str) -> list:
    # 粗略：be 动词 + 过去分词(-ed/常见不规则)
    rx = re.compile(r"\b(?:is|are|was|were|be|been|being)\s+(?:\w+ly\s+)?"
                    r"(?:\w+ed|done|made|shown|found|given|taken|seen|known|built|"
                    r"set|used|based|proposed|trained|tested)\b", re.IGNORECASE)
    n = len(rx.findall(text))
    sents = len(_split_sentences(text, "en"))
    if sents == 0:
        return []
    ratio = n / sents
    sev = SEV_WARN if ratio > 0.6 else SEV_INFO
    return [Issue(sev, "STYLE_PASSIVE",
                  f"被动结构 ≈{n} 处 / {sents} 句（{ratio:.0%}）"
                  + ("；偏高，适度改主动可提升可读性" if sev == SEV_WARN else ""))]


def _check_latex(text: str) -> list:
    out = []
    mask = _math_mask(text)
    # 未转义特殊字符（数学外、非 \ 转义）
    spec_sev = {"%": (SEV_FAIL, "会注释掉整行"), "&": (SEV_WARN, "表格外会报 alignment 错"),
                "#": (SEV_INFO, "正文中应为 \\#"), "_": (SEV_INFO, "正文中应为 \\_（命令参数内可忽略）")}
    counts = {k: [] for k in spec_sev}
    for i, c in enumerate(text):
        if c in spec_sev and not mask[i]:
            prev = text[i - 1] if i else ""
            if prev != "\\":
                counts[c].append(i)
    for ch, positions in counts.items():
        if positions:
            sev, why = spec_sev[ch]
            out.append(Issue(sev, "LATEX_UNESCAPED",
                             f"未转义 '{ch}' ×{len(positions)}（{why}）；应写 '\\{ch}'",
                             line=_line_of(text, positions[0]), count=len(positions)))
    # $ 配平
    n_dollar = sum(1 for i, c in enumerate(text)
                   if c == "$" and (i == 0 or text[i - 1] != "\\"))
    if n_dollar % 2 == 1:
        out.append(Issue(SEV_FAIL, "LATEX_MATH_UNBALANCED",
                         f"行内数学定界符 '$' 出现 {n_dollar} 次（奇数），未配平"))
    # Markdown 污染
    md = list(re.finditer(r"\*\*[^*]+\*\*|(?<!\w)__[^_]+__|^\s{0,3}#{1,6}\s", text, re.MULTILINE))
    if md:
        out.append(Issue(SEV_WARN, "LATEX_MARKDOWN",
                         f"LaTeX 中混入 Markdown ×{len(md)}（如 {md[0].group(0).strip()[:20]!r}）；"
                         f"加粗应用 \\textbf{{}}，标题用 \\section{{}}",
                         line=_line_of(text, md[0].start()), count=len(md)))
    return out


def _check_word_markdown(text: str) -> list:
    md = list(re.finditer(r"\*\*[^*]+\*\*|(?<!\w)__[^_]+__|(?<!\*)\*[^*\s][^*]*\*|"
                          r"^\s{0,3}#{1,6}\s|^\s{0,3}[-*+]\s|`[^`]+`|\[[^\]]+\]\([^)]+\)",
                          text, re.MULTILINE))
    if md:
        return [Issue(SEV_FAIL, "WORD_MARKDOWN",
                      f"Word/纯文本端残留 Markdown 标记 ×{len(md)}（如 {md[0].group(0).strip()[:20]!r}）；"
                      f"必须清成纯文本才能粘进 Word",
                      line=_line_of(text, md[0].start()), count=len(md))]
    return []


def _check_fullwidth(text: str) -> list:
    # 半角标点紧邻中文字符 → 建议全角
    rx = re.compile(r"[一-鿿]\s?([,;:!?])|([,;:!?])\s?[一-鿿]")
    hits = list(rx.finditer(text))
    # 排除小数/英文缩写场景较难，给 WARN 让人确认
    if len(hits) >= 2:
        return [Issue(SEV_WARN, "ZH_HALFWIDTH",
                      f"中文文本中疑似半角标点 ×{len(hits)}；中文正文应用全角，。；：！？",
                      line=_line_of(text, hits[0].start()), count=len(hits))]
    return []


# ──────────────────────────────────────────────────────────────────────────
# V2 academic-writing contract checks (advisory unless noted)
# ──────────────────────────────────────────────────────────────────────────

_NOT_BUT_PATTERNS = (
    ("不是…而是…", r"不是[^。！？；\n]{0,80}而是"),
    ("并非…而是…", r"并非[^。！？；\n]{0,80}而是"),
    ("不在于…而在于…", r"不在于[^。！？；\n]{0,80}而在于"),
    ("并不是…", r"并不是"),
    ("而不是…", r"而不是"),
    ("not ... but ...", r"\bnot\b[^.!?;\n]{1,100}\bbut\b"),
    ("rather than", r"\brather\s+than\b"),
    ("is not ... instead", r"\bis\s+not\b[^.!?;\n]{1,80}[;,]\s*instead\b"),
    ("does not ... but ...", r"\bdoes\s+not\b[^.!?;\n]{1,80}\bbut\b"),
    ("not simply ... but ...", r"\bnot\s+simply\b[^.!?;\n]{1,80}\bbut\b"),
)


def _check_not_but_cluster(text: str) -> list:
    """Flag clustered contrastive templates without banning one necessary contrast."""
    matches = []
    for name, pattern in _NOT_BUT_PATTERNS:
        for hit in re.finditer(pattern, text, re.IGNORECASE):
            matches.append((hit.start(), hit.end(), name, hit.group(0)))
    matches.sort()
    if len(matches) < 2:
        return []

    paragraph_counts = {}
    for start, _end, _name, _value in matches:
        paragraph = text.count("\n\n", 0, start)
        paragraph_counts[paragraph] = paragraph_counts.get(paragraph, 0) + 1
    sentence_index = []
    for start, _end, _name, _value in matches:
        # This intentionally tolerates mixed Chinese/English punctuation.
        sentence_index.append(len(re.findall(r"[.!?。！？；]", text[:start])))
    local_cluster = any(
        sentence_index[i + 1] - sentence_index[i] <= 2
        for i in range(len(sentence_index) - 1)
    )
    same_paragraph_cluster = any(count >= 2 for count in paragraph_counts.values())
    document_template_cluster = len(matches) >= 3
    if not (local_cluster or same_paragraph_cluster or document_template_cluster):
        return []

    examples = [value.strip()[:80] for _start, _end, _name, value in matches[:4]]
    out = [Issue(
        SEV_WARN,
        "NOT_BUT_CLUSTER",
        "NOT_BUT_CONSTRUCTION_CLUSTER：对比/防御句式在局部或全文聚集；保留必要边界并优先正面直陈",
        line=_line_of(text, matches[0][0]),
        count=len(matches),
        examples=examples,
    )]
    # A separate stable code makes the repeated-defensive-contrast contract easy
    # for downstream workflows to consume without treating one contrast as an error.
    if same_paragraph_cluster or document_template_cluster:
        out.append(Issue(
            SEV_WARN,
            "REPEATED_DEFENSIVE_CONTRAST",
            "同一段或全文重复表达防御性边界；检查 STORY_RELEVANCE_AND_DEFENSE_AUDIT，必要边界只保留最精确的一次",
            line=_line_of(text, matches[0][0]),
            count=len(matches),
            examples=examples,
        ))
    return out


def _check_manual_line_break(text: str, mode: str) -> list:
    """Detect prose line-break artifacts while allowing syntax-oriented lines."""
    hits = []
    for match in re.finditer(r"<br\s*/?>|\u2028|\u2029|\x0b", text, re.IGNORECASE):
        hits.append((match.start(), match.group(0)))
    for match in re.finditer(r"[ \t]{2,}\r?\n", text):
        hits.append((match.start(), "Markdown hard break"))

    # In Markdown/plain/Word prose, a single newline between two ordinary
    # non-empty lines is a soft break. Blank lines remain normal paragraph
    # boundaries. Structural table/list/code lines are excluded.
    if mode != "latex":
        lines = text.splitlines(keepends=True)
        offset = 0
        in_fence = False
        for index, raw in enumerate(lines[:-1]):
            line = raw.rstrip("\r\n")
            next_line = lines[index + 1].rstrip("\r\n")
            stripped = line.strip()
            next_stripped = next_line.strip()
            if stripped.startswith(("```", "~~~")) or next_stripped.startswith(("```", "~~~")):
                in_fence = not in_fence
            section_heading = lambda value: bool(re.fullmatch(
                r"(?:#{1,6}\s*)?(?:abstract|introduction|methods?|results?|discussion|conclusion|supplement(?:ary)?|appendix)\s*:?.*",
                value,
                re.IGNORECASE,
            ))
            structural = (
                not stripped or not next_stripped or in_fence
                or stripped.startswith(("|", ">", "#", "- ", "* ", "+ "))
                or next_stripped.startswith(("|", ">", "#", "- ", "* ", "+ "))
                or section_heading(stripped)
                or section_heading(next_stripped)
            )
            if not structural and raw.endswith(("\n", "\r")):
                # A hard break was already recorded above; keep one issue per
                # location and let the message explain the most likely cause.
                newline_pos = offset + len(raw.rstrip("\r\n"))
                if not any(pos == newline_pos for pos, _kind in hits):
                    hits.append((newline_pos, "soft line break"))
            offset += len(raw)

    if not hits:
        return []
    kinds = sorted({kind for _pos, kind in hits})
    return [Issue(
        SEV_WARN,
        "MANUAL_LINE_BREAK",
        "正文含手动/软换行（" + ", ".join(kinds) + "）；使用正常段落边界，代码/公式/表格语法例外",
        line=_line_of(text, hits[0][0]),
        count=len(hits),
        examples=[kind for _pos, kind in hits[:4]],
    )]


def _table_line_cells(line: str, mode: str):
    """Return rough table cell payloads for the two supported text syntaxes."""
    stripped = line.strip()
    if mode in {"markdown", "plain", "word", "docx"} and "|" in stripped:
        body = stripped[1:-1] if stripped.startswith("|") and stripped.endswith("|") else stripped
        return [cell for cell in re.split(r"(?<!\\)\|", body)]
    if mode == "latex" and "&" in stripped:
        body = re.sub(r"\\\\\s*$", "", stripped)
        return body.split("&")
    return []


def normalize_table_cell_whitespace(text: str, mode: str = "markdown") -> str:
    """Trim table-cell edges without changing table delimiters or prose.

    This helper is intentionally conservative: it only rewrites lines that
    look like Markdown/LaTeX table rows. It is useful to artifact generators;
    the linter itself reports the candidate and does not mutate user text.
    """
    lines = text.splitlines(keepends=True)
    output = []
    for raw in lines:
        ending = ""
        body = raw
        if raw.endswith("\r\n"):
            body, ending = raw[:-2], "\r\n"
        elif raw.endswith(("\n", "\r")):
            body, ending = raw[:-1], raw[-1]
        if mode == "markdown" and "|" in body:
            leading = body[: len(body) - len(body.lstrip())]
            stripped = body.strip()
            outer_left = stripped.startswith("|")
            outer_right = stripped.endswith("|")
            core = stripped[1:-1] if outer_left and outer_right else stripped
            cells = [cell.strip() for cell in re.split(r"(?<!\\)\|", core)]
            rebuilt = "|".join(cells)
            if outer_left:
                rebuilt = "|" + rebuilt
            if outer_right:
                rebuilt += "|"
            output.append(leading + rebuilt + ending)
        elif mode == "latex" and "&" in body:
            suffix = ""
            match = re.search(r"(\\\\\s*)$", body)
            if match:
                suffix = match.group(1)
                body = body[: match.start()]
            cells = [cell.strip() for cell in body.strip().split("&")]
            output.append(" & ".join(cells) + suffix + ending)
        else:
            output.append(raw)
    return "".join(output)


def _check_cell_leading_whitespace(text: str, mode: str) -> list:
    issues = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        cells = _table_line_cells(line, mode)
        if not cells:
            continue
        # Markdown separator rows are formatting, not data cells.
        if all(not cell.strip() or re.fullmatch(r":?-{2,}:?", cell.strip()) for cell in cells):
            continue
        bad_leading = [cell for cell in cells if re.match(r"^(?:\t| {2,}|　{2,})", cell)]
        bad_trailing = [cell for cell in cells if re.search(r"[ \t　]+$", cell)]
        if bad_leading or bad_trailing:
            examples = [repr(cell) for cell in (bad_leading + bad_trailing)[:4]]
            issues.append(Issue(
                SEV_WARN,
                "CELL_LEADING_WHITESPACE",
                "表格单元格存在开头两个空格/全角空格/tab或尾随空白；应用 THREE_LINE_TABLE_CONTRACT 前 trim",
                line=line_number,
                count=len(bad_leading) + len(bad_trailing),
                examples=examples,
            ))
    return issues


def _section_for_line(lines: list[str], line_index: int) -> str:
    current = "body"
    for line in lines[: line_index + 1]:
        value = line.strip().lower().rstrip(":")
        if re.fullmatch(r"(?:abstract|introduction|methods?|results?|discussion|conclusion|supplement(?:ary)?|appendix)", value):
            current = value
        elif re.fullmatch(r"(?:fig(?:ure)?|table)\s*[s]?\d+.*", value):
            current = "artifact"
    return current


def _check_repeated_low_value_numbers(text: str, mode: str) -> list:
    """Warn on repeated exact numbers when no section-level allowance applies."""
    lines = text.splitlines()
    occurrences = {}
    number_rx = re.compile(r"(?<![A-Za-z0-9])(?:\d{2,}(?:\.\d+)?|\d+\.\d+)(?:\s*%|\s*[A-Za-zµ²]+)?")
    for line_index, line in enumerate(lines):
        if mode in {"markdown", "latex"} and _table_line_cells(line, mode):
            # Self-contained artifact rows are allowed to repeat a value.
            continue
        for hit in number_rx.finditer(line):
            token = re.sub(r"\s+", "", hit.group(0)).lower()
            occurrences.setdefault(token, []).append((line_index, hit.start()))

    issues = []
    allowed_pairs = {
        frozenset({"abstract", "methods"}),
        frozenset({"abstract", "results"}),
        frozenset({"results", "discussion"}),
        frozenset({"abstract", "methods", "results"}),
    }
    for token, positions in sorted(occurrences.items()):
        if len(positions) < 2:
            continue
        sections = {_section_for_line(lines, index) for index, _column in positions}
        if sections == {"artifact"}:
            continue
        if frozenset(sections) in allowed_pairs:
            continue
        examples = [f"L{index + 1}:{lines[index].strip()[:70]}" for index, _column in positions[:3]]
        issues.append(Issue(
            SEV_WARN,
            "REPEATED_LOW_VALUE_NUMBER_CANDIDATE",
            f"REPEATED_LOW_VALUE_NUMBER：精确数值 {token!r} 出现 {len(positions)} 次；核对 FACT_PLACEMENT_LEDGER，必要报告可保留",
            line=positions[1][0] + 1,
            count=len(positions),
            examples=examples,
        ))
    return issues


def _check_repeated_figure_citations(text: str) -> list:
    citation_rx = re.compile(
        r"\b(?:(supplementary)\s+)?(fig(?:ure)?|table)\.?\s*([s]?\d+)\b",
        re.IGNORECASE,
    )
    grouped = {}
    for hit in citation_rx.finditer(text):
        prefix = "supplementary " if hit.group(1) else ""
        key = f"{prefix}{hit.group(2).lower()} {hit.group(3).lower()}"
        grouped.setdefault(key, []).append(hit)
    issues = []
    for key, hits in sorted(grouped.items()):
        if len(hits) < 2:
            continue
        issues.append(Issue(
            SEV_WARN,
            "REPEATED_FIGURE_CITATION_CANDIDATE",
            f"REPEATED_FIGURE_CITATION：{key} 在正文中出现 {len(hits)} 次；仅在新的 substantive claim 需要时保留后续引用",
            line=_line_of(text, hits[1].start()),
            count=len(hits),
            examples=[hit.group(0) for hit in hits[:4]],
        ))
    return issues


def _check_figure_table_order(text: str) -> list:
    """Advisory first-use order check for figures and tables."""
    citation_rx = re.compile(
        r"\b(?:(supplementary)\s+)?(fig(?:ure)?|table)\.?\s*([s]?\d+)\b",
        re.IGNORECASE,
    )
    first_seen = {"figure": [], "table": []}
    seen_keys = set()
    for hit in citation_rx.finditer(text):
        kind = "figure" if hit.group(2).lower().startswith("fig") else "table"
        raw_number = hit.group(3).lower().lstrip("s")
        key = (kind, bool(hit.group(1)), raw_number)
        if key in seen_keys:
            continue
        seen_keys.add(key)
        try:
            first_seen[kind].append((int(raw_number), hit))
        except ValueError:
            continue
    issues = []
    for kind, ordered in first_seen.items():
        numbers = [number for number, _hit in ordered]
        if numbers != sorted(numbers):
            first_out_of_order = next(
                index for index in range(1, len(numbers)) if numbers[index] < numbers[index - 1]
            )
            hit = ordered[first_out_of_order][1]
            issues.append(Issue(
                SEV_WARN,
                "FIGURE_TABLE_ORDER",
                f"{kind} first-citation order is {numbers}; check numbering and caption-text consistency",
                line=_line_of(text, hit.start()),
                count=len(numbers),
                examples=[str(number) for number in numbers],
            ))
    return issues


def _check_hedge_stack(text: str, lang: str) -> list:
    """Flag multiple near-synonymous hedges in one sentence; never remove them."""
    terms = (r"\b(?:may|might|possibly|potentially|perhaps|could|possibly)\b"
             if lang == "en" else r"可能|或许|也许|潜在(?:地)?")
    hits = []
    for sentence in _split_sentences(text, lang):
        matches = list(re.finditer(terms, sentence, re.IGNORECASE))
        if len(matches) >= 2:
            position = text.find(sentence)
            hits.append((position, sentence.strip()[:100], len(matches)))
    if not hits:
        return []
    return [Issue(SEV_WARN, "HEDGE_STACK", "同一句中有多个近义 hedge；保留最准确表达并维持必要不确定性",
                  line=_line_of(text, hits[0][0]), count=sum(n for _p, _s, n in hits),
                  examples=[s for _p, s, _n in hits[:3]])]


def _check_repeated_causal_disclaimer(text: str) -> list:
    patterns = (r"\b(?:cannot|can not|does not|do not)\s+(?:infer|establish|demonstrate)\s+causal(?:ity| effects?)?\b",
                r"\bnot\s+(?:a\s+)?causal(?: claim| effect| inference)?\b",
                r"(?:不能|无法|不可)(?:据此)?(?:推断|证明|识别)因果(?:关系|效应)?")
    matches = [m for pattern in patterns for m in re.finditer(pattern, text, re.IGNORECASE)]
    if len(matches) < 2:
        return []
    return [Issue(SEV_WARN, "REPEATED_CAUSAL_DISCLAIMER",
                  "可能重复表达因果边界；在最相关位置保留一次，除非各处保护不同 estimand/范围",
                  line=_line_of(text, matches[1].start()), count=len(matches),
                  examples=[m.group(0) for m in matches[:4]])]


def _check_internal_label_prose(text: str) -> list:
    # Candidate-only check: underscore labels often come from code or analysis tables.
    hits = list(re.finditer(r"(?<![A-Za-z0-9])(?:[a-z][a-z0-9]*_){1,}[a-z0-9]+(?![A-Za-z0-9])", text))
    if not hits:
        return []
    return [Issue(SEV_WARN, "INTERNAL_LABEL_TO_PROSE",
                  "疑似内部/code label 原样进入正文；核对是否应转写为自然科学语言或正式定义",
                  line=_line_of(text, hits[0].start()), count=len(hits),
                  examples=[m.group(0) for m in hits[:4]])]


def _check_nonsignificant_attribution(text: str) -> list:
    rx = re.compile(
        r"(?:non[- ]significant|not statistically significant|不显著|未达到统计学显著性)"
        r"[^。！？.!?;\n]{0,100}(?:because|due to|owing to|attribut(?:e|able) to|caused by|由于|归因于|因为)"
        r"[^。！？.!?;\n]{0,100}(?:sample size|power|measurement error|model specification|样本量|统计功效|测量误差|模型设定)",
        re.IGNORECASE,
    )
    hits = list(rx.finditer(text))
    if not hits:
        return []
    return [Issue(SEV_WARN, "NONSIGNIFICANT_RESULT_ATTRIBUTION",
                  "不显著结果被归因于样本量/功效/测量误差/模型设定；确认有额外证据支持该解释",
                  line=_line_of(text, hits[0].start()), count=len(hits),
                  examples=[m.group(0).strip()[:100] for m in hits[:3]])]


def _check_punctuation_density(text: str, lang: str) -> list:
    """Flag unusually dense prose punctuation as a review cue, not a replacement rule."""
    chars = "—–;:：；（），()\"'“”‘’、"
    issues = []
    for sentence in _split_sentences(text, lang):
        # Avoid triggering on short clauses and formula-heavy snippets.
        if len(sentence) < 40:
            continue
        count = sum(sentence.count(ch) for ch in chars)
        if count >= 6:
            pos = text.find(sentence)
            issues.append((pos, sentence.strip()[:100], count))
    if not issues:
        return []
    return [Issue(SEV_WARN, "PUNCTUATION_DENSITY",
                  "句内补充性标点密度偏高；检查是否拆句，同时保留公式、变量和引用所需符号",
                  line=_line_of(text, issues[0][0]), count=sum(n for _p, _s, n in issues),
                  examples=[s for _p, s, _n in issues[:3]])]


def _check_hyphen_noun_chain(text: str) -> list:
    # Deliberately advisory: standardized technical terms and ranges can be valid.
    rx = re.compile(r"(?<![A-Za-z0-9])(?:[A-Za-z]{2,}-){1,}[A-Za-z]{2,}(?![A-Za-z0-9])")
    hits = list(rx.finditer(text))
    if not hits:
        return []
    return [Issue(SEV_INFO, "HYPHEN_NOUN_CHAIN",
                  "发现连字符名词链候选；仅在非标准/非必要时改写，保留正式术语、变量、范围及引用格式",
                  line=_line_of(text, hits[0].start()), count=len(hits),
                  examples=[m.group(0) for m in hits[:4]])]


# ──────────────────────────────────────────────────────────────────────────
# 主入口
# ──────────────────────────────────────────────────────────────────────────

def lint_text(text: str, mode: str = "plain", lang: str = "en") -> list:
    """对一段文本做写作质量检查，返回 Issue 列表。"""
    issues: list = []
    sents = _split_sentences(text, lang)
    n_sent = len(sents)

    if lang == "en":
        issues += _check_wordset(text, AI_TELL_WORDS_EN, "AI_WORD", SEV_WARN, "AI 指纹词")
        issues += _check_patterns(text, AI_TELL_PHRASES_EN, "AI_PHRASE", SEV_WARN, "AI 套话短语")
        issues += _check_wordset(text, PROMO_WORDS_EN, "PROMO", SEV_WARN, "promotional 夸张词")
        issues += _check_patterns(text, VAGUE_ATTR_EN, "VAGUE_ATTR", SEV_WARN, "空泛归因（缺具体引用）")
        issues += _check_superficial_ing(text)
        issues += _check_mech_connectives(text, MECH_CONNECTIVES_EN, n_sent, "en")
        issues += _check_possessive(text)
        issues += _check_passive(text)
    else:  # zh
        issues += _check_wordset(text, set(AI_TELL_WORDS_ZH), "AI_WORD_ZH", SEV_WARN, "中文 AI 味词", ci=False)
        issues += _check_patterns(text, VAGUE_ATTR_ZH, "VAGUE_ATTR_ZH", SEV_WARN, "空泛归因")
        issues += _check_mech_connectives(text, MECH_CONNECTIVES_ZH, n_sent, "zh")
        issues += _check_fullwidth(text)

    issues += _check_negative_parallel(text)
    issues += _check_not_but_cluster(text)
    issues += _check_manual_line_break(text, mode)
    issues += _check_cell_leading_whitespace(text, mode)
    issues += _check_repeated_low_value_numbers(text, mode)
    issues += _check_repeated_figure_citations(text)
    issues += _check_figure_table_order(text)
    issues += _check_hedge_stack(text, lang)
    issues += _check_repeated_causal_disclaimer(text)
    issues += _check_internal_label_prose(text)
    issues += _check_nonsignificant_attribution(text)
    issues += _check_punctuation_density(text, lang)
    issues += _check_hyphen_noun_chain(text)
    issues += _check_emdash(text, n_sent)
    issues += _check_burstiness(sents, lang)

    if mode == "latex":
        issues += _check_latex(text)
    elif mode in ("word", "docx"):
        issues += _check_word_markdown(text)
        if lang == "zh":
            pass  # 全角已在上面查

    # 排序：FAIL > WARN > INFO，再按行号
    order = {SEV_FAIL: 0, SEV_WARN: 1, SEV_INFO: 2}
    issues.sort(key=lambda x: (order.get(x.severity, 9), x.line))
    return issues


def summarize(issues: list) -> dict:
    n_fail = sum(1 for i in issues if i.severity == SEV_FAIL)
    n_warn = sum(1 for i in issues if i.severity == SEV_WARN)
    n_info = sum(1 for i in issues if i.severity == SEV_INFO)
    verdict = "FAIL" if n_fail else ("WARN" if n_warn else "PASS")
    return {"verdict": verdict, "fail": n_fail, "warn": n_warn, "info": n_info,
            "total": len(issues)}


def print_report(issues: list, mode: str, lang: str) -> int:
    s = summarize(issues)
    icon = {SEV_FAIL: "[FAIL]", SEV_WARN: "[WARN]", SEV_INFO: "[info]"}
    print(f"==== writing_lint  (mode={mode}, lang={lang}) ====")
    for it in issues:
        loc = f"  L{it.line}" if it.line else ""
        print(f"{icon.get(it.severity, '[?]')}{loc}  {it.code}: {it.message}")
    badge = {"PASS": "✅ PASS", "WARN": "⚠️  WARN", "FAIL": "❌ FAIL"}[s["verdict"]]
    print(f"---- {badge}  (FAIL {s['fail']} / WARN {s['warn']} / INFO {s['info']}) ----")
    return 2 if s["verdict"] == "FAIL" else (1 if s["verdict"] == "WARN" else 0)


def _main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="SciPilot 学术写作质量 linter")
    ap.add_argument("path", help="文本文件路径；用 '-' 从 stdin 读")
    ap.add_argument("--mode", choices=["latex", "word", "docx", "markdown", "plain"],
                    default="plain", help="文本载体（决定转义/Markdown 检查）")
    ap.add_argument("--lang", choices=["en", "zh"], default="en", help="语言")
    ap.add_argument("--report", default=None, help="把结构化结果写到该 JSON 路径")
    ap.add_argument("--quiet", action="store_true", help="只输出结论行")
    args = ap.parse_args(argv)

    if args.path == "-":
        text = sys.stdin.read()
    else:
        with open(args.path, "r", encoding="utf-8") as f:
            text = f.read()

    issues = lint_text(text, mode=args.mode, lang=args.lang)
    s = summarize(issues)

    if args.report:
        with open(args.report, "w", encoding="utf-8") as f:
            json.dump({"summary": s, "mode": args.mode, "lang": args.lang,
                       "issues": [asdict(i) for i in issues]},
                      f, ensure_ascii=False, indent=2)

    if args.quiet:
        print(f"{s['verdict']}  (FAIL {s['fail']} / WARN {s['warn']} / INFO {s['info']})")
        return 2 if s["verdict"] == "FAIL" else (1 if s["verdict"] == "WARN" else 0)
    return print_report(issues, args.mode, args.lang)


if __name__ == "__main__":
    sys.exit(_main())
