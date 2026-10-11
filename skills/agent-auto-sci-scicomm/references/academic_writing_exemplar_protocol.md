# Academic Writing Exemplar Decomposition Protocol

**Version:** V1
**Role:** pre-drafting and pre-revision argument-architecture handoff
**Owner:** `agent-auto-sci-scicomm`
**Not:** a top-level skill, a literature-review owner, or a polishing owner

## Purpose and invariant

Use this protocol to learn reusable argument architecture from verified, function-matched papers before drafting or substantially revising a manuscript. The protocol decomposes structure, rhetorical function, evidence ordering, figure ordering, and discussion strategy. It never supplies facts for the user's manuscript.

The scientific contract is invariant across clients:

- author text, author data, verified results, and verified literature are the evidence boundary;
- numbers, formulas, variables, citations, effect directions, and sample sizes are protected content;
- exemplar patterns can inform organization, but cannot add results, mechanisms, causal claims, references, data, or contributions;
- scientific content is stabilized before prose polishing;
- `Style strength <= evidence strength`.

Language tools serve clarity, naturalness, argument rhythm, and author voice. They are not used for AI-detection evasion. Hidden Unicode or formatting residue may be cleaned as document hygiene, but provenance metadata is preserved by default.

## Routing contract

### `WRITING_EXEMPLAR_MODE`

The mode is one of `REQUIRED`, `AUTO`, or `SKIP`.

| Mode | Select when | Minimum action |
|---|---|---|
| `REQUIRED` | The user says to imitate, benchmark, learn from a target journal, follow named paper structures, or requests target-journal adaptation. | Obtain or request exemplars, record read scope, build maps, and apply the anti-copying contract. If sources are unavailable, use the degraded mode and report the limitation. |
| `AUTO` | The task is substantive writing: full manuscript, Introduction, Discussion, Conclusion, Abstract, review synthesis, major restructuring, or journal-targeted revision, and at least one function-matched exemplar can be obtained from an authorized corpus or current retrieval. | Run the protocol for each substantive section; do not reuse one paper set for the whole manuscript by default. |
| `SKIP` | Sentence-level proofreading, grammar-only correction, citation-format-only work, a minor typo, a single caption micro-edit, or a pure code task. | Continue to the existing writing or lint owner without exemplar search. |

Explicit user instructions take precedence over automatic classification. A structured journal format, reporting guideline, or scientific-content requirement takes precedence over the user's soft style preference.

### Existing-owner handoff

The protocol is inserted into the existing route; it does not replace an owner:

```text
auto-sci-research
  -> agent-auto-sci-scicomm (argument and communication owner)
  -> domain writing skill when applicable
  -> own evidence map and argument outline
  -> academic writing exemplar protocol when REQUIRED/AUTO
  -> draft or revise from our evidence
  -> Academic Prose Style Guard
  -> scipilot-writing-skill (final prose, polishing, and lint owner)
```

For simple proofreading or a minor edit, route directly to the existing prose/polishing owner. The protocol must not create a global trigger collision.

## Preflight: premise, evidence, and document scope

Before selecting papers, check the user's premise and the working materials for:

1. false premises or category errors;
2. logic jumps between evidence and conclusion;
3. missing information needed for a defensible claim;
4. unsupported conclusions or causal escalation;
5. section leakage (for example, mechanism in Results or a policy claim without a boundary);
6. whole-document consistency requirements.

For a long document, use this order:

```text
whole-document consistency audit
  -> section-by-section work
  -> cross-section final review
```

Do not accommodate an obviously false premise merely to preserve tone. Record unresolved items as `UNKNOWN`, `NOT_REPORTED`, `NOT_APPLICABLE`, or `NOT_VERIFIED` as appropriate.

## Exemplar selection

Select **3–5 function-matched papers for each substantive section by default**, rather than one fixed set for the entire manuscript. Score and document the reasons using:

`TOPIC_PROXIMITY`, `RQ_PROXIMITY`, `DESIGN_PROXIMITY`, `OUTCOME_PROXIMITY`, `SECTION_FUNCTION_PROXIMITY`, `PLANNING_FUNCTION_PROXIMITY`, `VENUE_RELEVANCE`, `RECENCY`, and `FULLTEXT_AVAILABILITY`.

Journal prestige, IF, JCR, and CAS ranking may be supporting signals only; none may be the sole ranking criterion. A scientifically close, high-quality paper outranks a high-IF paper with a different question or design. When a target journal is known, recent function-matched articles from that venue may be added, but venue fit does not override evidence or design fit.

Source priority is:

1. user-specified verified papers;
2. the project Zotero library or authoritative corpus;
3. verified near-neighbor papers;
4. current web retrieval when necessary.

## Read-scope rules

Every exemplar record must include exactly one primary `READ_SCOPE` value:

| `READ_SCOPE` | Permitted statement |
|---|---|
| `FULLTEXT` | The full text (and supplement when available) was read; article-level structure and section function may be analyzed. |
| `ABSTRACT_ONLY` | Only the abstract was read; use for topic, gap, design, and headline finding orientation. Do **not** claim full-manuscript structure analysis. |
| `METADATA_ONLY` | Only bibliographic metadata was verified; use only for identity, venue, year, and retrieval planning. |

If a source changes from abstract/metadata to full text, update the record rather than silently upgrading a claim.

## Article Story Map schema

Create one map per exemplar or tightly bounded exemplar set. The record may be Markdown, YAML, or JSON, but must preserve these fields:

```yaml
bibliography: "verified parent metadata and source identifier"
read_scope: FULLTEXT | ABSTRACT_ONLY | METADATA_ONLY
selection_reason: []
research_problem: ""
known_evidence: []
specific_gap: ""
why_gap_matters: ""
research_question: ""
study_design: ""
evidence_sequence: []
main_findings_function: ""
discussion_sequence: []
claim_boundary: ""
planning_or_theoretical_function: ""
patterns_to_learn: []
patterns_not_to_copy: []
```

`known_evidence` and `evidence_sequence` summarize source evidence faithfully. They are not a license to transplant the exemplar's claims into the user's manuscript.

## Introduction Move Map

Mark the rhetorical function of each move; do not force a fixed paragraph count:

`ESTABLISH_IMPORTANCE` · `DEFINE_OBJECT` · `NARROW_PROBLEM` · `SYNTHESIZE_PRIOR_STREAM` · `IDENTIFY_LIMITATION` · `ESTABLISH_UNRESOLVED_RELATION` · `EXPLAIN_WHY_GAP_MATTERS` · `STATE_RQ` · `STATE_DESIGN` · `STATE_CONTRIBUTION`.

The map records what a move accomplishes and which verified sources support it. Generic move order may be learned; distinctive wording, citation chains, novelty claims, and unsupported transitions may not.

## Methods Logic Map

Use methods exemplars to learn the logic of reproducibility, not to copy procedures:

`DESIGN` -> `SETTING_AND_POPULATION` -> `DATA_SOURCE` -> `MEASUREMENT` -> `PROCESSING` -> `MODEL_OR_ESTIMAND` -> `VALIDATION_AND_UNCERTAINTY` -> `ETHICS_OR_LICENSING` -> `SCOPE_BOUNDARY`.

Each step must be populated from the user's verified methods. If a source uses a stronger design than ours, retain the difference and prevent design-strength escalation.

## Results Argument Map

Use only the functions that are supported by the user's analysis:

`BASELINE` · `MAIN_PATTERN` · `GROUP_DIFFERENCE` · `SPATIAL_HETEROGENEITY` · `RELATIONSHIP` · `NONLINEARITY` · `INTERACTION` · `ROBUSTNESS` · `SCENARIO_COMPARISON` · `PLANNING_PRIORITY`.

For every figure or result group, record:

```yaml
question_answered: ""
evidence_added: []
why_it_follows_previous_result: ""
claim_enabled: []
claim_not_enabled: []
```

Results should report the core result first, simplify secondary results, and compress repeated patterns without deleting scientifically necessary results. Factual orientation, comparison, and pattern clarification are acceptable in Results; mechanism and causal interpretation belong in Discussion unless the design and section convention explicitly support otherwise.

## Figure Argument Map

For each figure, record its claim, evidence source, sequence role, and boundary:

```yaml
figure_id: ""
question: ""
claim_supported: ""
evidence_source: []
why_this_order: ""
reader_action: ""
claim_not_supported: []
```

Learn figure sequencing logic (for example, context -> design -> core pattern -> heterogeneity -> explanation -> planning implication), but rebuild every figure from the user's data and verified outputs.

## Discussion Move Map

Use the following functions as a menu, not a template:

`KEY_FINDING` · `NEAREST_STUDY_COMPARISON` · `AGREEMENT` · `DIFFERENCE` · `EVIDENCE_SUPPORTED_EXPLANATION` · `THEORETICAL_INTERPRETATION` · `PLANNING_INTERPRETATION` · `BOUNDARY` · `LIMITATION` · `FUTURE_RESEARCH`.

The default evidence-first sequence is:

```text
finding
  -> nearest prior work
  -> agreement or difference
  -> evidence-supported explanation
  -> implication
  -> necessary boundary
```

Keep association, mechanism, and causation distinct. An exemplar's causal language cannot migrate to an observational study without matching design and evidence.

## Claim Ladder

Classify each planned statement by its strongest defensible level:

1. **Observation:** directly reported pattern or estimate.
2. **Comparison/association:** relationship or difference supported by the design.
3. **Evidence-supported explanation:** a mechanism or interpretation supported by measured pathways and appropriate alternatives.
4. **Implication:** a bounded theoretical or planning implication tied to the result and its conditions.

Move down the ladder when evidence, design, scale, measurement, or uncertainty does not support the higher level. Never add a causal claim, result, mechanism, citation, or contribution from an exemplar.

## Rhetorical Function Library

Reusable generic moves include:

- establish why the problem matters, then narrow to the measurable object;
- synthesize a prior stream by agreement, contrast, or unresolved relation;
- state the gap as a missing relationship, measurement, population, scale, or decision use;
- orient a result with a factual comparison before interpretation;
- compare a finding with the nearest design- and outcome-matched study;
- state the implication and immediately preserve the boundary that prevents overgeneralization;
- compress repeated evidence while retaining a necessary null, conflict, denominator, or uncertainty.

These are functions, not reusable sentences.

## Own-evidence-first contract

Before drafting the user's manuscript, complete:

```text
OUR_EVIDENCE_MAP
  -> OUR_ARGUMENT_OUTLINE
  -> EXEMPLAR_COMPARISON
  -> DRAFT
```

The comparison is a diagnostic of organization and rhetorical function. It must never become `EXEMPLAR_TEXT -> synonym replacement -> OUR results`. If the user's evidence map is incomplete, pause drafting or use a clearly labeled structural-only outline.

## Anti-copying contract

### Prohibited

- verbatim copying;
- close paraphrase of distinctive prose;
- sentence-by-sentence mimicry;
- copying citation chains;
- copying another paper's novelty claim;
- copying another paper's causal interpretation;
- copying its result logic when the user's evidence does not support it.

### Permitted

- section function;
- argument ordering;
- generic rhetorical moves;
- evidence presentation strategy;
- figure sequencing logic.

Run a similarity/anti-copying review on any draft that was explicitly benchmarked against named papers. A high textual or distinctive-phrase overlap is a flag for rewrite, not a success criterion.

## Target-journal adaptation and journal recommendation

Target-journal adaptation may learn structure, evidence ordering, discussion strategy, and figure conventions from recent function-matched papers. It may not imitate wording or import the journal's claims. Official journal requirements outrank user preferences in this order:

```text
OFFICIAL_JOURNAL_REQUIREMENT
  > REPORTING_GUIDELINE
  > SCIENTIFIC_CONTENT
  > USER_ABSTRACT_PREFERENCE
```

When recommending journals, do not rank from Title/Abstract alone. When available, use the full manuscript plus the research field, scientific question, gap, contribution, methods, main conclusions, and overall manuscript level. Verify current publisher scope, indexing, IF/JCR/CAS only when verified, OA/APC, recent similar papers, and review time only when reliable. Do not sort by IF alone.

## Preferred empirical abstract profile

`PREFERRED_EMPIRICAL_ABSTRACT_PROFILE` is a soft default only when the target journal has no stricter structured format and the user has not specified another format:

```yaml
background: very short
gap: one compact sentence
study_response: directly answers the gap
methods: mention only one or two central methods
results: prioritize main findings; avoid equal-weight variable-by-variable reporting
implication: one concise final statement
word_count: soft target only; never a hard scientific gate
```

The journal's official format wins over this profile. Do not delete a scientifically necessary null, uncertainty, or boundary to meet a soft length target.

## Failure and degraded modes

| Condition | Safe response |
|---|---|
| No authorized exemplar can be retrieved | Keep `REQUIRED`/`AUTO` as the requested mode, record `EXEMPLAR_UNAVAILABLE`, and proceed only with an evidence-based outline or ask for a source. |
| Abstract or metadata only | Record `ABSTRACT_ONLY` or `METADATA_ONLY`; do not claim full-text structure. |
| Exemplar and user design differ | Preserve the user's design and downgrade the claim ladder; do not migrate causal language. |
| Exemplar findings conflict | Preserve the conflict and avoid consensus language. |
| User premise is false or incomplete | Surface the material issue before drafting; do not optimize prose around the false premise. |
| Journal requirements conflict with profile | Apply official requirement and record the preference as superseded for that task. |
| Exemplar wording is too close | Flag the passage and rewrite from the user's evidence and outline. |
| Humanizer/cleanup skill is absent | Use this protocol plus the prose guard and SciPilot lint; do not create an empty replacement skill. |

## Handoffs

### Handoff to Academic Prose Style Guard

After evidence and argument structure stabilize, hand off to `references/academic_prose_style_guard.md`. The guard remains responsible for positive-first prose, necessary uncertainty, causal/measurement/scope boundaries, and semantic repetition. This protocol does not replace it.

### Handoff to polishing/lint (SciPilot)

`scipilot-writing-skill` remains the final writing and polishing owner. In substantial drafting or major rewriting, it may read the protocol's argument structure and rhetorical-function maps after evidence stabilization. For proofreading, citation-format-only work, and minor edits, it must not force exemplar search.

### Optional companions and metadata hygiene

If a registered `academic-humanizer` skill later becomes available, it is an optional companion after evidence stabilization and before or alongside final prose QC. This repository currently has no such skill. `remove-ai-marks` and `clean-user-facing-text`, if installed later, may handle hidden Unicode, formatting residue, and user-facing normalization through their registered names. Automatic C2PA, provenance, or authorship-marker stripping remains disabled:

```text
ACADEMIC_HUMANIZER_AVAILABLE = NO
REMOVE_AI_MARKS_AVAILABLE = NO
CLEAN_USER_FACING_TEXT_AVAILABLE = NO
PROVENANCE_METADATA_AUTO_STRIP = NO
```

## Public profile schema

The cross-client private profile may contain only reusable preferences under these keys:

`preferred_academic_tone`, `long_document_audit`, `claim_forward_preference`, `results_prioritization`, `abstract_soft_profile`, `punctuation_and_rhythm`, `anti_template_preference`, `journal_exemplar_preference`, and `necessary_boundary_preservation`.

It must not contain absolute personal paths, API secrets, private manuscript text, or copied copyrighted prose.
