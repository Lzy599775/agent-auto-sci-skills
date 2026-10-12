# M11 Cross-Surface Correction and ChatGPT Handoff

## Outcome

Correct the M10 ChatGPT Project/GitHub boundary and export an executable one-time ChatGPT handoff without changing the core workflow architecture.

## Completed scope

- Rechecked current official OpenAI Projects, Skills, and Plugins documentation.
- Removed the unsupported claim that the GitHub repository is a persistent ChatGPT Project source.
- Documented Project instructions + Project memory/context + connected GitHub app + on-demand retrieval.
- Distinguished the portable Research Orchestrator Skill, optional plugin container, and GitHub App connector.
- Recorded current personal ChatGPT Skill installation support as `UNKNOWN` because account entitlement is not observable.
- Marked the repo-local plugin package `LOCAL_CODEX_ONLY` rather than inferring ChatGPT directory availability.
- Added Test D as the ordinary-chat negative control with `EXPECTED_NOT_PERSISTENT`.
- Exported `dist/chatgpt/project_instructions.txt`, the portable Skill directory, and `INSTALL_CHATGPT.md`.
- Kept PR #2 open and Draft; no merge was performed.

## Validation

- Repository validator
- Skill Creator validation for source and exported Skill
- Source/export and source/plugin mirror equality
- Link validation
- Public-safety scan
- Git whitespace and staged-scope review
