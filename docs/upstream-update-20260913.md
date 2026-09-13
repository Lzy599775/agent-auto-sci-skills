# Upstream Update Check, 2026-09-13

This audit refreshed every configured upstream mirror and compared the selected packaged paths against the latest GitHub `main` snapshots.

| Upstream | Previous snapshot | Latest snapshot | Result | Local action |
|---|---:|---:|---|---|
| `K-Dense-AI/scientific-agent-skills` | `1e5eeff` (`v2.66.0`) | `c1ed16d` (`v2.66.0+main`) | Updated | Synchronized the selected `geomaster`, `scientific-slides`, and `umap-learn` directories. Other selected directories were unchanged. |
| `Imbad0202/academic-research-skills-codex` | `925975e` (`v0.1.28`) | `925975e` | No change | No package change. |
| `skyllwt/AutoSci` | `8642426` | `9ff3087` | Reference updated | Reviewed the dependency pointer change to a GitHub-hosted `requests` fork; the local original router and requirements were not overwritten. |
| `Haojae/scipilot-figure-skill` | `43098dd` | `43098dd` | No change | No package change. |
| `Haojae/scipilot-writing-skill` | `51c5fd3` | `51c5fd3` | No change | No package change. |
| `xiangyu-Ge/sci-writing-geors` | `1f58c00` | `1f58c00` | No change | No package change. |

The K-Dense package remains a selected wrapper rather than a wholesale mirror. Unselected upstream changes, including new database and genomics skills, were not imported. Existing attribution and license boundaries remain unchanged.
