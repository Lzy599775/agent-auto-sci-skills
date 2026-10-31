# Upstream Update Audit: 2026-10-31

本次审计检查 `agent-auto-sci-skills` 已登记的外部上游，并将有更新且仍满足保留规则的内容同步到本地。当前日期为 `2026-10-31`，按“超过 50 天未更新即移除”的规则，截止日期为 `2026-09-11`。

## 结论

| 上游项目 | 最新提交 | 提交日期 | 本地处理 |
|---|---:|---:|---|
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | `5f2bc03` | 2026-10-26 | 已同步 27 个登记精选目录 |
| [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | `a155655` | 2026-10-27 | 已同步 ARS Codex package `v3.24.0` |
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | `f2d109e` | 2026-10-31 | 未直接覆盖；package manifest 锁定 `b34c63f` |
| [skyllwt/AutoSci](https://github.com/skyllwt/AutoSci) | `3c3922f` | 2026-10-30 | 仅作参考，保留本地原创 router |
| [Haojae/scipilot-figure-skill](https://github.com/Haojae/scipilot-figure-skill) | `43098dd` | 2026-06-15 | 超过 50 天，移除本地 package |
| [Haojae/scipilot-writing-skill](https://github.com/Haojae/scipilot-writing-skill) | `51c5fd3` | 2026-06-15 | 超过 50 天，移除本地 package |
| [xiangyu-Ge/sci-writing-geors](https://github.com/xiangyu-Ge/sci-writing-geors) | `1f58c00` | 2026-06-03 | 超过 50 天，移除本地 adapter |

## K-Dense 同步范围

本次从 `5f2bc03` 同步以下 27 个已登记目录；没有将整个上游仓库复制到本地：

- ML/AI：`aeon`、`pytorch-lightning`、`scikit-learn`、`shap`、`timesfm-forecasting`、`torch-geometric`、`transformers`、`umap-learn`
- Data/Viz：`dask`、`exploratory-data-analysis`、`matplotlib`、`networkx`、`polars`、`scientific-visualization`、`seaborn`、`statistical-analysis`
- Geo/RS：`geomaster`、`geopandas`
- SciComm：`citation-management`、`latex-posters`、`literature-review`、`markdown-mermaid-writing`、`peer-review`、`pptx-posters`、`scientific-schematics`、`scientific-slides`、`scientific-writing`

## ARS 锁定关系

本地 `academic-research-suite` 使用 ARS Codex package `v3.24.0`，package commit 为 `a1556557887f345aac99bdc6027e008e91fef236`。其 `manifest.json` 当前将 ARS source 锁定为 `b34c63f828b3535f403079a4f42bc7955da2f64b`，因此没有把 source 仓库当天更新的 `f2d109e` 擅自混入已封装 package。

本地 standalone 适配保留在 `codex/scripts/ars_codex_quality_gates.py`，用于处理嵌套 package 路径、standalone 运行边界和本地质量门；ARS 原有研究内容、实验产物和 `topology-experiment/results/runs/` 保持在 package 内。

## 50 天删除边界

本规则只作用于有明确 GitHub 上游、且作为第三方内容封装或 adapter 存在的外部 skill。因而本次移除：

- `skills/scipilot-figure-skill`
- `skills/scipilot-writing-skill`
- `skills/geors-sci-writing-adapter`
- `site/skills/scipilot-figure-skill.html`

本地原创 `agent-auto-sci-*`、领域 skill 和本仓库自有 workflow 没有独立外部上游，不因“最近提交时间”缺失而删除。已退休项目的来源、提交日期和许可证判断保留在 [`docs/external-skills.md`](external-skills.md) 中，便于追溯。

## 许可证与公开安全

- ARS 和 K-Dense wrapper 保留各自的许可证、NOTICE 和来源信息。
- GeoRS 上游未检测到明确 LICENSE；本次只保留来源审计，不继续分发其内容或 adapter。
- 本次没有修改科研原始数据、模型参数、seed、fold、checkpoint、authority 或正式结果。
- 临时上游检出目录不属于发布内容，提交前必须删除并通过 `scripts/scan_public_safety.ps1`。
