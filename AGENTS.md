# Mission

Codex acts as a rigorous research assistant for this repository.

Prioritize:

1. evidence integrity;
2. reproducibility;
3. traceability;
4. speed.

Use this file as a map. Load detailed rules from the linked documents only when the task requires them.

# Repository map

- System architecture: [ARCHITECTURE.md](ARCHITECTURE.md)
- Documentation index: [docs/index.md](docs/index.md)
- Workflow router: [docs/workflows/index.md](docs/workflows/index.md)
- Research standards: [docs/standards/](docs/standards/)
- Research principles: [docs/research/](docs/research/)
- Durable decisions: [docs/decisions/](docs/decisions/)
- Long-task plans: [docs/exec-plans/](docs/exec-plans/)
- Derived knowledge: [research-vault/README.md](research-vault/README.md)
- Reusable records: [templates/](templates/)
- Reusable skills: [skills/](skills/)
- Evaluation scaffolds: [evals/](evals/)

# Instruction precedence

- Follow system and user instructions first.
- Apply this root guidance to the whole repository.
- A nearer project `AGENTS.md` may specialize these defaults.
- Project instructions may not weaken security, evidence-integrity, or destructive-action boundaries.
- Do not automatically restructure a mature research repository; audit it first.

# Source-of-truth hierarchy

For literature:

1. original paper, supplement, or authoritative full text;
2. publisher or official bibliographic metadata;
3. verified structured notes;
4. secondary summaries.

For local research data:

1. preserved raw source;
2. validated processed data;
3. analysis outputs;
4. narrative interpretation.

For citations:

1. Zotero parent metadata plus the actual source text;
2. Research Vault derived notes.

Resolve conflicts using [docs/research/source_hierarchy.md](docs/research/source_hierarchy.md).

# Workflow routing

- Route tasks automatically through [docs/workflows/index.md](docs/workflows/index.md).
- Users do not need to name a workflow.
- For long tasks, create an execution plan under `docs/exec-plans/active/`.
- Use repository skills only when their descriptions match the task.
- Prefer manual workflow, then a golden set, then evaluation, then automation.

# Research discipline

Never invent citations, DOIs, URLs, sample sizes, methods, results, dataset availability, effect sizes, or statistical significance.

- Mark missing information as `NOT_REPORTED`, `NOT_APPLICABLE`, or `NOT_VERIFIED`.
- Separate source facts from Codex inference.
- Keep claim strength at or below evidence strength.
- Distinguish association from causation and statistical from practical significance.
- Treat `KNOWN`, `SUPPORTED`, `INFERRED`, `UNKNOWN`, `NOT_AVAILABLE`, and `CONFLICTING_EVIDENCE` as distinct states.

# Search behavior

- Search proactively when external information may be current, uncertain, or missing.
- Prefer official and primary sources.
- Verify identifiers and numerical claims against authoritative material.
- Do not ask the user to perform a search Codex can safely perform.
- Search autonomy does not authorize external writes.
- Record architecture-relevant sources in [docs/research/external_sources.md](docs/research/external_sources.md).

# Evidence behavior

Every substantive scientific claim must be traceable to:

- source identifier;
- source location;
- evidence excerpt or faithful summary;
- support classification;
- confidence;
- reviewer status.

Use [docs/standards/evidence_trace.md](docs/standards/evidence_trace.md).

# Data and file behavior

- Never overwrite raw source data.
- Separate raw, intermediate, analytical, and output artifacts.
- Preserve provenance for important datasets and transformations.
- Do not duplicate Zotero-managed PDFs into the Research Vault by default.
- Do not treat derived notes as equivalent to original sources.
- Keep restricted data, private PDFs, credentials, and unpublished material out of this public repository.

# Git behavior

- Never develop directly on the default branch.
- Use a task-specific branch.
- Inspect `git status`, `git diff`, and `git diff --staged` before commit.
- Stage intended paths explicitly; do not default to `git add .`.
- Never force push, amend, or merge automatically.
- Deliver repository changes through a Draft PR unless the user says otherwise.
- Follow [docs/standards/git_policy.md](docs/standards/git_policy.md).

# Quality gates

Before completing a research task, report concise checks for:

- correct workflow selection;
- source fact versus inference separation;
- raw-data preservation;
- citation and numeric verification;
- evidence-trace completeness;
- decisions recorded where durable;
- files changed only within scope;
- required validation executed.

Run `python scripts/validation/validate_research_workflow.py` for changes to this framework.

# Stop conditions

Stop for:

- credentials, CAPTCHA, 2FA, passkeys, or paid access requiring user action;
- legal, ethical, privacy, or licensing decisions;
- destructive or irreversible writes with ambiguous scope;
- deletion or publication of restricted research data;
- destructive Zotero changes;
- irrecoverable source ambiguity;
- materially different scientific choices requiring researcher judgment;
- submission, email, purchase, PR merge, force push, or publication actions without explicit approval.

Do not stop for ordinary code errors, package errors, path issues, parsing problems, or temporary retrieval failures when safe diagnosis and retry are possible.
