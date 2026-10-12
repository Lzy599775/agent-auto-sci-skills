#!/usr/bin/env python3
"""Routing-core sync lint (#892).

`shared/references/routing_core.md` holds the cross-skill routing core and
says which files carry it and why. This lint keeps the verbatim copies in
`.claude/CLAUDE.md` and in every top-level `SKILL.md` byte-identical to it.
The manifest-declared Codex distribution checks its five core WORKFLOW.md
entries instead: Claude loader files are excluded, and experiment-agent is
a separately pinned project rather than an ARS routing-core carrier.
The SessionStart announce reads the canonical file at runtime;
`test_check_routing_core_sync.py` runs the announce to check the block arrives.

Checks:
  RC-1  The canonical file holds exactly one begin marker and one end marker,
        each alone on its line, begin before end, around a non-empty block.
  RC-2  Every copy holds exactly one such marker pair, and its block is
        byte-identical to the canonical block, line endings included.

Usage:
    python scripts/check_routing_core_sync.py [--root PATH]

Exit codes: 0 all checks pass; 1 a check failed; 2 a required file is missing.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _skill_lint import (  # noqa: E402
    _uses_codex_workflow_overlay,
    check_marker_copies,
    extract_marker_block,
    iter_skill_files,
    read_or_exit2,
)

CANONICAL = Path("shared/references/routing_core.md")
CLAUDE_MD = Path(".claude/CLAUDE.md")
CORE_SKILLS = ("academic-paper", "academic-paper-reviewer", "academic-pipeline", "deep-research", "sr-screener")
BEGIN = "<!-- routing-core:begin -->"
END = "<!-- routing-core:end -->"


def extract_block(text: str, label: str) -> tuple[str | None, list[str]]:
    """Return the text between the one marker pair, or None with the errors."""
    return extract_marker_block(text, label, BEGIN, END, "routing-core")


def copies(root: Path) -> list[Path]:
    """Required routing carriers, including missing files so deletion fails.

    Unknown skill entries remain in the sweep; only the explicitly separate
    experiment-agent tree is excluded in the Codex distribution.
    """
    codex_overlay = _uses_codex_workflow_overlay(root)
    filename = "WORKFLOW.md" if codex_overlay else "SKILL.md"
    required = {Path(name) / filename for name in CORE_SKILLS}
    discovered = {
        path.relative_to(root) for path in iter_skill_files(root)
        if not (codex_overlay and path.parent.name == "experiment-agent")
    }
    return ([] if codex_overlay else [CLAUDE_MD]) + sorted(required | discovered)


def check(root: Path) -> list[str]:
    """Run RC-1 and RC-2 under `root`; a missing file exits 2."""
    # Read the canonical file before copies() scans the tree, so a bad --root
    # exits 2 on the missing canonical file instead of failing in the scan.
    read_or_exit2(root, str(CANONICAL), exact=True)
    _, errors = check_marker_copies(root, CANONICAL, copies(root), BEGIN, END,
                                    "routing-core", "RC-1", "RC-2")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args(argv)
    errors = check(args.root)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"check_routing_core_sync: OK ({len(copies(args.root))} copies match {CANONICAL})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
