---
name: sport-geography-sci-writing
description: "体育地理 SCI 顶刊写作全流程技能。用于体育设施可达性、体育公园、绿地/绿色暴露、热暴露、蓝绿空间、15 分钟生活圈、环境公平、健康公平、空间机制、机器学习解释和投稿期刊适配。触发于：体育地理论文、体育设施公平、sports geography, sport facility accessibility, green exposure, heat exposure, urban green space equity, SHAP 写作、SCI 投稿、Sustainable Cities and Society、Cities、Landscape and Urban Planning、Ecological Indicators、Environmental Research、npj Urban Sustainability 等。"
metadata:
  version: "1.0.0"
  source_corpus_date: "2026-05-26"
  local_master_file: "<your-sport-geography-project>/writing"
---

# Sport Geography SCI Writing

This skill turns a sport geography or green/heat exposure study into a journal-positioned SCI manuscript. It is based on a local writing playbook and a corpus scan of sport geography, green exposure, heat exposure, and equity papers.

Use it for manuscripts about sports facilities, sports parks, urban parks, green exposure, heat exposure, accessibility, equity, spatial justice, and explainable machine learning in urban geography.

## Core Rule

Do not start from methods. Start from the manuscript contract:

`public problem -> spatial inequity -> measurement gap -> proposed framework -> decisive evidence -> mechanism -> planning implication -> boundary`

Every section must close one part of that chain. Every main claim must point to a figure, table, statistic, formula, or sensitivity check.

## Fast Workflow

1. **Position the paper**
   - Identify target journal family.
   - State the main contribution as one of: concept, metric, data, method, mechanism, scenario, or planning translation.
   - Read `references/journal-playbooks.md` for journal-specific rules.

2. **Build the argument**
   - Write a claim-evidence map before drafting.
   - For each claim, record: evidence, figure/table, interpretation, boundary.
   - Read `references/section-patterns.md` for Title, Abstract, Introduction, Study area, Data, Methods, Results, Discussion, and Conclusion patterns.

3. **Audit data and methods**
   - Confirm all variables have a role in Results.
   - Explain accessibility, exposure, equity, and use as separate concepts.
   - Read `references/data-methods-ml.md` for accessibility models, Gini/Theil, spatial models, machine learning, SHAP, and robustness.

4. **Design tables, formulas, and figures**
   - Decide what each table or figure proves before choosing its form.
   - Read `references/tables-figures-formulas.md` for table content, map composition, color, figure captions, and formula reporting.

5. **Draft and revise**
   - Keep Results descriptive but claim-led.
   - Make Discussion explain mechanisms, compare literature, translate to planning, and state boundaries.
   - Read `references/workflow-checklists.md` for pre-submission checks.

For end-to-end projects, this skill enters after the topic, literature, data, analysis, and figure plan have stable outputs. If the user asks to start from zero, route first through `auto-sci-research/references/08_full_research_to_manuscript_pipeline.md`, then return here for the empirical manuscript.

## Journal Routing

| If the main contribution is... | Prefer journal playbook |
|---|---|
| Large-scale comparison, global/cross-city evidence, concept contribution | Nature Communications / npj Urban Sustainability |
| Sustainable city, heat, resilience, green-sport coupling, full method chain | Sustainable Cities and Society |
| Urban governance, public service equity, accessibility, mechanism, policy | Cities / Applied Geography / Habitat International |
| Green space quality, park design, landscape services, blue-green planning | Landscape and Urban Planning / Urban Forestry & Urban Greening |
| Exposure metric, health pathway, systematic review, environmental justice | Ecological Indicators / Environment International / Environmental Research / Social Science & Medicine |
| Local planning, national policy, implementation strategy | Chinese planning / sport journals |

## Default Manuscript Architecture

1. Title: object + spatial problem + contribution or lens.
2. Abstract: background pressure, gap, data/method, core findings, mechanism, implication.
3. Introduction: public problem, object value, method landscape, precise gap, objectives.
4. Study area: why this place is theoretically and practically suitable.
5. Data: source, year, scale, preprocessing, uncertainty, role in analysis.
6. Methods: framework, indicator definitions, formulas, models, validation.
7. Results: spatial pattern, group/equity pattern, mechanism, scenario or robustness.
8. Discussion: mechanism interpretation, literature dialogue, planning translation, limitations.
9. Conclusion: answer research questions, state contribution, avoid new results.

## Must Not Do

- Do not equate accessibility with actual use.
- Do not equate exposure with benefit.
- Do not equate equality with equity.
- Do not write "we used SHAP" as the contribution; explain what mechanism SHAP revealed and where it is stable.
- Do not list data without scale, year, preprocessing, and known bias.
- Do not include a variable in Data/Methods if it never appears in Results or robustness checks.
- Do not use different color scales for comparable maps unless the caption explicitly justifies it.
- Do not make journal-specific claims without reading the matching playbook.

## Reference Map

- `references/paper-corpus-lessons-20260526.md`: what was learned from the 56-PDF local corpus.
- `references/section-patterns.md`: section-by-section writing logic, templates, and sentence moves.
- `references/data-methods-ml.md`: accessibility, equity, spatial statistics, machine learning, SHAP, and robustness logic.
- `references/tables-figures-formulas.md`: table, formula, figure, caption, map, and color rules.
- `references/journal-playbooks.md`: journal-specific subskills and positioning rules.
- `references/workflow-checklists.md`: end-to-end workflow and pre-submission checks.

## Local Evidence Files

When the user asks "where did this come from" or wants deeper paper-level evidence, read:

- the user's local Sportpark writing playbook when available.
- the user's local Sportpark role/protocol notes when available.
- the user's local Sportpark figure-system memories when the task is specifically about paper figures.

Do not copy private paper full text from those folders into public outputs.

