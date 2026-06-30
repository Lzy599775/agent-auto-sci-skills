# 去 AI 味与人性化（De-AI & Humanize）

> 大模型生成的文本有稳定的语言指纹。本文件是"识别 + 改写"的对照表，与
> `scripts/writing_lint.py` 的词表/正则一一呼应（机器先粗筛，人/AI 读稿再精改）。
>
> **第一原则：宁缺毋滥。** 输入若已自然地道、无明显 AI 特征，判"[检测通过]"并给肯定，
> **不为换词而换词**。去 AI 味是为了更像严谨的人类学者，不是把文字改得面目全非。

---

## 1. AI 指纹：识别清单（detect）

### 1.1 被滥用的"高级"词（英文）
delve / delve into、leverage、harness、underscore、pivotal、crucial、realm、landscape、
tapestry、nuanced、intricate、showcase、myriad、plethora、paradigm、seamless(ly)、
robust（泛用时）、testament、beacon、elevate、boast、unveil、embark、foster、encompass、
meticulous、groundbreaking、revolutionary、transformative、unprecedented、cutting-edge、
state-of-the-art（CS 中 SOTA 可接受，他处慎用）。

> 完整可参考的"高 AI 味词"扩展集（命中即考虑替换，仅供参考）：
> Accentuate, Amplify, Alleviate, Ascertain, Advocate, Articulate, Bolster, Bustling,
> Conceptualize, Consolidate, Convey, Culminate, Decipher, Delineate, Disseminate,
> Elucidate, Endeavor, Envision, Exacerbate, Expedite, Galvanize, Harmonize, Hone,
> Innovate, Interpolate, Manifest, Nurture, Perpetuate, Permeate, Ponder, Prevailing,
> Profound, Reconcile, Rectify, Reimagine, Scrutinize, Substantiate, Tailor, Transcend,
> Traverse, Unveil, Vibrant。

### 1.2 句式 / 结构指纹
1. **机械连接词开头扎堆**：Moreover / Furthermore / Additionally / In addition /
   It is worth noting that / It is important to note / Notably（每段都用就可疑）。
2. **Rule of three（三点式排比泛滥）**：无信息必要地三联——"efficient, scalable, and robust"、
   "clear, concise, and compelling"。人类偶用，AI 成瘾式连用。
3. **破折号（em dash）滥用**：每段多处 `—` 作万能停顿/插入语。
4. **悬垂 -ing 伪洞见（superficial -ing）** ★最强指纹之一：
   "…, highlighting the importance of…"、"…, showcasing its potential…"、
   "…, paving the way for…"、"…, underscoring the need for…"——伪装成洞见的空话尾巴。
5. **否定式平行**："It's not just X, it's Y"；"not only… but also…" 的过度使用。
6. **过度 promotional / 夸张**：groundbreaking、revolutionary、game-changing、seamlessly、
   unprecedented、vast、a wide range of、rich。
7. **空泛归因**："Studies show…"、"Experts agree…"、"It is widely recognized that…" 而无具体引用。
8. **膨胀的象征 / 拔高**："plays a vital role in"、"stands as a testament to"、"a beacon of"、
   "in the ever-evolving landscape of"、"at the forefront of"。
9. **套话收尾**："In conclusion, …"、"Overall, …"、"Ultimately, …" 配空泛展望。
10. **节奏均匀、句长一致、零具体细节**：每句等长对称，缺 human burstiness（用 `text_stats.py` 看 cv）。

### 1.3 中文 AI 味
- **空洞渲染词**：毋庸置疑、众所周知、不可磨灭、范式转移、颠覆性、至关重要、令人惊叹、
  深远的影响、划时代、里程碑式、切中要害、本质上、某种程度上。
- **翻译腔 / 机器味**："为了解决这一痛点"、"展现了令人惊叹的能力"、英式长定语
  "一个……的……的……"、过度"被"字句、机械的"首先…其次…最后…"罗列。
- **公文腔残留**：无故把"旨在"改"拟"、"是"改"系"。

---

## 2. 去 AI 味：改写原则（rewrite）

1. **以具体替代抽象**：把 "underscores its importance" 换成"为什么、对谁、影响多大"（给数字/机制）。
2. **删悬垂 -ing 尾巴**：把 "…, highlighting X" 改为独立句陈述 X 的实质，或直接删。
3. **打散三点式**：保留信息必要的并列；无信息的三联删到一或二，换非排比表达。
4. **连接词减负**：多数 Moreover/Furthermore 可删；用**实质性逻辑衔接**（给-新信息链）替代标签式过渡。
5. **降 promotional**：删 groundbreaking/revolutionary/seamlessly；**让数据自己说话**。
6. **加 burstiness**：长短句交替，打破均匀节奏；允许简短有力的句子。
7. **节制破折号**：多数 em dash 改逗号、冒号或拆句。
8. **实化归因**："Studies show" → "Smith et al. (2021) report…"（找文献转 `scipilot-cite-skill`）。
9. **回归领域具体性**：用本领域术语与精确量词替换 generic 形容词（robust→给指标；a wide range→列举/给范围）。
10. **删 meta 套话**："It is worth noting / important to note" 一律删，直接说事。
11. 改后做**一致性与事实核查**：去 AI 味绝不能引入夸大或改变数值/结论（IRON RULE 1/6）。

### 中文专项
- 情感渲染词 → 具体客观描述："为了解决这一痛点"→"针对上述问题"；"展现了令人惊叹的能力"→"表现出显著的性能提升"。
- 拆英式长定语为短句；少用"被"字句（"被用来优化"→"采用…优化"）。
- 机械罗列融成连贯段落（但算法步骤/几项约束等列举更清晰时可保留）。
- 当代学术书面语：平实、流畅、准确，不堆辞藻、不掉书袋。

---

## 3. 留人味（Inject voice，不只是删）

去掉 AI 痕迹后，好的学术文本仍应有"人"的特征：
1. **有观点、有判断**：明确哪个结果最重要、哪个解释更可信，而非平铺罗列。
2. **承认不确定性**：得体的 hedging（见 `sci_writing_principles.md` §3）本身就是人类学者的特征。
3. **节奏变化**：关键结论用短句收束，铺垫用长句；段落有起伏。
4. **领域质感**：用同行才会用的精确表达，而非通用"高级词"。

---

## 4. 输出规范（去 AI 味任务）

- **Part 1**：重写文本（已足够好则原样返回）。LaTeX 守纯净+转义；Word 纯文本+全角+零 Markdown。
- **Part 2**：直译核对（中↔英任务）。
- **Part 3 / 检测结论**：
  - 有修改 → 简述删改了哪些典型 AI 表达。
  - 未修改 → 直接输出"**[检测通过] 原文表达地道自然，无明显 AI 味，建议保留。**"
- 必过 `writing_lint.py`（抓词表/悬垂-ing/破折号/否定平行/连接词）+ `text_stats.py`（句长 cv 看节奏）。
