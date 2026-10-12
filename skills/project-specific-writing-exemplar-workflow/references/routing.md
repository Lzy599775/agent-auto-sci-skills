# Per-Manuscript Exemplar Routing

The normative state, transition guards, refresh rules, identity handling, analysis protocol, and section-writing order are in the shared [workflow](../../../docs/workflows/PER_MANUSCRIPT_WRITING_EXEMPLAR_WORKFLOW_V1.md) and [state machine](../../../docs/workflows/PER_MANUSCRIPT_EXEMPLAR_STATE_MACHINE_V1.md). Do not fork those rules in a client-specific copy.

## Route

1. Classify substantive writing versus micro-edit. Micro-edits skip heavy initialization; a current skill may provide lightweight style constraints.
2. Resolve `MANUSCRIPT_ID`. If uncertain, do not load or inherit a project skill.
3. Read the single authoritative private state record for this ID. Never reconstruct state from chat memory.
4. If no current active skill exists, initialize this manuscript only and stop at `S4_CORE_3_PENDING_AUTHOR_APPROVAL`.
5. If Core 3 is explicitly approved, automatically continue deep analysis. No second approval is required.
6. If active, select a fresh 4–5 section-matched subset from the same manuscript's Master 20 and reread the relevant source sections before writing.

## Section needs

- Introduction: narrowing, synthesis, gap derivation, RQ transition.
- Methods: question/design alignment, reproducibility, procedure and validation reporting.
- Results: prioritization, evidence order, figure sequence, calibrated report functions.
- Discussion: flexible finding -> prior evidence -> interpretation -> implication -> boundary; no mandatory paragraph count.
- Abstract/Conclusion: journal constraints and bounded synthesis from verified evidence.

Core 3 are prioritized candidates, not a fixed section set. Selection responds to the actual writing problem, evidence structure, journal style, and relevant full-text availability.

The cross-client synthetic cases G01-G15 are in `evals/academic-writing-exemplar/PER_MANUSCRIPT_EXEMPLAR_ROUTING_GOLDEN_SET_V1.json`; they must remain synthetic and must not name or encode real exemplar papers.
