# Evidence Trace Standard

## Canonical evidence unit

| Field | Requirement |
|---|---|
| `claim_id` | Stable project-local identifier |
| `claim_text` | Exact claim being evaluated or supported |
| `source_id` | DOI, Zotero key, dataset ID, repository path, or other resolvable identifier |
| `source_type` | Paper, supplement, dataset, code, documentation, analysis output, or other type |
| `source_location` | Section, page, paragraph, table, figure, supplement, line, or cell range as applicable |
| `evidence_excerpt_or_summary` | Short faithful excerpt or non-distorting summary |
| `support_type` | Classification below |
| `confidence` | `HIGH`, `MEDIUM`, or `LOW` |
| `reviewer_status` | Unreviewed, agent-reviewed, researcher-reviewed, or disputed |
| `notes` | Qualifiers, conflicts, inference boundary, or follow-up |

## Support types

- `DIRECT_SUPPORT`: source directly establishes the claim at comparable strength and scope.
- `PARTIAL_SUPPORT`: only part of the claim, scope, population, or strength is supported.
- `CONTEXTUAL_SUPPORT`: relevant background but not evidence for the exact claim.
- `CONTRADICTORY`: source materially conflicts with the claim.
- `NOT_SUPPORTED`: the cited source does not establish the claim.

## Fact versus inference

Record what the source explicitly reports separately from Codex interpretation. Inferences must name their premises and use an uncertainty state. An evidence record must never imply that an inferred mechanism was directly observed.
