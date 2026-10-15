# Per-Manuscript Writing Exemplar Workflow V1

**Workflow owner:** `agent-auto-sci-scicomm` (existing academic writing owner)
**Polish owner:** existing academic prose guard / `scipilot-writing-skill`
**Project content:** private manuscript-specific state only

## Contract

Pattern libraries record positive-first claim patterns, direct result reporting, comparisons, evidence-to-interpretation transitions, summaries, and qualifications; frequency is never a quality mandate.

The workflow engine is shared; every manuscript has an independent `MANUSCRIPT_ID`, profile, candidate pool, Master 20, Core 3, section exemplar sets, pattern library, and project skill. No fixed global corpus or Core 3 exists. One manuscript must not read another manuscript's private exemplar state unless the user explicitly requests a cross-project comparison. Cross-client field names and invariants are defined in [the state contract template](../../templates/CROSS_CLIENT_MANUSCRIPT_STATE_CONTRACT_V1.yaml); the template is a schema, not storage for live state.

Public repository content is limited to generic workflow, schema, templates, routing, and synthetic tests. Bibliographic facts continue to come from Zotero parent records and primary sources. Derived notes are not substitutes for source text. NotebookLM is an optional full-text synthesis helper, never a required dependency or source of bibliographic/evidence truth.

## Entry routing

This is the automatic companion route for every substantive manuscript-writing request. Invoke it without requiring a named Skill when the user asks to draft/rewrite a substantive section, restructure a manuscript, or adapt it to a journal. In online literature search used to build the candidate pool, apply the paper artifact protocol to all surfaced/shortlisted papers; every Master 20 record must carry a current-enough Level 2 `PAPER_ARTIFACT_RECORD_V1`. Repository/code/data availability is a secondary selection attribute only.

For substantive academic writing, resolve identity in this order: explicit `MANUSCRIPT_ID`; matching private project-state record; canonical title and research question; source-document identity. A chat title, filename, or title string alone is not a durable identity. If identity is ambiguous, set `MANUSCRIPT_IDENTITY_UNCERTAIN`, do not inherit a project skill, and ask only for the minimum disambiguating information after routing.

Substantive triggers include full manuscript work; substantive Introduction, Methods, Results, Discussion, Conclusion, or Abstract drafting/rewrite; target-journal adaptation; major revision; and response-driven restructuring. Typo, grammar-only, citation-format-only, single-sentence micro-edit, and minor caption tasks bypass heavy initialization; an existing project's lightweight style constraints may still be read.

After identity resolution, read that manuscript's one authoritative private state record. The shared state contract is `MANUSCRIPT_ID`, `EXEMPLAR_STATE`, `MASTER20_VERSION`, `CORE3_VERSION`, `PROJECT_SKILL_VERSION`, and `PAPER_ARTIFACT_RECORDS`, namespaced to one manuscript. Codex and ChatGPT Web/Desktop must use the same configured authoritative private state store and versions. Never infer a corpus, artifact status, or approval from chat memory. If the state record cannot be read, report the limitation and do not proceed as though the skill were active.

## Initialization lifecycle

If the manuscript has no current project skill, initialize only that manuscript:

1. Profile the manuscript and assign a stable ID; record research question, design, data, methods, main results, current stage, target journal, and source pointers with unknowns explicit.
2. Discover a manuscript-specific candidate pool, recommended size 40–80. Search in this order where available: the manuscript's cited references, Zotero, a verified literature corpus, target journal, nearest journals, then current scholarly search. Do not reuse another manuscript's 20-paper corpus.
3. Select exactly 20 Master Corpus records using question, object, outcome, design, method, planning/theoretical function, journal relevance, writing quality, and full-text availability. Impact-factor/JCR/CAS fields are auxiliary only; they do not rank exemplars.
4. Recommend a manuscript-specific Core 3 from that Master 20 and present a concise approval packet. No deep paragraph/sentence/lexical analysis or major rewrite occurs before the Core 3 gate.
5. Set `S4_CORE_3_PENDING_AUTHOR_APPROVAL` and stop. The only required author gate is Core 3: approve all, replace one/two with listed Master 20 alternatives, or reject all. A rejection returns to Core 3 recommendation, not an implicit approval.
6. On explicit approval, persist the decision and automatically continue to deep analysis (`S5` -> `S6`); do not ask for another go-ahead. Core 3 receives the highest depth; the remaining 17 receive standard depth. A supporting paper may be promoted to `DEEP_SECTION_EXEMPLAR` when a section need warrants it.
7. Build and privately store the project skill only when analysis and quality checks are complete. Activate it for writing only after the anti-copying, evidence-boundary, author-style, and source-pointer checks pass.

## Corpus and analysis protocol

Each corpus record distinguishes source-reported metadata from selection rationale/inference and carries identity/source pointers, full-text status, evidence state, uncertainty, reviewer status, and version. A source may be selected with partial full text only when the limitation is explicit and its use is bounded. The 20-paper corpus, Core 3, section exemplars, pattern library, and project skill have the same manuscript namespace and independent versions.

Analyze exemplar writing at four levels: (1) article/scientific story—problem, known evidence, synthesis, exact gap, question, method response, evidence sequence, findings, discussion logic, contribution, boundary; (2) paragraph logic—paragraph ID, primary/secondary function, preceding input, new information, evidence role, output to next paragraph, and why it exists/what would be lost if removed; (3) sentence function—claim, background fact, literature evidence, result report/orientation, comparison, interpretation, explanation, summary, gap, RQ, method description/justification, transition, qualification, boundary, implication, or low-information filler; (4) functional lexical/phrase choices—reporting/comparison/stance/interpretation/association/causal verbs, hedges, boosters, transition/summary/contrast/planning markers, scientific collocations, and sentence openings.

Do not treat ordinary word counts (e.g., articles, generic nouns, or field terms) as writing insights. Extract corpus-stable patterns only after independent repetition and quality review; retain a high-quality low-frequency pattern when justified. Frequency is not quality. Explicit author constraints override exemplar frequency, including constraints against mechanical contrasts, defensive disclaimers, and formulaic transitions. Store source pointers and derived functions, not long source passages or distinctive phrases.

## Section writing and selection

For every substantive section task while the project skill is active, choose a fresh set of 4–5 papers from that manuscript's own Master 20. Rank by section-function proximity, the current writing problem, evidence structure, target-journal style, and relevant full-text availability. Core 3 are preferred candidates, not mandatory selections; Introduction and Discussion sets may differ. Before drafting, reread the selected papers' relevant sections and restore their paragraph maps, sentence-function maps, and functional lexicon. Do not rely on a project-skill summary alone.

Fixed writing sequence:

`OUR_EVIDENCE_MAP -> OUR_ARGUMENT_MAP -> SECTION_EXEMPLAR_REFRESH -> STRUCTURAL_COMPARISON -> OUR_DRAFT_OR_REVISION -> ACADEMIC_PROSE_GUARD -> REDUNDANCY_AUDIT -> FIGURE/TABLE_CITATION_AUDIT -> FACT_PLACEMENT_AUDIT -> FINAL_CONSISTENCY_CHECK`

The evidence and argument maps must be built first from the user's verified evidence and scientific logic. Exemplars may calibrate organization; they must not supply scientific logic, facts, values, citations, results, mechanisms, causal claims, or distinctive language. No exemplar-first fill-in-the-blanks drafting.

Section emphasis: Introduction—narrow the problem, synthesize literature, derive the gap and RQ without a fixed broad-background/“few studies”/“this study” template. Results—learn prioritization, evidence and figure sequence, and sentence functions; all numbers and interpretation come from the user's analysis. Discussion—learn the flexible finding -> prior evidence -> interpretation -> implication -> boundary progression without a mechanical five-paragraph formula; judge where to expand, compress, compare, and stop explaining. Methods—learn reproducible design-to-question and procedure reporting, never import another study's procedure. Abstract and Conclusion remain bounded by the manuscript's verified evidence and target-journal requirements.

## Refresh and versioning

Persist `MASTER_CORPUS_VERSION`, `CORE3_VERSION`, and `PROJECT_SKILL_VERSION`. On a changed target journal, materially changed RQ/positioning, major method change, new primary outcome, major reviewer-driven repositioning, or material new literature, set `S9_REFRESH_REQUIRED` and evaluate what needs refresh; do not assume all 20 must be replaced. Corpus age over 12 months is a review prompt, not an automatic expiry. Do not continue using a stale skill as active until the refresh assessment is recorded.

## Private storage and safety

Store project profiles, bibliographic selections, approval decisions, analyses, and manuscript-specific skills only in the private research-project-state hub or an explicitly configured private project state store (for the hub, one `projects/<project_slug>/CURRENT_STATE.md` per manuscript). The single per-manuscript record is authoritative across Codex and ChatGPT Web. Public templates contain placeholders only. Do not modify the manuscript, Zotero, or Obsidian as a side effect of workflow initialization. Preserve primary-source pointers and provenance; keep private PDFs and unpublished content out of this repository.

See [the state machine](PER_MANUSCRIPT_EXEMPLAR_STATE_MACHINE_V1.md), [templates](../../templates/), and [ChatGPT Web router](../chatgpt/CHATGPT_WEB_PER_MANUSCRIPT_EXEMPLAR_ROUTER_V1.md).
