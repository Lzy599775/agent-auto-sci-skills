# Darwin Evaluation: ARS Subskill Packaging

Date: 2026-06-07

Scope: `urban-exposure-review-radar-workflow` with vendored `subskills/academic-research-suite`.

Upstream package:

- Codex package: `Imbad0202/academic-research-skills-codex` v0.1.12
- Upstream ARS content: `Imbad0202/academic-research-skills@529c6d25a3778843fb94edf9f03eda4cd7e0f416`
- License: CC BY-NC 4.0, attribution and non-commercial restriction preserved in `subskills/academic-research-suite/LICENSE`

## Score

Darwin 9-dimension score: 86.4 / 100

| Dimension | Weight | Score | Weighted | Evidence |
|---|---:|---:|---:|---|
| Frontmatter quality | 7 | 9.0 | 6.3 | Name is stable; description includes urban-exposure triggers plus ARS aliases; description length is under 1024 characters. |
| Workflow clarity | 12 | 9.0 | 10.8 | Parent workflow has route decision, journal gate, formal/radar separation, and ARS routing sequence. |
| Failure-mode encoding | 12 | 9.0 | 10.8 | Parent workflow has explicit failure/fallback table and keeps formal corpus separate from frontier radar. |
| Checkpoint design | 6 | 8.0 | 4.8 | Checkpoints exist for route ambiguity, journal gate, corpus validity, causality, and sensitive data modalities. Could be stronger with explicit red-light labels. |
| Executable specificity | 17 | 8.5 | 14.5 | Concrete relative paths, workflow selection rules, script entrypoint, and ARS alias mapping. Minor risk from the large vendored suite requiring disciplined progressive loading. |
| Resource integration | 4 | 10.0 | 4.0 | Required references, scripts, ARS router, manifest, license, workflows, agents, commands, and shared schemas are present. |
| Overall architecture | 12 | 9.0 | 10.8 | ARS is isolated as a subskill; parent skill remains domain-specific and lean. |
| Tested performance | 23 | 8.3 | 19.1 | Dry-run validation across bibliometric review, exposure-health systematic review, remote-sensing radar, and ARS pipeline prompts. Independent judge agents were not used in this run. |
| Counterexamples and blacklist | 6 | 9.0 | 5.4 | Parent skill has `Must Not Do`, security boundaries, and corpus/radar handoff rules. |

## Project Value

For the urban exposure, sports geography, and bibliometric-review project, this packaging adds four practical capabilities:

1. Research-to-paper continuity: the parent skill still handles exposure/accessibility/radar decisions, while ARS adds topic narrowing, literature review, outline, drafting, revision, and finalization workflows.
2. Stronger integrity gates: ARS brings citation checks, claim-evidence alignment, Material Passport style provenance, reviewer simulation, and staged audit logic.
3. Better manuscript iteration: reviewer-response roadmaps, re-review, abstract-only, revision-coach, and format-convert modes support journal submission workflows.
4. Cleaner specialization boundary: urban-exposure rules remain authoritative for causality, corpus inclusion, spatial exposure validity, and journal evidence standards; ARS is called only when a broader academic pipeline is needed.

## Dry-Run Test Summary

| Prompt group | Expected behavior | Result |
|---|---|---|
| Bibliometric + critical review for SCS/Cities | Use parent route table, WoS/Scopus protocol, manual coding, policy agenda, and journal gate. | Pass |
| Exposure-health systematic review | Use PEO/PICOS, screening, extraction, risk/bias checks, and causal-language boundary. | Pass |
| Remote-sensing and Geospatial AI radar | Keep frontier radar separate from formal corpus and use dated source scanning. | Pass |
| ARS full paper pipeline | Apply parent research positioning first, then route to `subskills/academic-research-suite/SKILL.md` and one relevant `WORKFLOW.md`. | Pass |

## Verification

- `test-prompts.json`: JSON parse passed.
- Scaffold script: created 16 temporary project artifacts and cleaned the temporary directory.
- Required paths: parent references, scaffold script, ARS router, manifest, license, five ARS workflows, key agents, commands, shared schemas, and Codex runtime manifest exist.
- Vendored package completeness: upstream skill directory relative paths match the copied subskill directory; no `.git` directory is present.
- Secret scan: no common API token pattern matched.
- Runtime scan: parent and subskill router are clean. `README.upstream.md` contains Claude Code comparison text as preserved upstream documentation, not active runtime instruction.

## Risks And Controls

| Risk | Control |
|---|---|
| Vendored ARS is large and can overload context if loaded wholesale. | Parent skill instructs to read only the ARS router first, then one `WORKFLOW.md`. |
| Upstream package may become stale. | Track v0.1.12 and upstream commit in manifest; refresh deliberately rather than silently. |
| CC BY-NC 4.0 restricts commercial reuse. | Keep license and attribution with the subskill; avoid sharing without license notice. |
| Historical ARS design docs contain TODO or placeholder text. | Treat `ars/docs/design/` as traceability material, not active runtime instruction. |
| Dry-run scoring is weaker than blind independent judge evaluation. | Mark dimension 8 as `dry_run`; use multi-agent judges only when explicitly requested. |

## Recommendation

Keep this packaging. It meaningfully improves the project when the task moves from domain review planning into manuscript production, peer review simulation, citation integrity, or full research-to-paper workflow. It should not replace the parent domain skill; it should remain a routed subskill.
