"""Synthetic twelve-case table/Word/routing format contract tests."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("format_validator", Path(__file__).with_name("validate_academic_writing_v2.py"))
assert SPEC and SPEC.loader
V = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(V)


def _synthetic_doc(path: Path, manual_break: bool = False, vertical: bool = False) -> None:
    import zipfile
    br = '<w:br/>' if manual_break else ''
    vertical_xml = '<w:insideV w:val="single"/>' if vertical else '<w:insideV w:val="nil"/>'
    xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>
<w:p><w:r><w:t>First paragraph.</w:t></w:r></w:p><w:p><w:r><w:t>Second paragraph.</w:t>{br}</w:r></w:p>
<w:tbl><w:tblPr><w:tblBorders><w:top w:val="single"/><w:bottom w:val="single"/>{vertical_xml}</w:tblBorders></w:tblPr>
<w:tr><w:tc><w:tcPr><w:tcBorders><w:bottom w:val="single"/></w:tcBorders></w:tcPr><w:p><w:r><w:t>Header</w:t></w:r></w:p></w:tc><w:tc><w:tcPr><w:tcBorders><w:bottom w:val="single"/></w:tcBorders></w:tcPr><w:p><w:r><w:t>Unit</w:t></w:r></w:p></w:tc></w:tr>
<w:tr><w:tc><w:p><w:r><w:t>1</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>2 kg</w:t></w:r></w:p></w:tc></w:tr></w:tbl><w:sectPr/></w:body></w:document>'''
    with zipfile.ZipFile(path, 'w') as archive:
        archive.writestr('word/document.xml', xml)


class DocumentFormatContractTests(unittest.TestCase):
    def test_T01_standard_three_line_table(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "t01.docx"; _synthetic_doc(p)
            self.assertEqual([], V.validate_docx_three_line_table(p))

    def test_T02_no_vertical_rules(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "t02.docx"; _synthetic_doc(p)
            self.assertNotIn("UNEXPECTED_VERTICAL_OR_BODY_RULE", V.validate_docx_three_line_table(p))

    def test_T03_header_bottom_rule(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "t03.docx"; _synthetic_doc(p)
            self.assertNotIn("MISSING_HEADER_BOTTOM_RULE", V.validate_docx_three_line_table(p))

    def test_T04_cell_first_character_trimmed(self):
        codes = {x.code for x in V.LINT.lint_text("|Header|Value|\n|---|---|\n|1|2|", mode="markdown", lang="en")}
        self.assertNotIn("CELL_LEADING_WHITESPACE", codes)

    def test_T05_numeric_unit_preserved(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "t05.docx"; _synthetic_doc(p)
            self.assertEqual([], V.validate_docx_three_line_table(p))

    def test_T06_word_paragraph_markers(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "t06.docx"; _synthetic_doc(p)
            self.assertEqual([], V.validate_docx_manual_line_breaks(p))

    def test_T07_word_body_has_no_manual_break(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "t07.docx"; _synthetic_doc(p, manual_break=True)
            self.assertEqual(["MANUAL_LINE_BREAK"], V.validate_docx_manual_line_breaks(p))

    def test_T08_special_pagination_not_removed(self):
        self.assertEqual([], V.validate_no_manual_break("Page one.\n\nPage two."))

    def test_T09_single_valid_contrast_allowed(self):
        codes = {x.code for x in V.LINT.lint_text("This route is not only shorter but also easier.", lang="en")}
        self.assertNotIn("AI_NEG_PARALLEL", codes)

    def test_T10_adjacent_mechanical_contrast_detected(self):
        issues = V.LINT.lint_text("The mechanism is not established but plausible.\n\nThe implication is not universal but local.", lang="en")
        self.assertIn("AI_NEG_PARALLEL", {x.code for x in issues})

    def test_T11_router_parity(self):
        project = (ROOT / "docs/chatgpt/CHATGPT_PROJECT_RESEARCH_OS_ROUTER_V1.md").read_text(encoding="utf-8")
        global_router = (ROOT / "docs/chatgpt/CHATGPT_GLOBAL_RESEARCH_OS_ROUTER_V1.txt").read_text(encoding="utf-8")
        for token in ("DEFAULT_ACADEMIC_WRITING_PREFERENCES", "three-line", "manual line breaks"):
            self.assertIn(token.lower(), project.lower()); self.assertIn(token.lower(), global_router.lower())

    def test_T12_manuscript_state_isolation(self):
        state_a = {"MANUSCRIPT_ID": "A", "EXEMPLAR_STATE": "S8_ACTIVE_FOR_WRITING"}
        state_b = {"MANUSCRIPT_ID": "B", "EXEMPLAR_STATE": "S0_UNINITIALIZED"}
        self.assertNotEqual(state_a["MANUSCRIPT_ID"], state_b["MANUSCRIPT_ID"])


if __name__ == "__main__":
    unittest.main()
