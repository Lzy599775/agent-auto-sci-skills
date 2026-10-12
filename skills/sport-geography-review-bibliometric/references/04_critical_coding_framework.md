# Critical Coding Framework

Use this reference to turn a bibliometric corpus into a high-level review.

## 1. Why Manual Coding Is Required

Bibliometric tools show networks and trends. They do not reliably answer:

- what exposure means;
- whether accessibility implies actual use;
- which justice dimension is addressed;
- which population groups are recognised;
- whether planning implications are actionable.

Manual coding supplies the critical review layer.

## 2. Core Coding Dimensions

### Object Type

- sports facilities;
- sports parks;
- recreation facilities;
- fitness centres;
- playgrounds;
- schoolyards;
- urban parks;
- pocket parks;
- public open spaces;
- green infrastructure;
- blue-green spaces;
- active recreation infrastructure.

### Exposure / Access Metric

- Euclidean buffer;
- network distance;
- travel time;
- service area/catchment;
- 2SFCA or enhanced FCA;
- gravity model;
- supply-demand ratio;
- park area per capita;
- quality-adjusted access;
- visitation/use intensity;
- thermal/cooling exposure;
- cumulative exposure;
- perceived accessibility.

### Spatial Scale

- individual address;
- grid;
- census unit;
- neighbourhood;
- district;
- city;
- metropolitan region;
- cross-city;
- national/global.

### Population Group

- children/youth;
- older adults;
- women;
- migrants;
- low-income groups;
- ethnic/racial minorities;
- disabled people;
- residents in urban villages or informal settlements;
- heat-vulnerable populations;
- general population.

### Justice Dimension

- distributional justice: who gets access or exposure;
- procedural justice: who participates in planning and decisions;
- recognition justice: whose needs and identities are considered;
- environmental justice: unequal environmental benefit and burden;
- climate justice: unequal heat/cooling risk and adaptation capacity;
- health equity: unequal health opportunity or outcome.

### Evidence Role

- conceptual foundation;
- measurement method;
- data source innovation;
- empirical benchmark;
- vulnerable group evidence;
- planning intervention;
- policy agenda;
- critique/limitation.

## 3. Coding Rules

- Code accessibility, exposure, quality, and use separately.
- Code equality and equity separately.
- Record whether the paper measures health outcome, health behaviour, or only opportunity.
- Record whether the paper proposes actual planning interventions or only states generic implications.
- Record if the method can be transferred to Chinese urban contexts.

## 4. Synthesis Matrix

Build a matrix:

`object type x exposure metric x justice dimension x population group x planning implication`

Use the matrix to find:

- over-studied combinations;
- neglected groups;
- missing methods;
- gaps between measurement and policy;
- opportunities for a new review contribution.

## 5. Evidence-to-Argument Conversion

Convert paper-level coding in four explicit steps:

1. **Paper-level evidence**: record the source-reported finding, full-text status, exact source locator, design, context, population, exposure/concept, outcome, method, direction, uncertainty, and boundary conditions in the Evidence Trace.
2. **Comparable dimensions**: compare only dimensions that are substantively aligned. Keep accessibility, exposure, availability, quality, and use as separate concepts; keep equality, equity, and justice as separate concepts.
3. **Cross-paper relation**: link Evidence IDs in the Cross-paper Argument Map as supporting, contradictory, contextual, partial, or not supported. Record heterogeneity in population, context, exposure/concept, outcome, scale, time, design, confounding adjustment, and measurement before labelling evidence as convergent or conflicting.
4. **Synthesis claim**: state the narrowest claim supported by the relation map, including uncertainty, competing explanations, boundary conditions, and unresolved gaps. Evidence strength is a reasoned narrative judgement based on design, data quality, comparability, uncertainty, consistency, and competing evidence; it is not a count or score.

Do not turn correlation, feature importance, RF/SHAP output, or bibliometric co-occurrence into a causal mechanism. An abstract-only record remains `ABSTRACT_ONLY` and cannot supply a fabricated full-text locator.

