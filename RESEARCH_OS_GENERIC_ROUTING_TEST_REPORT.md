# Generic routing test report

## Test environment

- Worktree: dedicated isolated candidate worktree (machine-specific path intentionally omitted).
- Base: `d5e913f07f9b7ea8d3666cb28fcacc0232c912fa`.
- Candidate workflow metadata: `1.1.0-rc.4`; current main workflow: `1.1.0-rc.3`.
- Python: `3.13.9` (configured local runtime; executable path intentionally omitted).
- pytest: `8.4.2`.
- Synthetic temporary root: unique isolated test directory (machine-specific path intentionally omitted).
- Real papers, private manuscripts, Zotero, and user datasets: not read.

## Results

| Check | Result |
|---|---:|
| General routing contract A–M | 13/13 PASS |
| Cross-project isolation tests | 8/8 PASS |
| Generic routing unittest module | 27/27 PASS |
| Full unittest discovery | 58/58 PASS |
| Full pytest validation directory | 60/60 PASS |
| Research workflow validator | PASS (54 required files; 105 Markdown files) |
| Academic writing V2 | PASS |
| Writing exemplar routing | PASS |
| Paper-artifact/writing routing | PASS |
| Public-safety scan | PASS |
| `git diff --check` | PASS |

The first run exposed two incorrect test assumptions about shared primary owners; the test was
revised to compare mode and state gates as well as the primary route. No implementation behavior
was weakened to pass the test. The final run passed all listed checks.

## Interpretation

These are structural, synthetic, and contract-level results. They do not establish that a fresh
Codex session or ChatGPT Web/Desktop chat will automatically load a Skill. That requires a separate
black-box run with actual tool/file-read evidence.

## Counts and reproducibility

- Date: 2026-10-15, Asia/Shanghai.
- OS: Windows 11, build 26200; existing Anaconda Python, no dependency installation.
- New module: total 27, passed 27, failed 0, skipped 0.
- Existing tests under pytest: total 33, passed 33, failed 0, skipped 0.
- Combined pytest: total 60, passed 60, failed 0, skipped 0.
- Combined unittest: total 58, passed 58, failed 0, skipped 0. Two existing pytest
  function tests are not collected by unittest; this is not a skipped-test claim.
- A–M primary decisions: 13/13; near-neighbor contract comparisons: 13/13.
- Paraphrase inputs are prepared for later black-box runs; natural-language intent recognition
  and real Skill invocation were NOT_EXECUTED, not counted as passed.
- Tested scope: `scripts/validation`; unrelated vendored suites/holdouts were not traversed or run.

Commands (run at the development worktree):

```text
python -B -m unittest discover -s scripts/validation -p test_generic_research_routing.py -v
python -B scripts/validation/validate_research_workflow.py
python -B scripts/validation/validate_generic_research_routing.py
python -B scripts/validation/validate_academic_writing_v2.py
python -B scripts/validation/validate_writing_exemplar_routing.py
python -B scripts/validation/validate_paper_artifact_and_writing_routing.py
pwsh -NoProfile -File scripts/scan_public_safety.ps1
git diff --check
```

Full unittest/pytest runs assigned `tempfile.tempdir` to the unique D: root inside a
`python -B -c` wrapper; they did not change environment variables. Pytest used
`-p no:cacheprovider` and a fresh `--basetemp` child for each run. No worktree Python
bytecode or pytest caches were created; DOCX fixtures were generated in temporary directories.

Core tested source hashes (uncommitted source, not a newly released commit):

```text
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
```

## A–M observations

ACTUAL_ROUTE below is the executable decision contract's result over the reviewed semantic
intent. It is not a fresh-client observation or evidence that the prompt loaded a Skill.
Inputs, paraphrases and neighbors are synthetic.

```text
CASE A
TASK_INPUT = Does the vaccination policy design identify a heterogeneous intervention effect?
EXPECTED_PRIMARY_ROUTE = methodology
EXPECTED_COMPANION = NONE_REQUIRED
EXPECTED_SPECIALIST_SKILL = agent-auto-sci-methodology
ACTUAL_ROUTE = methodology
PASS_OR_FAIL = PASS

CASE B
TASK_INPUT = Appraise randomization, replication and precision in a proposed alloy experiment.
EXPECTED_PRIMARY_ROUTE = methodology
EXPECTED_COMPANION = NONE_REQUIRED
EXPECTED_SPECIALIST_SKILL = agent-auto-sci-methodology
ACTUAL_ROUTE = methodology
PASS_OR_FAIL = PASS

CASE C
TASK_INPUT = Review selection and unmeasured confounding in observational species monitoring.
EXPECTED_PRIMARY_ROUTE = methodology
EXPECTED_COMPANION = NONE_REQUIRED
EXPECTED_SPECIALIST_SKILL = agent-auto-sci-methodology
ACTUAL_ROUTE = methodology
PASS_OR_FAIL = PASS

CASE D
TASK_INPUT = Assess survey sampling and construct measurement validity before fieldwork.
EXPECTED_PRIMARY_ROUTE = methodology
EXPECTED_COMPANION = NONE_REQUIRED
EXPECTED_SPECIALIST_SKILL = agent-auto-sci-methodology
ACTUAL_ROUTE = methodology
PASS_OR_FAIL = PASS

CASE E
TASK_INPUT = Clean this synthetic CSV, audit missing values and execute the planned regression.
EXPECTED_PRIMARY_ROUTE = data_analysis
EXPECTED_COMPANION = NONE_REQUIRED
EXPECTED_SPECIALIST_SKILL = agent-auto-sci-data-viz
ACTUAL_ROUTE = data_analysis
PASS_OR_FAIL = PASS

CASE F
TASK_INPUT = Evaluate the fitted model's predictive accuracy using held-out synthetic data.
EXPECTED_PRIMARY_ROUTE = data_analysis
EXPECTED_COMPANION = NONE_REQUIRED
EXPECTED_SPECIALIST_SKILL = agent-auto-sci-ai-ml
ACTUAL_ROUTE = data_analysis
PASS_OR_FAIL = PASS

CASE G
TASK_INPUT = Create a figure of the supplied synthetic results with uncertainty intervals.
EXPECTED_PRIMARY_ROUTE = figure_workflow
EXPECTED_COMPANION = NONE_REQUIRED
EXPECTED_SPECIALIST_SKILL = agent-auto-sci-data-viz
ACTUAL_ROUTE = figure_workflow
PASS_OR_FAIL = PASS

CASE H
TASK_INPUT = Review and reorganize the argument structure of this manuscript Discussion.
EXPECTED_PRIMARY_ROUTE = manuscript_writing
EXPECTED_COMPANION = PER_MANUSCRIPT_WRITING_EXEMPLAR_WORKFLOW_V1
EXPECTED_SPECIALIST_SKILL = agent-auto-sci-scicomm
ACTUAL_ROUTE = manuscript_writing
PASS_OR_FAIL = PASS

CASE I
TASK_INPUT = Polish the grammar of this one academic sentence without changing its meaning.
EXPECTED_PRIMARY_ROUTE = manuscript_writing
EXPECTED_COMPANION = NONE_REQUIRED
EXPECTED_SPECIALIST_SKILL = agent-auto-sci-scicomm
ACTUAL_ROUTE = manuscript_writing
PASS_OR_FAIL = PASS

CASE J
TASK_INPUT = Reproduce a published model result using its released code and synthetic test inputs.
EXPECTED_PRIMARY_ROUTE = paper_reproduction
EXPECTED_COMPANION = PAPER_ARTIFACT_AVAILABILITY_PROTOCOL_V1
EXPECTED_SPECIALIST_SKILL = NONE_REQUIRED; select by actual execution needs
ACTUAL_ROUTE = paper_reproduction
PASS_OR_FAIL = PASS

CASE K
TASK_INPUT = Verify that this claimed code and data repository belongs to the named paper.
EXPECTED_PRIMARY_ROUTE = literature_review
EXPECTED_COMPANION = PAPER_ARTIFACT_AVAILABILITY_PROTOCOL_V1
EXPECTED_SPECIALIST_SKILL = literature
ACTUAL_ROUTE = literature_review
PASS_OR_FAIL = PASS

CASE L
TASK_INPUT = Before any scientific computation, report disk and RAM risk without starting the job.
EXPECTED_PRIMARY_ROUTE = data_analysis
EXPECTED_COMPANION = NONE_REQUIRED
EXPECTED_SPECIALIST_SKILL = NONE_REQUIRED; select by actual execution needs
ACTUAL_ROUTE = data_analysis
PASS_OR_FAIL = PASS

CASE M
TASK_INPUT = Evaluate the novelty and feasibility of this new research direction.
EXPECTED_PRIMARY_ROUTE = research_idea_evaluation
EXPECTED_COMPANION = NONE_REQUIRED
EXPECTED_SPECIALIST_SKILL = agent-auto-sci-methodology
ACTUAL_ROUTE = research_idea_evaluation
PASS_OR_FAIL = PASS
```
