# Upstream Update Audit - 2026-10-12

本次审计逐项核对了当前仓库已登记的第三方来源，并只同步有明确来源、许可证和本地封装边界的内容。没有启动正式科研实验，也没有修改科研数据、模型参数、seed、fold、checkpoint 或正式运行证据。

## 结果总表

| 上游项目 | 最新提交 | 本地处理 | 许可证/边界 |
|---|---|---|---|
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | `92ace75ac21efe19a620434e0ca4e356081fe807` | 已同步 27 个登记精选目录 | MIT；保留各 wrapper 的 `LICENSE.upstream.md`，未全量 vendoring |
| [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | `52228e8280dd1770e18ecfc3b1fdf16b13b58104` (`v3.23.0`) | 已同步 ARS Codex 包，并保留 standalone 适配 | CC BY-NC 4.0；保留 `LICENSE`、`NOTICE.md`、`manifest.json` |
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | `6ab4b03bf70a118a1b3ee7f3263ed9f19031061b` | 随 ARS package 锁定 | 由 ARS package manifest 记录 |
| [skyllwt/AutoSci](https://github.com/skyllwt/AutoSci) | `f5c2fe009c6683b6aa5b668de759a0610c938aaf` | 仅作参考，未覆盖本地原创 router | 不将其新运行时、依赖或实验产物引入本仓库 |
| [Haojae/scipilot-writing-skill](https://github.com/Haojae/scipilot-writing-skill) | `51c5fd39e2a386b7ddca021181b4c8071d3c3da7` | 无更新 | MIT；本地已是该提交 |
| [Haojae/scipilot-figure-skill](https://github.com/Haojae/scipilot-figure-skill) | `43098ddb9e6a6d142218540c114f9ed38922fc42` | 无更新 | MIT；本地已是该提交 |
| [xiangyu-Ge/sci-writing-geors](https://github.com/xiangyu-Ge/sci-writing-geors) | `1f58c002b5c11fe8a893dd74b3986e0bb3c1f2f2` | 无更新；继续使用原创 adapter | 当前检查仍未发现明确 LICENSE，不复制其正文或代码 |

## 已同步内容

### K-Dense 精选封装

本轮同步以下 27 个登记目录到 `92ace75`：

- `kdense-ml-ai-selected`：`aeon`、`pytorch-lightning`、`scikit-learn`、`shap`、`timesfm-forecasting`、`torch-geometric`、`transformers`、`umap-learn`
- `kdense-data-viz-selected`：`dask`、`exploratory-data-analysis`、`matplotlib`、`networkx`、`polars`、`scientific-visualization`、`seaborn`、`statistical-analysis`
- `kdense-geospatial-rs-selected`：`geomaster`、`geopandas`
- `kdense-scicomm-selected`：`citation-management`、`latex-posters`、`literature-review`、`markdown-mermaid-writing`、`peer-review`、`pptx-posters`、`scientific-schematics`、`scientific-slides`、`scientific-writing`

上游已删除的 TimesFM 示例输出文件也按源快照移除；这些是示例生成物，不是本地科研结果。

### Academic Research Suite

本地 `academic-research-suite` 更新到 `3.23.0`。本轮保留并重新验证了 nested standalone 适配：

- 嵌套 `skills/academic-research-suite/...` manifest 路径解析到本地 suite root；
- 缺少 Desktop plugin 的 standalone 包跳过仅针对插件 bundle、插件版本和仓库级 topology receipt 的 gate；
- skill manifest、root router、routing core、hook safety、fixture、upstream lock 等 skill-level gate 仍保持启用；
- `sr-screener` 是 explicit-only：只有用户明确要求记录筛选、纳排标准、pilot、冲突裁决、排除审计或筛选报告时才调用；
- 新增的 run ledger、acronym checks、citation-locale evals 和 routing-core 检查随 package 保留。

### AutoSci 参考源

AutoSci 已检查到 `f5c2fe0`。该版本包含 `hiera-experiment`、二维码和工具相关变化，但本仓库的 `auto-sci-research` 是面向当前科研方向的原创 router。为避免引入不同的运行时依赖、实验假设和目录协议，本轮不覆盖、不 vendoring AutoSci 新内容，仅记录为参考源。

## 文档更新

- `README.md`、`README_EN.md`：更新日期、版本、上游提交和 explicit-only 边界。
- `docs/skill-map.md`：新增 ARS `sr-screener` 选择规则。
- `site/index.html`、`site/agent-auto-sci-evolution.html`：更新本地介绍页、版本事件和审计链接。
- 各 K-Dense wrapper 的 `NOTICE.md`、ARS `VERSION` 与 `NOTICE.md`：更新来源和版本锁定。

## 未改变的对象

- 未修改原始科研数据、analysis-ready 数据、正式结果、checkpoint、authority、manifest 运行状态或 topology 运行证据。
- 未推送任何分支；目标是直接更新 `main`。
- 保留工作区中既有的 `_rollback/`、`_staging/` 和 `results/runs/` 未跟踪目录，不纳入提交。
