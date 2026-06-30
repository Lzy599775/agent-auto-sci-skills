# scipilot-writing-skill

> SciPilot Skills family. Academic **writing & polishing co-pilot** — a top-journal editor and a harsh reviewer, built into your workflow.
> SciPilot Skills 家族成员 — 学术论文**写作与润色副驾驶**：把"顶刊编辑 + 严苛审稿人"装进你的写作流程。

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python: 3.9+](https://img.shields.io/badge/Python-3.9%2B-3776AB.svg)](#依赖--dependencies)
[![Status: v1.0.0](https://img.shields.io/badge/Status-v1.0.0-success.svg)](#)
[![Mode](https://img.shields.io/badge/Mode-Editor%2BReviewer-c41e3a.svg)](#为什么这不只是一份-prompt-清单)
[![Lint](https://img.shields.io/badge/Quality-machine--checked-orange.svg)](#写作质量证据链)
[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-orange.svg)](https://claude.com/claude-code)

A [Claude Code](https://claude.com/claude-code) / [Codex](https://github.com/openai/codex) / Cursor Skill that takes scientific text the last mile: from a Chinese draft, a rough paragraph, or a whole section, to **submission-grade** English (or Chinese) prose. It covers translation, condensing, expanding, polishing, de-AI / humanizing, logic checking, section drafting (Title / Abstract / Introduction-CARS / Methods / Results / Discussion), figure & table captions, results analysis, reviewer-style self-check, cover letters, and rebuttals. Unlike a prompt cookbook, **writing quality here is a machine-checked contract**: every delivery passes `writing_lint.py` (deterministic AI-tell / LaTeX-escape / Markdown-contamination / full-width-punctuation checks) plus an AI read-back self-review loop.

> [中文文档](#中文文档) | [English](#english)

---

## 中文文档

### 概览

科研写作最磨人的，往往不是"不会写"，而是反复调润色 prompt、改完不知道好没好、投出去才发现满是
中文乱标点 / LaTeX 没转义 / 读着一股 AI 味。`scipilot-writing-skill` 是 SciPilot 家族的写作成员，
专治这"最后一公里"——**先判断后下笔，宁缺毋滥，改完必自检。**

### 为什么这不只是一份 prompt 清单

```
普通写作 prompt 清单          scipilot-writing-skill
──────────────────         ──────────────────────
复制 prompt → 粘贴 →  改完   先按 Stage 0 问清：任务/载体/目标刊/语言/学科/保守度
凭感觉觉得"好像不错"          改写走三段式：改后文 + 回译核对 + 修改日志
                            机器自检 writing_lint：AI 指纹/转义/全角/被动/节奏
                            AI 读稿审稿人视角自审：逻辑/夸大/AI味/一致性 → 回改
                            诚信红线：只动表达不动数值/方向/结论，绝不臆造引用
```

### 写作质量证据链

这是 SciPilot 家族的统一签名——把"写得好"从口头承诺变成机器可核对的记录，与
`scipilot-figure-skill` 的视觉自检闭环、`scipilot-cite-skill` 的幻觉门控同源。

```
改写 → writing_lint.py 机器自检（确定性指纹）
        + AI 读稿审稿人自审（感知/逻辑问题）
                  ↓ 发现问题
        回改 → 重检，最多 3 轮，残留如实标注
```

- **机器抓确定性问题**：`writing_lint.py` 命中即报——中英 AI 指纹词、机械连接词、悬垂 -ing、
  否定式平行、破折号密度、空泛归因、模型名所有格、LaTeX 未转义、Word 端残留 Markdown、
  中文半角标点、被动比例、句长节奏（burstiness）。输出 `lint_report.json`。
- **AI 读稿抓感知问题**：节奏是否机械、是否 overclaim、术语是否漂移——这些程序查不出。
- **诚信复核**：diff 确认没动任何数值、公式、引用键、结论方向。

### 核心工作流（Stage 0–7）

```
0. 信息收集 ── 任务/载体/目标刊/语言/学科/保守度（必问，禁止默默假设）
   ↓
1. 解析载体 ── .tex / .docx / .md / 纯文本，定位处理范围
   ↓
2. 选路由   ── prompt_library + section_playbooks + journal_styles
   ↓
3. 起草改写 ── 三段式：改后文 + 回译核对 + 修改日志
   ↓
4. 机器自检 ── writing_lint.py（Gate，命中 FAIL 必处理）
   ↓
5. AI 自审  ── 审稿人视角读稿，发现问题回 3，最多 3 轮
   ↓
6. 一致性诚信复核 ── 术语/缩写/时态/数字/US-UK；diff 确认未动事实
   ↓
7. 交付报告 ── 做了什么 + lint 摘要 + 残留项 + 家族协作建议
```

### 七条铁律（IRON RULES）

1. **诚信**：只动表达，绝不改数据/数值/方向/结论，绝不臆造文献或结果。
2. **宁缺毋滥**：原文已好就保留并肯定，不为换词而换词。
3. **透明可溯**：绝不静默重写，永远给三段式（改后文 + 回译 + 修改日志）。
4. **去 AI 味但留人味**：删 AI 指纹，但保留作者观点、节奏与术语。
5. **格式纯净随载体**：LaTeX 转义、Word 全角纯文本、拒绝无谓列表化。
6. **断言=证据**：hedging/boosting 匹配证据强度，绝不 overclaim，绝不把相关说因果。
7. **机检门控**：交付前必跑 `writing_lint.py`，FAIL 必处理，不伪造检查。

### 覆盖的写作任务（同类清单的全部 + 更多）

中译英润色 · 英译中 · 中文重写 · 缩写 · 扩写 · 英文润色 · 中文润色 · 逻辑检查 ·
去 AI 味(中/英) · 图标题 · 表标题 · 实验结果分析 · 审稿人视角自检 —— 以上对齐同类 prompt 清单；
**额外**：Title 创作 · Abstract 起草 · Introduction(CARS) · Methods/Results/Discussion 起草 ·
**Cover letter** · **Rebuttal / 审稿回复** —— 高水平 SCI 高频、同类清单普遍缺失的能力。

### 安装

```
请帮我安装这个 Skill：https://github.com/Haojae/scipilot-writing-skill.git
```

或手动：

```bash
git clone https://github.com/Haojae/scipilot-writing-skill.git \
          ~/.claude/skills/scipilot-writing-skill
# 仅处理 .docx 时才需要：
pip install python-docx
```

`writing_lint.py` / `latex_clean.py` / `text_stats.py` 只用 Python 标准库，开箱即用。

### 命令行直接调脚本

```bash
# 写作质量机检（核心）
python scripts/writing_lint.py draft.tex --mode latex --lang en --report lint_report.json
python scripts/writing_lint.py draft.txt --mode word  --lang zh

# LaTeX 转义 + 体检
python scripts/latex_clean.py draft.tex --check
python scripts/latex_clean.py draft.tex            # 转义后输出

# 量化指标：句长节奏 / 被动 / 名词化 / hedging
python scripts/text_stats.py draft.txt --lang en

# 读 Word 为纯文本（喂给机检）
python scripts/docx_text.py read paper.docx --to body.txt
```

### SciPilot Skills 家族

| Skill | 状态 | 功能 |
|---|---|---|
| scipilot-cite-skill | [v1.0.0](https://github.com/Haojae/scipilot-cite-skill) | 文献检索与引用插入 |
| scipilot-figure-skill | [v2.1.0](https://github.com/Haojae/scipilot-figure-skill) | 可视化顾问 + 绘制 + 视觉自检闭环 |
| **scipilot-writing-skill** | **v1.0.0 (本仓库)** | **写作与润色 + 写作质量证据链** |
| scipilot-review-skill | 规划中 | AI 模拟审稿 |
| scipilot-submit-skill | 规划中 | 投稿格式适配 |
| scipilot-read-skill | 规划中 | 论文阅读与翻译 |

### 许可证

[MIT](LICENSE) © 2026 Haojae

---

## English

### Overview

The hardest part of scientific writing is rarely "I can't write" — it's re-tuning polish prompts
forever, never knowing if the result is good, and discovering at submission time that the text is
full of half-width punctuation, unescaped LaTeX, or an unmistakable AI smell.
`scipilot-writing-skill` is the writing member of the SciPilot family, built for that last mile:
**judge before you write, change only what needs changing, and always self-check.**

### Why this isn't just a prompt cookbook

```
Generic prompt list          scipilot-writing-skill
──────────────────          ──────────────────────
copy prompt → paste → edit   First asks: task / medium / target journal / language / field / how aggressive
"looks fine I guess"         Rewrites in 3 parts: revised text + back-translation + change log
                             Machine self-check (writing_lint): AI-tells / escapes / passive / rhythm
                             AI read-back as a reviewer: logic / overclaim / AI smell / consistency
                             Integrity line: never touch numbers / direction / conclusions; never fabricate refs
```

### Writing-quality evidence chain

The family signature — turning "it reads well" from a verbal promise into a machine-checkable record,
the same DNA as the visual self-check loop in `scipilot-figure-skill` and the hallucination gate in
`scipilot-cite-skill`.

- **Machine catches deterministic issues**: `writing_lint.py` flags AI-tell words (EN+ZH), mechanical
  connectives, dangling -ing, negative parallelism, em-dash density, vague attribution, possessive on
  model names, unescaped LaTeX specials, Markdown contamination in Word output, half-width punctuation
  in Chinese, passive ratio, and sentence-length burstiness. Emits `lint_report.json`.
- **AI catches perceptual issues**: monotone rhythm, overclaiming, terminology drift — invisible to a linter.
- **Integrity review**: a diff confirms no number, formula, citation key, or conclusion was altered.

### Tasks covered (everything a prompt list does, and more)

zh→en polish · en→zh · Chinese rewrite · condense · expand · English polish · Chinese polish ·
logic check · de-AI (zh/en) · figure caption · table caption · results analysis · reviewer self-check —
all on par with comparable prompt collections. **Plus**: Title ideation · Abstract drafting ·
Introduction (CARS) · Methods/Results/Discussion drafting · **Cover letter** · **Rebuttal** — high-value
for SCI submission and usually missing from prompt lists.

### Installation

```
Please install this Skill for me: https://github.com/Haojae/scipilot-writing-skill.git
```

```bash
git clone https://github.com/Haojae/scipilot-writing-skill.git \
          ~/.claude/skills/scipilot-writing-skill
pip install python-docx   # only needed for .docx I/O
```

### SciPilot Skills family

| Skill | Status | Purpose |
|---|---|---|
| scipilot-cite-skill | [v1.0.0](https://github.com/Haojae/scipilot-cite-skill) | Reference discovery & insertion |
| scipilot-figure-skill | [v2.1.0](https://github.com/Haojae/scipilot-figure-skill) | Visualization advisor + renderer + visual self-check |
| **scipilot-writing-skill** | **v1.0.0 (this repo)** | **Writing & polishing + writing-quality evidence chain** |
| scipilot-review-skill | Planned | AI peer-review simulation |
| scipilot-submit-skill | Planned | Submission formatting |
| scipilot-read-skill | Planned | Paper reading & translation |

### License

[MIT](LICENSE) © 2026 Haojae

### 依赖 / Dependencies

```
# 核心脚本零依赖（Python 3.9+ 标准库）
python-docx>=1.1   # optional; only for reading/writing .docx
```
