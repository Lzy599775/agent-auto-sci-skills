# Workflow Version

- `workflow_version`: `1.1.0-rc.4`
- `contract_schema_version`: `1`
- `stable_branch_after_merge`: `main`
- `current_validation_ref`: `codex/general-purpose-routing-v1`
- `last_reviewed_date`: `2026-10-15`

## Reporting rule

Research Orchestrator runs must report the repository ref and workflow version used. During this
Draft PR validation, use `codex/general-purpose-routing-v1` and report it as an unmerged candidate.
After the validated changes are merged, update the validation ref to `main` in the release metadata
and use `main` as the stable source unless a task explicitly requests another reviewed ref.

Do not use commit hashes as mandatory scientific gates. A commit SHA may be reported when available for audit precision.
