# ADR-0001: Keep Root AGENTS.md Concise

- Status: Accepted
- Date: 2026-08-23

## Context

Codex loads root instructions into every repository task. A large manual would consume context and duplicate detailed documentation.

## Decision

Keep root `AGENTS.md` as a mission, repository map, invariant rules, routing entry point, quality gates, and stop conditions. Store detailed policies and workflows under `docs/`.

## Consequences

Instructions remain discoverable and durable without crowding task context. Linked documents must stay valid and validation must catch broken references.
