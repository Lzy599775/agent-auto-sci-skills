# Upstream Update Check, 2026-06-23

This pass checked the locally packaged skills and their upstream sources for `Lzy599775/agent-auto-sci-skills`.

## Packaged Upstream Sources

| Upstream | Previous local snapshot | Latest checked snapshot | Status | Local action |
|---|---:|---:|---|---|
| `K-Dense-AI/scientific-agent-skills` | `2093901` (`v2.52.0-3-g2093901`) | `ddd2f7f` (`v2.52.0-4-gddd2f7f`) | Upstream changed | Updated wrapper NOTICE files. Diff only touched upstream root `SECURITY.md`; selected packaged subskill files were unchanged. |
| `Haojae/scipilot-figure-skill` | `43098dd` (`v2.1.0-1-g43098dd`) | `43098dd` (`v2.1.0-1-g43098dd`) | No upstream change | No package change. |
| `Imbad0202/academic-research-skills-codex` | `763bccd` (`v0.1.11-5-g763bccd`) / adapter `0.1.12` | `36cc610` (`v0.1.14`) / adapter `0.1.14` | Upstream changed | Re-synced `urban-exposure-review-radar-workflow/subskills/academic-research-suite` from the upstream Codex package and refreshed attribution/version docs. |
| `skyllwt/AutoSci` | `71469e8` (`v1.0.0-26-g71469e8`) | `5568c25` (`v1.0.0-28-g5568c25`) | Upstream changed | Updated ignored local mirror under `external_repos/latest`. No wholesale re-wrap because the public `auto-sci-research` package is a domain-adapted skill rather than a direct AutoSci vendoring. |

## Optional Reference Sources

| Upstream | Latest checked snapshot | Local action |
|---|---:|---|
| `assafelovic/gpt-researcher` | `b364917` | No packaged wrapper change. |
| `hwang847/codex-paper-reader` | `59bad33` | No packaged wrapper change. |
| `Leey21/awesome-ai-research-writing` | `c07628b` | Reference only; no packaged wrapper change. |
| `STRYXTN/awesome-ai-research-writing` | `16bb967` | Reference only; no packaged wrapper change. |
| `alchaincyf/nuwa-skill` | `f4c9bc3` | Reference only; no packaged wrapper change. |
| `leo-lilinxiao/codex-autoresearch` | `e294349` | Reference only; no packaged wrapper change. |
| `bionoob7/nlr-workflow` | `7399d5d` | Reference only; no packaged wrapper change. |
| `limi124/remote-sensing-research-radar` | `3614505` | Reference only; no packaged wrapper change. |

## Packaging Notes

- Third-party repositories remain ignored under `external_repos/`.
- Public changes are limited to packaged skill content, attribution files, and documentation.
- `academic-research-suite` remains isolated under the urban exposure workflow; the parent skill keeps domain authority for exposure validity, accessibility/use separation, causal language, formal corpus rules, and frontier-radar handoff.
- Cross-model/API behavior in ARS remains disabled by default and requires explicit user consent and provider configuration.
