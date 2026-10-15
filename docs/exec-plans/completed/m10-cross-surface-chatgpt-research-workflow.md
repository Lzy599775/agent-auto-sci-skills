# M10 Cross-Surface ChatGPT Research Workflow

## Objective

Extend the existing agentic research workflow so Codex, ChatGPT Projects, and installed Skill/Plugin surfaces can retrieve and apply one versioned GitHub source of truth without repeated long prompts.

## Inputs

- Existing framework on `feature/agentic-research-workflow-v1`.
- Draft PR #2.
- Current official OpenAI documentation for Projects, `AGENTS.md`, Skills, Plugins, apps, and workspace controls.
- Installed Skill Creator and Plugin Creator tooling.

## Constraints

- Continue on the same feature branch and Draft PR.
- Do not merge, amend, force push, or modify `main` directly.
- Keep GitHub as the canonical workflow backend.
- Keep ChatGPT Project instructions and the orchestrator concise.
- Do not duplicate detailed research policies into ChatGPT or a Skill.
- Do not touch research repositories, Zotero content, research data, private files, or credentials.

## Steps and gates

1. Re-audit current official OpenAI guidance. **Complete**
2. Document cross-surface gaps and source-of-truth contract. **Complete**
3. Add ChatGPT Project instructions and new-chat behavior. **Complete**
4. Create and validate Research Orchestrator Skill. **Complete**
5. Audit and, if supported, package the Skill as a minimal plugin. **Complete**
6. Add version-drift protection and cross-surface eval definitions. **Complete**
7. Run repository, skill, plugin, link, public-safety, and Git QA. **Complete**
8. Commit logically, push the same branch, and verify Draft PR #2. **Complete**

## Expected outputs

- Focused `docs/chatgpt/` entrypoint documents.
- Thin Research Orchestrator Skill.
- Minimal validated plugin package when supported.
- Cross-surface evaluation protocol.
- Version record and validation coverage.
- Updated Draft PR #2.

## Current blockers

- ChatGPT Project selection and UI installation are user-owned one-time setup actions; repository implementation can continue without them.

## Decisions

- Treat the top-level `skills/research-orchestrator/` as the authoring source.
- If a plugin is built, keep its bundled copy byte-identical and enforce that invariant in validation.
- Treat Workspace Agents as optional and plan/workspace-dependent, not the default research discussion surface.

## Completion record

- Branch: `feature/agentic-research-workflow-v1`
- Implementation commits:
  - `dbdd6c2` `feat: add cross-surface research workflow entrypoints`
  - `189af75` `test: validate cross-surface workflow packaging`
- Existing Draft PR: https://github.com/Lzy599775/agent-auto-sci-skills/pull/2
- GitHub connector retrieval of candidate branch core files: PASS
- Repository validator: PASS (52 required files, 84 Markdown files, 147 root `AGENTS.md` lines)
- Literature Skill validation: PASS
- Research Orchestrator Skill validation: PASS
- Plugin validation: PASS
- Python compilation: PASS
- Public-safety scan: PASS
- Git whitespace checks: PASS
- Codex fresh-task product test: MANUAL_TEST_REQUIRED
- ChatGPT Project new-chat test: MANUAL_TEST_REQUIRED
- Ordinary ChatGPT new-chat Skill test: NOT_TESTABLE_ON_CURRENT_SURFACE until installation
- Research repositories modified: NO
- Research data modified: NO
- Default branch directly modified: NO
