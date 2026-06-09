---
name: kdense-geospatial-rs-selected
description: "精选 K-Dense Scientific Agent Skills 的地理空间科学与遥感工具包。用于 geomaster、geopandas、GIS、遥感、矢量/栅格处理、空间分析、空间机器学习和地球观测工作流，并按 Auto-sci-research 的体育设施可达性、绿色暴露、热暴露、LCZ、空间公平和城市健康研究进行封装。"
---

# K-Dense Geospatial / Remote Sensing Selected

This wrapper packages the selected Geospatial Science & Remote Sensing skills from `K-Dense-AI/scientific-agent-skills`.

Use it when a task needs:

- GIS workflow planning;
- vector processing and GeoPandas operations;
- remote sensing and Earth observation workflow reasoning;
- spatial ML, terrain, raster/vector, or cloud-native geospatial pipelines.

## Included Upstream Subskills

Located in `subskills/k-dense/`:

- `geomaster`
- `geopandas`

## Local Adaptation

Use these upstream skills with Auto-sci-research spatial rules:

1. Audit CRS before distance, area, buffer, or network calculations.
2. Separate exposure, accessibility, availability, quality, and actual use.
3. Record sensor, acquisition date, spatial resolution, temporal window, and resampling for remote-sensing data.
4. For heat exposure, separate surface temperature, air temperature, thermal comfort, and population-weighted exposure.
5. For maps involving China context, use compliant standard-map material.

For domain-specific guidance, also read:

- `../agent-auto-sci-geospatial/references/k_dense_geospatial_mapping.md`
- `../agent-auto-sci-geospatial/references/sport_geography_spatial_playbook.md`
- `../urban-exposure-review-radar-workflow/references/workflow_playbook.md`

## Must Not Do

- Do not calculate distance or area in unprojected geographic CRS.
- Do not treat NDVI, park area, green quality, and use as interchangeable.
- Do not use remote-sensing pixels without checking date, cloud, resolution, and aggregation.
- Do not overclaim health effects from exposure maps alone.

