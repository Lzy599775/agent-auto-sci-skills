from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest


CODEX_ROOT = Path(__file__).resolve().parents[1]
SUITE_ROOT = CODEX_ROOT.parent
PLANNER_PATH = CODEX_ROOT / "scripts" / "ars_codex_full_runtime.py"
GATES_PATH = CODEX_ROOT / "scripts" / "ars_codex_quality_gates.py"
MODEL_TIERING_CHECK = SUITE_ROOT / "ars" / "scripts" / "check_model_tiering.py"


def _load_planner():
    spec = importlib.util.spec_from_file_location("ars_codex_full_runtime", PLANNER_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def _load_gates():
    spec = importlib.util.spec_from_file_location("ars_codex_quality_gates", GATES_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


_CORE_WORKFLOWS = {
    "deep-research",
    "academic-paper",
    "academic-paper-reviewer",
    "academic-pipeline",
}
_EXTERNAL_WORKFLOWS = {"experiment-agent"}
_REQUIRED_WORKFLOWS = _CORE_WORKFLOWS | _EXTERNAL_WORKFLOWS


def _inventory_gate_fixture(
    tmp_path: Path,
    monkeypatch,
    *,
    disk_names: set[str] | None = None,
    router_names: set[str] | None = None,
    runtime_names: set[str] | None = None,
    external_names: set[str] | None = None,
    router_preamble: str = "",
    router_trailer: str = "",
):
    gates = _load_gates()
    suite_root = tmp_path / "academic-research-suite"
    ars_root = suite_root / "ars"
    codex_root = suite_root / "codex"
    ars_root.mkdir(parents=True)
    codex_root.mkdir()

    disk_names = set(_REQUIRED_WORKFLOWS if disk_names is None else disk_names)
    router_names = set(_REQUIRED_WORKFLOWS if router_names is None else router_names)
    runtime_names = set(_REQUIRED_WORKFLOWS if runtime_names is None else runtime_names)
    external_names = set(_EXTERNAL_WORKFLOWS if external_names is None else external_names)

    for name in disk_names:
        entry = ars_root / name / "WORKFLOW.md"
        entry.parent.mkdir()
        entry.write_text(f"# {name}\n", encoding="utf-8")

    router_rows = "\n".join(
        f"| {name} intent | `ars/{name}/WORKFLOW.md` |"
        for name in sorted(router_names)
    )
    (suite_root / "SKILL.md").write_text(
        "# Fixture router\n\n"
        "## Workflow Router\n\n"
        f"{router_preamble}"
        "| User intent | Read first |\n"
        "|---|---|\n"
        f"{router_rows}\n\n"
        f"{router_trailer}"
        "## Next Section\n",
        encoding="utf-8",
    )
    full_runtime_manifest = codex_root / "full-runtime-manifest.json"
    full_runtime_manifest.write_text(
        json.dumps({"workflows": {name: {} for name in sorted(runtime_names)}}),
        encoding="utf-8",
    )
    package_manifest = suite_root / "manifest.json"
    package_manifest.write_text(
        json.dumps(
            {
                "source_repositories": [
                    {
                        "name": "academic-research-skills",
                        "included_paths": sorted(_CORE_WORKFLOWS),
                    },
                    {
                        "name": "external-fixture",
                        "included_paths": sorted(external_names),
                    },
                ]
            }
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(gates, "SUITE_ROOT", suite_root)
    monkeypatch.setattr(gates, "ARS_ROOT", ars_root)
    monkeypatch.setattr(gates, "FULL_RUNTIME_MANIFEST", full_runtime_manifest)
    monkeypatch.setattr(gates, "PACKAGE_MANIFEST", package_manifest)
    return gates


def test_vague_paper_topic_routes_to_deep_research_socratic() -> None:
    planner = _load_planner()
    plan = planner.plan_request(
        "Use $academic-research-suite. I want to write a paper on AI adoption in higher education quality assurance. I do not yet have a clear research question.",
        env={},
    )
    assert plan["workflow"] == "deep-research"
    assert plan["mode"] == "socratic"
    assert plan["route_reason"] == "paper_topic_scoping_override"


def test_explicit_empty_env_never_inherits_process_runtime_flags(monkeypatch) -> None:
    planner = _load_planner()
    monkeypatch.setenv("ARS_CODEX_FULL_RUNTIME", "1")
    monkeypatch.setenv("ARS_CODEX_AGENT_TEAM", "1")
    plan = planner.plan_request("ars-reviewer full review for this manuscript.", env={})
    assert plan["profile"]["agent_team_enabled"] is False
    assert plan["topology_plan"]["arm_id"] == "inline-solo"
    assert plan["agent_team_plan"] == []


def test_vague_topic_with_unclear_research_question_still_routes_to_socratic() -> None:
    planner = _load_planner()
    plan = planner.plan_request(
        "Use $academic-research-suite. I want to write a paper on AI governance in universities, but my research question is still unclear.",
        env={},
    )
    assert plan["workflow"] == "deep-research"
    assert plan["mode"] == "socratic"
    assert plan["route_reason"] == "paper_topic_scoping_override"


def test_ars_plan_routes_to_academic_paper_plan_when_rq_exists() -> None:
    planner = _load_planner()
    plan = planner.plan_request(
        "ars-plan Research question: How do QA agencies evaluate AI governance in universities?",
        env={},
    )
    assert plan["command_alias"] == "ars-plan"
    assert plan["workflow"] == "academic-paper"
    assert plan["mode"] == "plan"
    assert plan["command_recipe"] == "ars/commands/ars-plan.md"


def test_ars_lit_review_alias_routes_to_lit_review_mode() -> None:
    planner = _load_planner()
    plan = planner.plan_request(
        "ars-lit-review Research question: What is known about AI governance in university QA?",
        env={},
    )
    assert plan["workflow"] == "academic-paper"
    assert plan["mode"] == "lit-review"


def test_ars_cache_invalidate_alias_routes_to_pipeline_cache_mode() -> None:
    planner = _load_planner()
    plan = planner.plan_request("ars-cache-invalidate smith2024", env={})
    assert plan["command_alias"] == "ars-cache-invalidate"
    assert plan["workflow"] == "academic-pipeline"
    assert plan["mode"] == "cache-invalidate"
    assert plan["command_recipe"] == "ars/commands/ars-cache-invalidate.md"


def test_ars_3w_alias_routes_to_deep_research_three_way_scan() -> None:
    planner = _load_planner()
    plan = planner.plan_request("ars-3w compare these three papers", env={})
    assert plan["command_alias"] == "ars-3w"
    assert plan["workflow"] == "deep-research"
    assert plan["mode"] == "three-way-scan"
    assert plan["command_recipe"] == "ars/commands/ars-3w.md"


def test_ars_rebuttal_audit_alias_routes_to_academic_paper() -> None:
    planner = _load_planner()
    plan = planner.plan_request("ars-rebuttal-audit check my response draft against these reviewer comments", env={})
    assert plan["command_alias"] == "ars-rebuttal-audit"
    assert plan["workflow"] == "academic-paper"
    assert plan["mode"] == "rebuttal-audit"
    assert plan["command_recipe"] == "ars/commands/ars-rebuttal-audit.md"


def test_korean_revision_routes_to_academic_paper_not_reviewer() -> None:
    planner = _load_planner()
    plan = planner.plan_request(
        "이 논문을 수정해줘. 심사 의견은 아직 없고, 초고를 더 다듬고 싶어.",
        env={},
    )
    assert plan["workflow"] == "academic-paper"
    assert plan["mode"] == "revision"


def test_korean_review_routes_to_reviewer_not_revision() -> None:
    planner = _load_planner()
    plan = planner.plan_request("이 논문을 심사해줘.", env={})
    assert plan["workflow"] == "academic-paper-reviewer"
    assert plan["mode"] == "full"


def test_model_tiering_is_surfaced_without_forcing_a_codex_model() -> None:
    planner = _load_planner()
    inline = planner.plan_request("ars-plan Research question: Why?", env={"ARS_MODEL_TIERING": "economy"})
    assert inline["profile"]["model_tiering_status"] == "inline_noop"

    delegated = planner.plan_request(
        "ars-plan Research question: Why?",
        env={
            "ARS_CODEX_FULL_RUNTIME": "1",
            "ARS_CODEX_AGENT_TEAM": "1",
            "ARS_MODEL_TIERING": "quality-boost",
        },
    )
    assert delegated["profile"]["model_tiering_status"] == "advisory_requires_runtime_model_override"
    assert delegated["profile"]["model_tiering_requested"] == "quality-boost"


def test_command_model_hints_match_upstream_frontmatter_semantics() -> None:
    manifest = json.loads((CODEX_ROOT / "full-runtime-manifest.json").read_text(encoding="utf-8"))
    hints = {
        command["aliases"][1]: command["model_hint"]
        for command in manifest["commands"]
    }

    for alias in ("ars-full", "ars-reviewer", "ars-revision-coach"):
        assert hints.pop(alias) == "inherit"
    assert hints
    assert set(hints.values()) == {"sonnet"}


def test_cross_model_configuration_requires_dispatcher_consent_gate() -> None:
    planner = _load_planner()
    inline = planner.plan_request(
        "ars-reviewer full review for this manuscript.",
        env={"ARS_CROSS_MODEL": "gpt-5.5"},
    )
    assert inline["profile"]["cross_model_configured"] == "gpt-5.5"
    assert inline["profile"]["cross_model_handoff_status"] == (
        "inline_transport_requires_explicit_request_and_consent"
    )

    delegated = planner.plan_request(
        "ars-reviewer full review for this manuscript.",
        env={
            "ARS_CODEX_FULL_RUNTIME": "1",
            "ARS_CODEX_AGENT_TEAM": "1",
            "ARS_CROSS_MODEL": "gpt-5.5",
        },
    )
    assert delegated["profile"]["cross_model_handoff_status"] == (
        "dispatcher_transport_requires_explicit_request_and_consent"
    )
    reviewer_2 = next(
        item
        for item in delegated["agent_team_plan"]
        if item["agent"] == "domain_reviewer_agent"
    )
    assert reviewer_2["cross_model_reviewer_track"] == (
        "configured_requires_explicit_content_consent"
    )


def test_cross_model_transport_selector_surfaces_closed_api_and_unset_states() -> None:
    planner = _load_planner()

    default = planner.plan_request("ars-plan Research question: Why?", env={})
    assert default["profile"]["cross_model_transport_selector"] == "unset"
    assert default["profile"]["cross_model_effective_transport"] == "api"
    assert default["profile"]["cross_model_transport_scope"] == "none"

    api = planner.plan_request(
        "ars-reviewer full review for this manuscript.",
        env={
            "ARS_CROSS_MODEL": "gpt-5.5",
            "ARS_CROSS_MODEL_TRANSPORT": "api",
        },
    )
    assert api["profile"]["cross_model_transport_selector"] == "api"
    assert api["profile"]["cross_model_effective_transport"] == "api"
    assert api["profile"]["cross_model_transport_scope"] == "api_cross_model_workflows"
    assert api["profile"]["cross_model_explicit_consent_required"] is True


def test_codex_transport_is_citation_only_and_excluded_from_reviewer_plan() -> None:
    planner = _load_planner()
    plan = planner.plan_request(
        "ars-reviewer full review for this manuscript.",
        env={
            "ARS_CODEX_FULL_RUNTIME": "1",
            "ARS_CODEX_AGENT_TEAM": "1",
            "ARS_CROSS_MODEL": "gpt-5.6-sol",
            "ARS_CROSS_MODEL_TRANSPORT": "codex",
        },
    )
    profile = plan["profile"]
    assert profile["cross_model_transport_selector"] == "codex"
    assert profile["cross_model_effective_transport"] == "codex"
    assert profile["cross_model_transport_ready"] is True
    assert profile["cross_model_transport_scope"] == "citation_integrity_only"
    assert profile["cross_model_explicit_consent_required"] is True
    assert profile["cross_model_handoff_status"] == (
        "codex_citation_only_requires_explicit_request_and_consent"
    )
    assert set(profile["cross_model_forbidden_uses"]) == {
        "devils_advocate",
        "reviewer_seat",
        "re_review_judge",
        "general_judgment",
    }

    reviewer_2 = next(
        item
        for item in plan["agent_team_plan"]
        if item["agent"] == "domain_reviewer_agent"
    )
    assert reviewer_2["cross_model_reviewer_track"] == (
        "excluded_codex_transport_is_citation_only"
    )
    devil = next(
        item
        for item in plan["agent_team_plan"]
        if item["agent"] == "devils_advocate_reviewer_agent"
    )
    assert "cross_model_reviewer_track" not in devil


def test_codex_transport_without_ars_cross_model_is_visibly_unavailable() -> None:
    planner = _load_planner()
    plan = planner.plan_request(
        "ars-citation-check verify this reference.",
        env={"ARS_CROSS_MODEL_TRANSPORT": "codex"},
    )
    profile = plan["profile"]
    assert profile["cross_model_effective_transport"] == "codex"
    assert profile["cross_model_transport_ready"] is False
    assert profile["cross_model_transport_scope"] == "none"
    assert profile["cross_model_handoff_status"] == (
        "codex_transport_unavailable_missing_ARS_CROSS_MODEL"
    )


def test_invalid_cross_model_transport_selector_fails_closed() -> None:
    planner = _load_planner()
    for invalid_selector in ("openai", "unset"):
        with pytest.raises(
            ValueError,
            match="expected the variable to be absent, or set to api or codex",
        ):
            planner.plan_request(
                "ars-reviewer full review for this manuscript.",
                env={
                    "ARS_CROSS_MODEL": "gpt-5.5",
                    "ARS_CROSS_MODEL_TRANSPORT": invalid_selector,
                },
            )

    result = subprocess.run(
        [sys.executable, str(PLANNER_PATH), "ars-reviewer", "full", "review"],
        env={"ARS_CROSS_MODEL_TRANSPORT": "openai"},
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "refused to fall through" in result.stderr
    assert not result.stdout


def test_v318_cache_controls_are_surfaced_without_changing_gate_semantics() -> None:
    planner = _load_planner()
    default = planner.plan_request("ars-cache-invalidate smith2024", env={})
    assert default["profile"]["cache_stale_advisory_days"] == 30
    assert default["profile"]["cache_revalidation_status"] == "cached_default"

    requested = planner.plan_request(
        "ars-cache-invalidate smith2024",
        env={"ARS_CACHE_STALE_ADVISORY_DAYS": "0", "ARS_CACHE_REVALIDATE": "1"},
    )
    assert requested["profile"]["cache_stale_advisory_days"] == 0
    assert requested["profile"]["cache_revalidation_requested"] is True
    assert requested["profile"]["cache_revalidation_status"] == (
        "live_bibliographic_revalidation_requested"
    )

    malformed = planner.plan_request(
        "ars-cache-invalidate smith2024",
        env={"ARS_CACHE_STALE_ADVISORY_DAYS": "not-a-number"},
    )
    assert malformed["profile"]["cache_stale_advisory_days"] == 30


def test_ars_full_starts_pipeline_and_stops_at_dashboard_checkpoint() -> None:
    planner = _load_planner()
    plan = planner.plan_request(
        "ars-full Research question: How do QA agencies evaluate AI governance? Stop after producing the pipeline dashboard.",
        env={"ARS_CODEX_FULL_RUNTIME": "1", "ARS_CODEX_AGENT_TEAM": "1"},
    )
    assert plan["profile"]["execution_mode"] == "codex_agent_team"
    assert plan["workflow"] == "academic-pipeline"
    assert plan["mode"] == "pipeline"
    assert plan["stop_at_checkpoint"] == "pipeline_dashboard"
    assert [item["agent"] for item in plan["agent_team_plan"]][:2] == [
        "pipeline_orchestrator_agent",
        "state_tracker_agent",
    ]
    topology = plan["topology_plan"]
    assert topology["arm_id"] == "workflow-current"
    integrity = next(node for node in topology["nodes"] if node["id"] == "integrity_verification_agent")
    assert integrity["phase"] == "checkpoint_2_5_or_4_5"


def test_reviewer_full_agent_team_records_field_then_blind_panel_then_synthesis() -> None:
    planner = _load_planner()
    plan = planner.plan_request(
        "ars-reviewer full review for this manuscript.",
        env={"ARS_CODEX_FULL_RUNTIME": "1", "ARS_CODEX_AGENT_TEAM": "1"},
    )
    agents = [item["agent"] for item in plan["agent_team_plan"]]
    assert plan["workflow"] == "academic-paper-reviewer"
    assert plan["mode"] == "full"
    assert "editorial_synthesizer_agent" == agents[-1]
    assert "methodology_reviewer_agent" in agents[:-1]
    assert "devils_advocate_reviewer_agent" in agents[:-1]
    topology = plan["topology_plan"]
    assert topology["arm_id"] == "reviewer-full-seven"
    field = topology["nodes"][0]
    assert field["id"] == "field_analyst_agent"
    assert field["depends_on"] == []
    reviewers = [node for node in topology["nodes"] if node["phase"] == "blind_review"]
    assert len(reviewers) == 5
    assert all(node["depends_on"] == ["field_analyst_agent"] for node in reviewers)
    assert all(not any(value.endswith("_report") for value in node["reads"]) for node in reviewers)
    synth = topology["nodes"][-1]
    assert synth["id"] == "editorial_synthesizer_agent"
    assert set(synth["depends_on"]) == {"field_analyst_agent", *(node["id"] for node in reviewers)}
    assert topology["information_sharing"]["peer_outputs"] == "hidden_until_synthesis"


def test_topology_arm_variable_alone_does_not_enable_experiment() -> None:
    planner = _load_planner()
    plan = planner.plan_request(
        "ars-reviewer full review for this manuscript.",
        env={"ARS_CODEX_TOPOLOGY_ARM": "reviewer-five-panel"},
    )
    assert plan["profile"]["topology_arm_status"] == "ignored_without_experiment_opt_in"
    assert plan["topology_plan"]["arm_id"] == "inline-solo"
    assert plan["agent_team_plan"] == []


def test_explicit_topology_experiment_requires_agent_team_for_non_inline_arm() -> None:
    planner = _load_planner()
    plan = planner.plan_request(
        "ars-reviewer full review for this manuscript.",
        env={
            "ARS_CODEX_TOPOLOGY_EXPERIMENT": "1",
            "ARS_CODEX_TOPOLOGY_ARM": "reviewer-two-plus-synthesis",
        },
    )
    assert plan["topology_plan"]["execution_blocked"] is True
    assert "topology_agent_team_runtime_required" in plan["topology_plan"]["reason_codes"]


def test_explicit_reviewer_two_arm_has_two_blind_roots_and_one_sink() -> None:
    planner = _load_planner()
    plan = planner.plan_request(
        "ars-reviewer full review for this manuscript.",
        env={
            "ARS_CODEX_FULL_RUNTIME": "1",
            "ARS_CODEX_AGENT_TEAM": "1",
            "ARS_CODEX_TOPOLOGY_EXPERIMENT": "1",
            "ARS_CODEX_TOPOLOGY_ARM": "reviewer-two-plus-synthesis",
        },
    )
    topology = plan["topology_plan"]
    assert topology["execution_blocked"] is False
    assert [node["id"] for node in topology["nodes"]] == [
        "methodology_reviewer_agent",
        "domain_reviewer_agent",
        "editorial_synthesizer_agent",
    ]
    assert len(topology["edges"]) == 2
    assert all(edge["to"] == "editorial_synthesizer_agent" for edge in topology["edges"])
    assert {tuple(edge["artifacts"]) for edge in topology["edges"]} == {
        ("methodology_reviewer_agent_report",),
        ("domain_reviewer_agent_report",),
    }


def test_cli_outputs_json_plan() -> None:
    result = subprocess.run(
        [sys.executable, str(PLANNER_PATH), "ars-reviewer", "full", "review"],
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(result.stdout)
    assert payload["workflow"] == "academic-paper-reviewer"
    assert payload["mode"] == "full"


def test_v320_manifest_registers_only_hermetic_runtime_contract_gates() -> None:
    manifest = json.loads((CODEX_ROOT / "full-runtime-manifest.json").read_text(encoding="utf-8"))
    options = manifest["runtime_options"]
    transport = options["cross_model_transport"]
    assert transport["allowed_values"] == ["api", "codex"]
    assert transport["variable_may_be_absent"] is True
    assert transport["normalized_absent_label"] == "unset"
    assert transport["codex_scope"] == "citation_integrity_only"
    assert transport["codex_requires_explicit_consent"] is True
    assert transport["codex_requires_ars_cross_model"] is True
    assert transport["codex_min_cli_version"] == "0.147.0"
    assert transport["codex_login_attestation"] == "Logged in using ChatGPT"
    assert set(transport["codex_forbidden_uses"]) >= {
        "devils_advocate",
        "reviewer_seat",
        "re_review_judge",
        "general_judgment",
    }

    pdf = options["pdf_content_classifier"]
    assert pdf["mode"] == "optional_advisory"
    assert pdf["auto_install"] is False
    assert pdf["verdict_scope"] == "STRUCTURE_ONLY"
    assert (SUITE_ROOT / pdf["dependency_file"]).is_file()

    gates = {
        gate["id"]: gate
        for gate in manifest["quality_gates"]
        if gate["id"].startswith("v320_")
    }
    required = {
        "v320_codex_subscription_transport_contract",
        "v320_codex_subscription_transport_runtime",
        "v320_pdf_content_classifier_isolation",
        "v320_phase_e_evidence_rows",
        "v320_revision_roadmap_author_adjudication",
        "v320_post_terminal_adjudication_activity",
        "v320_human_subjects_authority",
        "v320_review_pathway_rule_trace",
        "v320_submission_packet_manifest",
        "v320_human_subjects_reference_migration",
        "v320_human_subjects_content_coverage",
        "v320_bibliographic_integrity_signals",
        "v320_retraction_status",
        "v320_tortured_phrase_advisory",
        "v320_preregistration_cross_document_advisory",
        "v320_review_target_context",
        "v320_review_criteria_binding",
        "v320_committee_correspondence",
    }
    assert required == set(gates)
    for gate in gates.values():
        assert gate["execution"] == "hermetic"
        runner = gate["runner"].removeprefix("upstream:")
        assert (SUITE_ROOT / runner).is_file(), runner

    all_runners = "\n".join(gate["runner"] for gate in manifest["quality_gates"])
    assert "cross_model_smoke_test_codex.sh" not in all_runners
    assert "run_review_criteria_constructive_value.py" not in all_runners


def test_v3211_manifest_registers_bounded_hermetic_contracts() -> None:
    manifest = json.loads(
        (CODEX_ROOT / "full-runtime-manifest.json").read_text(encoding="utf-8")
    )
    options = manifest["runtime_options"]

    transport = options["cross_model_transport"]
    assert transport["codex_login_attestation_streams"] == ["stdout", "stderr"]
    assert transport["codex_provider_schema_omits_unique_items"] is True
    assert transport["codex_local_duplicate_source_refusal"] is True
    assert transport["codex_code_mode_disabled"] is True
    assert transport["codex_search_host_available"] is True

    profile = options["research_workflow_profile"]
    assert profile["mode"] == "default_off_deterministic_substrate"
    assert profile["activation"] == "explicit_selection_or_direct_invocation"
    assert profile["manuscript_inference"] is False
    assert profile["pipeline_hook"] is False
    assert profile["behavioral_evidence"] == "NOT_RUN"
    assert (SUITE_ROOT / profile["fallback_profile"]).is_file()

    ledger = options["inquiry_branch_ledger"]
    assert ledger["environment"] == "ARS_INQUIRY_LEDGER"
    assert ledger["enabled_value"] == "1"
    assert ledger["default_enabled"] is False
    assert ledger["execution"] == "local_offline"
    assert ledger["publication_threshold"] == "second_branch"
    assert ledger["external_call_authority"] is False
    assert ledger["outcome_claims"] == "none"

    gates = {
        gate["id"]: gate
        for gate in manifest["quality_gates"]
        if gate["id"].startswith("v3211_")
    }
    required = {
        "v3211_research_workflow_profile",
        "v3211_inquiry_branch_ledger",
        "v3211_data_access_level",
        "v3211_review_criteria_source_proving_set",
        "v3211_promotion_bakeoff_preregistration_contract",
    }
    assert required == set(gates)
    for gate in gates.values():
        assert gate["execution"] == "hermetic"

    for gate in manifest["quality_gates"]:
        runner = gate["runner"]
        if runner.startswith("upstream:"):
            assert (SUITE_ROOT / runner.removeprefix("upstream:")).is_file(), runner

    active_runners = {gate["runner"] for gate in manifest["quality_gates"]}
    assert (
        "upstream:ars/scripts/check_promotion_bakeoff_preregistration.py"
        not in active_runners
    )
    assert not any("cross_model_smoke_test_codex.sh" in runner for runner in active_runners)
    assert not any("run_review_criteria_constructive_value.py" in runner for runner in active_runners)
    assert not any("run_fleet.py" in runner for runner in active_runners)
    assert not any("alternative_explanation_register" in runner for runner in active_runners)

    package = json.loads((SUITE_ROOT / "manifest.json").read_text(encoding="utf-8"))
    inactive_paths = {item["path"] for item in package["inactive_upstream_scripts"]}
    assert (
        "skills/academic-research-suite/ars/scripts/check_promotion_bakeoff_preregistration.py"
        in inactive_paths
    )


def test_quality_gates_all_pass() -> None:
    result = subprocess.run(
        [sys.executable, str(GATES_PATH), "all", "--json"],
        cwd=SUITE_ROOT.parents[1],
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(result.stdout)
    assert all(item["ok"] for item in payload.values()), payload


def test_single_root_inventory_matches_all_codex_surfaces(
    tmp_path: Path, monkeypatch
) -> None:
    gates = _inventory_gate_fixture(tmp_path, monkeypatch)
    messages = gates.check_single_root_skill()
    assert any("4 core workflows match" in message for message in messages)
    assert any("1 separately sourced workflow" in message for message in messages)


@pytest.mark.parametrize(
    ("mutated_surface", "error_pattern"),
    [
        ("disk", r"core workflow inventory mismatch for root_router"),
        ("router", r"root router lists workflows without WORKFLOW\.md on disk"),
        (
            "runtime",
            r"full-runtime manifest lists workflows without WORKFLOW\.md on disk",
        ),
    ],
)
def test_single_root_inventory_rejects_unpaired_workflow_mutations(
    tmp_path: Path,
    monkeypatch,
    mutated_surface: str,
    error_pattern: str,
) -> None:
    names = {
        "disk": set(_REQUIRED_WORKFLOWS),
        "router": set(_REQUIRED_WORKFLOWS),
        "runtime": set(_REQUIRED_WORKFLOWS),
    }
    names[mutated_surface].add("unrouted-workflow")
    gates = _inventory_gate_fixture(
        tmp_path,
        monkeypatch,
        disk_names=names["disk"],
        router_names=names["router"],
        runtime_names=names["runtime"],
    )
    with pytest.raises(
        gates.GateFailure,
        match=error_pattern,
    ):
        gates.check_single_root_skill()


def test_single_root_inventory_allows_separately_sourced_trace_workflow(
    tmp_path: Path, monkeypatch
) -> None:
    gates = _inventory_gate_fixture(
        tmp_path,
        monkeypatch,
        disk_names=_REQUIRED_WORKFLOWS | {"trace-addon"},
        external_names=_EXTERNAL_WORKFLOWS | {"trace-addon"},
    )
    messages = gates.check_single_root_skill()
    assert any("4 core workflows match" in message for message in messages)
    assert any("2 separately sourced workflow" in message for message in messages)


@pytest.mark.parametrize("mutated_surface", ["router", "runtime"])
def test_single_root_inventory_rejects_dangling_external_routes(
    tmp_path: Path, monkeypatch, mutated_surface: str
) -> None:
    names = {
        "router": set(_REQUIRED_WORKFLOWS),
        "runtime": set(_REQUIRED_WORKFLOWS),
    }
    names[mutated_surface].add("trace-addon")
    gates = _inventory_gate_fixture(
        tmp_path,
        monkeypatch,
        router_names=names["router"],
        runtime_names=names["runtime"],
        external_names=_EXTERNAL_WORKFLOWS | {"trace-addon"},
    )
    with pytest.raises(
        gates.GateFailure,
        match=r"lists workflows without WORKFLOW\.md on disk: \['trace-addon'\]",
    ):
        gates.check_single_root_skill()


@pytest.mark.parametrize("mutated_surface", ["router", "runtime"])
def test_single_root_inventory_rejects_partially_advertised_external_workflow(
    tmp_path: Path, monkeypatch, mutated_surface: str
) -> None:
    names = {
        "router": set(_REQUIRED_WORKFLOWS),
        "runtime": set(_REQUIRED_WORKFLOWS),
    }
    names[mutated_surface].add("trace-addon")
    gates = _inventory_gate_fixture(
        tmp_path,
        monkeypatch,
        disk_names=_REQUIRED_WORKFLOWS | {"trace-addon"},
        router_names=names["router"],
        runtime_names=names["runtime"],
        external_names=_EXTERNAL_WORKFLOWS | {"trace-addon"},
    )
    with pytest.raises(
        gates.GateFailure,
        match=r"separately sourced workflow inventory mismatch",
    ):
        gates.check_single_root_skill()


def test_secondary_source_overlap_does_not_exclude_core_workflow(
    tmp_path: Path, monkeypatch
) -> None:
    gates = _inventory_gate_fixture(
        tmp_path,
        monkeypatch,
        external_names=_EXTERNAL_WORKFLOWS | {"academic-paper"},
    )
    package = json.loads(gates.PACKAGE_MANIFEST.read_text(encoding="utf-8"))
    assert gates._external_workflow_names(package) == _EXTERNAL_WORKFLOWS


def test_incidental_table_does_not_count_as_root_router_enumeration(
    tmp_path: Path, monkeypatch
) -> None:
    gates = _inventory_gate_fixture(
        tmp_path,
        monkeypatch,
        disk_names=_REQUIRED_WORKFLOWS | {"unrouted-workflow"},
        router_trailer=(
            "### Incidental comparison\n\n"
            "| Note | Example |\n"
            "|---|---|\n"
            "| Not a route | `ars/unrouted-workflow/WORKFLOW.md` |\n\n"
        ),
    )
    with pytest.raises(
        gates.GateFailure,
        match=r"missing_from_root_router=\['unrouted-workflow'\]",
    ):
        gates.check_single_root_skill()


def test_incidental_table_before_router_table_is_rejected(
    tmp_path: Path, monkeypatch
) -> None:
    gates = _inventory_gate_fixture(
        tmp_path,
        monkeypatch,
        router_preamble=(
            "| Note | Example |\n"
            "|---|---|\n"
            "| Not a route | `ars/deep-research/WORKFLOW.md` |\n\n"
        ),
    )
    with pytest.raises(
        gates.GateFailure,
        match=r"table headers must include exactly one 'User intent' and 'Read first'",
    ):
        gates.check_single_root_skill()


def test_route_like_path_outside_read_first_column_is_rejected(
    tmp_path: Path, monkeypatch
) -> None:
    gates = _inventory_gate_fixture(tmp_path, monkeypatch)
    root_skill = gates.SUITE_ROOT / "SKILL.md"
    text = root_skill.read_text(encoding="utf-8")
    text = text.replace(
        "| academic-paper intent | `ars/academic-paper/WORKFLOW.md` |",
        "| `ars/academic-paper/WORKFLOW.md` | Not a route |",
    )
    root_skill.write_text(text, encoding="utf-8")
    with pytest.raises(
        gates.GateFailure,
        match=r"Read first cell must contain exactly one",
    ):
        gates.check_single_root_skill()


def test_model_tiering_lint_accepts_separately_vendored_experiment_agents() -> None:
    result = subprocess.run(
        [sys.executable, str(MODEL_TIERING_CHECK)],
        cwd=SUITE_ROOT / "ars",
        check=True,
        capture_output=True,
        text=True,
    )
    assert "39 agents classified" in result.stdout
