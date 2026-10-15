# Paper Artifact Availability Protocol V1

## Purpose and trigger

This protocol discovers and verifies paper-linked code, data, supplementary material, repositories, and reproducibility resources. Automatically run Level 1 for every paper returned to the user, shortlisted, entered into an evidence table, considered as an exemplar, included in a method comparison, or used in literature-review synthesis. The user need not separately ask for code or data. Do not run it over every raw result in a large literature-monitor feed.

The source hierarchy for scientific claims remains: original paper, supplement, official data/code repository, author repository, then derived AI synthesis. Repository code can clarify implementation but cannot override a paper's methodological claims; a conflict is `CONFLICTING_EVIDENCE` and must be reported rather than silently resolved.

## Tiered discovery

| Stage | Trigger | Required work |
|---|---|---|
| `DISCOVERY_RAW` | All machine/review monitor hits before qualification | No repository deep search; preserve citation identity and screening metadata only |
| Level 1 / `SURFACED` | User-facing result, qualified `HIGH`/review candidate, shortlist/evidence table, method comparison, or synthesis | Check publisher page, supplement links, Data Availability and Code Availability statements; inspect repository links; run bounded web discovery across GitHub, GitLab, Zenodo, OSF, Figshare, Dryad, Dataverse, Code Ocean, institutional repositories, author/lab public repositories, and general web |
| Level 2 / `VERIFIED_READING` | Verified high relevance, reading queue, exemplar candidate, or requested reproduction | Resolve candidate identity and paper linkage; inspect applicable README, citation metadata, archival/release metadata, license, environment, and data manifest; assess apparent reproduction completeness |

The same paper record can advance tiers; record `artifact_audit_level` and `ARTIFACT_SEARCHED_AT`. Re-audit when status is stale under the consuming workflow or when the user requests current availability. Network/retrieval failure is `DEGRADED` and produces `NOT_VERIFIED_DUE_TO_NETWORK`, never `SEARCHED_NOT_FOUND`.

## Search procedure

1. Normalize a canonical paper ID using DOI when verified; otherwise use an authoritative article identifier plus a title/author/year disambiguation record. Do not merge records solely on a fuzzy title.
2. Inspect the publisher's article page and original paper for supplementary files, Data Availability, Code Availability, repository links, article identifiers, and author pointers.
3. Query exact DOI, exact title, DOI + GitHub, title + GitHub, first/corresponding author + title keywords, and article identifier. Search GitHub, GitLab, Zenodo, OSF, Figshare, Dryad, Dataverse, Code Ocean, institutional and author/lab repositories, and general web as applicable. Record which queries/surfaces were unavailable; do not treat a failed source as a completed negative search.
4. Check linked and candidate repositories for DOI/title/authors in README, `CITATION.cff`, Zenodo metadata, release metadata, publisher reverse links, and consistency with the paper's Data/Code Availability statement.
5. Search for supplementary material on the publisher page and linked official repositories. Distinguish no supplement listed from inaccessible, partial, restricted, and broken links.
6. Record source URLs, access date, identity evidence, license evidence, missingness, and conflicts in `PAPER_ARTIFACT_RECORD_V1`. Do not infer absence from an incomplete search.

GitHub and other public repository inspection is read-only. Do not star, fork, issue, PR, upload, or otherwise write. Clone/download only when method inspection or an explicit reproduction task actually requires it.

## Availability states

```text
CODE_STATUS = NOT_SEARCHED | SEARCHED_NOT_FOUND | CANDIDATE_REPOSITORY_FOUND | VERIFIED_PUBLIC | PARTIALLY_PUBLIC | RESTRICTED | REQUEST_ONLY | BROKEN_LINK
DATA_STATUS = NOT_SEARCHED | SEARCHED_NOT_FOUND | CANDIDATE_DATASET_FOUND | VERIFIED_PUBLIC | PARTIALLY_PUBLIC | RESTRICTED | REQUEST_ONLY | BROKEN_LINK
SUPPLEMENT_STATUS = NOT_CHECKED | NONE_FOUND | PUBLIC | PARTIAL | RESTRICTED | BROKEN_LINK
REPOSITORY_IDENTITY = VERIFIED | PROBABLE | CANDIDATE_ONLY | REJECTED
ARTIFACT_SEARCH_STATUS = COMPLETE | DEGRADED
```

`VERIFIED_PUBLIC` means the resource was retrieved/inspected and its paper identity is `VERIFIED`; a merely plausible search hit remains `CANDIDATE_REPOSITORY_FOUND` / `CANDIDATE_DATASET_FOUND`. Use `PARTIALLY_PUBLIC` where only a subset is publicly available. `SEARCHED_NOT_FOUND` requires completed, recorded queries; it does not mean the paper has no resource anywhere. `RESTRICTED`, `REQUEST_ONLY`, and `BROKEN_LINK` are distinct. Code and data statuses are independent. When retrieval/search failure prevents a reliable classification, set `ARTIFACT_SEARCH_STATUS = DEGRADED` and report `NOT_VERIFIED_DUE_TO_NETWORK`, never a negative availability finding.

Repository identity is `VERIFIED` only with direct linking evidence such as DOI/article identifier, title and author match plus a repository citation, archival metadata, publisher reverse link, or explicit paper availability statement. Similar names or topic keywords alone support at most `CANDIDATE_ONLY`; contradictory identity is `REJECTED`. Only `REPOSITORY_IDENTITY = VERIFIED` may support `CODE_PUBLIC_VERIFIED`.

Record `CODE_LICENSE` and `DATA_LICENSE` separately. If no license is found, use `LICENSE_NOT_FOUND`; publicly viewable is not equivalent to open-source or reusable. Do not infer permission from repository visibility.

## Reproducibility status

```text
R0_NO_PUBLIC_ARTIFACT_FOUND
R1_PUBLIC_ARTIFACT_FOUND_UNVERIFIED
R2_PAPER_LINKED_CODE_OR_DATA_VERIFIED
R3_REPRODUCTION_MATERIALS_APPEAR_COMPLETE
R4_PARTIAL_REPRODUCTION_EXECUTED
R5_TARGET_RESULT_REPRODUCED
```

Do not call an artifact reproducible merely because a GitHub repository exists. R2 requires verified paper linkage. R3 requires an inspected bundle that appears to include relevant code/data, documentation, dependencies/environment, and enough inputs/instructions for the stated target; it is an assessment, not an execution claim. R4/R5 require an actual documented execution; R5 requires reproducing the specified target result. Ordinary discovery reaches at most R2/R3.

## Paper artifact record

Create one record per surfaced paper using [the V1 template](../../templates/PAPER_ARTIFACT_RECORD_TEMPLATE_V1.yaml). It records canonical identity, title, DOI, authors, journal, year, search date/tier, publisher URL, supplement/code/data status and URLs, repository identity/owner, code/data license, citation file, archive DOI, release tag, last commit date, environment file, README, data manifest, reproducibility status, verification evidence, and notes. Unsupported fields are `NOT_REPORTED`, `NOT_APPLICABLE`, `NOT_VERIFIED`, or `LICENSE_NOT_FOUND` as appropriate.

## Literature, monitor, and exemplar integration

- A normal online literature search audits all records it surfaces in the user-facing output; display Code, Data, Supplement, Repository identity, License, and Reproducibility resources/status in the result table.
- Automated monitors keep raw discovery cheap. Audit only records when promoted to user-facing/qualified-review/shortlist status (Level 1); move to Level 2 only when verified-high-relevance, reading-queue, exemplar, or reproduction use warrants identity verification.
- Every paper admitted to a manuscript-specific Master 20 has a `PAPER_ARTIFACT_RECORD_V1` at Level 2, including repository identity and license checks; audit is required but does not determine admission. Papers under consideration as exemplar candidates already qualify for Level 2.
- Core 3 ranking is primarily scientific/story proximity, evidence architecture, writing quality, and journal relevance. Code/data access is secondary and cannot automatically promote a paper.
- After Core 3 approval, verified code/data may clarify variable construction, implementation, parameters, or workflow organization; manuscript claims still trace to paper/supplement/evidence, and code-paper conflicts stay explicit.
- Every manuscript independently selects its own candidate pool, Master 20, Core 3, project skill, and section sets. `NO_GLOBAL_FIXED_EXEMPLARS = YES`; no corpus/status/approval is inherited from another manuscript or inferred from chat memory.
- For each substantive section in an active manuscript, select and reread 4–5 function-matched exemplars from that manuscript's Master 20, then build section, paragraph, sentence-function, and functional-lexicon maps. Learn article story -> paragraph logic -> sentence function -> functional lexicon/phraseology, not bare word frequency. Build our evidence and argument maps first.

## Evidence and value boundaries

Availability can increase reproducibility utility or method-learning value only. It does not increase scientific relevance, causal credibility, result validity, or journal quality. Never claim `NO CODE`/`NO DATA` after failed access; report the search failure and `NOT_VERIFIED_DUE_TO_NETWORK`. Keep scientific facts sourced to primary papers/supplements and make repository evidence a separate source type.
