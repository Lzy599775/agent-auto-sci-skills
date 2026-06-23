# External Skills And References

This repository primarily contains self-developed and domain-adapted skills. Some upstream skills are included as selected, attributed wrappers when they directly strengthen the Auto-sci-research workflow.

Current vendored/wrapped upstream additions:

Latest upstream check: [`docs/upstream-update-20260623.md`](upstream-update-20260623.md).

| Upstream project | Local wrapper | Scope |
|---|---|---|
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | `kdense-ml-ai-selected`, `kdense-data-viz-selected`, `kdense-geospatial-rs-selected`, `kdense-scicomm-selected` | Only four selected areas are packaged: ML/AI, data analysis and visualization, geospatial/remote sensing, and scientific communication. The full upstream repository is not installed wholesale. Current checked upstream snapshot: `ddd2f7f` (`v2.52.0-4-gddd2f7f`); selected packaged subskill files were unchanged from the previous packaged snapshot. |
| [Haojae/scipilot-figure-skill](https://github.com/Haojae/scipilot-figure-skill) | `scipilot-figure-skill` | Publication-figure design, chart choice, visual QA, CJK-safe labels, and figure-story alignment. Current packaged upstream snapshot: `43098dd` (`v2.1.0-1-g43098dd`). |
| [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | `urban-exposure-review-radar-workflow/subskills/academic-research-suite` | Codex-native Academic Research Suite vendored as an isolated subskill inside the urban exposure workflow. Current packaged adapter version: `0.1.14`; upstream ARS commit is recorded in the subskill manifest. |

The projects below remain optional references or extension sources.

| Project | Use |
|---|---|
| [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | README and academic-writing prompt-library style reference |
| [STRYXTN/awesome-ai-research-writing](https://github.com/STRYXTN/awesome-ai-research-writing) | academic writing prompt templates |
| [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | autonomous web deep research |
| [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | persona/thinking-framework skill distillation |
| [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | academic research suite for Codex; currently wrapped inside `urban-exposure-review-radar-workflow` |
| [leo-lilinxiao/codex-autoresearch](https://github.com/leo-lilinxiao/codex-autoresearch) | long-running improve-verify loops |
| [hwang847/codex-paper-reader](https://github.com/hwang847/codex-paper-reader) | local PDF reading workflow |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | broad scientific agent skill organization; partially wrapped in selected local modules |
| [Haojae/scipilot-figure-skill](https://github.com/Haojae/scipilot-figure-skill) | scientific figure design and visual QA; wrapped as a local figure companion skill |
| [skyllwt/AutoSci](https://github.com/skyllwt/AutoSci) | long-horizon research-agent memory and workflow ideas |
| [bionoob7/nlr-workflow](https://github.com/bionoob7/nlr-workflow) | narrative literature review workflow discipline: search, screening, extraction, synthesis, drafting, audit, citation export, and submission gates |
| [limi124/remote-sensing-research-radar](https://github.com/limi124/remote-sensing-research-radar) | remote-sensing and Geospatial AI frontier radar, CV-to-RS transfer analysis, candidate ranking, and research idea generation |

Before adapting a third-party project:

1. Check the license.
2. Keep attribution.
3. Do not copy private examples or keys.
4. Avoid installing overlapping skills without a clear use case; prefer selected wrappers over wholesale copying.
5. Treat external APIs and cloud tools as optional.
