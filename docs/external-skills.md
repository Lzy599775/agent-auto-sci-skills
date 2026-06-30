# External Skills And References

本仓库优先维护原创和领域适配 skill。第三方项目只在能明显增强体育地理、城市暴露、GIS/遥感、文献综述、图件或 SCI 写作工作流时封装，并遵守许可证边界。

Latest upstream check: [`docs/upstream-update-20260630.md`](upstream-update-20260630.md).

## Packaged Or Wrapped Sources

| Upstream project | Local package | Current checked snapshot | License/status | Packaging decision |
|---|---|---:|---|---|
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | `kdense-ml-ai-selected`, `kdense-data-viz-selected`, `kdense-geospatial-rs-selected`, `kdense-scicomm-selected` | `0807ddb` (`v2.53.0-6-g0807ddb`) | Upstream license kept in wrappers | Only selected ML/AI, data-viz, geospatial/RS, and scicomm areas are packaged. The 2026-06-30 upstream changes did not touch selected packaged subskills. |
| [Haojae/scipilot-figure-skill](https://github.com/Haojae/scipilot-figure-skill) | `scipilot-figure-skill` | `43098dd` (`v2.1.0-1-g43098dd`) | MIT | Full figure-advisor package retained with NOTICE and LICENSE. |
| [Haojae/scipilot-writing-skill](https://github.com/Haojae/scipilot-writing-skill) | `scipilot-writing-skill` | `51c5fd3` (`v1.0.0`) | MIT | Full writing/polishing package vendored with scripts, references, examples, NOTICE, and LICENSE. |
| [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | `urban-exposure-review-radar-workflow/subskills/academic-research-suite` | `efdbc2a` (`v0.1.15`) | CC BY-NC 4.0 via vendored ARS license | Vendored as an isolated subskill. Parent urban-exposure skill keeps domain authority. |
| [xiangyu-Ge/sci-writing-geors](https://github.com/xiangyu-Ge/sci-writing-geors) | `geors-sci-writing-adapter` | `1f58c00` | No explicit LICENSE file detected | No upstream text vendored. Local package is an original Codex adapter with attribution and source link only. |

## Optional Reference Sources

| Project | Use |
|---|---|
| [skyllwt/AutoSci](https://github.com/skyllwt/AutoSci) | Long-horizon research-agent memory and workflow ideas. Checked `6f5a9f6` on 2026-06-30; no direct vendoring. |
| [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | Autonomous web deep research reference. |
| [hwang847/codex-paper-reader](https://github.com/hwang847/codex-paper-reader) | Local PDF reading workflow reference. |
| [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | Academic writing prompt-library style reference. |
| [STRYXTN/awesome-ai-research-writing](https://github.com/STRYXTN/awesome-ai-research-writing) | Academic writing prompt templates. |
| [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | Persona/thinking-framework skill distillation. |
| [leo-lilinxiao/codex-autoresearch](https://github.com/leo-lilinxiao/codex-autoresearch) | Improve-verify loops. |
| [bionoob7/nlr-workflow](https://github.com/bionoob7/nlr-workflow) | Narrative literature review workflow discipline. |
| [limi124/remote-sensing-research-radar](https://github.com/limi124/remote-sensing-research-radar) | Remote-sensing and Geospatial AI frontier radar reference. |

## Packaging Rules

1. Check license before copying files.
2. Preserve attribution and license files for vendored upstream content.
3. Do not copy private examples, keys, paid data exports, or unlicensed large text.
4. Prefer selected wrappers over wholesale importing when the upstream project is broad.
5. Treat external APIs/cloud tools as optional and disabled unless the user explicitly configures them.
6. If a repository has no explicit license, do not vendor its text or code into the public repo; create an original adapter and link to the source instead.
