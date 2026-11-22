#!/usr/bin/env python3
"""Fast, dependency-free structural checks for Rungsmith's Agent Skills.

These checks validate the skill package, not Ignition Designer or Gateway behavior.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
ENGINEERING = SKILLS / "rungsmith-perspective-engineering"
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)\n]+)\)")
NAME_RE = re.compile(r"^name:\s*(.+?)\s*$", re.MULTILINE)
DESCRIPTION_RE = re.compile(r"^description:\s*(.+?)\s*$", re.MULTILINE)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def check_frontmatter(errors: list[str]) -> int:
    count = 0
    for path in sorted(SKILLS.glob("*/SKILL.md")):
        count += 1
        content = path.read_text(encoding="utf-8")
        if not content.startswith("---\n"):
            fail(errors, f"{path}: missing YAML frontmatter")
            continue
        parts = content.split("---", 2)
        if len(parts) < 3:
            fail(errors, f"{path}: unfinished frontmatter")
            continue
        meta = parts[1]
        name = NAME_RE.search(meta)
        description = DESCRIPTION_RE.search(meta)
        if not name or name.group(1).strip("'\" ") != path.parent.name:
            fail(errors, f"{path}: name does not match its directory")
        if not description or not description.group(1).strip("'\" "):
            fail(errors, f"{path}: missing description")
    return count


def check_links(errors: list[str], path: Path) -> int:
    content = path.read_text(encoding="utf-8")
    checked = 0
    for match in LINK_RE.finditer(content):
        uri = match.group(1).strip().split()[0].strip("<>")
        if uri.startswith(("http://", "https://", "mailto:", "#", "data:", "app://")):
            continue
        target = unquote(uri.split("#", 1)[0].split("?", 1)[0])
        if not target:
            continue
        checked += 1
        resolved = (path.parent / target).resolve()
        if not resolved.is_relative_to(ROOT.resolve()):
            fail(errors, f"{path}: local link escapes repository: {uri}")
        elif not resolved.exists():
            fail(errors, f"{path}: missing target for {uri}")
    return checked


def main() -> int:
    errors: list[str] = []
    count = check_frontmatter(errors)
    checked_links = 0
    checked = list(ENGINEERING.rglob("*.md")) + [
        SKILLS / "rungsmith-perspective" / "SKILL.md",
        SKILLS / "rungsmith-ask-rungsmith" / "SKILL.md",
        SKILLS / "rungsmith-performance" / "SKILL.md",
        SKILLS / "rungsmith-data-quality" / "SKILL.md",
        SKILLS / "rungsmith-perspective-css" / "SKILL.md",
        SKILLS / "README.md",
        SKILLS / "COMPARISON.md",
    ]
    for path in checked:
        if not path.is_file():
            fail(errors, f"{path}: expected Markdown missing")
            continue
        checked_links += check_links(errors, path)

    eval_path = ENGINEERING / "EVALS.md"
    if eval_path.is_file():
        cases = re.findall(r"^\| E\d{2} \|", eval_path.read_text(encoding="utf-8"), re.MULTILINE)
        if len(cases) < 9:
            fail(errors, "Perspective engineering must provide >= 9 evaluation cases")

    for error in errors:
        print("ERROR:", error, file=sys.stderr)
    print(f"Checked {count} SKILL frontmatters, {len(checked)} Markdown files, {checked_links} local links; errors={len(errors)}")
    if errors:
        return 1
    print("Structural skill checks passed. Native Perspective verification is NOT included.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
