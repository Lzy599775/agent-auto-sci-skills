---
name: agent-auto-sci-scicomm
description: "科学交流与学术写作子 skill。用于论文结构、IMRAD、综述写作、图表叙事、英文润色、投稿信、审稿意见拆解、rebuttal、学术海报、PPT、研究汇报、图形摘要和文献引用管理。触发于 scientific writing、paper draft、paper plan、peer review、rebuttal、poster、slides、cover letter、citation management 等任务。"
---

# Agent Auto Sci Scientific Communication

Use this subskill when the output is a manuscript, response, slide deck, poster, abstract, or research narrative.

## Fast Workflow

1. Define target audience and venue.
2. Build a claim-evidence map before drafting.
3. Choose structure: empirical IMRAD, systematic review, scoping review, bibliometric review, policy agenda, or presentation.
4. For substantive writing, classify `WRITING_EXEMPLAR_MODE` and, when `REQUIRED`/`AUTO`, read `references/academic_writing_exemplar_protocol.md`.
5. For substantive manuscript drafting, major restructuring, or target-journal adaptation, check the generic per-manuscript exemplar workflow under this skill's ownership. It is an orchestration layer, not a second global writing owner.
   - This state check and workflow are automatic for substantive manuscript writing; do not wait for the user to name a Skill. Read the same manuscript's authoritative private state, including `MANUSCRIPT_ID`, `EXEMPLAR_STATE`, `MASTER20_VERSION`, `CORE3_VERSION`, `PROJECT_SKILL_VERSION`, and `PAPER_ARTIFACT_RECORDS`. Never infer state from chat memory or another manuscript. Micro-edits bypass heavy initialization.
6. Build `OUR_EVIDENCE_MAP` and `OUR_ARGUMENT_OUTLINE` before comparing function-matched exemplars.
7. Draft in paragraphs, not bullet lists, unless preparing an outline.
8. Check every claim against evidence.
9. Translate methods and results into field value.
10. After scientific content stabilizes, resolve `DEFAULT_ACADEMIC_WRITING_PREFERENCES` from the Academic Writing Exemplar Protocol (the sole authority; `ACADEMIC_WRITING_PROFILE_V2` is compatibility-only), then run the Academic Prose Style Guard to check positive-first framing, bilingual contrast-overuse clusters, paragraph rhythm, and semantic repetition without weakening boundaries.
11. Run reviewer-risk and citation checks.
12. For substantive rewrites, run the V2 story-relevance, sentence-increment, paragraph-contribution, fact-placement, and figure/table-citation audits before final polishing.

Keep these checks internal by default. Surface only issues that materially change scientific interpretation, estimand, sample, result, or conclusion; request author input only when safe continuation is impossible or a material scientific choice is theirs to make. Do not turn routine checks into a user-facing QC log. In manuscript prose, omit workflow/status terms such as `gate`, `guard`, `PASS`, `FAIL`, `NOT_VERIFIED`, `blocking`, `routing`, and `QC` unless they are formal research-method terms. Retain only material limitations in the manuscript and avoid repeating a boundary already stated unless the section needs it independently or the underlying judgment changes.

Read `references/scientific_communication_workflows.md`.
Read `references/academic_prose_style_guard.md` whenever generating manuscript prose, review synthesis, abstracts, conclusions, rebuttals, or substantial academic interpretation.
Read `references/academic_writing_exemplar_protocol.md` for `REQUIRED`/`AUTO` substantive writing. It supplies argument maps and rhetorical functions only; it never replaces the prose guard or SciPilot polishing owner.

For full paper projects, this skill owns title, abstract, highlights, IMRAD structure, paragraph logic, figure-text narrative, journal matching, cover letter, reference/citation checks, response-to-reviewers, and final submission readiness. Use `sport-geography-sci-writing` for field-specific empirical manuscript logic.

For deeper K-Dense-style encapsulation:

- `references/k_dense_scicomm_mapping.md`: how scientific writing, peer review, slides, schematics, and citation-management skills are adapted.
- `references/sport_geography_communication_playbook.md`: Cities/SCS/Nature-family style positioning, claim-evidence maps, rebuttal, and presentation routes.

## Writing-exemplar route

The protocol is a pre-drafting/pre-revision handoff. Use 3–5 function-matched exemplars per substantive section, record `FULLTEXT`, `ABSTRACT_ONLY`, or `METADATA_ONLY`, and keep source facts separate from inference. Learn section function, argument ordering, evidence presentation, and figure sequencing; never copy distinctive prose, citation chains, novelty claims, causal interpretation, or unsupported result logic. Draft only after `OUR_EVIDENCE_MAP` and `OUR_ARGUMENT_OUTLINE` exist. Simple proofreading and minor edits remain on the ordinary prose/lint route and do not force exemplar retrieval.

The canonical cross-client contract is documented in `docs/CROSS_CLIENT_WRITING_ROUTING_MATRIX_V1.md` and the copy-paste `CHATGPT_GLOBAL_ACADEMIC_WRITING_INSTRUCTIONS_V2.txt`.

When literature search supports a manuscript's candidate pool, automatically apply `docs/workflows/PAPER_ARTIFACT_AVAILABILITY_PROTOCOL_V1.md` to surfaced papers and require a `PAPER_ARTIFACT_RECORD_V1` for every Master 20 paper. Artifact availability is a secondary attribute, never a shortcut to Core 3 selection.

## V2 academic-writing contract handoff

Load `DEFAULT_ACADEMIC_WRITING_PREFERENCES` for every substantive academic-writing route. The required order is:

```text
whole-document/story audit
  -> OUR_EVIDENCE_MAP -> OUR_ARGUMENT_MAP
  -> exemplar protocol (REQUIRED/AUTO; SKIP for minor proofreading)
  -> draft/revise from our evidence
  -> sentence academic increment + paragraph story contribution audit
  -> Academic Prose Style Guard
  -> SciPilot writing lint and final cross-section checks
```

The V2 contract adds advisory `NOT_BUT_CONSTRUCTION_CLUSTER`, bilingual `_contrast_matches`/`AI_NEG_PARALLEL`, `AI_PARAGRAPH_RHYTHM`, `STORY_RELEVANCE_AND_DEFENSE_AUDIT`, repeated-fact/number checks, and figure/table citation-ledger checks. It also preserves Methods reproducibility, section boundaries, uncertainty, null/conflicting evidence, and the `ROBUSTNESS_PLACEMENT_RULE`. Final table artifacts use `THREE_LINE_TABLE_CONTRACT` with trimmed cell edges and OOXML verification for Word; chat Markdown tables are `PREVIEW_ONLY`; ordinary prose has no manual line breaks, and generated DOCX body text must contain no manual line breaks. Hidden formatting cleanup may be automatic, but `PROVENANCE_METADATA_STRIPPING = EXPLICIT_OPT_IN_ONLY`.

## Related Helper Skills

- `scientific-writing`
- `peer-review`
- `scientific-slides`
- `scientific-schematics`
- `citation-management`
- `sport-geography-sci-writing`
- `sport-geography-review-bibliometric`

## Must Not Do

- Do not let text polish hide weak evidence.
- Do not invent citations or journal requirements.
- Do not make policy claims without mechanism and evidence boundary.
- Do not write final manuscripts as bullets.
