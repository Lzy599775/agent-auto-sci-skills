# External Design Sources

Access date for all sources below: **2026-08-23**.

| Title | Organization | URL | Architectural decision supported |
|---|---|---|---|
| Custom instructions with AGENTS.md | OpenAI | https://learn.chatgpt.com/docs/agent-configuration/agents-md | Keep root instructions concise, repository-scoped, and overridable by nearer project instructions. |
| Build skills | OpenAI | https://learn.chatgpt.com/docs/build-skills | Use focused skills with concise triggering metadata and progressive disclosure through references/scripts. |
| Long-running work | OpenAI | https://learn.chatgpt.com/docs/long-running-work | Store outcome, constraints, verification, decisions, and status for multi-step work. |
| Projects and chats | OpenAI | https://learn.chatgpt.com/docs/projects | Use Project instructions, files, and connected sources as shared context for new chats created inside the same ChatGPT Project; do not extend that guarantee to ordinary chats outside the Project. |
| Skills & Plugins | OpenAI | https://learn.chatgpt.com/docs/skills-and-plugins | Use Skills for reusable workflows and Plugins as installable bundles shared across supported ChatGPT and Codex surfaces. |
| Build plugins | OpenAI | https://developers.openai.com/plugins/build/plugins | Package the thin Research Orchestrator as a self-contained skills-only plugin and validate it before installation or sharing. |
| Plugins | OpenAI | https://learn.chatgpt.com/docs/plugins | Treat plugin installation as a supported cross-surface distribution mechanism that becomes available to new chats after installation. |
| GitHub flow | GitHub | https://docs.github.com/en/get-started/using-github/github-flow | Develop on isolated branches and use pull requests as the review boundary. |
| Git status documentation | Git project | https://git-scm.com/docs/git-status | Inspect working-tree and staging state before commits. |
| Git diff documentation | Git project | https://git-scm.com/docs/git-diff | Review unstaged and staged changes as explicit quality gates. |
| Zotero Web API v3 | Zotero | https://www.zotero.org/support/dev/web_api/v3/start | Treat Zotero as a structured bibliographic source and respect authenticated write boundaries. |

## Installed guidance inspected

- OpenAI bundled `openai-docs` skill and current Codex manual.
- OpenAI bundled `skill-creator` guidance and validator.
- OpenAI bundled `plugin-creator` guidance, scaffold, marketplace contract, and validator.
- OpenAI-curated `plugin-management` guidance.
- OpenAI-curated Zotero skill version `0.1.2`; its helper exposes status, inventory, search, collections, tags, BibTeX, citations, children, full text, file URLs, and explicitly gated imports.

Only decision-relevant evidence is recorded here; source pages are not copied into the repository.
