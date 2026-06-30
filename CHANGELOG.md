# Changelog

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
