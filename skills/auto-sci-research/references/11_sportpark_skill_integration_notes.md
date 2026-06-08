# Sportpark Skill Integration Notes

Use this reference when integrating prior work from the user's local Sportpark project into `agent-auto-sci-skills`.

## 1. Integration Decision

The Sportpark project contained three kinds of relevant material:

1. A duplicate snapshot of `agent-auto-sci-skills` in the Sportpark temporary Darwin analysis workspace.
2. The `darwin-skill` evaluator package in the same temporary analysis workspace.
3. Sport geography writing, figure, and role-protocol memories in the Sportpark writing and learning folders.

The integration strategy is:

- keep the Sportpark source workspace untouched;
- treat duplicated skill snapshots as already represented in this repository;
- fold Sportpark writing and figure lessons into references and routing rules;
- treat `darwin-skill` as an optional evaluation method, not a required runtime dependency;
- avoid copying private paper full text or non-public materials into public skill files.

## 2. Deduplication Rule

Use `agent-auto-sci-skills` in this repository as the canonical copy.

Do not create duplicate skills for:

- `agent-auto-sci-ai-ml`;
- `agent-auto-sci-automation`;
- `agent-auto-sci-data-viz`;
- `agent-auto-sci-geospatial`;
- `agent-auto-sci-methodology`;
- `agent-auto-sci-scicomm`;
- `auto-sci-research`;
- `sport-geography-review-bibliometric`;
- `sport-geography-sci-writing`;
- `urban-exposure-review-radar-workflow`.

If a Sportpark file improves one of these skills, add the reusable guidance to that skill's `references/` directory instead of adding a second skill with a similar name.

## 3. Reusable Sportpark Lessons

From the Sportpark writing skill:

- Start papers from the public problem and planning/health value, not from a technical model.
- Use a research-question matrix before methods are chosen.
- Keep four loops closed: problem, method, evidence, and policy.
- Introduction should move through macro pressure, object value, prior methods, concrete gaps, and study aims.
- Methods must explain spatial unit, exposure window, accessibility assumptions, variables, and reproducibility details.
- Discussion must connect findings to mechanism, literature, governance, and limitations.

From the role and review protocols:

- Separate role boundaries: writer, reviewer, citation checker, language editor, and formatter.
- Use two-round self-review before external submission.
- Keep citation and evidence boundaries explicit.
- Do not let polishing hide weak logic or unsupported claims.

From figure memories:

- Each figure should answer a manuscript question.
- Study-area maps must satisfy map compliance and design clarity.
- SHAP and response plots need interpretation boundaries.
- Each figure folder benefits from a manifest or composition note when the figure is part of a manuscript package.

## 4. Darwin-Skill Evaluation Boundary

`darwin-skill` is useful as an evolution evaluator because it emphasizes:

- rubric-based assessment;
- before/after comparison;
- test prompts;
- human-in-the-loop acceptance;
- ratcheting so skills do not regress.

Use it when changing core workflows, but do not require it for ordinary manuscript drafting. If unavailable, use the local validation checklist:

1. Does the change improve routing, evidence checks, reproducibility, or review resistance?
2. Is the added context discoverable without bloating `SKILL.md`?
3. Can the change be verified with a realistic prompt or file check?
4. Does the change avoid secrets, private full text, and fragile external dependencies?
5. Is the evolution archive updated?

## 5. Release Boundary

Before publishing to GitHub:

- run a secret scan;
- verify no private PDF text or paid database export is copied into the package;
- keep local absolute paths only as documented provenance or examples, not as required runtime paths;
- prefer summaries and workflows over raw extracted materials;
- keep `agent-auto-sci-skills` as the canonical source.
