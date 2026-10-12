"""Ensure the synthetic Codex and ChatGPT Web routing set stays in parity."""
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GOLDEN = ROOT / "evals/academic-writing-exemplar/CROSS_CLIENT_ROUTING_GOLDEN_SET_V1.json"


def test_five_natural_language_cases_have_equal_expected_routes():
    cases = json.loads(GOLDEN.read_text(encoding="utf-8"))["cases"]
    assert len(cases) == 5
    assert len({case["id"] for case in cases}) == 5
    assert all(case["input"] and case["expected_route"] for case in cases)
    assert all(case["codex_expected"] and case["chatgpt_web_expected"] for case in cases)
    assert all(case["codex_expected"] == case["chatgpt_web_expected"] for case in cases)


def test_existing_owner_is_not_duplicated_by_router():
    router = (ROOT / "docs/chatgpt/CHATGPT_PROJECT_RESEARCH_OS_ROUTER_V1.md").read_text(encoding="utf-8")
    assert "agent-auto-sci-scicomm" in router
    assert "not an additional global writing owner" in (
        ROOT / "docs/workflows/manuscript_writing.md"
    ).read_text(encoding="utf-8")
    golden = json.loads(GOLDEN.read_text(encoding="utf-8"))
    assert "NotebookLM optional" in golden["cases"][3]["codex_expected"]
