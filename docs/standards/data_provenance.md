# Data Provenance Standard

Create a dataset record for every important external or derived dataset.

## Required fields when applicable

- `dataset_name`
- `provider`
- `official_url`
- `version`
- `release_date`
- `download_date`
- `license`
- `spatial_resolution`
- `temporal_resolution`
- `coverage`
- `crs`
- `raw_path`
- `processed_path`
- `processing_script`
- `variables_used`
- `known_limitations`

Use `NOT_REPORTED`, `NOT_APPLICABLE`, or `NOT_VERIFIED` rather than guessing.

## Checksums

Record checksums when they protect integrity for downloaded releases, regulated artifacts, long-lived archives, or transfer verification. Do not impose hashes ceremonially on every project file.
