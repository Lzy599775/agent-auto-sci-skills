# Notice

This subskill is packaged from:

- Codex package repository: `Imbad0202/academic-research-skills-codex`
- Codex package commit used: `52228e8`
- Codex package tag snapshot: `v3.23.0`
- Upstream ARS repository: `Imbad0202/academic-research-skills`
- Upstream ARS commit recorded in `manifest.json`: `6ab4b03bf70a118a1b3ee7f3263ed9f19031061b`
- Upstream license: CC BY-NC 4.0, see `LICENSE`.

The suite is vendored only as an isolated subskill under `urban-exposure-review-radar-workflow`. The parent skill remains responsible for urban exposure, sport geography, accessibility/use separation, causal-language boundaries, and formal-corpus versus frontier-radar separation.

Local distribution adaptation: `codex/scripts/ars_codex_quality_gates.py` resolves manifest paths from this nested standalone skill root and skips only the repository-level Desktop plugin bundle check when `plugins/ars-codex` is not packaged. Skill manifest, routing, hook safety, reviewer fixture, topology, and upstream-lock gates remain active.

The v3.23.0 package adds an explicit-only `sr-screener` workflow, run-ledger and acronym checks, citation-locale evaluations, and routing-core updates. The standalone quality-gate adaptation is retained for this nested distribution.
