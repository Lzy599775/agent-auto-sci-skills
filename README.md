# Auto-sci-research

[中文](README.md) | [English](README_EN.md) | [🌐 展示页](site/index.html) | [进化档案](site/agent-auto-sci-evolution.html)

> 面向 **Codex** 的地理学 + 体育学 + 城市健康科研 Skill 套件。  
> From literature review to bibliometrics, geospatial exposure assessment, machine learning, SCI writing, peer review, and policy agenda.

`Auto-sci-research` 是一套面向科研写作与科研自动化的 Codex Skills。它服务于体育公园、体育设施、绿地暴露、热暴露、空间公平、城市健康、GIS/遥感、文献计量、系统综述、scoping review、机器学习、科学可视化与 SCI 论文写作。

它不是“自动生成论文”的快捷方式，而是一个 **可复用、可审计、可进化的科研工作台**：帮助研究者把选题、检索、阅读、编码、分析、图表、写作、审稿回复和政策议程组织成稳定流程。

当前版本把 `auto-sci-research` 升级为完整科研管线总控：从选题、文献检索、数据下载、代码处理、统计/机器学习分析、论文级图件、初稿写作、投稿排版到审稿回复，都有对应子 skill 和子智能体组合。`urban-exposure-review-radar-workflow` 继续负责城市暴露、体育地理、热-绿复合暴露、公共健康数据库连接和高水平综述/前沿雷达路线。

---

## ✨ 一句话定位

如果你的研究问题长这样：

- 体育公园 / 体育设施是否公平可达？
- 绿地暴露、热暴露与身体活动或城市健康之间有什么机制？
- 城市公园、口袋公园、蓝绿空间如何影响健康与空间正义？
- 文献计量结果如何从“关键词聚类”升级为“批判性框架 + 政策议程”？
- 面向 Cities / SCS / UFUG / Environment International 等期刊，论文该怎么定位、分析和表达？

那么 `Auto-sci-research` 的目标就是把这些问题拆解成可执行的 Codex workflow。

核心链路：

```text
sources
-> structured memory
-> idea and method design
-> literature review / bibliometrics / coding
-> GIS / exposure / data / ML analysis
-> manuscript / figures / tables / policy agenda
-> reviewer-risk audit / rebuttal
-> evolution archive
```

---

## 🧭 借鉴了什么

本主页结构参考了三个优秀 skill 项目的公开呈现方式，但内容是针对地理学 + 体育学研究重新设计的：

- [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills)：清晰的功能特性、风险提示、快速开始和命令参考。
- [BoHeFan/academic-paper-writer-pro-2](https://github.com/BoHeFan/academic-paper-writer-pro-2)：学术写作与排版流程的场景化表达。
- [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills)：Codex 优先的安装说明、Skill index、What it does / Key rules / Reference files 结构。

本仓库不会复制第三方项目代码或大段文本，只迁移其“好用的组织逻辑”。

---

## 🚀 Codex 部署

### 方式 1：一键安装全部 skills

```powershell
git clone https://github.com/Lzy599775/agent-auto-sci-skills.git
cd agent-auto-sci-skills
.\scripts\install.ps1
```

默认安装到：

```text
$env:USERPROFILE\.codex\skills
```

安装后重启 Codex，新的 skills 会出现在可用 skill 列表中。

### 方式 2：安装到自定义目录

```powershell
.\scripts\install.ps1 -Target "$env:USERPROFILE\.agents\skills"
```

### 方式 3：手动复制

如果不想运行脚本，可以把 `skills/` 下需要的 skill 文件夹复制到 Codex 的 skills 目录。建议复制完整文件夹，而不是只复制 `SKILL.md`，因为很多 skill 依赖 `references/`、`scripts/` 和 `agents/openai.yaml`。

---

## 🧩 Skill Index

| Skill | 状态 | 适用任务 | 典型触发方式 |
|---|---:|---|---|
| `auto-sci-research` / legacy `agent-auto-sci` | Stable | 总控、路由、长期记忆、进化档案 | “使用 Auto-sci-research 规划这个科研任务” |
| `agent-auto-sci-automation` | Stable | 自动科研、source manifest、checkpoint、API 安全 | “建立文献项目的自动化流程” |
| `agent-auto-sci-methodology` | Stable | 研究问题、机制框架、证据分级、偏倚审计 | “把选题改成可检验研究问题” |
| `agent-auto-sci-geospatial` | Stable | GIS、遥感、可达性、绿地/热暴露、空间公平 | “检查我的空间分析流程” |
| `agent-auto-sci-data-viz` | Stable | EDA、统计分析、论文图表、文献计量图 | “设计主图、补充图和 caption” |
| `agent-auto-sci-ai-ml` | Stable | 机器学习、SHAP/XAI、泄露检查、空间验证 | “检查模型验证和解释边界” |
| `agent-auto-sci-scicomm` | Stable | SCI 写作、图文叙事、投稿、审稿回复 | “重构论文 argument 和回复审稿人” |
| `urban-exposure-review-radar-workflow` | Stable | 综述类型判别、文献计量+批判性综述、系统/范围综述、遥感前沿雷达、CV-to-RS、医学数据库连接 | “先判断这篇综述/雷达/实证设计该走什么路线” |
| `sport-geography-review-bibliometric` | Stable | 系统综述、scoping review、文献计量、批判性编码 | “设计综述 + 文献计量 + 政策议程” |
| `sport-geography-sci-writing` | Stable | 体育地理实证论文、目标期刊适配、讨论写作 | “把可达性/暴露结果写成 SCI 论文” |

完整模块关系见 [docs/skill-map.md](docs/skill-map.md)。

---

## 🧠 每个子 skill 做什么

### 1. `auto-sci-research` / `agent-auto-sci`

**What it does**
总领型科研 Agent。它不替代子 skill，而是先判断任务类型，再把任务路由给文献、方法、空间、数据、模型或写作模块。

**Key rules**

- 不把科研任务当成一次性回答，要保留可复用知识。
- 外部项目只能转化为本地 workflow，不能盲目整包复制。
- 涉及重大 skill 变动时，需要更新进化记录。

**Typical output**

- 任务路线图；
- 子 skill 调用顺序；
- 需要读取的参考文件；
- 质量检查点和下一步动作。

### 2. `agent-auto-sci-automation`

**What it does**  
把科研自动化拆成安全、可恢复、可审计的流程，适合长期文献库、自动阅读、知识库、checkpoint 和失败复盘。

**Key rules**

- 密钥、私有 PDF、付费数据库导出和未发表论文不能进入公开仓库。
- 自动化流程必须有 source manifest、状态记录和失败恢复点。
- 复杂任务先 checkpoint，再运行长流程。

**Typical output**

- source manifest；
- checkpoint 表；
- 失败日志模板；
- API 配置和安全边界。

### 3. `agent-auto-sci-methodology`

**What it does**  
把宽泛选题转成研究问题、机制路径、假设矩阵、证据分级和偏倚审计。

**Key rules**

- 区分相关、机制和因果主张。
- 横断面或观察性研究不能写成强因果。
- 空间公平与环境正义需要明确受影响人群、空间机制和政策工具。

**Typical output**

- research question matrix；
- mechanism map；
- bias audit；
- evidence grading；
- limitations and policy boundary。

### 4. `agent-auto-sci-geospatial`

**What it does**  
处理 GIS、遥感、可达性、暴露评估、空间公平和地图合规。

**Key rules**

- 先审计 CRS、空间单位、尺度、边界和网络假设。
- 暴露指标要说明时间、空间、强度和人群权重。
- 地图必须服务论证，不能只做装饰。

**Typical output**

- CRS / geometry audit；
- accessibility workflow；
- NDVI / LST / LCZ exposure plan；
- spatial equity metrics；
- publication map checklist。

### 5. `agent-auto-sci-data-viz`

**What it does**  
把 EDA、统计分析、文献计量图、论文图表和 policy matrix 组织成支撑论文 claim 的视觉证据。

**Key rules**

- 每张图必须回答一个问题或支撑一个 claim。
- caption 要说明发现，而不仅描述图里有什么。
- 文献计量图不能停留在“漂亮网络”，要连接主题演化、证据缺口和政策意义。

**Typical output**

- figure plan；
- main/supplementary figure split；
- table shells；
- caption drafts；
- policy matrix。

### 6. `agent-auto-sci-ai-ml`

**What it does**  
服务于地理学和体育学研究中的机器学习、SHAP/XAI、模型比较、泄露检查和可复现性。

**Key rules**

- baseline 先于复杂模型。
- 空间/时间切分优先于随机切分。
- SHAP 和特征重要性不是直接因果证据。

**Typical output**

- modeling plan；
- feature/label audit；
- validation split；
- leakage checklist；
- SHAP interpretation boundary。

### 7. `agent-auto-sci-scicomm`

**What it does**  
用于 SCI 论文结构、段落功能、图文叙事、投稿信、审稿回复、PPT 和海报。

**Key rules**

- 写作必须围绕 claim-evidence map。
- 不为了语言漂亮而扩张证据。
- 审稿回复要把每条意见映射到行动、证据和修改位置。

**Typical output**

- manuscript outline；
- claim-evidence map；
- reviewer-risk scan；
- cover letter；
- response-to-reviewers。

### 8. `urban-exposure-review-radar-workflow`

**What it does**

城市暴露、体育地理、遥感热环境、绿色暴露、体育设施可达性与公共健康连接的高级综述/前沿雷达工作流。它不是单一综述模板，而是一个 **domain router + evidence gate + research pipeline adapter**：先判断任务应该走 narrative review、systematic review、scoping review、bibliometric + critical review、frontier radar 还是 review-informed empirical design，再把检索、筛选、提取、编码、图表、写作、审稿和期刊门控组织成稳定流程。

新版已封装独立子 skill：`subskills/academic-research-suite`。该子 skill 来自 `Imbad0202/academic-research-skills-codex` v0.1.11，是 `Imbad0202/academic-research-skills` 的 Codex 原生分发版。它负责通用科研生产链条：深度研究、论文写作、同行评审模拟、完整 research-to-paper pipeline、实验规划、引用核查和完整性验证。父 skill 仍保留城市暴露和体育地理领域判断权，避免 ARS 的通用写作流程覆盖 exposure validity、accessibility/use 区分、因果语言和正式语料库边界。

**Internal architecture**

```text
urban-exposure-review-radar-workflow
├─ parent domain router
│  ├─ review route decision
│  ├─ journal evidence gate
│  ├─ formal corpus vs frontier radar handoff
│  ├─ exposure/accessibility/use boundary
│  └─ M1-M9 urban exposure modules
└─ subskills/academic-research-suite
   ├─ deep-research
   ├─ academic-paper
   ├─ academic-paper-reviewer
   ├─ academic-pipeline
   └─ experiment-agent
```

**Key rules**

- 正式综述语料库和 arXiv/GitHub/会议页面等前沿雷达候选必须分开。
- 前沿热点不能自动变成系统综述证据，除非通过同一纳入标准。
- 目标期刊路线必须绑定证据门槛：Cities/SCS 强调城市治理与规划机制，EI/Health & Place 强调暴露-健康证据与混杂控制。
- ARS 子 skill 只能在需要写作、审稿、引用核查、完整科研管线或实验规划时调用；默认只读取 ARS router 和一个必要的 `WORKFLOW.md`。
- 绿色暴露、热暴露、公园/设施可达性、设施质量、实际使用和健康收益不能互相替代。
- 横截面、生态关联或空间描述性结果不能写成个体层面的强因果结论。

**M1-M9 direction modules**

| Module | Purpose |
|---|---|
| M1 | 文献计量 + 批判性综述：把 CiteSpace/VOSviewer/bibliometrix 从描述性图谱升级为机制框架和政策议程。 |
| M2 | 系统综述：PRISMA、PEO/PICOS、筛选记录、提取字段、偏倚风险和证据综合。 |
| M3 | 范围综述：概念边界、研究版图、方法谱系、证据地图和未来议程。 |
| M4 | 绿色暴露 / 体育公园暴露：暴露窗口、活动空间、服务效用、人群异质性。 |
| M5 | 公园 / 体育设施可达性：网络可达性、2SFCA、服务区、公平性和机会结构。 |
| M6 | 遥感热暴露：LST、LCZ、传感器、尺度效应、验证数据和不确定性。 |
| M7 | 热-绿复合暴露：绿地降温、复合风险、适应性规划和公平影响。 |
| M8 | 城市暴露 + 公共健康数据库：空间连接、暴露窗口、混杂控制、隐私伦理和分层分析。 |
| M9 | Geospatial AI / CV-to-RS 雷达：arXiv、OpenReview、CVF、GitHub、Hugging Face 和遥感迁移潜力。 |

**ARS subskill workflows**

| Sub-workflow | What it adds |
|---|---|
| `deep-research` | 研究问题收敛、文献检索、事实核查、source verification、meta-analysis 预判断。 |
| `academic-paper` | 论文大纲、摘要、文献综述、方法叙述、讨论、修订、格式转换和 AI disclosure。 |
| `academic-paper-reviewer` | EIC 初筛、领域审查、方法审查、反方审查、审稿意见整合和修改后复审。 |
| `academic-pipeline` | 从选题到终稿的完整 research-to-paper 管线，包含 integrity gate 和 claim-reference alignment audit。 |
| `experiment-agent` | 代码实验、人群研究方案、统计解释、复现验证和实验结果回写论文。 |

**Typical output**

- route decision table；
- formal corpus / radar candidate handoff；
- WoS/Scopus/PubMed/SPORTDiscus/OpenAlex 检索策略；
- 遥感/Geospatial AI 前沿雷达；
- 绿色暴露、热暴露、体育设施可达性、医学数据库连接的提取与编码框架；
- journal evidence gate；
- ARS-backed paper pipeline / reviewer-risk audit / citation check；
- project scaffold。

**Quality status**

- Darwin 9 维评分：86.4 / 100。
- 已通过 JSON 解析、路径完整性、脚手架创建、密钥模式扫描、`.git` 排除和 dry-run prompt 验证。
- 详细记录见 `skills/urban-exposure-review-radar-workflow/references/darwin_ars_subskill_evaluation.md`。
- 上游 ARS 许可证为 CC BY-NC 4.0；复制和二次封装必须保留署名、许可证和非商业限制。

### 9. `sport-geography-review-bibliometric`

**What it does**  
体育地理综述与文献计量专用 skill。适合 systematic review、scoping review、bibliometric analysis，以及“综述 + 批判性框架 + 政策议程”路线。

**Key rules**

- 检索式必须能被复现。
- PRISMA、纳入排除、编码表和图表必须互相支撑。
- 高水平综述要提出机制框架和政策议程，而不是只报告关键词。

**Typical output**

- search strategy；
- PRISMA protocol；
- screening criteria；
- coding framework；
- CiteSpace / VOSviewer / R bibliometrix figure plan；
- policy agenda。

### 10. `sport-geography-sci-writing`

**What it does**  
体育地理实证 SCI 写作 skill。适合体育设施可达性、体育公园暴露、绿地/热暴露、空间公平、城市健康和身体活动机制研究。

**Key rules**

- Introduction 要从城市健康问题进入，而不是从技术指标进入。
- Methods 要写清楚空间单位、暴露窗口、可达性假设和数据限制。
- Discussion 要连接机制、治理、规划和公平，不只复述结果。

**Typical output**

- target-journal positioning；
- introduction gap chain；
- methods structure；
- results narrative；
- figure/table plan；
- discussion and policy implications。

---

## 🧪 全流程写作 Pipeline

### 0. 从选题到完稿总流程

```text
auto-sci-research
-> agent-auto-sci-methodology
-> sport-geography-review-bibliometric / urban-exposure-review-radar-workflow
-> agent-auto-sci-automation
-> agent-auto-sci-geospatial
-> agent-auto-sci-ai-ml / agent-auto-sci-data-viz
-> sport-geography-sci-writing
-> agent-auto-sci-scicomm
-> reviewer-risk scan / rebuttal / evolution archive
```

阶段产物：

1. 选题矩阵、SMART 研究问题、创新性和可行性评估；
2. 中英文关键词体系、检索式、筛选标准、文献矩阵和 evidence map；
3. 数据源清单、下载/清洗记录、空间单位、变量和指标定义；
4. 可复现代码或 notebook、统计/机器学习方案、稳健性和泄露检查；
5. 主图/补充图/表格/caption 计划，确保每张图服务一个 claim；
6. 标题、摘要、引言、方法、结果、讨论和结论初稿；
7. 参考文献、格式、投稿信、审稿意见拆解和逐条回复。

详细执行说明见：

- `skills/auto-sci-research/references/08_full_research_to_manuscript_pipeline.md`
- `skills/auto-sci-research/references/09_subagent_composition_matrix.md`
- `skills/auto-sci-research/references/10_prompt_workflow_from_academic_pdf.md`
- `skills/auto-sci-research/references/11_sportpark_skill_integration_notes.md`

### A. 综述 / 文献计量 / 政策议程

```text
auto-sci-research
-> urban-exposure-review-radar-workflow
-> sport-geography-review-bibliometric
-> agent-auto-sci-methodology
-> agent-auto-sci-data-viz
-> agent-auto-sci-scicomm
```

适合：

- sport park exposure；
- sport facility accessibility；
- green exposure / green equity；
- heat exposure；
- urban health；
- active-living infrastructure；
- park equity and environmental justice。

建议产物：

1. 检索式与数据库策略；
2. PRISMA 流程和纳入排除标准；
3. 编码表和 evidence map；
4. 文献计量图谱和主题演化；
5. 批判性分析框架；
6. 面向城市规划和公共健康的政策议程；
7. 目标期刊版 manuscript outline。

### A2. 城市暴露 / 遥感前沿雷达 / 医学数据库连接

```text
auto-sci-research
-> urban-exposure-review-radar-workflow
-> agent-auto-sci-geospatial
-> agent-auto-sci-methodology
-> agent-auto-sci-scicomm
```

适合：

- 城市热暴露、LCZ、UHI、LST 和人体热风险；
- 绿地暴露、街景绿量、蓝绿空间和可见绿量；
- Geospatial AI、遥感基础模型、开放词汇分割、VLM、CV-to-RS 迁移；
- 城市暴露与公共医学数据库、队列、医院、医保、死亡登记或健康调查连接；
- 不同年龄、性别、慢病和社会经济群体的健康影响研究设计。

建议产物：

1. 路线判别：系统综述、范围综述、计量综述、叙事综述、前沿雷达或实证设计；
2. formal corpus 与 radar candidates 交接表；
3. 遥感/AI 候选论文项目评分表；
4. 暴露窗口、空间连接、健康结局、混杂控制和隐私伦理检查；
5. 面向 Cities / SCS / EI / Health & Place / UFUG / Nature-family 的证据门槛。

### B. 体育设施可达性 / 暴露 / 空间公平实证论文

```text
auto-sci-research
-> sport-geography-sci-writing
-> agent-auto-sci-geospatial
-> agent-auto-sci-data-viz
-> agent-auto-sci-methodology
```

建议产物：

1. 研究问题与机制路径；
2. 数据源、空间单位、暴露窗口和可达性假设；
3. GIS / 遥感 / 网络分析 workflow；
4. 统计或机器学习方案；
5. 主图、表格和补充材料；
6. 讨论、政策启示和局限；
7. 投稿前 reviewer-risk scan。

### C. 机器学习 + 空间健康解释

```text
auto-sci-research
-> agent-auto-sci-ai-ml
-> agent-auto-sci-geospatial
-> agent-auto-sci-methodology
-> agent-auto-sci-scicomm
```

建议产物：

1. baseline 与模型比较；
2. 空间/时间切分；
3. 泄露检查；
4. SHAP/XAI 解释边界；
5. 结果写法和政策外推限制。

---

## 💬 Codex 使用示例

```text
使用 Auto-sci-research 和 sport-geography-review-bibliometric，
为“体育公园暴露、绿色公平与城市健康”的系统综述设计完整路线。
要求包括检索式、PRISMA、纳入排除标准、编码表、文献计量图表、批判性框架和政策议程。
目标期刊偏向 Cities / Sustainable Cities and Society。
```

```text
使用 sport-geography-sci-writing 和 agent-auto-sci-geospatial，
检查我的体育设施可达性实证论文。
重点看空间单位、网络可达性、暴露测度、地图合规、空间公平指标和审稿风险。
```

```text
使用 agent-auto-sci-data-viz，
把我的 CiteSpace、VOSviewer 和 R bibliometrix 结果整理成论文图表计划。
每张图都要说明支撑哪个 claim，以及适合放主文还是补充材料。
```

```text
使用 agent-auto-sci-scicomm，
基于已有结果重构论文 Introduction 和 Discussion。
要求输出 claim-evidence map、段落功能、目标期刊风险和需要补强的证据。
```

---

## 📁 项目结构

```text
agent-auto-sci-skills/
├─ skills/                 # 10 个可安装的 Codex skills
├─ docs/                   # skill map、使用场景、第三方参考和发布说明
├─ scripts/                # 安装脚本和公开安全扫描脚本
├─ site/                   # GitHub Pages 展示页和子 skill 详情页
├─ .github/workflows/      # 校验与 Pages 发布
├─ README.md               # 中文主页
└─ README_EN.md            # English README
```

---

## 🔒 公开安全原则

本仓库不应包含：

- API key、token、cookie、password；
- 私有 PDF 全文；
- WoS / Scopus 等付费数据库原始导出；
- 未发表论文正文；
- 审稿意见原文；
- 私人文献库、私人数据集或个人本地绝对路径；
- 无授权的第三方代码或大段文本。

发布前运行：

```powershell
.\scripts\scan_public_safety.ps1
```

---

## 🤝 Contribution

欢迎 issue 和 PR。建议按下面格式提交新 skill 或改进建议：

```text
1. 这个 skill 解决什么科研任务？
2. 适用学科、数据类型或期刊场景是什么？
3. 需要哪些 references、scripts 或 assets？
4. 触发关键词是什么？
5. 如何验证它真的有用？
6. 是否包含密钥、私有数据、版权风险或不可公开材料？
```

---

## License

MIT License。若未来引入第三方源代码、模板或素材，需要逐一核对许可证并保留 attribution。
