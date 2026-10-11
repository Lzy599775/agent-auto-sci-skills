# Optional NotebookLM Research Provider

## Provider identity and precedence

- `ZOTERO = BIBLIOGRAPHIC_AND_PDF_SOURCE_OF_TRUTH`.
- `ORIGINAL_PAPER = SCIENTIFIC_FACT_SOURCE_OF_TRUTH`.
- `NOTEBOOKLM = DERIVED_EVIDENCE_SYNTHESIS_PROVIDER`.
- NotebookLM output is labeled `NOTEBOOKLM_DERIVED_SYNTHESIS`. It may help draft a comparison or locate passages, but it cannot replace source identity checks or verification against the original paper.
- A returned citation is not verified merely because NotebookLM attaches a reference. Set `SOURCE_VERIFIED = YES` only after the reference resolves through the source manifest to an identified source and the referenced original passage supports the claim. Otherwise use `SOURCE_VERIFIED = NO`.

## Allowed role

Use NotebookLM optionally for an already approved corpus: multi-document questions, comparison matrices, research-design comparison, gap mapping, and writing-exemplar structure retrieval. It does not own relevance classification, bibliographic identity, systematic-search completeness, or evidence grading.

For `literature_review`, this is an optional synthesis helper after corpus selection, metadata verification, and full-text availability checks. For academic writing exemplars, use only as `EXEMPLAR_EVIDENCE_RETRIEVAL_PROVIDER`; verify any key full-text passage directly. Keep current argument and evidence owners unchanged.

## Closed-corpus and source-scope contract

- For a fixed-corpus task, use `nlm_ask`; `nlm_research` is OFF unless the user explicitly asks for external discovery or search expansion.
- Closed corpus means `WEB_RESEARCH = OFF` and `SOURCE_ADDITION = OFF`; use only the approved notebook/corpus.
- Pinned upstream `claude-world/notebooklm-skill` v1.3.0 exposes `nlm_ask(notebook, query)` without `source_ids`, `selected_sources`, or `source_filter`. Therefore a prompt that asks for three named studies within a larger notebook is not enforced source isolation: set `PROMPT_ONLY_SOURCE_SCOPE = NON_ENFORCED`.
- For a strict subset, use a dedicated notebook containing only the approved subset, or defer until a source-scoped adapter is implemented and tested. Creating that notebook and uploading sources are external mutations; require explicit user approval first.
- Never bulk-upload a Zotero library. Upload only public papers, user-approved collections/papers, or explicitly approved local files. Unpublished manuscripts, confidential reviews, and collaborator-private files default to `DO_NOT_UPLOAD`.
- Do not create notebooks automatically. Organize any future notebooks by research question, not as one mega-notebook. Capacity is `PLAN_DEPENDENT`, not a hard-coded source-count rule.

## Safe read-only first phase

When authenticated, begin only with auth verification, notebook listing, source listing, summary, and ask. Do not delete, add sources, upload, import research results, generate/overwrite artifacts, or create notebooks unless separately authorized. Do not automatically write or overwrite Obsidian notes.

## Evidence and citation handling

For each important claim or comparison-table cell, preserve the answer reference and resolve:

`NotebookLM answer -> returned reference -> manifest entry -> Zotero/original source identity -> original passage`.

Assign `SUPPORTED`, `PARTIALLY_SUPPORTED`, `UNSUPPORTED`, or `AMBIGUOUS` after source-text review. Citation numbers without a source mapping are not source verification. Bibliographic conflicts defer to Zotero parent metadata plus the actual paper/authoritative registry. Keep sample size, period, design (simulation/observation), outcome, exposure, model, causal status, and finding distinct. Do not present a comparison fact without a reference and source trace.

## Provider status and fallback

Use one of `AVAILABLE`, `AUTH_REQUIRED`, `DEGRADED`, `UNAVAILABLE`. Auth expiry, Google outage, quota, network error, or unofficial API drift must not block Codex, Zotero, literature-review, or writing work. Fall back to original PDFs, Zotero, and local files. Report the unavailable provider briefly and continue.

## Routing

- Explicit requests to use/query the user's NotebookLM may route to the installed `notebooklm-research` provider skill, constrained by this contract.
- Generic “compare these papers” routes to NotebookLM only when the target papers are confirmed in a suitable notebook and the provider is available; otherwise prefer original PDFs/Zotero.
- `nlm_research`, external web search, source import, upload, notebook creation, deletion, and overwrite are never implicit.

## Provenance

Audited upstream: `https://github.com/claude-world/notebooklm-skill`, commit `dc38bd8106a2c5f23557fc03bf895c53fb19f67e`, package `notebooklm-skill` 1.3.0, MIT. This is an unofficial integration using NotebookLM's web API via `notebooklm-py`; availability and behavior can drift.
