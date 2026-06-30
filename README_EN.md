# Auto-sci-research

[中文](README.md) | [English](README_EN.md) | [Showcase](site/index.html)

> A Codex-first skill suite for geography, sport science, urban health, GIS/remote sensing, green exposure, sport parks/facilities, spatial equity, literature review, bibliometrics, machine learning, scientific figures, and SCI writing.

`Auto-sci-research` is a reusable research workbench, not a one-click paper generator. It helps Codex route research tasks across topic design, literature review, source manifests, GIS/RS processing, exposure/accessibility measurement, statistics, ML/XAI, publication figures, manuscript writing, cover letters, rebuttals, and project memory.

The repository now contains **17 installable Codex skills**, plus an isolated `academic-research-suite` subskill inside `urban-exposure-review-radar-workflow`.

Latest upstream refresh: 2026-06-30.

- ARS updated to `v0.1.15` (`efdbc2a`).
- K-Dense checked at `v2.53.0-6-g0807ddb`; selected local wrapper scope had no changed files.
- SciPilot Figure remains `v2.1.0-1-g43098dd`.
- SciPilot Writing `v1.0.0` was newly packaged.
- GeoRS SCI Writing Adapter was added as an original adapter because the checked upstream source did not include an explicit license.

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
| Route a complex multi-stage research task | `auto-sci-research` |
| Build source manifests, checkpoints, and safe automation | `agent-auto-sci-automation` |
| Refine research questions, mechanisms, evidence strength, and causality | `agent-auto-sci-methodology` |
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
| Router and automation | `auto-sci-research`, `agent-auto-sci-automation` |
| Methodology and evidence design | `agent-auto-sci-methodology`, `urban-exposure-review-radar-workflow` |
| Geospatial, RS, exposure, accessibility | `agent-auto-sci-geospatial`, `kdense-geospatial-rs-selected`, `geors-sci-writing-adapter` |
| Data, visualization, ML | `agent-auto-sci-data-viz`, `agent-auto-sci-ai-ml`, `kdense-data-viz-selected`, `kdense-ml-ai-selected`, `scipilot-figure-skill` |
| Review and bibliometrics | `sport-geography-review-bibliometric`, `urban-exposure-review-radar-workflow`, `academic-research-suite` |
| Writing and submission | `sport-geography-sci-writing`, `agent-auto-sci-scicomm`, `scipilot-writing-skill`, `geors-sci-writing-adapter`, `kdense-scicomm-selected` |

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

### Green/heat exposure review

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

### Publication figures

```text
agent-auto-sci-data-viz
-> kdense-data-viz-selected
-> scipilot-figure-skill
-> agent-auto-sci-scicomm
```

## Documentation

- [Skill Map](docs/skill-map.md)
- [External Skills And References](docs/external-skills.md)
- [Upstream Update 2026-06-30](docs/upstream-update-20260630.md)
- [Use Cases](docs/use-cases.md)

## Public Safety

This repository must not contain API keys, tokens, cookies, private PDFs, paid database exports, unpublished manuscripts, reviewer comments, private datasets, personal absolute paths, or unauthorized third-party content.

## License

Original repository content is MIT licensed. Third-party vendored or wrapped content follows its own license. Unlicensed upstream content is not copied into the public repository; only attribution and original adapters are included.
