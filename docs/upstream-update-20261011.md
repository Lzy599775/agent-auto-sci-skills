# NotebookLM provider integration — 2026-10-11

## Change

Audited `claude-world/notebooklm-skill` at commit `dc38bd8106a2c5f23557fc03bf895c53fb19f67e` (`1.3.0`, MIT) and added a thin, optional provider contract for fixed-corpus synthesis. The implementation records the key source-filter limitation (`nlm_ask` accepts notebook and query only), preserves Zotero/original-paper authority, adds source-manifest and citation-verification contracts, and routes an optional helper through the existing literature-review and academic-writing owners.

## Validation

- Repository workflow validation: PASS.
- Source manifest schema and routing JSON: PASS.
- Codex helper skill validation: PASS.
- Public safety scan: PASS.
- Authenticated NotebookLM, account listing, and claim-citation checks: NOT TESTED; require user-performed Google login and an approved existing notebook.

## External runtime

Windows-native isolated install of `notebooklm-skill==1.3.0` with Playwright Chromium is located outside the repository at `%LOCALAPPDATA%\Programs\notebooklm-skill\venv`. Codex has an enabled stdio MCP registration and a narrow user-local `notebooklm-research` skill. No auth flow was run; no notebooks/sources were queried or changed.

## Evolution archive note

This public repository snapshot does not contain the `agent_auto_sci/evolution_archive/evolution_data.json`, its HTML generator, or the project log named in `skills/auto-sci-research/references/04_evolution_archive_protocol.md`. This dated upstream-update record and the audit report are the durable public change record for this branch; no parallel archive structure was introduced.
