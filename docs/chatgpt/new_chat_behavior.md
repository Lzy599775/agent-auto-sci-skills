# New-Chat Behavior

## Codex fresh task in this repository

Codex should discover `AGENTS.md`, route through `docs/workflows/index.md`, and load only the relevant workflow and standards. The user should state the research goal, not repeat the framework prompt.

## ChatGPT new chat inside the configured Project

A new chat created inside the same ChatGPT Project should inherit that Project's instructions, approved files/sources, and Project memory/context where available. It should recognize a substantive research task, retrieve current workflow context from GitHub when needed, route automatically, and report the ref/version used.

Project persistence is bounded to that Project. Do not claim that a chat started from ChatGPT Home or another Project inherits these instructions.

## Ordinary ChatGPT new chat outside the Project

Project instructions cannot be assumed. Reusable behavior requires the installed Agentic Research Workflow plugin or Research Orchestrator Skill on that surface. If it is not installed, the cross-surface ordinary-chat test is `NOT_TESTABLE_ON_CURRENT_SURFACE` rather than a synthetic pass.

## Workspace Agent role

`WORKSPACE_AGENT_ROLE = OPTIONAL`.

Workspace Agents can add value for eligible workspaces with highly repeatable, published, structured jobs and governed shared connections. Availability depends on workspace plan and administrative controls and is not required for this architecture. Open-ended scientific reasoning, exploratory research, and repository implementation remain normal ChatGPT/Codex interactions by default.

## One-time setup boundary

1. Add the copy-ready block from [project_instructions.md](project_instructions.md) to the intended ChatGPT Project and connect/approve the GitHub repository source.
2. Install the validated Agentic Research Workflow plugin when ordinary chats outside that Project also need automatic routing.

Start a new chat after either setup change before testing.
