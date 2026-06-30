# 期刊风格与报告规范

> 同一篇研究，投 Nature 和投 IEEE Trans，结构、篇幅、语气、报告清单都不同。本文件按
> **目标刊 + 研究类型**给路由。**硬性数字以投稿当时目标刊的 "Instructions for Authors" 为准**
> （子刊与主刊常有差异）；本文件给的是数量级与惯例，用于起草时定调。

---

## 0. 投稿前路由（先定两件事）

| 维度 | 决策 |
|---|---|
| 目标刊体例 | 查 target journal 的 "Information / Instructions for Authors" + "Article types" |
| 研究类型 → 报告规范 | RCT→CONSORT；观察性→STROBE；系统综述/Meta→PRISMA；动物→ARRIVE；诊断→STARD；预测模型→TRIPOD；病例报告→CARE；定性→COREQ；卫生经济→CHEERS；不确定→查 **EQUATOR**（700+ 指南库）|
| 署名 / 伦理 | ICMJE 4 条标准 |

---

## 1. 顶刊核心数字速查（数量级，以官方为准）

| 刊 | 正文 | 摘要 | Display items | Refs | 特色强制项 |
|---|---|---|---|---|---|
| **Nature** Article | ≤ ~3,500 词 | ~150 词，**无引用** | ≤ 6 | ≤ ~50 | Methods **后置**（不进印刷版）；**首段须通俗化**写给外行 |
| **Science** Research Article | ≤ ~3,000 词（长版 ~6,000）| ≤ 125 词（上限 250）| 3–5（长 6）| ~50（长 100）| **one-sentence summary ≤ 135 字符**；refs 列**全部作者** |
| **Cell** | 页预算 | ~150 词单段 | — | — | **Highlights** 4×≤85 字符；**eTOC** ~40 词；Graphical Abstract 1200×1200；**STAR Methods** |
| **PNAS** | — | ≤ 250 词 | — | — | **Significance Statement ≤ 120 词**，写给领域外读者 |
| **IEEE** Trans | 初稿 ~10–12 页 | 150–250 词，无引用/公式/缩写 | — | 编号制 | **Index Terms** 3–10 个 |

> 这些"写给外行"的组件（Nature 首段、PNAS Significance、Cell eTOC）是编辑 triage 的依据——
> 常先读 Title→Abstract→Significance/Highlights 决定是否送审。**别写成压缩版 abstract**。

---

## 2. 跨学科风格差异

### 2.1 CS / AI 顶会（NeurIPS / ICLR / CVPR / ACL）
1. 结构灵活，常显式 **Contributions 列表** + 独立 Related Work；允许 "We" 主动语态，claim 较直接强。
2. **可复现性硬要求**：checklist、代码/数据/超参/seed 释出；附录可极长。
3. 引用密度高；模板定引用制（NeurIPS 编号）；**双盲**，投稿期匿名。
4. **页数硬限**（正文 8–9 页 + 无限附录）；baseline 对比表是核心。
5. 标题常 declarative + 含方法名；摘要直接给 SOTA 数字与提升幅度。

### 2.2 自然科学顶刊（Nature / Science / Cell）
1. **广受众导向**：首段/significance/blurb 去行话写给跨领域读者；叙事性（"we show that…"）。
2. **极严篇幅/display 限制**；大量内容入 Extended Data / Supplementary。
3. Methods 后置或 STAR，但要求极高可复现细节与试剂溯源（RRID）。
4. 新颖性与广泛意义门槛高；Discussion 强调 broad implication。
5. 引用受限，精选代表性文献而非穷举。

### 2.3 医学（NEJM / Lancet / JAMA / BMJ）
1. **报告规范强制**：按类型套 CONSORT/STROBE/PRISMA，提交 checklist + flow diagram。
2. **统计严格**：预注册、primary/secondary outcomes 事先界定、样本量/效能、ITT 分析、effect size + 95% CI、多重比较校正；结构式摘要。
3. **伦理与透明**：试验注册号、IRB、知情同意、COI、资助方角色、数据共享声明。
4. **临床意义优先于统计显著**：报 NNT、绝对风险差等可解释指标。
5. 谨慎 hedging，避免因果过度宣称（观察性研究尤甚）。

### 2.4 工程（IEEE Transactions）
1. 结构：Abstract→Index Terms→Intro→方法/实验→Conclusion→References；摘要 150–250 词、无引用/公式/缩写。
2. **编号引用 [n]**，按正文出现顺序；公式居中右编号 (1)，变量斜体、矢量粗体、单位正体。
3. 双栏模板、页数预算 + 超页费；图表清晰，含复杂度/性能对比。
4. 技术中性语气，被动较多但主动渐增；强调 problem formulation 与系统贡献。

### 2.5 中文核心期刊（计算机学报 / 软件学报 / 自动化学报）
1. **全角标点**：中文句内用全角 `，。；：""（）、`；数字与西文用半角并与中文留排版间距。
2. **文风**：规范书面语，少第一人称口语；摘要为"目的-方法-结果-结论"结构式；须中英双语题名/摘要/关键词。
3. 结构：引言-相关工作-本文方法-实验-结论；参考文献国标 **GB/T 7714**（`[J]/[C]/[M]` 标识）。
4. 元数据：基金资助脚注、作者简介、中图分类号（TP…）、文献标识码。
5. 量和单位执行国标（GB 3100/3101），变量斜体、单位正体。

---

## 3. 报告规范清单（按研究类型）

### EQUATOR Network（总入口）
健康研究报告规范伞状库（700+），按方法选规范。`equator-network.org`

### CONSORT（随机对照试验 RCT）
- **CONSORT 2025**（优先）：30 项，新增 **Open Science** 板块（注册、protocol、数据/代码可得性、资助）。
- CONSORT 2010（旧稿常见）：25 项 / 6 板块。
- **Flow Diagram 必备**：Enrollment→Allocation→Follow-Up→Analysis，各阶段人数与排除/失访原因（体现 ITT）。

### PRISMA 2020（系统综述 / Meta 分析）
- **27 项**；含检索式、合成方法、**证据确定性（GRADE）**、利益冲突、数据代码可得性。
- **四阶段流程图**：Identification→Screening→Eligibility→Included；区分 records / reports / studies。

### ARRIVE 2.0（动物研究）
**Essential 10**：研究设计 / 样本量(含效能) / 纳入排除 / 随机化 / 盲法 / 结局指标 / 统计方法(+软件) /
实验动物(种系性别龄重来源) / 实验流程(可复现) / 结果(汇总统计+变异度量+效应量与CI)。另 Recommended 11–21。

### STROBE（观察性：队列 / 病例对照 / 横断面）
**22 项**（18 通用 + 6/12/14/15 设计特异）；Methods 含偏倚应对、样本量、统计（混杂/亚组/缺失/敏感性）；
Results 报校正前后估计 + 95% CI；Discussion 含 Limitations 偏倚方向与 Generalisability。

### ICMJE 署名 4 标准（须全部满足）
①实质贡献于构思设计或数据获取/分析/解读；②起草或批判性修改；③最终批准；④同意对全部工作负责。
**仅满足 <4 条 → 致谢，不署名**。获取资助 / 一般监督 / 语言润色**不单独构成署名**。

---

## 4. 起草时的"定调"清单

接到任务先回答：
1. 目标刊属于哪一栏（§2）？→ 决定语气、主动/被动、claim 强度、是否要"写给外行"的组件。
2. 篇幅与 display 限制（§1）？→ 决定详略与什么进正文 vs 补充材料。
3. 研究类型对应哪个报告规范（§3）？→ Methods/Results 必须覆盖其清单项。
4. 引用格式与文献交给 `scipilot-cite-skill`；配图交给 `scipilot-figure-skill`。
