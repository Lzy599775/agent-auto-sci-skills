"""The Codex loader carries the 3.22.2 routing core and description contract."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import shutil

import pytest
import yaml


CODEX_ROOT = Path(__file__).resolve().parents[1]
SUITE_ROOT = CODEX_ROOT.parent
CANONICAL = Path("shared/references/routing_core.md")
BEGIN = "<!-- routing-core:begin -->"
END = "<!-- routing-core:end -->"


def load_gates():
    spec = importlib.util.spec_from_file_location(
        "ars_codex_quality_gates", CODEX_ROOT / "scripts/ars_codex_quality_gates.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def fixture(tmp_path, monkeypatch):
    """Only the two runtime documents: no Claude loader or vendor carriers."""
    gates = load_gates()
    canonical = tmp_path / "ars" / CANONICAL
    canonical.parent.mkdir(parents=True)
    shutil.copyfile(SUITE_ROOT / "SKILL.md", tmp_path / "SKILL.md")
    shutil.copyfile(SUITE_ROOT / "ars" / CANONICAL, canonical)
    monkeypatch.setattr(gates, "SUITE_ROOT", tmp_path)
    monkeypatch.setattr(gates, "ARS_ROOT", tmp_path / "ars")
    return gates, tmp_path / "SKILL.md", canonical


def set_description(path, value):
    text = path.read_text(encoding="utf-8")
    _, _, body = text.split("---", 2)
    frontmatter = yaml.safe_dump({"name": "academic-research-suite", "description": value}, allow_unicode=True)
    path.write_text(f"---\n{frontmatter}---{body}", encoding="utf-8")


def test_shipped_root_router_passes_and_gate_is_registered():
    gates = load_gates()
    assert gates.GATES["root-router"] is gates.check_root_router
    assert len(gates.run_gate("root-router")) == 2


def test_router_gate_needs_no_claude_loader(fixture):
    gates, _, _ = fixture
    assert len(gates.check_root_router()) == 2


@pytest.mark.parametrize("target", ["router", "canonical"])
def test_changed_byte_fails(fixture, target):
    gates, router, canonical = fixture
    path = router if target == "router" else canonical
    text = path.read_text(encoding="utf-8")
    assert "Do NOT auto-route" in text
    path.write_text(text.replace("Do NOT auto-route", "Do not auto-route"), encoding="utf-8")
    with pytest.raises(gates.GateFailure, match="routing-core block differs"):
        gates.check_root_router()


@pytest.mark.parametrize("target", ["router", "canonical"])
@pytest.mark.parametrize("mutation", ["missing", "duplicate", "inline", "reversed", "empty"])
def test_invalid_routing_block_fails(fixture, target, mutation):
    gates, router, canonical = fixture
    path = router if target == "router" else canonical
    text = path.read_text(encoding="utf-8")
    if mutation == "missing":
        text = text.replace(BEGIN, "").replace(END, "")
    elif mutation == "duplicate":
        text += f"\n{BEGIN}\nduplicate\n{END}\n"
    elif mutation == "inline":
        text = text.replace(BEGIN, f"prefix {BEGIN}")
    elif mutation == "reversed":
        text = text.replace(BEGIN, "@@BEGIN@@").replace(END, BEGIN).replace("@@BEGIN@@", END)
    else:
        head, rest = text.split(BEGIN, 1)
        _, tail = rest.split(END, 1)
        text = f"{head}{BEGIN}\n\n{END}{tail}"
    path.write_text(text, encoding="utf-8")
    with pytest.raises(gates.GateFailure, match="routing|root SKILL"):
        gates.check_root_router()


def test_line_ending_drift_fails(fixture):
    gates, router, _ = fixture
    router.write_bytes(router.read_bytes().replace(b"\n", b"\r\n"))
    with pytest.raises(gates.GateFailure, match="routing-core block differs"):
        gates.check_root_router()


def test_matching_crlf_blocks_pass(fixture):
    gates, router, canonical = fixture
    for path in (router, canonical):
        path.write_bytes(path.read_bytes().replace(b"\n", b"\r\n"))
    assert gates.check_root_router()


@pytest.mark.parametrize("target", ["router", "canonical"])
def test_missing_file_fails_visibly(fixture, target):
    gates, router, canonical = fixture
    (router if target == "router" else canonical).unlink()
    with pytest.raises(gates.GateFailure, match="required routing file cannot be read"):
        gates.check_root_router()


@pytest.mark.parametrize("length,valid", [(1023, True), (1024, True), (1025, False)])
def test_description_boundary(fixture, length, valid):
    gates, router, _ = fixture
    set_description(router, "文" * length)
    if valid:
        assert f"{length}/1024" in gates.check_root_router()[1]
    else:
        with pytest.raises(gates.GateFailure, match="description exceeds 1024"):
            gates.check_root_router()


@pytest.mark.parametrize("value", [None, True, 1024, [], {}, "", " \t\n"])
def test_description_missing_wrong_type_or_blank_fails(fixture, value):
    gates, router, _ = fixture
    set_description(router, value)
    with pytest.raises(gates.GateFailure, match="description must"):
        gates.check_root_router()


def test_description_count_does_not_trim(fixture):
    gates, router, _ = fixture
    set_description(router, " " + "x" * 1024)
    with pytest.raises(gates.GateFailure, match="description exceeds 1024"):
        gates.check_root_router()


def test_folded_description_counts_parsed_newline(fixture):
    gates, router, _ = fixture
    _, _, body = router.read_text(encoding="utf-8").split("---", 2)
    router.write_text(f"---\ndescription: >\n  hello\n  world\n---{body}", encoding="utf-8")
    assert "12/1024" in gates.check_root_router()[1]


@pytest.mark.parametrize("frontmatter", ["description: [broken", "- list", "name: no-description"])
def test_invalid_frontmatter_fails(fixture, frontmatter):
    gates, router, _ = fixture
    _, _, body = router.read_text(encoding="utf-8").split("---", 2)
    router.write_text(f"---\n{frontmatter}\n---{body}", encoding="utf-8")
    with pytest.raises(gates.GateFailure, match="frontmatter|description"):
        gates.check_root_router()
