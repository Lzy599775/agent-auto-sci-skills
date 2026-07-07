# Use Cases

本页把常见科研任务映射到推荐 skill 组合。原则是先确定任务性质，再进入具体工具，不用一次性加载所有 skill。

## 1. 体育公园或体育设施可达性实证论文

| 阶段 | 推荐 skill | 产出 |
|---|---|---|
| 任务拆解 | `auto-sci-research` | 研究路线、子 skill 顺序、质量门控 |
| 论文定位 | `sport-geography-sci-writing` | 目标期刊、gap chain、IMRAD 结构 |
| 空间处理 | `agent-auto-sci-geospatial` | CRS 审计、可达性算法、暴露/使用区分 |
| 统计与图件 | `agent-auto-sci-data-viz`, `scipilot-figure-skill` | figure plan、统计路线、投稿级图件 QA |
| 解释边界 | `agent-auto-sci-methodology` | 机制链、因果语言、限制 |
| 最后润色 | `scipilot-writing-skill` | 改后文本、回译、修改日志、lint 报告 |

## 2. 绿地或热暴露与城市健康综述

| 阶段 | 推荐 skill | 产出 |
|---|---|---|
| 路线判断 | `urban-exposure-review-radar-workflow` | 系统综述、范围综述、文献计量、批判性综述或前沿雷达判定 |
| 检索与编码 | `sport-geography-review-bibliometric` | 检索式、PRISMA、编码表、计量图计划 |
| 方法论审计 | `agent-auto-sci-methodology` | 证据等级、偏倚来源、机制框架 |
| 图表叙事 | `agent-auto-sci-data-viz` | 趋势图、主题图、政策矩阵 |
| 论文论证 | `agent-auto-sci-scicomm` | claim-evidence map、讨论框架、投稿材料 |

## 3. 遥感反演或时空变化 SCI 论文

| 阶段 | 推荐 skill | 产出 |
|---|---|---|
| 写作适配 | `geors-sci-writing-adapter` | 标题、摘要、IMRAD 段落、cover letter |
| 空间与遥感 | `agent-auto-sci-geospatial`, `kdense-geospatial-rs-selected` | 数据产品、空间尺度、遥感处理路线 |
| 建模与解释 | `agent-auto-sci-ai-ml`, `kdense-ml-ai-selected` | 模型路线、验证切分、解释边界 |
| 图件 | `agent-auto-sci-data-viz`, `scipilot-figure-skill` | 主图和补充图设计、视觉 QA |
| 最后文本 | `scipilot-writing-skill` | 语言润色、回译核对、投稿文本 |

## 4. 论文图件和可视化

| 情况 | 推荐 skill | 注意点 |
|---|---|---|
| 不知道该画什么 | `scipilot-figure-skill` | 先说明图要支持的 claim |
| 需要统计或 EDA 路线 | `agent-auto-sci-data-viz` | 先做数据质量和变量审计 |
| 需要具体库技术参考 | `kdense-data-viz-selected` | 可调用 Matplotlib、Seaborn、NetworkX、Polars、Dask、统计分析子包 |
| 需要论文叙事 | `agent-auto-sci-scicomm` | caption 和正文必须互相支持 |

## 5. 机器学习和空间解释

| 阶段 | 推荐 skill | 产出 |
|---|---|---|
| 设计验证 | `agent-auto-sci-ai-ml` | baseline、泄漏清单、空间/时间切分 |
| 工具参考 | `kdense-ml-ai-selected` | scikit-learn、Lightning、Transformers、SHAP、TimesFM、GNN、UMAP playbook |
| 空间约束 | `agent-auto-sci-geospatial` | 空间单元、尺度、邻近性、空间自相关边界 |
| 结论边界 | `agent-auto-sci-methodology` | 预测、解释、机制、因果的边界 |

## 6. 投稿、审稿回复和语言最后一公里

| 任务 | 推荐 skill | 产出 |
|---|---|---|
| 论文整体论证 | `agent-auto-sci-scicomm` | claim-evidence map、结构重写、审稿风险 |
| 体育地理实证论文 | `sport-geography-sci-writing` | 领域化 IMRAD、讨论和政策启示 |
| 地理/遥感 SCI 章节 | `geors-sci-writing-adapter` | 章节写作、空间语言风险检查 |
| 润色、翻译、去 AI 味 | `scipilot-writing-skill` | 改后文本、回译、修改日志、lint |
| 模板和展示材料 | `kdense-scicomm-selected` | slides、posters、schematics、citation 技术参考 |
