"""Synthetic tests for the global academic contrast and paragraph-rhythm profile."""

from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "evals/academic-writing-exemplar/CONTRAST_OVERUSE_GOLDEN_SET_V1.json"
LINT_PATH = ROOT / "skills/scipilot-writing-skill/scripts/writing_lint.py"
SPEC = importlib.util.spec_from_file_location("academic_contrast_writing_lint", LINT_PATH)
assert SPEC and SPEC.loader
LINT = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = LINT
SPEC.loader.exec_module(LINT)


class AcademicContrastOveruseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
        cls.cases = cls.payload["cases"]

    def test_synthetic_fixture_categories_and_indicators(self) -> None:
        self.assertEqual(
            self.payload["fixture_policy"],
            "SYNTHETIC_ONLY_NO_REAL_MANUSCRIPTS_NO_SCIENTIFIC_RESULT_CLAIMS",
        )
        self.assertEqual([case["id"] for case in self.cases], [f"P{i:02d}" for i in range(1, 8)])
        expected_contexts = {
            "Chinese academic writing",
            "English Results",
            "English Discussion across adjacent paragraphs",
            "General information answer",
            "Methodological review and boundary",
            "Literature-review synthesis paragraph rhythm",
            "Non-academic explanation",
        }
        self.assertEqual({case["context"] for case in self.cases}, expected_contexts)
        self.assertTrue(all(case["preserve_scientific_negation"] is True for case in self.cases))

    def test_contrast_cluster_and_preservation_expectations(self) -> None:
        for case in self.cases:
            with self.subTest(case=case["id"], context=case["context"]):
                issues = LINT.lint_text(case["text"], lang=case["lang"])
                contrast = [issue for issue in issues if issue.code == "AI_NEG_PARALLEL"]
                rhythm = [issue for issue in issues if issue.code == "AI_PARAGRAPH_RHYTHM"]
                expected = case["expected_contrast"]
                if expected == "WARN_CLUSTER":
                    self.assertEqual(len(contrast), 1)
                    self.assertEqual(contrast[0].severity, "WARN")
                else:
                    self.assertEqual(contrast, [], "single valid contrast/required boundary must not be flagged")
                if case.get("expected_rhythm") == "WARN_CLUSTER":
                    self.assertEqual(len(rhythm), 1)
                    self.assertEqual(rhythm[0].severity, "WARN")

    def test_required_chinese_and_english_patterns_are_recognized(self) -> None:
        coverage = self.payload["pattern_coverage"]
        for lang in ("zh", "en"):
            with self.subTest(lang=lang):
                for text in coverage[lang]:
                    self.assertGreaterEqual(len(LINT._contrast_matches(text, lang)), 1, text)

    def test_profile_and_existing_owner_are_wired_without_new_skill(self) -> None:
        profile = (ROOT / "docs/standards/academic_writing_profile_v2.md").read_text(encoding="utf-8")
        scicomm = (ROOT / "skills/agent-auto-sci-scicomm/SKILL.md").read_text(encoding="utf-8")
        exemplar = (ROOT / "docs/workflows/PER_MANUSCRIPT_WRITING_EXEMPLAR_WORKFLOW_V1.md").read_text(encoding="utf-8")
        project = (ROOT / "docs/chatgpt/CHATGPT_PROJECT_RESEARCH_OS_ROUTER_V1.md").read_text(encoding="utf-8")
        global_router = (ROOT / "docs/chatgpt/CHATGPT_GLOBAL_RESEARCH_OS_ROUTER_V1.txt").read_text(encoding="utf-8")
        for token in ("CLAIM_FIRST_PROSE", "DIRECT_RESULT_REPORTING", "EVIDENCE_LED_EXPLANATION", "NATURAL_SENTENCE_VARIATION", "LOW_TEMPLATE_DENSITY", "sentence quotas", "negative results"):
            self.assertIn(token.lower(), profile.lower())
        self.assertIn("name: agent-auto-sci-scicomm", scicomm)
        self.assertIn("ACADEMIC_WRITING_PROFILE_V2", scicomm)
        self.assertIn("evidence-to-interpretation", exemplar)
        self.assertIn("ACADEMIC_WRITING_PROFILE_V2", project)
        self.assertIn("ACADEMIC_WRITING_PROFILE_V2", global_router)
        self.assertIn("one-time user installation", global_router)
        self.assertIn("does not configure or verify Web/Desktop deployment", global_router)
        self.assertTrue((ROOT / "scripts/validation/test_academic_contrast_overuse.py").is_file())


if __name__ == "__main__":
    unittest.main()
