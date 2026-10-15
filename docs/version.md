# Workflow Version

- `workflow_version`: `1.1.0-rc.4`
- `contract_schema_version`: `1`
- `stable_branch_after_merge`: `main`
- `current_validation_ref`: `codex/general-purpose-routing-v1`
- `stable_source_policy`: use `main` for released work; use the candidate ref only when explicitly requested
- `last_reviewed_date`: `2026-10-15`

## Reporting rule

Research Orchestrator runs must report the repository ref and workflow version used. `main` is the
stable source for released work. During PR7 validation, `codex/general-purpose-routing-v1` is a
reviewed but unmerged candidate and may be used only when the task explicitly selects it; report
that candidate status. After an approved merge, update `current_validation_ref` to `main` and
continue using `main` as the stable source unless a task explicitly requests another reviewed ref.

Do not use commit hashes as mandatory scientific gates. A commit SHA may be reported when available for audit precision.
