# New-Chat Behavior

## Codex fresh task in this repository

Codex should discover `AGENTS.md`, route through `docs/workflows/index.md`, and load only the relevant workflow and standards. The user should state the research goal, not repeat the framework prompt.

## ChatGPT new chat inside the configured Project

A new chat created inside the same ChatGPT Project should inherit that Project's instructions, project files/sources, and Project memory/context where available. In that chat, the connected GitHub app can retrieve current workflow context on demand; GitHub is not treated as a permanently mounted Project source. The chat should recognize a substantive research task, route automatically, and report the ref/version used.

Project persistence is bounded to that Project. Do not claim that a chat started from ChatGPT Home or another Project inherits these instructions.

## Ordinary ChatGPT new chat outside the Project

Project instructions cannot be assumed. Reusable behavior requires an installed Research Orchestrator Skill or plugin on that surface. Whether personal Skill upload/install is available depends on the ChatGPT plan, workspace controls, role, and surface; this repository cannot infer the user's entitlement. If it is unavailable or unverified, record `ORDINARY_CHAT_PERSISTENCE_NOT_CURRENTLY_AVAILABLE_VIA_PERSONAL_SKILL` rather than a synthetic pass.

## Workspace Agent role

`WORKSPACE_AGENT_ROLE = OPTIONAL`.

Workspace Agents can add value for eligible workspaces with highly repeatable, published, structured jobs and governed shared connections. Availability depends on workspace plan and administrative controls and is not required for this architecture. Open-ended scientific reasoning, exploratory research, and repository implementation remain normal ChatGPT/Codex interactions by default.

## One-time setup boundary

1. Add the copy-ready block from [project_instructions.md](project_instructions.md) to the intended ChatGPT Project.
2. Confirm the GitHub app is connected and usable in Project chats; retrieve the repository on demand when workflow context is required.
3. Install the validated Research Orchestrator Skill or Agentic Research Workflow plugin only if the current ChatGPT surface/account supports it and ordinary chats outside that Project also need automatic routing.

Start a new chat after either setup change before testing.
