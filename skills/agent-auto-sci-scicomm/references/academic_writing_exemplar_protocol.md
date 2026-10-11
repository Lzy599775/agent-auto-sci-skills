# Academic Writing Exemplar Decomposition Protocol

**Version:** V2
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

`preferred_academic_tone`, `long_document_audit`, `claim_forward_preference`, `results_prioritization`, `abstract_soft_profile`, `punctuation_and_rhythm`, `anti_template_preference`, `journal_exemplar_preference`, `necessary_boundary_preservation`, `sentence_academic_increment_audit`, `paragraph_story_contribution_audit`, `methods_reproducibility_priority`, `robustness_placement_rule`, `three_line_table_contract`, `no_manual_line_break_in_prose`, `figure_table_citation_ledger`, and `fact_placement_ledger`.

It must not contain absolute personal paths, API secrets, private manuscript text, or copied copyrighted prose.

## V2 global academic-writing contract

`DEFAULT_ACADEMIC_WRITING_PREFERENCES` is the reusable default for substantive academic-writing routes. It is a workflow contract, not a replacement for a target journal's official requirements, reporting guidelines, author evidence, or researcher judgment. Apply the following precedence:

```text
OFFICIAL_JOURNAL_REQUIREMENT
  > REPORTING_GUIDELINE
  > VERIFIED_SCIENTIFIC_CONTENT
  > NECESSARY_REPRODUCIBILITY
  > DEFAULT_ACADEMIC_WRITING_PREFERENCES
  > USER_SOFT_STYLE_PREFERENCE
```

```yaml
DEFAULT_ACADEMIC_WRITING_PREFERENCES:
  claim_forward: true
  positive_first_when_boundary_preserved: true
  preserve_causal_measurement_uncertainty_scope_boundaries: true
  long_document_order: whole_document_audit -> section_revision -> cross_section_audit
  own_evidence_order: OUR_EVIDENCE_MAP -> OUR_ARGUMENT_MAP -> EXEMPLAR_COMPARISON -> OUR_DRAFT -> PROSE_STYLE_GUARD -> POLISHING
  sentence_increment_audit: required_for_substantial_rewriting
  paragraph_story_contribution_audit: required_for_substantial_rewriting
  methods_reproducibility_priority: higher_than_story_compression
  results_hierarchy: main_result_complete -> secondary_result_compressed -> repeated_pattern_summary_or_supplement
  introduction_relevance: every_paragraph_advances_problem_synthesis_gap_or_question
  discussion_nonrepetition: every_paragraph_adds_interpretation_comparison_explanation_implication_or_boundary
  hidden_formatting_cleanup: AUTO
  provenance_metadata_stripping: EXPLICIT_OPT_IN_ONLY
```

### Preflight and long-document order

Before a rewrite, inspect the premise, evidence map, and document scope for a false premise, logic jump, missing input, unsupported causal escalation, and section leakage. Record unresolved information as `UNKNOWN`, `NOT_REPORTED`, `NOT_APPLICABLE`, or `NOT_VERIFIED`; do not repair a missing fact by inventing prose. For long documents, the required order is:

```text
WHOLE_DOCUMENT_AUDIT -> SECTION_REVISION -> CROSS_SECTION_AUDIT
```

The whole-document audit identifies the research question, claim/evidence chain, repeated facts, figure/table order, terminology, and section boundaries. Section revision then works on the highest-value scientific functions. The cross-section audit checks that abstract, Introduction, Methods, Results, Discussion, Conclusion, figures, tables, and supplements remain consistent.

### Sentence academic increment audit

For substantial rewriting, classify each sentence or smallest meaning unit as one of:

`CORE_CLAIM` · `EVIDENCE` · `METHOD_REPRODUCIBILITY` · `INTERPRETATION` · `ESSENTIAL_TRANSITION` · `NECESSARY_BOUNDARY` · `SUPPORTING_CONTEXT` · `REDUNDANT_LOW_INCREMENT`.

`REDUNDANT_LOW_INCREMENT` is the default deletion candidate. A sentence is not low increment merely because it is short, cautious, or non-narrative: a required Methods detail, null result, uncertainty statement, conflict, denominator, or scope boundary remains protected. The audit must record the reason for a deletion or move rather than silently optimizing for stylistic variety.

### Paragraph story contribution audit

For each paragraph, state which function it serves: `research_question`, `argument_chain`, `evidence_chain`, `main_finding`, `interpretation`, `planning_or_scientific_implication`, `reproducibility`, `citation_synthesis`, or `necessary_boundary`. If removing the paragraph leaves the scientific story unchanged and it does not carry reproducibility, citation synthesis, or a necessary boundary, mark it `DELETE` or `MOVE_TO_SUPPLEMENT`. This check must never delete required Methods information merely because its story contribution is low.

### Results, Introduction, and Discussion selection rules

**Results hierarchy.** The main result receives complete evidence, necessary numbers, denominators, statistical or spatial support, and two or three sentences of factual orientation without adding an unsupported mechanism. Secondary results receive one or two sentences when they change interpretation or answer a declared sub-question. Repeated patterns are summarized or moved to a supplement while preserving a necessary null, uncertainty, conflict, or denominator.

**Introduction relevance.** Each paragraph must advance problem narrowing, literature synthesis, gap establishment, question framing, or a directly necessary context. Encyclopedia-style background, ordinary facts, and citations that do not move the gap are deletion or relocation candidates.

**Discussion nonrepetition.** A Discussion paragraph must add at least one of `INTERPRETATION`, `NEAREST_STUDY_COMPARISON`, `EVIDENCE_SUPPORTED_EXPLANATION`, `IMPLICATION`, or `BOUNDARY`. A paragraph that only restates a Results sentence is a `REDUNDANT_LOW_INCREMENT` candidate. The audit does not prohibit a necessary quantitative reminder when it carries new interpretation.

### NOT_BUT_CONSTRUCTION_CLUSTER

`NOT_BUT_CONSTRUCTION_CLUSTER` is an advisory cluster rule, not a global word ban. Detect these forms in Chinese and English, with ordinary punctuation tolerated:

```text
不是……而是……       并非……而是……       不在于……而在于……
并不是……             而不是……
not ... but ...        rather than          is not ...; instead ...
does not ... but ...   not simply ... but ...
```

Keep one necessary comparison when it protects a real scientific boundary. Emit a warning when the same paragraph has at least two contrastive-defensive constructions, a three-sentence window has at least two, adjacent paragraphs repeat the same boundary, or the full document shows a fixed template pattern. Rewrite from the positive core (for example, “本研究聚焦 Y，并将 X 作为……”); do not mechanically replace words or erase the protected distinction.

### STORY_RELEVANCE_AND_DEFENSE_AUDIT

For every defensive or qualifying sentence, ask:

1. Does it protect a real estimand, causal status, population, measurement meaning, uncertainty, or scope boundary?
2. Would deletion change claim strength, interpretation, or reviewer ability to evaluate the result?
3. Has the same boundary already been stated nearby?
4. Does the sentence add information to the research story?

If no new scientific information is added and the boundary is already protected, mark `DELETE` or merge. If the boundary is necessary, keep the most precise formulation once. This audit is advisory and must not auto-delete a material caveat.

### Methods reproducibility preservation

`METHOD_REPRODUCIBILITY` has priority over `STORY_COMPRESSION`. Preserve details required to reproduce the design or interpret the estimand, including data source, population, measurement, processing, parameters, model, validation, uncertainty, ethics/licensing, and scope. If detail is too long for the main text, move it to a clearly linked Supplement/Appendix; never delete it solely because it does not advance the narrative.

### ROBUSTNESS_PLACEMENT_RULE

For sensitivity analysis, robustness checks, alternative specifications, bandwidth checks, and secondary diagnostics:

- keep the analysis in the main text when it is necessary evidence for the core claim, identification credibility, interpretation, or a reader's evaluation of the main result;
- otherwise place detailed results in Supplementary Materials or an Appendix and keep at most one bounded pointer sentence in the main text (for example, “Results were robust to … (Supplementary …)”);
- omit even the pointer when it adds no academic increment;
- never make robustness or sensitivity the main scientific storyline by default.

### THREE_LINE_TABLE_CONTRACT

For final Word, LaTeX, XLSX, or manuscript artifacts, every table has exactly the semantic equivalent of a top rule, a header separator rule, and a bottom rule, with no vertical rules. LaTeX should prefer `\toprule`, `\midrule`, and `\bottomrule` from `booktabs`. Word should keep only the table top border, header bottom border, and table bottom border. Cell text is trimmed at both ends; a cell may not begin with two half-width spaces, two full-width spaces, or a tab.

Chat Markdown tables are `CHAT_TABLE = PREVIEW_ONLY`: they preview row/column semantics and cannot be claimed to be publication-grade three-line tables. When a DOCX/LaTeX/XLSX/manuscript artifact is requested, convert to its native three-line contract.

### NO_MANUAL_LINE_BREAK_IN_PROSE

Generated prose paragraphs must not contain soft line breaks, manual line breaks, `<br>`, Markdown hard breaks (two trailing spaces followed by a newline), U+2028, U+2029, or vertical tab. Word Shift+Enter equivalents are also prohibited. Normal paragraph boundaries are valid. LaTeX commands, code, equations, and table syntax may contain line breaks required by their grammar; the exception does not apply to ordinary prose text.

### FIGURE_TABLE_CITATION_LEDGER

Maintain a ledger for every `Fig.`, `Figure`, `Table`, `Supplementary Figure`, and `Supplementary Table` with `first_introduction_location`, `claim_supported`, and `subsequent_citations`. Introduce an item completely at the first meaningful location. A later citation is allowed only when a new substantive claim requires the reader to inspect that item again. Otherwise mark `REPEATED_FIGURE_CITATION = REMOVE`. Check first-citation order, numbering, and caption/text consistency; do not introduce Figure 3 before Figure 2 unless the venue explicitly allows it.

### FACT_PLACEMENT_LEDGER

Record a canonical narrative location for concrete facts and numbers, including sample size, street-block/grid counts, time ranges, thresholds, radii, model parameters, and main effect sizes. A low-value exact number or semantically equivalent fact normally appears fully once. Necessary repetition is allowed in an abstract, a core result, a self-contained figure/table, or a Discussion interpretation when it adds a distinct function. Otherwise emit the advisory `REPEATED_LOW_VALUE_NUMBER` or `REPEATED_FACT_CANDIDATE`; do not suppress required reporting mechanically.

### Target-journal recommendations and abstract profile

`EMPIRICAL_ABSTRACT_USER_PROFILE` remains a soft default:

```yaml
background: very_short
gap: compact
study_response: direct_answer_to_gap
methods: one_or_two_central_methods
results: main_findings_prioritized
implication: concise_and_bounded
```

Official journal structure, reporting guidelines, scientific content, and necessary uncertainty outrank this preference. Journal recommendations require full-manuscript analysis when the manuscript is available and should compare scope, research-question fit, recent similar papers, novelty fit, manuscript level, positioning, acceptance plausibility, and verified current metrics. Unverified live data must be labeled `NOT_VERIFIED`; title, abstract, or IF alone is insufficient.

### Hidden formatting and provenance

`HIDDEN_FORMATTING_CLEANUP = AUTO` may remove accidental hidden Unicode and formatting residue as document hygiene. `PROVENANCE_METADATA_STRIPPING = EXPLICIT_OPT_IN_ONLY`. C2PA, XMP/EXIF provenance, authorship provenance, and source metadata must not be removed automatically or merely to evade AI/source detection. The contract does not support AI-detection evasion.

## V2 handoff sequence

For a substantive academic-writing route, the existing owners use this order:

```text
whole-document/story audit
  -> own evidence and argument maps
  -> exemplar protocol (REQUIRED or AUTO; SKIP for minor proofreading)
  -> draft/revise from our evidence
  -> sentence and paragraph increment/story audits
  -> Academic Prose Style Guard
  -> SciPilot polishing and lint
  -> figure/table/fact/section cross-check
```

The route remains an insertion into the existing owner chain. It does not create a duplicate top-level skill or require a user to paste the contract into every Codex conversation.
