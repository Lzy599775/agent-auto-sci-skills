"""Validate the evidence-first writing-exemplar routing golden set.

This is a small deterministic contract check for the Markdown routing rules. It
does not replace model judgment or retrieve literature; it prevents drift in
the required/automatic/skip modes and the scientific safety boundaries.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


EXPECTED_IDS = {f"G{i:02d}" for i in range(1, 13)}
SKIP_KINDS = {
    "sentence_proofreading",
    "grammar_only",
    "citation_format_only",
    "minor_typo",
    "caption_micro_edit",
    "pure_code",
}
SUBSTANTIVE_KINDS = {
    "introduction_rewrite",
    "discussion_rewrite",
    "conclusion_rewrite",
    "abstract_rewrite",
    "full_manuscript",
    "review_synthesis",
    "major_restructuring",
    "substantive_writing",
}


def classify_mode(case: dict[str, Any]) -> str:
    kind = case.get("task_kind")
    if kind in SKIP_KINDS:
        return "SKIP"
    if kind == "explicit_exemplar_adaptation" or case.get("named_exemplars"):
        return "REQUIRED"
    if kind in SUBSTANTIVE_KINDS:
        return "AUTO"
    return "SKIP"


def classify(case: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {"mode": classify_mode(case)}
    kind = case.get("task_kind")
    result["exemplar_search"] = result["mode"] in {"REQUIRED", "AUTO"} and bool(
        case.get("exemplar_available", True)
    )
    result["guard"] = kind in SUBSTANTIVE_KINDS or result["mode"] == "REQUIRED"
    if result["mode"] == "REQUIRED":
        result["anti_copying"] = True
    if kind in SUBSTANTIVE_KINDS:
        result["route_after_draft"] = "Academic Prose Style Guard"

    if kind == "exemplar_selection":
        candidates = case.get("selection_candidates", [])
        if candidates:
            selected = max(
                candidates,
                key=lambda item: (
                    float(item.get("topic_proximity", 0.0))
                    + float(item.get("rq_proximity", 0.0))
                    + float(item.get("design_proximity", 0.0))
                    + float(item.get("outcome_proximity", 0.0)),
                    float(item.get("if", 0.0)),
                ),
            )
            result["selection_preference"] = (
                "scientific_near_neighbor" if selected["id"] == "near-neighbor" else selected["id"]
            )

    if kind == "read_scope":
        scope = case.get("read_scope")
        result["read_scope"] = scope
        result["fulltext_structure_claim"] = scope == "FULLTEXT"

    if kind == "claim_boundary":
        observational = case.get("our_design") == "observational"
        causal_exemplar = case.get("exemplar_claim") == "causal"
        result["causal_transfer"] = "prohibited" if observational and causal_exemplar else "review"
        result["claim_ladder_max"] = "association" if observational else "design-dependent"

    if kind == "results_prioritization":
        result.update(
            core_first=True,
            compress_secondary=True,
            retain_necessary=True,
            mechanism_in_results=False,
        )

    if kind == "abstract_precedence":
        result.update(
            precedence=(
                "OFFICIAL_JOURNAL_REQUIREMENT"
                if case.get("journal_structured_abstract")
                else "USER_ABSTRACT_PREFERENCE"
            ),
            profile_is_soft=True,
        )

    if kind == "metadata_hygiene":
        result.update(
            hidden_unicode_allowed=bool(case.get("hidden_unicode")),
            provenance_auto_strip=False,
        )

    if kind == "anti_copying":
        high_similarity = case.get("source_similarity") == "high"
        result.update(
            anti_copying_flag=high_similarity,
            action="rewrite_from_our_evidence" if high_similarity else "retain_after_review",
        )

    return result


def assert_expected(case: dict[str, Any], actual: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    for key, expected in case.get("expected", {}).items():
        if actual.get(key) != expected:
            failures.append(
                f"{case['id']}: {key} expected {expected!r}, got {actual.get(key)!r}"
            )
    return failures


def validate_contract(repo_root: Path) -> list[str]:
    failures: list[str] = []
    protocol = (
        repo_root
        / "skills"
        / "agent-auto-sci-scicomm"
        / "references"
        / "academic_writing_exemplar_protocol.md"
    )
    matrix = repo_root / "docs" / "CROSS_CLIENT_WRITING_ROUTING_MATRIX_V1.md"
    fixture = (
        repo_root
        / "skills"
        / "agent-auto-sci-scicomm"
        / "tests"
        / "writing_exemplar_golden_set.json"
    )
    for path in (protocol, matrix, fixture):
        if not path.is_file():
            failures.append(f"missing required routing artifact: {path}")

    if failures:
        return failures

    protocol_text = protocol.read_text(encoding="utf-8")
    required_fragments = (
        "WRITING_EXEMPLAR_MODE",
        "REQUIRED",
        "AUTO",
        "SKIP",
        "FULLTEXT",
        "ABSTRACT_ONLY",
        "METADATA_ONLY",
        "Article Story Map",
        "Introduction Move Map",
        "Methods Logic Map",
        "Results Argument Map",
        "Figure Argument Map",
        "Discussion Move Map",
        "Claim Ladder",
        "Anti-copying contract",
        "OUR_EVIDENCE_MAP",
        "OUR_ARGUMENT_OUTLINE",
        "PREFERRED_EMPIRICAL_ABSTRACT_PROFILE",
        "OFFICIAL_JOURNAL_REQUIREMENT",
        "ACADEMIC_HUMANIZER_AVAILABLE = NO",
        "REMOVE_AI_MARKS_AVAILABLE = NO",
        "CLEAN_USER_FACING_TEXT_AVAILABLE = NO",
        "PROVENANCE_METADATA_AUTO_STRIP = NO",
        "Handoff to polishing/lint",
    )
    for fragment in required_fragments:
        if fragment not in protocol_text:
            failures.append(f"protocol missing required contract fragment: {fragment}")
    misspelled_token = "EX" + "AMPLAR_"
    if misspelled_token in protocol_text:
        failures.append("protocol contains a misspelled exemplar token")
    forbidden_tokens = (
        "C:" + "\\Users\\LI ZEYANG",
        "C:" + "\\Users\\HP\\",
        "sk-",
        "BEGIN OPENSSH " + "PRIVATE KEY",
    )
    for forbidden in forbidden_tokens:
        if forbidden.lower() in protocol_text.lower():
            failures.append(f"protocol contains forbidden public-safety token: {forbidden}")

    matrix_text = matrix.read_text(encoding="utf-8")
    for fragment in (
        "Codex expected route",
        "ChatGPT Web expected route",
        "scientific contract",
        "anti-copying",
        "FULLTEXT",
    ):
        if fragment.lower() not in matrix_text.lower():
            failures.append(f"cross-client matrix missing: {fragment}")

    payload = json.loads(fixture.read_text(encoding="utf-8"))
    cases = payload.get("cases", [])
    ids = {case.get("id") for case in cases}
    if payload.get("case_count") != 12 or len(cases) != 12 or ids != EXPECTED_IDS:
        failures.append(
            f"golden set must contain exactly G01-G12; count={len(cases)}, ids={sorted(ids)}"
        )
    for case in cases:
        failures.extend(assert_expected(case, classify(case)))

    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="repository root (defaults to the parent of scripts/validation)",
    )
    args = parser.parse_args()
    failures = validate_contract(args.repo_root.resolve())
    if failures:
        print("WRITING_EXEMPLAR_ROUTING=FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("WRITING_EXEMPLAR_ROUTING=PASS")
    print("GOLDEN_SET_CASE_COUNT=12")
    print("MODES=REQUIRED/AUTO/SKIP")
    print("READ_SCOPE_CONTRACT=FULLTEXT|ABSTRACT_ONLY|METADATA_ONLY")
    print("PROVENANCE_METADATA_AUTO_STRIP=NO")
    return 0


if __name__ == "__main__":
    sys.exit(main())
