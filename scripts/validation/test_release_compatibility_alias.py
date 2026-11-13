"""Compatibility tests for the canonical and legacy contrast issue identifiers."""
from contextlib import redirect_stdout
from io import StringIO
import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LINT_PATH = ROOT / "skills/scipilot-writing-skill/scripts/writing_lint.py"
SPEC = importlib.util.spec_from_file_location("release_lint", LINT_PATH)
assert SPEC and SPEC.loader
LINT = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = LINT
SPEC.loader.exec_module(LINT)


class IssueCodeCompatibilityTests(unittest.TestCase):
    def setUp(self):
        self.text = (
            "The estimate is not precise but stable. "
            "The association is not universal but conditional."
        )
        self.issues = LINT.lint_text(self.text, lang="en")

    def test_legacy_assertion_and_canonical_contract_are_both_exposed(self):
        contrast = [i for i in self.issues if i.code in {"NOT_BUT_CLUSTER", "AI_NEG_PARALLEL"}]
        self.assertEqual(len(contrast), 2)
        self.assertIn("NOT_BUT_CLUSTER", {i.code for i in contrast})
        legacy = next(i for i in contrast if i.code == "AI_NEG_PARALLEL")
        self.assertEqual(legacy.alias_of, "NOT_BUT_CLUSTER")

    def test_summary_counts_one_logical_warning(self):
        summary = LINT.summarize(self.issues)
        self.assertEqual(summary["warn"], 1)
        self.assertEqual(summary["total"], len(self.issues) - 1)
        self.assertEqual(summary["info"], 1)

    def test_user_report_shows_only_canonical_issue_code(self):
        output = StringIO()
        with redirect_stdout(output):
            exit_code = LINT.print_report(self.issues, "plain", "en")
        self.assertEqual(exit_code, 1)
        self.assertEqual(output.getvalue().count("NOT_BUT_CLUSTER"), 1)
        self.assertNotIn("AI_NEG_PARALLEL", output.getvalue())


if __name__ == "__main__":
    unittest.main()
