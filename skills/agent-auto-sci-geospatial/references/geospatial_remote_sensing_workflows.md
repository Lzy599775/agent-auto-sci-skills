# Geospatial and Remote-Sensing Workflows

## 1. Spatial Data Audit

Create a table:

| Layer | Type | CRS | Year | Resolution/scale | Source | Role | Risk |
|---|---|---|---|---|---|---|---|

Check:

- CRS consistency;
- invalid geometries;
- duplicated features;
- missing attributes;
- raster nodata;
- temporal mismatch;
- boundary mismatch.

## 2. Accessibility Workflow

1. Define facility type and population demand.
2. Choose mode: walking, cycling, transit, driving.
3. Build network or use validated travel-time data.
4. Calculate proximity, service area, 2SFCA/3SFCA/MH3SFCA, or cumulative opportunity.
5. Run sensitivity by threshold, speed, decay, supply capacity, and demand scale.
6. Evaluate distribution by population group and spatial unit.

## 3. Green and Heat Exposure Workflow

Possible metrics:

- NDVI/EVI/SAVI;
- land cover green ratio;
- park area or public green space;
- tree canopy or urban forest quality;
- street-view green view index;
- LCZ type;
- land surface temperature;
- UTCI/PET/thermal comfort proxy.

Always state what the metric can and cannot measure.

## 4. Remote Sensing Workflow

1. Select satellite and period.
2. Apply cloud/shadow and quality masks.
3. Harmonize resolution and projection.
4. Calculate indices or classify land cover.
5. Validate with ground truth or trusted products.
6. Aggregate to analysis units with uncertainty notes.

## 5. Map Design

Every map should include:

- data year;
- scale bar;
- north arrow when appropriate;
- CRS or projection note;
- legend with units;
- boundary source;
- inset/location panel when needed;
- color choices matched to variable type.

For China maps, use standard map service resources and retain approval information when required.


