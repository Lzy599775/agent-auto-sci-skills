# Auto-sci-research

[中文](README.md) | [English](README_EN.md) | [Local showcase](site/index.html) | [Evolution archive](site/agent-auto-sci-evolution.html)

> A Codex-first skill suite for geography, sport science, urban health, GIS/remote sensing, green exposure, sport parks/facilities, spatial equity, literature review, bibliometrics, machine learning, scientific figures, and SCI writing.

`Auto-sci-research` is a reusable research workbench, not a one-click paper generator. It helps ChatGPT and Codex route research tasks across topic design, literature review, source manifests, GIS/RS processing, exposure/accessibility measurement, statistics, ML/XAI, publication figures, manuscript writing, cover letters, rebuttals, and project memory.

The repository contains **19 installable skills**, plus an isolated `academic-research-suite` subskill inside `urban-exposure-review-radar-workflow`.

Latest upstream refresh: **2026-08-01**.

- ARS Codex package updated to `v0.1.22` (`f8d6b06`), carrying ARS `v3.19.0`.
- K-Dense checked at `v2.62.0` (`ad21a38`); 26 of 27 selected subskills were refreshed, while `transformers` had no file-level change.
- SciPilot Figure remains `v2.1.0-1-g43098dd`.
- SciPilot Writing remains `v1.0.0` (`51c5fd3`).
- GeoRS SCI Writing Adapter remains an original adapter because the checked upstream source still has no explicit LICENSE file.

## Installation

```powershell
git clone https://github.com/Lzy599775/agent-auto-sci-skills.git
cd agent-auto-sci-skills
.\scripts\install.ps1
```

Default target:

```text
$env:USERPROFILE\.codex\skills
```

Custom target:

```powershell
.\scripts\install.ps1 -Target "$env:USERPROFILE\.agents\skills"
```

Before public release:

```powershell
.\scripts\scan_public_safety.ps1
```

## Which Skill Should I Use?

| Need | Start with |
|---|---|
| Route a substantive research goal across ChatGPT and Codex | `research-orchestrator` |
| Route a complex multi-stage research task | `auto-sci-research` |
| Search, verify, extract, synthesize literature, or audit citation support | `literature` |
| Build source manifests, checkpoints, and safe automation | `agent-auto-sci-automation` |
| Refine research questions, mechanisms, evidence strength, and causal language | `agent-auto-sci-methodology` |
| Audit GIS, remote sensing, exposure, accessibility, and spatial equity | `agent-auto-sci-geospatial` |
| Design EDA, statistics, bibliometric visuals, and paper figures | `agent-auto-sci-data-viz` |
| Audit ML, SHAP/XAI, leakage, and spatial/temporal validation | `agent-auto-sci-ai-ml` |
| Build manuscript argument, cover letters, rebuttals, and presentations | `agent-auto-sci-scicomm` |
| Write sport geography empirical SCI papers | `sport-geography-sci-writing` |
| Design sport geography reviews and bibliometric manuscripts | `sport-geography-review-bibliometric` |
| Route urban exposure reviews, radar scans, and health database linkage | `urban-exposure-review-radar-workflow` |
| Use a full academic research and paper pipeline | `urban-exposure-review-radar-workflow/subskills/academic-research-suite` |
| Decide what chart to use and produce publication-grade figures | `scipilot-figure-skill` |
| Polish, translate, humanize, write cover letters, or rebut reviews | `scipilot-writing-skill` |
| Write geography/remote-sensing SCI sections | `geors-sci-writing-adapter` |
| Use selected upstream technical playbooks | `kdense-ml-ai-selected`, `kdense-data-viz-selected`, `kdense-geospatial-rs-selected`, `kdense-scicomm-selected` |

## Skill Categories

| Category | Skills |
|---|---|
| Router and automation | `research-orchestrator`, `auto-sci-research`, `agent-auto-sci-automation` |
| Methodology and evidence design | `agent-auto-sci-methodology`, `urban-exposure-review-radar-workflow` |
| Geospatial, RS, exposure, accessibility | `agent-auto-sci-geospatial`, `kdense-geospatial-rs-selected`, `geors-sci-writing-adapter` |
| Data, visualization, ML | `agent-auto-sci-data-viz`, `agent-auto-sci-ai-ml`, `kdense-data-viz-selected`, `kdense-ml-ai-selected`, `scipilot-figure-skill` |
| Review and bibliometrics | `literature`, `sport-geography-review-bibliometric`, `urban-exposure-review-radar-workflow`, `academic-research-suite` |
| Writing and submission | `sport-geography-sci-writing`, `agent-auto-sci-scicomm`, `scipilot-writing-skill`, `geors-sci-writing-adapter`, `kdense-scicomm-selected` |

## Detailed Skill Index

| Skill | Role | Best for | Typical output | Boundary |
|---|---|---|---|---|
| `research-orchestrator` | Cross-surface router | Substantive academic/scientific goals in ChatGPT or Codex | Workflow route, source ref/version, specialist Skill, QC | Retrieves live GitHub rules; discloses fallback instead of silently using stale policy |
| `auto-sci-research` | Router | Multi-stage tasks across topic, literature, data, analysis, figures, writing, submission | Skill sequence, route map, quality gates | Does not replace specialist skills |
| `literature` | Evidence workflow | Literature search, DOI/metadata verification, paper extraction, synthesis, citation-claim audits | Verified corpus, paper notes, evidence traces, support classifications | Manual workflow and golden-set validation precede broad automation |
| `agent-auto-sci-automation` | Automation | Source manifests, checkpoints, project memory, API safety | Manifest, status table, recovery plan | Never stores secrets or private materials |
| `agent-auto-sci-methodology` | Methodology | Research questions, mechanisms, causal language, evidence strength | RQ matrix, mechanism map, bias audit | Correlation is not written as causality |
| `agent-auto-sci-geospatial` | GIS/RS | Accessibility, exposure, LCZ, spatial equity, maps | CRS audit, exposure window, map QA | Keeps exposure/accessibility/use separate |
| `agent-auto-sci-data-viz` | Data/figures | EDA, statistics, bibliometrics, manuscript figures | Figure plan, statistical route, captions | Every chart must serve a claim |
| `agent-auto-sci-ai-ml` | ML/XAI | Prediction, SHAP, leakage checks, validation design | Baseline, split plan, interpretation limits | Feature importance is not causal evidence |
| `agent-auto-sci-scicomm` | Writing/submission | Manuscript argument, cover letters, rebuttals, slides | Claim-evidence map, response matrix | Polishing must not change evidence strength |
| `sport-geography-review-bibliometric` | Domain review | Sport geography reviews and bibliometrics | Search strategy, PRISMA, coding table | Bibliometrics must support a framework |
| `sport-geography-sci-writing` | Domain writing | Sport facilities, sport parks, spatial equity empirical papers | Journal positioning, IMRAD sections | Start from the public problem, not only metrics |
| `urban-exposure-review-radar-workflow` | Domain workflow | Urban exposure reviews, formal corpus, frontier radar | Route decision, journal gate, radar handoff | Formal corpus and radar candidates stay separate |
| `kdense-ml-ai-selected` | Upstream wrapper | ML/AI technical playbooks | Model and training guidance | Technical reference only |
| `kdense-data-viz-selected` | Upstream wrapper | EDA, statistics, plotting, large tables | Library-level route and code guidance | Does not design manuscript claims |
| `kdense-geospatial-rs-selected` | Upstream wrapper | GeoPandas, GeoMaster, GIS/RS details | Spatial processing guidance | Does not bypass CRS/scale audit |
| `kdense-scicomm-selected` | Upstream wrapper | Writing, peer review, citation, slides/posters/schematics | Templates and technical references | Does not replace domain judgment |
| `scipilot-figure-skill` | Figure advisor | Chart choice and publication-grade visual QA | Chart advice, plotting route, export checks | First decide what the figure proves |
| `scipilot-writing-skill` | Writing polish | Translation, polishing, de-AI, cover letters, rebuttals | Revised text, back-translation, lint report | Does not alter facts, values, citations |
| `geors-sci-writing-adapter` | Geo/RS writing | Inversion, spatiotemporal change, exposure/accessibility papers | Section drafting, journal positioning, spatial writing checks | Original adapter, no unlicensed upstream text |

## Typical Workflows

### Sport facility accessibility manuscript

```text
auto-sci-research
-> sport-geography-sci-writing
-> agent-auto-sci-geospatial
-> agent-auto-sci-data-viz
-> agent-auto-sci-methodology
-> scipilot-writing-skill
```

### Green or heat exposure review

```text
auto-sci-research
-> urban-exposure-review-radar-workflow
-> sport-geography-review-bibliometric
-> agent-auto-sci-methodology
-> agent-auto-sci-data-viz
-> agent-auto-sci-scicomm
```

### Remote-sensing inversion or spatiotemporal change paper

```text
auto-sci-research
-> geors-sci-writing-adapter
-> agent-auto-sci-geospatial
-> agent-auto-sci-ai-ml
-> agent-auto-sci-data-viz
-> scipilot-writing-skill
```

## Upstream And Licensing

- `Haojae/scipilot-writing-skill`: MIT, fully packaged with LICENSE and NOTICE.
- `Haojae/scipilot-figure-skill`: MIT, packaged as a figure-advisor skill.
- `Imbad0202/academic-research-skills-codex`: ARS Codex package, synced to `v0.1.22`.
- `K-Dense-AI/scientific-agent-skills`: selected wrappers only, not a full import.
- `xiangyu-Ge/sci-writing-geors`: no explicit LICENSE detected, so this repo keeps only attribution and an original adapter.

See [docs/external-skills.md](docs/external-skills.md), [docs/skill-map.md](docs/skill-map.md), and [docs/upstream-update-20260801.md](docs/upstream-update-20260801.md).

## ChatGPT and Codex cross-surface use

Start at [docs/chatgpt/index.md](docs/chatgpt/index.md) for the one-time ChatGPT Project instructions, ordinary-new-chat Skill/Plugin route, GitHub source-of-truth contract, and evaluation protocol. Detailed research rules remain versioned in the repository.

## License

Original repository content is MIT licensed. Third-party vendored or wrapped content follows its own license. Unlicensed upstream content is not copied into the public repository; only attribution and original adapters are included.
