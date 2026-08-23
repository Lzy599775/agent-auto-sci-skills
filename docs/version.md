# Workflow Version

- `workflow_version`: `1.1.0-rc.1`
- `contract_schema_version`: `1`
- `stable_branch_after_merge`: `main`
- `current_validation_ref`: `feature/agentic-research-workflow-v1`
- `last_reviewed_date`: `2026-08-23`

## Reporting rule

Research Orchestrator runs must report the repository ref and workflow version used. During Draft PR validation, use the current validation ref. After the validated changes are merged, use `main` as the stable source unless a task explicitly requests another reviewed ref.

Do not use commit hashes as mandatory scientific gates. A commit SHA may be reported when available for audit precision.
