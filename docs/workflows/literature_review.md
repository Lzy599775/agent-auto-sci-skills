# Literature Review Workflow

## Objective

Build a verified, deduplicated, traceable corpus and a bounded synthesis without creating a competing bibliographic database.

## Pipeline

`query formulation -> search -> deduplication -> eligibility -> metadata verification -> full-text availability -> structured extraction -> evidence trace -> QC -> cross-paper synthesis`

## Zotero-first, current, and venue-aware discovery

Use this order automatically for every actual scholarly-paper search, including literature discovery supporting another workflow. This is a source-discovery priority; scientific eligibility and evidence validity govern the final corpus. Do not transfer a collection or manuscript state between projects.

1. **Inspect Zotero first (read-only).** Run a narrow search in the accessible library/selected collection using the research concepts and synonyms, then exact DOI/title/author for known papers. Inspect parent metadata, citation identity, and existing attachments/full text as relevant. Record `IN_ZOTERO`, `NOT_FOUND_IN_SEARCHED_SCOPE`, or `ZOTERO_UNAVAILABLE` with the scope checked; a scoped miss does not establish absence from every collection. Do not run a large inventory if a targeted search suffices. Zotero is the existing-library index, not proof that a paper is scientifically valid or up to date.
2. **Search authoritative external sources independently.** After Zotero, formulate precise bilingual/field-appropriate search terms from the actual research question, variables, population/context, study design, and outcome. Search publisher/journal pages, DOI/Crossref/OpenAlex, PubMed or other discipline-specific indexes as applicable. Use both (a) searches targeted to preferred journals and (b) a broader field-wide search to catch relevant studies elsewhere; refine terms and record search date, query, and source. Derive the query vocabulary from established terminology in verified relevant article titles, abstracts, author keywords, and subject indexing; use documented synonyms to improve retrieval. Do not invent a search label and present it as a recognized disciplinary term. Match words to the actual measured construct. External discovery remains required when the task asks for new/latest research even if Zotero already contains relevant papers.
3. **Prioritize publication freshness.** First inspect genuinely recent items, normally the rolling previous 12 months (including verified online-first dates); extend the evidence sweep across the preceding 3–5 years and include older foundational or uniquely relevant papers where scientifically necessary. Adapt the lookback to the question, especially systematic reviews, historical claims, or slow-moving fields. Verify online publication dates, article year, DOI, and corrections/retractions rather than assuming search rank means newer.
4. **Use these venue preferences for urban/built-environment/planning/landscape/heat-exposure research, when the scope fits:**
   - **First targeted sweep:** `Nature`, `Science`, relevant Nature-family research journals (e.g., `Nature Communications` / NC, `Nature Cities`, `Nature Sustainability`, `Nature Climate Change`), `Science Advances`, and `Proceedings of the National Academy of Sciences` (PNAS). PNAS is a separate journal, not a Nature-family title; do not infer equal selectivity or scope from inclusion in the same search priority.
   - **Field-journal sweep:** `Landscape and Urban Planning` (LUP), `Sustainable Cities and Society` (SCS), `Environmental Impact Assessment Review` (EIAR), `Urban Forestry & Urban Greening` (UFUG), `Urban Climate`, and other journals matched to the question and scientific standard (such as `Building and Environment`, `Cities`, or relevant environmental-health journals). These are search preferences, not a fixed impact-factor or universal prestige ranking.
   - **Other disciplines:** For stand-alone sports, medicine, aging, statistics, and other projects, select comparably rigorous **discipline-relevant** journals based on that project's question; do not impose the urban-planning journal list. An explicit user-specified venue or journal list overrides this default.
5. **Screen and rank by evidence fit.** Assess question/concept match, design and measurement comparability, methods and results, verifiability, study limitations, then recency and venue suitability. Never exclude a highly relevant study solely because its journal is outside the preferred list; never favor an irrelevant high-profile paper over a relevant robust one. Deduplicate Zotero and web results by verified DOI/identifiers; distinguish papers already held from newly found items.
6. **Report a compact, verifiable shortlist.** For material candidates provide journal, exact DOI/identifier, verified online/publication date when available, topic/method fit, Zotero presence, full-text/attachment status, and whether the result came from existing library or external search. Treat metadata-only hits as metadata-only; apply the existing paper-artifact protocol when a paper is surfaced. If Zotero cannot be reached, continue external search and disclose `ZOTERO_UNAVAILABLE`; never claim the library was checked. Avoid persisting duplicate PDFs, large inventories, or separate PASS/FAIL logs by default.

## Procedure

1. Define research question, concepts, inclusion/exclusion criteria, date range, languages, and source types.
2. Record database-specific queries and search dates.
3. Use Zotero for existing library search, bibliographic metadata, PDFs, and citation keys when available.
4. Search authoritative scholarly services for missing or current literature.
   - For every paper surfaced to the user or promoted to a shortlist, evidence table, method comparison, exemplar candidate, or synthesis, automatically run [Paper Artifact Availability Protocol V1](PAPER_ARTIFACT_AVAILABILITY_PROTOCOL_V1.md). Do not deep-search unqualified raw monitor hits; apply its tiered trigger rules.
5. Deduplicate using DOI first, then authoritative identifiers and title/author/year checks.
6. Verify metadata against the original source or authoritative registry.
7. Classify full-text status as available, partial, inaccessible, or not sought.
8. Extract only supported fields into `templates/paper_note.md`; preserve explicit missing states.
9. Create claim-level records using `templates/evidence_record.md`.
10. Run metadata, design, numeric, and citation-support QC before synthesis.
11. Synthesize agreements, heterogeneity, mechanisms, limitations, and evidence gaps without flattening study differences.

## Zotero boundary

- Zotero: bibliography, parent metadata, attachments, citation keys, full text.
- Research Vault: derived notes, evidence records, comparisons, and synthesis.
- Do not import, edit, or delete Zotero records without explicit authorization.
- Do not copy PDFs into the Research Vault by default.

## Outputs

- Search log and eligibility criteria.
- Verified corpus inventory.
- Paper notes and evidence records.
- QC findings.
- Cross-paper synthesis with uncertainty states.
- For each surfaced paper, a `PAPER_ARTIFACT_RECORD_V1` and a result row covering code, data, supplement, repository identity/license, and reproducibility resources. Network failure is `NOT_VERIFIED_DUE_TO_NETWORK`, not a negative availability finding.
