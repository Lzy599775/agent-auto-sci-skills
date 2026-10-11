"""Deterministic checks for the V2 academic-writing contract.

The validator checks the public contract and executes the conservative lint
fixtures. It does not decide whether a scientific caveat is necessary; those
story/evidence judgments remain advisory review work.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
LINT_PATH = ROOT / "skills" / "scipilot-writing-skill" / "scripts" / "writing_lint.py"
SPEC = importlib.util.spec_from_file_location("academic_writing_lint_v2", LINT_PATH)
assert SPEC and SPEC.loader
LINT = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = LINT
SPEC.loader.exec_module(LINT)


def classify_exemplar(case: dict[str, Any]) -> dict[str, Any]:
    kind = case.get("task_kind")
    if kind == "explicit_exemplar_adaptation":
        return {"mode": "REQUIRED"}
    if kind in {"introduction_rewrite", "discussion_rewrite", "abstract_rewrite", "full_manuscript"}:
        return {"mode": "AUTO"}
    if kind == "sentence_proofreading":
        return {"mode": "SKIP"}
    if kind == "read_scope":
        return {"read_scope": case.get("read_scope")}
    if kind == "anti_copying":
        if case.get("source_similarity") == "high":
            return {"action": "BLOCK"}
        return {"action": "REWRITE_GENERICALLY"}
    return {"mode": "SKIP"}


def validate_three_line_table(text: str, mode: str) -> list[str]:
    """Validate the semantic table contract for small text fixtures."""
    if mode == "markdown":
        return ["PREVIEW_ONLY"]
    failures: list[str] = []
    if mode == "latex":
        for token in (r"\toprule", r"\midrule", r"\bottomrule"):
            if token not in text:
                failures.append(f"missing {token}")
        if re.search(r"\\begin\{tabular\}\{[^}]*\|", text) or "\\vline" in text:
            failures.append("vertical rule present")
        for line_number, line in enumerate(text.splitlines(), start=1):
            cells = LINT._table_line_cells(line, mode)
            if any(re.match(r"^(?:\t| {2,}|　{2,})", cell) for cell in cells):
                failures.append(f"leading cell whitespace at line {line_number}")
    elif mode == "word":
        required = ("TOP_BORDER", "HEADER_BOTTOM_BORDER", "BOTTOM_BORDER")
        for token in required:
            if token not in text:
                failures.append(f"missing {token}")
        if "VERTICAL_BORDER" in text:
            failures.append("vertical rule present")
    else:
        failures.append(f"unsupported final table mode: {mode}")
    return failures


def validate_no_manual_break(text: str, mode: str = "plain") -> list[str]:
    codes = {issue.code for issue in LINT.lint_text(text, mode=mode, lang="en")}
    return ["MANUAL_LINE_BREAK"] if "MANUAL_LINE_BREAK" in codes else []


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_contract(repo_root: Path = ROOT) -> list[str]:
    failures: list[str] = []
    required = [
        repo_root / "USER_POLISHING_PROMPT_RULE_MAPPING_V1.md",
        repo_root / "CHATGPT_GLOBAL_ACADEMIC_WRITING_INSTRUCTIONS_V2.txt",
        repo_root / "skills" / "agent-auto-sci-scicomm" / "references" / "academic_writing_exemplar_protocol.md",
        repo_root / "skills" / "agent-auto-sci-scicomm" / "references" / "academic_prose_style_guard.md",
        repo_root / "skills" / "scipilot-writing-skill" / "scripts" / "writing_lint.py",
        repo_root / "scripts" / "validation" / "writing_redundancy_golden_set_v2.json",
        repo_root / "skills" / "agent-auto-sci-scicomm" / "tests" / "writing_exemplar_golden_set_v2.json",
    ]
    for path in required:
        if not path.is_file():
            failures.append(f"missing V2 artifact: {path.relative_to(repo_root)}")
    if failures:
        return failures

    protocol = (repo_root / "skills" / "agent-auto-sci-scicomm" / "references" / "academic_writing_exemplar_protocol.md").read_text(encoding="utf-8")
    guard = (repo_root / "skills" / "agent-auto-sci-scicomm" / "references" / "academic_prose_style_guard.md").read_text(encoding="utf-8")
    mapping = (repo_root / "USER_POLISHING_PROMPT_RULE_MAPPING_V1.md").read_text(encoding="utf-8")
    global_text = (repo_root / "CHATGPT_GLOBAL_ACADEMIC_WRITING_INSTRUCTIONS_V2.txt").read_text(encoding="utf-8")
    for label, text, fragments in (
        ("protocol", protocol, ("DEFAULT_ACADEMIC_WRITING_PREFERENCES", "NOT_BUT_CONSTRUCTION_CLUSTER", "STORY_RELEVANCE_AND_DEFENSE_AUDIT", "ROBUSTNESS_PLACEMENT_RULE", "THREE_LINE_TABLE_CONTRACT", "NO_MANUAL_LINE_BREAK_IN_PROSE", "FIGURE_TABLE_CITATION_LEDGER", "FACT_PLACEMENT_LEDGER", "PROVENANCE_METADATA_STRIPPING = EXPLICIT_OPT_IN_ONLY")),
        ("guard", guard, ("NOT_BUT_CONSTRUCTION_CLUSTER", "STORY_RELEVANCE_AND_DEFENSE_AUDIT", "REDUNDANT_LOW_INCREMENT", "REPEATED_LOW_VALUE_NUMBER", "REPEATED_FIGURE_CITATION", "ROBUSTNESS_PLACEMENT_RULE")),
        ("mapping", mapping, ("SOURCE_RULE", "GENERIC_WORKFLOW_RULE", "IMPLEMENTATION_LOCATION", "TEST_CASE", "ADOPT", "ADAPT", "SOFT_PREFERENCE", "S01", "S46")),
        ("global instructions", global_text, ("PREVIEW_ONLY", "NO_MANUAL_LINE_BREAK_IN_PROSE", "USER_UI_ACTION_REQUIRED_FOR_ALL_WEB_CHATS = YES", "CHATGPT_ACCOUNT_SETTINGS_MODIFIED = NO")),
    ):
        for fragment in fragments:
            if fragment not in text:
                failures.append(f"{label} missing required fragment: {fragment}")

    redundancy = _load_json(repo_root / "scripts" / "validation" / "writing_redundancy_golden_set_v2.json")
    if redundancy.get("case_count") != 12 or len(redundancy.get("cases", [])) != 12:
        failures.append("redundancy golden set must contain 12 cases")
    expected_ids = {f"R{i:02d}" for i in range(1, 13)}
    if {case.get("id") for case in redundancy.get("cases", [])} != expected_ids:
        failures.append("redundancy golden set IDs must be R01-R12")
    for case in redundancy.get("cases", []):
        issues = LINT.lint_text(case.get("input", ""), mode="plain", lang="en")
        codes = {issue.code for issue in issues}
        expected = case.get("expected")
        if expected == "WARN_REPEATED_LOW_VALUE_NUMBER" and "REPEATED_LOW_VALUE_NUMBER_CANDIDATE" not in codes:
            failures.append(f"{case['id']} did not emit repeated-number advisory")
        if expected == "ALLOW_REQUIRED_REPETITION" and "REPEATED_LOW_VALUE_NUMBER_CANDIDATE" in codes:
            failures.append(f"{case['id']} incorrectly warned on allowed abstract/methods repetition")
        if expected == "WARN_REPEATED_FIGURE_CITATION" and "REPEATED_FIGURE_CITATION_CANDIDATE" not in codes:
            failures.append(f"{case['id']} did not emit repeated-figure advisory")
        if expected == "PASS_SINGLE_CONTRAST" and "NOT_BUT_CLUSTER" in codes:
            failures.append(f"{case['id']} incorrectly flagged one contrast")
        if expected == "WARN_NOT_BUT_CLUSTER" and "NOT_BUT_CLUSTER" not in codes:
            failures.append(f"{case['id']} did not emit not-but cluster advisory")

    exemplar = _load_json(repo_root / "skills" / "agent-auto-sci-scicomm" / "tests" / "writing_exemplar_golden_set_v2.json")
    if exemplar.get("case_count") != 6 or len(exemplar.get("cases", [])) != 6:
        failures.append("V2 exemplar golden set must contain 6 cases")
    for case in exemplar.get("cases", []):
        actual = classify_exemplar(case)
        expected = {key: value for key, value in case.items() if key.startswith("expected_")}
        expected = {key.removeprefix("expected_"): value for key, value in expected.items()}
        for key, value in expected.items():
            if actual.get(key) != value:
                failures.append(f"{case['id']}: {key} expected {value!r}, got {actual.get(key)!r}")

    latex_good = r"\begin{tabular}{lr}\toprule A & B \\ \midrule 1 & 2 \\ \bottomrule\end{tabular}"
    if validate_three_line_table(latex_good, "latex"):
        failures.append("valid LaTeX three-line fixture failed")
    if validate_three_line_table("| A | B |\n|---|---|\n| 1 | 2 |", "markdown") != ["PREVIEW_ONLY"]:
        failures.append("Markdown table must be marked PREVIEW_ONLY")
    if not validate_no_manual_break("First line\nsecond line", "plain"):
        failures.append("soft line-break fixture did not warn")
    if validate_no_manual_break("First paragraph.\n\nSecond paragraph.", "plain"):
        failures.append("normal paragraph boundary was incorrectly flagged")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    args = parser.parse_args()
    failures = validate_contract(args.repo_root.resolve())
    if failures:
        print("ACADEMIC_WRITING_V2=FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("ACADEMIC_WRITING_V2=PASS")
    print("REDUNDANCY_GOLDEN_SET=R01-R12")
    print("EXEMPLAR_GOLDEN_SET=E01-E06")
    print("THREE_LINE_TABLE=PASS")
    print("NO_MANUAL_LINE_BREAK=PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
