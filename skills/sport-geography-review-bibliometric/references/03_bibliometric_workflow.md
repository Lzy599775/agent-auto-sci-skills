# Bibliometric Workflow

Use this reference for VOSviewer, CiteSpace, bibliometrix, and R/Python bibliometric analysis.

## 1. Minimum Reproducible Pipeline

1. Export full records and cited references from WoS and/or Scopus.
2. Save raw files unchanged.
3. Convert to bibliometrix format.
4. De-duplicate by DOI, title, and author-year-title fallback.
5. Build a thesaurus for keywords, author names, institutions, and countries.
6. Save all cleaned intermediate data.
7. Run analysis in documented parameter blocks.

## 2. Analyses Worth Keeping

For high-impact journals, keep only analyses that support the argument.

### Performance Analysis

Use for:

- annual growth;
- source distribution;
- countries/institutions/authors;
- top cited documents.

Avoid long descriptive lists in the main text. Put full rankings in supplements.

### Collaboration Structure

Use for:

- country collaboration;
- institutional clusters;
- internationalisation patterns.

Keep in main text only if collaboration explains knowledge gaps, geographic bias, or policy transfer.

### Intellectual Structure

Use:

- co-citation clusters;
- burst references;
- timeline view;
- landmark papers.

Interpret clusters as knowledge bases, not just labels.

### Conceptual Structure

Use:

- keyword co-occurrence;
- overlay maps;
- thematic evolution;
- thematic map;
- topic modelling if justified.

Interpret as field evolution:

`physical activity / built environment -> accessibility / parks -> equity / justice / exposure / heat`

### Methodological Evolution

This is especially important for the user's topic.

Code method families:

- buffer/proximity;
- network accessibility;
- 2SFCA/gravity;
- supply-demand/optimization;
- quality/perception/audit;
- mobile phone/social media/online review;
- remote sensing and spatial morphology;
- machine learning/GeoAI;
- mixed methods/participatory methods.

## 3. Tool Roles

### bibliometrix / Biblioshiny

Use for:

- descriptive analysis;
- thematic evolution;
- three-field plots;
- source and author metrics.

### VOSviewer

Use for:

- keyword co-occurrence;
- co-authorship;
- citation/co-citation networks;
- overlay/density maps.

Clean thesaurus before final figures.

### CiteSpace

Use for:

- burst detection;
- timeline clusters;
- turning point references.

Do not overuse default cluster labels. Manually interpret labels against paper titles and abstracts.

### Python / R

Use for:

- reproducible cleaning;
- custom coding;
- figure redesign;
- heatmaps, stacked bars, Sankey/alluvial plots;
- robustness checks.

## 4. Figure Priority

Recommended main figures:

1. PRISMA + dataset profile;
2. annual evolution and source distribution;
3. thematic evolution or keyword overlay;
4. method-family evolution;
5. justice/population coding map;
6. integrated framework and planning agenda.

Move ordinary author/institution networks to supplements unless the target journal expects them.

## 5. Common Failure Modes

- Too many maps and no argument.
- Keyword clusters not interpreted.
- Early Access years handled inconsistently.
- Scopus and WoS merged without clear de-duplication.
- Search string too narrow for the real concept.
- JCR/CAS partition claims not verified.
- Bibliometrics presented as current truth without a search date.


