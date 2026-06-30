# 逐章节写作 Playbook

> 同类"写作 prompt 清单"通常只做句子级润色；高水平 SCI 论文的难点其实在**章节结构**。
> 本文件给每个章节的：**目标 / 信息流 / 要点 / 常见错误**。起草或重写某节时加载对应小节。

---

## Title（标题）

**两类基调**
- **Descriptive / 信息型**：陈述主题（"Single-cell analysis of X in Y"）。综述、方法、保守领域常用。
- **Declarative / 陈述发现型**：直接给结论（"X drives Y via Z"）。顶刊与高影响结果倾向此类。

**要点**
1. **关键词前置**：最重要的概念放句首——读者只扫前几个词，检索引擎也偏重前部。
2. 长度多为 **10–15 词**；写清 system / method / finding，避免 "A study on…/Investigation of…" 零信息开头。
3. 可用冒号副标题承载方法名或体系（"MethodName: what it does"）。
4. **避免**：未定义缩写、行话、5+ 名词连串的 noun pile、问号式标题（部分刊不喜）、
   "Novel / First-ever / 最…" 自夸词、与摘要/结论不一致的夸大。

**产出建议**：给 5 个候选（2 descriptive + 3 declarative），标注各自适配的期刊基调，让作者选。

---

## Abstract（摘要）

**信息流**（单段或结构式通用）：
`Background(1句) → Gap/问题(1句) → Approach/方法(1–2句) → Key results 带数字(2–3句) → Implication(1句)`

**要点**
1. **结构式 vs 非结构式**：医学/部分 IEEE 用带小标题的 structured abstract；Nature/Science/Cell 多为非结构式单段。按目标刊定。
2. **关键结果必须带数字**：报告效应量/关键指标（"reduced X by 32%, P < 0.001"、"AUC 0.91"），不要只说 "significantly improved"。
3. **自足**：不引用文献、不含未定义缩写、不引图表编号（Science/IEEE 明确禁止）。
4. 第一句别从教科书常识起笔；直接进入本研究语境。
5. 严卡词数，把"意义"压成一句；不写 "Further studies are needed" 这类空话。

**常见错误**：摘要承诺正文没兑现的结论；只有定性词无定量结果；把 Introduction 整段搬进来；漏掉主发现的方向与幅度。

---

## Introduction（引言，Swales CARS 模型）

**CARS = Create A Research Space**，三个 Move 构成由宽到窄的漏斗：

### Move 1 — Establishing a territory（建立领域重要性）
- 陈述领域核心事实/重要性（现在时，呈现为公认知识）。
- 综述相关前人工作，**按主题组织**，不做逐篇编年流水账。
- 避免开头过宽（"Since the dawn of…"）。

### Move 2 — Establishing a niche（指出 gap / 缺口）★ 枢纽
- 用转折标记开启：**However / Yet / Despite / Nevertheless / remains unclear / has not been addressed**。
- 指出文献的不足、矛盾、未解问题或方法局限。
- **gap 必须真实，且与本文贡献精确对应**——这是全篇说服力的支点。Move 2 缺失，读者就不知道你为什么要做这项研究。

### Move 3 — Occupying the niche（占据缺口，陈述本文）
- 明确目的/做了什么（"Here we… / In this work, we…"）。
- 概述方法或主要发现（可前瞻结论）。
- 可给 **contributions 列表** + 论文结构（CS/工程常见）。

**最后一段 contributions 写法**
1. 用并列动词开头，或 "We make the following contributions:" / "First… Second… Third…"。
2. 每条 = 一个**可验证、可区分**的贡献（新方法/新数据集/新分析/新结论），**与 Results 章节一一对应**。
3. 动词凸显新颖性：propose / introduce / design / demonstrate / establish / release。
4. 别把"做了实验"当贡献；别让贡献数 > 论文真实新意（灌水感）。

**常见错误**：Intro 写成 literature review；gap 与贡献不对应；末段没清楚说"本文做了什么"。

---

## Methods（方法）

**核心目标：可复现性**——他人据此能重做。

**要点**
1. **时态用过去时**（描述已完成的操作）。
2. **语态混用**：强调"我们的设计决策"用主动；强调"对象被如何处理"用被动（"Samples were incubated…"）。
3. 结构化分小节：材料/试剂（厂商、catalog #、RRID）、设备、样本与受试者（纳入/排除、伦理批件号、知情同意）、流程、数据处理、**统计方法**。
4. **统计方法须报告**：检验名称及单/双侧、显著性阈值、多重比较校正、效应量与区间算法、缺失数据处理、**软件及版本**、随机化与盲法、**样本量如何确定**（效能分析）。
5. 遵循对应**报告规范**（见 `journal_styles.md`）：RCT→CONSORT，观察性→STROBE，动物→ARRIVE。
6. 给出**数据/代码可得性**指引；如有预注册/protocol 须引用。
7. 已发表方法可引用省篇幅（"as described in [x]"），但关键改动须写明。

**常见错误**：细节不足无法复现；只报"用了 t 检验"不报前提与校正；混用时态；遗漏版本/厂商；把结果或解释写进 Methods。

---

## Results（结果）

**核心原则：只陈述发现，不解释**（解释留给 Discussion）。

**要点**
1. 按逻辑/重要性而非时间组织；每子节有 topic sentence 概括该发现。
2. **图表与正文分工**：数据放图表；正文点出趋势与关键数值并解读走向，**不逐格复述表格**。引用为 "(Fig. 2a)"。
3. **统计量报告**（详见 `sci_writing_principles.md` §6.3）：报 effect size + CI；P 给具体值；明确 n 与检验量；有效数字一致。
4. 时态：现在时陈述图表本身（"Figure 2 shows"），过去时陈述具体观测（"Expression increased"）。
5. 负面/非预期结果照实报告（IRON RULE 1）。

**常见错误**：在 Results 里解释机制或与文献比较（应移 Discussion）；文字复述整张表；只报 P 不报效应量与方向；"trend toward significance" 这类暧昧表述；选择性报告（cherry-picking）。

---

## Discussion（讨论，倒漏斗，由窄到宽）

**结构**
1. **开头重述关键发现**（不重复数字，用解读语言："Our results demonstrate that…"）。
2. **与文献对话**：与前人结果对照，解释一致/矛盾。
3. **机制解释 / interpretation**：为何得到该结果，提出机制或理论含义。
4. **Limitations**：诚实列方法/样本/外推局限及其**对结论的影响方向**。
5. **Future work / implications**：后续方向与实际/理论意义。

**要点**
- 第一段不要重复 Results 的罗列；聚焦"发现意味着什么"。
- Hedging 得体：机制推断用 may/suggest/likely；不把相关说因果。
- Limitations 要**具体且配应对**（"Although the sample was limited to X, the effect held across Y"），而非套话清单。
- 结论句呼应 Intro 的 gap，显示 gap 已（部分）被填补。

**常见错误**：Discussion = Results 复述；overclaiming，把单一研究上升为普适；limitations 写成免责套话或避而不谈；引入 Results 未呈现的新数据。

---

## Conclusion（结论）

1. 一段；凝练**本文回答了什么 + 最重要的一条 take-home**。
2. 不引入新结果/新引用。
3. 可给一句 forward-looking 的影响或应用。
4. 避免与 Abstract 逐字重复（换表述、聚焦最高层结论）。

---

## Limitations / 声明类

- **Limitations**：若无独立节则并入 Discussion；覆盖内/外部效度、样本、测量、可推广性。
- **Data Availability Statement**：多刊强制；写明仓库名 + accession/DOI、获取条件、受限数据的合规理由。
- **Code Availability**：链接仓库（GitHub + 版本/commit 或 Zenodo DOI）。
- **其他**：Funding；Author contributions（可用 CRediT）；Competing interests；Ethics（IRB/IACUC 批号）；
  Acknowledgments（资助/技术/语言润色等**非作者贡献**，据 ICMJE 不构成署名）；如用 AI 工具须按目标刊要求声明。

---

## 章节写作推荐顺序（减少返工）

> 经验：先写"有数据支撑、最确定"的部分，最后写需要全局视野的部分。

```
Methods + Results（配对写，一一对应）
   → Discussion（基于已定的发现）
   → Introduction（Move 3 的贡献要呼应 Results）
   → Conclusion
   → Abstract（全文定稿后压缩）
   → Title（最后定，与摘要/结论一致）
```
