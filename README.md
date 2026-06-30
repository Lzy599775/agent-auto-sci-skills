# Auto-sci-research

[中文](README.md) | [English](README_EN.md) | [本地展示页](site/index.html) | [进化档案](site/agent-auto-sci-evolution.html)

> 面向 Codex 的地理学、体育学、城市健康、GIS/遥感、绿色暴露、体育公园/体育设施、公平性、文献综述、机器学习和 SCI 写作 skill 套件。

`Auto-sci-research` 不是“自动写论文”的快捷按钮，而是一套可复用、可审计、可扩展的科研工作台。它把选题、检索、阅读、编码、GIS/遥感处理、统计和机器学习、图表、论文写作、投稿信、审稿回复和项目记忆拆成清晰的子 skill，让你在 Codex 里知道“现在该用哪个工具、为什么用、产出什么、边界在哪里”。

当前仓库包含 **17 个可安装 Codex skill**，并额外在 `urban-exposure-review-radar-workflow` 内封装了一个隔离的 `academic-research-suite` 子 skill。2026-06-30 已刷新上游：ARS 更新到 `v0.1.15`，K-Dense 检查到 `v2.53.0-6-g0807ddb` 但本仓库精选范围内无文件变化，SciPilot Figure 仍为 `v2.1.0-1-g43098dd`，新增 SciPilot Writing `v1.0.0` 和 GeoRS SCI Writing Adapter。

## 一句话选型

| 你现在要做什么 | 先用哪个 skill |
|---|---|
| 不知道整个科研任务怎么拆 | `auto-sci-research` |
| 建文献库、source manifest、checkpoint、长期记忆 | `agent-auto-sci-automation` |
| 把模糊选题变成研究问题、机制和假设 | `agent-auto-sci-methodology` |
| 做 GIS、遥感、可达性、暴露、空间公平 | `agent-auto-sci-geospatial` |
| 做 EDA、统计、论文图表、文献计量图 | `agent-auto-sci-data-viz` |
| 做机器学习、SHAP/XAI、泄露检查、空间验证 | `agent-auto-sci-ai-ml` |
| 组织论文 argument、投稿、审稿回复 | `agent-auto-sci-scicomm` |
| 做体育地理综述、文献计量、政策议程 | `sport-geography-review-bibliometric` |
| 写体育设施/体育公园/暴露公平实证 SCI 论文 | `sport-geography-sci-writing` |
| 判断城市暴露综述、前沿雷达、医学数据库连接路线 | `urban-exposure-review-radar-workflow` |
| 需要通用深度研究、论文管线、审稿模拟 | `urban-exposure-review-radar-workflow/subskills/academic-research-suite` |
| 不知道数据该画什么图，或要投稿级图件 QA | `scipilot-figure-skill` |
| 润色、翻译、去 AI 味、写 cover letter/rebuttal | `scipilot-writing-skill` |
| 写地理/遥感 SCI 的标题、摘要、IMRAD、cover letter | `geors-sci-writing-adapter` |
| 需要上游 K-Dense 技术 playbook | `kdense-*selected` 四个精选包 |

## 安装

```powershell
git clone https://github.com/Lzy599775/agent-auto-sci-skills.git
cd agent-auto-sci-skills
.\scripts\install.ps1
```

默认安装到：

```text
$env:USERPROFILE\.codex\skills
```

安装后重启 Codex。也可以指定目录：

```powershell
.\scripts\install.ps1 -Target "$env:USERPROFILE\.agents\skills"
```

发布前安全扫描：

```powershell
.\scripts\scan_public_safety.ps1
```

## 分类总览

### A. 总控与项目编排

| Skill | 作用 | 典型产出 | 不要让它做什么 |
|---|---|---|---|
| `auto-sci-research` | 总控路由。判断任务属于选题、综述、GIS、数据、ML、图件、写作还是投稿，并安排子 skill 顺序。 | 任务路线图、子 skill 调用顺序、质量门控、进化记录。 | 不替代具体分析或写作子 skill；它负责路由和管线。 |
| `agent-auto-sci-automation` | 长期项目自动化、安全边界、source manifest、checkpoint 和失败恢复。 | 文献/数据清单、状态表、失败日志、API 边界、复现目录规范。 | 不提交密钥、私有 PDF、付费数据库导出、未发表正文。 |

### B. 方法论与研究设计

| Skill | 作用 | 典型产出 | 适用场景 |
|---|---|---|---|
| `agent-auto-sci-methodology` | 把宽泛选题变成可检验问题、机制链条、假设矩阵和证据等级。 | SMART 研究问题、机制图、偏倚审计、因果语言边界。 | 选题不清、机制薄弱、讨论容易过度解释时。 |
| `urban-exposure-review-radar-workflow` | 城市暴露和体育地理高级路线判别。区分系统综述、范围综述、文献计量+批判性综述、前沿雷达和实证设计。 | route decision、正式语料/雷达候选分离、期刊证据门槛、M1-M9 模块路线。 | 绿地暴露、热暴露、体育设施可达性、公共健康数据库、遥感前沿雷达。 |
| `sport-geography-review-bibliometric` | 体育地理综述和文献计量专用。 | 检索式、PRISMA、编码表、CiteSpace/VOSviewer/bibliometrix 图表计划、政策议程。 | 体育公园、体育设施、绿地公平、城市健康综述。 |

### C. 地理空间、遥感与暴露测度

| Skill | 作用 | 典型产出 | 边界 |
|---|---|---|---|
| `agent-auto-sci-geospatial` | GIS、遥感、可达性、绿地/热暴露、空间公平和地图合规。 | CRS 审计、暴露窗口、可达性算法、空间公平指标、地图检查表。 | 不混用 exposure、accessibility、availability、quality 和 use。 |
| `kdense-geospatial-rs-selected` | K-Dense 精选 GeoPandas、GeoMaster 等上游技术 playbook。 | 具体库和技术路线、矢量/栅格处理提示、遥感处理注意点。 | 只提供技术参考，研究设计仍由 geospatial/methodology 把关。 |
| `geors-sci-writing-adapter` | 地理/遥感 SCI 写作适配，尤其适合遥感反演、时空变化、暴露和可达性论文。 | 标题、摘要、Introduction、Methods、Results、Discussion、Conclusion、cover letter。 | 上游未声明许可证，本仓库只保留原创适配，不复制未授权全文。 |

### D. 数据分析、图表与机器学习

| Skill | 作用 | 典型产出 | 使用提示 |
|---|---|---|---|
| `agent-auto-sci-data-viz` | EDA、统计分析、论文图表、文献计量图和 policy matrix。 | 数据质量审计、统计路线、figure plan、caption、table shell。 | 每张图必须服务一个 claim。 |
| `agent-auto-sci-ai-ml` | 机器学习、SHAP/XAI、空间/时间验证、泄露检查。 | baseline、特征/标签审计、验证切分、指标表、解释边界。 | SHAP 和特征重要性不是因果证据。 |
| `kdense-data-viz-selected` | K-Dense 精选 EDA、统计、Matplotlib、Seaborn、NetworkX、Polars、Dask。 | 技术路线、绘图和大表处理参考。 | 不替代论文 claim 设计。 |
| `kdense-ml-ai-selected` | K-Dense 精选 scikit-learn、PyTorch Lightning、Transformers、SHAP、TimesFM、GNN、UMAP。 | 模型选择、训练评估、解释方法、时间序列/图模型技术参考。 | 需要和 methodology/AI-ML skill 一起控制验证和解释边界。 |
| `scipilot-figure-skill` | 科研数据图顾问。先剖析数据和论证目标，再选图、绘图、视觉自检。 | 图型选择、绘图代码方向、色盲安全、字体/裁切/重叠检查、导出建议。 | 用户说“帮我画图”时也要先确认图要证明什么。 |

### E. 写作、投稿与审稿

| Skill | 作用 | 典型产出 | 适用场景 |
|---|---|---|---|
| `agent-auto-sci-scicomm` | 科学交流、论文结构、claim-evidence map、投稿信、审稿回复、PPT/海报。 | IMRAD 大纲、审稿风险扫描、cover letter、response matrix。 | 需要整体论证、投稿材料或审稿回复时。 |
| `sport-geography-sci-writing` | 体育地理实证 SCI 写作。 | 期刊定位、引言 gap chain、方法叙事、结果段落、讨论和政策启示。 | 体育设施可达性、体育公园暴露、空间公平、城市健康机制论文。 |
| `scipilot-writing-skill` | SciPilot 写作与润色。覆盖中英互译、润色、缩写/扩写、去 AI 味、图表标题、cover letter 和 rebuttal。 | 改后文本、回译核对、修改日志、writing_lint 机检报告、残留问题。 | 最适合论文最后一公里的语言、逻辑和投稿文本处理。 |
| `kdense-scicomm-selected` | K-Dense 精选科学写作、审稿、引用、slides、posters、schematics。 | 写作模板、引用检查思路、slides/posters/schematics 技术参考。 | 作为上游技术/模板库，不替代本地领域写作判断。 |

### F. 内置上游子 skill

| Subskill | 位置 | 作用 |
|---|---|---|
| `academic-research-suite` | `skills/urban-exposure-review-radar-workflow/subskills/academic-research-suite` | 通用深度研究、文献综述、论文写作、同行评审模拟、完整 research-to-paper pipeline、实验规划和引用完整性检查。 |

ARS 只在父 skill 判断需要“通用科研生产管线”时调用。城市暴露、体育地理、暴露/可达性定义、因果语言和正式语料库规则仍由父 skill 把关。

## 推荐工作流

### 1. 体育公园/体育设施可达性实证论文

```text
auto-sci-research
-> sport-geography-sci-writing
-> agent-auto-sci-geospatial
-> agent-auto-sci-data-viz
-> agent-auto-sci-methodology
-> scipilot-writing-skill
```

### 2. 绿地/热暴露与城市健康综述

```text
auto-sci-research
-> urban-exposure-review-radar-workflow
-> sport-geography-review-bibliometric
-> agent-auto-sci-methodology
-> agent-auto-sci-data-viz
-> agent-auto-sci-scicomm
```

### 3. 遥感反演或时空变化 SCI 论文

```text
auto-sci-research
-> geors-sci-writing-adapter
-> agent-auto-sci-geospatial
-> agent-auto-sci-ai-ml
-> agent-auto-sci-data-viz
-> scipilot-writing-skill
```

### 4. 机器学习 + 空间解释

```text
auto-sci-research
-> agent-auto-sci-ai-ml
-> kdense-ml-ai-selected
-> agent-auto-sci-geospatial
-> agent-auto-sci-methodology
-> agent-auto-sci-scicomm
```

### 5. 论文图件

```text
auto-sci-research
-> agent-auto-sci-data-viz
-> kdense-data-viz-selected
-> scipilot-figure-skill
-> agent-auto-sci-scicomm
```

## 详细子 Skill 索引

| Skill | 领域偏向 | 何时使用 | 输入 | 输出 |
|---|---|---|---|---|
| `auto-sci-research` | 总控 | 任务跨多个阶段或不知道先用哪个 skill | 任务描述、项目目标、已有材料 | 路线图、子 skill 顺序、质量门控 |
| `agent-auto-sci-automation` | 自动化 | 长期项目、数据/文献清单、API/安全边界 | 数据源、文献源、目录 | manifest、checkpoint、失败恢复方案 |
| `agent-auto-sci-methodology` | 方法论 | 研究问题、机制、因果语言、证据等级 | 选题、变量、结果或草稿 | RQ、机制图、偏倚审计、限制 |
| `agent-auto-sci-geospatial` | GIS/RS | 空间分析、可达性、暴露、地图 | 空间数据、指标、代码或方法 | CRS/尺度审计、流程修正、地图检查 |
| `agent-auto-sci-data-viz` | 数据/图表 | EDA、统计、文献计量、论文图表 | 数据、结果、图表需求 | figure plan、统计路线、caption |
| `agent-auto-sci-ai-ml` | ML/XAI | 建模、SHAP、验证、泄露检查 | 特征、标签、模型、结果 | baseline、验证方案、解释边界 |
| `agent-auto-sci-scicomm` | 写作/投稿 | 论文结构、argument、投稿信、rebuttal | 草稿、结果、审稿意见 | claim-evidence map、改写路线、回复矩阵 |
| `sport-geography-review-bibliometric` | 体育地理综述 | 系统综述、scoping review、文献计量 | 主题、数据库、初始文献 | 检索式、PRISMA、编码和图表计划 |
| `sport-geography-sci-writing` | 体育地理 SCI | 体育设施/公园/暴露/公平实证论文 | 结果、方法、目标期刊 | IMRAD 写作方案和段落 |
| `urban-exposure-review-radar-workflow` | 城市暴露 | 综述路线、前沿雷达、医学数据库连接 | 主题、目标期刊、语料来源 | 路线判别、证据门槛、雷达/语料分离 |
| `kdense-ml-ai-selected` | 上游 ML 技术 | 需要具体 ML 工具 playbook | 模型任务、技术栈 | 技术参考和注意点 |
| `kdense-data-viz-selected` | 上游数据可视化 | 需要统计/绘图库技术细节 | 数据和图表任务 | 库级别路线和代码参考 |
| `kdense-geospatial-rs-selected` | 上游 GIS/RS | 需要 GeoPandas/GeoMaster 技术细节 | 空间数据任务 | 技术路线和处理提示 |
| `kdense-scicomm-selected` | 上游科学交流 | 需要写作、引用、slides/poster 模板参考 | 写作或展示任务 | 模板和结构建议 |
| `scipilot-figure-skill` | 图件顾问 | 不知道用什么图，或图不够投稿级 | 数据、claim、目标期刊 | 图型建议、绘图、自检和导出 |
| `scipilot-writing-skill` | 语言润色 | 翻译、润色、去 AI 味、cover letter、rebuttal | 文本、目标期刊、载体、保守度 | 改后文本、回译、修改日志、机检报告 |
| `geors-sci-writing-adapter` | 地理/遥感写作 | 地理/遥感/暴露 SCI 章节写作 | 论文类型、数据方法、目标期刊 | 章节写作、期刊定位、空间写作风险检查 |

## 上游与许可证策略

- `Haojae/scipilot-writing-skill`：MIT，完整封装并保留 LICENSE/NOTICE。
- `Haojae/scipilot-figure-skill`：MIT，已封装为图件顾问。
- `Imbad0202/academic-research-skills-codex`：ARS Codex 包，已同步到 v0.1.15；许可证和来源见 subskill 内 `LICENSE`、`NOTICE.md`、`manifest.json`。
- `K-Dense-AI/scientific-agent-skills`：只保留 4 个与本研究方向强相关的精选 wrapper，不全量引入。
- `xiangyu-Ge/sci-writing-geors`：未检测到明确 LICENSE，因此只做原创 Codex 适配，不复制上游参考全文。

详见 [docs/external-skills.md](docs/external-skills.md) 与 [docs/upstream-update-20260630.md](docs/upstream-update-20260630.md)。

## 公开安全原则

本仓库不应包含 API key、token、cookie、私有 PDF、WoS/Scopus 原始导出、未发表论文正文、审稿意见原文、私人数据集、个人绝对路径或无授权第三方内容。发现泄露时应立即移除跟踪、更新忽略规则，并轮换相关密钥。

## License

本仓库主代码与原创文档按 MIT License 发布。第三方 vendored/wrapped 内容遵循其各自许可证；未明确授权的上游只保留链接、来源说明和原创适配，不复制原文。
