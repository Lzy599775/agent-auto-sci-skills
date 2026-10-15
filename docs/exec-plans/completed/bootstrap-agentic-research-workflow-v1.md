# Bootstrap Agentic Research Workflow V1

## Objective

Extend `Lzy599775/agent-auto-sci-skills` with a persistent, auditable, evidence-first research workflow architecture and deliver it through a Draft PR.

## Inputs

- Existing repository structure and scientific skills.
- Current OpenAI Codex documentation on `AGENTS.md`, skills, and long-running work.
- GitHub flow guidance.
- Installed Zotero skill behavior and official Zotero API guidance.

## Constraints

- Keep root `AGENTS.md` concise.
- Do not modify research repositories or research data.
- Do not duplicate Zotero-managed PDFs.
- Build Literature Skill V0 as a specification, not a large automation system.
- Work only on `feature/agentic-research-workflow-v1`.
- No force push, automatic merge, or direct default-branch write.

## Steps and gates

1. Research authoritative sources. **Complete**
2. Audit and select repository. **Complete**
3. Add architecture and persistent instruction map. **Complete**
4. Add Research Vault, templates, workflows, and standards. **Complete**
5. Add Literature Skill V0 and eval scaffold. **Complete**
6. Add and run lightweight validation. **Complete**
7. Review diff, commit, push, and open Draft PR. **Complete**

## Expected outputs

- Root instructions and architecture.
- Routed research workflows and standards.
- Derived-knowledge vault and reusable schemas.
- Literature Skill V0 with Zotero integration map.
- Golden-set evaluation scaffold.
- Validation script and passing QA report.
- Draft PR for review.

## Current blockers

None.

## Decisions

- Extend the existing `agent-auto-sci-skills` repository rather than create a competing source of truth.
- Keep Zotero as bibliographic/PDF source of truth and the Research Vault as derived knowledge only.

## Completion record

- Branch: `feature/agentic-research-workflow-v1`
- Implementation commits:
  - `fa885dc` `docs: establish research workflow architecture`
  - `d5a6ca9` `docs: add research workflows and evidence standards`
  - `96eafa5` `feat: scaffold literature workflow skill`
  - `afa4fc3` `test: add research workflow validation`
- Draft PR: https://github.com/Lzy599775/agent-auto-sci-skills/pull/2
- Repository validator: PASS (38 required files, 68 Markdown files, 146 root `AGENTS.md` lines)
- Literature Skill validation: PASS
- Python compilation: PASS
- Public-safety scan: PASS
- Branch diff whitespace check: PASS
- Research repositories modified: NO
- Research data modified: NO
- Default branch directly modified: NO
