# 示例：一段 Discussion 的"机检 → 回改 → 通过"

这个例子演示 `scipilot-writing-skill` 的写作质量证据链：同一段意思，AI 初稿满是指纹且
LaTeX 没转义（机检 **FAIL**），按本技能原则重写后干净自然（机检 **PASS**）。

## 复现

```bash
# 初稿：应 FAIL（未转义 % + 一堆 AI 味）
python ../scripts/writing_lint.py demo_before.tex --mode latex --lang en

# 改后：应 PASS
python ../scripts/writing_lint.py demo_after.tex  --mode latex --lang en
python ../scripts/text_stats.py  demo_after.tex  --lang en
```

## `demo_before.tex`（AI 初稿，机检 FAIL）

> In the ever-evolving landscape of deep learning, our novel framework leverages a myriad of
> techniques to tackle this crucial problem. Moreover, it is worth noting that the model's
> performance is pivotal. Furthermore, extensive experiments demonstrate that our robust method
> achieves 95% accuracy, showcasing its potential and underscoring the importance of this
> groundbreaking direction. Notably, the approach is not only efficient but also scalable, paving
> the way for future research.

机检命中（节选）：

```
[FAIL] LATEX_UNESCAPED: 未转义 '%' ×1（会注释掉整行）
[WARN] AI_WORD: crucial / groundbreaking / landscape / leverages / myriad / pivotal / robust / showcasing / underscoring
[WARN] AI_PHRASE: 'In the ever-evolving landscape' / 'paving the way for' / 'it is worth noting that'
[WARN] AI_SUPERFICIAL_ING ×2（showcasing its potential / underscoring the importance）
[WARN] AI_MECH_CONNECTIVE ×3（Moreover / Furthermore / Notably）
[WARN] AI_NEG_PARALLEL: not only … but also
[WARN] PROMO: groundbreaking
---- ❌ FAIL ----
```

毛病：① `95%` 未转义会注释掉后半行；② 通篇"高级词"堆砌、机械连接词、悬垂 -ing 伪洞见、
否定式平行；③ `model's` 所有格；④ 句长均匀、零具体数字（除了那个会被注释掉的 95%）。

## `demo_after.tex`（重写后，机检 PASS）

> Deep learning has advanced quickly, yet sample efficiency under domain shift remains an open
> problem. We address it with a lightweight adapter: a frozen backbone feeds a task-specific routing
> layer that is trained on a fraction of the usual data. Across four benchmarks, the method reaches
> 95\% accuracy, a gain of 3.1 points over the strongest baseline. The margin is stable. It holds
> whether labels are scarce or abundant, which suggests the gain does not hinge on data volume. Why
> it works, we cannot yet say.

```
[info] STYLE_PASSIVE: 17%
[info] AI_MONOTONE: 句长 mean=14.0 sd=6.9 cv=0.49（min 4 / max 25）
---- ✅ PASS ----
```

改了什么（对应 IRON RULES 与 `de_ai_humanize.md`）：

| 初稿 | 改后 | 原则 |
|---|---|---|
| ever-evolving landscape / groundbreaking / myriad / pivotal | 删除，换具体陈述 | 去 promotional 与高级词堆砌 |
| Moreover / Furthermore / Notably | 删除，靠逻辑自然衔接 | 连接词减负 |
| showcasing its potential / underscoring the importance | 改为给出具体数字与机制 | 删悬垂 -ing 伪洞见 |
| the model's performance | the method / 直接陈述 | 避免方法名所有格 |
| 95% | 95\% | LaTeX 转义 |
| 句长均匀 | 加入 "The margin is stable." / "Why it works, we cannot yet say." | 节奏 burstiness |
| "demonstrate … crucial"（无据强断言）| "suggests … warrants further study"（hedge）| 断言=证据 |

注意：改后**保留了关键数字**（95% 准确率、+3.1 点），并把"会被 % 注释掉"的隐患修好——
去 AI 味绝不以牺牲信息为代价（IRON RULE 1）。
