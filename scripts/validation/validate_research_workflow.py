from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]

REQUIRED_FILES = [
    "AGENTS.md",
    "ARCHITECTURE.md",
    "docs/index.md",
    "docs/research/research_principles.md",
    "docs/research/source_hierarchy.md",
    "docs/research/external_sources.md",
    "docs/research/uncertainty_policy.md",
    "docs/workflows/index.md",
    "docs/workflows/literature_review.md",
    "docs/workflows/paper_reproduction.md",
    "docs/workflows/data_analysis.md",
    "docs/workflows/manuscript_writing.md",
    "docs/workflows/citation_claim_audit.md",
    "docs/workflows/figure_workflow.md",
    "docs/workflows/research_idea_evaluation.md",
    "docs/standards/evidence_trace.md",
    "docs/standards/academic_claims.md",
    "docs/standards/data_provenance.md",
    "docs/standards/reproducibility.md",
    "docs/standards/git_policy.md",
    "docs/standards/file_integrity.md",
    "docs/decisions/index.md",
    "research-vault/README.md",
    "templates/paper_note.md",
    "templates/evidence_record.md",
    "templates/dataset_record.md",
    "templates/method_record.md",
    "templates/research_question.md",
    "templates/reproduction_plan.md",
    "templates/decision_record.md",
    "templates/project_bootstrap/AGENTS.md",
    "skills/literature/SKILL.md",
    "skills/literature/agents/openai.yaml",
    "skills/literature/references/contracts.md",
    "skills/literature/references/zotero-integration.md",
    "skills/literature/references/failure-and-qc.md",
    "skills/literature/tests/activation_cases.md",
    "evals/literature/README.md",
]

TEMPLATE_FIELDS = {
    "templates/paper_note.md": [
        "paper_id",
        "zotero_item_key",
        "citation_key",
        "research_question",
        "methods",
        "main_results",
        "evidence_records",
        "review_status",
    ],
    "templates/evidence_record.md": [
        "claim_id",
        "claim_text",
        "source_id",
        "source_location",
        "support_type",
        "confidence",
        "reviewer_status",
    ],
    "templates/dataset_record.md": [
        "dataset_name",
        "provider",
        "official_url",
        "version",
        "license",
        "raw_path",
        "processed_path",
        "processing_script",
        "known_limitations",
    ],
    "templates/reproduction_plan.md": [
        "reproduction_type",
        "required_inputs",
        "substitutions",
        "validation_criteria",
        "difference_attribution_categories",
    ],
}

LINK_ROOTS = [
    ROOT / "AGENTS.md",
    ROOT / "ARCHITECTURE.md",
    ROOT / "README.md",
    ROOT / "docs",
    ROOT / "research-vault",
    ROOT / "templates",
    ROOT / "skills" / "literature",
    ROOT / "evals" / "literature",
]

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_required_files(errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")


def check_agents(errors: list[str]) -> None:
    path = ROOT / "AGENTS.md"
    if not path.is_file():
        return
    lines = read_text(path).splitlines()
    if not 80 <= len(lines) <= 150:
        errors.append(f"AGENTS.md must be 80-150 lines; found {len(lines)}")


def markdown_files() -> list[Path]:
    files: set[Path] = set()
    for entry in LINK_ROOTS:
        if entry.is_file():
            files.add(entry)
        elif entry.is_dir():
            files.update(entry.rglob("*.md"))
    return sorted(files)


def check_links(errors: list[str]) -> None:
    for path in markdown_files():
        for raw_target in LINK_RE.findall(read_text(path)):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = unquote(target.split("#", 1)[0])
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                errors.append(
                    f"broken relative link: {path.relative_to(ROOT)} -> {raw_target}"
                )


def check_templates(errors: list[str]) -> None:
    for relative, fields in TEMPLATE_FIELDS.items():
        path = ROOT / relative
        if not path.is_file():
            continue
        text = read_text(path)
        for field in fields:
            if field not in text:
                errors.append(f"template field missing: {relative}: {field}")


def check_skill(errors: list[str]) -> None:
    path = ROOT / "skills" / "literature" / "SKILL.md"
    if not path.is_file():
        return
    text = read_text(path)
    if not text.startswith("---\n"):
        errors.append("skills/literature/SKILL.md lacks YAML frontmatter")
        return
    parts = text.split("---", 2)
    if len(parts) < 3:
        errors.append("skills/literature/SKILL.md frontmatter is not closed")
        return
    keys = []
    values: dict[str, str] = {}
    for line in parts[1].splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"invalid skill frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        keys.append(key)
        values[key] = value.strip()
    if set(keys) != {"name", "description"}:
        errors.append(f"skill frontmatter keys must be name and description; found {keys}")
    if values.get("name") != "literature":
        errors.append("literature skill name does not match its folder")
    if not values.get("description") or "TODO" in values.get("description", ""):
        errors.append("literature skill description is missing or incomplete")


def check_placeholders(errors: list[str]) -> None:
    for path in markdown_files():
        if "[TODO" in read_text(path):
            errors.append(f"unresolved TODO placeholder: {path.relative_to(ROOT)}")


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    check_agents(errors)
    check_links(errors)
    check_templates(errors)
    check_skill(errors)
    check_placeholders(errors)

    if errors:
        print("Research workflow validation: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Research workflow validation: PASS")
    print(f"- required files: {len(REQUIRED_FILES)}")
    print(f"- markdown files checked: {len(markdown_files())}")
    print(f"- AGENTS.md lines: {len(read_text(ROOT / 'AGENTS.md').splitlines())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
