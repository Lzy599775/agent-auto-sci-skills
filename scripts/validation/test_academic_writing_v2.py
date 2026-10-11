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

    def test_source_specific_lint_advisories(self) -> None:
        cases = [
            ("The result may possibly be due to a potential process.", "en", "HEDGE_STACK"),
            ("We cannot infer causality from this result. This is not a causal effect.", "en", "REPEATED_CAUSAL_DISCLAIMER"),
            ("The high_risk_group increased.", "en", "INTERNAL_LABEL_TO_PROSE"),
            ("The non-significant result was due to low statistical power.", "en", "NONSIGNIFICANT_RESULT_ATTRIBUTION"),
            ("We surveyed it; while however: the pattern was (after adjustment), notably—under constraints; and consistently, across time, space, and groups.", "en", "PUNCTUATION_DENSITY"),
            ("This is a city-scale evidence-based planning framework.", "en", "HYPHEN_NOUN_CHAIN"),
        ]
        for text, lang, expected in cases:
            with self.subTest(code=expected):
                codes = {issue.code for issue in MODULE.LINT.lint_text(text, mode="plain", lang=lang)}
                self.assertIn(expected, codes)

    def test_source_specific_contract_preserves_valid_symbols_and_science(self) -> None:
        text = r"The conditional average treatment effect (CATE) was estimated for x_i using \cite{source}; 95% CI was reported."
        codes = {issue.code for issue in MODULE.LINT.lint_text(text, mode="plain", lang="en")}
        self.assertNotIn("HEDGE_STACK", codes)
        self.assertNotIn("NONSIGNIFICANT_RESULT_ATTRIBUTION", codes)

    def test_chinese_mechanical_connectors_include_source_examples(self) -> None:
        text = "此外，结果变化。再者，结果一致。进一步而言，范围较窄。总而言之，仍需解释。由此可见，尚有差异。"
        codes = {issue.code for issue in MODULE.LINT.lint_text(text, mode="plain", lang="zh")}
        self.assertIn("AI_MECH_CONNECTIVE", codes)


if __name__ == "__main__":
    unittest.main()
