# ChatGPT Web Per-Manuscript Exemplar Router V1

For a substantive academic writing request, use the same contract as Codex:

1. Resolve the stable `MANUSCRIPT_ID` from explicit user input, then the active project's configured private-state path, canonical title/RQ, and source-document identity. If uncertain, mark `MANUSCRIPT_IDENTITY_UNCERTAIN`; never inherit another manuscript's skill or corpus.
2. Read the one authoritative per-manuscript private state record. Do not reconstruct state from chat memory. Codex and ChatGPT Web must use the same record and versions.
3. Load the shared generic workflow and the matching private project skill, if present and current. If absent/stale, initialize only this manuscript through profile -> candidate pool -> Master 20 -> Core 3 recommendation.
4. Stop at `S4_CORE_3_PENDING_AUTHOR_APPROVAL`. Only explicit Core 3 approval is a user gate. On approval, persist the decision and automatically continue deep analysis; do not ask again.
5. If active, select 4–5 manuscript-local exemplars for the requested section, reread the relevant source sections, and build evidence/argument maps before drafting.

NotebookLM may assist full-text synthesis if available. If not, use authorized PDFs/Zotero/local sources; bibliographic truth remains Zotero parent metadata plus primary sources. Tool differences do not change approval, isolation, provenance, or evidence boundaries. Micro-edits bypass the heavy workflow.
