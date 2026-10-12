# PR #6 Final Diff Scope Audit

- Audited head: `fa7654a7f6bd71707f5c7d4538898c727ed0fddb` (before current-main conflict-resolution merge).
- Comparison basis: public `main` at `9fedd5ff98fd6d34489a46cf591ae3adecade609` and integration head; 140 changed paths, 5,761 additions, 29 deletions before adding this audit record.
- Classification means the path is within the controlled Research OS/writing release scope; the audit record itself is excluded from the 140-path input set.
- `PR6_INCLUDES_REQUIRED_PR2_FOUNDATION = YES`: the branch contains the general workflow/Research OS bootstrap (router, workflow docs, evidence standards, installer-facing skill metadata and research-vault scaffolding). It is needed because the original integration base did not contain that foundation. **Recommendation: SUPERSEDE PR #2** after PR #6 is pushed, conflict-free, CI-green, and author-approved; do not rebase PR #6 onto PR #2 because that would preserve duplicate stacked history.
- Scope review found no manuscript corpus, named private exemplar set, project state, classifier, monitor runtime, scheduler, Zotero, or Obsidian edits.

| Classification | Count |
|---|---:|
| EXPECTED_ROUTING | 25 |
| EXPECTED_BOOTSTRAP | 80 |
| EXPECTED_WRITING | 26 |
| EXPECTED_TEST | 9 |
| UNRELATED | 0 |
| **Total audited paths** | **140** |

## Per-file classification

### EXPECTED_ROUTING

- `.agents/plugins/marketplace.json`
- `.agents/plugins/plugins/agentic-research-workflow/.codex-plugin/plugin.json`
- `.agents/plugins/plugins/agentic-research-workflow/skills/research-orchestrator/SKILL.md`
- `.agents/plugins/plugins/agentic-research-workflow/skills/research-orchestrator/agents/openai.yaml`
- `.agents/plugins/plugins/agentic-research-workflow/skills/research-orchestrator/references/routing-and-qc.md`
- `.agents/plugins/plugins/agentic-research-workflow/skills/research-orchestrator/references/source-retrieval.md`
- `.agents/plugins/plugins/agentic-research-workflow/skills/research-orchestrator/tests/activation_cases.md`
- `dist/chatgpt/INSTALL_CHATGPT.md`
- `dist/chatgpt/project_instructions.txt`
- `dist/chatgpt/research-orchestrator-skill/SKILL.md`
- `dist/chatgpt/research-orchestrator-skill/agents/openai.yaml`
- `dist/chatgpt/research-orchestrator-skill/references/routing-and-qc.md`
- `dist/chatgpt/research-orchestrator-skill/references/source-retrieval.md`
- `dist/chatgpt/research-orchestrator-skill/tests/activation_cases.md`
- `docs/CROSS_CLIENT_WRITING_ROUTING_MATRIX_V1.md`
- `docs/chatgpt/CHATGPT_GLOBAL_RESEARCH_OS_ROUTER_V1.txt`
- `docs/chatgpt/CHATGPT_PROJECT_RESEARCH_OS_ROUTER_V1.md`
- `docs/chatgpt/CHATGPT_WEB_PER_MANUSCRIPT_EXEMPLAR_ROUTER_V1.md`
- `docs/chatgpt/cross_surface_contract.md`
- `docs/chatgpt/cross_surface_gap_analysis.md`
- `docs/chatgpt/index.md`
- `docs/chatgpt/new_chat_behavior.md`
- `docs/chatgpt/project_instructions.md`
- `docs/skill-map.md`
- `docs/version.md`

### EXPECTED_BOOTSTRAP

- `.github/workflows/validate.yml`
- `AGENTS.md`
- `ARCHITECTURE.md`
- `CHANGELOG.md`
- `README.md`
- `README_EN.md`
- `agent_auto_sci/00_AGENT_AUTO_SCI_\346\200\273\350\247\210\344\270\216\345\217\230\346\233\264\350\256\260\345\275\225.md`
- `agent_auto_sci/evolution_archive/agent-auto-sci-evolution.html`
- `agent_auto_sci/evolution_archive/evolution_data.json`
- `agent_auto_sci/evolution_archive/update_evolution_html.py`
- `docs/decisions/ADR-0001-research-architecture.md`
- `docs/decisions/ADR-0002-zotero-source-of-truth.md`
- `docs/decisions/ADR-0003-research-vault-derived-knowledge.md`
- `docs/decisions/ADR-0004-literature-golden-set-first.md`
- `docs/decisions/ADR-0005-per-manuscript-writing-exemplar-state.md`
- `docs/decisions/index.md`
- `docs/exec-plans/README.md`
- `docs/exec-plans/active/README.md`
- `docs/exec-plans/completed/README.md`
- `docs/exec-plans/completed/bootstrap-agentic-research-workflow-v1.md`
- `docs/exec-plans/completed/m10-cross-surface-chatgpt-research-workflow.md`
- `docs/exec-plans/completed/m11-cross-surface-correction-and-chatgpt-handoff.md`
- `docs/index.md`
- `docs/research/external_sources.md`
- `docs/research/research_principles.md`
- `docs/research/source_hierarchy.md`
- `docs/research/uncertainty_policy.md`
- `docs/standards/academic_claims.md`
- `docs/standards/academic_prose_logic.md`
- `docs/standards/data_provenance.md`
- `docs/standards/evidence_trace.md`
- `docs/standards/file_integrity.md`
- `docs/standards/git_policy.md`
- `docs/standards/reproducibility.md`
- `docs/workflows/citation_claim_audit.md`
- `docs/workflows/data_analysis.md`
- `docs/workflows/figure_workflow.md`
- `docs/workflows/index.md`
- `docs/workflows/literature_review.md`
- `docs/workflows/manuscript_writing.md`
- `docs/workflows/paper_reproduction.md`
- `docs/workflows/research_idea_evaluation.md`
- `research-vault/README.md`
- `research-vault/concepts/README.md`
- `research-vault/datasets/README.md`
- `research-vault/evidence/README.md`
- `research-vault/literature/README.md`
- `research-vault/methods/README.md`
- `research-vault/projects/README.md`
- `research-vault/synthesis/README.md`
- `scripts/validation/validate_research_workflow.py`
- `site/agent-auto-sci-evolution.html`
- `skills/auto-sci-research/SKILL.md`
- `skills/auto-sci-research/references/02_subskill_registry.md`
- `skills/auto-sci-research/references/08_full_research_to_manuscript_pipeline.md`
- `skills/literature/SKILL.md`
- `skills/literature/agents/openai.yaml`
- `skills/literature/references/contracts.md`
- `skills/literature/references/failure-and-qc.md`
- `skills/literature/references/zotero-integration.md`
- `skills/literature/tests/activation_cases.md`
- `skills/research-orchestrator/SKILL.md`
- `skills/research-orchestrator/agents/openai.yaml`
- `skills/research-orchestrator/references/routing-and-qc.md`
- `skills/research-orchestrator/references/source-retrieval.md`
- `skills/research-orchestrator/tests/activation_cases.md`
- `templates/dataset_record.md`
- `templates/decision_record.md`
- `templates/evidence_record.md`
- `templates/method_record.md`
- `templates/paper_note.md`
- `templates/project_bootstrap/AGENTS.md`
- `templates/project_bootstrap/README.md`
- `templates/project_bootstrap/docs/data_inventory.md`
- `templates/project_bootstrap/docs/decision_log.md`
- `templates/project_bootstrap/docs/methods.md`
- `templates/project_bootstrap/docs/project_context.md`
- `templates/project_bootstrap/docs/research_questions.md`
- `templates/reproduction_plan.md`
- `templates/research_question.md`

### EXPECTED_WRITING

- `CHATGPT_GLOBAL_ACADEMIC_WRITING_INSTRUCTIONS_V2.txt`
- `USER_POLISHING_PROMPT_RULE_MAPPING_V1.md`
- `docs/exec-plans/active/academic-writing-exemplar-cross-client-routing-v1.md`
- `docs/exec-plans/active/academic-writing-exemplar-global-contract-v2.md`
- `docs/exec-plans/active/per_manuscript_exemplar_workflow_v1.md`
- `docs/workflows/PER_MANUSCRIPT_EXEMPLAR_STATE_MACHINE_V1.md`
- `docs/workflows/PER_MANUSCRIPT_WRITING_EXEMPLAR_WORKFLOW_V1.md`
- `scripts/validation/validate_academic_writing_v2.py`
- `scripts/validation/validate_writing_exemplar_routing.py`
- `scripts/validation/writing_redundancy_golden_set_v2.json`
- `skills/agent-auto-sci-scicomm/SKILL.md`
- `skills/agent-auto-sci-scicomm/references/academic_prose_style_guard.md`
- `skills/agent-auto-sci-scicomm/references/academic_writing_exemplar_protocol.md`
- `skills/agent-auto-sci-scicomm/tests/writing_exemplar_golden_set.json`
- `skills/agent-auto-sci-scicomm/tests/writing_exemplar_golden_set_v2.json`
- `skills/project-specific-writing-exemplar-workflow/SKILL.md`
- `skills/project-specific-writing-exemplar-workflow/agents/openai.yaml`
- `skills/project-specific-writing-exemplar-workflow/references/routing.md`
- `skills/project-specific-writing-exemplar-workflow/references/schema.md`
- `skills/scipilot-writing-skill/SKILL.md`
- `skills/scipilot-writing-skill/scripts/writing_lint.py`
- `templates/CORE3_APPROVAL_TEMPLATE_V1.yaml`
- `templates/MANUSCRIPT_WRITING_PROFILE_TEMPLATE_V1.yaml`
- `templates/MASTER_EXEMPLAR_CORPUS_TEMPLATE_V1.yaml`
- `templates/PROJECT_EXEMPLAR_SKILL_TEMPLATE_V1.md`
- `templates/SECTION_EXEMPLAR_SELECTION_TEMPLATE_V1.yaml`

### EXPECTED_TEST

- `evals/academic-writing-exemplar/CROSS_CLIENT_ROUTING_GOLDEN_SET_V1.json`
- `evals/academic-writing-exemplar/PER_MANUSCRIPT_EXEMPLAR_ROUTING_GOLDEN_SET_V1.json`
- `evals/academic-writing-exemplar/README.md`
- `evals/cross-surface/README.md`
- `evals/literature/README.md`
- `scripts/validation/test_academic_writing_v2.py`
- `scripts/validation/test_cross_client_routing_parity.py`
- `scripts/validation/test_per_manuscript_exemplar_workflow.py`
- `scripts/validation/test_writing_exemplar_routing.py`

