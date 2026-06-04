# Skill Design Principles

This skill follows two external design ideas and one local corpus rule.

## 1. Prompt Library Lessons

From academic AI writing prompt libraries, keep:

- task-specific prompts rather than one generic writing prompt;
- explicit role, task, constraints, output format, and self-check;
- separate modes for translation, polishing, logic checking, reviewer perspective, figure/table titles, and full-paper review;
- clean output rules for Word/LaTeX use.

Apply this by making the skill section-aware: search protocol, review synthesis, bibliometric maps, critical coding, journal positioning, and policy agenda are separate tasks.

## 2. Nature-Style Skill Lessons

From high-impact journal skill bundles, keep:

- one skill per stable task family;
- `SKILL.md` as a compact trigger and routing layer;
- detailed rules in `references/`;
- templates in `assets/`;
- repeatable operations in `scripts/`;
- mandatory verification before claiming completion;
- figure-first thinking: define what each figure proves before choosing its visual form.

Apply this by keeping this skill focused on review/bibliometric writing, while leaving empirical SCI manuscript drafting to `sport-geography-sci-writing`.

## 3. Local Corpus Rule

This skill must remain corpus-backed.

When the user provides local PDFs, tables, or downloaded non-OA papers:

1. build or update the corpus index;
2. match PDFs by DOI where possible;
3. extract section structure;
4. summarise journal and topic patterns;
5. update the local change log;
6. only then write reusable rules.

Do not turn one batch of papers into universal rules without checking journal scope and topic composition.


