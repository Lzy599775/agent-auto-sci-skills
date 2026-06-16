# Auto-sci-research

[中文](README.md) | [English](README_EN.md) | [🌐 Showcase](site/index.html)

> A Codex-first skill suite for geography, sport science, urban health, geospatial exposure assessment, literature review, bibliometrics, machine learning, and SCI writing.

`Auto-sci-research` is a reusable research-agent skill bundle for Codex. It is designed for research on sport parks, sport facilities, green exposure, heat exposure, spatial equity, urban health, GIS/remote sensing, systematic reviews, scoping reviews, bibliometrics, machine learning, scientific visualization, and manuscript writing.

It is not a paper generator. It is a maintainable research workbench that helps researchers organize search, screening, coding, analysis, figures, writing, peer-review responses, and policy agendas.

This release upgrades `urban-exposure-review-radar-workflow` into a domain router plus research-pipeline adapter. It combines review-project discipline with remote-sensing / Geospatial AI frontier radar, and now vendors an isolated `academic-research-suite` subskill for deep research, paper writing, reviewer simulation, citation checks, full research-to-paper pipelines, and experiment planning.

The suite also packages the latest selected upstream skills from `K-Dense-AI/scientific-agent-skills` and `Haojae/scipilot-figure-skill`. K-Dense is not installed wholesale: only Machine Learning & AI, Data Analysis & Visualization, Geospatial Science & Remote Sensing, and Scientific Communication are wrapped as installable domain modules. `scipilot-figure-skill` is included as a publication-figure and visual-QA companion.

## Core Workflow

```text
sources
-> structured memory
-> idea and method design
-> literature review / bibliometrics / coding
-> GIS / exposure / data / ML analysis
-> manuscript / figures / tables / policy agenda
-> reviewer-risk audit / rebuttal
-> evolution archive
```

## Installation for Codex

```powershell
git clone https://github.com/Lzy599775/agent-auto-sci-skills.git
cd agent-auto-sci-skills
.\scripts\install.ps1
```

Default target:

```text
$env:USERPROFILE\.codex\skills
```

Restart Codex after installation.

Custom target:

```powershell
.\scripts\install.ps1 -Target "$env:USERPROFILE\.agents\skills"
```

The 2026-06-16 F-drive skill consolidation and upstream refresh report is available at [docs/upstream-update-20260616.md](docs/upstream-update-20260616.md).

## Skill Index

| Skill | Status | Purpose | Typical trigger |
|---|---:|---|---|
| `auto-sci-research` / legacy `agent-auto-sci` | Stable | Router, project memory, workflow orchestration, evolution archive | “Use Auto-sci-research to plan this research task.” |
| `agent-auto-sci-automation` | Stable | Source manifests, checkpoints, failure logs, API safety | “Build a persistent research workflow.” |
| `agent-auto-sci-methodology` | Stable | Research questions, hypotheses, evidence grading, bias audit | “Turn this topic into testable questions.” |
| `agent-auto-sci-geospatial` | Stable | GIS, remote sensing, accessibility, exposure, spatial equity | “Audit my spatial workflow.” |
| `agent-auto-sci-data-viz` | Stable | EDA, statistics, publication figures, bibliometric visuals | “Design figures and captions.” |
| `agent-auto-sci-ai-ml` | Stable | ML, SHAP/XAI, leakage checks, spatial validation | “Audit model validation and interpretation.” |
| `agent-auto-sci-scicomm` | Stable | Manuscript structure, journal fit, rebuttal, slides | “Rebuild the manuscript argument.” |
| `kdense-ml-ai-selected` | New | Selected K-Dense ML/AI tools: scikit-learn, PyTorch Lightning, Transformers, SHAP, time series, GNN, UMAP | “Use the selected K-Dense ML toolkit for this modeling task.” |
| `kdense-data-viz-selected` | New | Selected K-Dense EDA, statistics, plotting, visualization, NetworkX, Polars, Dask tools | “Use the selected K-Dense data-viz toolkit to analyze and plot this dataset.” |
| `kdense-geospatial-rs-selected` | New | Selected K-Dense geospatial and remote-sensing helpers: GeoMaster and GeoPandas | “Use the selected K-Dense geospatial toolkit for this GIS workflow.” |
| `kdense-scicomm-selected` | New | Selected K-Dense writing, review, slides, schematics, citation and literature-review helpers | “Use the selected K-Dense scicomm toolkit to polish this manuscript package.” |
| `scipilot-figure-skill` | New | Scientific figure design, chart selection, visual QA, CJK-compatible publication figures | “Use SciPilot Figure Skill to design and audit my figures.” |
| `urban-exposure-review-radar-workflow` | Stable | Review-route decision, bibliometric + critical review, systematic/scoping review, remote-sensing radar, CV-to-RS, medical database linkage | “Decide which route this review/radar/study should take.” |
| `sport-geography-review-bibliometric` | Stable | Systematic/scoping reviews, bibliometrics, critical coding, policy agenda | “Design a review + bibliometrics manuscript.” |
| `sport-geography-sci-writing` | Stable | Empirical SCI writing for sport geography, exposure, equity, urban health | “Turn my results into an SCI manuscript.” |

## Full Research Pipelines

### Urban exposure review radar + ARS academic pipeline

```text
auto-sci-research
-> urban-exposure-review-radar-workflow
-> subskills/academic-research-suite
   -> deep-research
   -> academic-paper
   -> academic-paper-reviewer
   -> academic-pipeline
   -> experiment-agent
```

Outputs: route decision, journal evidence gates, formal-corpus / radar-candidate handoff, extraction and coding plan, ARS-backed literature review, manuscript outline, citation check, reviewer-risk audit, revision roadmap, and integrity verification.

### Review + bibliometrics + policy agenda

```text
auto-sci-research
-> urban-exposure-review-radar-workflow
-> sport-geography-review-bibliometric
-> agent-auto-sci-methodology
-> agent-auto-sci-data-viz
-> agent-auto-sci-scicomm
```

Outputs: search strategy, PRISMA protocol, screening criteria, coding framework, bibliometric figure plan, critical framework, and policy agenda.

### Urban exposure + remote-sensing radar + health database linkage

```text
auto-sci-research
-> urban-exposure-review-radar-workflow
-> agent-auto-sci-geospatial
-> agent-auto-sci-methodology
-> agent-auto-sci-scicomm
```

Outputs: route decision, formal-corpus / radar-candidate handoff, remote-sensing and Geospatial AI candidate ranking, exposure-window and spatial-linkage plan, public-health outcome framework, journal evidence gate, and publishable research ideas.

### Sport facility accessibility and spatial equity manuscript

```text
auto-sci-research
-> sport-geography-sci-writing
-> agent-auto-sci-geospatial
-> agent-auto-sci-data-viz
-> agent-auto-sci-methodology
```

Outputs: research questions, mechanism pathway, spatial data audit, accessibility/exposure/equity metrics, figures, discussion, limitations, and reviewer-risk scan.

### ML + spatial health interpretation

```text
auto-sci-research
-> agent-auto-sci-ai-ml
-> kdense-ml-ai-selected
-> agent-auto-sci-geospatial
-> agent-auto-sci-methodology
-> agent-auto-sci-scicomm
```

Outputs: baselines, spatial/temporal splits, leakage checks, SHAP/XAI interpretation boundaries, and manuscript-ready explanation.

### Publication figures and visual QA

```text
auto-sci-research
-> agent-auto-sci-data-viz
-> kdense-data-viz-selected
-> scipilot-figure-skill
-> agent-auto-sci-scicomm
```

Outputs: figure argument, chart selection, statistics and plotting route, visual QA checklist, CJK font / label checks, caption-to-claim alignment, and journal-ready figure package.

## Example Prompts

```text
Use urban-exposure-review-radar-workflow to decide whether my project on heat exposure, green exposure, sport facility accessibility, and urban health should be a systematic review, scoping review, bibliometric + critical review, frontier radar, or empirical design. Include journal evidence gates for Cities, Sustainable Cities and Society, Environment International, and Health & Place.
```

```text
Use Auto-sci-research and sport-geography-review-bibliometric to design a systematic review on sport park exposure, green equity, and urban health. Include search strategy, PRISMA, screening criteria, coding table, bibliometric figures, critical framework, and policy agenda. Target journals: Cities or Sustainable Cities and Society.
```

```text
Use sport-geography-sci-writing and agent-auto-sci-geospatial to audit my empirical paper on sport facility accessibility. Focus on spatial units, network accessibility, exposure measurement, map compliance, spatial equity metrics, and reviewer risks.
```

## Public Safety

This repository must not contain API keys, tokens, cookies, private PDFs, paid database exports, unpublished manuscripts, reviewer comments, private datasets, personal absolute paths, or unauthorized third-party content.

Before release:

```powershell
.\scripts\scan_public_safety.ps1
```

## References

The public presentation borrows structural ideas from several open-source skill repositories, including XiaohongshuSkills, academic-paper-writer-pro-2, and nature-skills. The workflows here are redesigned for geography + sport science research and do not vendor those projects.

## License

MIT License. Third-party code, templates, or assets must be reviewed separately for license compatibility and attribution.
