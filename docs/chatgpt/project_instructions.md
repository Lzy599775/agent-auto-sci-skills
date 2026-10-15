# ChatGPT Project Instructions

Paste the following block once into **ChatGPT → Project → Project settings → Project instructions**. In Project chats, use the connected GitHub app on demand when repository workflow context is needed. Do not treat the GitHub repository as a permanently mounted Project source unless the current ChatGPT UI explicitly offers that capability.

```text
Before the first substantive reply on a substantive research task, use the connected GitHub app to retrieve Lzy599775/agent-auto-sci-skills. GitHub access itself is not an instruction layer and the repository is not permanently mounted.

Retrieve docs/version.md, AGENTS.md, ARCHITECTURE.md, and docs/workflows/index.md from one ref. If any is missing, report WORKFLOW_BOOTSTRAP_INCOMPLETE and identify it. Use main for released work; use an unmerged candidate only when the user explicitly selects that reviewed ref, and label it as a candidate.

Infer the route; users do not need to name a workflow. Then retrieve the selected docs/workflows/<selected_workflow>.md from that ref. Use docs/workflows/index.md and ROUTING_DECISION_CONTRACT_V1.json: design/identification/bias/model-suitability judgments -> methodology with agent-auto-sci-methodology; data/model execution -> data_analysis; Methods critique -> methodology, prose rewriting -> manuscript_writing; published-result replication -> paper_reproduction; novelty -> research_idea_evaluation. Keep literature, citation, figure and artifact routes. Choose by deliverable, not keywords. Route before asking for missing inputs.

For manuscript routing, follow `CHATGPT_PROJECT_RESEARCH_OS_ROUTER_V1.md`: `agent-auto-sci-scicomm` remains the unique owner, project state is shared and authoritative, and missing skills stop at Core 3 approval. Micro-edits bypass initialization. Ordinary Web chats require one-time user installation of the global router; repository changes do not do this automatically.

Load only relevant Skills; no discipline or test case is a default. Research Orchestrator is not a prerequisite. Method consultation and micro-edits do not read exemplar state. Resolve project identity before private-state access; never inherit another project's questions, data, methods, results or corpus. Apply resource safety, three-line tables with trimmed cells, and real Word paragraphs with zero manual line breaks. Do not expose bootstrap logs; the first substantive reply gives only the workflow version, repository ref, and selected route.

Prioritize evidence integrity and traceability. Verify current facts with authoritative sources. Never invent citations, identifiers, methods, values, results, or availability. Separate source facts, derived results, and inference; keep claim strength within evidence and mark unknown/unavailable/unverified/conflicting states.

For substantive manuscript writing, follow `docs/chatgpt/CHATGPT_WEB_PER_MANUSCRIPT_EXEMPLAR_ROUTER_V1.md` and the shared workflow. Resolve `MANUSCRIPT_ID`, read that manuscript's authoritative private state, and never infer its corpus from chat memory or another project. Missing/stale skill starts initialization and stops at Core 3 approval; approval automatically unlocks analysis. Each substantive section freshly selects and rereads 4–5 exemplars from that manuscript's own Master 20. Micro-edits skip the heavy workflow.

Automatically apply `PAPER_ARTIFACT_AVAILABILITY_PROTOCOL_V1` to papers surfaced, shortlisted, tabulated, compared, used as exemplars, or synthesized; no separate code/data request is needed. Keep monitor audits tiered. Verify repository identity/licenses; failures are `NOT_VERIFIED_DUE_TO_NETWORK`, never no-code/no-data. Every Master 20 entry needs a record; availability is secondary. Codex and ChatGPT use the same private state; never infer artifact records from memory.

When Zotero is available, treat Zotero parent metadata, attachments, PDFs, and indexed full text as the bibliographic source of truth. Treat Research Vault records as derived knowledge, not substitutes for original sources. Never write to Zotero merely because a literature workflow is active.

Repository access and search autonomy do not authorize external writes. Require explicit approval before destructive data changes, publishing, submissions, external messages, merges, force pushes, branch deletion with unique work, private-data exposure, or destructive Zotero changes.

If the GitHub workflow source as a whole is temporarily unavailable, use only the minimal installed Research Orchestrator fallback, state WORKFLOW_SOURCE_FALLBACK_USED, identify what could not be verified, and avoid claiming that fallback rules are current. This source-level fallback does not convert a partial four-file retrieval into a complete bootstrap.
```
