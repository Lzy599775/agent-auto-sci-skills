# Per-Manuscript Exemplar State Machine V1

Each state belongs to one stable `MANUSCRIPT_ID`; never merge state across IDs.

| State | Meaning | Allowed next states / guard |
|---|---|---|
| `S0_UNINITIALIZED` | No validated profile/corpus lifecycle for this manuscript | `S1` after identity is sufficiently resolved and profile is created |
| `S1_MANUSCRIPT_PROFILED` | Manuscript profile and sources/unknowns recorded | `S2` after candidate pool is deduplicated and traceable |
| `S2_CANDIDATE_POOL_READY` | Recommended broad candidate pool ready | `S3` after exactly 20 records selected from this manuscript's pool |
| `S3_MASTER_20_SELECTED` | Versioned Master 20 exists; Core 3 recommendation not yet gated | `S4` after Core 3 packet is generated |
| `S4_CORE_3_PENDING_AUTHOR_APPROVAL` | Core 3 recommendation awaits explicit author decision | Remain `S4` until approve/replace/reject; no deep imitation or major rewrite. Approval -> `S5`; replacement/rejection -> revised recommendation and `S4` |
| `S5_CORE_3_APPROVED` | Approval is persisted and version-linked | Automatically continue deep analysis -> `S6`; do not request a second approval |
| `S6_CORPUS_DEEP_ANALYSIS_COMPLETE` | Four-level analysis, quality review, and pattern synthesis complete | `S7` after private project skill is built and validated |
| `S7_PROJECT_EXEMPLAR_SKILL_BUILT` | Manuscript-specific skill stored privately and versioned | `S8` after isolation, user-style, anti-copying, and provenance checks pass |
| `S8_ACTIVE_FOR_WRITING` | Skill may route section writing and fresh 4–5 selection | Remain `S8` while framing and versions remain current; any refresh trigger -> `S9` |
| `S9_REFRESH_REQUIRED` | A material change or review trigger requires refresh assessment | Return to appropriate prior state after assessment; rerun affected profiling/candidate/corpus/Core 3/analysis stages as needed; new Core 3 requires explicit approval |

Identity resolution precedes normal transitions. Ambiguous identity is an overlay `MANUSCRIPT_IDENTITY_UNCERTAIN`, not a state that licenses inheritance; stay in the current state or `S0` until resolved. `S4` is a hard gate for deep analysis and major rewriting. Rejection is not approval. A recorded approval automatically unlocks `S5 -> S6`.

Refresh triggers: changed target journal, materially changed research question or scientific positioning, major method change, new primary outcome, major reviewer-driven repositioning, or material new literature. Corpus age `>12 months` is a prompt only. Refresh does not necessarily require rebuilding all 20 records, but requires a recorded impact assessment.

State schema includes manuscript ID, profile, exemplar state, state history, corpus/Core 3/skill versions, approval decision and timestamp, private paths/pointers, source provenance, and update timestamps. Client surfaces must read and update the same authoritative state record; chat history is never the state store.
