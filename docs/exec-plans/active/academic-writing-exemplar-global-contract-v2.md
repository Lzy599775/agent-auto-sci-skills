# Academic Writing Exemplar and Global Writing Contract V2

## Objective

Extend the V1 evidence-first exemplar handoff into a cross-client academic-writing contract. Map the supplied polishing prompt rules to generic workflow rules, add redundancy/story/format contracts, update Codex and SciPilot routing, and publish a copy-paste Web instruction file plus a private reusable profile.

## Scope

- Public repository: mapping, V2 exemplar/prose-guard protocols, deterministic writing-lint and routing tests, global Web instructions, skill handoffs, and evolution documentation.
- Private repository: only `shared/writing/ACADEMIC_WRITING_PROFILE_V2.md` and `shared/writing/CHATGPT_WEB_ACADEMIC_WRITING_ROUTER_V2.md`; never modify `projects/*` state.
- No new top-level skill and no changes to classifier/runtime, literature monitor, scheduler, Zotero, Obsidian, doctoral state, or Dalian causal state.

## Source and evidence boundary

- The attached task text was read in full. The separately named `润色prompt - 副本.txt` was searched in available workspace roots and was not found; the mapping marks unavailable source-specific claims as `NOT_VERIFIED` rather than inventing them.
- Public artifacts contain generic rules only: no private manuscript text, copied exemplar prose, secrets, or personal absolute paths.
- Provenance stripping remains explicit opt-in only; hidden formatting cleanup may be automatic.

## Implementation order

1. Create the complete rule mapping and V2 contract schemas before code changes.
2. Update the exemplar protocol, prose guard, and skill handoffs.
3. Add deterministic lint checks for advisory clusters, line breaks, cell whitespace, repeated facts/numbers, and figure/table citations.
4. Add routing, redundancy, exemplar, three-line-table, and no-manual-break golden tests.
5. Add the copy-paste global Web instructions and update evolution/docs.
6. Update the private profile and Web router in the V2 private worktree.

## Validation gates

- Existing repository validation plus all new routing/lint/table/line-break/golden tests.
- Python syntax, JSON parsing, `git diff --check`, public safety scan, and install smoke test to the actual Codex skills directory.
- Inspect public and private diffs; confirm only scoped paths changed.
- Report install refresh and Web UI/account-setting boundaries explicitly.
