# Prompt Library for Sport Geography Review and Bibliometric Writing

Use this file when the user asks for prompts, prompt chains, manuscript drafting prompts, review prompts, bibliometric prompts, critical coding prompts, or policy agenda prompts for geography + sport science review work.

This library is adapted for topics such as sports parks, sports facilities, active recreation infrastructure, parks, urban green space, green exposure, heat exposure, accessibility, equity, environmental justice, physical activity, and urban health.

## 1. Prompt Design Rules

Every useful prompt should include nine parts:

1. Role: specify the expert lens, such as urban health geographer, systematic review methodologist, bibliometric analyst, planner, or reviewer.
2. Task: state one concrete task, not a vague request to "write something".
3. Context: provide topic, target journal, review type, database, corpus size, and current manuscript stage.
4. Evidence: list the input evidence the model may use; forbid invented citations, numbers, or claims.
5. Method: state the framework, such as PRISMA 2020, PRISMA-ScR, bibliometrix, VOSviewer, CiteSpace, PROGRESS-Plus, environmental justice, or exposure pathway.
6. Output: require a table, checklist, paragraph, outline, coding scheme, RQ set, or reviewer report.
7. Constraints: define length, language, tone, citation rules, claim strength, and non-goals.
8. Self-check: ask for risks, missing evidence, overclaiming, or journal-fit problems.
9. Next step: ask what evidence or analysis is needed before writing the next section.

Default reusable prompt skeleton:

```text
请你作为【角色】，围绕【主题/稿件目标】完成【具体任务】。

背景与目标：
- 研究对象：【体育公园/体育设施/城市公园/绿地/口袋公园/热暴露/绿色暴露等】
- 核心关系：【暴露/可达性/使用/身体活动/健康/公平/治理】
- 目标期刊：【Cities/Sustainable Cities and Society/LUP/UFUG/Environment International/其他】
- 文章类型：【系统综述/scoping review/文献计量/混合综述/批判性综述】
- 可用证据：【检索式/文献表/全文摘录/图表结果/编码表】

要求：
1. 只基于我提供的证据和可核验的常识进行分析，不编造文献、DOI、数据或结论。
2. 区分“已有证据支持”“合理推断”“需要进一步验证”。
3. 输出应服务于高水平期刊的论证链，而不是资料罗列。
4. 若证据不足，请明确指出缺口，并给出下一步最小补证方案。

输出格式：
【指定表格/分节提纲/正文段落/审稿风险清单/编码框架】
```

## 2. Input Variable Pack

Before using any prompt, fill this pack as much as possible.

```text
主题暂定：
目标期刊：
文章路线：
研究对象：
空间尺度：
人群或公平维度：
暴露/可达性指标：
健康或行为结果：
数据库：
检索日期：
纳入文献数量：
主要分析工具：
已有图表：
已有编码字段：
最担心的审稿风险：
希望输出语言：
```

## 3. Topic Positioning Prompts

### 3.1 Manuscript Route Selection

```text
请你作为 Cities 和 Sustainable Cities and Society 的综述稿件顾问，基于以下研究想法判断最合适的论文路线：
【粘贴研究想法、已有文献数据、目标期刊】

请比较四种路线：
1. 系统综述；
2. scoping review；
3. 文献计量分析；
4. 文献计量 + 批判性编码 + 政策议程的混合综述。

每种路线请输出：
- 适合回答的研究问题；
- 对数据和全文阅读的要求；
- 对 Cities/SCS 的潜在吸引力；
- 主要审稿风险；
- 最小可发表版本；
- 如果要冲击更高水平期刊，还需要补强什么。

最后推荐一条主路线和一条备选路线，并说明不建议采用的路线。
```

### 3.2 Contribution Diagnosis

```text
请审查以下综述选题是否具备高水平期刊贡献：
【研究主题/摘要/大纲】

请从五个层面诊断：
1. 概念贡献：是否重新界定了体育设施、绿色暴露、可达性、使用和健康之间的关系；
2. 方法贡献：是否超越普通 VOSviewer/CiteSpace 图谱；
3. 证据贡献：是否形成可复核的证据地图或编码结果；
4. 理论贡献：是否连接环境正义、活动空间、健康路径或空间治理；
5. 政策贡献：是否能转化为规划、投资、维护和治理建议。

输出一个表格：贡献类型、当前强度、证据基础、主要短板、补强动作、可写进论文的保守表述。
```

### 3.3 Journal Fit Prompt

```text
请作为目标期刊编辑，判断以下稿件是否适合【目标期刊】：
【题目、摘要、大纲、主要图表、研究问题】

请按以下维度打分并解释：
- 城市问题重要性；
- 空间/地理分析深度；
- 健康与公平议题的严谨性；
- 方法透明度；
- 图表的信息密度；
- 政策议程是否具体；
- 与该期刊近期综述/文献计量文章的匹配度。

最后输出：
1. 适合该期刊的定位句；
2. 最可能被编辑 desk reject 的原因；
3. 投稿前必须补强的 5 个点；
4. 若改投，推荐期刊层级和理由。
```

## 4. Research Question and Concept Boundary Prompts

### 4.1 RQ Builder

```text
请将【宽泛主题】改写为 4 个可由综述和文献计量共同回答的研究问题。

要求：
- RQ1 关注知识生产格局；
- RQ2 关注研究主题和方法演化；
- RQ3 关注暴露/可达性/使用/健康/公平之间的证据链；
- RQ4 关注规划治理和政策议程。

每个 RQ 请说明：
- 适合用哪类证据回答；
- 需要哪些图表；
- 需要哪些人工编码字段；
- 哪些结论不能仅靠文献计量得到。
```

### 4.2 Concept Boundary

```text
请为【体育公园/体育设施暴露/绿色暴露/公园可达性】建立概念边界。

请输出：
1. 核心概念定义；
2. 相邻概念及区别；
3. 不应混用的概念；
4. 检索时应纳入的同义词；
5. 检索时应排除的噪声词；
6. 在正文中建议采用的术语系统。

请特别区分：
- accessibility 与 exposure；
- availability 与 quality；
- objective exposure 与 perceived exposure；
- access 与 actual use；
- equality、equity、justice；
- sport facility、recreation facility、active living infrastructure、park amenity。
```

## 5. Search Strategy and PRISMA Prompts

### 5.1 Search Term Ontology

```text
请为以下主题生成可用于 Web of Science 和 Scopus 的检索词本体：
【主题】

请分为五组：
1. 对象词：sports park, sport facility, recreation facility, park, green space 等；
2. 暴露/可达性词：accessibility, exposure, availability, proximity, service area 等；
3. 公平/正义词：equity, inequality, environmental justice, deprivation, vulnerability 等；
4. 健康/活动词：physical activity, active living, health, wellbeing, heat stress 等；
5. 空间方法词：GIS, network analysis, remote sensing, activity space, spatial equity 等。

输出：
- 英文检索词表；
- 需要合并的同义词；
- 容易造成噪声的词；
- WoS TS 检索式草案；
- Scopus TITLE-ABS-KEY 检索式草案；
- 为什么该检索式既不过宽也不过窄。
```

### 5.2 PRISMA Protocol Draft

```text
请基于以下研究目标，为系统综述/文献计量混合研究撰写 PRISMA 风格方法方案：
【研究目标、数据库、时间范围、语言、文献类型、检索式】

必须包含：
- 数据库和检索日期；
- 完整检索式；
- 纳入标准；
- 排除标准；
- 去重策略；
- 标题摘要筛选规则；
- 全文筛选规则；
- 争议处理方式；
- 数据提取字段；
- 质量或偏倚评价是否需要；
- bibliometric 与 manual coding 的分工。

请输出为可直接放入方法部分的分节提纲，并附一个 PRISMA 流程图数字占位模板。
```

### 5.3 Screening Calibration

```text
请作为第二筛选者，基于以下纳排标准判断这些文献是否应纳入：
【纳排标准】
【题名+摘要+关键词列表】

请输出表格：
- 编号；
- 初步决定：纳入/排除/不确定；
- 决定理由；
- 触发的纳入标准；
- 触发的排除标准；
- 需要全文确认的信息；
- 是否可能属于边界文献。

注意：不要因为题名中出现 park/green/sport 就自动纳入，必须判断它是否回答本综述的研究问题。
```

## 6. Bibliometric Analysis Prompts

### 6.1 Bibliometric Analysis Plan

```text
请为以下文献库设计一套可用于 R bibliometrix、VOSviewer 和 CiteSpace 的文献计量分析方案：
【文献数量、数据库、导出字段、主题范围、目标期刊】

请输出：
1. performance analysis：年度发文、期刊、作者、机构、国家、引用；
2. science mapping：合作网络、共词网络、共被引、文献耦合；
3. temporal analysis：主题演化、突现词、时间线；
4. software division：哪些图用 bibliometrix，哪些图用 VOSviewer，哪些图用 CiteSpace；
5. 每张图回答的研究问题；
6. 审稿人可能质疑的地方；
7. 需要人工解释或编码补充的地方。
```

### 6.2 Keyword Cleaning and Thesaurus

```text
请根据以下关键词列表，为 VOSviewer/bibliometrix 构建关键词清洗方案：
【关键词频次表】

请输出三张表：
1. 同义词合并表：label、replace by、理由；
2. 删除词表：term、删除理由；
3. 保留但需解释的边界词：term、可能含义、是否需要人工复核。

请特别处理：
- urban green space / greenspace / green spaces；
- park / parks / urban park / public park；
- sport facility / sports facility / recreation facility；
- physical activity / exercise / active living；
- environmental justice / equity / inequality / deprivation；
- heat exposure / thermal comfort / urban heat island。

注意：不要为了美化网络图而过度合并概念。
```

### 6.3 Interpreting Bibliometric Maps

```text
请基于以下文献计量结果写一段高水平结果解释：
【图表结果、聚类标签、时间范围、关键词/文献/国家网络】

要求：
- 先描述可观察事实，再解释其学术含义；
- 区分结构性发现、时间演化和地理不均；
- 不要把软件聚类标签当作理论结论；
- 每个结论必须指向一个研究问题；
- 最后说明哪些问题需要人工编码进一步回答。

输出结构：
1. 主要发现；
2. 证据来自哪些图表；
3. 解释；
4. 局限；
5. 与下一节人工编码的过渡句。
```

## 7. Scoping Review and Systematic Review Prompts

### 7.1 Scoping Review Evidence Map

```text
请把以下纳入文献整理为 scoping review 证据地图：
【文献表】

编码维度必须包括：
- 地理区域；
- 城市类型；
- 空间尺度；
- 研究对象；
- 暴露或可达性指标；
- 数据源；
- 方法类型；
- 人群分组；
- 公平/正义维度；
- 身体活动或健康结果；
- 规划启示。

请输出：
1. 证据分布总览；
2. 高密度研究区域；
3. 低证据或空白区域；
4. 方法集中和方法缺口；
5. 对下一步系统综述或文献计量的建议。
```

### 7.2 Systematic Synthesis

```text
请对以下文献编码结果进行系统综述式综合，而不是逐篇总结：
【编码表或文献摘录】

请按主题综合：
1. 空间供给与可达性；
2. 绿色/热暴露测度；
3. 公平与环境正义；
4. 身体活动与健康路径；
5. 规划治理和政策工具。

每个主题请回答：
- 已有证据一致在哪里；
- 分歧在哪里；
- 分歧是否来自尺度、数据、指标或研究设计；
- 对体育公园/体育设施研究有什么启示；
- 哪些结论需要谨慎表述。
```

### 7.3 Evidence Strength Classification

```text
请基于以下证据摘要，对每条结论进行证据强度分级：
【结论列表 + 支撑文献】

分级：
- Strong：多地区、多方法、一致发现；
- Moderate：证据较多但存在尺度或方法差异；
- Limited：证据少或集中在少数地区；
- Mixed：结论方向不一致；
- Speculative：主要来自理论推断或间接证据。

输出表格：
结论、证据等级、支撑证据、反向证据、主要偏倚、适合写在正文的位置、建议表述强度。
```

## 8. Critical Coding Prompts

### 8.1 Coding Framework Builder

```text
请为“地理学 + 体育学”综述建立一套批判性人工编码框架。

研究主题：
【主题】

框架至少包含：
- facility/object：体育公园、运动场地、健身设施、绿道、公园、口袋公园等；
- exposure/access：距离、网络时间、面积、质量、眼动/街景绿视率、热暴露等；
- actual use：访问、停留、身体活动强度、运动类型；
- population：儿童、老年人、低收入群体、女性、残障群体、少数族裔等；
- justice：分配正义、程序正义、承认正义、能力正义；
- method：GIS、遥感、问卷、观察、GPS、社交媒体、机器学习、自然实验；
- scale：城市、社区、街区、活动空间、设施内部；
- outcome：身体活动、心理健康、热舒适、社会凝聚、环境质量；
- policy lever：规划供给、维护质量、交通连接、收费制度、参与治理、热风险管理。

请输出字段名、定义、编码值、判断规则、例子和常见误判。
```

### 8.2 Full-text Coding Assistant

```text
请读取以下论文摘录，并按既定编码框架提取信息：
【论文题名、摘要、方法、结果、讨论摘录】
【编码框架】

输出表格：
- DOI/题名；
- 研究对象；
- 地理位置；
- 空间尺度；
- 暴露/可达性指标；
- 数据源；
- 方法；
- 人群；
- 公平维度；
- 健康/活动结果；
- 主要发现；
- 政策启示；
- 证据强度；
- 需要人工复核的字段。

请不要根据常识补全论文没有报告的信息。未报告请写 NR。
```

### 8.3 Gap and Bias Audit

```text
请审计以下编码结果中的结构性偏差：
【编码结果表】

请检查：
- 是否过度集中于北美、欧洲、中国或高收入城市；
- 是否忽视全球南方、县域城市或中小城市；
- 是否只测供给而忽视使用；
- 是否只测数量而忽视质量；
- 是否只讨论分配正义而忽视程序正义和承认正义；
- 是否把可达性等同于健康收益；
- 是否缺少热暴露、季节性和时间维度；
- 是否缺少体育设施的具体类型差异。

输出：偏差类型、证据、影响、如何在讨论中处理、后续研究议程。
```

## 9. Figure and Table Prompts

### 9.1 Figure Planning

```text
请为这篇综述/文献计量论文规划一套面向【目标期刊】的图表系统：
【研究问题、数据、已有结果】

要求每张图都回答一个明确问题，避免装饰性图谱。

建议至少考虑：
1. PRISMA 流程图；
2. 年度发文与主题阶段图；
3. 关键词共现/主题演化图；
4. 国家或地区知识生产与合作图；
5. 批判性编码证据地图；
6. 暴露-使用-健康-公平机制框架；
7. 政策议程矩阵。

输出表格：图号、图名、核心问题、数据来源、制作工具、主要信息、正文放置位置、潜在审稿风险。
```

### 9.2 Table Design

```text
请为以下综述结果设计高信息密度表格：
【结果或编码字段】

请给出：
- 表题；
- 列名；
- 每列含义；
- 是否适合正文或补充材料；
- 如何减少表格过宽；
- 表注需要解释哪些缩写；
- 这张表对论证链的贡献。
```

## 10. Manuscript Section Prompts

### 10.1 Abstract

```text
请为【目标期刊】写一个综述/文献计量论文摘要。

输入：
【背景、研究空白、数据来源、文献数量、方法、关键发现、政策启示、局限】

结构要求：
1. 城市健康/可持续治理问题；
2. 现有研究空白；
3. 数据库、时间范围和方法；
4. 2-3 个实质性发现；
5. 理论或政策贡献；
6. 克制的边界说明。

禁止：
- 宣称首次，除非已有完整检索证明；
- 把可达性直接写成健康改善；
- 使用空泛词，如 significant implications 但不说明是什么。
```

### 10.2 Introduction

```text
请为以下主题设计引言四段式结构：
【主题、目标期刊、研究问题】

四段分别为：
1. 城市问题和公共健康/可持续压力；
2. 已有研究进展；
3. 关键不足：概念、方法、证据、政策转化；
4. 本文如何用系统综述/文献计量/批判性编码解决不足。

每段请输出：
- 中心句；
- 论证要点；
- 需要引用的文献类型；
- 不能过度声称的地方。
```

### 10.3 Methods

```text
请把以下检索和分析流程写成可复现的方法部分：
【数据库、检索式、筛选流程、纳入数量、软件、参数、编码框架】

必须说明：
- 为什么选择这些数据库；
- 为什么选择这些检索字段；
- 去重和筛选如何进行；
- bibliometric 软件版本和关键参数；
- 人工编码字段和一致性检查；
- 质量控制；
- 数据和代码可用性安排。

写作要求：客观、可复现、不提前报告结果。
```

### 10.4 Results

```text
请根据以下图表结果撰写 Results 段落：
【图表结果】

要求：
- 只报告发现，不展开价值判断；
- 每段对应一个研究问题；
- 先给总体趋势，再给关键比较；
- 指向图表编号；
- 对不稳定或弱证据结果保持克制。
```

### 10.5 Discussion and Policy Agenda

```text
请把以下结果转化为讨论和政策议程：
【主要发现、编码结果、图表、目标期刊】

讨论结构：
1. 回答研究问题；
2. 与既有综述或实证研究对话；
3. 解释为何出现这些模式；
4. 指出方法和证据短板；
5. 提出政策议程。

政策议程必须从“问题诊断”走向“治理动作”：
- 空间诊断；
- 目标人群识别；
- 设施供给和质量提升；
- 交通连接与活动空间；
- 热风险和绿色基础设施协同；
- 参与式治理；
- 监测指标和数据更新。

请区分短期行动、中期制度建设、长期研究议程。
```

## 11. Reviewer and Quality Control Prompts

### 11.1 Rejection Risk Scan

```text
请作为【目标期刊】匿名审稿人，对以下稿件做拒稿风险扫描：
【题目、摘要、大纲、方法、主要图表】

请按高/中/低风险输出：
- 风险点；
- 为什么会影响接收；
- 对应证据；
- 最小修改方案；
- 理想修改方案；
- 是否需要重新分析。

重点检查：
- 文献计量是否只是描述；
- 检索策略是否可复现；
- 是否缺少系统编码；
- 是否混淆 exposure/access/use/health；
- 政策建议是否空泛；
- 结论是否超出证据。
```

### 11.2 Claim-Evidence Audit

```text
请审计以下正文段落的 claim-evidence 匹配：
【正文段落】
【可用参考文献/图表/编码结果】

输出表格：
- claim；
- claim 类型：事实/解释/机制/政策/预测；
- 支撑证据；
- 证据强度；
- 是否过度外推；
- 建议改写；
- 需要补充引用或分析的位置。
```

### 11.3 Final Checklist

```text
请为这篇综述/文献计量稿生成投稿前检查清单：
【目标期刊、稿件类型、图表、补充材料】

覆盖：
- 题名和摘要；
- 检索日期和检索式；
- PRISMA 流程；
- 纳排标准；
- 软件版本和参数；
- 关键词清洗表；
- 编码手册；
- 图表编号和引用；
- 数据与代码可用性；
- 局限性；
- 政策建议；
- 引用准确性；
- 期刊格式。
```

## 12. Language, Translation, and Style Prompts

### 12.1 Chinese Notes to English Academic Prose

```text
请把以下中文研究笔记改写为英文综述论文段落：
【中文笔记】

要求：
- 翻译论证意图，不逐字照搬中文语序；
- 保持 Cities/SCS 风格：问题导向、证据克制、政策相关；
- 不新增文献和数据；
- 对未被证据支持的因果词进行降调；
- 输出英文段落和中文回译，便于核对。
```

### 12.2 De-AI and Original Academic Expression

```text
请将以下段落改写为自然、克制、原创的学术表达：
【段落】

要求：
- 保留原意和引用位置；
- 重组论证顺序，而不是简单同义词替换；
- 删除宣传式表达；
- 避免模板化连接词；
- 标出哪些句子因证据不足被降调。

注意：目标是提高原创性和学术清晰度，不是规避检测或掩盖来源。
```

## 13. Policy Agenda Prompts

### 13.1 Diagnosis-to-Action Matrix

```text
请基于以下综述发现建立政策议程矩阵：
【主要发现】

矩阵列：
- 证据发现；
- 暴露/可达性/使用/健康/公平中的哪一环；
- 受影响人群；
- 空间尺度；
- 规划或治理问题；
- 可执行政策工具；
- 责任主体；
- 监测指标；
- 潜在副作用；
- 需要进一步研究的证据。

请避免泛泛建议，例如“增加绿地”。必须说明在哪里、为谁、通过什么机制、如何监测。
```

### 13.2 Equity-Centered Planning Agenda

```text
请将以下发现转化为以公平为核心的体育公园/绿色空间规划议程：
【发现与编码结果】

请分别给出：
1. 分配正义：设施和绿色/冷却资源如何更公平分配；
2. 程序正义：如何让弱势群体参与规划和维护；
3. 承认正义：如何识别不同人群的运动、休闲、安全和文化需求；
4. 能力正义：如何让可达性转化为真实使用和健康机会。

每项议程都要包含可操作政策、可能风险和监测指标。
```

## 14. Prompt Chains

### Chain A: From Broad Topic to Journal Route

1. Use 3.1 to select route.
2. Use 4.1 to build RQs.
3. Use 4.2 to define concepts.
4. Use 3.3 to test journal fit.

### Chain B: From Search to Evidence Map

1. Use 5.1 to build search ontology.
2. Use 5.2 to draft protocol.
3. Use 5.3 to calibrate screening.
4. Use 7.1 to build evidence map.

### Chain C: From Bibliometric Results to Argument

1. Use 6.1 to plan analyses.
2. Use 6.2 to clean keywords.
3. Use 6.3 to interpret maps.
4. Use 8.1 and 8.3 to add critical coding.
5. Use 10.5 to build discussion and policy agenda.

### Chain D: From Draft to Submission

1. Use 10.1-10.5 for section drafting.
2. Use 11.1 for rejection-risk scan.
3. Use 11.2 for claim-evidence audit.
4. Use 12.1 or 12.2 for language polishing.
5. Use 11.3 for final checklist.


