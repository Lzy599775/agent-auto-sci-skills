# NotebookLM provider audit and controlled integration

## Objective

Evaluate the pinned `claude-world/notebooklm-skill` release and integrate it as an optional, non-authoritative synthesis provider for approved fixed corpora. Keep the canonical checkout and research data untouched.

## Boundaries

- Work only in task branch `analysis/notebooklm-provider-integration-v1`.
- Treat NotebookLM as derived synthesis; Zotero and original papers remain source of truth.
- Never read, display, copy, log, commit, or report auth state, cookies, or tokens.
- No notebook creation, source upload, deletion, deep research, Obsidian/Zotero/monitor/scheduler/classifier mutation.
- Use only Windows-native isolated runtime and Codex stdio MCP, if supported.
- Stop for user-performed Google login before authenticated notebook tests.

## Phases

1. Pin and audit upstream files, dependencies, auth, MCP operations, ask source-filter contract, and Windows installation boundary.
2. Inspect Codex MCP CLI contract and existing server names without reading secret config values; verify isolated runtime options.
3. Add the provider contract, manifest schema, citation test protocol, routing golden set, integration references, license ledger, audit report, and evolution record.
4. Install into an isolated Windows environment; register the Codex skill/MCP only after checking for conflicts. Completed: package 1.3.0, Playwright Chromium, Codex skill, and stdio MCP registration.
5. Run non-authenticated checks, repository validation, routing/evidence tests, and public safety scans. Offline checks passed. Pause for user Google login before read-only live NotebookLM validation.
6. Review diffs and report exact completed/deferred states; do not merge.
