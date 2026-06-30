# Urban Exposure Review Radar Workflow

面向体育地理、城市健康、绿色暴露、公园可达性、体育设施暴露、热环境遥感与文献计量综述的 Codex skill 包。

这个仓库不是一个普通提示词集合，而是一套可以长期维护的科研工作流系统。它的定位是把“选题判断、综述设计、前沿扫描、证据编码、图表规划、论文写作、审稿回复和引用核查”放进同一条可验证的研究管线中，同时保持城市暴露与体育地理研究的领域边界。

## 核心定位

本 skill 解决四类高频科研问题：

1. 研究方向还不够聚焦，需要把绿色暴露、热暴露、体育公园、公园可达性、空间公平、城市健康等宽泛主题收敛成可投稿的研究问题。
2. 已经确定要做综述，但需要判断应该走系统综述、范围综述、文献计量 + 批判性综述、叙述综述还是前沿雷达。
3. 已经有文献或数据，需要建立提取表、编码框架、证据图谱、claim-evidence map、图件设计和期刊证据门控。
4. 已经进入论文写作、修改、引用核查、同行评审模拟或审稿回复阶段，需要更完整的 Academic Research Suite 管线支持。

## 设计原则

- 领域先行：先判断暴露、可达性、可用性、质量与实际使用是否被混淆，再决定技术路线。
- 证据优先：系统综述、范围综述、文献计量和前沿雷达使用不同证据标准，不把新论文/新项目直接混入正式语料库。
- 期刊门控：SCS、Cities、Health & Place、Environment International、Environmental Research、Landscape and Urban Planning、Urban Forestry & Urban Greening、Nature-family urban/health outlets 使用不同贡献边界。
- 渐进加载：父 skill 负责领域判断，子 skill 负责通用科研写作管线；默认只加载当前任务需要的一个 workflow。
- 可验证交付：保留测试 prompt、Darwin 评分、路径完整性检查、密钥扫描和脚手架测试记录。

## 目录结构

```text
urban-exposure-review-radar-workflow/
  SKILL.md
  README.md
  NOTICE.md
  test-prompts.json
  results.tsv
  scripts/
    create_review_radar_scaffold.py
  references/
    workflow_playbook.md
    darwin_quality_gate.md
    darwin_ars_subskill_evaluation.md
  subskills/
    academic-research-suite/
      SKILL.md
      manifest.json
      LICENSE
      NOTICE.md
      agents/
      ars/
      codex/
```

## 父 Skill: Urban Exposure Review Radar Workflow

父 skill 是本包的领域控制层。它处理体育地理、城市健康和遥感交叉研究中最容易跑偏的判断：

- 研究类型：叙述综述、系统综述、范围综述、文献计量 + 批判性综述、前沿雷达、实证研究设计或混合路径。
- 贡献边界：研究是服务城市治理、空间公平、健康机制、景观规划，还是方法创新。
- 证据边界：正式综述语料库与前沿雷达候选必须分开。
- 暴露有效性：绿色暴露、热暴露、可达性、可用性、设施质量和实际使用不能互相替代。
- 因果语言：横截面或生态关联不能写成个体因果结论。
- 图表门控：每一张图都必须回答一个研究问题，不能只展示软件默认输出。

### M1-M9 方向模块

| 模块 | 主题 | 适用任务 |
|---|---|---|
| M1 | 文献计量 + 批判性综述 | CiteSpace、VOSviewer、bibliometrix、知识图谱、主题演化和政策议程。 |
| M2 | 系统综述 | PRISMA、PEO/PICOS、筛选记录、偏倚风险、证据综合和因果边界。 |
| M3 | 范围综述 | 研究范围、概念分类、方法谱系、证据地图和未来研究议程。 |
| M4 | 绿色暴露 / 体育公园暴露 | NDVI、公园接触、体育公园服务、活动空间、健康与公平机制。 |
| M5 | 公园 / 体育设施可达性 | 2SFCA、网络距离、服务区、公平性、设施质量、机会结构。 |
| M6 | 遥感热暴露 | LST、LCZ、热环境、尺度效应、传感器、验证与不确定性。 |
| M7 | 热-绿复合暴露 | 绿地降温、热风险缓解、复合暴露路径和适应性规划。 |
| M8 | 城市暴露 + 公共健康数据库 | 空间连接、暴露窗口、人群分层、混杂控制、伦理与隐私。 |
| M9 | Geospatial AI / CV-to-RS 前沿雷达 | arXiv、CVF、OpenReview、GitHub、Hugging Face、遥感迁移潜力。 |

## 子 Skill: Academic Research Suite

路径：`subskills/academic-research-suite/SKILL.md`

这是本包封装的独立子 skill，来源于 `Imbad0202/academic-research-skills-codex` v0.1.15。它是 `Imbad0202/academic-research-skills` 的 Codex 原生分发版，已保留 manifest、license、NOTICE 和必要的上游追踪文档。

它的作用不是替代父 skill，而是在研究进入“通用科研生产链条”后接管更复杂的写作、评审、引用和完整管线任务。父 skill 仍然负责城市暴露、体育地理和健康地理的领域判断。

### 子 Skill 入口规则

1. 先用父 skill 判断研究类型、期刊路线、证据门槛和风险边界。
2. 只有当任务进入深度研究、论文写作、审稿、引用核查或完整科研管线时，才读取 `subskills/academic-research-suite/SKILL.md`。
3. 再根据 ARS router 只加载一个必要的 `WORKFLOW.md`。
4. 不一次性加载整个 ARS 套件。
5. 父 skill 的领域黑名单持续有效：不混淆 exposure/accessibility/use，不夸大因果，不把 radar candidate 当正式 corpus。

## ARS 内部 Workflow 说明

虽然 Codex 只注册一个 `academic-research-suite` 子 skill，但它内部包含五条主要科研 workflow。每条 workflow 都有自己的角色提示、参考材料和交付边界。

### 1. Deep Research

路径：`subskills/academic-research-suite/ars/deep-research/WORKFLOW.md`

适用于研究问题还需要收敛、需要系统检索、需要文献综述、需要事实核查或需要 meta-analysis 思路判断的阶段。

典型任务：

- 从“体育公园可达性与健康”这类宽题收敛成可回答的 RQ。
- 设计系统综述、范围综述或文献综述检索策略。
- 建立源验证、时间线提取、风险偏倚、证据综合和研究架构。
- 对关键文献、指标、数据集和引用做事实核查。

核心价值：

- 让早期选题不直接跳到写作，而是先确认问题、对象、机制、证据和方法。
- 适合与父 skill 的 M1-M3、M8-M9 联合使用。

### 2. Academic Paper

路径：`subskills/academic-research-suite/ars/academic-paper/WORKFLOW.md`

适用于论文大纲、摘要、引言、文献综述、方法叙述、结果解释、讨论、修订和格式转换。

典型任务：

- 将文献提取表转成论文结构。
- 写 abstract-only、outline-only、literature review 或 full draft。
- 根据目标期刊调整论证层次与段落功能。
- 做 citation-check、format-convert、AI disclosure 或 revision-coach。

核心价值：

- 把“材料堆积”转化为可投稿的论证结构。
- 与父 skill 的 journal evidence gate 联合使用时，可以避免把描述性地图写成机制贡献。

### 3. Academic Paper Reviewer

路径：`subskills/academic-research-suite/ars/academic-paper-reviewer/WORKFLOW.md`

适用于模拟同行评审、编辑初筛、方法审查、领域审查、反方审查和修改后复审。

典型任务：

- 让 EIC 视角判断是否 desk reject。
- 让 methodology reviewer 检查识别策略、模型、混杂、尺度和可重复性。
- 让 domain reviewer 判断领域贡献是否成立。
- 生成 revision roadmap 和 rebuttal 重点。

核心价值：

- 对体育地理和城市健康论文尤其有用，因为这类文章常见风险是概念贡献不足、暴露测量不稳、空间尺度解释过度和健康因果语言过强。

### 4. Academic Pipeline

路径：`subskills/academic-research-suite/ars/academic-pipeline/WORKFLOW.md`

适用于从研究设计到最终稿的完整管线。它将研究规划、写作、审查、修订、完整性验证和最终交付串联起来。

典型任务：

- 从选题进入完整 paper pipeline。
- 维护 Material Passport 风格的来源、证据和改动记录。
- 在关键阶段运行 integrity verification。
- 做 claim-reference alignment audit。

核心价值：

- 适合大型论文、基金选题、综述论文和需要多轮修改的投稿项目。
- 能把父 skill 的 evidence map、claim-evidence map 和 journal gate 纳入完整写作流程。

### 5. Experiment Agent

路径：`subskills/academic-research-suite/ars/experiment-agent/WORKFLOW.md`

适用于代码实验、人群研究方案、统计解释、实验记录和复现验证。

典型任务：

- 设计可复现的数据处理或模型实验。
- 检查统计推断、效应解释和常见 fallacy。
- 管理 human study protocol、伦理检查和数据处理边界。
- 将实验结果带回论文写作阶段。

核心价值：

- 对遥感暴露、可达性模型、城市健康空间连接和分层分析很有帮助。
- 能避免“方法可跑但证据不稳”的论文风险。

## 测试与质量门控

本包已经通过以下本地检查：

- `test-prompts.json` 解析通过。
- `create_review_radar_scaffold.py` 脚手架测试通过，临时目录创建 16 个项目产物后清理。
- ARS router、manifest、license、五个 `WORKFLOW.md`、关键 agent、commands、shared schemas 和 Codex runtime manifest 均存在。
- vendored ARS 目录未包含 `.git`。
- 常见 API token 模式扫描未命中。
- Darwin 9 维评分为 86.4 / 100，详见 `references/darwin_ars_subskill_evaluation.md`。

## 使用示例

### 文献计量 + 批判性综述

```text
为 SCS/Cities 设计体育公园、绿地可达性与城市健康的文献计量 + 批判性综述路线。
```

预期行为：先走父 skill 的 M1，稳定 WoS/Scopus 检索范围，再设计知识图谱、手工编码、政策机制和投稿门控。

### 系统综述

```text
设计绿色暴露、热暴露与心理健康结局的系统综述方案。
```

预期行为：使用 PEO/PICOS、筛选记录、提取字段、偏倚风险和因果语言边界，不把前沿雷达候选混入正式 corpus。

### 前沿雷达

```text
做城市热暴露、LCZ、绿地暴露与 Geospatial AI 的月度前沿雷达。
```

预期行为：扫描当前来源，标注日期和来源，把项目分为 `radar-candidate`、`background-method` 或 `excluded`。

### 完整论文管线

```text
用 ARS 帮我把体育公园可达性与城市健康这篇论文从选题、文献综述、写作到审稿回复做成完整流程。
```

预期行为：先用父 skill 锁定研究定位和证据门控，再进入 `academic-research-suite` 子 skill 的 pipeline。

## 许可证与来源

本包包含 vendored upstream content：

- `subskills/academic-research-suite` 来自 `Imbad0202/academic-research-skills-codex`。
- 上游 ARS 内容记录在 `subskills/academic-research-suite/manifest.json`。
- ARS 内容遵循 CC BY-NC 4.0，详见 `subskills/academic-research-suite/LICENSE`。

复制、分享或二次封装时必须保留署名、许可证文本、非商业限制和改动说明。
