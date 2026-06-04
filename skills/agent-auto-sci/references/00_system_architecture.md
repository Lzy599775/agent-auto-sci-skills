# Agent Auto Sci System Architecture

Use this file to reason about the umbrella research-agent system.

## 1. Design Goal

The system is a local, evolving research infrastructure for geography + sport science. It should support:

- literature search and paper ingestion;
- review, systematic review, scoping review, and bibliometric work;
- empirical sport-geography SCI manuscripts;
- geospatial and remote-sensing data analysis;
- machine learning and explainable AI;
- statistical analysis and visualization;
- scientific communication, rebuttal, and presentation;
- project memory and skill evolution tracking.

## 2. Adapted AutoSci Pattern

AutoSci/OmegaWiki contributes four transferable ideas:

1. **Wiki-centric memory**: papers, methods, concepts, ideas, experiments, failures, and outputs are structured entities.
2. **Lifecycle automation**: research is a pipeline from source ingestion to discovery, idea generation, experiment design, paper drafting, review, rebuttal, and visualization.
3. **Checkpointed execution**: long workflows create checkpoints, manifests, and logs so they can resume and be audited.
4. **Self-evolution**: feedback, failed experiments, weak ideas, and review criticism update future workflows.

For this user's Codex setup, we do not require AutoSci's full runtime. We translate the pattern into local skills, references, scripts, and HTML records.

## 3. Local Architecture

```text
agent-auto-sci
├── automation          -> research lifecycle, memory, source ingestion, evolution log
├── ai-ml               -> machine learning, deep learning, XAI, model validation
├── data-viz            -> EDA, statistics, tables, publication figures
├── geospatial          -> GIS, remote sensing, spatial accessibility, spatial ML
├── scicomm             -> manuscript, slides, posters, peer review, rebuttal
├── methodology         -> hypotheses, research design, critical appraisal
├── sport empirical     -> sport-geography-sci-writing
└── sport review        -> sport-geography-review-bibliometric
```

## 4. Project Memory Layers

| Layer | Purpose | Default location |
|---|---|---|
| Raw sources | PDFs, data, notes, web pages | project-specific folders |
| Structured tables | literature tables, coding sheets, data dictionaries | `review_literature_library/00_表格与清单` |
| Text extraction | paper text, prompt text, indexes | `review_literature_library/02_PDF文本提取与匹配索引` |
| Skill references | reusable procedures | `<codex-skills-dir>/*/references` |
| Evolution archive | visible progress and skill map | `<project-root>/agent_auto_sci/evolution_archive` |

## 5. Default Research Lifecycle

1. **Define route**: empirical paper, systematic review, bibliometric review, model experiment, map/figure task, or grant/presentation.
2. **Build memory**: source inventory, extraction, DOI/data validation, entity tables.
3. **Design questions**: research questions, hypotheses, concepts, variables, metrics, coding schema.
4. **Analyze**: bibliometrics, coding, statistics, spatial analysis, ML/XAI, visualization.
5. **Synthesize**: claim-evidence map, manuscript plan, figure plan, policy agenda.
6. **Critique**: reviewer-risk scan, evidence boundary check, reproducibility check.
7. **Archive evolution**: update skill docs, evolution JSON, and HTML.

## 6. Quality Gates

- Source gate: every corpus or data source has path, date, inclusion logic, and ownership.
- Method gate: every metric or model has a role in the argument.
- Evidence gate: every major claim has table, figure, citation, or code output.
- Reproducibility gate: scripts, parameters, environment notes, and data boundaries are recorded.
- Safety gate: no secrets, private IDs, or non-shareable raw text in public-facing outputs.


