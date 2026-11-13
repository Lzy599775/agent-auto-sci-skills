"""Fail-closed local release gate for the writing-lint contract candidate."""
import argparse
import ast
import json
import subprocess
import sys
from pathlib import Path


LINTER_REL = Path("skills/scipilot-writing-skill/scripts/writing_lint.py")
TEST_DIR_REL = Path("scripts/validation")
VALIDATOR_REL = TEST_DIR_REL / "validate_academic_writing_v2.py"
REQUIRED_API = {"Issue", "_contrast_matches", "_check_not_but_cluster", "_check_paragraph_rhythm", "lint_text", "summarize"}


def _run(args: list[str], root: Path) -> subprocess.CompletedProcess:
    return subprocess.run(args, cwd=root, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)


def gate(root: Path) -> dict:
    root = root.resolve()
    lint_path = root / LINTER_REL
    report = {"candidate_status": "ISOLATED_CANDIDATE_NOT_OFFICIAL_RELEASE", "root": str(root), "checks": {}}
    if not lint_path.is_file() or lint_path.stat().st_size == 0:
        report["checks"]["lint_dependency"] = {"status": "FAIL", "reason": "required writing_lint.py missing or empty"}
        report["status"] = "FAIL"
        return report
    try:
        tree = ast.parse(lint_path.read_text(encoding="utf-8"))
        compile(tree, str(lint_path), "exec")
        api = {n.name for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))}
        missing_api = sorted(REQUIRED_API - api)
        report["checks"]["lint_dependency"] = {"status": "PASS" if not missing_api else "FAIL", "missing_api": missing_api}
    except (OSError, SyntaxError, UnicodeError) as exc:
        report["checks"]["lint_dependency"] = {"status": "FAIL", "reason": type(exc).__name__}
        report["status"] = "FAIL"
        return report
    if missing_api:
        report["status"] = "FAIL"
        return report

    tests = _run([sys.executable, "-B", "-m", "unittest", "discover", "-s", str(TEST_DIR_REL), "-p", "test_*.py"], root)
    lines = [line.strip() for line in tests.stdout.splitlines() if line.strip()]
    run_summary = next((line for line in lines if line.startswith("Ran ")), "Ran line missing")
    test_ok = tests.returncode == 0 and "OK" in lines[-1:]
    report["checks"]["regression_suite"] = {"status": "PASS" if test_ok else "FAIL", "exit_code": tests.returncode, "summary": run_summary, "failure_markers": [line for line in lines if line.startswith(("FAIL:", "ERROR:"))]}

    validator_path = root / VALIDATOR_REL
    if not validator_path.is_file():
        report["checks"]["academic_validator"] = {"status": "FAIL", "reason": "validator missing"}
    else:
        validation = _run([sys.executable, "-B", str(VALIDATOR_REL), "--repo-root", str(root)], root)
        marker = next((line.strip() for line in validation.stdout.splitlines() if line.startswith("ACADEMIC_WRITING_V2=")), "validator result marker missing")
        report["checks"]["academic_validator"] = {"status": "PASS" if validation.returncode == 0 and marker.endswith("=PASS") else "FAIL", "exit_code": validation.returncode, "summary": marker}

    report["status"] = "PASS" if all(item["status"] == "PASS" for item in report["checks"].values()) else "FAIL"
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    result = gate(args.root)
    if args.report:
        report_path = args.report.resolve()
        try:
            report_path.relative_to(args.root.resolve())
        except ValueError:
            parser.error("report path must remain under --root")
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "PASS" else 1)
