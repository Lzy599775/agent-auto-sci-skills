# Research Workflow Router

Route from the user's goal and available inputs. The user does not need to name a workflow.

This is a general-purpose research system. No discipline, paper, dataset, or demonstration
case is a default topic. Domain Skills are optional specialists selected for the actual task.

| Signals | Primary workflow | Common companion |
|---|---|---|
| literature, papers, references, DOI, Zotero, review | [Literature review](literature_review.md) | [Paper artifact availability protocol](PAPER_ARTIFACT_AVAILABILITY_PROTOCOL_V1.md); [Citation-claim audit](citation_claim_audit.md) |
| design appraisal, estimand, identification, bias, sampling/measurement validity, model appropriateness | [Methodology / Research Design](methodology.md) | `agent-auto-sci-methodology`; [Data analysis](data_analysis.md) only when execution is needed |
| reproduce, replicate, reimplement, benchmark | [Paper reproduction](paper_reproduction.md) | [Data analysis](data_analysis.md) |
| clean data, fit a model, execute statistics/regression, evaluate prediction performance | [Data analysis](data_analysis.md) | [Figure workflow](figure_workflow.md) |
| draft, rewrite, or restructure Introduction, Methods, Results, Discussion, manuscript | [Manuscript writing](manuscript_writing.md) | [Per-manuscript exemplar workflow](PER_MANUSCRIPT_WRITING_EXEMPLAR_WORKFLOW_V1.md); [Citation-claim audit](citation_claim_audit.md) |
| citation supports claim, verify sentence, source checking | [Citation-claim audit](citation_claim_audit.md) | [Literature review](literature_review.md) |
| plot, chart, table, map, figure, visualization | [Figure workflow](figure_workflow.md) | [Data analysis](data_analysis.md) |
| new idea, research topic, novelty, feasibility | [Research idea evaluation](research_idea_evaluation.md) | [Literature review](literature_review.md) |

## Routing procedure

1. Identify the decision or deliverable, not only keywords.
2. Inspect available sources, files, repository instructions, and access constraints.
3. Select one primary workflow; add companions only when they protect validity or complete the deliverable.
4. Create an execution plan for long or multi-stage tasks.
5. Apply the relevant standards from `docs/standards/`.
6. Report the selected route and concise final quality-control results.

## Deliverable precedence

- Scientific method/design critique (including a Methods section) -> `methodology`, with
  `agent-auto-sci-methodology`. Model suitability is a judgment; fitting/evaluation is execution.
- Cleaning files, executing regression, or evaluating a predictive model -> `data_analysis`.
- Novelty/feasibility of a new direction -> `research_idea_evaluation`; methodology is optional.
- Methods text rewriting -> `manuscript_writing`; method validity appraisal -> `methodology`.
- Reproducing a published model/result -> `paper_reproduction`; add methodology/data analysis
  as needed. Artifact identity/availability checks alone use literature plus the artifact protocol.
- A compute resource check is a precondition, not a new scientific owner. For a standalone
  pre-compute check use `data_analysis` in `preflight_only` mode; do not start computation.
- Micro-edits use the lightweight writing mode without private exemplar-state access.

The [decision contract](ROUTING_DECISION_CONTRACT_V1.json) encodes these deliverable-level
choices for deterministic validation. It consumes an interpreted intent, not raw keywords.
Mixed goals use one primary deliverable plus necessary companions; never route solely on
Methods, model, causal forest, a test prompt, or a field name.

## Project-state boundary

Research questions, data sources, papers/Zotero collections, methods, results, figures, manuscript
state, Master20, and Core3 belong to their private project. Never inherit another project's state
or select a global corpus. Resolve explicit project/manuscript identity before reading private
state. Missing identity means ask/mark uncertain without probing candidate projects. Ordinary
method consultation, search, analysis, and micro-edits do not initialize Master20/Core3.

## Automatic companion contracts

- Any online paper search automatically applies the paper artifact protocol to every user-facing, shortlisted, evidence-table, method-comparison, exemplar, or synthesis paper. Raw monitor candidates remain exempt until qualified; see the protocol's tiered triggers.
- Any substantive manuscript writing automatically checks the isolated per-manuscript state before drafting or restructuring. Micro-edits bypass heavy initialization. Users do not need to name a Skill or repeat either trigger.

## Universal gates

- Verify current or uncertain external information.
- Preserve raw data and original source text.
- Distinguish source fact, derived result, and inference.
- Record important provenance and decisions.
- Stop before destructive, publishing, submission, credential, or ambiguous scientific-choice boundaries.
