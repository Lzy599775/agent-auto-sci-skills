# Tables, Figures, Formulas, and Visual Style

## Table Logic

Tables should carry information that readers may need to verify.

| Table | Purpose | Required content |
|---|---|---|
| Table 1 Data inventory | reproducibility | source, year, scale, processing, derived variable, role, limitations |
| Table 2 Variables | model transparency | variable name, abbreviation, unit, expected sign, data source |
| Table 3 Descriptive statistics | baseline | min, max, mean, SD, group/region if relevant |
| Table 4 Equity/access results | core evidence | accessibility and inequality by region/group/facility type |
| Table 5 Model results | mechanism | OLS/spatial/ML metrics, coefficients or feature importance |
| Table 6 Robustness/scenario | credibility | threshold, decay, model, or planning scenario comparison |

Do not place a table in the manuscript if it simply repeats a map without giving exact values.

## Figure Sequence for Sport Geography SCI

Default main figures:

1. Study area and resource distribution.
2. Conceptual or methodological framework.
3. Supply and demand baseline.
4. Accessibility/exposure pattern.
5. Equity and mismatch.
6. Mechanism model.
7. Green/heat/sports coupling.
8. Planning scenario.

## Map Composition

Every map must include study boundary, analysis unit, legend with unit, data year, scale bar and north arrow when appropriate, consistent projection, readable labels, and consistent classification for comparable maps.

For multi-panel maps, use the same color scale for the same metric, put a shared legend outside panels, and keep administrative boundaries light gray.

## Color Rules

| Data type | Palette logic | Notes |
|---|---|---|
| Accessibility/exposure level | sequential | light means low, dark means high |
| Positive/negative change | diverging | set zero or mean as midpoint |
| Heat risk/LST | yellow-orange-red or purple-red | keep comparable |
| Cooling effect | blue-green or blue | avoid confusing cooling with high access |
| Green exposure | yellow-green or green-blue | avoid all-green one-note maps |
| Facility categories | qualitative | colors must be distinguishable |
| Equity risk | purple/orange emphasis | separate from accessibility palette |

For sport geography, a professional palette often uses base gray for city fabric, deep teal/blue for accessibility, muted green for green exposure, orange/red for heat or deficit, purple for vulnerable-group risk, and dark gray for boundaries and labels.

## Figure Caption Formula

> Fig. X. [Main message of figure]. (a) [panel meaning]; (b) [panel meaning]; (c) [panel meaning]. Colors represent [indicator, unit, classification]. Data are from [source/year]. [If relevant] The same color scale is used across panels to support comparison.

A caption should not be only a title. It must explain the indicator and comparison logic.

## Formula Presentation

Formula section pattern:

1. Introduce why the equation is needed.
2. Present the equation.
3. Define all symbols and units.
4. Explain parameter selection.
5. State implementation details.
6. Mention sensitivity checks.

## Visual Red Flags

Reviewers may object when maps lack units, comparable panels use different color scales, SHAP plots lack mechanism interpretation, tables are redundant, formulas omit units, or strategy maps are not derived from results.

