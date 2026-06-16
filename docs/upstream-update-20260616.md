# Upstream Update And Skill Consolidation, 2026-06-16

## Consolidation Result

The local `Skill` workspace is the canonical working copy for
`Lzy599775/agent-auto-sci-skills`.

Local-only consolidation folders were added to `.gitignore`:

- `external_repos/`
- `archives/`
- `incoming/`
- `inventory/`
- `unpackaged/`
- `_local/`

Moved into the local `Skill` workspace:

| Source label | Destination label | Purpose |
|---|---|---|
| `Skill_external_repos` | `external_repos/20260616_consolidation/from_Skill_external_repos` | Historical external skill repositories. |
| `A_literature_metrics external repositories` | `external_repos/20260616_consolidation/from_A_literature_metrics_agent_auto_sci_external_repos` | External research and skill repositories collected during earlier packaging. |
| `A_literature_metrics/agent-auto-sci-skills` | `archives/20260616_consolidation/from_A_literature_metrics/agent-auto-sci-skills_dirty_clone` | Older dirty clone, archived instead of merged blindly. |
| `A_literature_metrics/github_upload` | `archives/20260616_consolidation/from_A_literature_metrics/github_upload` | Older upload staging clones. |
| `A_literature_metrics/agent_auto_sci/local_skill_packages` | `archives/20260616_consolidation/from_A_literature_metrics/local_skill_packages` | Old local packaged skill copy. |
| `A_sportpark/tmp` | `archives/20260616_consolidation/from_A_sportpark/tmp` | Historical Darwin and installer temporary skill work. |

Post-cleanup scan:

- `A_sportpark`: 0 `SKILL.md`, 0 `skills` directories.
- `A_literature_metrics`: 0 `SKILL.md`, 0 `skills` directories.

## Packaged Skills In `skills/`

### Self-developed or domain-adapted core skills

| Skill | Role |
|---|---|
| `auto-sci-research` | Umbrella router, project memory, skill routing, external skill governance, research-to-manuscript workflow. |
| `agent-auto-sci-automation` | Research automation, source manifest, checkpoint, API and failure-memory protocol. |
| `agent-auto-sci-methodology` | Research question design, mechanism logic, evidence grading, bias audit. |
| `agent-auto-sci-geospatial` | GIS, remote sensing, accessibility, exposure, spatial equity, map compliance. |
| `agent-auto-sci-data-viz` | EDA, statistics, publication figures, bibliometric visuals, figure story and caption logic. |
| `agent-auto-sci-ai-ml` | Machine learning, SHAP/XAI, leakage checks, spatial/temporal validation. |
| `agent-auto-sci-scicomm` | Scientific communication, manuscript structure, rebuttal, journal fit, slides and policy narrative. |
| `sport-geography-review-bibliometric` | Sport geography systematic/scoping/bibliometric review and critical coding. |
| `sport-geography-sci-writing` | Sport geography SCI writing for exposure, accessibility, equity and urban health. |
| `urban-exposure-review-radar-workflow` | Urban exposure review route decision, frontier radar, medical database linkage, and ARS-backed paper pipeline. |

### Packaged upstream wrappers

| Wrapper | Upstream | Packaged scope |
|---|---|---|
| `kdense-ml-ai-selected` | `K-Dense-AI/scientific-agent-skills` | Selected ML/AI skills. |
| `kdense-data-viz-selected` | `K-Dense-AI/scientific-agent-skills` | Selected EDA, statistics, plotting and scientific visualization skills. |
| `kdense-geospatial-rs-selected` | `K-Dense-AI/scientific-agent-skills` | Selected geospatial and remote-sensing skills. |
| `kdense-scicomm-selected` | `K-Dense-AI/scientific-agent-skills` | Selected scientific writing, review, citation, slides, posters and schematics skills. |
| `scipilot-figure-skill` | `Haojae/scipilot-figure-skill` | Scientific figure advisor, chart choice, rendering and visual QA. |
| `academic-research-suite` | `Imbad0202/academic-research-skills-codex` | Vendored inside `urban-exposure-review-radar-workflow/subskills/academic-research-suite`. |

## Research Writing And Drawing Related Skills

Primary skills:

- `agent-auto-sci-scicomm`
- `agent-auto-sci-data-viz`
- `sport-geography-sci-writing`
- `sport-geography-review-bibliometric`
- `urban-exposure-review-radar-workflow`
- `auto-sci-research`
- `scipilot-figure-skill`
- `kdense-scicomm-selected`
- `kdense-data-viz-selected`

Important subskills:

- `academic-research-suite`
- `scientific-writing`
- `peer-review`
- `citation-management`
- `literature-review`
- `markdown-mermaid-writing`
- `scientific-slides`
- `scientific-schematics`
- `latex-posters`
- `pptx-posters`
- `scientific-visualization`
- `matplotlib`
- `seaborn`
- `statistical-analysis`
- `exploratory-data-analysis`
- `networkx`

## Upstream Update Check

| Upstream | Previous local snapshot | Latest checked snapshot | Status | Local action |
|---|---:|---:|---|---|
| `K-Dense-AI/scientific-agent-skills` | `9881fe4` / `effb57c` | `2093901` (`v2.52.0-3-g2093901`) | Updated upstream | Re-copied selected subskills into four K-Dense wrappers and updated NOTICE/license files. |
| `Haojae/scipilot-figure-skill` | `2c90803` | `43098dd` (`v2.1.0-1-g43098dd`) | Updated upstream | Replaced local SciPilot skill content, preserved local agents metadata, updated NOTICE. |
| `Imbad0202/academic-research-skills-codex` | `1857434` / adapter `0.1.11` | `763bccd` / adapter `0.1.12` | Updated upstream | Replaced vendored ARS subskill and updated wrapper documentation. |
| `skyllwt/AutoSci` | `d89cc72` | `71469e8` | Updated upstream | Downloaded latest full upstream into `external_repos/latest`; not re-wrapped in this pass because current local AutoSci adaptation is already domain-specific and needs a separate diff review. |
| `assafelovic/gpt-researcher` | `b364917` | `b364917` | No upstream change | No package change. |
| `hwang847/codex-paper-reader` | `59bad33` | `59bad33` | No upstream change | No package change. |

## Notes

- Historical dirty clones were archived, not merged, to avoid overwriting newer canonical files.
- External repositories are local-only and ignored by Git.
- Public packaged content remains under `skills/`, `docs/`, `scripts/`, `site/`, README files and repository metadata.
