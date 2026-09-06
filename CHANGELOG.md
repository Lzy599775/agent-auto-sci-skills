# Changelog

## 0.8.0

- Refreshed all configured upstream checks on 2026-09-06.
- Updated the selected K-Dense wrappers to `v2.66.0` (`1e5eeff`); 26 of 27 selected directories changed and `timesfm-forecasting` remained file-identical.
- Updated the isolated ARS Codex package to `v0.1.28` (`925975e`) with ARS upstream content at `9443623`.
- Rechecked AutoSci at `8642426`; its rotating image-only delta remains reference-only and does not replace the local domain router.
- Confirmed SciPilot Figure, SciPilot Writing, and GeoRS have no new main-branch commit.
- Refreshed source notices, upstream audit, skill map, and local HTML navigator metadata.

## 0.7.0

- Refreshed all configured upstream mirrors on 2026-08-01.
- Updated the vendored `academic-research-suite` from `v0.1.17` to `v0.1.22` (`f8d6b06`), carrying ARS `v3.19.0` with local-PDF read-integrity preflight, read-scope attestations, cross-model verification guards, and revision claim-drift checks.
- Adapted the ARS quality-gate runner for this nested standalone distribution while retaining all skill-level gates and explicitly skipping only the absent repository-level Desktop plugin bundle check.
- Updated K-Dense selected wrappers from `v2.53.0-10-g4d97e29` to `v2.62.0` (`ad21a38`): 26 of 27 selected subskills changed; `transformers` remained file-identical.
- Verified SciPilot Figure, SciPilot Writing, and GeoRS had no new commit.
- Checked AutoSci at `ff3485e`; documented its cold-start `/init` handoff change without overwriting the local original router.
- Updated Chinese and English READMEs, skill map, external-source registry, local HTML navigator, evolution page, notices, and the dated upstream audit.

## 0.6.0

- Refreshed upstream mirrors on 2026-07-07.
- Updated `urban-exposure-review-radar-workflow/subskills/academic-research-suite` to ARS Codex package `v0.1.17` (`8626ccb`) and restored root attribution files.
- Checked `K-Dense-AI/scientific-agent-skills` at `v2.53.0-10-g4d97e29`; synced the selected `statistical-analysis` subskill into `kdense-data-viz-selected`.
- Verified SciPilot Figure, SciPilot Writing, and GeoRS SCI Writing Adapter had no upstream commit change.
- Checked AutoSci at `a01841d`; latest delta only touched a WeChat image asset, so no public package change was made.
- Rebuilt README, README_EN, skill map, external skill notes, use cases, upstream update notes, and local HTML pages with clean UTF-8 Chinese text and clearer skill classification.

## 0.5.0

- Refreshed upstream mirrors on 2026-06-30.
- Updated `urban-exposure-review-radar-workflow/subskills/academic-research-suite` to ARS Codex package `v0.1.15` (`efdbc2a`) and restored root attribution files.
- Checked `K-Dense-AI/scientific-agent-skills` at `v2.53.0-6-g0807ddb`; selected local wrapper files were unchanged.
- Added `scipilot-writing-skill` from `Haojae/scipilot-writing-skill` `v1.0.0` with MIT license, scripts, references, examples, NOTICE, and Codex UI metadata.
- Added `geors-sci-writing-adapter` as an original geography/remote-sensing SCI writing adapter inspired by `xiangyu-Ge/sci-writing-geors`; no upstream text was vendored because no explicit LICENSE file was detected.
- Rebuilt README, README_EN, skill map, external skill notes, upstream update notes, and local HTML homepage around a clearer 17-skill classification system.
- Updated `auto-sci-research` routing and internal registry for the new writing skills.

## 0.4.0

- Added selected wrappers from `K-Dense-AI/scientific-agent-skills` instead of installing the full upstream repository.
- Added `kdense-ml-ai-selected` for scikit-learn, PyTorch Lightning, Transformers, SHAP, time-series ML, TimesFM, PyTorch Geometric, and UMAP.
- Added `kdense-data-viz-selected` for EDA, statistics, Matplotlib, Seaborn, scientific visualization, NetworkX, Polars, and Dask.
- Added `kdense-geospatial-rs-selected` for GeoMaster and GeoPandas geospatial/remote-sensing workflows.
- Added `kdense-scicomm-selected` for scientific writing, peer review, slides, schematics, citation management, literature review, Mermaid, and posters.
- Added `scipilot-figure-skill` from `Haojae/scipilot-figure-skill` for publication-figure planning, chart selection, visual QA, CJK label checks, and figure-story alignment.
- Updated README, README_EN, skill map, use cases, external references, router registry, and site pages for the expanded 15-skill suite.

## 0.3.0

- Added an end-to-end research-to-manuscript pipeline for topic selection, literature search, data/code, analysis, publication figures, drafting, internal review, formatting, and rebuttal.
- Added a subagent composition matrix that groups existing skills into scoped roles instead of creating duplicate skills.
- Distilled the local academic prompt PDF into workflow structure and quality gates without copying long prompt text.
- Integrated Sportpark writing, figure, and Darwin-style evolution lessons as references while keeping the Sportpark source project untouched.
- Updated routing rules and full-pipeline ownership across core skills.

## 0.2.0

- Added `urban-exposure-review-radar-workflow` for urban exposure review routing, systematic/scoping review planning, bibliometric + critical review, remote-sensing frontier radar, CV-to-RS transfer, and public-health database linkage.
- Updated README, README_EN, docs, GitHub Pages homepage, and skill detail pages.
- Added public references to `bionoob7/nlr-workflow` and `limi124/remote-sensing-research-radar` as design inspirations without vendoring their repositories.

## 0.1.0

- Initial public packaging of Agent Auto Sci skills.
- Includes sport geography review, bibliometrics, geospatial analysis, data visualization, ML/XAI, methodology, and scientific communication workflows.
