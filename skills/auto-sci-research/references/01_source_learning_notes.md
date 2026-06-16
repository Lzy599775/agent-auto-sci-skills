# Source Learning Notes

Use this file when updating the system based on external skills or repositories.

## 1. AutoSci / OmegaWiki

Source inspected: `https://github.com/skyllwt/AutoSci`.

Important local clone:

`<local-skill-workspace>/external_repos/latest/AutoSci`

### What to Learn

- Research knowledge should compound instead of resetting each task.
- Use structured entities: papers, topics, concepts, methods, ideas, experiments, summaries, outputs.
- `/init` pattern: prepare sources, discover related papers, build scaffold, ingest in parallel, rebuild index and graph.
- `/ideate` pattern: landscape scan, dual-model brainstorming, validation, novelty scoring, failed-idea memory, pilot experiments.
- `/exp-design` pattern: candidate methods, baselines, ablation, sensitivity, main experiment, generalization, deep analysis.
- `/paper-plan` pattern: evidence map drives sections; every section exists because it supports an idea or evidence item.
- `/review` pattern: independent critique improves quality; never let one model's first pass be final.
- API configuration is modular: Semantic Scholar for citation graph, DeepXiv for semantic paper search, OpenAI-compatible reviewer LLM for independent critique.

### How to Translate Locally

| AutoSci idea | Local translation |
|---|---|
| Wiki as source of truth | Use structured project folders, tables, and skill references as the source of truth. |
| Entity pages | Use markdown reference files and coding tables. |
| slash commands | Use Codex skills and scripts. |
| checkpoint JSON | Use manifests, extraction indexes, and evolution_data.json. |
| Review LLM | Use independent reviewer prompts or available tools; mark unavailable if not configured. |
| Graph visualization | Use HTML evolution archive and optional future graph/dashboard. |

### What Not to Copy Blindly

- Do not require Claude Code-specific slash commands.
- Do not require external APIs for every task.
- Do not store private corpus text in public evolution HTML.
- Do not let automated discovery overwrite the user's curated literature boundary.

## 2. K-Dense Scientific Agent Skills

Source inspected: `https://github.com/K-Dense-AI/scientific-agent-skills`.

Important local clone:

`<local-skill-workspace>/external_repos/latest/scientific-agent-skills`

### What to Learn

The repo works because each skill is narrowly scoped, triggerable, documented, and often paired with scripts or references. It also explicitly warns against installing everything blindly.

For this user, keep only these directions:

- Machine learning and AI: scikit-learn, PyTorch Lightning, transformers, SHAP, time series, model evaluation.
- Data analysis and visualization: exploratory-data-analysis, statistical-analysis, matplotlib, seaborn, scientific-visualization, networkx.
- Geospatial science and remote sensing: geomaster, geopandas, raster/vector workflows, spatial ML, STAC/COG, OSM/network analysis.
- Scientific communication: scientific-writing, peer-review, scientific-slides, posters, schematics, citation management.
- Research methodology: hypothesis-generation, scientific-brainstorming, scientific-critical-thinking, scholar-evaluation, research-grants.

### Local Adaptation Principle

K-Dense provides library-level skills. `auto-sci-research` adds project-level orchestration for sport geography, urban health, and sustainable cities research.

## 3. Hailuo AI Evolution HTML Guide

Source inspected:

`https://cdn.hailuoai.com/mcp/cdn_upload/327407489771057158/388658179654272/1776829119_793b3324.txt`

Local copy:

`<project-root>/agent_auto_sci/external_notes/AI进化可视化HTML页面制作指南.txt`

Useful pattern:

- header with current identity and update date;
- statistics grid;
- skill cards;
- memory or capability cards;
- timeline of evolution events;
- future direction section.

Local adjustment:

- Use a restrained research dashboard style rather than a decorative page.
- Do not include secrets or private full-text content.
- Maintain the page through JSON + generator script so future updates are repeatable.
