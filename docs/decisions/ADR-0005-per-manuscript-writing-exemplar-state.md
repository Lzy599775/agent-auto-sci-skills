# ADR-0005: Isolate Writing Exemplars Per Manuscript

- Status: Accepted
- Date: 2026-10-12

## Context

Reusable exemplar selection and analysis can improve substantive manuscript writing, but a global paper list or project skill risks cross-manuscript contamination and can let exemplar structure replace the author's scientific logic. Codex and ChatGPT Web also need consistent approval and corpus state.

## Decision

- Keep `agent-auto-sci-scicomm` as the global writing workflow owner and the existing prose guard as the polishing layer.
- Use the per-manuscript exemplar workflow only as an orchestration helper.
- Give each manuscript an independent stable ID, private profile/state, Master 20, Core 3, section selections, pattern library, and project skill.
- Require explicit author approval only for Core 3; pending approval blocks deep analysis and major rewriting. Approval automatically unlocks deep analysis.
- Store the single authoritative state record in the configured private state hub; Codex and ChatGPT Web read/write that same record rather than chat memory.
- Keep the public repository generic: workflow, schemas, templates, routing, and synthetic tests only.

## Consequences

- Manuscript-specific content cannot be reused implicitly across projects.
- Substantive section writing freshly selects and rereads 4–5 records from that manuscript's Master 20 after constructing its evidence and argument maps.
- The workflow requires an explicit refresh assessment when scientific positioning changes; it does not require replacing all 20 by default.
- Private-state availability is a precondition for cross-client continuity. If unavailable or identity is uncertain, do not infer state.
