---
name: research-orchestrator
description: Route substantive academic and scientific research goals through the current Agentic Research Workflow source of truth. Use for research planning, literature reviews, paper or method analysis, data-analysis planning, paper reproduction, manuscript evidence review, citation verification, figure planning, research idea evaluation, method design, and scientific workflow organization. Do not use for casual conversation, simple arithmetic, generic translation, or unrelated software questions unless repository research rules are materially needed.
---

# Research Orchestrator

Use this Skill as a thin cross-surface router. Retrieve current rules from GitHub, load only task-relevant context, select a specialist workflow or Skill, and report concise QC. Do not duplicate the repository manual here.

## Establish the workflow source

Use `Lzy599775/agent-auto-sci-skills` as the authoritative workflow repository.

- During validation of Draft PR #2, use `feature/agentic-research-workflow-v1`.
- After the validated work is merged, use `main` as the stable ref.
- Retrieve `docs/version.md`, `AGENTS.md`, `ARCHITECTURE.md`, and `docs/workflows/index.md` at the start of a substantive workflow.
- Report the workflow version and ref used.

Read [references/source-retrieval.md](references/source-retrieval.md) for GitHub retrieval, fallback, and version-drift behavior.

## Route the goal

Infer one primary route from the intended decision or deliverable:

- papers, literature, DOI, citations, Zotero, or synthesis -> literature;
- reproduce, replicate, reimplement, or benchmark -> paper reproduction;
- dataset, CSV/XLSX, statistics, regression, or model -> data analysis;
- Introduction, Methods, Results, Discussion, or manuscript -> manuscript writing;
- whether a citation supports a statement -> citation-claim audit;
- plot, map, table, chart, or figure -> figure workflow;
- novelty, feasibility, research topic, or new idea -> research idea evaluation.

Do not require the user to name the workflow. Load the selected file under `docs/workflows/`, then only the standards and specialist Skills required to complete the task.

## Execute with evidence discipline

Apply these minimal fallback invariants on every surface:

- prioritize evidence integrity, reproducibility, and traceability;
- prefer original and authoritative sources;
- never invent citations, identifiers, source text, methods, values, results, or availability;
- separate source-reported fact, derived result, and inference;
- keep claim strength at or below evidence strength;
- preserve explicit unknown, unavailable, unverified, and conflicting states;
- treat Zotero as bibliographic/PDF source of truth when available;
- treat Research Vault records as derived knowledge, not original evidence;
- require explicit approval for destructive, publishing, submission, external-message, merge, force-push, private-data, or destructive Zotero actions.

Read [references/routing-and-qc.md](references/routing-and-qc.md) before finalizing the route or reporting completion.

## Use specialists

Prefer an installed specialist Skill when its scope matches. In particular, use `literature` for evidence-traceable literature search, extraction, synthesis, Zotero work, and citation-support audits. Specialist Skills implement procedures; this Skill owns orchestration and cross-surface source retrieval.

## Handle unavailable GitHub context

If the repository cannot be retrieved:

1. State `WORKFLOW_SOURCE_FALLBACK_USED`.
2. Identify the intended ref and files that could not be verified.
3. Apply only the minimal invariants in this Skill.
4. Avoid claiming the fallback is current or complete.
5. Continue low-risk work when valid; stop only at genuine access, legal, destructive, or material scientific-choice boundaries.

## Return

Report the selected route, workflow repository/ref/version, repository files loaded, specialist Skills used, evidence and uncertainty state, artifacts created, QC results, fallback status, and unresolved blockers.
