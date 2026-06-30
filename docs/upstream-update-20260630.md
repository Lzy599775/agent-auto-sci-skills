# Upstream Update Check, 2026-06-30

This pass refreshed the ignored local mirrors under `external_repos/latest`, checked packaged upstream scope, and updated public wrappers where appropriate.

## Summary

| Upstream | Previous checked snapshot | Latest checked snapshot | Status | Local action |
|---|---:|---:|---|---|
| `K-Dense-AI/scientific-agent-skills` | `ddd2f7f` (`v2.52.0-4-gddd2f7f`) | `0807ddb` (`v2.53.0-6-g0807ddb`) | Upstream changed | No selected wrapper file changed. New upstream changes mainly touched broader K-Dense skills outside the current ML/data-viz/geospatial/scicomm selection. Updated docs to record the latest checked snapshot. |
| `Haojae/scipilot-figure-skill` | `43098dd` (`v2.1.0-1-g43098dd`) | `43098dd` (`v2.1.0-1-g43098dd`) | No upstream change | No package change. |
| `Haojae/scipilot-writing-skill` | Not packaged | `51c5fd3` (`v1.0.0`) | New packaged upstream | Vendored as `skills/scipilot-writing-skill` with MIT license, scripts, references, examples, NOTICE, and Codex UI metadata. |
| `Imbad0202/academic-research-skills-codex` | `36cc610` (`v0.1.14`) | `efdbc2a` (`v0.1.15`) | Upstream changed | Re-synced `urban-exposure-review-radar-workflow/subskills/academic-research-suite` and restored root `LICENSE`/`NOTICE.md`. |
| `skyllwt/AutoSci` | `5568c25` (`v1.0.0-28-g5568c25`) | `6f5a9f6` (`v1.0.0-29-g6f5a9f6`) | Upstream changed | Mirror refreshed only. No public package change because this repo uses a domain-adapted Auto-sci workflow rather than direct AutoSci vendoring. |
| `xiangyu-Ge/sci-writing-geors` | Not packaged | `1f58c00` | New source checked | No explicit LICENSE detected. Created `geors-sci-writing-adapter` as an original Codex adapter with attribution only; no upstream reference text copied. |

## K-Dense Scope Check

Diff check from `ddd2f7f` to `0807ddb` against currently selected packaged areas returned no changed files for:

- ML/AI: `scikit-learn`, `pytorch-lightning`, `transformers`, `shap`, `aeon`, `timesfm-forecasting`, `torch-geometric`, `umap-learn`
- Data/visualization: `exploratory-data-analysis`, `statistical-analysis`, `matplotlib`, `seaborn`, `scientific-visualization`, `networkx`, `polars`, `dask`
- Geospatial/RS: `geomaster`, `geopandas`
- Scientific communication: `scientific-writing`, `peer-review`, `scientific-slides`, `scientific-schematics`, `citation-management`, `literature-review`, `markdown-mermaid-writing`, `latex-posters`, `pptx-posters`

Therefore, wrappers remain functionally current even though the upstream repository advanced.

## Licensing Notes

- `scipilot-writing-skill`: MIT; safe to vendor with license and notice.
- `sci-writing-geors`: no explicit `LICENSE` file in checked snapshot; public package is an original adapter and does not copy upstream `skills/skill.md` or `skills/references/`.
- `academic-research-suite`: license preserved at the subskill root and upstream manifest retained.

## Public Files Updated

- `skills/scipilot-writing-skill/`
- `skills/geors-sci-writing-adapter/`
- `skills/urban-exposure-review-radar-workflow/subskills/academic-research-suite/`
- `README.md`
- `README_EN.md`
- `docs/skill-map.md`
- `docs/external-skills.md`
- `site/index.html`

## Validation Plan

Run:

```powershell
.\scripts\scan_public_safety.ps1
git status -sb
git diff --stat
```
