"""Validate generic routing contracts; no natural-language classifier or client execution.

The synthetic resolver takes a reviewed semantic intent, never a raw user prompt.
It models private-state access for tests only; it is not an installed project-state loader.
"""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[2]
CONTRACT = "docs/workflows/ROUTING_DECISION_CONTRACT_V1.json"
GOLDEN = "evals/routing/GENERAL_PURPOSE_ROUTING_GOLDEN_SET_V1.json"
STATE_FIXTURE = "evals/routing/SYNTHETIC_PROJECT_STATES_V1.json"
ENTRYPOINTS = (
    "skills/research-orchestrator/SKILL.md",
    "docs/chatgpt/project_instructions.md",
    "docs/chatgpt/CHATGPT_PROJECT_RESEARCH_OS_ROUTER_V1.md",
    "docs/chatgpt/CHATGPT_GLOBAL_RESEARCH_OS_ROUTER_V1.txt",
    "docs/chatgpt/cross_surface_contract.md",
    "dist/chatgpt/project_instructions.txt",
)


def load_contract(root: Path = ROOT) -> dict:
    return json.loads((root / CONTRACT).read_text(encoding="utf-8"))


def resolve_contract(intent: str, *, root: Path = ROOT) -> dict:
    """Resolve an interpreted deliverable. Unknown/ambiguous intent fails closed."""
    contract = load_contract(root)
    if intent not in contract["intents"]:
        raise ValueError("INTENT_NOT_VERIFIED: interpret the deliverable before routing")
    result = deepcopy(contract["intents"][intent])
    result["zotero_write_authorized"] = False
    return result


def evaluate_synthetic_state_access(
    intent: str,
    manuscript_id: str | None,
    read_state: Callable[[str], dict],
) -> dict:
    """Executable test model of the documented identity/approval boundary.

    A caller injects a synthetic reader. No discovery, filesystem scan, real project
    lookup, persistence, Zotero API, or inherited chat state exists in this evaluator.
    """
    decision = resolve_contract(intent)
    decision.update(gate="NOT_REQUIRED", state=None)
    if decision["private_state"] == "none":
        return decision
    if not manuscript_id or not manuscript_id.strip():
        decision["gate"] = "MANUSCRIPT_IDENTITY_UNCERTAIN"
        return decision
    try:
        state = deepcopy(read_state(manuscript_id))
    except KeyError:
        decision["gate"] = "STATE_NOT_VERIFIED"
        return decision
    if state.get("MANUSCRIPT_ID") != manuscript_id:
        decision["gate"] = "STATE_IDENTITY_CONFLICT"
        return decision
    decision["state"] = state
    if state.get("CORE3_APPROVED") is not True:
        decision["gate"] = "BLOCK_PENDING_CORE3_APPROVAL"
    elif state.get("PROJECT_STATE") != "S8_ACTIVE_FOR_WRITING":
        decision["gate"] = "STATE_REFRESH_OR_INITIALIZATION_REQUIRED"
    elif not all(state.get(key) for key in ("MASTER20_VERSION", "CORE3_VERSION")):
        decision["gate"] = "STATE_NOT_VERIFIED"
    else:
        decision["gate"] = "ALLOW_SUBSTANTIVE_WRITING"
    return decision


def golden_results(root: Path = ROOT) -> list[dict]:
    """Compute contract results; does not claim to interpret the fixture's prompt."""
    cases = json.loads((root / GOLDEN).read_text(encoding="utf-8"))["cases"]
    results = []
    for case in cases:
        actual = resolve_contract(case["INTERPRETED_INTENT"], root=root)
        passed = (
            actual["primary_route"] == case["EXPECTED_PRIMARY_ROUTE"]
            and actual["specialist"] == case["EXPECTED_SPECIALIST_SKILL"]
            and actual["companions"] == case["EXPECTED_COMPANION"]
        )
        results.append({
            "id": case["id"], "TASK_INPUT": case["TASK_INPUT"],
            "EXPECTED_PRIMARY_ROUTE": case["EXPECTED_PRIMARY_ROUTE"],
            "EXPECTED_COMPANION": case["EXPECTED_COMPANION"],
            "EXPECTED_SPECIALIST_SKILL": case["EXPECTED_SPECIALIST_SKILL"],
            "ACTUAL_ROUTE": actual["primary_route"],
            "PASS_OR_FAIL": "PASS" if passed else "FAIL",
            "EVIDENCE_TYPE": "SEMANTIC_INTENT_CONTRACT_EVALUATION_ONLY",
        })
    return results


def validate_contract(root: Path = ROOT) -> list[str]:
    errors = []
    contract = load_contract(root)
    if contract["default_domain"] is not None or contract["private_state_default"] != "deny":
        errors.append("global topic/private-state defaults must be absent/deny")
    if contract["zotero_write_default"] is not False:
        errors.append("routing must not authorize Zotero writes")
    for intent, rule in contract["intents"].items():
        if not (root / "docs/workflows" / (rule["primary_route"] + ".md")).is_file():
            errors.append(f"missing primary workflow: {intent}")
        if rule["specialist"] and not (root / "skills" / rule["specialist"] / "SKILL.md").is_file():
            errors.append(f"missing specialist: {intent}")
        for companion in rule["companions"]:
            if not (root / "docs/workflows" / (companion + ".md")).is_file():
                errors.append(f"missing companion: {intent}: {companion}")
        expected_private = "identity_then_approval" if intent == "substantive_writing" else "none"
        if rule["private_state"] != expected_private:
            errors.append(f"exemplar-state boundary drift: {intent}")
    for relative in ENTRYPOINTS:
        text = (root / relative).read_text(encoding="utf-8")
        if "ROUTING_DECISION_CONTRACT_V1.json" not in text:
            errors.append(f"entrypoint must defer to canonical decision contract: {relative}")
        if "agent-auto-sci-methodology" not in text or "methodology" not in text:
            errors.append(f"missing methodology handoff: {relative}")
    source = root / "skills/research-orchestrator"
    source_files = {p.relative_to(source) for p in source.rglob("*") if p.is_file()}
    for relative in (
        ".agents/plugins/plugins/agentic-research-workflow/skills/research-orchestrator",
        "dist/chatgpt/research-orchestrator-skill",
    ):
        mirror = root / relative
        mirror_files = {p.relative_to(mirror) for p in mirror.rglob("*") if p.is_file()}
        if source_files != mirror_files:
            errors.append(f"mirror file-set drift: {relative}")
        for path in source_files & mirror_files:
            if (source / path).read_bytes() != (mirror / path).read_bytes():
                errors.append(f"mirror content drift: {relative}/{path.as_posix()}")
    project = (root / "docs/chatgpt/project_instructions.md").read_text(encoding="utf-8")
    copy_ready = project.split("```text\n", 1)[1].split("```", 1)[0].strip()
    if copy_ready != (root / "dist/chatgpt/project_instructions.txt").read_text(encoding="utf-8").strip():
        errors.append("distribution Project instructions drift")
    errors.extend(f"golden case failed: {r['id']}" for r in golden_results(root) if r["PASS_OR_FAIL"] != "PASS")
    return errors


if __name__ == "__main__":
    failures = validate_contract()
    print(json.dumps({"scope": "STATIC_AND_SYNTHETIC_CONTRACT_ONLY", "results": golden_results(),
                      "failures": failures}, ensure_ascii=False, indent=2))
    raise SystemExit(bool(failures))
