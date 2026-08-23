# Cross-Surface Evaluation Protocol

These tests verify routing and persistence without writing research data. Record the workflow version/ref, available surface, source retrieval result, selected route, and QC outcome for every run.

## Shared behavioral checks

- Route the research goal without requiring a workflow name.
- Retrieve the stated GitHub workflow ref or disclose `WORKFLOW_SOURCE_FALLBACK_USED`.
- Do not hallucinate repository files or rules.
- Prefer original/authoritative evidence and preserve uncertainty states.
- Keep claim strength at or below evidence strength.
- Stop at high-risk write boundaries.
- Require no repeated bootstrap prompt.

## Test A — Codex fresh task

Start a fresh Codex task with this repository as the primary working directory.

Prompt only:

> 检查一篇文献是否支持论文中的一句话。

Expected:

- applicable root `AGENTS.md` discovered;
- automatic route to citation-claim audit;
- `literature` selected when source retrieval/extraction is needed;
- request for the claim/source only if they cannot be safely discovered;
- current workflow version/ref reported.

Automated structural proxy: repository validator confirms the router, `AGENTS.md`, Literature Skill, and activation case are present. A real fresh-session result must still be recorded before claiming product-surface behavior.

## Test B — ChatGPT new chat inside Project

After the one-time Project instructions/source setup, create a new chat inside that Project.

Prompt only:

> 帮我评估一个新的绿地暴露研究选题。

Expected:

- Project instructions and approved GitHub source available;
- automatic route to research idea evaluation, with literature review as a companion;
- no request to restate the workflow;
- evidence, feasibility, uncertainty, and high-risk boundaries preserved;
- workflow version/ref reported.

Until run in the configured ChatGPT Project, record `MANUAL_TEST_REQUIRED`.

## Test C — ordinary ChatGPT new chat

Run only after the Agentic Research Workflow plugin or Research Orchestrator Skill is installed on that ChatGPT surface. Start a new ordinary chat outside the Project.

Prompt only:

> 帮我检查一篇论文的方法是否足以支持其因果结论。

Expected:

- Research Orchestrator activates or is directly selectable;
- GitHub workflow backend retrieved;
- route to method/evidence and citation-claim review;
- association is not upgraded to causation;
- workflow version/ref reported.

If the Skill/Plugin is not installed, record `NOT_TESTABLE_ON_CURRENT_SURFACE`; do not fabricate a pass.

## Result record

| Field | Value |
|---|---|
| test_id | A, B, or C |
| date | ISO date |
| surface | Codex, ChatGPT Project, or ordinary ChatGPT |
| workflow_version | From `docs/version.md` |
| repository_ref | Resolved ref |
| source_retrieval | PASS, FALLBACK, or FAIL |
| selected_route | Workflow name |
| specialist_skill | Skill name or NOT_APPLICABLE |
| uncertainty_behavior | PASS or FAIL |
| approval_boundary | PASS or FAIL |
| result | PASS, FAIL, MANUAL_TEST_REQUIRED, or NOT_TESTABLE_ON_CURRENT_SURFACE |
| notes | Concise evidence only |

## M10 implementation-time status

- GitHub connector retrieval of remote candidate `AGENTS.md`, `ARCHITECTURE.md`, and `docs/workflows/index.md`: `PASS`.
- Structural router/Skill/plugin validation: `PASS`.
- Test A fresh Codex product session: `MANUAL_TEST_REQUIRED`; this repository is not currently registered as a saved Codex Project, and the packaged WindowsApps CLI executable could not be launched from the validation shell.
- Test B ChatGPT Project chat: `MANUAL_TEST_REQUIRED` after the one-time Project setup.
- Test C ordinary ChatGPT chat: `NOT_TESTABLE_ON_CURRENT_SURFACE` until the plugin is installed and a new chat is started.
