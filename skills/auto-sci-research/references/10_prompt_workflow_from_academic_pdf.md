# Prompt Workflow From Academic PDF

This reference summarizes the workflow structure distilled from the user's local PDF:

the user's local "GPT 学术高级 Prompt 大全_AIplus 高级扩充版" PDF.

The PDF is treated as a private local source for workflow design. Do not copy long prompt text into public skill files. Reuse only the structure, quality logic, and task coverage.

## 1. Distilled Structure

The PDF covers a full research lifecycle:

1. Research topic and problem definition.
2. Literature search and review construction.
3. Research design and methods route.
4. Experiment execution and data analysis.
5. Manuscript writing and structural optimization.
6. Submission, peer review, and academic communication.
7. Quality control and final polishing.

Auto-sci-research maps these seven parts into local skills and adds sport-geography, geospatial, bibliometric, figure, and reproducibility gates.

## 2. How To Use The Prompt Logic

For each task, ask the agent to produce:

- the research decision being made;
- the evidence or data needed;
- the method or analysis route;
- the expected output artifact;
- the risk or reviewer concern;
- the minimal version that can be completed with current resources.

Avoid prompts that only ask for "more ideas" or "better writing". Require structured outputs that can be checked.

## 3. Phase-To-Skill Mapping

| PDF phase | Local implementation | Quality gate |
|---|---|---|
| Topic brainstorming | `agent-auto-sci-methodology` topic matrix | publishable problem, feasible data, measurable contribution |
| Direction narrowing | `agent-auto-sci-methodology` scope audit | not too broad, not merely a method showcase |
| SMART question | `agent-auto-sci-methodology` question table | object, variable, method, comparison, boundary |
| Hypotheses | `agent-auto-sci-methodology` mechanism/competing hypothesis table | falsifiable and tied to data |
| Innovation diagnosis | `agent-auto-sci-methodology` + `agent-auto-sci-scicomm` | contribution is evidence-backed, not promotional |
| Feasibility | `agent-auto-sci-automation` + `agent-auto-sci-methodology` | minimum viable paper and fallback plan |
| Research boundary | `agent-auto-sci-methodology` | explicit scope, exclusion, and causal boundary |
| Keywords | `sport-geography-review-bibliometric` | reproducible Chinese/English keyword system |
| Screening | `sport-geography-review-bibliometric` | inclusion/exclusion criteria and disagreement rule |
| High-impact papers | `urban-exposure-review-radar-workflow` + `sport-geography-review-bibliometric` | classic, method, benchmark, frontier, and controversy papers separated |
| Reading framework | `codex-paper-reader` + `sport-geography-review-bibliometric` | paper notes serve the user's own argument |
| Literature matrix | `sport-geography-review-bibliometric` | evidence matrix, not chronological summaries |
| Gap extraction | `agent-auto-sci-methodology` | fact, method, theory, data, scene, or evaluation gap classified |
| Review reorganization | `agent-auto-sci-scicomm` | theme sentence -> evidence comparison -> limitation -> transition |
| Conceptual framework | `agent-auto-sci-methodology` + `agent-auto-sci-data-viz` | nodes, arrows, assumptions, data link |
| Overall design | `agent-auto-sci-methodology` | main, auxiliary, and robustness analyses |
| Data plan | `agent-auto-sci-automation` + `agent-auto-sci-geospatial` | source, cleaning, privacy, split/versioning |
| Variables and indicators | `agent-auto-sci-methodology` + `agent-auto-sci-geospatial` | operational definition, unit, error, relevance |
| Method choice | `agent-auto-sci-ai-ml` + `agent-auto-sci-methodology` | simple baseline, standard route, advanced route |
| Processing | `agent-auto-sci-geospatial` + `agent-auto-sci-automation` | no leakage, reproducible logs |
| Baselines and ablation | `agent-auto-sci-ai-ml` | fair comparison and component-level evidence |
| Robustness | `agent-auto-sci-data-viz` + `agent-auto-sci-methodology` | alternative data, metric, model, and subgroup checks |
| Statistical tests | `agent-auto-sci-data-viz` | test matches design; effect size and CI considered |
| Error/failure cases | `agent-auto-sci-ai-ml` + `agent-auto-sci-scicomm` | failure conditions are concrete and honest |
| Explainability | `agent-auto-sci-ai-ml` | XAI supports interpretation but is not causal proof |
| Result visualization | `agent-auto-sci-data-viz` | each figure has a claim |
| Title/abstract | `agent-auto-sci-scicomm` | problem, method, result, contribution, boundary |
| Introduction | `sport-geography-sci-writing` | public pressure -> research gap -> contribution |
| Methods writing | `agent-auto-sci-scicomm` | reproducible detail, no results leaked into methods |
| Results writing | `agent-auto-sci-scicomm` + `agent-auto-sci-data-viz` | report evidence before explanation |
| Discussion | `sport-geography-sci-writing` | mechanism, literature dialogue, implication, limitation |
| Polishing | `agent-auto-sci-scicomm` | logic first, language second |
| Journal match | `agent-auto-sci-scicomm` | topic fit, article type, method preference, risk |
| Cover letter | `agent-auto-sci-scicomm` | concise fit and contribution, no exaggeration |
| Reference check | `citation-management` + `agent-auto-sci-scicomm` | format, recency, relevance, missing classics |
| Reviewer response | `agent-auto-sci-scicomm` | concern -> action -> location |
| Final audit | `auto-sci-research` + `agent-auto-sci-methodology` | high-risk issues handled before submission |

## 4. Sport Geography Adaptation

When adapting the PDF's general AI-plus examples to the user's field:

- Replace generic "AI improves accuracy" with a spatial or public-health question.
- Replace generic datasets with POI, OSM, population grids, survey, mobility, NDVI, LST, LCZ, land cover, built environment, and administrative/statistical data.
- Replace generic model metrics with accessibility, exposure, equity, uncertainty, spatial autocorrelation, model validation, and policy-priority evidence.
- Add map compliance, CRS, scale, boundary, and ecological fallacy checks.
- Treat SHAP and feature importance as mechanism clues, not causal proof.

## 5. Reusable Prompt Pattern

Use this compact template instead of copying long prompts:

```text
请作为[角色]，围绕[研究主题/材料]完成[具体任务]。
必须输出：[结构化表格或清单]。
每一项都要说明：研究意义、可用证据、方法路径、质量检查、风险边界、最小可行版本。
请避免泛泛表述，不要把相关性或模型重要性写成因果结论。
```

For manuscript writing:

```text
请基于[claim-evidence map/结果表/图件]撰写[章节]。
要求：先明确本段功能，再写连贯段落；每个核心主张必须对应证据；讨论可提出机制解释，但要标明证据边界；不要编造引用。
```

## 6. Copyright And Release Boundary

The PDF may guide local workflow design. Public skill files should include:

- phase names;
- task categories;
- quality gates;
- adapted local templates;
- source attribution as a local private input.

Public skill files should not include:

- long verbatim prompt blocks;
- full PDF text;
- screenshots or extracted pages;
- any paid or non-public distribution material.
