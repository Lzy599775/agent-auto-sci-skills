# External Skill Coverage Audit

Use this file when checking whether the local `auto-sci-research` system has preserved the useful logic of the two GitHub repositories while adapting it to geography + sport science.

## 1. Source Status

| Source | Local copy | Current checked status | Local adaptation |
|---|---|---|---|
| `skyllwt/AutoSci` | `<project-root>/agent_auto_sci/external_repos/AutoSci` | local `HEAD` matched `origin/main` at audit time | converted from command-centered autonomous research into Codex-readable workflows, memory schemas, checkpoints, and evolution records |
| `K-Dense-AI/scientific-agent-skills` | `<project-root>/agent_auto_sci/external_repos/scientific-agent-skills` | local `HEAD` matched `origin/main` at audit time | selected only ML/AI, data/viz, geospatial/remote sensing, scientific communication, and methodology families |
| AI evolution HTML guide | `<project-root>/agent_auto_sci/external_notes/AI进化可视化HTML页面制作指南.txt` | downloaded reference | adapted into a local research-agent evolution archive rather than a generic promotional page |

## 2. AutoSci Coverage

| AutoSci component | Preserved locally | Local owner |
|---|---|---|
| source preparation and `/init` | project root, source manifest, source boundaries, source-to-memory conversion | `agent-auto-sci-automation` |
| `/discover` and `/daily-arxiv` | current-literature refresh as optional workflow, with source provenance | `agent-auto-sci-automation`, `sport-geography-review-bibliometric` |
| wiki/OmegaWiki memory | structured entities for papers, concepts, methods, failed ideas, outputs, reviews, evolution | `agent-auto-sci-automation` |
| `/ideate` | landscape scan, mechanism-first idea generation, critique, feasibility screen | `agent-auto-sci-methodology` |
| `/novelty` | novelty matrix, prior-art search, conservative scoring, failed-idea check | `agent-auto-sci-methodology`, `sport-geography-review-bibliometric` |
| `/exp-design` | baseline, ablation, sensitivity, robustness, generalization plan | `agent-auto-sci-ai-ml`, `agent-auto-sci-data-viz`, `agent-auto-sci-geospatial` |
| `/paper-plan` | claim-evidence map, section plan, figure plan, citation plan | `agent-auto-sci-scicomm` |
| `/review` | internal peer-review pass, evidence risk, method risk, writing risk | `agent-auto-sci-scicomm`, `agent-auto-sci-methodology` |
| `/rebuttal` | reviewer-comment decomposition and response strategy | `agent-auto-sci-scicomm` |
| `/visualize` | output visualization and evolution archive | `agent-auto-sci-data-viz`, `auto-sci-research` |

## 3. K-Dense Coverage

| K-Dense family | Included skills or ideas | Local owner |
|---|---|---|
| Machine learning and AI | scikit-learn, PyTorch Lightning, transformers, SHAP, time-series modeling, baseline/evaluation rules | `agent-auto-sci-ai-ml` |
| Data analysis and visualization | EDA, statistical testing, effect size, matplotlib/seaborn, scientific visualization, network visualization | `agent-auto-sci-data-viz` |
| Geospatial science and remote sensing | GeoPandas, geomaster, CRS, raster/vector, spatial joins, OSM/network, remote-sensing indices | `agent-auto-sci-geospatial` |
| Scientific communication | scientific writing, peer review, slides, schematics, citation management | `agent-auto-sci-scicomm` |
| Research methodology | hypothesis generation, critical thinking, scholar evaluation, evidence appraisal | `agent-auto-sci-methodology` |

## 4. What Was Intentionally Not Copied

- Full biomedical, chemistry, quantum, molecular, clinical, and lab-automation skill sets from K-Dense are out of scope.
- AutoSci commands that assume an unavailable autonomous backend are converted into local procedures instead of copied as executable commands.
- Any API keys, tokens, private endpoints, and personal credentials are excluded.
- External wording is not copied verbatim as a skill body; it is transformed into local procedures for the user's sport-geography research system.

## 5. Remaining Improvement Targets

- Add deterministic scripts for repeated literature-library audits, PRISMA table generation, and figure inventory.
- Add optional web/API adapters only after API credentials and data-security boundaries are explicitly configured.
- Add example outputs for one complete review route and one empirical sport-geography paper route.

## 6. 2026-06-01 External Deployment Addendum

Additional research skills deployed after the initial AutoSci/K-Dense audit:

| Source | Installed local skill | Status |
|---|---|---|
| `assafelovic/gpt-researcher` | `gpt-researcher` | installed as a direct upstream skill |
| `alchaincyf/nuwa-skill` | `huashu-nuwa` | installed as a direct upstream skill |
| `Imbad0202/academic-research-skills-codex` | `academic-research-suite` | installed as a direct upstream skill |
| `leo-lilinxiao/codex-autoresearch` | `codex-autoresearch` | installed as a direct upstream skill |
| `hwang847/codex-paper-reader` | `codex-paper-reader` | installed with local frontmatter name adapted for discoverability |
| `Epsilon617/Codex-Academic-Skills` | `codex-academic-skills-index` | wrapped as a local skill because upstream is an index, not a direct skill |
| `STRYXTN/awesome-ai-research-writing` | `awesome-ai-research-writing` | wrapped as a local skill because upstream is a prompt library, not a direct skill |

