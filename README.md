# Auto-sci-research

[中文](README.md) | [English](README_EN.md) | [本地介绍页](site/index.html) | [进化档案](site/agent-auto-sci-evolution.html)

> 面向 Codex 的科研 skill 套件，聚焦地理学、体育学、城市健康、GIS/遥感、绿色暴露、体育公园/体育设施、空间公平、文献综述、文献计量、机器学习、论文图件和 SCI 写作。

`Auto-sci-research` 不是“一键写论文”按钮，而是一套可审计、可扩展、可复用的科研工作台。它把选题、文献、数据、GIS/遥感、统计和机器学习、图表、写作、投稿、审稿回复、长期项目记忆拆成清晰的子 skill，让 ChatGPT 与 Codex 知道“现在该用哪个、为什么用、产出什么、边界在哪里”。

## 持久科研工作流

仓库根目录的 [AGENTS.md](AGENTS.md) 提供精简的长期规则和路由入口；详细架构、工作流、证据标准、Research Vault、模板与评估体系从 [ARCHITECTURE.md](ARCHITECTURE.md) 和 [docs/index.md](docs/index.md) 进入。核心原则是：给 agent 一张可导航的地图，而不是把全部规则塞进一个巨大提示词。

当前仓库包含 **14 个可安装 Codex skill**，并在 `urban-exposure-review-radar-workflow` 内置一个隔离的 `academic-research-suite` 子 skill。最新上游检查为 **2026-11-09**：

- ARS Codex 包已同步到 `v3.24.2` (`82725ac`)，上游 ARS 内容锁定到 `fd5ff1b`。
- K-Dense 仓库已检查到 `a25cf9e`，但 27 个精选子目录最近更新均为 2026-10-01，按 30 天规则移除四个封装。
- AutoSci 已检查到 `3c3922f`，仍作为参考源，不覆盖本地原创 router。
- SciPilot Figure、SciPilot Writing 仍已退役。GeoRS 上游在 2026-11-03 更新，恢复本地原创适配；因无明确许可证，不复制上游内容。

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

也可以指定目录：

```powershell
.\scripts\install.ps1 -Target "$env:USERPROFILE\.agents\skills"
```

公开发布前建议运行：

```powershell
.\scripts\scan_public_safety.ps1
```

## 一句话选型

| 你现在要做什么 | 先用哪个 skill |
|---|---|
| 在 ChatGPT/Codex 中自动识别并路由综合科研目标 | `research-orchestrator` |
| 不知道整个科研任务怎么拆 | `auto-sci-research` |
| 搜索、核验、提取、综合文献或审计 citation–claim | `literature` |
| 建文献库、source manifest、checkpoint、长期记忆 | `agent-auto-sci-automation` |
| 把模糊选题变成研究问题、机制和假设 | `agent-auto-sci-methodology` |
| 做 GIS、遥感、可达性、暴露、空间公平 | `agent-auto-sci-geospatial` |
| 做 EDA、统计、论文图表、文献计量图 | `agent-auto-sci-data-viz` |
| 做机器学习、SHAP/XAI、泄漏检查、空间验证 | `agent-auto-sci-ai-ml` |
| 组织论文 argument、投稿、审稿回复 | `agent-auto-sci-scicomm` |
| 按目标期刊近邻论文拆解论证结构 | `agent-auto-sci-scicomm` + `academic_writing_exemplar_protocol`（参考协议，不是新顶层 skill） |
| 为单篇稿件建立私有 exemplar profile 和 Core 3 审批门 | `project-specific-writing-exemplar-workflow` |
| 做体育地理综述、文献计量、政策议程 | `sport-geography-review-bibliometric` |
| 写体育设施/体育公园/暴露公平实证 SCI 论文 | `sport-geography-sci-writing` |
| 判断城市暴露综述、前沿雷达、医学数据库连接路线 | `urban-exposure-review-radar-workflow` |
| 需要通用深度研究、论文管线、审稿模拟 | `urban-exposure-review-radar-workflow/subskills/academic-research-suite` |
| 明确要求筛选已有文献记录、制定纳排标准或生成排除审计 | ARS `sr-screener`（仅显式调用） |
| 写地理学或遥感 SCI 论文 | `geors-sci-writing-adapter` |

## 六类入口

### A. 总控与项目编排

| Skill | 作用 | 输入 | 输出 | 边界 |
|---|---|---|---|---|
| `research-orchestrator` | ChatGPT/Codex 跨表面薄型入口。读取 GitHub 当前 workflow ref，判断任务类型，加载必要标准并交给专项 skill。 | 科研目标、已有材料、期望产出。 | workflow route、使用的 ref/version、专项 skill、QC。 | 不复制完整规则；GitHub 不可用时必须报告 fallback。 |
| `auto-sci-research` | 总控 router。判断任务属于选题、综述、GIS、数据、ML、图件、写作还是投稿，并安排子 skill 顺序。 | 任务描述、项目目标、已有材料、当前阶段。 | 路线图、子 skill 调用顺序、质量门控、进化记录。 | 不替代具体分析或写作子 skill。 |
| `literature` | 证据可追溯的通用文献 workflow V0。 | 研究问题、seed papers、Zotero/DOI/引用或待核查 claim。 | 检索与去重记录、paper note、evidence trace、citation-support 结论。 | 先手工 workflow 与 golden set，不自动猜测缺失字段。 |
| `agent-auto-sci-automation` | 长期项目自动化、source manifest、checkpoint、失败恢复和公开安全边界。 | 数据源、文献源、项目目录、API/密钥边界。 | manifest、状态表、恢复点、失败日志、目录规范。 | 不提交密钥、私有 PDF、付费导出或未发表正文。 |

### B. 方法论与综述路线

| Skill | 作用 | 输入 | 输出 | 适用场景 |
|---|---|---|---|---|
| `agent-auto-sci-methodology` | 把宽泛选题变成可检验问题、机制链条、假设矩阵和证据等级。 | 选题、变量、初步结果、草稿。 | RQ 矩阵、机制图、偏倚审计、因果语言边界。 | 选题不清、机制薄弱、讨论容易过度解释时。 |
| `urban-exposure-review-radar-workflow` | 城市暴露和体育地理高级路线判断。区分系统综述、范围综述、文献计量、批判性综述、前沿雷达和实证设计。 | 主题、目标期刊、语料来源、数据库范围、研究对象。 | route decision、journal gate、正式语料/雷达候选分离、M1-M9 模块路线。 | 绿地暴露、热暴露、体育设施可达性、公共健康数据库、遥感前沿雷达。 |
| `sport-geography-review-bibliometric` | 体育地理综述和文献计量专用。 | 主题、数据库、关键词、初始文献、目标期刊。 | 检索式、PRISMA、编码表、CiteSpace/VOSviewer/bibliometrix 图表计划、政策议程。 | 体育公园、体育设施、绿地公平、城市健康综述。 |

### C. 地理空间、遥感与暴露测度

| Skill | 作用 | 输入 | 输出 | 边界 |
|---|---|---|---|---|
| `agent-auto-sci-geospatial` | GIS、遥感、可达性、绿色/热暴露、空间公平和地图合规。 | 空间数据、指标、代码、地图或方法描述。 | CRS 审计、暴露窗口、可达性流程、空间公平指标、地图检查表。 | 必须区分 exposure、accessibility、availability、quality、use。 |

### D. 数据分析、图表与机器学习

| Skill | 作用 | 输入 | 输出 | 使用提示 |
|---|---|---|---|---|
| `agent-auto-sci-data-viz` | EDA、统计分析、论文图表、文献计量图和 policy matrix。 | 数据、结果、图表需求、已有图件。 | 数据质量审计、统计路线、figure plan、caption、table shell。 | 每张图必须服务一个 claim。 |
| `agent-auto-sci-ai-ml` | 机器学习、SHAP/XAI、空间/时间验证、泄漏检查。 | 特征、标签、模型、验证方式、结果。 | baseline、特征/标签审计、验证切分、指标表、解释边界。 | SHAP 和特征重要性不是因果证据。 |

### E. 写作、投稿与审稿

| Skill | 作用 | 输入 | 输出 | 适用场景 |
|---|---|---|---|---|
| `agent-auto-sci-scicomm` | 科学交流、论文结构、claim-evidence map、投稿信、审稿回复、PPT/海报。 | 草稿、结果、目标期刊、审稿意见。 | IMRAD 大纲、审稿风险扫描、cover letter、response matrix。 | 需要整体论证、投稿材料或审稿回复时。 |
| `project-specific-writing-exemplar-workflow` | 稿件专属 exemplar 生命周期和作者审批门。 | `MANUSCRIPT_ID`、Master 20、稿件证据、目标期刊。 | Core 3 approval、section exemplars、证据/论证地图。 | 只使用项目私有状态，不复制来源原文，不跨项目继承。 |
| `sport-geography-sci-writing` | 体育地理实证 SCI 写作。 | 研究问题、方法、结果、目标期刊。 | 期刊定位、引言 gap chain、方法叙事、结果段落、讨论和政策启示。 | 体育设施可达性、体育公园暴露、空间公平、城市健康机制论文。 |
| `geors-sci-writing-adapter` | 地理学、遥感、暴露与可达性 SCI 写作原创适配。 | 论文类型、研究问题、真实方法与结果、目标期刊。 | claim-evidence map、IMRAD 章节与投稿前核查。 | 不复制无许可上游正文；不改变科学结论。 |

### F. 内置上游子 skill

| Subskill | 位置 | 版本 | 作用 |
|---|---|---:|---|
| `academic-research-suite` | `skills/urban-exposure-review-radar-workflow/subskills/academic-research-suite` | `3.24.2` | 通用深度研究、文献综述、论文写作、同行评审模拟、research-to-paper pipeline、实验规划、PDF/引用检查；`sr-screener` 只处理用户明确要求的记录筛选、纳排标准、pilot、冲突裁决和排除审计。 |

ARS 只在父 skill 判定需要“通用科研生产管线”时调用。`sr-screener` 不会因为用户提到“综述”或“系统综述”而自动触发；只有用户明确要求筛选已有记录、纳排标准、筛选 pilot、冲突裁决、排除审计或筛选报告时才使用。城市暴露、体育地理、暴露/可达性定义、因果语言和正式语料库规则仍由父 skill 把关。

## 推荐组合工作流

### 1. 体育公园/体育设施可达性实证论文

```text
auto-sci-research
-> sport-geography-sci-writing
-> agent-auto-sci-geospatial
-> agent-auto-sci-data-viz
-> agent-auto-sci-methodology
-> agent-auto-sci-scicomm
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
-> agent-auto-sci-geospatial
-> agent-auto-sci-ai-ml
-> agent-auto-sci-data-viz
-> agent-auto-sci-scicomm
```

### 4. 机器学习加空间解释

```text
auto-sci-research
-> agent-auto-sci-ai-ml
-> agent-auto-sci-geospatial
-> agent-auto-sci-methodology
-> agent-auto-sci-scicomm
```

### 5. 论文图件

```text
auto-sci-research
-> agent-auto-sci-data-viz
-> agent-auto-sci-scicomm
```

## Evidence-first 学术写作对标

“对标目标期刊 / 学习顶刊写法”在本套件中不是语言模仿，而是证据优先的 exemplar decomposition：先建立 `OUR_EVIDENCE_MAP` 与 `OUR_ARGUMENT_OUTLINE`，再按每个 substantive section 选择 3–5 篇功能近邻论文，记录 `FULLTEXT`、`ABSTRACT_ONLY` 或 `METADATA_ONLY` 的阅读范围，最后从自己的证据起草并交给本地 Academic Prose Style Guard 和一致性检查做语言质控。

这项能力位于 `agent-auto-sci-scicomm` 的参考协议中，稿件专属生命周期由 `project-specific-writing-exemplar-workflow` 管理，不取代 literature owner 或 domain writing owner。允许学习 section function、argument ordering、evidence presentation 和 figure sequencing；禁止复制原句、独特措辞、citation chain、novelty claim、因果解释或超出自有证据的结果逻辑。

摘要偏好 `PREFERRED_EMPIRICAL_ABSTRACT_PROFILE` 仅是无更严格期刊格式且用户未另行指定时的 soft target；官方期刊要求和 reporting guideline 优先。期刊推荐也必须结合完整稿件（若可用）、研究问题、gap、contribution、methods 和 conclusions，并核验 scope、indexing、OA/APC 与近邻论文，不能只按 IF 排序。

Codex 路由与 ChatGPT Web 共用同一公共协议；跨客户端契约见 [CROSS_CLIENT_WRITING_ROUTING_MATRIX_V1](docs/CROSS_CLIENT_WRITING_ROUTING_MATRIX_V1.md)。

V2 进一步把学术写作契约扩展为可复用的全局偏好：先做 story relevance、sentence academic increment 和 paragraph contribution 审计，再做 exemplar handoff、Academic Prose Style Guard 与本地一致性 lint；保留 Methods 可复现性和因果/测量/不确定性边界。三线表、正文禁手动换行、图表引用 ledger 与 fact-placement ledger 均有可执行检查。ChatGPT Web 可复制 [CHATGPT_GLOBAL_ACADEMIC_WRITING_INSTRUCTIONS_V2](CHATGPT_GLOBAL_ACADEMIC_WRITING_INSTRUCTIONS_V2.txt) 到 Project Instructions 或账户级 Custom Instructions；仓库不会声称已修改用户账户设置。

## 上游与许可证策略

- `Imbad0202/academic-research-skills-codex`：ARS Codex 包，已同步到 `v3.24.2`；许可证和来源见 subskill 内 `LICENSE`、`NOTICE.md`、`manifest.json`。
- `K-Dense-AI/scientific-agent-skills`：27 个精选子目录最近更新均早于 2026-10-10，四个 wrapper 已按 30 天规则退役。
- SciPilot Figure/Writing 保持退役。GeoRS 已恢复原创适配，不分发无许可上游正文。

详见 [docs/external-skills.md](docs/external-skills.md)、[docs/skill-map.md](docs/skill-map.md) 与 [docs/upstream-update-20261109.md](docs/upstream-update-20261109.md)。

## 公开安全原则

本仓库不应包含 API key、token、cookie、私有 PDF、WoS/Scopus 原始导出、未发表论文正文、审稿意见原文、私人数据集、个人绝对路径或无授权第三方内容。发现泄露时应立即移除跟踪、更新忽略规则，并轮换相关密钥。

## ChatGPT 与 Codex 跨表面使用

从 [docs/chatgpt/index.md](docs/chatgpt/index.md) 获取 ChatGPT Project 的一次性 instructions、普通新聊天的 Skill/Plugin 路线、GitHub source-of-truth 合约和测试协议。详细科研规则仍只在版本化仓库中维护。

## License

本仓库主代码与原创文档按 MIT License 发布。第三方 vendored/wrapped 内容遵循其各自许可证；未明确授权的上游只保留链接、来源说明和原创适配，不复制原文。
