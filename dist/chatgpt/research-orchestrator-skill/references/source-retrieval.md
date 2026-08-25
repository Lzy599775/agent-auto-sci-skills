# Workflow Source Retrieval

## Preferred backend

Use the connected GitHub app, connector, or approved repository access to retrieve files from `Lzy599775/agent-auto-sci-skills`.

Retrieve in this order:

1. `docs/version.md`
2. `AGENTS.md`
3. `ARCHITECTURE.md`
4. `docs/workflows/index.md`
5. the selected workflow
6. only the relevant standards and specialist Skill files

During Draft PR #2 validation, use `feature/agentic-research-workflow-v1`. After merge, use `main` unless the user explicitly selects another reviewed ref.

## Access versus instruction

A connected GitHub app provides repository data access. It does not automatically apply `AGENTS.md` as ChatGPT instructions. Retrieve and interpret the workflow context explicitly.

## Version reporting

Report `workflow_version`, repository ref, and—when available—the resolved commit SHA. Do not use commit hashes as mandatory scientific gates.

## Fallback

When GitHub retrieval fails, emit `WORKFLOW_SOURCE_FALLBACK_USED`, state what could not be verified, and use only the minimal invariants in `SKILL.md`. Do not silently substitute cached policy or imply it matches the current repository.
