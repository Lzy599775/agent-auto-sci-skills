# 句子与段落层面的高水平写作技法

> 这是把一段话从"语法正确"提升到"读着像顶刊"的内功。`scipilot-writing-skill` 在
> Stage 3 改写时套用本文原则，Stage 5 读稿时据此复核。

---

## 1. 时态规范（各章节惯用）

| 语境 | 时态 | 例 |
|---|---|---|
| 公认事实 / 普遍真理 | 一般现在时 | "Proteins fold into specific structures." |
| 文献既有发现（泛指） | 现在时 / 现在完成时 | "Prior work shows / has shown…" |
| 引用某具体研究做了什么 | 过去时 | "Smith et al. (2020) found…" |
| 本文的方法与所得结果 | 过去时 | "We measured…; expression increased…" |
| 指代图表本身 | 现在时 | "Figure 2 shows…" |
| 结论 / 意义 / 推断 | 现在时 | "These results suggest…" |
| 研究空白尚存 | 现在时 / 现在完成时 | "remains unclear / has not been examined" |

**易错**：同一段里方法过去时与结果现在时来回跳；Abstract 里背景与结果时态混乱。

---

## 2. 语态：主动 vs 被动

1. **现代趋势是适度提高主动语态**。Nature/Science 等明确鼓励用 "We" 提升可读性与责任归属。
2. **被动仍有正当用途**：当操作对象是焦点、施动者无关或显然时（Methods 尤甚）——
   "Samples were incubated at 37 °C" 比 "We incubated the samples" 更聚焦对象。
3. **按信息焦点选语态**，不是教条地全主动或全被动；同段要维持给-新衔接（见 §4）。
4. 避免"僵尸被动"——施动者被藏起来导致责任不清（"mistakes were made"）。

经验法则：强调**我们的设计决策**用主动；强调**对象被如何处理**用被动。

---

## 3. Epistemic stance：Hedging 与 Boosting

学术写作的可信度，很大程度来自**断言强度与证据强度匹配**。

- **Hedging（缓和）**：may / might / could、suggest / indicate / appear、likely / possibly、
  tend to、relatively、to some extent。用于：机制推断、外推、涉及因果的主张。
  **这是严谨的体现，不是不自信。**
- **Boosting（强化）**：clearly、demonstrate、establish、show（强义）、substantially、markedly。
  用于：有强证据直接支撑的核心发现。

**得体三原则**
1. 有强数据 → 可 boost；超出数据的推断 → 必 hedge。
2. 区分 **show / demonstrate（有直接数据）** 与 **suggest / imply（间接、推断）**。
3. **忌堆叠**："may possibly suggest" 三重冗余；"It is clearly obvious that" 过度。一处一个强度词即可。

**红线**：绝不把相关说成因果（"X is associated with Y" ≠ "X causes Y"）；绝不把单一/有限研究上升为普适。

---

## 4. 衔接与连贯（Cohesion & Coherence）

1. **Topic sentence（主题句）**：每段首句给主旨，段内句子都服务于它。读者扫首句就能抓结构。
2. **Given-new contract（旧信息在前，新信息在后）**——英文段落连贯的核心机制：
   句子开头承接上句已知信息，句尾落下新信息；下一句再从这个新信息接起，形成信息链。
   > 例：…improves accuracy. **This improvement** stems from the auxiliary loss. **The loss** …
3. **Signposting / 元话语**：First… Second…、In contrast、Consequently、Taken together、
   "Having established X, we next…"。给读者路标，但**别机械堆砌**（见 `de_ai_humanize.md`）。
4. **Parallelism（平行结构）**：并列项语法形式一致——"designing X, training Y, and evaluating Z"。
   列表、对比、贡献项尤其需要平行。
5. **指代清晰**：This / These 后接名词（"This increase" 而非裸 "This"）；避免悬空指代。
6. **段落长度**：一段一观点，3–6 句为宜；过长拆分，过碎合并。

---

## 5. 简洁性（Concision）

1. **去名词化**：动作藏进名词会笨重。
   - perform an analysis of → analyze
   - make a comparison between → compare
   - is indicative of → indicates
   - provide an explanation for → explain
2. **冗余短语替换**：
   - in order to → to ｜ due to the fact that → because ｜ a majority of → most
   - in the event that → if ｜ at this point in time → now ｜ has the ability to → can
   - a number of → several / 给具体数 ｜ in spite of the fact that → although
3. **弱化 there is / it is 开头**："There are many studies that show" → "Many studies show"。
4. **删空泛限定词**：very / quite / really / basically / actually / 不必要的 "in the literature"。
5. **避免双重否定绕弯**："not unlike" → "like"。
6. 一句一个核心意思；超过约 40 词的长难句拆开。

---

## 6. 数字 / 单位 / 统计 / 缩写 / 拼写一致性

### 6.1 数字
- 句首不用阿拉伯数字（要么拼写，要么改写句子）。
- 常规：<10 拼写、≥10 用数字（刊规不一，服从目标刊）；**带单位一律数字**（5 mg）。

### 6.2 单位
- SI 单位；数与单位间空格（5 kg；例外：`%` 与 `°` 不空格）。
- 变量斜体、单位正体；全文统一千分位与小数风格。

### 6.3 统计量报告（顶刊硬规范）
- 报告 **effect size + 不确定性（95% CI 或 SD/SEM）**，不要只给 P 值。
- **P 值**：给具体值（P = 0.003）而非仅 "P < 0.05"；极小写 P < 0.001；**绝不写 P = 0.000**。
- 明确 n、自由度、检验统计量（如 t(38) = 2.1）。
- **有效数字一致**：按测量精度，通常 2–3 位有效数字；P 值 2 位有效数字；不给超过仪器精度的位数。
- **统计显著 ≠ 实际重要**；不显著 ≠ "无效应"（用 CI 体现精度）。
- 统计符号斜体：P、t、n、r、F；希腊字母按惯例。

### 6.4 缩写
- 首次出现给全称（缩写），随后统一用缩写；Abstract 与正文**各自首次**定义。
- 不为只出现一次的词造缩写；避免缩写过密导致阅读阻塞。

### 6.5 US / UK 拼写
- 全文统一一种：analyze/analyse、color/colour、-ize/-ise、center/centre、modeling/modelling。
- 服从目标刊（多数美刊用 US；部分英刊/Elsevier 接受 UK）——但**必须一致**。

### 6.6 其他一致性
- Oxford comma（随刊）；连字符（作定语时 well-known、state-of-the-art）。
- 物种名斜体（*E. coli*）；基因/蛋白命名遵循领域命名委员会。
- 参考文献格式全文统一（交给 `scipilot-cite-skill`）。

---

## 7. 一句话速记

> **时态分场景、语态看焦点、断言配证据、句子给-新接、能删就删、数字守规范、全文要一致。**
