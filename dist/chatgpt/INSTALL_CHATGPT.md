# ChatGPT Handoff

This package provides two distinct routes. The GitHub repository remains the versioned workflow source of truth. The connected GitHub app retrieves repository content on demand; it is not treated as a permanently mounted ChatGPT Project source.

## Capability distinctions

- **Research Orchestrator Skill:** portable workflow instructions that recognize and route substantive research tasks.
- **Plugin:** an optional container that can package Skills and Apps for supported distribution channels.
- **GitHub App:** the external connector used to retrieve authorized repository content or perform separately approved actions.

The plugin marketplace metadata in this repository is local to Codex. `LOCAL_PLUGIN_STATUS = LOCAL_CODEX_ONLY`. A `codex://` link does not establish ChatGPT installation or directory availability.

## Route A — same ChatGPT Project

1. Open the target ChatGPT Project.
2. Open **Project menu → Project settings**.
3. Paste the complete contents of `project_instructions.txt` into **Project instructions**.
4. Confirm the GitHub app is connected to ChatGPT and is available in Project chats.
5. Do not add or describe the GitHub repository as a persistent Project source unless the current ChatGPT UI explicitly supports it.
6. Create a new chat inside the same Project.
7. Test with: `帮我评估一个新的绿地暴露研究选题。`

Expected: ChatGPT applies the Project instructions, recognizes a research task, retrieves `Lzy599775/agent-auto-sci-skills` through the GitHub app when needed, selects research idea evaluation, and reports the workflow ref/version used.

## Route B — ordinary ChatGPT chat

`CURRENT_CHATGPT_SKILL_INSTALL_SUPPORT = UNKNOWN` because this repository cannot observe the user's ChatGPT plan, role, workspace policy, region, or current Skills UI.

Only if the account exposes personal Skill creation/upload:

1. Open **Sidebar → Plugins → Skills → Create → Upload from your computer** (labels may vary as the UI evolves).
2. Upload the `research-orchestrator-skill` directory from this package.
3. Install or enable the Skill as prompted.
4. Confirm the GitHub app is connected.
5. Start a completely ordinary new chat outside the Project.
6. Test with: `帮我检查一篇论文的方法是否足以支持其因果结论。`

Expected: Research Orchestrator is applicable, routes to method/evidence and citation-claim review, and retrieves the GitHub workflow backend when needed.

If the personal Skills controls are absent, record:

`ORDINARY_CHAT_PERSISTENCE_NOT_CURRENTLY_AVAILABLE_VIA_PERSONAL_SKILL`

Do not invent a workaround or infer ChatGPT support from the local Codex plugin.

## Negative control

In an ordinary chat with no Project instructions and no installed Skill/plugin, the repository workflow is not guaranteed to persist. Record `EXPECTED_NOT_PERSISTENT`; a connected GitHub app alone does not automatically apply `AGENTS.md`.
