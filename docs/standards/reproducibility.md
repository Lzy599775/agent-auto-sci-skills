# Reproducibility Standard

## Artifact classes

- `RAW`: immutable source data or source captures.
- `INTERMEDIATE`: deterministic transformations not used directly for final inference.
- `ANALYTICAL`: analysis-ready data used by models, statistics, or figures.
- `OUTPUT`: tables, figures, models, reports, and manuscripts.

## Rules

- Never overwrite raw source data.
- Document inputs, outputs, processing order, parameters, exclusions, and software versions when material.
- Make transformations scriptable and rerunnable from documented inputs.
- Record random seeds when stochastic variation affects scientific conclusions or verification.
- Validate joins, row/entity counts, units, CRS, time zones, and identifiers where relevant.
- Keep environment-specific paths out of public configuration.
- Do not claim reproducibility merely because code ran once.

## Completion evidence

A reproducible workflow needs documented inputs, deterministic or bounded-stochastic execution, validation of important intermediate artifacts, and enough provenance for another researcher to diagnose divergence.
