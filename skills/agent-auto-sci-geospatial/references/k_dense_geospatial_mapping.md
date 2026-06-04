# K-Dense Geospatial Mapping

Use this reference when adapting K-Dense geospatial, GeoPandas, and remote-sensing skills to the user's sport-geography research.

## 1. Included Skill Families

| K-Dense skill family | Local use | Domain adaptation |
|---|---|---|
| `geomaster` | broad geospatial workflow, CRS, raster/vector, remote sensing | acts as the high-level GIS reasoning layer |
| `geopandas` | vector data cleaning, overlay, dissolve, spatial join, buffers | neighborhoods, parks, sport facilities, service areas |
| raster tooling | raster read/write, zonal statistics, reprojection | NDVI, LST, LCZ, impervious surface, canopy |
| network analysis | graph construction, shortest path, catchments | walking/cycling/transit access to parks and facilities |
| spatial statistics | spatial autocorrelation, clustering, spatial regression | equity hot spots, residual patterns, scale effects |
| data/viz helper skills | map export and figure design | publication-ready maps and legends |

## 2. Spatial Workflow

1. Inventory layer type, CRS, resolution, date, source, and license.
2. Fix invalid geometries and duplicate IDs.
3. Choose an analysis CRS before distance or area operations.
4. Harmonize spatial units and temporal windows.
5. Compute exposure/accessibility with explicit assumptions.
6. Run sensitivity checks for buffer/network/radius/threshold.
7. Check spatial autocorrelation and scale effects.
8. Export analysis-ready tables, maps, and reproducible scripts.

## 3. CRS And Geometry Rules

- Do not calculate distance or area in EPSG:4326.
- For city-scale China studies, use an appropriate projected CRS, documenting why.
- Keep raw geometry and processed geometry separate.
- Validate geometries before overlay.
- Record whether boundaries are administrative, statistical, planning, or custom grids.
- For maps involving China locator or national boundary, use compliant official standard-map material.

## 4. Raster/Remote-Sensing Rules

For NDVI/LST/LCZ or similar rasters:

- check acquisition date and season;
- check cloud, missing pixels, and resampling;
- avoid mixing resolutions without documenting aggregation;
- use zonal statistics with explicit unit and aggregation rule;
- compare raster date to facility/park/population data date;
- report uncertainty or sensitivity when exposure depends on thresholding.

## 5. Network Accessibility Rules

Define:

- travel mode: walking, cycling, driving, transit;
- network source: OSM, official road network, GTFS, custom;
- impedance: time, distance, slope, crossing, barriers;
- facility eligibility: type, quality, capacity, public/private, opening status;
- catchment function: cumulative opportunity, gravity, 2SFCA, Gaussian decay;
- demand weighting: population, vulnerable groups, age group.

Potential access is not actual use. State this in manuscripts.

## 6. Spatial ML Rules

When combining spatial data and ML:

- build spatially blocked validation;
- check autocorrelation in residuals;
- avoid random train/test split for gridded spatial data;
- include simple spatial/statistical baselines;
- interpret SHAP or feature importance as model explanation only;
- report transferability limits across cities.

## 7. Map Export Rules

Each map should include:

- meaningful title/caption;
- data source and year;
- scale bar and north arrow when spatial orientation matters;
- legend with units;
- projection or CRS note where relevant;
- compliant locator if national context is shown;
- uncertainty or missing-data notation when needed.

