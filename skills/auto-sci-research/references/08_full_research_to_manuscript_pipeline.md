# Full Research To Manuscript Pipeline

Use this reference when the user wants an end-to-end workflow from topic selection to final manuscript submission.

This pipeline integrates the local `agent-auto-sci-*` skills, sport geography writing skills, and reusable lessons distilled from the user's Sportpark writing workspace. It is not a prompt dump. Treat every step as a research checkpoint with input, output, owner skill, and quality gate.

## 1. Phase Map

| Phase | Main question | Primary skills | Optional helper skills | Required outputs |
|---|---|---|---|---|
| 0. Intake and boundary | What is the project, what files/data are in scope, and what must stay private? | `auto-sci-research`, `agent-auto-sci-automation` | `codex-paper-reader` | project brief, source manifest, privacy boundary |
| 1. Topic selection | Is the topic meaningful, feasible, and publishable? | `agent-auto-sci-methodology` | `scientific-brainstorming`, `scholar-evaluation` | candidate topic matrix, novelty/risk table, minimal viable paper |
| 2. Research question | Can the topic become a measurable question? | `agent-auto-sci-methodology` | `hypothesis-generation` | SMART questions, concepts, variables, hypotheses, scope exclusions |
| 3. Literature search | Can the literature search be reproduced? | `sport-geography-review-bibliometric`, `urban-exposure-review-radar-workflow` | `paper-lookup`, `research-lookup`, `codex-paper-reader` | keyword table, Boolean strings, database plan, inclusion/exclusion criteria |
| 4. Literature synthesis | What is known, contested, and still missing? | `sport-geography-review-bibliometric`, `agent-auto-sci-methodology` | `academic-research-suite` | literature matrix, evidence map, gap taxonomy, theory/conceptual framework |
| 5. Data plan | What data are needed and what can be legally used? | `agent-auto-sci-automation`, `agent-auto-sci-geospatial` | `geopandas`, `geomaster`, `pyzotero` | data inventory, download plan, license/ethics note, versioning rule |
| 6. Processing and code | Can the analysis be reproduced in VS Code or notebooks? | `agent-auto-sci-geospatial`, `agent-auto-sci-ai-ml`, `agent-auto-sci-automation` | `polars`, `scikit-learn`, `statsmodels`, `shap` | scripts/notebooks, environment notes, logs, intermediate outputs |
| 7. Analysis | Do results answer the research question? | `agent-auto-sci-data-viz`, `agent-auto-sci-methodology`, `agent-auto-sci-ai-ml` | `statistical-analysis`, `exploratory-data-analysis` | EDA report, model/statistical results, robustness checks, interpretation limits |
| 8. Figures and tables | Does each figure support a claim? | `agent-auto-sci-data-viz`, `agent-auto-sci-geospatial`, `agent-auto-sci-scicomm` | `scientific-visualization`, `matplotlib`, `seaborn` | main/supplementary figure plan, export files, captions, table shells |
| 9. Drafting | Can the evidence become a coherent manuscript? | `sport-geography-sci-writing`, `agent-auto-sci-scicomm` | `scientific-writing`, `nature-polishing` | title, highlights, abstract, IMRAD outline, section drafts |
| 10. Internal review | What would reviewers attack first? | `agent-auto-sci-methodology`, `agent-auto-sci-scicomm`, `agent-auto-sci-data-viz` | `peer-review`, `scientific-critical-thinking` | reviewer-risk scan, claim-evidence audit, revision task list |
| 11. Formatting and submission | Does the manuscript match the target venue? | `agent-auto-sci-scicomm`, `agent-auto-sci-automation` | `venue-templates`, `citation-management`, `docx`, `pdf` | formatted manuscript, reference check, cover letter, reproducibility package |
| 12. Revision and rebuttal | Can each reviewer concern be mapped to action? | `agent-auto-sci-scicomm`, `agent-auto-sci-methodology` | `peer-review` | response matrix, revised manuscript, location map, residual risk note |

## 2. Sport Geography Default Narrative

For sport parks, sport facilities, green exposure, heat exposure, accessibility, and equity papers, default to this argument chain unless the corpus contradicts it:

`real public-health or urban-planning pressure -> unequal exposure or accessibility -> measurement and mechanism gap -> improved data/method framework -> spatial or social evidence -> mechanism explanation -> planning or governance implication -> evidence boundary`

Do not let methods lead the paper. Methods should enter only after the public problem and measurement gap are clear.

## 3. Minimum Viable Paper Gate

Before committing to a topic, require:

1. A specific population, place, exposure/resource, and outcome or equity dimension.
2. At least one feasible data source for each core construct.
3. A baseline method that can produce interpretable results without a complex model.
4. A target-journal route and one fallback route.
5. One table or figure that could become the paper's central evidence.
6. A clear limitation boundary that prevents overclaiming causality.

If any item fails, use `agent-auto-sci-methodology` to narrow the question before collecting more data.

## 4. Claim-Evidence Workflow

Maintain a claim-evidence map from Phase 4 onward.

| Claim type | Evidence requirement | Typical owner |
|---|---|---|
| Literature gap | reproducible search, matrix, and comparison across papers | `sport-geography-review-bibliometric` |
| Spatial pattern | map, scale/CRS audit, uncertainty or sensitivity note | `agent-auto-sci-geospatial`, `agent-auto-sci-data-viz` |
| Equity claim | group definition, denominator, fairness metric, affected population | `agent-auto-sci-methodology` |
| Mechanism claim | model, pathway, confounder discussion, alternative explanations | `agent-auto-sci-methodology`, `agent-auto-sci-ai-ml` |
| Model improvement | fair baselines, validation split, robustness, leakage check | `agent-auto-sci-ai-ml` |
| Policy implication | evidence-supported action, target actor, boundary condition | `agent-auto-sci-scicomm` |

Any paragraph with a strong claim but no evidence pointer must be revised or softened.

## 5. Data And Code Standards

For geography and sport-health work:

- Record original sources, download dates, licenses, spatial/temporal coverage, and transformation steps.
- Keep raw data read-only when possible.
- In notebooks, make project roots explicit when files move between folders.
- For spatial analysis, audit CRS, geometry validity, unit consistency, boundary choice, scale, travel mode, and network assumptions.
- For ML, prefer simple baselines before complex models; use spatial or temporal validation when leakage is plausible.
- Keep private data, paid database exports, API keys, and unpublished materials out of public skill files and HTML.

## 6. Figure System

A strong empirical paper usually needs:

1. Study area and data framework figure.
2. Analytical framework or conceptual model.
3. Core spatial pattern map.
4. Equity or group difference figure/table.
5. Mechanism or determinant figure.
6. Robustness or sensitivity evidence.
7. Policy-priority or planning implication map/table.

Each figure folder should include source code/notebook, exported image, data snapshot or data pointer, and a short composition note when it is part of a manuscript figure system.

## 7. Writing Sequence

Draft in this order:

1. One-paragraph core argument.
2. Target-journal positioning.
3. Figure/table plan.
4. Methods skeleton.
5. Results narrative from actual outputs.
6. Introduction gap chain.
7. Discussion mechanisms, literature dialogue, implications, and limits.
8. Abstract, title, highlights, keywords.
9. Cover letter and submission checklist.

Do not polish language before the claim-evidence map is stable.

## 8. Final Quality Gate

Before calling a manuscript or skill package ready:

- Search for placeholders, conflict markers, fake citations, and unsupported claims.
- Confirm every figure/table is referenced and every core variable appears in the methods.
- Check that limitations match the design and do not undermine the central contribution.
- Verify references are relevant, current enough for the topic, and formatted consistently.
- Update the evolution archive when the workflow or skill package changes.
