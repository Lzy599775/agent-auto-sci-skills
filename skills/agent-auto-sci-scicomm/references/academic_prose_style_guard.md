# Academic Prose Style Guard

**Contract version:** V2

## Purpose and boundary

Run this guard after the scientific content is stable and before final prose or reviewer-risk QC. It applies to manuscript prose, Introduction, Methods interpretation, Results interpretation, Discussion, Conclusion, Abstract, review synthesis, rebuttal prose, and substantial academic interpretation.

This is a writing-quality control, not a primary research router, evidence validator, or permission to weaken a claim. Preserve uncertainty, null results, conflicting findings, causal limits, estimand exclusions, scale limits, and reviewer-relevant caveats. `Style strength <= evidence strength`.

The default rule is:

> PRESERVE SCIENTIFIC BOUNDARIES, BUT DO NOT DEFAULT TO NEGATIVE FRAMING.

## Positive-first discourse order

Prefer the following discourse sequence when a paragraph makes a scientific claim:

`core finding -> interpretation -> mechanism/context -> implication -> necessary qualification`

Do not default to:

`claim -> not X -> cannot Y -> rather than Z -> another limitation`

Start by answering “What does the result mean?” A qualification should follow the result when it prevents a likely misreading. It should not replace the result or become a stack of defensive contrasts.

Example:

- Defensive: `This does not represent a citywide causal effect.`
- Positive-first: `The estimate describes the conditional marginal response within blocks satisfying the predefined support criteria.`
- Necessary boundary, when needed: `It should therefore not be generalized to all city blocks.`

The rewrite must remain faithful to the estimand, population, spatial support, design, and uncertainty actually reported. Do not invent a mechanism or a broader implication to make prose sound affirmative.

## Recast negative boundaries by discourse function

Do not mechanically replace words such as “not”, `cannot`, or `rather than`. Rebuild the sentence around the function of the boundary:

| Boundary function | Preferred move |
|---|---|
| Comparison scope | State how the entities differ, then name the dimension that is insufficient on its own. |
| Estimand or population scope | Define the estimate, population, support, or condition it describes. |
| Method limitation | State the residual uncertainty or unresolved analysis directly and name the next analysis needed. |
| Decision-use boundary | State what the result informs and which contextual decision remains open. |
| Uncertainty scope | State the scenarios, objectives, or combinations covered, then identify the extension required. |
| Intervention classification | Define the dimensions that should remain distinct instead of describing what must not be merged. |

Preferred patterns include:

- `Two measures differ in mechanism and applicability; response magnitude is only one dimension of comparison.`
- `Residual spatial interference requires additional neighborhood or spillover analysis.`
- `The current uncertainty analysis covers the predefined scenarios; broader decision analysis would require additional planning objectives and budget combinations.`

## Necessary negative statements

The following boundaries may remain explicit when they prevent a real scientific error:

- correlation is not causation;
- LST is not air temperature;
- SHAP does not identify causal mechanisms;
- exposure is not equivalent to use;
- accessibility is not equivalent to realized behavior;
- clearly defined estimand exclusions;
- explicit reviewer-risk boundaries.

Even necessary negatives should not be repeated in adjacent sentences. Keep the most precise formulation once, combine boundaries at the same level into one scope sentence, or move the detail to a limitation paragraph.

## Paragraph-level rhythm

For each paragraph, check the discourse functions rather than enforcing a fixed sentence count:

1. topic or claim;
2. evidence or interpretation;
3. mechanism, comparison, or context;
4. implication or necessary qualification.

A paragraph may use fewer or more sentences. The guard should flag a rhythm problem when adjacent sentences repeatedly use defensive forms such as `X does not...`, `Y cannot...`, `This should not...`, `Rather than...`, or their Chinese equivalents. A single necessary boundary is not a defect.

If several caveats address the same level of the argument, keep the most informative one in the main paragraph and consolidate the rest into one scope/limitation sentence. Do not hide a material limitation merely to improve rhythm.

## Lightweight defensive-contrast lint

Scan the local draft after content stabilization. Matching is case-insensitive for English and should tolerate normal punctuation. The following are triggers, not banned words.

Chinese triggers:

`而不是` · `不是` · `并非` · `不能` · `也不能` · `并不能` · `不应` · `无法` · `而非`

English triggers:

`rather than` · `is not` · `does not` · `cannot` · `should not` · `does not imply` · `should not be interpreted as` · `is not equivalent to`

Emit `DEFENSIVE_CONTRAST_CLUSTER` only when local repetition is present, for example:

- at least two trigger matches across three consecutive sentences;
- at least three matches within one paragraph; or
- two sentences within the same paragraph that express the same boundary despite different wording.

One isolated trigger remains an ordinary sentence and should not be flagged automatically. For each flagged span, report the paragraph/sentence location, matched forms, and a short hypothesis about the repeated boundary. Then require human or model review:

A. Is each boundary scientifically necessary?
B. Has the same boundary already been stated nearby?
C. Can the main meaning be expressed affirmatively?
D. Should a caveat move to the limitation or scope paragraph?
E. Can several caveats be merged without losing a reviewer-relevant distinction?

The lint is advisory. It must not auto-delete a caveat, and a resolved cluster may retain negative wording when the boundary is the clearest protection against misinterpretation.

## Semantic repetition audit

After surface matching, compare the meaning of nearby boundaries. Normalize each caveat to its underlying proposition, such as:

`engineering benefit is not identified` -> `the estimate does not establish an engineering intervention benefit` -> `the result should not guide implementation directly`.

When these express one boundary, the main text normally keeps one precise statement, gives the positive interpretation first, and moves any additional operational detail to the limitation or implication paragraph. Do not treat different boundaries as duplicates merely because they use similar negative grammar. Correlation/causation, exposure/use, spatial scale, and decision-use boundaries remain distinct when the evidence requires them.

The semantic audit must preserve:

- causal versus associational status;
- conditional versus universal scope;
- null or conflicting findings;
- measurement and spatial/temporal limitations;
- the difference between evidence absence and evidence of absence.

## Automatic routing as writing QC

When any of the following is generated, invoke this guard after the scientific content is stable:

| Writing route | Required handoff |
|---|---|
| `geors-sci-writing-adapter` | `-> Academic Prose Style Guard` |
| `sport-geography-sci-writing` | `-> Academic Prose Style Guard` |
| `agent-auto-sci-scicomm` | `-> Academic Prose Style Guard` |
| Review synthesis prose | `-> agent-auto-sci-scicomm -> Academic Prose Style Guard` |

The guard does not take ownership of literature search, empirical analysis, review evidence construction, or the primary manuscript route. It is a final discourse-quality handoff after claims, evidence, and scientific boundaries are fixed.

## Regression examples

For each example, preserve the boundary while changing the discourse function. These are regression fixtures for human/model review, not mechanical synonym substitutions.

### A

`ORIGINAL`: 而不是推翻高反射材料的基本辐射机制

`DISCOURSE FUNCTION`: mechanism-preserving qualification

`REWRITE`: The result refines the conditions under which high-reflectance materials operate; their basic radiative mechanism remains the reference process.

`BOUNDARY_PRESERVED = YES`

### B

`ORIGINAL`: 不能仅依据响应幅度把它们视为可互换措施

`DISCOURSE FUNCTION`: comparison scope and applicability

`REWRITE`: Two measures differ in mechanism and applicability; response magnitude is only one dimension of comparison.

`BOUNDARY_PRESERVED = YES`

### C

`ORIGINAL`: 不是完整的绿地空间配置问题

`DISCOURSE FUNCTION`: scope definition

`REWRITE`: The analysis addresses one spatial-allocation dimension of green-space planning; a complete configuration assessment requires the broader set of planning objectives defined for the decision context.

`BOUNDARY_PRESERVED = YES`

### D

`ORIGINAL`: 而不是直接替代实施决策

`DISCOURSE FUNCTION`: decision-use boundary

`REWRITE`: The result provides decision support for implementation, while the final choice remains contingent on the local decision context.

`BOUNDARY_PRESERVED = YES`

### E

`ORIGINAL`: 也不能完全解决潜在空间干扰

`DISCOURSE FUNCTION`: residual methodological limitation

`REWRITE`: Residual spatial interference requires additional neighborhood or spillover analysis.

`BOUNDARY_PRESERVED = YES`

### F

`ORIGINAL`: 没有为所有规划目标和预算组合建立完整概率分布

`DISCOURSE FUNCTION`: uncertainty-analysis scope

`REWRITE`: The current uncertainty analysis covers the predefined scenarios; broader decision analysis would require additional planning objectives and budget combinations.

`BOUNDARY_PRESERVED = YES`

### G

`ORIGINAL`: 而不是继续把所有“增绿”变化合并为同一种处理

`DISCOURSE FUNCTION`: intervention classification

`REWRITE`: Greening changes should be classified by their spatial form, intensity, and implementation context before their effects are compared.

`BOUNDARY_PRESERVED = YES`

## Scientific safety gate

Before accepting a rewrite, verify that it has not:

- removed a causal boundary;
- changed uncertain to certain;
- changed an association into an effect;
- changed a conditional estimate into a universal claim;
- deleted null or conflicting findings;
- hidden a method limitation;
- removed a reviewer-relevant caveat.

If a positive-first rewrite cannot preserve the evidence boundary, retain the negative statement and explain why it is necessary. The guard improves discourse function; it does not optimize away scientific caution.

## V2 story and redundancy audits

The following audits are required for substantial rewriting after the evidence map is stable. They are advisory unless a structural violation is deterministic; they must never erase a necessary scientific boundary.

### `NOT_BUT_CONSTRUCTION_CLUSTER`

The guard treats `不是……而是……`, `并非……而是……`, `不在于……而在于……`, `并不是……`, `而不是……`, `not ... but ...`, `rather than`, `is not ...; instead ...`, `does not ... but ...`, and `not simply ... but ...` as contrastive-template signals. A single necessary contrast is acceptable. Flag a cluster when two occur in one paragraph, two occur in a three-sentence window, the same underlying boundary is repeated across adjacent paragraphs, or the draft develops a document-level fixed template. The action is `WARN/REWRITE`, not mechanical replacement: state the positive core first and retain one precise contrast only when it protects a real comparison, estimand, causal, measurement, uncertainty, or scope boundary.

### `STORY_RELEVANCE_AND_DEFENSE_AUDIT`

For every defensive or qualifying sentence, record:

```yaml
protects_real_boundary: true | false
deletion_changes_estimand_causal_status_population_measurement_scope_or_claim_strength: true | false
already_expressed_nearby: true | false
adds_story_information: true | false
action: KEEP_ONCE | MERGE | DELETE | MOVE_TO_LIMITATION_OR_SUPPLEMENT
```

If a sentence protects no real boundary, changes no scientific interpretation, repeats a nearby boundary, and adds no story information, it is a deletion candidate. If it protects causal status, measurement meaning, uncertainty, conflicting evidence, population, estimand, or decision-use scope, keep the clearest formulation once. This is a review record, not an instruction to make a manuscript sound more confident.

### Sentence academic increment

Classify each sentence or smallest meaning unit as `CORE_CLAIM`, `EVIDENCE`, `METHOD_REPRODUCIBILITY`, `INTERPRETATION`, `ESSENTIAL_TRANSITION`, `NECESSARY_BOUNDARY`, `SUPPORTING_CONTEXT`, or `REDUNDANT_LOW_INCREMENT`. Default deletion applies only to the last category. Preserve nulls, denominators, uncertainty, conflicts, required Methods details, and any caveat that changes how a reader evaluates the result. When a low-increment sentence is removed or moved, record the reason in the transparent change log.

### Paragraph story contribution

Every paragraph must identify at least one contribution to the research question, argument chain, evidence chain, main finding, interpretation, planning/scientific implication, citation synthesis, reproducibility, or necessary boundary. A paragraph that can be removed without changing the scientific story and that carries none of the protected functions is `DELETE` or `MOVE_TO_SUPPLEMENT`. The story audit is subordinate to Methods reproducibility: quiet but reproducibility-critical details stay in Methods or move to a linked supplement.

### Section-level selection

- **Results:** report the main result completely, including necessary numbers, denominators, statistical/spatial evidence, and limited factual orientation; compress secondary results and summarize repeated patterns without adding mechanisms.
- **Introduction:** remove encyclopedic background, ordinary facts, and literature that do not narrow the problem, synthesize the relevant stream, establish the gap, or frame the question.
- **Discussion:** require interpretation, nearest-study comparison, evidence-supported explanation, implication, or a necessary boundary. Do not mechanically replay each Results paragraph.

### Repeated facts and numbers

Use a `FACT_PLACEMENT_LEDGER` to identify the canonical narrative location of sample sizes, counts, time ranges, thresholds, radii, parameters, and effect sizes. Emit `REPEATED_LOW_VALUE_NUMBER` or `REPEATED_FACT_CANDIDATE` when a second occurrence adds no new function, but allow necessary repetition in an Abstract, core Results, self-contained table/figure, or Discussion interpretation. Semantic duplicates with different wording require review; do not equate every repeated number with an error.

### Figure/table citation ledger and order

Maintain a `FIGURE_TABLE_CITATION_LEDGER` with first meaningful introduction, supported claim, and subsequent citations. Remove a later citation when it adds no substantive use (`REPEATED_FIGURE_CITATION = REMOVE`); retain it when a new claim requires the reader to inspect the item again. Check first-citation order, numbering, and caption-text consistency. Figure/table citations are not a substitute for explaining the result.

### Robustness placement

Apply `ROBUSTNESS_PLACEMENT_RULE`: keep sensitivity, robustness, alternative specification, bandwidth, and secondary diagnostic details in the main text only when they are necessary for the main claim, identification credibility, interpretation, or reader evaluation. Otherwise move detail to Supplementary Materials/Appendix and use at most one bounded pointer sentence; omit the pointer if it adds no academic increment. This check must not turn robustness into the paper's central story.

### Table and prose-format contracts

Final tables must satisfy `THREE_LINE_TABLE_CONTRACT`: top rule, header separator, bottom rule, no vertical rules, and trimmed cell text with no leading two spaces or tab. A Markdown table in chat is `CHAT_TABLE = PREVIEW_ONLY`, not proof of a final three-line artifact. Prose must satisfy `NO_MANUAL_LINE_BREAK_IN_PROSE`: no `<br>`, soft/hard Markdown break, U+2028, U+2029, vertical tab, or Word-style manual break. Syntax-required line breaks in code, equations, and table markup are scoped exceptions.

## Source-complete prose checks

- **Referent-aware study wording:** In formal Chinese narration, prefer `本研究` to `本文` when referring to the current study. Do not globally replace `本文` when it refers to the manuscript as a document.
- **Terminology and abbreviation first use:** At first use, give the full term followed by its abbreviation; use the abbreviation consistently thereafter. Audit consistency across Title, Abstract, main text, figures/tables, and Conclusion.
- **Internal labels to prose:** Do not paste internal analysis-table titles, code labels, or operational categories into prose as if they were natural scientific language. Translate them while preserving their defined construct; retain exact labels only when needed and formally introduced.
- **Evidence traceability:** Every major conclusion must link to a result from this study or a verified citation. `[证据边界问题]` may appear only in a working/QC draft and must be resolved and removed before submission-ready text.
- **Hedge calibration:** Keep one most accurate hedge where needed. Flag stacked near-synonymous hedges, but do not remove uncertainty that reflects a real evidence limitation.
- **Causal-boundary placement:** Do not mechanically append a causal disclaimer after every result. State each necessary boundary once at the location that best governs interpretation; retain distinct boundaries that protect different estimands, populations, measurements, or scopes.
- **Non-significant results:** Do not automatically attribute a non-significant result to sample size, low power, measurement error, or model specification. Each such explanation requires additional supporting evidence.
- **Punctuation and noun-chain density:** Review dashes, semicolons, colons, parentheses, Chinese enumeration commas, and quotation marks for overloaded density. Split layered asides when appropriate, not by global replacement. Use quotation marks for terms, direct quotations, or necessary emphasis. Flag unnecessary A-B/A-B-C noun chains while preserving established technical terms and required notation.
- **Symbol preservation:** Editing must preserve formula, variable, and citation-format symbols.

`[证据边界问题]` is never a submission-text substitute for a completed evidence review. It is a temporary QC annotation only.
