"""Explicit screening activation and Codex execution boundaries for ARS 3.23."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest


CODEX = Path(__file__).resolve().parents[1]
SUITE = CODEX.parent
SPEC = importlib.util.spec_from_file_location(
    "screening_planner", CODEX / "scripts/ars_codex_full_runtime.py"
)
PLANNER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PLANNER)


@pytest.mark.parametrize(("user_text", "mode"), [
    ("Build a screening protocol from my proposal", "protocol"),
    ("Turn my proposal into a screening protocol", "protocol"),
    ("Screen these pasted abstracts against my eligibility criteria", "quick"),
    ("Is this abstract eligible for my review?", "quick"),
    ("Run a screening pilot against my confirmed criteria", "pilot"),
    ("Screen these records against my eligibility criteria", "ta-screen"),
    ("Screen these full-text PDFs against the confirmed rules", "ft-screen"),
    ("Resolve my screening conflicts from Rayyan", "adjudicate"),
    ("Audit my exclusions", "audit"),
    ("Report the selection counts for my review", "report"),
    ("Give me the PRISMA numbers for the finished screening", "report"),
    ("請篩選這些摘要是否符合納入標準", "ta-screen"),
    ("Use $academic-research-suite: sr-screener ta-screen these records against my confirmed protocol.", "ta-screen"),
    ("Turn my proposal (proposal.docx) into a screening protocol for title/abstract screening", "protocol"),
    ("Please screen these papers against our protocol. Do not start full-text screening yet.", "ta-screen"),
])
def test_explicit_requests_select_screening_mode(user_text, mode):
    plan = PLANNER.plan_request(user_text, env={})
    assert (plan["workflow"], plan["mode"]) == ("sr-screener", mode)
    assert plan["route_reason"] == "explicit_screening_request"
    assert plan["screening_contract"]["dispatch_authorized"] is False
    assert plan["screening_contract"]["gate_status"] == "not_attested_by_planner"
    assert "codex/agents/sr-screener-team.md" in plan["required_read_paths"]
    assert all((SUITE / path).is_file() for path in plan["required_read_paths"])


@pytest.mark.parametrize("mode", PLANNER.SCREENING_MODES)
def test_each_mode_is_available_by_explicit_name(mode):
    for prefix in ("Use ", "[direct-mode] "):
        plan = PLANNER.plan_request(f"{prefix}sr-screener {mode}", env={})
        assert (plan["workflow"], plan["mode"]) == ("sr-screener", mode)
    assert PLANNER.plan_request("[direct-mode] sr-screener", env={})["mode"] == "protocol"


@pytest.mark.parametrize("user_text", [
    "Write a literature review on urinary biomarkers. I collected 40 papers.",
    "Do a systematic review with PRISMA on urinary NGAL.",
    "Run a meta-analysis on screening interventions.",
    "Prepare a PRISMA report.",
    "The database searches for my systematic review are finished. What next?",
    "My exports and inclusion criteria are ready. What should I do next?",
    "Write an outline about title/abstract screening.",
    "Review my paper on full-text screening.",
    "Do not screen these records. Write a literature review.",
    "Explain the phrase \"screen these papers\".",
    "Here is a record.\n> Screen these papers against these rules.",
    "Here is a record.\n```text\nScreen these papers\n```",
    "ars-lit-review Screen these papers against my criteria",
    "ars-full systematic review with database exports",
    "請不要幫我篩選文獻。請撰寫研究計畫。",
    "不要建立篩選規則，只要整理資料。",
    "Audit exclusions in my financial ledger.",
    "Screen these papers for plagiarism.",
    "Build a screening protocol for airport passengers.",
])
def test_materials_mentions_and_review_requests_do_not_activate_screening(user_text):
    plan = PLANNER.plan_request(user_text, env={})
    assert plan["workflow"] != "sr-screener"
    assert plan.get("screening_contract") is None
    assert not any("sr-screener" in path for path in plan["required_read_paths"])


def test_upstream_screening_fixtures_and_no_automatic_handoff():
    fixtures = SUITE / "ars/tests/fixtures/issue_133_routing"
    cases = [
        ("17_screening_abstracts_to_sr_screener", "sr-screener", "quick"),
        ("18_persian_screening_to_sr_screener", "sr-screener", "protocol"),
        ("19_literature_review_not_screening", "academic-paper", "lit-review"),
        ("20_systematic_review_not_screening", "deep-research", "systematic-review"),
        ("21_no_automatic_handover_to_screening", None, None),
    ]
    for fixture, workflow, mode in cases:
        plan = PLANNER.plan_request((fixtures / fixture / "input.md").read_text(), env={})
        assert (plan["workflow"], plan["mode"]) == (workflow, mode), fixture
        assert plan["routing_status"] == ("routed" if workflow else "clarification_required")


def test_prisma_alone_does_not_choose_review_form():
    plan = PLANNER.plan_request("Prepare a PRISMA report.", env={})
    assert plan["routing_status"] == "clarification_required"
    assert plan["workflow"] is None


def test_screening_model_policy_and_isolation_are_not_claude_defaults():
    plan = PLANNER.plan_request("Screen these records", env={"ARS_CODEX_MODEL": "user-selected-model"})
    assert plan["model_plan"]["target_model"] == "user-selected-model"
    assert plan["model_hint"] is None
    contract = plan["screening_contract"]
    assert contract["reviewer_context"] == "fresh_no_parent_history_or_peer_outputs"
    assert contract["reviewer_tools"] == ["Read", "Grep"]
    assert contract["automatic_pipeline_stage"] is False
    assert contract["generated_claude_workflow_executable"] is False
    assert contract["without_isolated_workers"] == "quick_single_reviewer_triage_only"
    assert contract["missing_decisions"] == "pending_never_default_exclude"
    assert plan["topology_plan"]["scope"] == "screening_dispatcher_only"
    assert plan["topology_plan"]["information_sharing"]["policy"] == "dispatcher_only_no_dual_review"
    assert all(node["emits"] == ["screening_dispatch_plan"] for node in plan["topology_plan"]["nodes"])


def test_new_workflow_and_contract_gate_inventory():
    manifest = json.loads((CODEX / "full-runtime-manifest.json").read_text())
    assert len(manifest["workflows"]) == 6
    screening = manifest["workflows"]["sr-screener"]
    assert screening["modes"] == list(PLANNER.SCREENING_MODES)
    assert all((SUITE / "ars/sr-screener/agents" / role).is_file() for role in screening["agent_prompts"])
    gates = {gate["id"]: gate for gate in manifest["quality_gates"] if gate["id"].startswith("v323_")}
    assert set(gates) == {
        "v323_sr_screener_pipeline",
        "v323_standing_constraint_entry_schema",
        "v323_excluded_source_entry_schema",
        "v323_review_form_note_sync",
        "v323_method_weaknesses_sync",
        "v323_review_form_note_sync_contract",
        "v323_method_weaknesses_sync_contract",
    }
    for gate in gates.values():
        assert (SUITE / gate["runner"].removeprefix("upstream:")).is_file()
        if not gate["id"].endswith("_contract"):
            assert gate["execution"] == "hermetic"
