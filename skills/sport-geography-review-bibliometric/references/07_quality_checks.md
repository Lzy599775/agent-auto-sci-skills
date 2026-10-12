# Quality Checks

Use this reference before finalising a review or bibliometric manuscript.

## 1. Scope Checks

- Does the title match the actual corpus?
- Are sports facilities, parks, green space, and public open space defined clearly?
- Is the field framed as sport geography / urban health geography rather than generic green-space research?
- Are exclusions justified?

## 2. Search Checks

- Are all search strings saved verbatim?
- Are search dates stated?
- Are databases and indexes stated?
- Are language, document type, and year limits stated?
- Is de-duplication reproducible?
- Are full-text exclusion reasons recorded?

## 3. Bibliometric Checks

- Are thesaurus rules saved?
- Are VOSviewer/CiteSpace/bibliometrix parameters recorded?
- Are Early Access and future-year records handled consistently?
- Are maps interpreted as evidence rather than decoration?
- Are raw and cleaned datasets preserved?

## 4. Citation Checks

- Verify every DOI in final references.
- Check author names, years, journal names, and titles.
- Do not rely on model-generated citations.
- Separate OA availability from inclusion quality.

## 5. JCR/CAS Checks

- Treat partition labels as working labels until verified.
- Use the user's institutional JCR/CAS access for final confirmation.
- Record the edition/year of the partition source.

## 6. Argument Checks

- Does each major claim map to a figure, table, citation, or coding result?
- Does Discussion explain mechanisms and planning implications?
- Does the manuscript avoid overclaiming causality?
- Are accessibility, exposure, quality, and use separated?
- Are equality, equity, and justice separated?

## 7. Evidence Synthesis Contract Checks

- Does every major synthesis claim have an `Argument_ID`?
- Does every `Argument_ID` trace to one or more `Evidence_ID`s?
- Does every `Evidence_ID` trace to a paper and a source locator with section/page/table/figure/supplement detail where available?
- Are supporting and contradictory evidence both retained?
- Are `most studies`, `consensus`, `widely established`, and `consistent evidence` supported by a traceable corpus-level comparison rather than impression?
- Is every abstract-only record labelled `ABSTRACT_ONLY` and prevented from supplying fabricated full-text locations?
- Is method similarity kept separate from empirical agreement?
- Are bibliometric patterns, SHAP, feature importance, and correlation prevented from becoming mechanisms or causal claims?
- Does the paragraph synthesis contract pass for every factual or synthesis paragraph?
- Does each citation support the paragraph's exact claim rather than merely its topic?

## 7. Skill Output Checks

When using this skill to create reusable materials:

- keep `SKILL.md` short;
- put detailed rules in `references/`;
- put templates in `assets/`;
- put repeatable scripts in `scripts/`;
- update the local corpus README/change log whenever files move or outputs are regenerated.

