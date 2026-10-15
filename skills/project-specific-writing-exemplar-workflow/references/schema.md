# Private State and Exemplar Schemas

The public machine-readable templates live in `templates/`; instantiate them only in the configured private research-project-state hub or private project store. The per-manuscript record is authoritative across Codex and ChatGPT Web. Do not store manuscript-specific instances in this repository.

## Manuscript profile

Use `MANUSCRIPT_WRITING_PROFILE_TEMPLATE_V1.yaml`. Required identity and state fields include `manuscript_id`, `project_slug`, canonical/working title, target journal, research question, design, data, methods, main results, current stage, timestamps, exemplar state, corpus/Core 3/project-skill versions, approval state, state history, source pointers, unknowns, identity status, and private-state URI.

`MANUSCRIPT_ID` must be stable and cannot be only a chat title, filename, or title text. When identity is ambiguous, set `MANUSCRIPT_IDENTITY_UNCERTAIN`; do not inherit any project corpus or skill.

## Master corpus

Use `MASTER_EXEMPLAR_CORPUS_TEMPLATE_V1.yaml`. It defines a candidate pool recommendation of 40–80 and exactly 20 selected records. Every record has source identity/pointer, metadata, manuscript namespace, selection class, source facts, selection rationale, section relevance, full-text status, evidence state, reviewer state, and limitations. Selection weights scientific proximity, design/method relevance, theoretical/planning function, journal relevance, writing quality, and full-text access. IF/JCR/CAS are auxiliary, not ranking proxies.

Evidence states remain distinct: `KNOWN`, `SUPPORTED`, `INFERRED`, `UNKNOWN`, `NOT_AVAILABLE`, `CONFLICTING_EVIDENCE`. Missing information is not a negative finding. Bibliographic truth remains Zotero parent metadata plus the primary source.

## Core 3 decision

Use `CORE3_APPROVAL_TEMPLATE_V1.yaml`. `CORE_3_RECOMMENDED` is not approval. Only explicit author `APPROVED`, `REPLACE_ONE`, `REPLACE_TWO`, or `REJECTED` is persisted. Pending/rejected proposals do not permit deep paragraph/sentence/lexical analysis, final project-skill creation, or major rewrite. Approval automatically continues the lifecycle to deep analysis.

## Section selection and project skill

Use `SECTION_EXEMPLAR_SELECTION_TEMPLATE_V1.yaml`: select exactly 4 or 5 records from the same manuscript's Master 20 for every substantive section request; preserve record IDs, rationale, relevant source sections read, and restored paragraph/sentence/lexicon maps. Use `PROJECT_EXEMPLAR_SKILL_TEMPLATE_V1.md` only as a generic seed for a private manuscript-specific skill after approval and completed quality checks.

No template should contain a fixed global corpus, Core 3, manuscript-specific identity, DOI, private PDF text, or real exemplar selection.
