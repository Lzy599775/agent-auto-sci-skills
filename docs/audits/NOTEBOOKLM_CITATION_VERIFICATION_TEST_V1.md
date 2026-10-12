# NotebookLM citation verification test protocol

## Scope and prerequisites

This is a read-only protocol for a user-approved existing notebook. It does not authorize notebook creation, upload, source import, deletion, artifact overwrite, or deep research. First complete user-driven Google login; never read or expose auth storage, cookies, or tokens. If no suitable approved notebook exists, report `NOT_TESTED` and request an approved target rather than creating one.

## Query

For the existing `notebooklm-skill` wrapper, use `nlm_ask`. For the isolated `notebooklm-py 0.8.4` migration test, use `notebooklm ask -n <notebook-id> --json "<question>"`. Ask it to compare studies' research object, sample/population and size, study period, indicator/exposure, dependent variable, observed versus simulated design, statistical/model method, main finding, and whether the design supports causal or associational interpretation. Require references for each material comparison and retain answer, references, and conversation ID in a local private record.

The 0.8.4 CLI has a source-ID option, but this acceptance query must exercise the whole selected notebook: omit `-s/--source`, `--new`, and `--save-as-note`. The old wrapper's `nlm_ask(notebook, query)` still has no source filter; do not conflate the two contracts.

## Claim-level verification

Select 5–10 material factual claims across the returned answer. For each, record:

| Field | Required value |
|---|---|
| `claim_id` | Stable local identifier |
| `claim_text` | Faithful short claim, not regenerated prose |
| `notebook_reference` | Returned reference object/locator |
| `manifest_match` | Source ID / `UNRESOLVED` |
| `zotero_item_key` | Verified key / `NOT_AVAILABLE` |
| `doi_or_openalex_id` | Verified identity / explicit missing state |
| `original_passage_locator` | Page/section/table/paragraph / `UNRESOLVED` |
| `support_status` | `SUPPORTED`, `PARTIALLY_SUPPORTED`, `UNSUPPORTED`, `AMBIGUOUS` |
| `source_verified` | `YES` only when identity and original passage resolve and support the claim |

If references do not resolve to an original paper passage, set `SOURCE_VERIFIED = NO`, even when NotebookLM returns a citation number. Do not put private full-text excerpts in the public report.

## Pass criteria

- Every important comparison-table cell has a returned reference and source mapping.
- Each verified claim's original passage directly supports the claim at the stated strength.
- Sample, period, design, outcome, exposure, model, and finding are not conflated.
- Zotero/original-source metadata wins any conflict with NotebookLM output.
- Unsupported or ambiguous claims are labeled, removed, or rechecked; they are not silently treated as source facts.

## Current execution status

`NOT_TESTED`: authenticated login, passive auth-network verification, full notebook listing, and per-notebook source listing passed on 2026-10-12 using isolated `notebooklm-py 0.8.4`. The account had two notebooks and 17 ready sources, but neither notebook met the requirement of at least three ready academic/research sources. No summary, ask, or citation trace was run. Request an approved existing research notebook; do not create one or upload sources. Private notebook/source inventories remain outside the public repository.
