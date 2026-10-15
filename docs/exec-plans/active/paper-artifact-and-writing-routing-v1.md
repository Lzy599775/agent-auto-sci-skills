# Paper Artifact Discovery and Per-Manuscript Writing Routing V1

## Objective

Add one synthetic-only, cross-client contract that automatically audits publication supplements, code, data, repositories, licenses, and reproducibility resources for qualifying surfaced papers, and ensures substantive manuscript writing enters the isolated per-manuscript exemplar workflow.

## In scope

- Generic paper artifact discovery protocol, record schema, states, and evidence hierarchy.
- Literature-search and tiered-monitor routing, manuscript Master 20 linkage, state-hub interface, Codex Skills, ChatGPT Project/global routers, and synthetic A01–A16 tests.
- No real paper search, corpus selection, manuscript-specific skill creation, manuscript modification, Zotero write, or Obsidian write.

## Sequence

1. [x] Add artifact protocol and record schema with identity, license, availability, reproducibility, and network-failure distinctions.
2. [x] Wire the protocol into literature search, monitor qualification, Master 20 candidate records, and writing-state routing.
3. [x] Update the existing Codex writing/literature owners and thin Project/global routers; preserve unique `agent-auto-sci-scicomm` writing ownership.
4. [x] Add synthetic A01–A16 fixtures and deterministic validators for artifact states, routing, tiering, and manuscript isolation.
5. [x] Run workflow, artifact, per-manuscript, and cross-client validations; review diffs and boundary scans.
6. [ ] Commit scoped changes onto the existing PR #6 branch and update its Draft PR if the safe fast-forward push succeeds. Do not merge. The PR-check connector currently requires a GitHub sign-in, so CI status is not verified here.

## Acceptance gates

- Paper artifact records distinguish search failure, not found, candidate, verified, partial, restricted, request-only, and broken states.
- A repository is linked to a paper only with direct identity evidence; only `VERIFIED` supports `CODE_PUBLIC_VERIFIED`.
- Public visibility is not an open-source license; code/data availability never raises scientific relevance or validity.
- Routine paper search audits surfaced/shortlisted/evidence/exemplar/method-comparison papers; monitors defer Level 1 until qualification and Level 2 until reading/exemplar queue.
- Every Master 20 candidate has an artifact record; Core 3 selection treats availability as secondary.
- Each manuscript has isolated exemplars and private state; substantive writing automatically checks state, while micro-edits skip heavy initialization.
- Project/global routers include both paper-artifact and manuscript-writing routes; all 16 cases are synthetic.
- No real paper, manuscript, Zotero, Obsidian, or private project state is modified.
