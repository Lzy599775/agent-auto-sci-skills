# K-Dense Data/Viz Mapping

Use this reference when adapting K-Dense data analysis and visualization skills to geography + sport science manuscripts.

## 1. Included Skill Families

| K-Dense skill family | Local use | Domain adaptation |
|---|---|---|
| exploratory data analysis | schema audit, missingness, outliers, distributions | spatial units, exposure variables, facility attributes, review metadata |
| statistical analysis | test selection, effect size, uncertainty, robustness | equity gaps, group differences, association models, sensitivity analysis |
| scientific visualization | publication-grade figures and figure logic | evidence-first maps, diagrams, bibliometric visuals, policy matrices |
| matplotlib/seaborn | reproducible figures | controlled palette, dimensions, caption, journal-safe export |
| networkx | graph/network visualizations | co-occurrence networks, collaboration networks, street/facility networks |
| xlsx/docx/pdf helpers | tables and manuscript artifacts | screening tables, coding sheets, appendix tables |

## 2. EDA Minimum

Before statistics or figures, audit:

- row count, unit of analysis, spatial scale;
- variable definitions and units;
- missingness by variable and spatial group;
- duplicate IDs, invalid geometries, invalid coordinates;
- distribution shape and outliers;
- temporal coverage;
- category imbalance;
- consistency between raw data, cleaned data, and analysis-ready data.

## 3. Statistical Decision Rules

| Research need | Preferred output |
|---|---|
| describe access or exposure distribution | summary table, histogram/density, map, inequality index |
| compare groups | effect size + CI, not only p-value |
| test association | model coefficient, uncertainty, diagnostics |
| compare spatial scenarios | paired difference, sensitivity chart, map of changes |
| review coding reliability | coder agreement, uncertain-code table |
| bibliometric trend | annual trend, normalized topic growth, burst period |

## 4. Figure Quality Rules

Every figure should answer one claim. Before export, check:

- title/caption states the question, not only the variable name;
- color scale matches variable type;
- legend units are clear;
- labels are readable at journal column width;
- maps include scale, north arrow, CRS/projection note if needed;
- color remains interpretable in grayscale and colorblind conditions;
- figure and caption do not imply causality beyond design.

## 5. Table Quality Rules

Use tables for precise comparison:

- define rows and columns by the decision the reader must make;
- include sample size and missingness;
- avoid too many decimal places;
- show effect size, uncertainty, and method notes;
- separate main-text tables from appendix evidence tables;
- for review papers, include inclusion criteria, coding dimensions, and evidence strength.

## 6. Reproducible Export

Record:

- input file paths;
- script path;
- package versions where relevant;
- random seed if sampling or layout algorithms are used;
- output dimensions;
- output file path;
- journal target or expected use.

