# Data Analysis Workflow

Use for data cleaning/QC, model execution, statistics, and predictive validation. For a
judgment about design, identification assumptions, or model suitability, select
[Methodology / Research Design](methodology.md) instead. Published-result reproduction
uses [Paper reproduction](paper_reproduction.md). Select by deliverable, not a model name.

Perform the applicable lightweight resource preflight before local execution. A standalone
preflight stops after reporting disk/RAM, estimated output, and path; it does not authorize a job.

## Procedure

1. Define the research question, outcome, unit of analysis, estimand, and decision criteria.
2. Inventory files, schemas, provenance, licenses, sensitive fields, and expected row/entity counts.
3. Preserve raw inputs; write derived artifacts to distinct intermediate, analytical, and output locations.
4. Audit missingness, duplicates, ranges, joins, leakage, temporal order, spatial reference, and sampling structure as applicable.
5. Specify transformations, exclusions, model assumptions, parameters, and validation design before interpreting results.
6. Use appropriate baselines and sensitivity analyses.
7. Verify numerical results with independent summaries or checks where practical.
8. Create figures and tables that map to defined claims.
9. Separate calculated results from interpretation and literature comparison.
10. Record limitations, unresolved anomalies, and uncertainty states.

## Outputs

- Dataset and provenance records.
- Data-quality audit.
- Reproducible analysis code or notebook.
- Validated results, tables, and figures.
- Interpretation bounded by design and evidence.
