# NotebookLM 0.7.3 to Current Compatibility Audit

**Task:** `NOTEBOOKLM_GEMINI_NOTEBOOK_HOST_MIGRATION_AND_LIVE_READONLY_ACCEPTANCE_V1`
**Workflow:** `literature_review` with `citation_claim_audit` companion (`1.1.0-rc.2`)
**Repository ref:** `analysis/notebooklm-provider-integration-v1`
**Audit date:** 2026-10-12

## Version and environment boundary

| Field | Existing production runtime | Isolated current test runtime |
|---|---|---|
| Wrapper | `notebooklm-skill==1.3.0` | Not installed |
| `notebooklm-py` | `0.7.3` | `0.8.4` |
| Python | `3.13.9` | `3.13.9` |
| Browser / MCP extras | Existing browser install | `notebooklm-py[browser,mcp]==0.8.4`; Playwright `1.63.0`, FastMCP `3.4.2` |
| Runtime location | Existing `%LOCALAPPDATA%\Programs\notebooklm-skill\venv` | Separate `%LOCALAPPDATA%\Programs\notebooklm-py-current\venv` |
| Production mutation | None | Not applicable |

PyPI and the upstream GitHub release endpoint both reported `0.8.4` as current when checked. Release commit: [`bff7c66ef5f353f6e160fc243228786d13905d64`](https://github.com/teng-lin/notebooklm-py/commit/bff7c66ef5f353f6e160fc243228786d13905d64). PyPI declares Python `>=3.10` and the `browser` and `mcp` extras. The old runtime and base Conda environment were not changed.

## Compatibility matrix

| Surface | `notebooklm-py 0.7.3` | `notebooklm-py 0.8.4` | Acceptance implication |
|---|---|---|---|
| Default personal base URL | `https://notebooklm.google.com` | `https://notebook.google.com` | The 0.8.4 default matches the observed Gemini Notebook landing host. |
| Accepted personal hosts | `notebooklm.google.com` only | `notebook.google.com` and legacy `notebooklm.google.com` | The new host is accepted without dropping the legacy host. |
| Accepted enterprise hosts | `notebooklm.cloud.google.com` | `notebook.cloud.google.com` and legacy `notebooklm.cloud.google.com` | Enterprise compatibility is separate from this personal-account test. |
| Login-success detection | Waits up to 300 seconds for `get_base_url()/**`; with no override, the target is the legacy personal host. | `accepted_login_hosts()` / `url_matches_base_host()` accept both personal hosts. | The old timeout is explained by a host mismatch, not evidence that Google login itself failed. |
| Default profile layout | `~/.notebooklm/profiles/<profile>/storage_state.json` and `browser_profile/` | Same profile and browser-profile layout | The current login reused the existing default persistent profile; `--fresh` was not used. |
| Notebook listing | CLI `notebooklm list`; wrapper MCP `nlm_list_notebooks` | CLI `notebooklm list --json`; current MCP has a notebook-list tool | The current CLI path was exercised successfully. |
| Source listing | CLI `notebooklm source list`; wrapper MCP `nlm_list_sources` | CLI `notebooklm source list -n <id> --json`; current MCP has source-list tools | Per-notebook source listing was exercised successfully. |
| Summary | CLI `notebooklm summary`; wrapper MCP `nlm_summarize` | CLI `notebooklm summary -n <id> --json`; current MCP includes chat/read capabilities | Not run because no eligible research notebook was present. |
| Ask and citations | `notebooklm-skill` `nlm_ask(notebook, query)` has no source-ID/filter argument; the wrapper returns answer/reference data. | CLI `notebooklm ask -n <id> --json` documents structured references with source IDs; repeatable `-s/--source` is also available. | This acceptance was specified as a whole-notebook ask and would not use source filtering. No ask was run because no suitable target corpus was present. |
| MCP surface | Wrapper exposes 13 tools; the Codex server retains its pre-existing read-only allowlist. | Current upstream registers notebook, source, chat, notes, Studio, research, sharing, and metadata tool modules, including mutations. | Do not install/register the broad current MCP surface or widen the Codex allowlist as part of this test. |

The current upstream package is not a drop-in dependency replacement for `notebooklm-skill==1.3.0`: that wrapper explicitly pins `notebooklm-py>=0.7.3,<0.8`. Direct use of current upstream CLI/MCP and retaining the old wrapper are distinct options; neither has been promoted to production here.

## Host-migration diagnosis

`HOST_MIGRATION_ROOT_CAUSE=CONFIRMED` for the reported five-minute false-negative. The old environment's `NOTEBOOKLM_BASE_URL` was unset. Its default therefore remained `https://notebooklm.google.com`, its personal-host allowlist excluded `notebook.google.com`, and the login helper waited specifically for a URL under the old default. The user-reported browser landing was `https://notebook.google.com/`. In the isolated 0.8.4 runtime, the same persistent browser profile was recognized as signed in; authentication storage was created, and `notebooklm auth check --test --passive` exited successfully. This confirms that the old host gate caused the reported detection mismatch; it does not claim that every possible account or network failure is ruled out.

No password, cookie value, token, or auth-storage body was inspected or recorded. Only the upstream CLI's normal login and passive auth-check paths were used; the storage file was checked for existence, not opened by Codex.

## Live read-only acceptance

| Gate | Result | Evidence / boundary |
|---|---|---|
| Parallel test environment | `PASS` | Separate venv created and pinned to upstream `0.8.4` with browser and MCP extras. |
| Existing production venv mutated | `NO` | Version check before/after remains `notebooklm-skill 1.3.0` / `notebooklm-py 0.7.3`. |
| Auth storage created | `YES` | Confirmed by file existence only; contents were not read. |
| Auth network check | `PASS` | `auth check --test --passive` exited `0`. |
| Notebook list | `PASS` | `2` notebooks. Titles and IDs are kept only in local private inventory files. |
| Source list | `PASS` | `17` total; `17` ready; `0` processing; `0` failed. Source names and IDs are kept only in local private inventory files. |
| Eligible citation-test notebook | `NO` | Neither existing notebook had at least three ready scholarly/research sources, based on notebook/source title and type metadata. No notebook was created and no source was added. |
| Summary / ask | `NOT_TESTED` | Deferred because no eligible approved research corpus was present. |
| Reference-to-original-passage trace | `NOT_TESTED` | No answer was produced; claim and reference counts are both `0`. |
| Source-verification capability | `PARTIAL` | Host, auth, notebook listing, and source listing work; reference mapping to original passages remains untested. |
| Codex MCP allowlist | `PASS` | Existing read-only allowlist (`list`, `list-sources`, `summarize`, `ask`) and external-research-off default were left unchanged; no current-upstream MCP registration was added. |

The requested `NOTEBOOKLM_LIVE_NOTEBOOK_INVENTORY_V1.json` and `NOTEBOOKLM_LIVE_SOURCE_INVENTORY_V1.json` were generated locally outside the repository. They contain private notebook/source metadata and are intentionally excluded from this public PR. The public record retains aggregate counts only.

## Provider decision

`PRODUCTION_PROVIDER_DECISION=NOT_READY`. Keep the existing production runtime and Codex MCP registration unchanged. The upstream-supported 0.8.4 CLI is the leading candidate for the next controlled test because it recognizes the migrated host and passed auth/list/source checks, but a user-approved research notebook is still required to test `summary`, `ask`, returned references, and at least 10 claim-to-original-passage traces. Until then, neither direct migration nor a wrapper compatibility change is supported by the completed live evidence.

## Reproduction commands (non-mutating paths only)

```powershell
notebooklm login --browser chromium
notebooklm auth check --test --passive
notebooklm list --json
notebooklm source list -n <notebook-id> --json
notebooklm summary -n <notebook-id> --json
notebooklm ask -n <notebook-id> --json "<approved whole-notebook comparison question>"
```

Do not use `--fresh`, source-add/upload/import, notebook create/delete/rename, artifact generation, deep research, or unfiltered MCP registration for this acceptance workflow.
