# Per-Manuscript Writing Exemplar Workflow V1

## Objective

Turn the existing writing-exemplar protocol into a generic per-manuscript lifecycle with isolated private state, cross-client routing parity, an explicit Core 3 author gate, section-specific selection, and synthetic-only tests. Preserve `agent-auto-sci-scicomm` as the writing workflow owner and the existing prose guard as the polish layer.

## Scope and invariants

- Public changes are limited to generic workflow, schemas, templates, routing, and tests.
- Do not select or approve real exemplar papers, analyze real papers, create a manuscript-specific skill, or edit a manuscript, Zotero, or Obsidian.
- Archive the existing manuscript-specific pilot outputs outside the public repository and label them pilot-only.
- Use one authoritative private state record per manuscript; Codex and ChatGPT Web must read/write that same record.
- All fixtures and golden cases are synthetic.

## Work sequence

1. Audit existing owner contracts, current dirty worktree, private-state destination, and validators.
2. Move only the named pilot outputs and their manuscript-specific plan to a private archive; preserve all unrelated dirty files.
3. Add the generic workflow, state machine, templates, cross-client router, and G01-G15 synthetic golden set.
4. Update the existing owner routing and project-specific workflow skill without creating a competing global owner.
5. Validate schema/routing/golden behavior and run repository workflow validation.
6. Review scoped diffs and report explicit no-selection/no-manuscript-mutation assertions.

## Acceptance checks

- All S0-S9 states, transition guards, refresh rules, identity uncertainty, and per-manuscript isolation are specified.
- The only author gate is Core 3 approval; approval unlocks Phase 2 automatically.
- Each substantive section selects 4-5 exemplars from that manuscript's own 20 and rereads their relevant source sections.
- Micro-edits bypass initialization/deep corpus workflow.
- NotebookLM remains optional; Zotero/primary source pointers remain bibliographic truth.
- The 15 golden cases are synthetic and test routing, isolation, approval, refresh, and fallback.
- No corpus, Core 3, or manuscript-specific skill content remains in the public repository.
