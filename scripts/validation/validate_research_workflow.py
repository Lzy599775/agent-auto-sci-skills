from __future__ import annotations

import json
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
    "docs/version.md",
    "docs/chatgpt/index.md",
    "docs/chatgpt/project_instructions.md",
    "docs/chatgpt/new_chat_behavior.md",
    "docs/chatgpt/cross_surface_contract.md",
    "docs/chatgpt/cross_surface_gap_analysis.md",
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
    "skills/research-orchestrator/SKILL.md",
    "skills/research-orchestrator/agents/openai.yaml",
    "skills/research-orchestrator/references/source-retrieval.md",
    "skills/research-orchestrator/references/routing-and-qc.md",
    "skills/research-orchestrator/tests/activation_cases.md",
    "evals/literature/README.md",
    "evals/cross-surface/README.md",
    ".agents/plugins/marketplace.json",
    ".agents/plugins/plugins/agentic-research-workflow/.codex-plugin/plugin.json",
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
    ROOT / "skills" / "research-orchestrator",
    ROOT / "evals" / "literature",
    ROOT / "evals" / "cross-surface",
    ROOT
    / ".agents"
    / "plugins"
    / "plugins"
    / "agentic-research-workflow"
    / "skills"
    / "research-orchestrator",
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
    text = read_text(path)
    lines = text.splitlines()
    if not 80 <= len(lines) <= 150:
        errors.append(f"AGENTS.md must be 80-150 lines; found {len(lines)}")

    # Structural validation protects the bootstrap instructions; it does not prove
    # real fresh-session routing behavior, which requires cross-surface testing.
    routing_anchors = {
        "workflow version bootstrap": ("docs/version.md",),
        "workflow router bootstrap": ("docs/workflows/index.md",),
        "first substantive reply timing": ("before the first substantive reply",),
        "route selection": ("primary route", "selected route"),
        "workflow naming is optional": ("Users do not need to name a workflow",),
    }
    for label, alternatives in routing_anchors.items():
        if not any(anchor in text for anchor in alternatives):
            errors.append(f"AGENTS.md routing bootstrap missing: {label}")


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


def check_skill(skill_name: str, errors: list[str]) -> None:
    path = ROOT / "skills" / skill_name / "SKILL.md"
    if not path.is_file():
        return
    text = read_text(path)
    if not text.startswith("---\n"):
        errors.append(f"skills/{skill_name}/SKILL.md lacks YAML frontmatter")
        return
    parts = text.split("---", 2)
    if len(parts) < 3:
        errors.append(f"skills/{skill_name}/SKILL.md frontmatter is not closed")
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
    if values.get("name") != skill_name:
        errors.append(f"{skill_name} skill name does not match its folder")
    if not values.get("description") or "TODO" in values.get("description", ""):
        errors.append(f"{skill_name} skill description is missing or incomplete")


def check_project_instructions(errors: list[str]) -> None:
    path = ROOT / "docs" / "chatgpt" / "project_instructions.md"
    if not path.is_file():
        return
    match = re.search(r"```text\s*(.*?)\s*```", read_text(path), re.DOTALL)
    if match is None:
        errors.append("ChatGPT Project instructions need one copy-ready text block")
        return
    word_count = len(match.group(1).split())
    if not 300 <= word_count <= 600:
        errors.append(
            f"ChatGPT Project instructions must be 300-600 words; found {word_count}"
        )


def check_version_record(errors: list[str]) -> None:
    path = ROOT / "docs" / "version.md"
    if not path.is_file():
        return
    text = read_text(path)
    for field in (
        "workflow_version",
        "stable_branch_after_merge",
        "current_validation_ref",
        "last_reviewed_date",
    ):
        if field not in text:
            errors.append(f"workflow version field missing: {field}")


def check_plugin_mirror(errors: list[str]) -> None:
    source = ROOT / "skills" / "research-orchestrator"
    mirror = (
        ROOT
        / ".agents"
        / "plugins"
        / "plugins"
        / "agentic-research-workflow"
        / "skills"
        / "research-orchestrator"
    )
    if not source.is_dir() or not mirror.is_dir():
        errors.append("Research Orchestrator plugin mirror is missing")
        return
    source_files = {
        path.relative_to(source) for path in source.rglob("*") if path.is_file()
    }
    mirror_files = {
        path.relative_to(mirror) for path in mirror.rglob("*") if path.is_file()
    }
    if source_files != mirror_files:
        errors.append("Research Orchestrator plugin mirror file set differs from source")
        return
    for relative in sorted(source_files):
        if (source / relative).read_bytes() != (mirror / relative).read_bytes():
            errors.append(f"Research Orchestrator plugin mirror drift: {relative}")


def check_plugin_metadata(errors: list[str]) -> None:
    manifest_path = (
        ROOT
        / ".agents"
        / "plugins"
        / "plugins"
        / "agentic-research-workflow"
        / ".codex-plugin"
        / "plugin.json"
    )
    marketplace_path = ROOT / ".agents" / "plugins" / "marketplace.json"
    try:
        manifest = json.loads(read_text(manifest_path))
        marketplace = json.loads(read_text(marketplace_path))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"plugin metadata is unreadable: {exc}")
        return
    if manifest.get("name") != "agentic-research-workflow":
        errors.append("plugin manifest name is incorrect")
    if manifest.get("skills") != "./skills/":
        errors.append("plugin manifest must expose ./skills/")
    entries = marketplace.get("plugins", [])
    match = next(
        (
            entry
            for entry in entries
            if entry.get("name") == "agentic-research-workflow"
        ),
        None,
    )
    if match is None:
        errors.append("agentic-research-workflow marketplace entry is missing")
        return
    if match.get("source", {}).get("path") != "./plugins/agentic-research-workflow":
        errors.append("agentic-research-workflow marketplace source path is incorrect")


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
    check_skill("literature", errors)
    check_skill("research-orchestrator", errors)
    check_project_instructions(errors)
    check_version_record(errors)
    check_plugin_mirror(errors)
    check_plugin_metadata(errors)
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
