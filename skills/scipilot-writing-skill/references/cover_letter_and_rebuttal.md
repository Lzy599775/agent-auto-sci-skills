# 投稿信与审稿回复（Cover Letter & Rebuttal）

> 这两类文本不进正文，却常常决定稿件命运。它们是"写作"的一部分，也是同类 prompt 清单
> 普遍缺失的能力——本技能的"只多"。

---

## Cover Letter（投稿信）

### 结构
1. **抬头**：致主编（尽量具名）、日期、稿件题名与类型。
2. **第 1 段**：一句话点明**研究做了什么 + 核心发现**。
3. **第 2 段**：**为何适配该刊**——契合 scope、对该刊读者的意义、与该刊近期文章的关联；
   **新颖性与重要性**（1–2 句，有据不浮夸）。
4. **第 3 段**：**合规声明**——原创且未一稿多投、所有作者同意署名、无未披露利益冲突、
   伦理批准（如涉及人/动物）、数据可得性。
5. **可选**：推荐 / 回避审稿人（附理由）、与编辑既往沟通（如 presubmission inquiry）。

### 要点
- **1 页以内**。
- **不是抄摘要**，而是"卖点 + 适配性"：摘要讲"做了什么"，投稿信讲"为什么是这本刊该发的"。
- significance 要具体而不夸大（避免 "the most important advance"）。
- 语气专业、克制、自信但不傲慢。

### 常见错误
- 套用通用模板忘改刊名（致命，编辑一眼看穿）。
- 直接复制摘要。
- 夸大重要性。
- 漏掉合规声明。

### 模板骨架
```
Dear Dr. [Editor Name],

We are pleased to submit our manuscript, "[Title]," for consideration as a
[Article Type] in [Journal].

[一句话：做了什么 + 核心发现，带一个关键数字]. [为何重要 / 填了什么 gap].

This work is well suited to [Journal] because [契合 scope / 对该刊读者的意义 /
与近期某文的关联]. [1 句新颖性，有据].

This manuscript is original, has not been published previously, and is not under
consideration elsewhere. All authors have approved the submission and declare no
competing interests. [伦理 / 数据可得性声明，如适用].

We thank you for your consideration.

Sincerely,
[Corresponding Author], on behalf of all authors
```

---

## Response to Reviewers / Rebuttal（审稿回复）

### 总体策略
1. **Point-by-point**：逐条**引用**审稿意见（编号/加粗），其下给回应，再标注稿件中修改位置（页/行或引用改后文字）。
2. **礼貌而有据**：开篇感谢审稿人；每条以建设性语气回应；**用数据 / 文献 / 逻辑支撑**，不靠情绪或空头承诺。
3. **区分三类意见**：
   - **能改的**（补实验、加分析、改写、补引用）→ 明确"已照做"，给出新结果/新文字。
   - **不认同的** → **礼貌反驳并给理由/证据**，不盲从；必要时折中（如加一句 limitation 说明而非重做）。
   - **结构性 / 超范围的** → 解释为何超出本文范围，或承诺 future work，坦诚说明限制。
4. **协调冲突**：多个审稿人意见冲突时要说明你如何取舍。
5. **一致性**：所有"已修改"必须与稿件实际改动对应（编辑会核对）。

### 格式约定
- 开头可附 **summary of major changes**。
- 用排版区分三种内容：**审稿意见**（一种字体/颜色）、**作者回应**（另一种）、**改后正文文字**（引号或第三种），便于编辑比对。
- 每条意见都要回应——哪怕只是"感谢指出，已修正"，**不漏任何一条**。

### 要点
- 承认合理批评会提升可信度，不是示弱。
- 反驳时**对事不对人**，给证据。
- 给审稿人**找到改动的便利**（精确定位页行）。

### 常见错误
- 笼统说"已修改"却不给位置。
- 忽略某条意见。
- 与审稿人争辩口角。
- 口头同意却没真改。
- 不同回应之间自相矛盾。

### 单条回应骨架
```
**Comment 1 (Reviewer 2):** [原样引用审稿意见]

**Response:** We thank the reviewer for this point. [回应：承认/解释/反驳，给依据].
We have [具体改了什么] (see Section X, p. Y, lines Z): "[引用改后的关键句]".
```

---

## 与本技能其他剧本的衔接
- 写完 rebuttal 后，用剧本 6（英文润色）+ 剧本 9（去 AI 味）把回复语言打磨干净。
- 需要补的新实验若涉及配图 → `scipilot-figure-skill`；补文献 → `scipilot-cite-skill`。
- 回复语气可借剧本 13（审稿人视角）反向预判："如果我是审稿人，这条回应能说服我吗？"
