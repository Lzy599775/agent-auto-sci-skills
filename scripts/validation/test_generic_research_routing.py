"""Synthetic generic decision/isolation tests. No client activation claims."""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import unittest

import validate_generic_research_routing as V


class CrossDomainRoutingTests(unittest.TestCase):
    def test_structural_parity_and_mirrors(self):
        self.assertEqual([], V.validate_contract())

    def test_fixture_scope_and_paraphrase_inputs(self):
        payload = json.loads((V.ROOT / V.GOLDEN).read_text(encoding="utf-8"))
        self.assertEqual("SYNTHETIC_ONLY_NO_PRIVATE_DATA", payload["fixture_policy"])
        self.assertEqual(list("ABCDEFGHIJKLM"), [c["id"] for c in payload["cases"]])
        for case in payload["cases"]:
            self.assertTrue(case["paraphrases"])
            self.assertNotEqual(case["TASK_INPUT"], case["paraphrases"][0])

    def test_near_neighbor_deliverable_boundaries(self):
        cases = json.loads((V.ROOT / V.GOLDEN).read_text(encoding="utf-8"))["cases"]
        for case in cases:
            with self.subTest(case=case["id"]):
                neighbor = case["near_neighbor"]
                actual = V.resolve_contract(neighbor["INTERPRETED_INTENT"])
                self.assertEqual(neighbor["EXPECTED_PRIMARY_ROUTE"], actual["primary_route"])
                original = V.resolve_contract(case["INTERPRETED_INTENT"])
                self.assertNotEqual(
                    (original["primary_route"], original["mode"], original["private_state"]),
                    (actual["primary_route"], actual["mode"], actual["private_state"]),
                )
                # Micro-edits vs substantial writing and preflight vs execution
                # intentionally share a primary owner but require different modes/gates.

    def test_unknown_intent_not_guessed_from_keywords(self):
        for raw in ("Methods causal forest green exposure", "PROJECT_A", "", "unclear"):
            with self.assertRaisesRegex(ValueError, "INTENT_NOT_VERIFIED"):
                V.resolve_contract(raw)

    def test_existing_literature_and_citation_routes(self):
        literature = V.resolve_contract("literature_synthesis")
        self.assertEqual("literature_review", literature["primary_route"])
        self.assertIn("PAPER_ARTIFACT_AVAILABILITY_PROTOCOL_V1", literature["companions"])
        self.assertEqual("citation_claim_audit", V.resolve_contract("citation_support")["primary_route"])

    def test_preflight_never_starts_computation(self):
        rule = V.resolve_contract("resource_preflight")
        self.assertEqual("preflight_only", rule["mode"])
        self.assertEqual("none", rule["private_state"])


def _golden_test(case):
    def test(self):
        actual = V.resolve_contract(case["INTERPRETED_INTENT"])
        self.assertEqual(case["EXPECTED_PRIMARY_ROUTE"], actual["primary_route"])
        self.assertEqual(case["EXPECTED_COMPANION"], actual["companions"])
        self.assertEqual(case["EXPECTED_SPECIALIST_SKILL"], actual["specialist"])
    return test


for _case in json.loads((V.ROOT / V.GOLDEN).read_text(encoding="utf-8"))["cases"]:
    setattr(CrossDomainRoutingTests, f"test_golden_{_case['id']}", _golden_test(_case))


class CrossProjectIsolationTests(unittest.TestCase):
    def setUp(self):
        payload = json.loads((V.ROOT / V.STATE_FIXTURE).read_text(encoding="utf-8"))
        self.states = {payload[key]["MANUSCRIPT_ID"]: payload[key] for key in ("PROJECT_A", "PROJECT_B")}
        self.original = deepcopy(self.states)
        self.reads = []

    def reader(self, manuscript_id):
        self.reads.append(manuscript_id)
        return self.states[manuscript_id]

    def decide(self, intent="substantive_writing", manuscript_id=None):
        return V.evaluate_synthetic_state_access(intent, manuscript_id, self.reader)

    def test_01_project_a_reads_only_a(self):
        result = self.decide(manuscript_id="SYNTHETIC_A")
        self.assertEqual(["SYNTHETIC_A"], self.reads)
        self.assertEqual(self.states["SYNTHETIC_A"], result["state"])
        self.assertEqual("ALLOW_SUBSTANTIVE_WRITING", result["gate"])

    def test_02_switch_to_b_reads_only_b_and_does_not_inherit_a(self):
        self.decide(manuscript_id="SYNTHETIC_A")
        self.reads.clear()
        result = self.decide(manuscript_id="SYNTHETIC_B")
        self.assertEqual(["SYNTHETIC_B"], self.reads)
        for key in ("MANUSCRIPT_ID", "RESEARCH_QUESTION", "PROJECT_STATE", "MASTER20_VERSION",
                    "CORE3_VERSION", "DATA_SOURCE", "RESULTS_LEDGER"):
            self.assertNotEqual(self.states["SYNTHETIC_A"][key], result["state"][key])
        result["state"]["RESULTS_LEDGER"].append("temporary mutation")
        self.assertEqual(self.original, self.states)

    def test_03_missing_identity_never_inherits_previous_project(self):
        self.decide(manuscript_id="SYNTHETIC_A")
        self.reads.clear()
        result = self.decide()
        self.assertEqual("MANUSCRIPT_IDENTITY_UNCERTAIN", result["gate"])
        self.assertIsNone(result["state"])
        self.assertEqual([], self.reads)

    def test_04_method_consultation_reads_no_manuscript_state(self):
        for intent in ("causal_identification", "model_suitability", "statistical_design", "bias_appraisal"):
            self.assertIsNone(self.decide(intent, "SYNTHETIC_A")["state"])
        self.assertEqual([], self.reads)

    def test_05_micro_edit_has_no_private_state_or_corpus_initialization(self):
        result = self.decide("language_micro_edit", "SYNTHETIC_B")
        self.assertEqual("lightweight", result["mode"])
        self.assertEqual([], result["companions"])
        self.assertIsNone(result["state"])
        self.assertEqual([], self.reads)

    def test_06_substantive_writing_requires_matching_identity(self):
        result = V.evaluate_synthetic_state_access("substantive_writing", "SYNTHETIC_B",
                                                   lambda _: self.states["SYNTHETIC_A"])
        self.assertEqual("STATE_IDENTITY_CONFLICT", result["gate"])
        self.assertIsNone(result["state"])
        unknown = self.decide(manuscript_id="SYNTHETIC_UNKNOWN")
        self.assertEqual("STATE_NOT_VERIFIED", unknown["gate"])

    def test_07_core3_approval_boundary(self):
        result = self.decide(manuscript_id="SYNTHETIC_B")
        self.assertEqual("BLOCK_PENDING_CORE3_APPROVAL", result["gate"])
        self.assertEqual(self.original, self.states)
        self.states["SYNTHETIC_B"]["CORE3_APPROVED"] = "true"
        self.assertEqual("BLOCK_PENDING_CORE3_APPROVAL", self.decide(manuscript_id="SYNTHETIC_B")["gate"])
        self.states["SYNTHETIC_B"]["CORE3_APPROVED"] = True
        self.assertEqual("STATE_REFRESH_OR_INITIALIZATION_REQUIRED", self.decide(manuscript_id="SYNTHETIC_B")["gate"])

    def test_08_artifact_search_authorizes_no_zotero_write(self):
        result = self.decide("artifact_identity", "SYNTHETIC_A")
        self.assertIs(result["zotero_write_authorized"], False)
        self.assertEqual([], self.reads)
        self.assertIsNone(result["state"])


if __name__ == "__main__":
    unittest.main()
