# Academic Prose Logic Standard

## Core rule

Academic prose must preserve the logic of the evidence rather than manufacture rhetorical coherence.

Scientific precision has priority over rhetorical smoothness. A slightly abrupt but logically correct transition is preferable to a fluent but unsupported one.

This standard governs how an already bounded scientific claim is expressed in prose. It complements, but does not replace, [Academic Claim Standard](academic_claims.md), which governs whether the claim itself exceeds the evidence.

## 1. Do not manufacture causal relations

Do not add causal, explanatory, or inferential relations unsupported by the study design, analysis, or cited evidence. Association, spatial co-occurrence, feature importance, SHAP values, model prediction, statistical significance, and temporal ordering do not by themselves establish causation, mechanism, or intervention effects.

Treat expressions such as *therefore*, *thus*, *consequently*, *hence*, *because*, *due to*, *lead to*, *result in*, *thereby*, *suggesting that*, and *indicating that*—and their Chinese equivalents—as evidence-bearing language, not decorative connectors. Use them only when the stated inference is justified.

## 2. Do not force sentence-to-sentence logic

Before connecting adjacent sentences, identify their actual relation: continuation, comparison, contrast, elaboration, evidence, interpretation, causal inference, implication, or `NONE`.

`NONE` is valid. If no defensible relation exists, keep the sentences sequential instead of inventing one.

## 3. Allow zero transition

Prefer content-driven progression to explicit discourse markers. Do not automatically insert *moreover*, *furthermore*, *additionally*, *meanwhile*, *however*, *therefore*, *notably*, *importantly*, or *in contrast*.

Retain a discourse or emphasis marker only when it expresses a real, necessary, and supported logical relation or salience judgment.

## 4. Control defensive writing

Add anticipatory qualification only when it communicates a genuine uncertainty, limitation, alternative explanation, inferential boundary, or reviewer-relevant ambiguity. Necessary qualification protects accuracy and must be retained; generic self-protection does not.

Avoid default constructions such as *it should be noted that*, *it is important to emphasize that*, *this does not necessarily mean that*, *this should be interpreted with caution*, *the present study does not attempt to*, and *it cannot simply be assumed that*. Do not manufacture an objection merely to rebut it.

## 5. Control parallel structures

Do not default to three-part lists, balanced triads, repeated *not only ... but also ...*, *on the one hand ... on the other hand ...*, or symmetrical sentences. Use coordination only for elements at the same logical level.

Do not present an empirical finding, methodological action, theoretical interpretation, and planning implication as equivalent categories.

## 6. Remove semantic repetition

Adjacent sentences must not merely paraphrase one another. Each sentence should contribute an identifiable function, such as a new result, comparison, condition, quantitative detail, evidence, interpretation, limitation, or implication. Remove restatements that add no scientific information.

## 7. Prevent missing-premise jumps

Before moving from a result to an interpretation, mechanism, recommendation, or planning implication, test any proposed `A -> B` relation:

1. Does `A` support `B`?
2. Does the inference require an unstated premise `C`?
3. Is `C` supported by the present analysis, theory, or cited evidence?

If a required premise is missing or unsupported, do not write `A` as implying `B`.

## 8. Keep model interpretation distinct from mechanism

Feature importance, SHAP, partial dependence, local importance, prediction accuracy, and other machine-learning interpretations describe model behavior unless the research design establishes more. Without additional evidence, do not recast them as a real-world causal mechanism, intervention effectiveness, behavioral response, or policy effect.

## 9. Avoid formulaic paragraph architecture

Do not force every paragraph into a topic sentence, three supporting statements, and a conclusion. Let the evidence and argument determine paragraph structure. Do not append a concluding glue sentence that only restates the paragraph.

## 10. Audit sentence-pair logic

Before finalizing a paragraph, inspect every adjacent pair (`S1 -> S2`, `S2 -> S3`, and so on):

1. Identify the intended relation.
2. Verify that the evidence supports it.
3. Check whether the connective strengthens it beyond that support.
4. Remove the connective when it is unnecessary.

## 11. Apply the rhetorical-strength gate

Writing must preserve this ordering:

`Evidence strength -> Claim strength -> Logical-relation strength -> Linguistic strength`

No downstream layer may exceed the layer above it. Weak or exploratory evidence must not become strong causal or mechanistic language.

## 12. Apply the deletion test

During revision, ask whether deleting a sentence removes a scientific, methodological, interpretive, or necessary navigational function. If it removes none of these, the sentence is likely rhetorical filler and should normally be deleted.

## 13. Use natural syntax

Vary sentence length and syntax only as informational load requires. Do not manufacture variation, and avoid repeating the same grammatical template across consecutive sentences or paragraphs.

## 14. Apply the standard by section

- **Introduction:** Separate established evidence, the unresolved gap, and study motivation. Do not manufacture a gap through rhetorical contrast.
- **Methods:** Prioritize procedural precision. Avoid persuasive or evaluative transitions.
- **Results:** Report findings before interpretation. Do not add unsupported mechanisms, causes, implications, or literature comparisons.
- **Discussion:** Permit interpretation while keeping evidence, inference, alternative explanations, limitations, and implications distinguishable.
- **Conclusion:** Synthesize only claims supported elsewhere in the manuscript. Do not strengthen causal, mechanistic, or policy language beyond the Results and Discussion.

## 15. Run the final prose audit

Before treating manuscript prose as final, ask:

1. Did wording introduce a causal relation absent from the evidence?
2. Was a connective added where no logical relation exists?
3. Do adjacent sentences repeat the same information?
4. Do parallel structures combine elements from different logical levels?
5. Is defensive qualification present without a genuine inferential need?
6. Does any sentence function only as rhetorical glue?
7. Was model interpretation escalated into a real-world mechanism?
8. Does a result-to-implication transition skip an unsupported premise?

Revise before finalization if any answer is yes.
