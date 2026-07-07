# Upstream Update Check, 2026-07-07

This pass refreshed the ignored local mirrors under `external_repos/latest`, checked packaged upstream scope, and updated public wrappers where appropriate.

## Summary

| Upstream | Previous checked snapshot | Latest checked snapshot | Status | Local action |
|---|---:|---:|---|---|
| `K-Dense-AI/scientific-agent-skills` | `0807ddb` (`v2.53.0-6-g0807ddb`) | `4d97e29` (`v2.53.0-10-g4d97e29`) | Upstream changed | Selected wrapper scope changed only in `statistical-analysis`. Synced that subskill into `kdense-data-viz-selected`; other selected K-Dense areas were checked and unchanged. |
| `Haojae/scipilot-figure-skill` | `43098dd` (`v2.1.0-1-g43098dd`) | `43098dd` (`v2.1.0-1-g43098dd`) | No upstream change | No package change. |
| `Haojae/scipilot-writing-skill` | `51c5fd3` (`v1.0.0`) | `51c5fd3` (`v1.0.0`) | No upstream change | No package change. |
| `Imbad0202/academic-research-skills-codex` | `efdbc2a` (`v0.1.15`) | `8626ccb` (`v0.1.17`) | Upstream changed | Re-synced `urban-exposure-review-radar-workflow/subskills/academic-research-suite`, restored root `LICENSE`/`NOTICE.md`, and aligned version metadata to `0.1.17`. |
| `skyllwt/AutoSci` | `6f5a9f6` (`v1.0.0-29-g6f5a9f6`) | `a01841d` (`v1.0.0-30-ga01841d`) | Upstream changed | Mirror refreshed only. Delta touched `assets/wechat_group_4.png`; no public package change. |
| `xiangyu-Ge/sci-writing-geors` | `1f58c00` | `1f58c00` | No upstream change | No package change. No explicit LICENSE file detected, so the local package remains an original adapter with attribution only. |

## K-Dense Scope Check

Diff check from `0807ddb` to `4d97e29` against currently selected packaged areas found changes only under:

- `skills/statistical-analysis/SKILL.md`
- `skills/statistical-analysis/references/assumptions_and_diagnostics.md`
- `skills/statistical-analysis/references/bayesian_statistics.md`
- `skills/statistical-analysis/references/effect_sizes_and_power.md`
- `skills/statistical-analysis/references/reporting_standards.md`
- `skills/statistical-analysis/scripts/assumption_checks.py`

These files were synced into:

```text
skills/kdense-data-viz-selected/subskills/k-dense/statistical-analysis
```

Checked selected areas with no file-level change:

- ML/AI: `scikit-learn`, `pytorch-lightning`, `transformers`, `shap`, `timesfm-forecasting`, `torch-geometric`, `umap-learn`
- Data/visualization except statistics: `exploratory-data-analysis`, `matplotlib`, `seaborn`, `scientific-visualization`, `networkx`, `polars`, `dask`
- Geospatial/RS: `geomaster`, `geopandas`
- Scientific communication: `scientific-writing`, `peer-review`, `scientific-slides`, `scientific-schematics`, `citation-management`, `literature-review`, `latex-posters`, `pptx-posters`

## Licensing Notes

- `K-Dense-AI/scientific-agent-skills`: MIT; selected vendored wrappers keep `LICENSE.upstream.md` and wrapper-level NOTICE files.
- `Haojae/scipilot-writing-skill`: MIT; safe to vendor with license and notice.
- `Haojae/scipilot-figure-skill`: MIT; safe to vendor with license and notice.
- `Imbad0202/academic-research-skills-codex`: CC BY-NC 4.0; isolated as a subskill under `urban-exposure-review-radar-workflow`.
- `xiangyu-Ge/sci-writing-geors`: no explicit `LICENSE` file in checked snapshot; public package remains an original adapter and does not copy upstream text.

## Public Files Updated

- `skills/kdense-data-viz-selected/subskills/k-dense/statistical-analysis/`
- `skills/kdense-*-selected/SKILL.md`
- `skills/kdense-*-selected/NOTICE.md`
- `skills/urban-exposure-review-radar-workflow/subskills/academic-research-suite/`
- `README.md`
- `README_EN.md`
- `docs/skill-map.md`
- `docs/external-skills.md`
- `docs/use-cases.md`
- `site/index.html`
- `site/agent-auto-sci-evolution.html`

## Validation Plan

Run:

```powershell
$env:PYTHONUTF8='1'
# Check top-level SKILL.md frontmatter/name/description.
$check = @'
from pathlib import Path
import re, sys
errs = []
for skill in sorted(p for p in Path('skills').iterdir() if p.is_dir()):
    f = skill / 'SKILL.md'
    if not f.exists():
        errs.append(f'{skill}: missing SKILL.md')
        continue
    text = f.read_text(encoding='utf-8')
    end = text.find('\n---\n', 4) if text.startswith('---\n') else -1
    fm = text[4:end] if end != -1 else ''
    if end == -1 or not re.search(r'^name:\s*.+$', fm, re.M) or not re.search(r'^description:\s*.+$', fm, re.M):
        errs.append(f'{f}: invalid frontmatter')
if errs:
    print('\n'.join(errs))
    sys.exit(1)
print('Top-level SKILL.md frontmatter OK')
'@
$check | python -
.\scripts\scan_public_safety.ps1
git diff --check
git status -sb
```
