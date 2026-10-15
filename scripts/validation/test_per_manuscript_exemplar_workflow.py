from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GOLDEN = ROOT / "evals/academic-writing-exemplar/PER_MANUSCRIPT_EXEMPLAR_ROUTING_GOLDEN_SET_V1.json"
STATE_DOC = ROOT / "docs/workflows/PER_MANUSCRIPT_EXEMPLAR_STATE_MACHINE_V1.md"
WORKFLOW_DOC = ROOT / "docs/workflows/PER_MANUSCRIPT_WRITING_EXEMPLAR_WORKFLOW_V1.md"


class PerManuscriptWorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(GOLDEN.read_text(encoding="utf-8"))
        cls.cases = cls.payload["cases"]

    def test_golden_set_is_synthetic_and_complete(self) -> None:
        self.assertEqual(self.payload["fixture_policy"], "SYNTHETIC_ONLY_NO_REAL_PAPERS_NO_REAL_MANUSCRIPT_IDENTIFIERS")
        self.assertEqual([case["id"] for case in self.cases], [f"G{i:02}" for i in range(1, 16)])
        self.assertTrue(all(case["synthetic"] is True for case in self.cases))

    def test_required_routing_behaviors(self) -> None:
        by_id = {case["id"]: case["expected"] for case in self.cases}
        expected = {
            "G01": "INITIALIZE_A", "G02": "LOAD_B_ONLY",
            "G03": "NO_CROSS_CORPUS_READ", "G04": "BLOCK_DEEP_ANALYSIS_AND_REWRITE",
            "G05": "AUTO_CONTINUE_DEEP_ANALYSIS", "G06": "SELECT_4_OR_5_DISCUSSION_EXEMPLARS",
            "G07": "SELECT_4_OR_5_RESULTS_EXEMPLARS_MAY_DIFFER_FROM_G06",
            "G08": "SET_REFRESH_REQUIRED", "G09": "SKIP_HEAVY_WORKFLOW",
            "G10": "FALLBACK_TO_AUTHORIZED_PRIMARY_FULLTEXT",
            "G11": "READ_SAME_AUTHORITATIVE_PRIVATE_RECORD_AND_VERSIONS",
            "G12": "DO_NOT_INHERIT_A_SKILL",
            "G13": "KEEP_CURRENT_SKILL_AFTER_IDENTITY_AND_FRESHNESS_CHECK",
            "G14": "SET_REFRESH_REQUIRED_AND_REASSESS",
            "G15": "NEVER_GLOBALIZE_OR_SELECT_REAL_EXEMPLARS",
        }
        self.assertEqual(by_id, expected)

    def test_state_machine_has_all_ten_states_and_approval_guard(self) -> None:
        text = STATE_DOC.read_text(encoding="utf-8")
        for i, state in enumerate(("UNINITIALIZED", "MANUSCRIPT_PROFILED", "CANDIDATE_POOL_READY", "MASTER_20_SELECTED", "CORE_3_PENDING_AUTHOR_APPROVAL", "CORE_3_APPROVED", "CORPUS_DEEP_ANALYSIS_COMPLETE", "PROJECT_EXEMPLAR_SKILL_BUILT", "ACTIVE_FOR_WRITING", "REFRESH_REQUIRED")):
            self.assertIn(f"S{i}_{state}", text)
        self.assertIn("hard gate", text)
        self.assertIn("automatically continue", text.lower())

    def test_workflow_enforces_isolation_and_section_refresh(self) -> None:
        text = WORKFLOW_DOC.read_text(encoding="utf-8")
        for anchor in ("4–5", "OUR_EVIDENCE_MAP", "OUR_ARGUMENT_MAP", "NotebookLM", "S4_CORE_3_PENDING_AUTHOR_APPROVAL", "MASTER_CORPUS_VERSION", "MANUSCRIPT_IDENTITY_UNCERTAIN"):
            self.assertIn(anchor, text)

    def test_templates_and_existing_owner_route_are_present(self) -> None:
        required = (
            "MANUSCRIPT_WRITING_PROFILE_TEMPLATE_V1.yaml",
            "MASTER_EXEMPLAR_CORPUS_TEMPLATE_V1.yaml",
            "CORE3_APPROVAL_TEMPLATE_V1.yaml",
            "SECTION_EXEMPLAR_SELECTION_TEMPLATE_V1.yaml",
            "PROJECT_EXEMPLAR_SKILL_TEMPLATE_V1.md",
        )
        for name in required:
            self.assertTrue((ROOT / "templates" / name).is_file(), name)
        skill = (ROOT / "skills/agent-auto-sci-scicomm/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("per-manuscript exemplar workflow", skill)
        self.assertIn("name: agent-auto-sci-scicomm", skill)


if __name__ == "__main__":
    unittest.main()
