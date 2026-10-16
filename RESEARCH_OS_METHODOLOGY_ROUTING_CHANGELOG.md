# Research OS methodology routing changelog

## Baseline

- Base: `d5e913f07f9b7ea8d3666cb28fcacc0232c912fa`.
- Candidate workflow: `1.1.0-rc.4` (base/main remains `1.1.0-rc.3` until merge).
- Branch: `codex/general-purpose-routing-v1`.
- Scope: generic methodology/research-design routing, cross-surface parity, and synthetic isolation.

## Changes

- Added `docs/workflows/methodology.md` as the discipline-neutral primary workflow for design
  appraisal, estimands, identification, bias, validity, inference assumptions, and model suitability.
- Updated `docs/workflows/index.md` with deliverable precedence separating method judgment from
  data/model execution, Methods critique from prose rewriting, and reproduction from analysis.
- Updated `skills/research-orchestrator/SKILL.md` and its plugin/distribution mirrors.
- Updated Codex/ChatGPT Project/global/cross-surface entrypoints to defer to the canonical
  routing decision contract and to preserve private project-state isolation.
- Marked prior green-exposure activation text as `SYNTHETIC_EXAMPLE`; added neutral and
  cross-domain A–M cases with near-neighbor deliverable changes.
- Added `docs/workflows/ROUTING_DECISION_CONTRACT_V1.json` for reviewed semantic intents.
- Updated `docs/version.md` and `CHANGELOG.md` so the candidate's version/ref metadata is
  internally consistent; the candidate is not yet main or a released client installation.

## Boundaries

The contract is not a keyword classifier and does not prove automatic Skill invocation. It
accepts an interpreted intent for deterministic validation; real new Codex and ChatGPT
black-box activation remains a separate acceptance task. No client installation, production
Skill refresh, ChatGPT setting change, Zotero write, or private project read occurred.
