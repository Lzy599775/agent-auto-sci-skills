# Uncertainty Policy

Use explicit states instead of plausible completion:

| State | Meaning |
|---|---|
| `KNOWN` | Directly observed in a trusted local or authoritative source |
| `SUPPORTED` | Backed by adequate evidence, with bounded interpretation |
| `INFERRED` | Reasoned from stated evidence but not directly reported |
| `UNKNOWN` | Not established by available evidence |
| `NOT_AVAILABLE` | Required source or data cannot currently be accessed |
| `CONFLICTING_EVIDENCE` | Credible sources disagree materially |

## Rules

- Label inference separately from source-reported fact.
- Give confidence as `HIGH`, `MEDIUM`, or `LOW` when judgment is involved.
- Explain what evidence would resolve important uncertainty.
- Do not convert `UNKNOWN` to a guessed value.
- Do not hide inaccessible full text, missing metadata, or failed validation.
- Preserve alternative interpretations when the evidence does not discriminate between them.
