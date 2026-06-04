# Data, Methods, Statistics, and Machine Learning

## Concept Boundaries

| Concept | Meaning | Common metric | Boundary |
|---|---|---|---|
| Accessibility | Potential opportunity to reach a resource | 2SFCA/G2SFCA, network time, gravity score | Does not prove actual use |
| Exposure | Environmental condition encountered by a population | NDVI, green view, LST, LCZ, activity-space exposure | Does not prove benefit |
| Use | Actual visitation or activity | mobile data, survey, check-in, observed use | Can be biased by data platform |
| Equality | Distributional evenness | Gini, Theil, Lorenz | Not always normatively fair |
| Equity | Need-sensitive fairness | group comparison, vertical equity, mismatch | Requires normative justification |
| Benefit | health, cooling, activity, wellbeing outcome | physical activity, mental health, heat relief | Needs causal or associative design |

## Accessibility Model Reporting

For 2SFCA variants, always report supply point definition, demand unit, catchment threshold, decay function, supply capacity, demand adjustment, and sensitivity checks.

Generic wording:

> We adopted a Gaussian-based two-step floating catchment area model to estimate potential access to sports facilities. In the first step, each facility's service capacity was allocated to surrounding demand units within a predefined travel-time threshold using a distance-decay function. In the second step, each demand unit accumulated the capacity-to-demand ratios of all reachable facilities.

## Supply Capacity for Sports Facilities

Do not use facility count alone when stronger data exist. Possible capacity terms include facility area, number of courts, facility type weight, diversity index, opening hours, public/private status, price, shade, thermal comfort, and safety.

## Equity Metrics

For Gini, report unit of population ordering, resource variable, weighting population, equation, interpretation, and limitations. Use maps or typologies to locate inequality because Gini alone does not show where inequality occurs.

Use Theil when decomposing inequality into between-region and within-region components. Use Lorenz curves when the paper needs a visual distributional argument.

## Spatial Statistics

| Method | Use | Reporting |
|---|---|---|
| Global Moran's I | overall spatial autocorrelation | I, p-value, weight matrix |
| LISA | local clusters and outliers | HH, LL, HL, LH classes |
| OLS | baseline association | coefficients, diagnostics, residual spatial autocorrelation |
| SLM/SAR | spatial lag dependence | why neighbor outcome matters |
| SEM | spatially correlated omitted factors | why residual dependence matters |
| GWR/MGWR | spatially varying associations | bandwidth, coefficient maps, local R2 |

## Machine Learning

Use ML when relationships are nonlinear, interactive, or predictive. Do not use it only to appear advanced.

Report target variable, feature list, train/test split or cross-validation, metrics, hyperparameter search, overfitting checks, SHAP interpretation, and spatial-split sensitivity if spatial autocorrelation is strong.

Good SHAP sentence:

> SHAP dependence plots indicate a threshold effect: accessibility improves sharply when road-network density exceeds [value], but the marginal gain flattens thereafter. This nonlinear pattern suggests that connectivity upgrades are most effective in poorly connected communities rather than in already well-connected central areas.

## Robustness and Sensitivity

Recommended checks: catchment threshold, distance decay, supply definition, demand definition, spatial unit, model comparison, equity metric, and map classification.

## Formula Writing

For every formula: define the real-world meaning before the equation, define every symbol, state units, state parameter choice, explain why the formula matches the research question, and state what was modified if adapted.

