# Cross-Surface Contract

## Canonical workflow source

The authoritative workflow repository is `Lzy599775/agent-auto-sci-skills`.

- Stable ref after V1 merge: `main`.
- Current Draft PR validation ref: `feature/agentic-research-workflow-v1`.
- Current version record: [docs/version.md](../version.md).

ChatGPT and Codex must not independently maintain divergent copies of research principles, workflow routing, evidence standards, reproducibility rules, citation rules, or Zotero boundaries. Those rules remain versioned in GitHub.

## Surface responsibilities

| Surface | Responsibility |
|---|---|
| GitHub repository | Versioned source of truth for instructions, workflows, standards, templates, Skills, evals, and change review |
| Codex repository session | Discover applicable `AGENTS.md`, read the checked-out repository, execute and validate scoped work |
| ChatGPT Project | Persist concise Project instructions, approved files/sources, and Project memory/context where available across chats inside that Project |
| Research Orchestrator Skill | Recognize substantive research goals, retrieve current workflow context, route, hand off, and report QC |
| Plugin | Distribute the Research Orchestrator to supported ChatGPT and Codex surfaces |
| GitHub app/connector | Provide authorized repository data access; it does not by itself make ChatGPT obey `AGENTS.md` |
| Zotero | Remain the bibliographic, attachment, PDF, and indexed-full-text source of truth when available |

## Retrieval contract

At the start of a substantive research workflow, retrieve `docs/version.md`, `AGENTS.md`, `ARCHITECTURE.md`, and `docs/workflows/index.md` from the applicable ref. Load only the selected workflow and standards needed for the task.

If GitHub is unavailable, use only the minimal bundled fallback in the Research Orchestrator and report `WORKFLOW_SOURCE_FALLBACK_USED`. Never imply that fallback rules are the current repository version.

## Write boundary

Repository or source access does not authorize writes. High-risk actions—including publication, destructive data changes, Zotero library changes, submissions, external messages, merges, and force pushes—still require explicit approval.
