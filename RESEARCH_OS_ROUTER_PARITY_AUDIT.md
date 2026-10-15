# Research OS router parity audit

## Scope

Compared the canonical Codex entrypoint, plugin mirror, ChatGPT Project instructions, global
router, cross-surface contract, and `dist/chatgpt` package. The authoritative decision contract is
`docs/workflows/ROUTING_DECISION_CONTRACT_V1.json`.

## Findings

- Codex and ChatGPT route design/identification/bias/validity/model-suitability judgments to
  `methodology` and `agent-auto-sci-methodology`.
- Data cleaning, fitting, statistics, and prediction evaluation remain `data_analysis`.
- Methods scientific critique and Methods prose rewriting are distinct deliverables.
- Reproduction, artifact identity, literature, citation, figure, novelty, and writing routes remain.
- `agent-auto-sci-scicomm` remains the sole substantive academic-writing owner.
- Project/manuscript data and exemplar state are isolated; method consultation and micro-edits do
  not read Master20/Core3 state.
- Research Orchestrator source, plugin mirror, and distribution mirror have identical five-file
  content hashes for `SKILL.md`, references, tests, and UI metadata.
- The copy-ready Project instructions are synchronized with `dist/chatgpt/project_instructions.txt`.

## Status

`STATIC_PARITY = PASS`; `FRESH_CLIENT_BLACK_BOX = NOT_TESTED`.
Repository changes do not install Skills or modify ChatGPT settings. A user must perform the
separate client acceptance run.

## Hash evidence

For each relative path below, source, plugin mirror, and ChatGPT distribution bytes match.
The existing five-file Skill set is unchanged; no competing Skill was created.

```text
SKILL.md
SHA256 = 6BB93F8838074D149D0CF909E57FD4172CCADAEBEFCB8C301411A85D0D6D4155

agents/openai.yaml
SHA256 = 9C37588EB18EF691FB62E5AF1DE4DFBC216FC0283049B2BA336238FB145085B5

references/routing-and-qc.md
SHA256 = 8FC4F5B47150831AA2B994C58FC5C0836DA3B522BB64FDF11CD9FDB1D9167F83

references/source-retrieval.md
SHA256 = A3DC3E59DEE7B05283888CCDB6E55CC04C627048BB819D6D8CE3E4291C128DD7

tests/activation_cases.md
SHA256 = F724524F7E45F2B3963F4584BF5460860544B5AED7981E571B27A3AB3E1267A9
```

The final Project copy-ready block is 547 words / 4,387 characters
(within the repository validator's 300–600 word contract). Installation length/feature
availability must still be checked against the user's live ChatGPT UI. The global router
is a repository source artifact; no claim is made that the full file fits any particular
account's Custom Instructions field. Existing personal/Project instructions must be preserved.

The Skill and its source-retrieval references now choose released `main` by default and
label explicitly requested unmerged refs as candidates. The handoff guide's methodology
expectation was updated from the obsolete citation/method hybrid. Deployment remains unchanged.
