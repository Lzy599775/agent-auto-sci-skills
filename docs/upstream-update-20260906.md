# Upstream Update Check, 2026-09-06

This audit refreshed every configured upstream mirror and compared the selected packaged paths against the latest GitHub `main` snapshots. Only the existing package scope was synchronized.

## Results

| Upstream | Previous snapshot | Latest snapshot | Result | Local action |
|---|---:|---:|---|---|
| `K-Dense-AI/scientific-agent-skills` | `ad21a38` (`v2.62.0`) | `1e5eeff` (`v2.66.0`) | Updated | Synchronized all 27 registered selected directories; 26 had file-level changes and `timesfm-forecasting` was file-identical. |
| `Imbad0202/academic-research-skills-codex` | `f8d6b06` (`v0.1.22`) | `925975e` (`v0.1.28`) | Updated | Re-synchronized the isolated ARS package, including current `ars/`, `codex/`, `agents/`, root entrypoint, manifest, version, and license. |
| `skyllwt/AutoSci` | `ff3485e` | `8642426` | Reference updated | Reviewed the image-only rotating WeChat asset delta; the local domain-specific router was not overwritten. |
| `Haojae/scipilot-figure-skill` | `43098dd` | `43098dd` | No change | No package change. |
| `Haojae/scipilot-writing-skill` | `51c5fd3` | `51c5fd3` | No change | No package change. |
| `xiangyu-Ge/sci-writing-geors` | `1f58c00` | `1f58c00` | No change | Kept the original attribution-only adapter because no explicit upstream license was detected. |

## Package Scope

- The four K-Dense wrappers remain selected packages, not a wholesale mirror of the upstream catalog.
- The ARS package remains isolated below `urban-exposure-review-radar-workflow`; its parent retains authority over urban exposure definitions, accessibility/use separation, corpus rules, and causal-language boundaries.
- AutoSci remains a reference source. Its latest delta does not justify changing the local research router.

## Validation Targets

The maintenance pass validates top-level skill frontmatter, K-Dense selected directory parity, ARS version and manifest alignment, ARS quality gates, public safety rules, whitespace, Python syntax, and the local HTML navigator at desktop and mobile widths. `_rollback/`, `_staging/`, and `external_repos/` remain local-only and are not release paths.

## License Boundary

K-Dense and SciPilot retain MIT notices. ARS retains its upstream CC BY-NC 4.0 license and attribution. GeoRS remains an original adapter because its source repository has no explicit license file in the checked snapshot.
