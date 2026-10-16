# Research Orchestrator Activation Cases

All examples below are `SYNTHETIC_EXAMPLE`. No example is a default research topic.
Choose by the intended scientific judgment or deliverable, not field names or model keywords.
The repository golden set `evals/routing/GENERAL_PURPOSE_ROUTING_GOLDEN_SET_V1.json`
contains A–M inputs, paraphrases, near-neighbor counterexamples, semantic intents and expected routes.

## Should activate

- A: public-health causal identification -> methodology.
- B: materials-experiment statistical design -> methodology.
- C: ecological observational bias -> methodology.
- D: survey sampling and measurement validity -> methodology.
- E: CSV cleaning and regression execution -> data_analysis.
- F: measured prediction-performance validation -> data_analysis.
- G: scientific figure creation -> figure_workflow.
- H: substantive Discussion structure revision -> manuscript_writing with isolated state.
- I: a single academic sentence edit -> lightweight writing; no Master20/Core3 or private-state read.
- J: published-result code/data reproduction -> paper_reproduction.
- K: paper/repository identity and availability -> literature_review plus artifact protocol.
- L: pre-compute resource check -> data_analysis, preflight_only; no computation.
- M: novelty/feasibility -> research_idea_evaluation.
- General literature synthesis -> literature_review; verify sources and paper artifacts.
- Citation support -> citation_claim_audit; literature specialist only when retrieval is needed.
- Model suitability before fitting -> methodology, not data_analysis.
- `SYNTHETIC_EXAMPLE`: “帮我评估一个新的绿地暴露研究选题。” ->
  research_idea_evaluation with literature as needed. This is an optional domain example.
- `SYNTHETIC_EXAMPLE`: “检查这个 Methods 是否足以支持因果结论。” ->
  methodology. Rewriting its wording instead uses manuscript_writing.

Default methodology specialist: `agent-auto-sci-methodology`. Do not create a competing owner.
Retain `agent-auto-sci-scicomm` as the unique substantive academic-writing owner.

## Should not activate

- Casual conversation or simple arithmetic.
- Generic translation with no scientific evidence requirement.
- Unrelated software debugging.

## Evaluation and evidence

Run `python -B -m unittest discover -s scripts/validation -p test_generic_research_routing.py -v`
from the repository root. These are synthetic contract/isolation tests, not fresh-client activation.
The test report records ACTUAL_ROUTE and PASS_OR_FAIL for the evaluated contract.
Paraphrases and near neighbors must later be sent to genuinely new Codex/ChatGPT chats without
Skill names; record actual workflow/file-read evidence. Do not mark those runs PASS from a fixture.

For project-isolation tests use two synthetic projects with distinct manuscript IDs, questions,
state, corpus versions, data sources and result ledgers. Record access attempts, enforce identity
before state access and preserve the Core3 approval gate. No real manuscript/Zotero data are inputs.
