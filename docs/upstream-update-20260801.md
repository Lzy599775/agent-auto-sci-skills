# Upstream Update Check, 2026-08-01

This audit refreshed every configured upstream mirror, compared each new GitHub snapshot against the exact directories packaged in this repository, and synchronized only content covered by the existing packaging and license policy.

## Results

| Upstream | Previous snapshot | Latest snapshot | Result | Local action |
|---|---:|---:|---|---|
| `K-Dense-AI/scientific-agent-skills` | `4d97e29` (`v2.53.0-10-g4d97e29`) | `ad21a38` (`v2.62.0`) | Updated | Re-mirrored the 27 selected subskills. Twenty-six had file-level changes; `transformers` was unchanged. |
| `Imbad0202/academic-research-skills-codex` | `8626ccb` (`v0.1.17`) | `f8d6b06` (`v0.1.22`) | Updated | Re-synced the isolated `academic-research-suite`, preserved local attribution files, and aligned `VERSION`, `SKILL.md`, and `manifest.json` at `0.1.22`. |
| `skyllwt/AutoSci` | `a01841d` (`v1.0.0-30-ga01841d`) | `ff3485e` (`v1.0.0-36-gff3485e`) | Updated upstream | Reviewed the research-router delta. It now hands cold-start bootstrap to `/init`; the local original router was not overwritten. |
| `Haojae/scipilot-figure-skill` | `43098dd` | `43098dd` (`v2.1.0-1-g43098dd`) | No change | No package change. |
| `Haojae/scipilot-writing-skill` | `51c5fd3` | `51c5fd3` (`v1.0.0`) | No change | No package change. |
| `xiangyu-Ge/sci-writing-geors` | `1f58c00` | `1f58c00` | No change | Kept the original attribution-only adapter because the checked upstream snapshot still has no explicit license file. |

## Coverage of the 17 Top-Level Skills

All 17 installable top-level skills were included in the audit:

- 10 locally maintained original skills (`auto-sci-research`, the six `agent-auto-sci-*` modules, two sport-geography modules, and `urban-exposure-review-radar-workflow`) have no one-to-one GitHub upstream to mirror; their routing and descriptions were checked against the refreshed packages.
- 4 K-Dense selected wrappers were synchronized to `v2.62.0`.
- 2 full SciPilot packages were checked and remain current at their existing commits.
- 1 GeoRS writing adapter was checked against its source repository and remains an original, attribution-only implementation.
- The nested ARS package inside `urban-exposure-review-radar-workflow` was synchronized separately to `v0.1.22`.

## K-Dense Selected Scope

The repository still packages four focused wrappers rather than the complete K-Dense catalog.

| Wrapper | Selected subskills | 2026-08-01 result | Main improvements |
|---|---:|---|---|
| `kdense-data-viz-selected` | 8 | 8 directories synchronized | Expanded EDA utilities, publication-figure export and style checks, Seaborn guidance, and refreshed tool metadata. |
| `kdense-ml-ai-selected` | 8 | 7 changed, `transformers` unchanged | Expanded SHAP workflows, scikit-learn checks, time-series forecasting guidance, and PyTorch Lightning helpers. |
| `kdense-geospatial-rs-selected` | 2 | 2 changed | Added GeoPandas scripts for CRS planning, geometry validity, spatial joins, export, sensitive-coordinate review, and vector inventory. |
| `kdense-scicomm-selected` | 9 | 9 changed | Expanded citation retrieval/validation, literature review, peer review, posters, slides, schematics, and scientific-writing workflows. |

The large upstream release also changed many biomedical, chemistry, office, and infrastructure skills outside the selected scope. Those directories were deliberately not added, so the suite remains focused on geography, sport, urban exposure, analysis, visualization, and academic communication.

## ARS 0.1.22 Highlights

The bundled Codex package now pins ARS `v3.19.0` at upstream commit `828ef3b613b0e8b91830da3328a1e33d4eb5ab4c`. Important additions since the previous local snapshot include:

- model-tiering and risk-stratified cross-model verification with explicit provider, content, credential, and consent gates;
- canonical cross-model handoff contracts, least-privilege tool allowlists, panel-synthesis checks, and degradation disclosure;
- fixed-seat Reviewer 2 and independent re-review paths that are disclosed rather than simulated when unavailable;
- local-PDF read-integrity preflight, optional human-read scope attestations, and partial-coverage handling;
- claim-strength, revision-evidence, token-conservation, and claim-drift checks for revision rounds.

The parent `urban-exposure-review-radar-workflow` remains authoritative for geography-specific definitions, corpus eligibility, accessibility/exposure distinctions, spatial causal language, and target-journal routing.

Because this repository vendors the standalone skill rather than the complete ARS-Codex plugin repository, its quality-gate runner has a narrow path adaptation: package paths resolve from the nested skill root, and the Desktop plugin bundle check is explicitly skipped only when that bundle is absent. All skill-level gates remain active.

## License Boundary

- K-Dense and both SciPilot packages retain their MIT notices and upstream license copies.
- The isolated ARS package retains its upstream CC BY-NC license and NOTICE files.
- GeoRS remains an original adapter with attribution only; no upstream prose is copied without an explicit license.
- AutoSci is inspected as a reference source and is not vendored into the public package.

## Validation Targets

After synchronization, the maintenance pass checks top-level skill frontmatter, ARS version alignment, repository public-safety rules, whitespace errors, and package-specific consistency scripts where available. Any upstream validator that depends on intentionally excluded runtime files is reported separately rather than treated as a local version mismatch.
