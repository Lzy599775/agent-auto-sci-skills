# Research Orchestrator Activation Cases

## Should activate

1. “帮我评估一个新的绿地暴露研究选题。”
2. “检查一篇文献是否支持论文中的一句话。”
3. “规划如何复现这篇论文。”
4. “检查这个 Methods 是否足以支持因果结论。”
5. “为这个数据分析建立可复现的研究计划。”
6. “审计论文图表和结论之间的证据关系。”

## Should not activate

1. Casual conversation.
2. Simple arithmetic.
3. Generic translation with no scientific evidence requirement.
4. Unrelated software debugging.

## Expected routing

- Citation support -> citation-claim audit, with `literature` as a specialist when source retrieval is needed.
- Green-exposure topic evaluation -> research idea evaluation plus literature review.
- Causal-method sufficiency -> citation/method evidence audit without upgrading association to causation.
