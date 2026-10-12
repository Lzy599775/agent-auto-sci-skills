# Research Workflow Router

Route from the user's goal and available inputs. The user does not need to name a workflow.

| Signals | Primary workflow | Common companion |
|---|---|---|
| literature, papers, references, DOI, Zotero, review | [Literature review](literature_review.md) | [Paper artifact availability protocol](PAPER_ARTIFACT_AVAILABILITY_PROTOCOL_V1.md); [Citation-claim audit](citation_claim_audit.md) |
| reproduce, replicate, reimplement, benchmark | [Paper reproduction](paper_reproduction.md) | [Data analysis](data_analysis.md) |
| CSV, XLSX, dataset, statistics, model, regression | [Data analysis](data_analysis.md) | [Figure workflow](figure_workflow.md) |
| Introduction, Methods, Results, Discussion, manuscript | [Manuscript writing](manuscript_writing.md) | [Per-manuscript exemplar workflow](PER_MANUSCRIPT_WRITING_EXEMPLAR_WORKFLOW_V1.md); [Citation-claim audit](citation_claim_audit.md) |
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

## Automatic companion contracts

- Any online paper search automatically applies the paper artifact protocol to every user-facing, shortlisted, evidence-table, method-comparison, exemplar, or synthesis paper. Raw monitor candidates remain exempt until qualified; see the protocol's tiered triggers.
- Any substantive manuscript writing automatically checks the isolated per-manuscript state before drafting or restructuring. Micro-edits bypass heavy initialization. Users do not need to name a Skill or repeat either trigger.

## Universal gates

- Verify current or uncertain external information.
- Preserve raw data and original source text.
- Distinguish source fact, derived result, and inference.
- Record important provenance and decisions.
- Stop before destructive, publishing, submission, credential, or ambiguous scientific-choice boundaries.
