# Skill Map

## 1. Core Router

| Skill | Role |
|---|---|
| `auto-sci-research` | Umbrella router, project memory, skill routing, full research writing pipeline, evolution archive |

## 2. Research Automation

| Skill | Role |
|---|---|
| `agent-auto-sci-automation` | Source manifest, checkpoints, project memory, API boundaries, failure logs |

## 3. Methodology

| Skill | Role |
|---|---|
| `agent-auto-sci-methodology` | Research question design, hypothesis matrix, evidence grading, bias audit |

## 4. Geospatial Science

| Skill | Role |
|---|---|
| `agent-auto-sci-geospatial` | GIS, remote sensing, accessibility, green/heat exposure, equity, map compliance |
| `kdense-geospatial-rs-selected` | Selected K-Dense geospatial and remote-sensing helpers, including GeoMaster and GeoPandas, wrapped for GIS data handling and remote-sensing preprocessing |
| `urban-exposure-review-radar-workflow` | Urban exposure domain router, review-route decision, remote-sensing and Geospatial AI frontier radar, and ARS-backed academic pipeline handoff |

## 5. Data And Visualization

| Skill | Role |
|---|---|
| `agent-auto-sci-data-viz` | EDA, statistics, publication figures, bibliometric visuals, policy matrices |
| `kdense-data-viz-selected` | Selected K-Dense data analysis and visualization helpers: EDA, statistical analysis, Matplotlib, Seaborn, scientific visualization, NetworkX, Polars, and Dask |
| `scipilot-figure-skill` | Scientific figure advisor for chart choice, publication-grade rendering, CJK-safe labels, and visual QA loops |

## 6. AI And Machine Learning

| Skill | Role |
|---|---|
| `agent-auto-sci-ai-ml` | ML, XAI, SHAP, baselines, leakage checks, reproducibility |
| `kdense-ml-ai-selected` | Selected K-Dense ML/AI helpers: scikit-learn, PyTorch Lightning, Transformers, SHAP, aeon, TimesFM, PyTorch Geometric, and UMAP |

## 7. Scientific Communication

| Skill | Role |
|---|---|
| `agent-auto-sci-scicomm` | Manuscript structure, claim-evidence map, rebuttal, slides, posters |
| `kdense-scicomm-selected` | Selected K-Dense scientific communication helpers: writing, peer review, slides, schematics, citation management, literature review, Mermaid, posters |

## 8. Sport Geography

| Skill | Role |
|---|---|
| `sport-geography-review-bibliometric` | Systematic review, scoping review, bibliometrics, critical coding, policy agenda |
| `sport-geography-sci-writing` | Empirical SCI writing for sport geography, exposure, accessibility, equity and urban health |
| `urban-exposure-review-radar-workflow` | Route decision and full workflow for bibliometric + critical review, systematic review, scoping review, frontier radar, urban exposure/medical database linkage, and ARS-backed paper pipeline |

## 9. Review And Frontier Radar

| Skill | Role |
|---|---|
| `urban-exposure-review-radar-workflow` | Combines review workflow discipline with remote-sensing frontier radar. It separates formal review corpora from current radar candidates, adds journal evidence gates for Cities, SCS, Health & Place, Environment International, UFUG, Landscape and Urban Planning, and Nature-family urban/health outlets, and routes writing/review/citation tasks into the vendored `academic-research-suite` subskill. |

## 10. Vendored Academic Research Suite

| Subskill | Role |
|---|---|
| `urban-exposure-review-radar-workflow/subskills/academic-research-suite` | Codex-native Academic Research Suite v0.1.12 vendored as an isolated subskill. Use only after the parent urban-exposure route and evidence gate are set. |

| Internal workflow | Role |
|---|---|
| `deep-research` | Research question narrowing, literature discovery, systematic review support, source verification, and evidence synthesis. |
| `academic-paper` | Paper outline, abstract, literature review, drafting, revision, citation checks, disclosure, and formatting support. |
| `academic-paper-reviewer` | Peer-review simulation, editor-in-chief screening, domain review, methodology review, and revision-response planning. |
| `academic-pipeline` | Full research-to-paper pipeline, state tracking, integrity verification, claim-reference alignment, and finalization gates. |
| `experiment-agent` | Experiment planning, code-run planning, human study protocol support, statistical interpretation, and reproducibility validation. |

## 11. Full Research-To-Manuscript Pipeline

Use `auto-sci-research` as the controller when the user asks for a full workflow from topic selection to final manuscript.

| Stage | Owner skills | Output |
|---|---|---|
| Intake and boundary | `auto-sci-research`, `agent-auto-sci-automation` | project brief, source manifest, privacy boundary |
| Topic and SMART question | `agent-auto-sci-methodology` | topic matrix, hypotheses, feasibility and scope |
| Literature search and synthesis | `sport-geography-review-bibliometric`, `urban-exposure-review-radar-workflow` | keyword system, screening protocol, literature matrix, evidence map |
| Data and spatial processing | `agent-auto-sci-geospatial`, `agent-auto-sci-automation` | data inventory, download/cleaning plan, CRS and exposure/accessibility audit |
| Modeling and analysis | `agent-auto-sci-ai-ml`, `kdense-ml-ai-selected`, `agent-auto-sci-data-viz`, `kdense-data-viz-selected`, `agent-auto-sci-methodology` | baselines, statistical tests, robustness, XAI boundary |
| Publication figures | `agent-auto-sci-data-viz`, `kdense-data-viz-selected`, `scipilot-figure-skill`, `agent-auto-sci-geospatial`, `agent-auto-sci-scicomm` | main/supplementary figure plan, captions, visual QA, map compliance |
| Manuscript draft | `sport-geography-sci-writing`, `agent-auto-sci-scicomm`, `kdense-scicomm-selected` | title, abstract, IMRAD draft, claim-evidence map |
| Review, formatting, rebuttal | `agent-auto-sci-methodology`, `agent-auto-sci-scicomm`, `agent-auto-sci-automation` | reviewer-risk scan, formatted package, response matrix |

Detailed references:

- `skills/auto-sci-research/references/08_full_research_to_manuscript_pipeline.md`
- `skills/auto-sci-research/references/09_subagent_composition_matrix.md`
- `skills/auto-sci-research/references/10_prompt_workflow_from_academic_pdf.md`
- `skills/auto-sci-research/references/11_sportpark_skill_integration_notes.md`
