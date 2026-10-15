"""Validate the synthetic paper-artifact and per-manuscript cross-client contract."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


EXPECTED = {f"A{i:02d}" for i in range(1, 17)}
ROOT = Path(__file__).resolve().parents[2]


def validate_contract(repo_root: Path) -> list[str]:
    failures: list[str] = []
    fixture_path = repo_root / "evals/literature/PAPER_ARTIFACT_AND_WRITING_ROUTING_GOLDEN_SET_V1.json"
    required_files = [
        repo_root / "docs/workflows/PAPER_ARTIFACT_AVAILABILITY_PROTOCOL_V1.md",
        repo_root / "templates/PAPER_ARTIFACT_RECORD_TEMPLATE_V1.yaml",
        repo_root / "templates/CROSS_CLIENT_MANUSCRIPT_STATE_CONTRACT_V1.yaml",
        repo_root / "docs/chatgpt/CHATGPT_PROJECT_RESEARCH_OS_ROUTER_V1.md",
        repo_root / "docs/chatgpt/CHATGPT_GLOBAL_RESEARCH_OS_ROUTER_V1.txt",
        repo_root / "skills/literature/SKILL.md",
        repo_root / "skills/agent-auto-sci-scicomm/SKILL.md",
        repo_root / "docs/workflows/PER_MANUSCRIPT_WRITING_EXEMPLAR_WORKFLOW_V1.md",
    ]
    if not fixture_path.is_file():
        failures.append(f"missing golden set: {fixture_path}")
        return failures
    for path in required_files:
        if not path.is_file():
            failures.append(f"missing contract file: {path}")
    if failures:
        return failures

    payload = json.loads(fixture_path.read_text(encoding="utf-8"))
    cases = payload.get("cases", [])
    ids = {case.get("id") for case in cases}
    if ids != EXPECTED or len(cases) != 16:
        failures.append(f"golden set must contain exactly A01-A16; count={len(cases)}, ids={sorted(ids)}")
    if payload.get("fixture_policy") != "SYNTHETIC_ONLY_NO_REAL_PAPERS_NO_REAL_MANUSCRIPTS":
        failures.append("golden set must explicitly enforce synthetic-only fixtures")
    for case in cases:
        if case.get("synthetic") is not True or not case.get("expected"):
            failures.append(f"{case.get('id')}: case must be synthetic and declare an expected outcome")

    protocol = (repo_root / "docs/workflows/PAPER_ARTIFACT_AVAILABILITY_PROTOCOL_V1.md").read_text(encoding="utf-8")
    schema = (repo_root / "templates/PAPER_ARTIFACT_RECORD_TEMPLATE_V1.yaml").read_text(encoding="utf-8")
    state = (repo_root / "templates/CROSS_CLIENT_MANUSCRIPT_STATE_CONTRACT_V1.yaml").read_text(encoding="utf-8")
    project_router = (repo_root / "docs/chatgpt/CHATGPT_PROJECT_RESEARCH_OS_ROUTER_V1.md").read_text(encoding="utf-8")
    global_router = (repo_root / "docs/chatgpt/CHATGPT_GLOBAL_RESEARCH_OS_ROUTER_V1.txt").read_text(encoding="utf-8")
    literature_skill = (repo_root / "skills/literature/SKILL.md").read_text(encoding="utf-8")
    writing_skill = (repo_root / "skills/agent-auto-sci-scicomm/SKILL.md").read_text(encoding="utf-8")
    manuscript_workflow = (repo_root / "docs/workflows/PER_MANUSCRIPT_WRITING_EXEMPLAR_WORKFLOW_V1.md").read_text(encoding="utf-8")

    for state_name in ("NOT_SEARCHED", "SEARCHED_NOT_FOUND", "CANDIDATE_REPOSITORY_FOUND", "VERIFIED_PUBLIC", "PARTIALLY_PUBLIC", "RESTRICTED", "REQUEST_ONLY", "BROKEN_LINK"):
        if state_name not in protocol:
            failures.append(f"protocol missing code/data availability state: {state_name}")
    for fragment in ("SUPPLEMENT_STATUS", "REPOSITORY_IDENTITY", "LICENSE_NOT_FOUND", "R0_NO_PUBLIC_ARTIFACT_FOUND", "R5_TARGET_RESULT_REPRODUCED", "NOT_VERIFIED_DUE_TO_NETWORK", "CODE_PUBLIC_VERIFIED", "Core 3 ranking", "Master 20", "DISCOVERY_RAW"):
        if fragment.lower() not in protocol.lower():
            failures.append(f"protocol missing required artifact invariant: {fragment}")
    for fragment in ("canonical_paper_id:", "artifact_searched_at:", "code_license:", "data_license:", "verification_evidence:", "queries_and_surfaces_checked:"):
        if fragment not in schema:
            failures.append(f"paper artifact schema missing: {fragment}")
    for fragment in ("MANUSCRIPT_ID:", "EXEMPLAR_STATE:", "MASTER20_VERSION:", "CORE3_VERSION:", "PROJECT_SKILL_VERSION:", "PAPER_ARTIFACT_RECORDS:"):
        if fragment not in state:
            failures.append(f"cross-client state contract missing: {fragment}")
    for label, text in (("Project router", project_router), ("Global router", global_router)):
        for fragment in ("PAPER_ARTIFACT_AVAILABILITY_PROTOCOL_V1", "substantive", "private state", "micro-edit"):
            if fragment.lower() not in text.lower():
                failures.append(f"{label} missing automatic routing invariant: {fragment}")
    if "automatically" not in literature_skill.lower() or "PAPER_ARTIFACT_AVAILABILITY_PROTOCOL_V1" not in literature_skill:
        failures.append("Literature Skill does not automatically invoke the artifact protocol")
    if "automatically" not in writing_skill.lower() or "PAPER_ARTIFACT_RECORDS" not in writing_skill:
        failures.append("Writing owner does not automatically check the shared per-manuscript state")
    if "4–5" not in manuscript_workflow or "No fixed global corpus" not in manuscript_workflow:
        failures.append("per-manuscript workflow missing section refresh or no-global-corpus invariant")

    # Ensure both automatic behaviors are represented and all route cases remain explicit.
    expected_by_id: dict[str, str] = {case["id"]: case["expected"] for case in cases}
    required_outcomes = {
        "A01": "AUTO_LEVEL_1_FOR_SURFACED_PAPERS",
        "A02": "SEARCHED_NOT_FOUND_NOT_NO_CODE_OR_NO_DATA",
        "A07": "DEGRADED_NOT_VERIFIED_DUE_TO_NETWORK",
        "A10": "EVERY_MASTER20_RECORD_HAS_ARTIFACT_RECORD",
        "A12": "NO_CROSS_MANUSCRIPT_CORPUS_OR_STATUS_REUSE",
        "A14": "MICRO_EDIT_SKIPS_HEAVY_INITIALIZATION",
        "A15": "CODEX_AUTO_ARTIFACT_ROUTE",
        "A16": "CHATGPT_AUTO_PER_MANUSCRIPT_ROUTE_SAME_LOGIC",
    }
    for case_id, expected in required_outcomes.items():
        if expected_by_id.get(case_id) != expected:
            failures.append(f"{case_id}: expected outcome must be {expected}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    args = parser.parse_args()
    failures = validate_contract(args.repo_root.resolve())
    if failures:
        print("PAPER_ARTIFACT_AND_WRITING_ROUTING=FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("PAPER_ARTIFACT_AND_WRITING_ROUTING=PASS")
    print("SYNTHETIC_GOLDEN_SET_CASES=16")
    print("REAL_PAPER_SEARCH=NO")
    print("REAL_EXEMPLAR_SELECTION=NO")
    return 0


if __name__ == "__main__":
    sys.exit(main())
