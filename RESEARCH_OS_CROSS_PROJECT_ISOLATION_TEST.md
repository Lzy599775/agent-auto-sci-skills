# Cross-project isolation test

## Fixture policy

`evals/routing/SYNTHETIC_PROJECT_STATES_V1.json` contains only synthetic PROJECT_A and PROJECT_B
records. They have different manuscript IDs, questions, state, corpus versions, data sources,
and result ledgers. No private paper, real manuscript, or Zotero record is an input.

## Results: 8/8 PASS

1. PROJECT_A reads only `SYNTHETIC_A` and allows writing only after its approved active state.
2. Switching to PROJECT_B reads only `SYNTHETIC_B`; no A values are inherited.
3. Missing identity returns `MANUSCRIPT_IDENTITY_UNCERTAIN` and performs no state read.
4. Method consultation never reads manuscript state, even when an ID is supplied.
5. A language micro-edit remains lightweight and does not initialize a corpus.
6. A mismatched state identity is rejected; an unknown state is not guessed.
7. PROJECT_B's pending Core 3 approval blocks deep writing; boolean/string confusion remains blocked.
8. Artifact identity checks authorize no Zotero write and read no manuscript state.

The evaluator deep-copies returned state and verifies that temporary result-ledger mutation does
not mutate the fixture. This proves the documented synthetic boundary only; it is not a live
private-state backend or a client black-box test.
