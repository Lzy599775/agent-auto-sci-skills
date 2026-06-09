---
name: kdense-scicomm-selected
description: "精选 K-Dense Scientific Agent Skills 的科学交流工具包。用于 scientific-writing、peer-review、scientific-slides、scientific-schematics、citation-management、literature-review、markdown-mermaid-writing、research posters 等科研写作、审稿、引用、幻灯片、示意图和展示材料任务，并按 Auto-sci-research 的地理学+体育学论文路线进行封装。"
---

# K-Dense Scientific Communication Selected

This wrapper packages the selected Scientific Communication skills from `K-Dense-AI/scientific-agent-skills` for Auto-sci-research.

Use it when a task needs:

- scientific manuscript writing;
- peer-review simulation and reviewer-risk scanning;
- citation management;
- literature review workflow support;
- slides, posters, schematics, and markdown/mermaid documents.

## Included Upstream Subskills

Located in `subskills/k-dense/`:

- `scientific-writing`
- `peer-review`
- `scientific-slides`
- `scientific-schematics`
- `citation-management`
- `literature-review`
- `markdown-mermaid-writing`
- `latex-posters`
- `pptx-posters`

## Local Adaptation

Use these upstream skills with Auto-sci-research writing rules:

1. Build a claim-evidence map before drafting.
2. Select the article type: empirical IMRAD, systematic review, scoping review, bibliometric review, narrative review, or policy agenda.
3. Keep citation verification separate from prose polishing.
4. For slides/posters, use one message per visual unit.
5. For peer review, convert each criticism into a revision action, evidence need, or response boundary.

For domain-specific guidance, also read:

- `../agent-auto-sci-scicomm/references/k_dense_scicomm_mapping.md`
- `../sport-geography-sci-writing/references/journal-playbooks.md`
- `../sport-geography-review-bibliometric/references/05_manuscript_structure.md`

## Must Not Do

- Do not invent citations, DOIs, journal policies, or reviewer expectations.
- Do not polish prose in a way that expands evidence strength.
- Do not merge private PDFs or reviewer comments into public artifacts.
- Do not write review papers as one-paper-at-a-time summaries.

