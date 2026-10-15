# Literature Golden-Set Evaluation Scaffold

The synthetic-only `PAPER_ARTIFACT_AND_WRITING_ROUTING_GOLDEN_SET_V1.json` covers 16 cross-client artifact discovery and per-manuscript routing cases. Run `python scripts/validation/validate_paper_artifact_and_writing_routing.py` to check the fixture and required public contracts. It performs no network requests and contains no real paper or manuscript identifiers.

Do not select papers merely to fill a quota. Build a reviewed 5–8 paper golden set that represents genuine workflow risks.

## Planned cases

1. Simple empirical paper.
2. Methods-heavy paper.
3. Review paper.
4. Paper with supplementary material.
5. Ambiguous citation-support case.
6. Incomplete metadata case.
7. Inaccessible or full-text-missing case.
8. Duplicate Zotero-parent case.

## Evaluation dimensions

- metadata accuracy;
- study-design extraction;
- method accuracy;
- numeric accuracy;
- evidence-trace completeness;
- claim-support classification;
- hallucination rate;
- missingness honesty.

## Case record

Each future case should include:

- stable case ID and source identity;
- licensing/access note;
- input prompt and available artifacts;
- researcher-reviewed expected fields;
- expected evidence locations;
- acceptable uncertainty states;
- forbidden hallucinations;
- scoring rubric and reviewer notes.

## Promotion gate

Do not add broad extraction automation until the golden set is licensed for evaluation, reviewed by a researcher, and shows repeatable performance on metadata, methods, numbers, evidence traces, and missingness honesty.
