# ML and AI Workflows for Sport Geography Research

## 1. Model Route Selection

| Research need | Preferred route |
|---|---|
| Explain facility exposure or accessibility inequality | tree-based ML + SHAP, or interpretable regression |
| Predict high-risk underserved areas | classification or ranking model with spatial validation |
| Model nonlinear relationships | random forest, gradient boosting, GAM, or neural model if data supports it |
| Time trend or panel signal | time-series or panel models before deep learning |
| Image/street-view/remote sensing extraction | deep learning or pretrained vision model, with manual validation |
| Text coding of abstracts/full text | embedding, topic modeling, supervised coding, manual audit |

## 2. Baseline First

Every ML workflow should include:

- null or majority baseline;
- simple regression or logistic model;
- tree ensemble baseline;
- domain-specific rule baseline if applicable;
- external or spatial holdout if possible.

## 3. Leakage Checks

Check:

- spatial neighbors from same place in train and test;
- same city/community split across folds;
- outcome-derived variables included as predictors;
- future data used to predict past outcomes;
- duplicate observations;
- preprocessing fitted on full data instead of train only.

## 4. Evaluation

| Task | Metrics |
|---|---|
| Regression | RMSE, MAE, R2, calibration, residual maps |
| Binary classification | AUROC, AUPRC, F1, sensitivity, specificity, calibration |
| Imbalanced classification | AUPRC, balanced accuracy, recall at fixed precision |
| Ranking/priority areas | top-k recall, precision@k, spatial concentration |
| Clustering | silhouette, stability, interpretability, spatial coherence |

Always report uncertainty, seeds, folds, and sample size.

## 5. Explainability

Use SHAP or related methods to ask:

- Which variables drive predictions?
- Are drivers stable across folds, cities, and subgroups?
- Do explanations align with urban theory?
- Are there signs of bias or proxy discrimination?

Do not say SHAP proves causality. Write it as model-attribution evidence.

## 6. Manuscript Translation

ML result claims should follow:

`model result -> robustness evidence -> plausible mechanism -> boundary -> planning implication`

Example:

`The model consistently ranked network travel time and facility quality among the strongest predictors of underserved-area status. This suggests that planning interventions should not focus only on facility counts, but the evidence remains predictive rather than causal.`


