# Academic Prose Style Guard

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
