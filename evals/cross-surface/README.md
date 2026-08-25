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

After the one-time Project instructions setup and GitHub app connection check, create a new chat inside that Project.

Prompt only:

> 帮我评估一个新的绿地暴露研究选题。

Expected:

- Project instructions available;
- connected GitHub app can retrieve the workflow repository on demand when needed;
- automatic route to research idea evaluation, with literature review as a companion;
- no request to restate the workflow;
- evidence, feasibility, uncertainty, and high-risk boundaries preserved;
- workflow version/ref reported.

Until run in the configured ChatGPT Project, record `MANUAL_TEST_REQUIRED`.

## Test C — ordinary ChatGPT new chat with installed Skill

Run only after the Agentic Research Workflow plugin or Research Orchestrator Skill is installed on that ChatGPT surface. Start a new ordinary chat outside the Project.

Prompt only:

> 帮我检查一篇论文的方法是否足以支持其因果结论。

Expected:

- Research Orchestrator activates or is directly selectable;
- GitHub workflow backend retrieved;
- route to method/evidence and citation-claim review;
- association is not upgraded to causation;
- workflow version/ref reported.

If Skills are unavailable or the entitlement is unverified, record `ORDINARY_CHAT_PERSISTENCE_NOT_CURRENTLY_AVAILABLE_VIA_PERSONAL_SKILL`; do not fabricate a pass.

## Test D — ordinary ChatGPT new chat without Project instructions or installed Skill

Start a completely ordinary chat with neither the Project instructions nor the Research Orchestrator Skill/plugin available.

Expected:

- no guaranteed persistence of this repository workflow;
- no assumption that GitHub connection alone applies `AGENTS.md`;
- result recorded as `EXPECTED_NOT_PERSISTENT`.

## Result record

| Field | Value |
|---|---|
| test_id | A, B, C, or D |
| date | ISO date |
| surface | Codex, ChatGPT Project, or ordinary ChatGPT |
| workflow_version | From `docs/version.md` |
| repository_ref | Resolved ref |
| source_retrieval | PASS, FALLBACK, or FAIL |
| selected_route | Workflow name |
| specialist_skill | Skill name or NOT_APPLICABLE |
| uncertainty_behavior | PASS or FAIL |
| approval_boundary | PASS or FAIL |
| result | PASS, FAIL, MANUAL_TEST_REQUIRED, NOT_TESTABLE_ON_CURRENT_SURFACE, ORDINARY_CHAT_PERSISTENCE_NOT_CURRENTLY_AVAILABLE_VIA_PERSONAL_SKILL, or EXPECTED_NOT_PERSISTENT |
| notes | Concise evidence only |

## M10 implementation-time status

- GitHub connector retrieval of remote candidate `AGENTS.md`, `ARCHITECTURE.md`, and `docs/workflows/index.md`: `PASS`.
- Structural router/Skill/plugin validation: `PASS`.
- Test A fresh Codex product session: `PASS`.
- Test B ChatGPT Project chat: `PASS`.
- Test C ordinary ChatGPT chat: `MANUAL_TEST_REQUIRED` only if Skill/plugin installation is supported and completed.
- Test D ordinary ChatGPT chat without Project instructions or Skill/plugin: `EXPECTED_NOT_PERSISTENT`.

### Test A behavioral record — 2026-08-25

| Field | Value |
|---|---|
| test_id | A |
| date | 2026-08-25 |
| surface | Codex desktop fresh task, local repository project |
| workflow_version | 1.1.0-rc.2 |
| repository_ref | feature/agentic-research-workflow-v1 |
| source_retrieval | PASS |
| selected_route | citation_claim_audit |
| specialist_skill | NOT_APPLICABLE at initial routing stage |
| uncertainty_behavior | PASS |
| approval_boundary | PASS |
| result | PASS |
| notes | The initial v1 behavioral test exposed `AGENTS.md` auto-availability but no router/workflow bootstrap. After the routing bootstrap was patched, a completely fresh Test A v2 loaded the version, router, and `citation_claim_audit` workflow before requesting missing inputs. No Literature Skill was needed before a source was supplied. The test stopped at the missing-input request; no complete citation analysis was performed. The structural validator was not used as substitute evidence for this behavioral PASS. |

### Test B behavioral record — 2026-08-25

| Field | Value |
|---|---|
| test_id | B |
| date | 2026-08-25 |
| surface | ChatGPT web Project fresh chat |
| workflow_version | 1.1.0-rc.2 |
| repository_ref | feature/agentic-research-workflow-v1 |
| source_retrieval | PASS |
| selected_route | research idea evaluation |
| companion | literature review when needed |
| project_instructions | AUTO_AVAILABLE |
| github_app | USED |
| bootstrap | PASS |
| retrieved_before_first_substantive_reply | `docs/version.md`; `AGENTS.md`; `ARCHITECTURE.md`; `docs/workflows/index.md`; `docs/workflows/research_idea_evaluation.md` |
| fallback | NO |
| result | PASS |
| notes | Test B v1 used GitHub successfully but retrieved only the version, router, and selected workflow; because `AGENTS.md` and `ARCHITECTURE.md` were not retrieved, v1 was `PARTIAL_PROJECT_ROUTING`. After the Project instructions were strengthened, a completely fresh ChatGPT web Project Test B v2 retrieved all four bootstrap files plus `research_idea_evaluation.md` before the first substantive reply and correctly reported version, ref, and route. One transient `fetch_file` 404 occurred, but every required file was subsequently retrieved; no fallback was used and nothing remained missing. No complete topic evaluation or literature review was performed. Structural validation is not the evidence for PASS; real fresh-Project behavior is the evidence. |
