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
| `kdense-ml-ai-selected` | Selected upstream K-Dense ML/AI subskills | scikit-learn, PyTorch Lightning, Transformers, SHAP, time-series ML, GNN, UMAP technical playbooks |
| `agent-auto-sci-data-viz` | EDA, statistics, tables, figures, dashboards | EDA report, statistical plan, publication figure plan |
| `kdense-data-viz-selected` | Selected upstream K-Dense data/viz subskills | EDA, statistical analysis, matplotlib, seaborn, scientific visualization, NetworkX, Polars, Dask |
| `scipilot-figure-skill` | Scientific figure advisor and plotter | data profiling, chart selection, publication export, CJK font setup, visual QA loop |
| `agent-auto-sci-geospatial` | GIS, remote sensing, spatial accessibility, spatial ML | spatial workflow, CRS audit, map plan, accessibility pipeline |
| `kdense-geospatial-rs-selected` | Selected upstream K-Dense geospatial and remote-sensing subskills | geomaster and GeoPandas technical workflows |
| `agent-auto-sci-scicomm` | Manuscript writing, slides, posters, peer review, rebuttal | manuscript plan, section draft, response letter, presentation plan |
| `kdense-scicomm-selected` | Selected upstream K-Dense scientific communication subskills | scientific writing, peer review, citations, literature review, slides, posters, schematics |
| `agent-auto-sci-methodology` | Hypothesis, research design, critical appraisal, evidence grading | hypothesis matrix, method critique, risk-of-bias table |
| `urban-exposure-review-radar-workflow` | Urban exposure review workflow, remote-sensing frontier radar, CV-to-RS idea generation, formal corpus/radar handoff | route decision, search/radar protocol, extraction/coding framework, journal evidence gate, project scaffold |

Each `agent-auto-sci-*` subskill now has two layers of references:

- a compact workflow reference that preserves the first version;
- a deeper mapping/playbook reference that adapts AutoSci or K-Dense patterns to sport geography, green/heat exposure, park equity, urban health, and review/bibliometric writing.

## 3. Existing Sport Geography Skills

| Skill | Role | Use when |
|---|---|---|
| `sport-geography-sci-writing` | Empirical SCI manuscript writing for sport geography, green/heat exposure, accessibility and equity | Drafting or revising an empirical paper, figures, discussion, journal route. |
| `sport-geography-review-bibliometric` | Review, systematic review, scoping review and bibliometric manuscripts in sport geography | Search strategy, PRISMA, WoS/Scopus analysis, coding framework, policy agenda. |
| `urban-exposure-review-radar-workflow` | Review/radar workflow for urban exposure, remote sensing, public health linkage, and high-impact journal routing | When the task must first decide among bibliometric review, systematic review, scoping review, narrative review, frontier radar, or empirical design. |

## 4. Related K-Dense Helper Skills

These are not subskills of this project, but they can be invoked as technical helpers when already installed:

- `kdense-ml-ai-selected`: selected K-Dense ML/AI bundle.
- `kdense-data-viz-selected`: selected K-Dense data analysis and visualization bundle.
- `kdense-geospatial-rs-selected`: selected K-Dense geospatial and remote-sensing bundle.
- `kdense-scicomm-selected`: selected K-Dense scientific communication bundle.
- `scipilot-figure-skill`: SciPilot figure advisor for chart selection, plotting, and visual QA.
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
2. If the task is a full research-to-manuscript workflow, read `08_full_research_to_manuscript_pipeline.md` and assign phase owners.
3. If the task is large enough for multiple role-specific agents, read `09_subagent_composition_matrix.md`.
4. If the task asks to reuse prompt-library logic or the local academic prompt PDF, read `10_prompt_workflow_from_academic_pdf.md` and avoid copying long text.
5. If the task asks to integrate the user's local Sportpark writing/figure memories, read `11_sportpark_skill_integration_notes.md` and keep source files untouched unless the user explicitly asks otherwise.
6. If the task is a concrete empirical sport-geography manuscript, use `sport-geography-sci-writing`.
7. If the task asks to decide among review types, add `urban-exposure-review-radar-workflow` before detailed review planning.
8. If the task is a focused sport-geography review or bibliometric paper, use `sport-geography-review-bibliometric`.
9. If the task asks for recent remote-sensing, Geospatial AI, CV-to-RS, heat/green exposure radar, use `urban-exposure-review-radar-workflow` plus `agent-auto-sci-geospatial`.
10. If the task involves spatial data or maps, add `agent-auto-sci-geospatial`.
11. If the task involves ML or SHAP, add `agent-auto-sci-ai-ml`; add `kdense-ml-ai-selected` when upstream package-level technical playbooks are needed.
12. If the task ends in figures/tables/statistics, add `agent-auto-sci-data-viz`; add `kdense-data-viz-selected` for upstream EDA/statistics/visualization playbooks and `scipilot-figure-skill` for chart selection or publication-grade data figures.
13. If the task ends in text, slides, poster, or rebuttal, add `agent-auto-sci-scicomm`; add `kdense-scicomm-selected` for upstream writing, citation, peer-review, slide, poster, or schematic workflows.
14. If the task is about research logic, evidence quality, or hypotheses, add `agent-auto-sci-methodology`.
15. If the task is external web research, use `gpt-researcher` only after checking privacy and source needs.
16. If the task is local paper reading, use `codex-paper-reader` before ad hoc PDF scanning.
17. If the task is broad academic paper orchestration, use `academic-research-suite` or route through `auto-sci-research`.
18. If the task asks to create a new thinking/persona skill, use `huashu-nuwa` and keep local evidence boundaries.
19. If the task asks for writing prompts, use `awesome-ai-research-writing` plus local sport-geography writing rules.

## 7. Full Pipeline Ownership

| Stage | Owner skills |
|---|---|
| Topic and feasibility | `agent-auto-sci-methodology`, `agent-auto-sci-automation` |
| Literature and corpus | `sport-geography-review-bibliometric`, `urban-exposure-review-radar-workflow` |
| Data and spatial processing | `agent-auto-sci-automation`, `agent-auto-sci-geospatial` |
| Modeling and analysis | `agent-auto-sci-ai-ml`, `kdense-ml-ai-selected`, `agent-auto-sci-data-viz`, `kdense-data-viz-selected`, `agent-auto-sci-methodology` |
| Publication figures | `agent-auto-sci-data-viz`, `scipilot-figure-skill`, `agent-auto-sci-geospatial`, `agent-auto-sci-scicomm` |
| Draft and revision | `sport-geography-sci-writing`, `agent-auto-sci-scicomm`, `kdense-scicomm-selected` |
| Reviewer risk and rebuttal | `agent-auto-sci-methodology`, `agent-auto-sci-scicomm` |
| Skill evolution and release | `auto-sci-research`, `agent-auto-sci-automation` |
