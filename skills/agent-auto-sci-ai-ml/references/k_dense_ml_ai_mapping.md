# K-Dense ML/AI Mapping

Use this reference when adapting K-Dense machine-learning and AI skills to geography + sport science research. It preserves the useful technical workflow while adding spatial, fairness, and manuscript-quality constraints.

## 1. Included Skill Families

| K-Dense skill family | Local use | Domain adaptation |
|---|---|---|
| `scikit-learn` | classical ML, pipelines, cross-validation, preprocessing, metrics | first-line models for tabular accessibility, exposure, equity, and health-outcome prediction |
| `pytorch-lightning` | deep learning training loops and reproducibility | use only when data volume and task complexity justify neural models |
| `transformers` | text classification, topic coding, embedding, semantic retrieval | review screening, abstract coding, policy-document analysis, not unsupervised "truth" |
| `shap` | model interpretation and feature contribution | explanatory support only; never causal proof |
| `aeon` / `timesfm` | time-series modeling and forecasting | heat exposure, activity demand, temporal accessibility, longitudinal policy monitoring |
| `statistical-analysis` | model diagnostics and inference support | complements ML with effect size, uncertainty, and robustness checks |

## 2. Model Selection Tree

1. If the question is descriptive distribution or map comparison, use spatial/statistical analysis before ML.
2. If the question predicts an outcome from tabular spatial features, start with linear/logistic baseline, tree model, and random forest or gradient boosting.
3. If the question uses text, start with transparent keyword/rule coding, then embeddings or transformers if needed.
4. If the question is temporal, compare naive, seasonal, classical time-series, and ML/forecasting models.
5. If the question is spatially autocorrelated, use spatial split, spatial lag/error alternatives, or geographically aware validation.
6. If the question requires policy explanation, prioritize interpretability and robustness over marginal accuracy gains.

## 3. Baseline Hierarchy

Always define baselines before complex models:

| Task | Baselines |
|---|---|
| classification | majority class, logistic regression, decision tree |
| regression | mean/median predictor, OLS/ridge/lasso, shallow tree |
| ranking accessibility gaps | simple distance or catchment metric |
| clustering | k-means or hierarchical clustering with stability check |
| text coding | human-coded sample, keyword rules, TF-IDF + linear model |
| forecasting | naive last value, seasonal naive, ARIMA/ETS where appropriate |

## 4. Validation Rules

Use validation that respects the data-generating process:

- spatial split for neighborhood/grid/city observations;
- temporal split for longitudinal exposure or demand;
- group split when multiple observations belong to one city, school, district, or park;
- external validation when transferring across cities;
- nested validation only when model selection risk is high;
- sensitivity checks for buffer radius, travel mode, catchment threshold, and exposure definition.

## 5. Leakage Checklist

Check for leakage before reporting any metric:

- outcome variables embedded in predictors;
- post-treatment variables used as predictors;
- same park/facility or same neighborhood appearing in train and test;
- future exposure used to predict past outcome;
- spatially adjacent grids split randomly when spatial autocorrelation is strong;
- normalization fitted on the full dataset rather than training set;
- manual labels generated after seeing model output without audit trail.

## 6. XAI Rules

SHAP, permutation importance, PDP, ICE, and ablation can support interpretation, but:

- do not describe them as causal effects;
- check feature correlation before ranking importance;
- report model, sample, background data, and feature preprocessing;
- use global and local explanation only when both answer a clear claim;
- compare explanation patterns across spatial groups when equity is central;
- link explanation back to plausible urban-health or spatial-justice mechanisms.

## 7. Manuscript Reporting Minimum

For publishable ML sections, report:

- target, unit of analysis, spatial/temporal scope;
- predictors and feature engineering;
- split strategy and why it prevents leakage;
- baseline models and final model;
- metrics with uncertainty or repeated-run stability;
- hyperparameter search scope;
- interpretability method and limitations;
- robustness/sensitivity results;
- code and data availability boundary.

