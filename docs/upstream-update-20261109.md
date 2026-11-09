# Upstream Update Audit: 2026-11-09

本次按“超过 30 天未更新即从当前技能集合移除”复核有明确 GitHub 上游的外部封装。检查日为 2026-11-09，截止日为 2026-10-10；最新提交早于截止日即退役。K-Dense 按每个已封装子目录的最新提交判定，不能用仓库级文档或安全扫描提交替子技能续期。本地原创技能按本仓库维护，不以外部仓库的日期推断其年龄。

| 上游 | 最新提交 | 最近提交日期 | 当前处理 |
|---|---|---|---|
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | `a25cf9e` | 2026-11-02 | 仓库有新提交，但 27 个已封装技能目录最近更新均为 2026-10-01；移除四个精选封装 |
| [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | `82725acb393c4410ac6f47634a7f51b40a162fa4` | 2026-11-06 | 同步 `v3.24.2` 包 |
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | `6d93886` | 2026-11-06 | 仅核对；包 manifest 锁定 `fd5ff1b858374219b4d342e38587b66e18f61cbd`，不直接混入 main |
| [skyllwt/AutoSci](https://github.com/skyllwt/AutoSci) | `3c3922f` | 2026-10-30 | 仅为本地原创路由的历史参考，不是可安装的上游封装 |
| [xiangyu-Ge/sci-writing-geors](https://github.com/xiangyu-Ge/sci-writing-geors) | `f515996d516b3d7b316dce9decc35cefc2e6d989` | 2026-11-03 | 恢复本地原创 GeoRS 写作适配；上游无明确 LICENSE，不复制其文本或代码 |
| [Haojae/scipilot-figure-skill](https://github.com/Haojae/scipilot-figure-skill) | `43098dd` | 2026-06-15 | 保持退役 |
| [Haojae/scipilot-writing-skill](https://github.com/Haojae/scipilot-writing-skill) | `51c5fd3` | 2026-06-15 | 保持退役 |

## K-Dense 子技能逐项核对

以下路径均为 [K-Dense 上游](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills) 的 `skills/<name>`。`scientific-slides` 最后路径提交为 `f7a50ed`（2026-10-01）；其余 26 项的最后路径提交均为 `a92663a`（2026-10-01）。截至本次检查都超过 30 天。

| 原封装 | 上游子目录 |
|---|---|
| `kdense-ml-ai-selected` | `aeon`, `pytorch-lightning`, `scikit-learn`, `shap`, `timesfm-forecasting`, `torch-geometric`, `transformers`, `umap-learn` |
| `kdense-data-viz-selected` | `dask`, `exploratory-data-analysis`, `matplotlib`, `networkx`, `polars`, `scientific-visualization`, `seaborn`, `statistical-analysis` |
| `kdense-geospatial-rs-selected` | `geomaster`, `geopandas` |
| `kdense-scicomm-selected` | `citation-management`, `latex-posters`, `literature-review`, `markdown-mermaid-writing`, `peer-review`, `pptx-posters`, `scientific-schematics`, `scientific-slides`, `scientific-writing` |

## ARS 锁定关系与本地边界

同步的 Codex package 为 `v3.24.2`、commit `82725acb393c4410ac6f47634a7f51b40a162fa4`，其 `manifest.json` 锁定 ARS source `fd5ff1b858374219b4d342e38587b66e18f61cbd`。保留本仓库嵌套 standalone 质量门适配、CC BY-NC 4.0 许可证、NOTICE 和未跟踪的 `codex/topology-experiment/results/runs/`。`sr-screener` 仍仅在用户明确要求记录筛选时使用。更新不执行正式实验，也不修改研究数据、模型、seed、fold、authority 或 checkpoint。
ARS 内部 `experiment-agent` 的上游 HEAD 为 `3b788b7`（2026-11-04），发布包 manifest 锁定 `e291e7d`。本次保持发布包锁定版本，不单独混入上游 HEAD。

## 当前集合

当前可安装顶层技能：14 个。ARS 为 `urban-exposure-review-radar-workflow` 下的隔离子技能，不另计；GeoRS 为原创适配，只引用近期更新的无许可上游。历史退役信息保留在 [来源登记](external-skills.md) 和 [2026-10-31 审计](upstream-update-20261031.md) 中。
