# Agentic Research Workflow Architecture

## Purpose

This repository provides a persistent, evidence-first operating system for AI-assisted research. It coordinates instructions, documentation, derived knowledge, reusable skills, evaluation, and Git delivery without granting unrestricted autonomy.

## Layers

| Layer | Responsibility | Source of truth |
|---|---|---|
| `AGENTS.md` | Concise mission, routing, invariants, and gates | Root repository instructions |
| `docs/` | Detailed policies, workflows, standards, decisions, and execution plans | Maintained human-readable system record |
| `research-vault/` | Derived knowledge and project reasoning | Structured records linked to sources |
| `templates/` | Stable schemas for repeated research records | Versioned Markdown templates |
| `skills/` | Focused reusable task workflows | `SKILL.md` plus on-demand references/scripts |
| `evals/` | Golden-set and behavioral evaluation definitions | Reviewed test cases and scoring rules |
| `scripts/validation/` | Deterministic structural checks | Lightweight executable validation |
| Git and Draft PRs | Change history and review boundary | Branch history and pull-request review |

## Control flow

1. Read applicable `AGENTS.md` instructions.
2. Route the request through `docs/workflows/index.md`.
3. Load only the relevant workflow, standards, skill, and project-specific context.
4. Gather authoritative evidence from local sources, Zotero, GitHub, official documentation, or scholarly services.
5. Produce derived artifacts with explicit provenance and uncertainty states.
6. Run workflow-specific and repository-level quality gates.
7. Record durable decisions and long-running state when justified.
8. Review Git diffs and deliver important changes through a task branch and Draft PR.

## Separation of concerns

- Zotero remains the bibliographic and PDF-management source of truth.
- The Research Vault stores derived notes, evidence records, method comparisons, dataset records, synthesis, and project reasoning.
- Skills encode reusable procedures, not project facts or giant manuals.
- Project repositories may specialize the global defaults with nearer instructions.
- Read autonomy does not imply write autonomy.

## Evolution path

New automation should follow:

`MANUAL WORKFLOW -> GOLDEN SET -> EVAL -> SKILL -> OPTIONAL PLUGIN`

Do not automate unstable extraction rules before a reviewed golden set demonstrates repeatable behavior.

## Architectural decisions

See [docs/decisions/index.md](docs/decisions/index.md) for the rationale behind instruction size, Zotero ownership, Research Vault scope, and evaluation-first skill development.
