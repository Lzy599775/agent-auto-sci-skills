# Methodology / Research Design

Use this primary workflow when the deliverable is a scientific judgment about a proposed design
or an existing study's methods. It applies across disciplines and data types, before data exist
and during critical appraisal. Load `agent-auto-sci-methodology` and its required general
methodology reference; use domain playbooks only when the actual task calls for them.

## Routing boundary

- Design appraisal, estimands, identification, bias, inference assumptions, and model
  appropriateness use `methodology`, including scrutiny of a paper's Methods section.
- Cleaning data, fitting models, and measuring prediction performance use `data_analysis`.
- Rewriting a Methods section uses `manuscript_writing`; scientific appraisal may accompany it.
- Reproducing a published model or result uses `paper_reproduction`, with methodology or
  data analysis as needed. Novelty and feasibility use `research_idea_evaluation`.
- Choose by the intended decision or deliverable. A model name or the word Methods is not
  enough to choose a route. Clarify a materially ambiguous goal after the routing bootstrap.

Ordinary method consultation does not initialize Master20/Core3 or read manuscript private
state. Appraisal of a supplied manuscript can use its explicitly authorized material without
activating exemplar initialization. Substantive rewriting follows the separate writing gate.

## Procedure

1. Define the research question, target population/context, unit, outcome, and decision.
   Distinguish descriptive, predictive, associational, and causal aims.
2. Specify the target estimand where applicable, including treatment/comparator, population,
   time, and heterogeneity target. Separate a model output from the scientific quantity.
3. Appraise the experimental, quasi-experimental, observational, survey, or other design.
   Review sampling, power/precision reasoning, measurement validity, and missingness.
4. State identification requirements and assess their evidence: confounding, selection,
   temporal order, exchangeability, positivity/overlap, interference, and design-specific
   conditions as applicable. Overlap and predictive accuracy do not establish identification.
5. Assess statistical inference assumptions, dependence/clustering, leakage, model
   appropriateness, uncertainty, multiplicity, and transportability where relevant.
6. Propose defensible alternatives, robustness and sensitivity checks, diagnostic evidence,
   and falsification tests. Explain what each can and cannot establish.
7. Bound conclusions by the design and available evidence. Preserve negative findings,
   uncertainty, raw data, provenance, and source traceability. Never invent user data or results.

## Output record

Use the fields below proportionately to the task. Missing facts are `NOT_VERIFIED`;
use `NOT_APPLICABLE` with a reason where a field does not apply. Recommendations are
clearly distinguished from established facts. No field requires fabricated precision.

```text
RESEARCH_QUESTION =
TARGET_ESTIMAND =
STUDY_DESIGN =
IDENTIFICATION_REQUIREMENTS =
KEY_ASSUMPTIONS =
MAJOR_BIAS_RISKS =
METHOD_SUITABILITY =
REQUIRED_EVIDENCE =
VALIDATION_PLAN =
CLAIM_BOUNDARY =
```

Apply the [evidence trace](../standards/evidence_trace.md),
[data provenance](../standards/data_provenance.md), and
[academic claim](../standards/academic_claims.md) standards as relevant. Preserve the
global resource guard and output-format contracts. No Zotero or external write follows
merely from selecting this workflow.
