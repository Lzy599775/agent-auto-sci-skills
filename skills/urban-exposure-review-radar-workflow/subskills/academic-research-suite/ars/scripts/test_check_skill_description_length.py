"""Parsed-string boundary and invalid-frontmatter regressions for #864."""
from pathlib import Path

import pytest
import yaml

from scripts.check_skill_description_length import SKILLS, check

REPO = Path(__file__).resolve().parents[1]


@pytest.fixture(params=["upstream", "codex"])
def root(tmp_path, request):
    root = tmp_path / "ars"
    root.mkdir()
    entry = "SKILL.md"
    if request.param == "codex":
        (tmp_path / "manifest.json").write_text('{"generated_for": "codex"}')
        entry = "WORKFLOW.md"
    for name in SKILLS:
        (root / name).mkdir()
        (root / name / entry).write_text('---\ndescription: "Valid"\n---\n')
    return root


def entry_path(root):
    return next((root / "academic-paper").glob("*.md"))


def write(root, frontmatter):
    entry_path(root).write_text(f"---\n{frontmatter}\n---\n", encoding="utf-8")


def test_current_descriptions_pass():
    counts, errors = check(REPO)
    assert errors == []
    assert set(counts) == set(SKILLS)


@pytest.mark.parametrize("length,valid", [(1023, True), (1024, True), (1025, False)])
def test_exact_boundary(root, length, valid):
    write(root, yaml.safe_dump({"description": "x" * length}))
    counts, errors = check(root)
    assert counts["academic-paper"] == length
    assert bool(errors) is not valid


def test_unicode_code_points_not_bytes_or_graphemes(root):
    value = "文é😀e\u0301" * 204 + "中文é😀"
    assert len(value) == 1024
    write(root, yaml.safe_dump({"description": value}, allow_unicode=True))
    counts, errors = check(root)
    assert counts["academic-paper"] == 1024
    assert errors == []


def test_folded_yaml_value_including_trailing_newline(root):
    write(root, "description: >\n  hello\n  world")
    counts, errors = check(root)
    assert counts["academic-paper"] == len("hello world\n")
    assert errors == []


def test_no_trimming_before_counting(root):
    write(root, yaml.safe_dump({"description": " " + "x" * 1024}))
    counts, errors = check(root)
    assert counts["academic-paper"] == 1025
    assert any("exceeds" in error for error in errors)


@pytest.mark.parametrize("value", [None, 1024, True, [], {}, "", " \t\n"])
def test_missing_wrong_type_and_blank_fail(root, value):
    write(root, yaml.safe_dump({"description": value}))
    assert check(root)[1]


@pytest.mark.parametrize("text", ["name: only", "description: [invalid", "- scalar"])
def test_invalid_frontmatter_fails(root, text):
    write(root, text)
    assert check(root)[1]


@pytest.mark.parametrize("text", ["No frontmatter", "---\ndescription: valid\n"])
def test_missing_fence_fails(root, text):
    entry_path(root).write_text(text)
    assert check(root)[1]


def test_missing_skill_does_not_pass_vacuously(root):
    entry_path(root).unlink()
    assert check(root)[1]


def test_wrong_entry_filename_does_not_pass_vacuously(root):
    path = entry_path(root)
    wrong = "SKILL.md" if path.name == "WORKFLOW.md" else "WORKFLOW.md"
    path.rename(path.with_name(wrong))
    assert check(root)[1]
