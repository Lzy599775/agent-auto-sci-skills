# Cross-Surface Gap Analysis

## Classification

| Category | Current mechanism | Persistence boundary |
|---|---|---|
| Codex-native | Root/nested `AGENTS.md`, checked-out repository files, local skills, validation scripts | Future Codex tasks that open the repository and discover its instruction tree |
| Cross-product | Open Agent Skills format and installable Plugins | Supported ChatGPT and Codex surfaces after the Skill/Plugin is available to that account or environment |
| ChatGPT-native | Project instructions, Project files/sources, Project chats, and Project memory/context where available | New chats created inside the same ChatGPT Project |
| Data access | Connected GitHub app or repository source | Authorized repository content only; no automatic instruction semantics |
| Repository-only today | Detailed workflows, standards, Research Vault rules, ADRs, and current version state | Available only when the repository is explicitly opened or retrieved |

## What did not survive a new ordinary ChatGPT chat

Before M10, an ordinary ChatGPT chat outside a configured Project had no guaranteed access to this repository, no durable instruction to retrieve it, and no installed high-level Skill that routed broad research requests. GitHub connection alone did not close that gap.

## M10 closure

- ChatGPT Project instructions provide a concise, persistent map for chats inside one Project.
- Research Orchestrator provides the reusable route for supported Skill/Plugin surfaces.
- GitHub remains the live workflow backend and version record.
- A minimal fallback is explicit and self-identifying rather than silently stale.

## Plugin feasibility

`CROSS_SURFACE_PLUGIN_FEASIBILITY`

- Plugin creation supported: `YES`.
- Custom/local plugin packaging supported: `YES`.
- Custom/local installation supported: `YES`, subject to user/workspace installation controls.
- ChatGPT surface supported: `YES` for supported Chat and Work plugin surfaces after installation.
- Codex surface supported: `YES` in the ChatGPT desktop app and Codex CLI; not in the IDE extension.
- Can include Skill: `YES`.
- Can use existing GitHub app: `INDIRECT`; the Skill can call an available authorized GitHub app/connector, but this package does not invent or bundle an undocumented dependency identifier.

This repository contains a minimal skills-only plugin package and repo-local marketplace metadata. Account/workspace installation remains a one-time user action.

## Remaining user-owned boundary

The repository cannot choose the user's ChatGPT Project or install a local/plugin marketplace into the user's ChatGPT account by itself. Project configuration and account installation must be completed once in the relevant UI, then verified with the manual tests in `evals/cross-surface/README.md`.
