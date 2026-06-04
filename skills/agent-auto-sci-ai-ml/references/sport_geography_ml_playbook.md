# Sport Geography ML Playbook

Use this reference for ML/AI tasks in sport parks, sport facilities, green exposure, heat exposure, urban health, spatial equity, and literature-review coding.

## 1. Common Research Tasks

| Task | Suitable models | Key risks |
|---|---|---|
| identify underserved sport-facility areas | interpretable classification/ranking, clustering | conflating low supply with low need |
| predict park-use or physical-activity opportunity | regression, count models, tree ensembles | missing behavior data, selection bias |
| explain inequity in access | transparent regression + SHAP/tree models | causal overclaim |
| classify literature themes | human-coded sample + transformer/embedding support | hallucinated labels, weak codebook |
| forecast heat exposure or activity demand | time-series baseline + ML | future leakage, nonstationarity |
| integrate remote-sensing features | regularized models, tree ensembles, spatial CV | scale mismatch and spatial autocorrelation |

## 2. Feature Families

Use controlled feature groups:

- built environment: density, land use, road network, block size, POI mix;
- sport opportunity: facility count, type diversity, capacity proxy, quality proxy, opening hours if available;
- green/blue exposure: NDVI/EVI, canopy, park area, water, vegetation quality;
- thermal environment: LST, UTCI/heat index proxy, LCZ, impervious surface;
- accessibility: network time, 2SFCA, gravity access, cumulative opportunity;
- population vulnerability: age, income, migrants, disability, students, older adults;
- demand and behavior: population, physical-activity proxies, social media/check-in if defensible;
- policy context: planning zones, park-service standards, regeneration areas.

## 3. Domain-Specific Splits

| Data structure | Preferred split |
|---|---|
| single city, grid/neighborhood units | spatial block split or district-level group split |
| multiple cities | leave-one-city-out or city-stratified split |
| repeated years | train on earlier years, test on later years |
| park-level observations | split by park or district, not random visits |
| literature abstracts | split by paper, not by sentence |

## 4. Equity Diagnostics

After model training, examine:

- metric performance by district, income, age, migrant status, and urban/rural group;
- false-negative areas where underserved places are missed;
- feature importance stability across vulnerable groups;
- whether the model reproduces unequal data availability;
- whether policy recommendations prioritize high-need but low-data areas.

## 5. Claim Boundaries

Use precise language:

- "associated with" for observational models;
- "predicts" only when held-out validation supports prediction;
- "explains model output" for SHAP or feature importance;
- "suggests a mechanism" only when literature and robustness align;
- "identifies priority areas" only when need, supply, and vulnerability are jointly considered.

## 6. Reviewer-Ready Checks

Before using ML in a Cities/SCS/UFUG/EI-style manuscript:

- show why ML is necessary beyond descriptive spatial analysis;
- include simple baselines;
- report spatial leakage prevention;
- include robustness for spatial scale and exposure definitions;
- connect model interpretation to planning or public-health implications;
- include limitations on representativeness, causal inference, and data quality.

