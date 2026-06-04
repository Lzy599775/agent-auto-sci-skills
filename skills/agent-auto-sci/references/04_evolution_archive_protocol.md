# Evolution Archive Protocol

Use this file whenever any `agent-auto-sci*` or sport-geography skill is updated.

## 1. Files

Main data:

`<project-root>/agent_auto_sci/evolution_archive/evolution_data.json`

Generated HTML:

`<project-root>/agent_auto_sci/evolution_archive/agent-auto-sci-evolution.html`

Generator:

`<project-root>/agent_auto_sci/evolution_archive/update_evolution_html.py`

Project log:

`<project-root>/agent_auto_sci/00_AGENT_AUTO_SCI_总览与变更记录.md`

## 2. Update Rule

After any meaningful change, update:

1. skill files;
2. `evolution_data.json`;
3. generated HTML;
4. project log markdown.

Then validate:

```powershell
$env:PYTHONUTF8='1'
python '<codex-skills-dir>\.system\skill-creator\scripts\quick_validate.py' '<codex-skills-dir>\agent-auto-sci'
python '<project-root>\\agent_auto_sci\evolution_archive\update_evolution_html.py'
```

## 3. What Counts as a Meaningful Change

- New skill or subskill.
- New reference file.
- Changed workflow or quality gate.
- New external repository learned and adapted.
- New project route.
- New script or template.
- Major validation result.

Minor spelling fixes do not need a new timeline event, but still may update the modified date.

## 4. HTML Content Rules

Include:

- skill names, roles, usage routes;
- evolution timeline;
- source repositories learned;
- current research routes;
- future directions;
- validation status.

Do not include:

- real API keys;
- full copyrighted article text;
- private reviewer comments unless summarized;
- unpublished sensitive data;
- personal identifiers beyond what the user explicitly wants.


