# Darwin Quality Gate

Use this checklist before merging this skill into Auto-sci-research or publishing it.

## Required Score Target

Target: 95 / 100.

Minimum acceptable before merge: 90 / 100 if and only if the remaining gaps require real user data or database exports.

## 9-Dimension Self-Check

| Dimension | Pass requirement |
|---|---|
| Frontmatter | Name and description clearly identify when to use the skill |
| Workflow clarity | Steps have ordered inputs, outputs, and decisions |
| Failure modes | Common failures have explicit fallback actions |
| Checkpoints | Ambiguous review type, journal route, data sufficiency, and causality trigger STOP |
| Actionability | The skill can produce tables, protocols, scaffolds, audits, and next actions |
| Resources | References and scripts are linked with correct relative paths |
| Structure | The skill is concise at entry point and detailed in references |
| Test performance | At least four representative prompts produce route-specific outputs |
| Blacklist | Must-not-do rules prevent overclaiming, genre confusion, and privacy leaks |

## Test Prompt Set

Use the repository-level file:

`agent_auto_sci/nlr_remote_sensing_distillation/test_prompts_综述与遥感雷达.json`

Expected coverage:

1. bibliometric + critical review for SCS/Cities;
2. systematic review for exposure-health evidence;
3. remote-sensing / geospatial AI frontier radar;
4. medical database linkage with urban exposure.

## Merge Blockers

- Hardcoded private local path.
- API key, token, or example secret.
- Unattributed copied external text.
- Systematic-review claims without reproducible screening records.
- Health causality claims without design support.
- Missing failure-mode fallback.

