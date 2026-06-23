# Changelog

All notable changes to the Codex package are documented here.

## Unreleased

## [0.1.14] - 2026-06-21

### Fixed
- Replaced the Codex Desktop plugin's `skills` symlink with a materialized
  bundled `skills/academic-research-suite` directory so Windows plugin caches
  register the bundled skill reliably.
- Added a package quality gate that fails if the Desktop plugin bundle reverts
  to symlink-based skill packaging.

## [0.1.13] - 2026-06-20

### What's Changed
- Updated the vendored ARS runtime from
  `529c6d25a3778843fb94edf9f03eda4cd7e0f416` (`v3.12.0-19-g529c6d2`,
  ARS main after the submission-package verifier slices) to
  `c22c17eed8a5753aa60681be9734919f2e2f5b42` (`v3.13.0-2-gc22c17e`,
  ARS main after the GitHub Copilot documentation updates).
- Added upstream ARS v3.12.1 and v3.13 mainline content, including
  reviewer-response triage modes, diff/patch revision mode adoption,
  format-profile support, provider-agnostic cross-model verification,
  Windows hook portability, Socratic adjacent-framing probe support,
  CITATION metadata, and repository instruction docs.
- Added Codex alias coverage for `ars-3w` and `ars-rebuttal-audit` in both
  the root router and the optional full-runtime planner.
- Preserved Codex packaging behavior: one root router skill, vendored workflow
  entry files named `WORKFLOW.md`, excluded Claude/plugin loader files,
  preserved nested upstream `.github` and root `agents` mirrors as inactive
  traceability/self-test fixtures, Codex setup/architecture overlays at the
  package root, nested-path lint adaptations, macOS Bash 3.2 audit wrapper
  compatibility, and explicit cross-model consent boundaries.

### Notes
- This sync pins ARS `main`, not an exact upstream tag. The nearest upstream tag
  is `v3.13.0`.

## [0.1.12] - 2026-06-11

### What's Changed
- Updated the vendored ARS runtime from
  `2560a072386d4b1a035e5a40ed24ce1edbc0a356` (`v3.11.1`) to
  `529c6d25a3778843fb94edf9f03eda4cd7e0f416` (`v3.12.0-19-g529c6d2`,
  ARS main after the submission-package verifier slices).
- Added upstream ARS v3.12 and post-tag mainline content, including
  sub-claim decomposition, cross-paper contradiction inventory, figure/table
  fidelity, experiment provenance intake, field-norm severity calibration,
  surface-form parity checks, repository hygiene config, and the submission
  package verifier.
- Added Codex alias coverage for `ars-cache-invalidate`.
- Preserved Codex packaging behavior: one root router skill, vendored workflow
  entry files named `WORKFLOW.md`, Codex setup/architecture overlays, excluded
  Claude/plugin loader files, nested-path lint adaptations, macOS Bash 3.2
  audit wrapper compatibility, and explicit cross-model consent boundaries.

### Notes
- This sync pins ARS `main`, not an exact upstream tag. The nearest upstream tag
  is `v3.12.0`.

## [0.1.11] - 2026-06-06

### What's Changed
- Updated the vendored ARS runtime from
  `ca5b713d9d802af85d4c74552604b062a618b1c1` (`v3.11.0` plus the first
  post-tag #310 follow-up fixes) to
  `2560a072386d4b1a035e5a40ed24ce1edbc0a356` (`v3.11.1`).
- In plain terms: this brings the Codex package up to the ARS patch release
  that cleaned up the first wave of post-ship problems after v3.11.0. The main
  changes are correctness and hardening fixes for citation verification,
  domain evidence profiles, eval thresholds, policy markers, provenance joins,
  and edge cases around schema-valid security-boundary inputs.
- Preserved the Codex packaging layer: one root router skill, vendored
  workflow entry files named `WORKFLOW.md`, Codex setup/architecture overlays,
  excluded Claude/plugin loader files, package-specific lint adaptations, and
  the explicit cross-model consent boundary.
- Kept local Codex validation runnable on macOS Python 3.9 by avoiding
  Python-3.11-only standard-library assumptions in the vendored test utilities
  and by using the active Python executable in adapter subprocess tests.

### Notes
- No new Codex package feature was added. This is a vendor sync plus metadata
  release so Codex users get the same v3.11.1 runtime fixes as upstream ARS.

## [0.1.10] - 2026-06-04

### Added
- Added an optional Codex full-runtime adapter profile under
  `skills/academic-research-suite/codex/`, including deterministic route
  planning, Codex agent-team templates, a disabled-by-default hook pack, and
  adapter quality gates. Default ARS Codex behavior remains inline role-prompt
  execution.

### Changed
- Vendored upstream ARS from `4c38571798da4b1ed604ec2c1e01a6f66a7de5a7`
  (`v3.10.0` plus release-manifest alignment) to
  `ca5b713d9d802af85d4c74552604b062a618b1c1` (`v3.11.0` plus post-tag #310
  follow-up fixes).
- Added ARS v3.11 runtime content, including the deterministic citation
  verification gate, arXiv resolver, persistent verification cache, citation
  verification summary contract, standalone verification gate API, and
  `ars-cache-invalidate` command recipe.
- Kept Codex-specific overlays: single root router skill, `WORKFLOW.md`
  vendored workflow entry files, Codex setup/architecture docs, nested-path lint
  patches, excluded showcase PDFs, macOS Bash 3.2 audit wrapper compatibility,
  and explicit cross-model consent boundaries.

### Security
- Added Codex security boundaries for untrusted research inputs, cross-model
  consent, local adapter filesystem handling, and fixed-host bibliographic API
  lookups.

## [0.1.9] - 2026-06-01

### Changed
- Vendored upstream ARS from `96b82e82142dc95f117595c207d3e150b078e411` (`v3.9.4.2`) to `4c38571798da4b1ed604ec2c1e01a6f66a7de5a7` (`v3.10.0` plus release-manifest alignment).
- Added ARS v3.10 runtime content, including the triangulation policy layer, eval harness/gold sets, Schema 11 commitment-ledger refactor, domain-evidence/version-family updates, and scoped-write guard scripts.
- Added newly vendored upstream `README.zh-CN.md`, `README.ja-JP.md`, `evals/`, `conftest.py`, and new `ars-*` command recipes.
- Kept Codex-specific overlays: single root router skill, `WORKFLOW.md` vendored workflow entry files, Codex setup/architecture docs, nested-path lint patches, excluded showcase PDFs, and macOS Bash 3.2 audit wrapper compatibility.
- Clarified beginner install instructions by using `python3` in command
  examples and documenting the `python` fallback when it points to Python 3.
- Added community acknowledgements for beginner-install feedback and issue
  discussion support.

## [0.1.8] - 2026-05-19

### Changed
- Vendored upstream ARS from `74413a42571867abece7b8b76f7a24ac472ab2a0` (`v3.9.0`) to `96b82e82142dc95f117595c207d3e150b078e411` (`v3.9.4.2`).
- Added ARS v3.9.1 client hardening, v3.9.2 phase-boundary routing discipline, v3.9.3 shared client utilities, and v3.9.4/v3.9.4.1 temporal verification runtime content.
- Kept Codex-specific overlays: single root router skill, `WORKFLOW.md` vendored workflow entry files, Codex setup/architecture docs, nested-path lint patches, and macOS Bash 3.2 audit wrapper compatibility.

### Notes
- Upstream v3.9.4.2 changes only `.github` CI/release-gate files, which are intentionally excluded from this Codex package. The manifest still pins the exact v3.9.4.2 commit for provenance.

## [0.1.7] - 2026-05-17

### Changed
- Aligned the Codex package with upstream ARS `v3.9.0`.
