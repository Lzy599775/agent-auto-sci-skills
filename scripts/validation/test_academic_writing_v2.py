"""Unit tests for the V2 writing contract and deterministic lint fixtures."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = Path(__file__).with_name("validate_academic_writing_v2.py")
SPEC = importlib.util.spec_from_file_location("academic_writing_v2_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class AcademicWritingV2Tests(unittest.TestCase):
    def test_public_contract_and_golden_sets(self) -> None:
        failures = MODULE.validate_contract(ROOT)
        self.assertEqual([], failures, "\n".join(failures))

    def test_three_line_table_contracts(self) -> None:
        good = r"\begin{tabular}{lr}\toprule A & B \\ \midrule 1 & 2 \\ \bottomrule\end{tabular}"
        self.assertEqual([], MODULE.validate_three_line_table(good, "latex"))
        self.assertEqual(["PREVIEW_ONLY"], MODULE.validate_three_line_table("|a|b|", "markdown"))
        self.assertTrue(MODULE.validate_three_line_table("TOP_BORDER\nHEADER_BOTTOM_BORDER\nBOTTOM_BORDER", "word") == [])
        bad = r"\begin{tabular}{l|r}\toprule A & B \\ \midrule  1 & 2 \\ \bottomrule\end{tabular}"
        self.assertTrue(MODULE.validate_three_line_table(bad, "latex"))

    def test_no_manual_break_contract(self) -> None:
        self.assertEqual([], MODULE.validate_no_manual_break("First paragraph.\n\nSecond paragraph."))
        self.assertEqual(["MANUAL_LINE_BREAK"], MODULE.validate_no_manual_break("First line\nsecond line"))
        self.assertEqual(["MANUAL_LINE_BREAK"], MODULE.validate_no_manual_break("First<br>Second"))
        for marker in ("  \n", "\u2028", "\u2029", "\x0b"):
            self.assertEqual(["MANUAL_LINE_BREAK"], MODULE.validate_no_manual_break(f"First{marker}Second"))

    def test_cell_whitespace_is_advisory(self) -> None:
        issues = MODULE.LINT.lint_text("| Header | Value |\n|---|---|\n|  1 |\t2 |", mode="markdown", lang="en")
        self.assertIn("CELL_LEADING_WHITESPACE", {issue.code for issue in issues})

    def test_figure_first_use_order_is_advisory(self) -> None:
        issues = MODULE.LINT.lint_text("Figure 3 is introduced. Figure 2 is introduced later.", mode="plain", lang="en")
        self.assertIn("FIGURE_TABLE_ORDER", {issue.code for issue in issues})


if __name__ == "__main__":
    unittest.main()
