# Failure Handling and Quality Control

## Failure states

- `FULL_TEXT_MISSING`: metadata known, source text unavailable.
- `METADATA_CONFLICT`: authoritative records disagree.
- `AMBIGUOUS_DUPLICATE`: candidate records cannot be safely merged.
- `IDENTIFIER_NOT_VERIFIED`: DOI or other identifier unresolved.
- `SOURCE_ACCESS_RESTRICTED`: paywall, credentials, CAPTCHA, or license boundary.
- `TEMPORARY_RETRIEVAL_FAILURE`: retryable network or service error.
- `INSUFFICIENT_EVIDENCE`: evidence cannot support the requested conclusion.

Do not hide these states or fill them with guesses.

## Quality checks

### Metadata

- title, authors, year, venue, DOI/identifier, and version match authoritative records;
- duplicate decisions have a stated basis;
- retractions, corrections, or expressions of concern are checked when relevant.

### Study and methods

- design, population, period, unit, sample, exposure/intervention, outcome, covariates, and validation come from source text;
- methods are not inferred from common practice;
- exact and substitute data are clearly separated.

### Numerical

- value, unit, denominator, subgroup, time period, uncertainty, and table/figure location are verified;
- statistical significance is not substituted for magnitude or practical importance.

### Evidence trace

- each substantive synthesis claim maps to a source and location;
- source statement and Codex inference are separated;
- support type and confidence are explicit.

## Retry and stop rules

Retry temporary technical failures with bounded attempts or alternate authoritative routes. Stop for credentials, paid access, legal/licensing ambiguity, destructive library writes, irrecoverable identity ambiguity, or scientific choices with materially different defensible outcomes.
