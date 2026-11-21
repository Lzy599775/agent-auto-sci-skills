# Upstream Update Audit: 2026-11-21

检查日为 2026-11-21；30 天截止日为 2026-10-22。仅对有明确外部 GitHub 上游的封装按其可安装技能目录的最近提交判定是否退役；参考仓库的普通文档提交不为旧技能续期。本地原创技能由本仓库维护，不能因为没有独立外部仓库就判为失效。此次未执行正式科研实验，也未修改数据、模型、seed、fold、authority、checkpoint 或 ARS 发布包锁。

| 来源 | GitHub 最新提交 | 最近提交日期 (UTC) | 本轮决定 |
|---|---|---|---|
| [ARS Codex 包](https://github.com/Imbad0202/academic-research-skills-codex) | `82725acb393c4410ac6f47634a7f51b40a162fa4` | 2026-11-06 | 与本地 `v3.24.2` 相同，无可同步的新包；保留 |
| [ARS 原始仓库](https://github.com/Imbad0202/academic-research-skills) | `bd57330f63f4b089dde8fdef9bf5f009ecc89f0c` | 2026-11-20 | 比包内 `fd5ff1b` 更新；等待 Codex 包适配，不直接混入 |
| [ARS experiment-agent](https://github.com/Imbad0202/experiment-agent) | `3b788b750081e8423f72e9bb99a9d1e25ea903c4` | 2026-11-04 | 包 manifest 锁定 `e291e7d`；不单独替换组件 |
| [K-Dense](https://github.com/K-Dense-AI/scientific-agent-skills) | `ec59a29a03d5c40f73ab40878df04860bc00e876` | 2026-11-16 | 仓库更新，但原封装的 27 个技能目录无新提交；继续退役 |
| [GeoRS 写作来源](https://github.com/xiangyu-Ge/sci-writing-geors) | `f515996d516b3d7b316dce9decc35cefc2e6d989` | 2026-11-03 | 原创本地适配保留；无明确上游 LICENSE，不复制正文或代码 |
| [AutoSci 参考源](https://github.com/skyllwt/AutoSci) | `aa852fd929128545ee3dce2e5629a4aeeab6ccf9` | 2026-11-13 | 相比 `3c3922f` 仅更新文档群二维码；不覆盖原创 router |
| [SciPilot Figure](https://github.com/Haojae/scipilot-figure-skill) | `43098ddb9e6a6d142218540c114f9ed38922fc42` | 2026-06-15 | 继续退役 |
| [SciPilot Writing](https://github.com/Haojae/scipilot-writing-skill) | `51c5fd39e2a386b7ddca021181b4c8071d3c3da7` | 2026-06-15 | 继续退役 |

## K-Dense 逐目录核对

下面日期来自 `origin/main` 对每个 `skills/<name>` 执行路径限定的最近提交查询。仓库级 HEAD 的新文档或其他技能更新不改变这些日期。所有 27 项均早于截止日；四个精选 wrapper 不恢复。

| 原封装 | 上游技能目录 | 最近路径提交 | 日期 |
|---|---|---|---|
| ML/AI | `aeon` | `a92663a0` | 2026-10-01 |
| ML/AI | `pytorch-lightning` | `a92663a0` | 2026-10-01 |
| ML/AI | `scikit-learn` | `a92663a0` | 2026-10-01 |
| ML/AI | `shap` | `a92663a0` | 2026-10-01 |
| ML/AI | `timesfm-forecasting` | `a92663a0` | 2026-10-01 |
| ML/AI | `torch-geometric` | `a92663a0` | 2026-10-01 |
| ML/AI | `transformers` | `a92663a0` | 2026-10-01 |
| ML/AI | `umap-learn` | `a92663a0` | 2026-10-01 |
| Data/Viz | `dask` | `a92663a0` | 2026-10-01 |
| Data/Viz | `exploratory-data-analysis` | `a92663a0` | 2026-10-01 |
| Data/Viz | `matplotlib` | `a92663a0` | 2026-10-01 |
| Data/Viz | `networkx` | `a92663a0` | 2026-10-01 |
| Data/Viz | `polars` | `a92663a0` | 2026-10-01 |
| Data/Viz | `scientific-visualization` | `a92663a0` | 2026-10-01 |
| Data/Viz | `seaborn` | `a92663a0` | 2026-10-01 |
| Data/Viz | `statistical-analysis` | `a92663a0` | 2026-10-01 |
| Geo/RS | `geomaster` | `a92663a0` | 2026-10-01 |
| Geo/RS | `geopandas` | `a92663a0` | 2026-10-01 |
| SciComm | `citation-management` | `a92663a0` | 2026-10-01 |
| SciComm | `latex-posters` | `a92663a0` | 2026-10-01 |
| SciComm | `literature-review` | `a92663a0` | 2026-10-01 |
| SciComm | `markdown-mermaid-writing` | `a92663a0` | 2026-10-01 |
| SciComm | `peer-review` | `a92663a0` | 2026-10-01 |
| SciComm | `pptx-posters` | `a92663a0` | 2026-10-01 |
| SciComm | `scientific-schematics` | `a92663a0` | 2026-10-01 |
| SciComm | `scientific-slides` | `f7a50ed2` | 2026-10-01 |
| SciComm | `scientific-writing` | `a92663a0` | 2026-10-01 |

## 发布包与本地状态

ARS Codex `manifest.json` 的 `adapter_version` 为 `3.24.2`，其 ARS source lock 为 `fd5ff1b858374219b4d342e38587b66e18f61cbd`，experiment-agent lock 为 `e291e7dc7ca268b2de7e1a9cf23bc2eef5dc0651`。原始 ARS 仓库自该锁后有新提交，但这些不是已适配的 Codex 发布包；保持整包一致性。GeoRS 是原创适配，不分发无许可上游文本。SciPilot Writing 退役目录内的独立 `writing_lint.py` 是本仓库后续写作校验工具，不构成 SciPilot 技能恢复，也不在本轮删除。

结果：**14 个顶层可安装技能 + 1 个内置 ARS 子技能**，与上次相同；**本轮新增删除 0 项，技能正文更新 0 项**。已更新来源登记、README、HTML 导航及审计链接。历史决策见 [2026-11-09 审计](upstream-update-20261109.md)。
