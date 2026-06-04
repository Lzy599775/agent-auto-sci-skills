# API And Checkpoint Templates

Use this reference when adding automation, API access, long-running research checks, or project-memory checkpoints. Never store secrets in a skill file, HTML file, markdown note, or example output.

## 1. API Role Map

| API or service role | Use | Safe local configuration |
|---|---|---|
| literature search API | refresh candidate papers, metadata, citation links | `.env` variables only; store search logs without keys |
| Semantic Scholar-like API | citation graph, abstracts, paper metadata | cache only public metadata and query dates |
| arXiv-like API | preprint discovery | record that preprints are not peer-reviewed |
| DeepXiv or review LLM | optional novelty/review signal | record model/provider/date; never treat as authority |
| Crossref/OpenAlex-like API | DOI metadata and bibliographic enrichment | keep raw query and cleaned output separate |
| local PDF tools | extract title/abstract/full text from user PDFs | do not upload private non-OA PDFs unless user explicitly approves |

## 2. Secret Handling

Required rules:

- Use environment variables or local `.env` files excluded from version control.
- Do not paste API keys into `SKILL.md`, references, evolution HTML, screenshots, or examples.
- If a key appears in a log, stop and tell the user it must be rotated.
- Separate public metadata from private downloaded PDFs.

Suggested variable names:

```text
SEMANTIC_SCHOLAR_API_KEY=
OPENALEX_EMAIL=
DEEPXIV_API_KEY=
REVIEW_LLM_API_KEY=
ZOTERO_API_KEY=
```

## 3. Source Manifest Template

Use this for project-level ingestion:

| column | required | notes |
|---|---|---|
| `source_id` | yes | stable local ID |
| `title` | if available | paper/report/dataset title |
| `authors` | if available | use as text, not authority key |
| `year` | if available | integer |
| `source_type` | yes | PDF, CSV, XLSX, SHP, GeoJSON, TIF, DOCX, note |
| `path_or_url` | yes | local path or web URL |
| `database` | if literature | WoS, Scopus, PubMed, CNKI, manual, GitHub |
| `access_status` | yes | OA, non-OA manual, local-only, public |
| `topic_tags` | yes | controlled tags |
| `screening_status` | yes | unscreened, included, excluded, uncertain |
| `quality_notes` | optional | data or evidence concerns |
| `last_checked` | yes | ISO date |

## 4. Checkpoint Manifest Template

Use this for every multi-step workflow:

| column | required | notes |
|---|---|---|
| `checkpoint_id` | yes | e.g. `ckpt_20260529_001` |
| `project` | yes | project name |
| `stage` | yes | ingest, screen, code, analyze, write, review, revise |
| `inputs` | yes | paths or source IDs |
| `outputs` | yes | paths or planned artifacts |
| `decision` | yes | continue, revise, stop, user-review |
| `reason` | yes | why this decision was made |
| `risks` | optional | evidence, method, data, copyright, privacy |
| `next_action` | yes | one executable next step |
| `updated` | yes | ISO date |

## 5. Failure Memory Template

Record failures because AutoSci's useful idea is not only automation, but accumulating research experience.

| column | meaning |
|---|---|
| `failure_id` | stable ID |
| `task` | what was attempted |
| `input` | data, paper set, query, code, or assumption |
| `failure_type` | no data, weak novelty, method invalid, tool error, journal mismatch, evidence gap |
| `symptom` | what happened |
| `diagnosis` | why it likely happened |
| `reuse_value` | what future work should learn |
| `status` | unresolved, workaround, resolved, abandoned |

## 6. Automation Readiness Checklist

Before turning a repeated task into automation, confirm:

- the input format is stable enough;
- the output can be validated;
- failure cases are foreseeable;
- private or non-OA sources will not be exposed;
- the user benefits from repetition rather than a one-off manual pass;
- the workflow has a clear owner skill.

