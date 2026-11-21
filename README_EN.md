# Auto-sci-research

[中文](README.md) | [English](README_EN.md) | [Local showcase](site/index.html) | [Evolution archive](site/agent-auto-sci-evolution.html)

> A Codex-first skill suite for geography, sport science, urban health, GIS/remote sensing, green exposure, sport parks/facilities, spatial equity, literature review, bibliometrics, machine learning, scientific figures, and SCI writing.

`Auto-sci-research` is a reusable research workbench, not a one-click paper generator. It helps ChatGPT and Codex route research tasks across topic design, literature review, source manifests, GIS/RS processing, exposure/accessibility measurement, statistics, ML/XAI, publication figures, manuscript writing, cover letters, rebuttals, and project memory.

The repository contains **14 installable skills**, plus an isolated `academic-research-suite` subskill inside `urban-exposure-review-radar-workflow`.

Latest upstream audit: **2026-11-21** (30-day cutoff: 2026-10-22).

- ARS Codex remains at its latest package, `v3.24.2` (`82725ac`), locking source content to `fd5ff1b`. The original ARS repository advanced to `bd57330`, but no corresponding Codex package has been released; unpublished content is not mixed into the adapter.
- K-Dense advanced to `ec59a29`, but all 27 formerly selected skill directories were last changed on 2026-10-01. Their four wrappers remain retired.
- AutoSci advanced to `aa852fd` with a documentation-only QR-code change. It remains reference-only.
- SciPilot Figure and Writing remain retired. GeoRS remains at `f515996` (2026-11-03); its original local adapter remains available without copying unlicensed source. No additional skill was removed in this audit.

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
| Decompose target-journal near-neighbor argument structure | `agent-auto-sci-scicomm` + `academic_writing_exemplar_protocol` (reference protocol, not a new top-level skill) |
| Write sport geography empirical SCI papers | `sport-geography-sci-writing` |
| Design sport geography reviews and bibliometric manuscripts | `sport-geography-review-bibliometric` |
| Route urban exposure reviews, radar scans, and health database linkage | `urban-exposure-review-radar-workflow` |
| Use a full academic research and paper pipeline | `urban-exposure-review-radar-workflow/subskills/academic-research-suite` |
| Explicitly screen existing records, define eligibility, resolve conflicts, or audit exclusions | ARS `sr-screener` (explicit invocation only) |
| Build a manuscript-specific exemplar profile with author approval gates | `project-specific-writing-exemplar-workflow` |
| Write a geography or remote-sensing SCI manuscript | `geors-sci-writing-adapter` |

## Skill Categories

| Category | Skills |
|---|---|
| Router and automation | `research-orchestrator`, `auto-sci-research`, `agent-auto-sci-automation` |
| Methodology and evidence design | `agent-auto-sci-methodology`, `urban-exposure-review-radar-workflow` |
| Geospatial, RS, exposure, accessibility | `agent-auto-sci-geospatial` |
| Data, visualization, ML | `agent-auto-sci-data-viz`, `agent-auto-sci-ai-ml` |
| Review and bibliometrics | `literature`, `sport-geography-review-bibliometric`, `urban-exposure-review-radar-workflow`, `academic-research-suite` |
| Writing and submission | `sport-geography-sci-writing`, `geors-sci-writing-adapter`, `agent-auto-sci-scicomm`, `project-specific-writing-exemplar-workflow` |

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
| `academic-research-suite` | Research pipeline | Deep research, paper pipeline, review simulation, citation/PDF checks | Research route, workflow artifacts, audit outputs | `sr-screener` is only for explicitly requested screening; it is not an automatic consequence of a review request |
| `geors-sci-writing-adapter` | Original writing adapter | Geography/RS, exposure and accessibility manuscripts | Claim-evidence map, IMRAD sections, submission checks | Does not copy unlicensed upstream text or change scientific results |
| `project-specific-writing-exemplar-workflow` | Manuscript-specific writing workflow | Build and refresh a private exemplar profile for substantive drafting and major revision | Core 3 approval gate, section exemplar sets, evidence/argument maps | Private manuscript state only; never copies source prose or bypasses author approval |

## Typical Workflows

### Sport facility accessibility manuscript

```text
auto-sci-research
-> sport-geography-sci-writing
-> agent-auto-sci-geospatial
-> agent-auto-sci-data-viz
-> agent-auto-sci-methodology
-> agent-auto-sci-scicomm
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
-> agent-auto-sci-geospatial
-> agent-auto-sci-geospatial
-> agent-auto-sci-ai-ml
-> agent-auto-sci-data-viz
-> agent-auto-sci-scicomm
```

## Evidence-first writing exemplar routing

Target-journal benchmarking is treated as evidence-first exemplar decomposition, not language imitation. Build `OUR_EVIDENCE_MAP` and `OUR_ARGUMENT_OUTLINE`, select 3–5 function-matched papers per substantive section, record `FULLTEXT`, `ABSTRACT_ONLY`, or `METADATA_ONLY`, draft from the user's evidence, and then hand off to the local academic prose and consistency checks. The reference protocol lives under `agent-auto-sci-scicomm`; manuscript-specific lifecycle control is provided by `project-specific-writing-exemplar-workflow`. Official journal requirements outrank the soft empirical abstract profile, and journal recommendations must use the full manuscript when available rather than IF alone. See [the cross-client matrix](docs/CROSS_CLIENT_WRITING_ROUTING_MATRIX_V1.md).

V2 adds a reusable global academic-writing contract: story-relevance, sentence-increment, paragraph-contribution, Results/Introduction/Discussion selection, Methods reproducibility, robustness placement, three-line tables, no manual prose breaks, figure/table citation and fact-placement ledgers, and conservative redundancy lint. Copy [CHATGPT_GLOBAL_ACADEMIC_WRITING_INSTRUCTIONS_V2](CHATGPT_GLOBAL_ACADEMIC_WRITING_INSTRUCTIONS_V2.txt) into Project Instructions or account-level Custom Instructions when desired; this repository cannot modify ChatGPT account settings.

## Upstream And Licensing

- `Imbad0202/academic-research-skills-codex`: ARS Codex package, synced to `v3.24.2`.
- `K-Dense-AI/scientific-agent-skills`: selected wrappers retired because their 27 skill directories predate the 30-day cutoff.
- SciPilot Figure and Writing remain retired. GeoRS is restored as an original adapter without upstream text redistribution.

See [docs/external-skills.md](docs/external-skills.md), [docs/skill-map.md](docs/skill-map.md), and [docs/upstream-update-20261121.md](docs/upstream-update-20261121.md).

## ChatGPT and Codex cross-surface use

Start at [docs/chatgpt/index.md](docs/chatgpt/index.md) for the one-time ChatGPT Project instructions, ordinary-new-chat Skill/Plugin route, GitHub source-of-truth contract, and evaluation protocol. Detailed research rules remain versioned in the repository.

## License

Original repository content is MIT licensed. Third-party vendored or wrapped content follows its own license. Unlicensed upstream content is not copied into the public repository; only attribution and original adapters are included.
