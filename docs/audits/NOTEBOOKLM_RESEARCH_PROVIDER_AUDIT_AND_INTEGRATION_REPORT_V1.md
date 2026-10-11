# NotebookLM Research Provider Audit and Integration Report

**Task:** `NOTEBOOKLM_RESEARCH_PROVIDER_AUDIT_SAFE_INSTALL_AND_WORKFLOW_INTEGRATION_V1`

**Workflow:** `literature_review` (`1.1.0-rc.2`)
**Repository ref:** `analysis/notebooklm-provider-integration-v1`

## Upstream audit

| Field | Verified value |
|---|---|
| `UPSTREAM_REPO` | `https://github.com/claude-world/notebooklm-skill` |
| `UPSTREAM_COMMIT` | `dc38bd8106a2c5f23557fc03bf895c53fb19f67e` (upstream main at audit time; release commit dated 2026-07-18) |
| `UPSTREAM_VERSION` | `1.3.0` (`pyproject.toml`, changelog, release commit) |
| `LICENSE` | MIT |
| `DEPENDENCIES` | `notebooklm-py[browser]>=0.7.3,<0.8`; `fastmcp>=2.13.1,<4`; `python-dotenv>=1.0,<2`; `httpx>=0.27,<1`; `feedparser>=6,<7`; Playwright browser extra |
| `PYTHON_REQUIREMENT` | `>=3.10` |
| `AUTH_METHOD` | User-completed browser Google login via Playwright/browser session; profile-aware local storage |
| `MCP_TOOL_COUNT` | 13 |
| `UNOFFICIAL_API_DEPENDENCY` | YES — NotebookLM web API through `notebooklm-py`; behavior may drift |
| `UPSTREAM_FILES_READ` | README, SKILL, LICENSE, SECURITY, pyproject, install.sh, CHANGELOG, references/api_surface, MCP server/tools, ask/client and auth implementation |

The upstream Bash installer is not used in PowerShell. `nlm_ask` is implemented as `nlm_ask(notebook, query)` and delegates to `client.chat.ask(notebook_id, question=...)`; it has no source-ID/selected-source/source-filter parameter. `nlm_generate` accepts source IDs, but that different operation does not scope `nlm_ask`.

## Safety and integration design

- Provider status: `AVAILABLE`, `AUTH_REQUIRED`, `DEGRADED`, or `UNAVAILABLE`; failures fall back to original PDFs, Zotero, and local files.
- Zotero remains bibliographic/PDF source of truth; original paper remains scientific-fact source; NotebookLM is derived synthesis; Obsidian remains derived knowledge.
- Fixed corpora route to `nlm_ask`; `nlm_research` is OFF absent explicit discovery intent. Upload/source addition/import, notebook creation/deletion, and overwrite are not implicit.
- Prompt-only scope inside a larger notebook is `NON_ENFORCED`. Strict subsets require source-local work or a user-approved dedicated notebook containing only the subset.
- The source-manifest schema and claim-verification protocol are in companion artifacts. Citation numbers without a resolved original passage are not verified.
- No new top-level research owner was added; integration is a thin provider reference routed from existing research/writing owners.

## Windows installation and authentication

The machine exposes Python 3.13.9 through base Conda, no `py` launcher, and `uv` 0.10.9. The canonical worktree was not used for installation. An isolated runtime is installed at `%LOCALAPPDATA%\Programs\notebooklm-skill\venv`, pinned to upstream `1.3.0`; Playwright Chromium and its browser support files installed after one transient network retry. CLI versions and the static MCP registry were verified (`MCP_TOOL_COUNT = 13`). The narrow `notebooklm-research` Codex helper is installed, and `codex mcp get notebooklm-research` confirms an enabled stdio registration pointing to the isolated executable.

Google authentication has not been run. When user browser login is required, state `USER_ACTION_REQUIRED = GOOGLE_LOGIN` and pause. Never read, show, copy, log, commit, or include storage state, cookies, or tokens. No notebook/source query or authenticated account access has occurred.

## Tests and current status

- `WINDOWS_NATIVE_INSTALL`: `PASS` (isolated venv, pinned package, browser installed; no base Conda/project environment mutation).
- `CODEX_SKILL_INSTALLED`: `YES` (`%USERPROFILE%\.codex\skills\notebooklm-research\SKILL.md`; valid under the Codex skill validator).
- `CODEX_MCP_CONFIGURED`: `YES`; transport `STDIO`; Codex CLI confirms enabled registration.
- Source-filter capability: `NO`.
- Prompt-only source-scope enforcement: `NO`.
- Citation resolution/coverage and 5–10-claim verification: `NOT_TESTED` (requires user login and an approved existing notebook plus original source texts).
- Read-only account acceptance (`auth verify`, list notebooks, list sources, summary, ask): `NOT_TESTED` pending user login.
- No notebooks were created; no sources uploaded/imported; no research/deep research, deletion, or artifact overwrite was performed.
- Repository workflow validation: `PASS` (`scripts/validation/validate_research_workflow.py`).
- Source manifest JSON Schema and routing golden-set JSON: `PASS` (schema validates; 10 cases parse).
- Installed helper-skill validation: `PASS`.
- Public safety scan for private absolute paths and token-like patterns: `PASS`; no auth storage was read.
- Public Draft PR: [#5](https://github.com/Lzy599775/agent-auto-sci-skills/pull/5), base `feature/agentic-research-workflow-v1`.
- Public CI: `PASS` (both `Validate Skills` checks completed successfully).

## Companion artifacts

- `skills/auto-sci-research/references/notebooklm_research_provider.md`
- `docs/schemas/NOTEBOOKLM_SOURCE_MANIFEST_SCHEMA_V1.json`
- `docs/audits/NOTEBOOKLM_CITATION_VERIFICATION_TEST_V1.md`
- `evals/routing/NOTEBOOKLM_CODEX_ROUTING_GOLDEN_SET_V1.json`
- `docs/exec-plans/active/notebooklm_provider_integration_v1.md`
- `docs/upstream-update-20261011.md` (evolution/change record; the protocol's external project archive files are absent from this repository snapshot)

## Deferred gate

Controlled live use requires isolated runtime verification, Codex stdio registration/skill setup, repository validation, user-driven Google login, and read-only live testing against an approved existing notebook. No PR merge is authorized.
