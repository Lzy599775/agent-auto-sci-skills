# Subskill Registry

Use this file to choose the right local skill.

## 1. Master Skill

| Skill | Role | Use when |
|---|---|---|
| `auto-sci-research` | Umbrella router and evolution controller | Task spans multiple research stages, asks to update skills, or requires project memory and evolution archive. |

## 2. Auto-sci-research Subskills

| Skill | Role | Typical outputs |
|---|---|---|
| `agent-auto-sci-automation` | Long-horizon research workflow, source ingestion, memory, checkpoints, automation, API setup | workflow plan, source manifest, memory schema, update protocol |
| `agent-auto-sci-ai-ml` | ML/AI modeling, baselines, XAI, model validation | model plan, leakage checklist, SHAP plan, experiment matrix |
| `agent-auto-sci-data-viz` | EDA, statistics, tables, figures, dashboards | EDA report, statistical plan, publication figure plan |
| `agent-auto-sci-geospatial` | GIS, remote sensing, spatial accessibility, spatial ML | spatial workflow, CRS audit, map plan, accessibility pipeline |
| `agent-auto-sci-scicomm` | Manuscript writing, slides, posters, peer review, rebuttal | manuscript plan, section draft, response letter, presentation plan |
| `agent-auto-sci-methodology` | Hypothesis, research design, critical appraisal, evidence grading | hypothesis matrix, method critique, risk-of-bias table |

Each `agent-auto-sci-*` subskill now has two layers of references:

- a compact workflow reference that preserves the first version;
- a deeper mapping/playbook reference that adapts AutoSci or K-Dense patterns to sport geography, green/heat exposure, park equity, urban health, and review/bibliometric writing.

## 3. Existing Sport Geography Skills

| Skill | Role | Use when |
|---|---|---|
| `sport-geography-sci-writing` | Empirical SCI manuscript writing for sport geography, green/heat exposure, accessibility and equity | Drafting or revising an empirical paper, figures, discussion, journal route. |
| `sport-geography-review-bibliometric` | Review, systematic review, scoping review and bibliometric manuscripts in sport geography | Search strategy, PRISMA, WoS/Scopus analysis, coding framework, policy agenda. |

## 4. Related K-Dense Helper Skills

These are not subskills of this project, but they can be invoked as technical helpers when already installed:

- `scikit-learn`, `pytorch-lightning`, `transformers`, `shap`, `aeon`, `timesfm-forecasting`
- `exploratory-data-analysis`, `statistical-analysis`, `matplotlib`, `seaborn`, `scientific-visualization`, `networkx`
- `geomaster`, `geopandas`
- `scientific-writing`, `peer-review`, `scientific-slides`, `scientific-schematics`, `citation-management`
- `hypothesis-generation`, `scientific-critical-thinking`, `scholar-evaluation`

## 5. Newly Deployed External Research Skills

These are installed locally under `<codex-skills-dir>` and are part of the wider `auto-sci-research` system.

| Skill | Source repo | Use when |
|---|---|---|
| `gpt-researcher` | `assafelovic/gpt-researcher` | Autonomous or MCP-style web deep research is needed. |
| `huashu-nuwa` | `alchaincyf/nuwa-skill` | The user wants to distill a person, theme, or thinking framework into a reusable skill. |
| `academic-research-suite` | `Imbad0202/academic-research-skills-codex` | A full academic workflow is needed: deep research, paper writing, reviewing, pipeline, or experiment planning. |
| `codex-autoresearch` | `leo-lilinxiao/codex-autoresearch` | The user wants a long-running improve-verify loop with measurable success criteria. |
| `codex-paper-reader` | `hwang847/codex-paper-reader` | Local literature folders, PDFs, paper indexes, reading packs, screenshots, or HTML reading notes are needed. |
| `codex-academic-skills-index` | `Epsilon617/Codex-Academic-Skills` | The user wants to choose or compare external academic Codex skills without installing too many. |
| `awesome-ai-research-writing` | `STRYXTN/awesome-ai-research-writing` | The user wants reusable academic-writing prompts for translation, polishing, captions, logic checks, or reviewer critique. |

## 6. Routing Rules

1. If the task asks to update the system, start with `auto-sci-research`.
2. If the task is a concrete empirical sport-geography manuscript, use `sport-geography-sci-writing`.
3. If the task is a review or bibliometric paper, use `sport-geography-review-bibliometric`.
4. If the task involves spatial data or maps, add `agent-auto-sci-geospatial`.
5. If the task involves ML or SHAP, add `agent-auto-sci-ai-ml`.
6. If the task ends in figures/tables/statistics, add `agent-auto-sci-data-viz`.
7. If the task ends in text, slides, poster, or rebuttal, add `agent-auto-sci-scicomm`.
8. If the task is about research logic, evidence quality, or hypotheses, add `agent-auto-sci-methodology`.
9. If the task is external web research, use `gpt-researcher` only after checking privacy and source needs.
10. If the task is local paper reading, use `codex-paper-reader` before ad hoc PDF scanning.
11. If the task is broad academic paper orchestration, use `academic-research-suite` or route through `auto-sci-research`.
12. If the task asks to create a new thinking/persona skill, use `huashu-nuwa` and keep local evidence boundaries.
13. If the task asks for writing prompts, use `awesome-ai-research-writing` plus local sport-geography writing rules.

