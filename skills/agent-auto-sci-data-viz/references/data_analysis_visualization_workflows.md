# Data Analysis and Visualization Workflows

## 1. EDA Report Structure

Every dataset should get:

- file path and timestamp;
- row/column count;
- data dictionary;
- missingness table;
- duplicate check;
- range and unit check;
- categorical level count;
- spatial/temporal coverage when relevant;
- recommended downstream analysis.

## 2. Statistical Planning

Before tests, define:

- research question;
- outcome variable;
- predictors or groups;
- design: independent, paired, repeated, spatial, temporal;
- assumptions;
- effect size;
- multiple-comparison control;
- practical interpretation.

## 3. Figure Planning Rule

For each figure:

| Field | Question |
|---|---|
| Claim | What does this figure prove? |
| Data | Which file/table supports it? |
| Visual form | Map, line, bar, scatter, box, heatmap, network, matrix |
| Encoding | Color, size, shape, facet, labels |
| Uncertainty | CI, SE, bootstraps, sensitivity |
| Caption | Can it be understood without the main text? |

## 4. Publication Figure Standards

- Use vector PDF/SVG for line art when possible.
- Use at least 300 dpi for raster images.
- Avoid `jet` and rainbow colormaps.
- Prefer perceptually uniform continuous maps: `viridis`, `cividis`, `magma`.
- Use diverging palettes only for meaningful midpoint data.
- Keep panel labels consistent.
- Avoid overfilled legends.

## 5. Bibliometric and Review Figures

For review papers, figures should include:

- PRISMA flow;
- annual trend and phase division;
- keyword co-occurrence or thematic evolution;
- co-citation or intellectual structure;
- critical coding evidence map;
- policy agenda matrix.

Each bibliometric figure must connect to a research question and a short interpretation.


