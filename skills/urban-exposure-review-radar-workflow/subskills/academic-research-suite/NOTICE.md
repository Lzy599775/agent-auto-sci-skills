# Notice

This subskill is packaged from:

- Codex package repository: `Imbad0202/academic-research-skills-codex`
- Codex package commit used: `82725acb393c4410ac6f47634a7f51b40a162fa4`
- Codex package tag snapshot: `v3.24.2`
- Upstream ARS repository: `Imbad0202/academic-research-skills`
- Upstream ARS commit recorded in `manifest.json`: `fd5ff1b858374219b4d342e38587b66e18f61cbd`
- Upstream license: CC BY-NC 4.0, see `LICENSE`.

The suite is vendored only as an isolated subskill under `urban-exposure-review-radar-workflow`. The parent skill remains responsible for urban exposure, sport geography, accessibility/use separation, causal-language boundaries, and formal-corpus versus frontier-radar separation.

Local distribution adaptation: `codex/scripts/ars_codex_quality_gates.py` resolves manifest paths from this nested standalone skill root and skips only the repository-level Desktop plugin bundle check when `plugins/ars-codex` is not packaged. Skill manifest, routing, hook safety, reviewer fixture, topology, and upstream-lock gates remain active.

The v3.24.2 package retains the explicit-only `sr-screener` workflow. The standalone quality-gate adaptation is retained for this nested distribution, including the new routing-core check; the Desktop plugin bundle and topology receipts remain outside this package.
