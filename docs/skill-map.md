# Skill Map

本页按“什么时候用哪个 skill”组织，而不是按文件夹字母顺序组织。

## 1. 七层架构

| 层级 | 目的 | Skills |
|---|---|---|
| L0 总控 | 判断任务类型、安排子 skill、维护科研管线 | `auto-sci-research` |
| L1 自动化与安全 | source manifest、checkpoint、长期记忆、公开安全 | `agent-auto-sci-automation` |
| L2 方法论 | 研究问题、机制、证据等级、因果语言 | `agent-auto-sci-methodology` |
| L3 空间与暴露 | GIS、遥感、可达性、暴露、空间公平 | `agent-auto-sci-geospatial`, `kdense-geospatial-rs-selected` |
| L4 数据、图表与模型 | EDA、统计、ML/XAI、论文图件 | `agent-auto-sci-data-viz`, `agent-auto-sci-ai-ml`, `kdense-data-viz-selected`, `kdense-ml-ai-selected`, `scipilot-figure-skill` |
| L5 综述与领域路线 | 体育地理综述、城市暴露综述、前沿雷达 | `sport-geography-review-bibliometric`, `urban-exposure-review-radar-workflow` |
| L6 写作与投稿 | SCI 写作、润色、投稿信、审稿回复 | `sport-geography-sci-writing`, `geors-sci-writing-adapter`, `agent-auto-sci-scicomm`, `scipilot-writing-skill`, `kdense-scicomm-selected` |

## 2. 子 Skill 作用矩阵

| Skill | 类型 | 最适用任务 | 典型产出 | 调用边界 |
|---|---|---|---|---|
| `auto-sci-research` | 总控 | 跨选题、文献、数据、分析、图表、写作、投稿的复杂任务 | 路线图、子 skill 顺序、质量门控 | 不替代专项 skill |
| `agent-auto-sci-automation` | 自动化 | 长期项目、source manifest、checkpoint、API 安全 | 项目清单、状态表、恢复点 | 不提交密钥或私有材料 |
| `agent-auto-sci-methodology` | 方法论 | 选题收敛、机制、因果语言、证据分级 | RQ 矩阵、机制图、偏倚审计 | 不把相关写成因果 |
| `agent-auto-sci-geospatial` | GIS/RS | 可达性、绿地/热暴露、LCZ、空间公平、地图 | CRS 审计、暴露窗口、空间指标 | 不混用 exposure/accessibility/use |
| `agent-auto-sci-data-viz` | 数据/图表 | EDA、统计、文献计量图、论文图表 | figure plan、caption、table shell | 图表服务 claim |
| `agent-auto-sci-ai-ml` | ML/XAI | 机器学习、SHAP、泄露检查、空间/时间验证 | baseline、验证切分、解释边界 | 特征重要性不是因果证据 |
| `agent-auto-sci-scicomm` | 写作/投稿 | 论文结构、投稿信、rebuttal、展示材料 | claim-evidence map、回复矩阵 | 润色不扩张证据 |
| `sport-geography-review-bibliometric` | 领域综述 | 体育公园、体育设施、绿地公平、城市健康综述 | 检索式、PRISMA、编码表、政策议程 | 文献计量必须上升到框架 |
| `sport-geography-sci-writing` | 领域写作 | 体育设施可达性、体育公园暴露、空间公平实证论文 | 期刊定位、IMRAD 段落、讨论 | 从公共问题进入，不从技术指标开篇 |
| `urban-exposure-review-radar-workflow` | 领域 workflow | 城市暴露综述、前沿雷达、医学数据库连接 | route decision、journal gate、radar handoff | 正式语料和雷达候选分开 |
| `kdense-ml-ai-selected` | 上游 wrapper | ML/AI 技术 playbook | 技术路线、模型注意点 | 只作技术参考 |
| `kdense-data-viz-selected` | 上游 wrapper | EDA、统计、绘图、大表处理 | 绘图和分析工具路线 | 不替代 claim 设计 |
| `kdense-geospatial-rs-selected` | 上游 wrapper | GeoPandas、GeoMaster、遥感/GIS 技术 | 空间处理技术路线 | 不绕过 CRS/尺度审计 |
| `kdense-scicomm-selected` | 上游 wrapper | 写作、审稿、引用、slides/posters/schematics | 模板和技术参考 | 不替代领域贡献判断 |
| `scipilot-figure-skill` | 图件顾问 | 图型选择、投稿级绘图、视觉 QA | 图型建议、代码方向、导出检查 | 先确定图要证明什么 |
| `scipilot-writing-skill` | 写作润色 | 翻译、润色、去 AI 味、cover letter、rebuttal | 改后文本、回译、日志、lint 报告 | 不改事实、数值、引用 |
| `geors-sci-writing-adapter` | 地理/遥感写作 | 遥感反演、时空变化、暴露/可达性 SCI 写作 | 章节写法、期刊定位、空间写作检查 | 原创适配，不复制未授权上游全文 |

## 3. 内置 Academic Research Suite

| Subskill | 位置 | 版本 | 作用 |
|---|---|---:|---|
| `academic-research-suite` | `urban-exposure-review-radar-workflow/subskills/academic-research-suite` | `0.1.15` | 深度研究、文献综述、论文管线、同行评审模拟、引用完整性、实验规划 |

使用原则：

1. 先由 `urban-exposure-review-radar-workflow` 判断是否需要 ARS。
2. 默认只读 ARS 根 `SKILL.md` 和一个必要的 `WORKFLOW.md`。
3. 城市暴露、体育地理、正式语料库、可达性/使用区分和因果语言仍由父 skill 决定。

## 4. 常见工作流

| 任务 | 推荐顺序 |
|---|---|
| 体育设施可达性实证论文 | `auto-sci-research -> sport-geography-sci-writing -> agent-auto-sci-geospatial -> agent-auto-sci-data-viz -> scipilot-writing-skill` |
| 绿地/热暴露综述 | `auto-sci-research -> urban-exposure-review-radar-workflow -> sport-geography-review-bibliometric -> agent-auto-sci-methodology -> agent-auto-sci-scicomm` |
| 遥感反演/时空变化 SCI 写作 | `auto-sci-research -> geors-sci-writing-adapter -> agent-auto-sci-geospatial -> agent-auto-sci-ai-ml -> scipilot-writing-skill` |
| 论文图件 | `agent-auto-sci-data-viz -> kdense-data-viz-selected -> scipilot-figure-skill -> agent-auto-sci-scicomm` |
| 机器学习解释 | `agent-auto-sci-ai-ml -> kdense-ml-ai-selected -> agent-auto-sci-methodology -> agent-auto-sci-scicomm` |

## 5. 选择规则

- 任务跨度大：先 `auto-sci-research`。
- 任务是“该不该这样研究”：先 `agent-auto-sci-methodology`。
- 任务涉及空间数据、地图、暴露或可达性：先 `agent-auto-sci-geospatial`。
- 任务涉及图表：先 `agent-auto-sci-data-viz`，再 `scipilot-figure-skill`。
- 任务涉及语言最后一公里：先 `scipilot-writing-skill`。
- 任务是地理/遥感 SCI 章节写作：先 `geors-sci-writing-adapter`。
- 任务是体育地理实证论文：先 `sport-geography-sci-writing`。
- 任务是城市暴露综述或前沿雷达：先 `urban-exposure-review-radar-workflow`。
