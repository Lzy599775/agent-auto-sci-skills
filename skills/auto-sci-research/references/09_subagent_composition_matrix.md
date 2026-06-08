# Subagent Composition Matrix

Use this reference when a research task is large enough to split into role-specific subagents. A subagent here means a scoped working role built from one or more local skills. It is not a new standalone skill unless repeated use proves the role deserves one.

## 1. Composition Rules

1. Assign one owner subagent for each phase.
2. Give each subagent a bounded input and output.
3. Keep private data and paid PDFs local; pass summaries or paths, not full copyrighted content.
4. Use `auto-sci-research` to coordinate handoffs and quality gates.
5. Record rejected ideas, failed routes, and reviewer-risk findings in the project memory or evolution archive when reusable.

## 2. Recommended Subagents

| Subagent | Skills combined | Owns | Typical outputs | Handoff target |
|---|---|---|---|---|
| Topic PI | `agent-auto-sci-methodology` + `agent-auto-sci-automation` | topic selection, feasibility, scope | topic matrix, minimum viable paper, risk plan | Literature Strategist |
| Literature Strategist | `sport-geography-review-bibliometric` + `urban-exposure-review-radar-workflow` | search, screening, corpus strategy | keyword system, PRISMA plan, literature matrix | Method Architect |
| Frontier Radar | `urban-exposure-review-radar-workflow` + `agent-auto-sci-geospatial` | recent RS/Geospatial AI ideas, CV-to-RS transfer | radar candidate table, novelty notes, route decision | Topic PI |
| Method Architect | `agent-auto-sci-methodology` + `agent-auto-sci-geospatial` + `agent-auto-sci-ai-ml` | design, variables, models, bias | method route, variable definitions, bias/confounding audit | Data Engineer |
| Data Engineer | `agent-auto-sci-automation` + `agent-auto-sci-geospatial` | data download, cleaning, reproducibility | source manifest, data dictionary, preprocessing log | Analyst |
| Analyst | `agent-auto-sci-data-viz` + `agent-auto-sci-ai-ml` + `agent-auto-sci-methodology` | statistics, ML, robustness | EDA, model results, sensitivity checks, interpretation boundary | Figure Editor |
| Figure Editor | `agent-auto-sci-data-viz` + `agent-auto-sci-geospatial` + `agent-auto-sci-scicomm` | publication figures and captions | figure plan, exported figures, captions, map compliance note | Manuscript Writer |
| Manuscript Writer | `sport-geography-sci-writing` + `agent-auto-sci-scicomm` | IMRAD draft, target-journal style | outline, section drafts, title, abstract, highlights | Reviewer Panel |
| Reviewer Panel | `agent-auto-sci-methodology` + `agent-auto-sci-scicomm` + `agent-auto-sci-data-viz` | internal critique | high/medium/low risk list, revision tasks | Manuscript Writer |
| Submission Editor | `agent-auto-sci-scicomm` + `agent-auto-sci-automation` | formatting, references, cover letter, materials | submission checklist, cover letter, reproducibility statement | User review |
| Rebuttal Manager | `agent-auto-sci-scicomm` + `agent-auto-sci-methodology` | revision response | response matrix, revision location map, residual risk | Submission Editor |
| Skill Curator | `auto-sci-research` + `agent-auto-sci-automation` | skill evolution and release prep | dedup log, updated references, evolution event, validation results | User/GitHub |

## 3. Handoff Schema

Every subagent handoff should include:

- `objective`: one sentence.
- `inputs`: paths, datasets, notes, or prior outputs.
- `decisions`: assumptions and choices already made.
- `outputs`: required artifacts and format.
- `quality_gate`: checks that must pass.
- `risks`: unresolved doubts or evidence limits.
- `next_owner`: the next subagent or user.

## 4. Example End-To-End Chain

For a sport facility accessibility and green/heat exposure paper:

1. Topic PI defines the paper as an active-health equity problem.
2. Literature Strategist builds search strings around sport facilities, accessibility, green exposure, heat exposure, equity, and built environment.
3. Method Architect defines accessibility, exposure, fairness, and mechanism variables.
4. Data Engineer prepares POI, road network, population, LCZ, NDVI/LST, and administrative boundaries.
5. Analyst runs accessibility, equity metrics, spatial models, ML/XAI, and robustness checks.
6. Figure Editor creates study-area map, framework diagram, spatial pattern maps, determinant plots, and policy-priority maps.
7. Manuscript Writer drafts IMRAD using the claim-evidence map.
8. Reviewer Panel attacks novelty, data leakage, causal overclaiming, map quality, and policy overreach.
9. Submission Editor formats, checks references, and prepares the cover letter.

## 5. When Not To Split

Do not split into subagents when:

- the task is a short paragraph edit;
- only one file needs a small correction;
- data are too sensitive to summarize safely;
- the user asked for a single direct answer;
- the overhead would exceed the likely benefit.
