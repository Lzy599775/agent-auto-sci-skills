# Workflow Playbook

This playbook gives route-specific instructions for geography + sport + urban health review and radar tasks.

## M1. Bibliometric + Critical Review

Use when the user wants CiteSpace, VOSviewer, bibliometrix, knowledge maps, hotspots, or thematic evolution.

Required workflow:

1. Define concept boundary: object terms, exposure/accessibility terms, health/activity terms, equity terms, exclusions.
2. Use WoS + Scopus by default; keep database exports separate until deduplication.
3. Record search date, query, fields, language filters, document type filters, and export options.
4. Clean records: DOI/title deduplication, author keyword normalization, thesaurus for synonyms.
5. Run bibliometrics:
   - performance: annual output, journals, countries, institutions, authors;
   - science mapping: co-word, co-citation, bibliographic coupling, thematic evolution;
   - turning points: burst keywords/references and timeline clusters.
6. Add manual coding:
   - facility / exposure object;
   - exposure/accessibility metric;
   - spatial scale;
   - population group;
   - justice/equity dimension;
   - health or physical-activity pathway;
   - planning implication.
7. Synthesize a critical framework and policy agenda.

Quality gate:

- Contribution cannot be “we used CiteSpace/VOSviewer”.
- Every major cluster needs interpretation beyond keyword labels.
- Figures must support a claim about field evolution, method gap, or policy implication.

## M2. Systematic Review

Use when the user needs transparent, reproducible, inclusion-rule-driven synthesis.

Required workflow:

1. Select PEO or PICOS.
2. Register or draft protocol if appropriate.
3. Search multiple databases according to the health/sport/geography scope.
4. Deduplicate and screen title/abstract, then full text.
5. Preserve exclusion reasons.
6. Extract exposure, outcome, population, methods, confounders, effect direction, limitations.
7. Assess risk of bias or evidence quality.
8. Synthesize by exposure type, health outcome, population strata, method, and setting.

Quality gate:

- Do not use systematic-review language without screening records.
- Do not report pooled effects unless meta-analysis assumptions are met.
- Use causal language only when supported by design and sensitivity checks.

## M3. Scoping Review

Use when the goal is to map concepts, methods, data types, or evidence gaps.

Required workflow:

1. Define the concept and boundaries.
2. Search broadly enough to cover the field.
3. Chart evidence rather than estimate effect size.
4. Build evidence maps by topic, method, scale, population, and geography.
5. End with a research agenda, not a causal conclusion.

Quality gate:

- The output must explain what is known, how it has been studied, and what remains uncharted.
- It should not claim exhaustive effect evidence unless it followed a systematic review design.

## M4. Green Exposure / Sports Park Exposure

Core dimensions:

- Object: parks, sports parks, sports facilities, green/open space, blue-green infrastructure, street greenery.
- Exposure: NDVI/EVI, vegetation coverage, visible green, park area, distance, duration, quality, perceived exposure.
- Mechanism: physical activity, restoration, social contact, thermal mitigation, air/noise pathways.
- Equity: opportunity, process, outcome, vulnerability, intersectional disadvantage.

Required caution:

- Exposure is not use.
- Park proximity is not health benefit.
- Green quantity is not green quality.

## M5. Green Park / Sports Facility Accessibility

Core dimensions:

- Network distance/time, entrances, barriers, service capacity, opening hours, facility quality.
- Methods: cumulative opportunity, gravity, 2SFCA/E2SFCA, space-time accessibility, multimodal accessibility.
- Demand: population density, age, sex, income, vulnerability, sport preference.

Quality gate:

- Always separate accessibility from availability, quality, affordability, safety, and actual participation.
- Run sensitivity checks for buffers, travel mode, supply capacity, and demand assumptions.

## M6. Remote-Sensing Heat Exposure

Core dimensions:

- Data: Landsat, MODIS, Sentinel, ECOSTRESS, ERA5, weather stations, LCZ, building morphology.
- Metrics: LST, UHI, heatwave days, nighttime heat, UTCI, WBGT, population-weighted exposure.
- Methods: retrieval, downscaling, fusion, ML, spatial-temporal interpolation, uncertainty analysis.
- Outcomes: mortality, ER visits, cardiovascular, respiratory, mental health, heat illness.

Quality gate:

- Record spatial and temporal mismatch between remote-sensing observations and health outcomes.
- Distinguish surface temperature from air temperature and human thermal stress.

## M7. Heat-Green Compound Exposure

Core questions:

- Does green exposure mitigate heat exposure?
- Does the effect vary by urban morphology, season, socioeconomic status, or baseline vulnerability?
- Are there non-linear, lagged, or interaction effects?

Methods:

- Interaction models, GAM, DLNM, multilevel models, spatial random effects, interpretable ML, sensitivity to exposure windows.

Quality gate:

- Do not assume green always cools or benefits all groups equally.
- State whether the study evaluates co-exposure, mediation, moderation, or combined risk.

## M8. Urban Exposure + Public Health / Medical Databases

Required workflow:

1. Identify health data type: cohort, survey, hospital, insurance, registry, CDC/public health, mortality.
2. Define linkage unit: home coordinate, grid, tract, ZIP/postcode, district, city.
3. Define exposure windows: daily, seasonal, annual, long-term, life-stage.
4. Stratify by age, sex, socioeconomic status, chronic disease, and vulnerability when data allow.
5. Adjust for individual and area-level confounders.
6. Audit spatial autocorrelation, selection bias, ecological fallacy, privacy, and ethics.

Quality gate:

- If individual-level location is unavailable, frame results at area level.
- If temporal alignment is weak, avoid acute-effect claims.

## M9. Geospatial AI / CV-to-RS Frontier Radar

Use before formal review or empirical design when the user asks for recent methods or publishable ideas.

Search sources:

- arXiv, OpenReview, CVF, IEEE/ISPRS/ACM pages, Papers with Code, GitHub, Hugging Face, official dataset/benchmark pages.

Score each candidate:

- novelty;
- technical depth;
- evidence and ablation;
- reproducibility;
- trend signal;
- transferability to urban exposure / remote sensing;
- fit to the user's target journal and data access.

For every transferable CV/AI method, report:

- transferable component;
- required adaptation to remote sensing or urban exposure;
- candidate datasets;
- first falsifiable experiment;
- risk.

Quality gate:

- Trend does not equal evidence.
- GitHub popularity does not equal scientific contribution.
- Recent arXiv work needs publication status and reproducibility checks.

## Formal Corpus / Radar Candidate Handoff Template

Use this template when a project combines formal review search with current-source radar.

| Field | Required value |
|---|---|
| Title / project | Exact title or repository name |
| Source | WoS, Scopus, PubMed, arXiv, OpenReview, GitHub, Hugging Face, conference page, dataset page |
| Date checked | YYYY-MM-DD |
| Status | `formal-corpus`, `radar-candidate`, `background-method`, or `excluded` |
| Inclusion rule passed | yes/no/not-applicable |
| Reason | One sentence explaining the status |
| Permitted manuscript use | corpus evidence, method outlook, future agenda, background only, or excluded |

Decision rules:

1. Use `formal-corpus` only for records that satisfy the review protocol.
2. Use `radar-candidate` for current papers/projects worth tracking but not yet protocol-eligible.
3. Use `background-method` for transferable AI/CV/RS methods that inform future research but do not answer the review question directly.
4. Use `excluded` for modality, topic, quality, or access mismatch.

This prevents recent arXiv/GitHub items from contaminating systematic counts while still preserving their value for future agenda writing.
