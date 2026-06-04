# AutoSci Workflow and Memory Adaptation

## 1. Source Intake

Use a manifest before analysis:

| Field | Meaning |
|---|---|
| source_id | stable local ID |
| path | absolute path |
| source_type | pdf, data, note, web, script, figure |
| status | raw, extracted, coded, used, excluded |
| owner_decision | user-provided, agent-discovered, generated |
| next_action | extract, screen, code, analyze, archive |

## 2. Research Lifecycle

```text
prepare sources -> ingest/index -> discover gaps -> generate ideas -> check novelty -> design analysis/experiment -> run/evaluate -> write -> review/rebut -> update memory
```

For sport geography, experiments may mean:

- bibliometric analysis runs;
- GIS accessibility workflows;
- statistical robustness checks;
- SHAP or ML interpretation;
- map and figure generation;
- reviewer-risk audits.

## 3. Checkpointing

For any workflow that may take multiple steps, create:

- input manifest;
- parameters or query file;
- intermediate index;
- output summary;
- validation note;
- next-action list.

## 4. API Configuration

Optional external APIs should be modular:

- Semantic Scholar: citation and related-paper discovery.
- DeepXiv: semantic paper discovery and TLDR.
- OpenAI-compatible reviewer LLM: independent critique.

If not configured, continue with local files and web/manual search where appropriate. Always report the degraded path.

## 5. Anti-Repetition Memory

Record:

- rejected research ideas and why;
- failed scripts and error cause;
- weak manuscript routes;
- review objections;
- overclaimed concepts;
- metrics that did not support the expected claim.

This prevents the next task from restarting from the same weak path.


