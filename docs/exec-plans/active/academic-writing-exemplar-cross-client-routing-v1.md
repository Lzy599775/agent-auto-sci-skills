# Academic Writing Exemplar and Cross-Client Routing V1

## Objective

Integrate an evidence-first writing-exemplar decomposition handoff into the existing writing owners, publish a reusable public protocol, align Codex and ChatGPT Web routing, and create a private cross-project writing preference profile.

## Scope

- Add one reference protocol under `agent-auto-sci-scicomm`; do not add a top-level skill.
- Update `auto-sci-research`, `agent-auto-sci-scicomm`, and `scipilot-writing-skill` handoffs.
- Add the cross-client parity matrix and a 12-case golden set with executable checks.
- Update README, skill map, changelog, and the evolution archive.
- Create only `shared/writing/` files in `research-project-state-hub`; do not modify project state files.

## Safety and evidence boundaries

- Work only in the clean feature worktree created from fetched `origin/main`.
- Preserve the existing literature, classifier/runtime, scheduler, Zotero, Obsidian, and project-state systems.
- Keep public protocol rules generic; do not copy private prompts, manuscript text, or third-party paper prose.
- Treat full-text structure claims as valid only for `READ_SCOPE=FULLTEXT`.

## Validation plan

1. Run the writing-exemplar golden-set validator.
2. Run repository structure/skill checks and `git diff --check`.
3. Run the public-safety scan and inspect absolute-path results.
4. Validate the evolution archive generator and private profile repository diff.
5. Inspect the final staged paths before any commit or push.
