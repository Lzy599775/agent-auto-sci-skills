# ADR-0004: Literature Automation Requires Golden-Set Validation

- Status: Accepted
- Date: 2026-08-23

## Context

Metadata, study design, numerical extraction, and citation support contain heterogeneous edge cases. Premature automation can make plausible but unverified errors repeatable.

## Decision

Develop literature capability in the order `manual workflow -> reviewed golden set -> evaluation -> skill automation`.

## Consequences

Literature Skill V0 defines contracts and boundaries but avoids unstable extraction heuristics. Expansion requires demonstrated evaluation performance.
