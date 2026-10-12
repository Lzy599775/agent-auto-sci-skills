# Literature Review Workflow

## Objective

Build a verified, deduplicated, traceable corpus and a bounded synthesis without creating a competing bibliographic database.

## Pipeline

`query formulation -> search -> deduplication -> eligibility -> metadata verification -> full-text availability -> structured extraction -> evidence trace -> QC -> cross-paper synthesis`

## Procedure

1. Define research question, concepts, inclusion/exclusion criteria, date range, languages, and source types.
2. Record database-specific queries and search dates.
3. Use Zotero for existing library search, bibliographic metadata, PDFs, and citation keys when available.
4. Search authoritative scholarly services for missing or current literature.
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
