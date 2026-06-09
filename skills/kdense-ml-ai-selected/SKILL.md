---
name: kdense-ml-ai-selected
description: "精选 K-Dense Scientific Agent Skills 的机器学习与人工智能工具包。用于 scikit-learn、PyTorch Lightning、Transformers、SHAP、time series ML、TimesFM、PyTorch Geometric、UMAP 等技术路线的科研建模封装，并按 Auto-sci-research 的体育地理、城市暴露、空间公平、健康影响和论文写作边界进行使用。"
---

# K-Dense ML/AI Selected

This wrapper packages the selected Machine Learning & AI skills from `K-Dense-AI/scientific-agent-skills` for Auto-sci-research.

Use it when a task needs technical guidance for:

- classical machine learning pipelines and model evaluation;
- deep learning training loops;
- Transformer models for text, vision, or multimodal tasks;
- model interpretability with SHAP;
- time-series ML and forecasting;
- graph neural networks;
- UMAP embeddings and dimensionality reduction.

## Included Upstream Subskills

Located in `subskills/k-dense/`:

- `scikit-learn`
- `pytorch-lightning`
- `transformers`
- `shap`
- `aeon`
- `timesfm-forecasting`
- `torch-geometric`
- `umap-learn`

## Local Adaptation

For Auto-sci-research, use these upstream skills through the following boundaries:

1. Start with transparent baselines before complex models.
2. Use spatial, temporal, or group splits when observations are geographically or temporally dependent.
3. Treat SHAP, embeddings, and feature importance as model explanations, not causal proof.
4. For review screening or text coding, keep a human-audited sample and clear coding rules.
5. For city transfer or cross-region prediction, report external validation and domain shift.

For domain-specific guidance, also read:

- `../agent-auto-sci-ai-ml/references/k_dense_ml_ai_mapping.md`
- `../agent-auto-sci-ai-ml/references/sport_geography_ml_playbook.md`

## Must Not Do

- Do not use random train/test split for spatially autocorrelated urban grid data without justification.
- Do not select a neural model before proving simpler baselines are insufficient.
- Do not use XAI output as direct causal evidence.
- Do not send private health, location, or unpublished data to external model APIs without explicit approval.

