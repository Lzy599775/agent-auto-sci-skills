# AutoSci Command Mapping

This reference converts AutoSci-style commands into local Codex workflows. Use it when the user asks for automated research infrastructure, project memory, idea pipelines, paper planning, or long-running research processes.

## 1. Adaptation Principle

AutoSci is treated as a workflow model, not as a command set to copy. The local implementation should preserve:

- long-horizon memory;
- source manifest and provenance;
- checkpointed research stages;
- failed-idea and failed-experiment records;
- multi-stage idea, method, paper, review, and rebuttal flow;
- visible system evolution through the HTML archive.

The local implementation should adapt these to sport geography, urban health, green/heat exposure, sport-park and facility equity, and review/bibliometric writing.

## 2. Command-to-Workflow Matrix

| AutoSci command family | Local workflow | Required output |
|---|---|---|
| `/init` | create or refresh project structure, source manifest, folder map, scope note | `source_manifest.*`, folder note, project boundary |
| `/ingest` | scan PDFs, metadata, datasets, notes, scripts, and figures into structured tables | paper inventory, data inventory, method index |
| `/discover` | search new literature and classify relevance | search log, screening table, gap map |
| `/daily-arxiv` | optional current-literature monitoring | dated update note, not a silent background claim |
| `/ideate` | generate research questions and policy-relevant ideas from evidence gaps | idea matrix with mechanism, data need, novelty, feasibility |
| `/novelty` | compare idea against WoS/Scopus/GitHub/field literature | novelty audit and conservative score |
| `/exp-design` | design empirical, spatial, ML, or review analysis plan | method matrix, baseline/sensitivity plan |
| `/exp-run` | execute scripts or manual analysis in small checkpoints | run log, outputs, errors, next action |
| `/exp-eval` | evaluate robustness, validity, bias, and interpretation | robustness table and claim boundary |
| `/paper-plan` | convert evidence into manuscript architecture | claim-evidence map, figure/table plan, section plan |
| `/paper-draft` | draft targeted sections | section draft with citation placeholders checked later |
| `/review` | run internal peer-review against target journal expectations | risk list, revision priorities |
| `/rebuttal` | decompose reviewer comments and build responses | response table, evidence-needed list |
| `/visualize` | summarize skill evolution and project outputs | updated HTML archive and timeline event |

## 3. Local Stage Gates

Every stage should pass a gate before moving forward:

| Stage | Gate |
|---|---|
| source ingestion | every source has path, type, provenance, status, and topic tag |
| literature screening | inclusion/exclusion rules are explicit and reproducible |
| idea generation | idea states mechanism, exposure/accessibility variable, population, spatial scale, and policy relevance |
| novelty check | top prior-art clusters are identified; novelty is not based only on keyword absence |
| method design | exposure, accessibility, availability, quality, and use are not conflated |
| spatial analysis | CRS, scale, MAUP, and spatial leakage are checked |
| ML analysis | baseline, split, leakage, uncertainty, and interpretability limits are checked |
| manuscript planning | every major claim has evidence, figure/table support, and citation source |
| review/rebuttal | every response maps to a manuscript change or a defensible no-change explanation |
| evolution archive | user-visible HTML and JSON are updated after meaningful skill changes |

## 4. Sport-Geography Adaptation

When AutoSci says "experiment", local workflows may mean:

- spatial accessibility calculation;
- green exposure or heat exposure measurement;
- sport facility distribution and equity analysis;
- WoS/Scopus bibliometric analysis;
- systematic review screening and critical coding;
- ML prediction or explanatory modeling;
- map, figure, and policy-agenda construction.

Do not force a lab-experiment vocabulary when the project is urban geography or public-health planning.

## 5. What To Record As Memory

Record these as persistent research memory:

- successful search strings and failed search strings;
- non-OA papers requested or manually downloaded;
- rejected topic routes and why they were rejected;
- screening decisions and ambiguous cases;
- analysis scripts, parameters, and failed runs;
- reviewer-style objections;
- journal preference observations;
- figure designs that worked or failed;
- policy framing that is too broad, too causal, or insufficiently evidenced.

## 6. Minimal Output Templates

### Source Manifest Row

| field | meaning |
|---|---|
| `source_id` | stable ID |
| `path_or_url` | local path or URL |
| `source_type` | PDF, CSV, shapefile, raster, note, script, HTML |
| `topic_tags` | e.g. sport park, green exposure, heat, equity, accessibility |
| `status` | raw, screened, coded, analyzed, excluded |
| `provenance` | database/search/source |
| `notes` | short issue or value |

### Idea Matrix Row

| field | meaning |
|---|---|
| `idea` | research idea |
| `mechanism` | plausible causal or explanatory pathway |
| `evidence_base` | literature/data support |
| `data_needed` | required data |
| `novelty_risk` | high/medium/low |
| `feasibility` | high/medium/low |
| `target_journal_fit` | Cities, SCS, UFUG, EI, Nature-family, etc. |

### Checkpoint Row

| field | meaning |
|---|---|
| `checkpoint_id` | stable ID |
| `stage` | ingest, ideate, design, run, evaluate, draft, review |
| `input` | files or assumptions used |
| `output` | generated artifact |
| `decision` | continue, revise, stop, ask user |
| `failure_or_risk` | what may break |
| `next_step` | concrete next action |

