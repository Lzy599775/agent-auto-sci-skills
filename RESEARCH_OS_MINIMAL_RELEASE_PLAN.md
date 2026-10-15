# Minimal release plan

## Allowlist

The candidate consists of 35 explicitly listed paths: 23 modified tracked files and 12 new
files, including five requested reports. The 30 source/fixture/plan files and their hashes
are listed below; the reports are listed separately to avoid a self-referential checksum.
No existing dirty PR worktree files, release checkout files, `.installer-smoke`, credentials,
private data, caches, or generated research outputs are in scope.

## Suggested review sequence

1. Review `docs/workflows/methodology.md` and `docs/workflows/index.md` for route semantics.
2. Review `ROUTING_DECISION_CONTRACT_V1.json` and the synthetic A–M/PROJECT_A-B fixtures.
3. Review the Orchestrator mirrors and ChatGPT parity documents.
4. Re-run the listed validators in `RESEARCH_OS_GENERIC_ROUTING_TEST_REPORT.md`.
5. Perform real fresh-client tests with no Skill-name prompt and record file/tool evidence.
6. Only after author approval, choose a release version/commit and open a Draft PR.

## Not authorized in this candidate

No commit, push, merge, installer refresh, ChatGPT settings update, production monitor/classifier
change, Zotero/Obsidian write, worktree deletion, cache cleanup, or destructive Git operation.

## Rollback

The patch is uncommitted. Leave this isolated worktree intact if review finds a conflict and
prepare a corrected patch here; do not reset or clean either original checkout. After a future
approved release, rollback should be a separately reviewed revert commit.

## Exact allowlist and source identity

Base and final remote-main query both returned
`d5e913f07f9b7ea8d3666cb28fcacc0232c912fa`. An intermediate query had a connection reset;
a later read-only retry succeeded. There was no fetch, branch update, commit or push.

```text
.agents/plugins/plugins/agentic-research-workflow/skills/research-orchestrator/references/source-retrieval.md
SHA256 = A3DC3E59DEE7B05283888CCDB6E55CC04C627048BB819D6D8CE3E4291C128DD7

.agents/plugins/plugins/agentic-research-workflow/skills/research-orchestrator/SKILL.md
SHA256 = 6BB93F8838074D149D0CF909E57FD4172CCADAEBEFCB8C301411A85D0D6D4155

.agents/plugins/plugins/agentic-research-workflow/skills/research-orchestrator/tests/activation_cases.md
SHA256 = F724524F7E45F2B3963F4584BF5460860544B5AED7981E571B27A3AB3E1267A9

.github/workflows/validate.yml
SHA256 = 30F75CB3BD7C9707361089C8DD20D2E6771813D4A7B81D45EA720350D9F52578

dist/chatgpt/INSTALL_CHATGPT.md
SHA256 = 26FEEDD8201AD4BA771A2D6BAF2301A53BEC20963B2848610CE90DE75E40E877

dist/chatgpt/project_instructions.txt
SHA256 = A837BA45BFBF0BDD6F24BBF06CA7B4064CE7D3D0F6EAD519F5740D242BB3EC3C

dist/chatgpt/research-orchestrator-skill/references/source-retrieval.md
SHA256 = A3DC3E59DEE7B05283888CCDB6E55CC04C627048BB819D6D8CE3E4291C128DD7

dist/chatgpt/research-orchestrator-skill/SKILL.md
SHA256 = 6BB93F8838074D149D0CF909E57FD4172CCADAEBEFCB8C301411A85D0D6D4155

dist/chatgpt/research-orchestrator-skill/tests/activation_cases.md
SHA256 = F724524F7E45F2B3963F4584BF5460860544B5AED7981E571B27A3AB3E1267A9

docs/chatgpt/CHATGPT_GLOBAL_RESEARCH_OS_ROUTER_V1.txt
SHA256 = D0A07A455401F94412081F9BE2DBF0E48BACCE07EBAC7DBBE26202F287AB230E

docs/chatgpt/CHATGPT_PROJECT_RESEARCH_OS_ROUTER_V1.md
SHA256 = 0402CC09F9319B58CD9676BB639863017CA7410C6B9B522383DD625D593434F7

docs/chatgpt/cross_surface_contract.md
SHA256 = 9E4EBD0C49CFC08167BDDDCD2B1677BDD2D12E74F3A741A9633B773778D88E9B

docs/chatgpt/project_instructions.md
SHA256 = 91DBAE5249632C01319D00B70E053FBB5EC7C774EBE98B43192C9FE6B585295B

docs/exec-plans/active/general-purpose-routing-completion-v1.md
SHA256 = D605F682450C7DA42903A6AA5DA104653EB259F02BCEDA12071C9A26E351C58F

docs/index.md
SHA256 = 1C6F9B20D22C00BE5699A76A8A52EE89A2D0D1F78406CF0AC517D3BAFED73302

docs/skill-map.md
SHA256 = B98D6F340EC0DF867E60329139B4227DC0E2ADC56A6B9242EBB5440B63F15126

docs/workflows/data_analysis.md
SHA256 = 2983010C78ACC766B3B564C5BE4B71E569C89D6180B993B2E856979D03FCE196

docs/workflows/index.md
SHA256 = 3E4197B5D472BFBA3E53F099A4F7E5B64ECDFF234C5371859310C5B04FB48DFC

docs/workflows/methodology.md
SHA256 = 00C4A2EAF5A1D6CA97FE6D2ABE36A3FC32AC4E0E871A62B613396878A030B1FD

docs/workflows/ROUTING_DECISION_CONTRACT_V1.json
SHA256 = 03875B958636D2CCC52D448666B04705752179A1B71EF02C4AC47D94B71EF0DB

evals/routing/GENERAL_PURPOSE_ROUTING_GOLDEN_SET_V1.json
SHA256 = 5A38302732A709734AE7BF0800CEA1808A16C7EEECC6556CE4822F06762A089E

evals/routing/SYNTHETIC_PROJECT_STATES_V1.json
SHA256 = D7531916CB03CCF4F02D8A47B20347E054F0E9D72657F5656B684F6F7686C3A4

scripts/validation/test_generic_research_routing.py
SHA256 = 88A2E8076B15F672B4325D901F44E05C9B4ED543DB8999DD16D106A93478B3E7

scripts/validation/validate_generic_research_routing.py
SHA256 = 3E4FD6A3F1562CBC9B4F02DF11C5E2ADDBAA47D02F429917EE7FACF1AB0F06A2

scripts/validation/validate_research_workflow.py
SHA256 = 038A4CC222B043C50B04DFBAC2CAA4DAF2D121047EBA80152944B108E49F6894

skills/research-orchestrator/references/source-retrieval.md
SHA256 = A3DC3E59DEE7B05283888CCDB6E55CC04C627048BB819D6D8CE3E4291C128DD7

skills/research-orchestrator/SKILL.md
SHA256 = 6BB93F8838074D149D0CF909E57FD4172CCADAEBEFCB8C301411A85D0D6D4155

skills/research-orchestrator/tests/activation_cases.md
SHA256 = F724524F7E45F2B3963F4584BF5460860544B5AED7981E571B27A3AB3E1267A9
```

Requested audit reports (also in the allowlist):

```text
RESEARCH_OS_CROSS_PROJECT_ISOLATION_TEST.md
RESEARCH_OS_GENERIC_ROUTING_TEST_REPORT.md
RESEARCH_OS_METHODOLOGY_ROUTING_CHANGELOG.md
RESEARCH_OS_MINIMAL_RELEASE_PLAN.md
RESEARCH_OS_ROUTER_PARITY_AUDIT.md
```

## Release proposal, not an applied version change

The Draft PR candidate is `1.1.0-rc.4`: it adds a methodology primary route and clarifies
boundaries while retaining all existing workflows, writing owner, state schema, and approval
rules. Existing `1.1.0-rc.3` remains the main/released version until an authorized merge.
After merge, a release metadata update must set the stable validation ref to `main`.

## Separate follow-up issues

- After author-approved merge, update the candidate validation ref in `docs/version.md` to
  `main`; do not leave the Draft PR branch identified as a stable source.
- ChatGPT account/Project UI limits and Skill availability remain unverified; installing the
  repository or matching hashes does not prove account-level routing. Preserve existing user
  instructions and check the actual field limits before a later installation.
- Previously reported installed-Skill customizations and fresh-client black-box acceptance
  belong to the separate activation task; they were not read, merged, or refreshed here.

## Protected environment / end-of-task check

The global resource guard SHA-256 remains
`C145D2E14136C7977A8FAF09B938A0714213AD784E2428FD90F5EC288BFDCC47`.
The original dirty checkout's 19 tracked modifications and 594 untracked file entries are
preserved. Its status-list SHA-256 is
`BFF28EE42BB12BE0FF1928B829ECE22291A25E804E09E1D9F541ACBF834C8A28`,
and tracked-diff SHA-256 is
`4C3B37AB942B6606FA5AEAE1B5EE6E91A5E2FAAE0CA01E10B1C1FADA2616E379`;
both match the pre-development snapshots. Untracked private contents were not read or hashed.
The protected PR6 release checkout remains clean at the base commit.

Only one new development worktree was created, for the explicitly required isolation.
No persistent compute job was launched; validation commands completed. Temporary test files
were confined to the unique D: root and no files remained there at the final inventory.
No existing files were deleted, moved, or cleaned. New audit reports/worktree are retained
for author review, not automatically removed.
