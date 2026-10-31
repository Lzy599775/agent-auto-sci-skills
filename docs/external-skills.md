# External Skills And References

本仓库优先维护原创和领域适配 skill。第三方项目只有在能明确增强体育地理、城市暴露、GIS/遥感、文献综述、图件或 SCI 写作工作流时才封装，并严格遵守许可证边界。

Latest upstream check: [`docs/upstream-update-20261031.md`](upstream-update-20261031.md).

## Packaged Or Wrapped Sources

| Upstream project | Local package | Current checked snapshot | License/status | Packaging decision |
|---|---|---:|---|---|
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | `kdense-ml-ai-selected`, `kdense-data-viz-selected`, `kdense-geospatial-rs-selected`, `kdense-scicomm-selected` | `5f2bc03` (`main`) | MIT, upstream license kept in wrappers | 27 registered ML/AI, data-viz, geospatial/RS, and scicomm directories synchronized on 2026-10-31; the full upstream repository is not vendored. |
| [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | `urban-exposure-review-radar-workflow/subskills/academic-research-suite` | `a155655` (`v3.24.0`, ARS source `b34c63f`) | CC BY-NC 4.0 via vendored ARS license | Vendored as an isolated subskill. Parent urban-exposure skill keeps domain authority; `sr-screener` is explicit-only. |

## Optional Reference Sources

| Project | Use | 2026-10-31 status |
|---|---|---|
| [skyllwt/AutoSci](https://github.com/skyllwt/AutoSci) | Long-horizon research-agent memory and workflow ideas. | Checked at `3c3922f`. New upstream changes remain reference-only; the local original router and requirements were not overwritten. |

## Retired By The 50-Day Rule

The following packages were removed from the installable skill set because their latest upstream commits were older than the 2026-09-11 cutoff:

| Upstream project | Last upstream commit | Last commit date | Removed local package |
|---|---:|---:|---|
| [Haojae/scipilot-figure-skill](https://github.com/Haojae/scipilot-figure-skill) | `43098dd` | 2026-06-15 | `scipilot-figure-skill` |
| [Haojae/scipilot-writing-skill](https://github.com/Haojae/scipilot-writing-skill) | `51c5fd3` | 2026-06-15 | `scipilot-writing-skill` |
| [xiangyu-Ge/sci-writing-geors](https://github.com/xiangyu-Ge/sci-writing-geors) | `1f58c00` | 2026-06-03 | `geors-sci-writing-adapter` |

Local original skills without a separate upstream repository are maintained under the repository's own commit history and are not classified as stale external packages by this rule.
| [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | Autonomous web deep research reference. | Reference only. |
| [hwang847/codex-paper-reader](https://github.com/hwang847/codex-paper-reader) | Local PDF reading workflow reference. | Reference only. |
| [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | Academic writing prompt-library style reference. | Reference only. |
| [STRYXTN/awesome-ai-research-writing](https://github.com/STRYXTN/awesome-ai-research-writing) | Academic writing prompt templates. | Reference only. |
| [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | Persona/thinking-framework skill distillation. | Reference only. |
| [leo-lilinxiao/codex-autoresearch](https://github.com/leo-lilinxiao/codex-autoresearch) | Improve-verify loops. | Reference only. |
| [bionoob7/nlr-workflow](https://github.com/bionoob7/nlr-workflow) | Narrative literature review workflow discipline. | Reference only. |
| [limi124/remote-sensing-research-radar](https://github.com/limi124/remote-sensing-research-radar) | Remote-sensing and Geospatial AI frontier radar reference. | Reference only. |

## Packaging Rules

1. Check license before copying files.
2. Preserve attribution and license files for vendored upstream content.
3. Do not copy private examples, keys, paid data exports, or unlicensed large text.
4. Prefer selected wrappers over wholesale importing when the upstream project is broad.
5. Treat external APIs/cloud tools as optional and disabled unless the user explicitly configures them.
6. If a repository has no explicit license, do not vendor its text or code into the public repo; create an original adapter and link to the source instead.
