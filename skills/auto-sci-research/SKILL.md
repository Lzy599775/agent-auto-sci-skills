---
name: auto-sci-research
description: "总领型自动科研 Agent skill。用于统筹地理学+体育学研究中的科研自动化、长期记忆、文献库建设、idea 生成、方法设计、数据分析、机器学习、地理空间/遥感、综述与文献计量、SCI 写作、审稿回复、进化档案维护。触发于 auto-sci-research、Auto-sci-research、agent-auto-sci、自动化科研、科研 Agent、跨项目记忆、skill 总控、科研工作流编排、进化档案、AutoSci/OmegaWiki 思路迁移、K-Dense scientific-agent-skills 精简封装等任务。"
---

# Auto-sci-research

This is the umbrella skill for the user's local scientific-agent system. It replaces the earlier public label `agent-auto-sci` while keeping that phrase as a legacy trigger. It does not replace domain skills. It routes work to the right subskill, preserves reusable knowledge, and requires every major improvement to leave a visible evolution record.

Core idea:

`sources -> structured memory -> idea and method design -> data/geo/ML analysis -> manuscript or review -> critique/rebuttal -> evolution archive`

## Routing

Use this skill first when the task spans multiple research stages or asks to improve the user's local skills.

| Task | Use |
|---|---|
| Build or update the overall research-agent workflow | `agent-auto-sci-automation` |
| Machine learning, AI model design, SHAP, model evaluation | `agent-auto-sci-ai-ml` |
| EDA, statistics, publication figures, tables, dashboards | `agent-auto-sci-data-viz` |
| GIS, spatial accessibility, remote sensing, spatial ML | `agent-auto-sci-geospatial` |
| Manuscript writing, slides, posters, peer review, rebuttal | `agent-auto-sci-scicomm` |
| Hypothesis, research design, critical appraisal, evidence grading | `agent-auto-sci-methodology` |
| Sport geography empirical SCI manuscript writing | `sport-geography-sci-writing` |
| Sport geography review, systematic review, bibliometrics | `sport-geography-review-bibliometric` |
| Web-based autonomous deep research | `gpt-researcher` |
| Full academic research suite and ARS workflows | `academic-research-suite` |
| Long-running improve/verify loops | `codex-autoresearch` |
| Local PDF library reading and HTML notes | `codex-paper-reader` |
| Persona or thinking-framework skill distillation | `huashu-nuwa` |
| Academic-writing prompt reuse | `awesome-ai-research-writing` |
| External academic skill selection | `codex-academic-skills-index` |

Read `references/02_subskill_registry.md` when choosing among skills.

## Operating Contract

1. Keep the user's research project persistent. Do not treat a task as a one-off answer if it creates reusable knowledge.
2. Convert useful external repositories into local workflows, not blind copies.
3. Separate memory, workflow, scripts, data, manuscripts, figures, and review feedback.
4. Record failed attempts, rejected ideas, weak evidence, and reviewer objections as first-class knowledge.
5. Never store secrets in skill files, HTML, markdown logs, or committed examples.
6. Every major skill change must update the evolution archive HTML.

## Workflow

1. **Scope the task**
   - Identify whether this is literature, idea, method, data, spatial, ML, writing, review, or skill-evolution work.
   - Decide which subskill owns the task and which existing sport-geography skill is relevant.
   - Read `references/00_system_architecture.md`.

2. **Load project memory**
   - Check local project notes, previous skill references, and the evolution archive.
   - For sport geography, reuse the established narrative: public problem -> spatial inequity -> measurement gap -> evidence -> mechanism -> planning implication.

3. **Run the smallest reliable workflow**
   - Prefer reproducible scripts and structured tables when the task repeats.
   - Prefer clear markdown references when the task is judgment-heavy.
   - Use external APIs only when their value justifies setup and security cost.

4. **Gate quality**
   - Verify files, scripts, outputs, citations, figures, and assumptions.
   - For manuscripts, run claim-evidence checks and reviewer-risk scans.
   - For data or models, run EDA, leakage checks, baselines, sensitivity, and reproducibility checks.

5. **Update evolution records**
   - Update `<project-root>/agent_auto_sci/evolution_archive/evolution_data.json`.
   - Run `<project-root>/agent_auto_sci/evolution_archive/update_evolution_html.py`.
   - Mention the generated HTML path in the final response.
   - Read `references/04_evolution_archive_protocol.md`.

## Reference Map

- `references/00_system_architecture.md`: total architecture and how AutoSci/OmegaWiki is adapted.
- `references/01_source_learning_notes.md`: what was learned from AutoSci and K-Dense Scientific Agent Skills.
- `references/02_subskill_registry.md`: current local subskill inventory and routing.
- `references/03_api_config_and_security.md`: API configuration, provider roles, and secret-handling rules.
- `references/04_evolution_archive_protocol.md`: how to maintain the HTML evolution archive.
- `references/05_project_routes.md`: current sport-geography review and empirical-manuscript routes.
- `references/06_external_skill_coverage_audit.md`: coverage matrix for AutoSci and K-Dense skills, including what is preserved, adapted, and intentionally excluded.
- `references/07_external_skills_deployment_20260601.md`: 2026-06-01 deployment record for gpt-researcher, nuwa-skill, ARS, autoresearch, paper reader, Codex Academic Skills, and AI writing prompts.

## Local Project Files

- `<project-root>/agent_auto_sci/00_AGENT_AUTO_SCI_总览与变更记录.md`
- `<project-root>/agent_auto_sci/evolution_archive/agent-auto-sci-evolution.html`
- `<project-root>/agent_auto_sci/evolution_archive/evolution_data.json`
- `<project-root>/agent_auto_sci/external_repos/AutoSci`
- `<project-root>/agent_auto_sci/external_repos/scientific-agent-skills`
- `<project-root>/agent_auto_sci/external_repos/gpt-researcher`
- `<project-root>/agent_auto_sci/external_repos/nuwa-skill`
- `<project-root>/agent_auto_sci/external_repos/academic-research-skills-codex`
- `<project-root>/agent_auto_sci/external_repos/codex-autoresearch`
- `<project-root>/agent_auto_sci/external_repos/Codex-Academic-Skills`
- `<project-root>/agent_auto_sci/external_repos/codex-paper-reader`
- `<project-root>/agent_auto_sci/external_repos/awesome-ai-research-writing-STRYXTN`

## Must Not Do

- Do not install all third-party skills blindly.
- Do not copy external workflows that require unavailable infrastructure without marking them as optional.
- Do not expose API keys, tokens, private PDFs, unpublished data, or reviewer-sensitive material in HTML.
- Do not create a new subskill when an existing subskill can be extended cleanly.
- Do not skip the HTML evolution archive after a meaningful skill change.

