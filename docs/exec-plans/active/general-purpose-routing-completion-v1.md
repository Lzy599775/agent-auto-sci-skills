# General-purpose routing completion

## Scope and baseline

- Author request: `RESEARCH_OS_GENERAL_PURPOSE_ROUTING_COMPLETION_V1`.
- Base: `d5e913f07f9b7ea8d3666cb28fcacc0232c912fa`, workflow `1.1.0-rc.3`.
- Development branch: `codex/general-purpose-routing-v1`.
- Isolated worktree: dedicated candidate worktree (machine-specific path intentionally omitted).
- Isolation protects the existing dirty checkout and the separate release checkout; both are
  outside this plan's write scope and retain their pre-existing state.
- Repository blobs total 43,628,201 bytes at the base; no dataset or dependency copy is needed.
- Artifact root: this worktree (reviewable source and five requested reports).
- Temp root: a unique directory on the designated test volume (machine-specific path intentionally omitted).
- Expected additional source/reports/test outputs: under 10 MiB, excluding the checkout.
- Retention: active worktree and required audit; temporary synthetic test outputs remain separate.

## Implementation

1. Add the generic methodology workflow and deliverable-based route precedence.
2. Update Orchestrator, Project/account routers, and required distribution mirrors.
3. Add a machine-readable decision contract and synthetic cross-domain/isolated-state tests.
4. Run framework, writing, artifact, format, parity, skill, and security checks.
5. Produce the five requested review reports and verify protected checkout fingerprints.
6. After author approval, commit the reviewed allowlist, push normally, and open Draft PR #7.

## Evidence limits

The decision-contract evaluator accepts a reviewed semantic intent, never matches prompt keywords.
Its tests validate contracts and synthetic access guards, not model intent recognition or actual
Codex/ChatGPT Skill activation. Fresh-client tests remain `NOT_TESTED` in this task.

At plan creation, no commit, push, merge, installer refresh, client-setting change, or private
research-data access had occurred. The reviewed candidate was subsequently committed as
`20c0ab7825a2d5bd9e5ed8b19219dfb9e0d7f950`, pushed normally, and opened as Draft PR #7; no merge,
installer refresh, client-setting change, or private research-data access has occurred.
The candidate version is `1.1.0-rc.4`; `main` remains the stable source until merge.

The A–M cross-domain checks are `SEMANTIC_INTENT_CONTRACT_TEST` evidence, and the eight project
checks are `SYNTHETIC_STATE_ISOLATION_TEST` evidence. Neither establishes natural-language intent
recognition or fresh-client Skill activation; those remain a separate black-box phase.
