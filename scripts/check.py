#!/usr/bin/env python3
"""Validate this collection's deliberately small, scalar-only skill format."""

import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = ("engineering", "creation", "design", "thinking")


def check(root=ROOT):
    errors, names = [], set()
    skills = sorted(p for category in CATEGORIES for p in (root / category).glob("*/SKILL.md"))
    for path in skills:
        text = path.read_text()
        parts = text.split("---\n", 2)
        if len(parts) != 3 or parts[0]:
            errors.append(f"{path}: missing frontmatter")
            continue
        fields = {}
        for line in parts[1].splitlines():
            key, separator, value = line.partition(": ")
            if not separator or key not in {"name", "description", "license"} or key in fields:
                errors.append(f"{path}: unsupported/duplicate metadata: {line}")
                continue
            # This repo uses plain single-line scalars or JSON double-quoted strings.
            if value.startswith('"'):
                try:
                    value = json.loads(value)
                except ValueError:
                    errors.append(f"{path}: invalid quoted scalar")
                    continue
            elif ": " in value or " #" in value or value[:1] in "[{&*!|>'":
                errors.append(f"{path}: quote this scalar using JSON double quotes")
            fields[key] = value
        name = fields.get("name", "")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64 or name != path.parent.name:
            errors.append(f"{path}: invalid name")
        if name in names:
            errors.append(f"{path}: duplicate skill name")
        names.add(name)
        description = fields.get("description", "")
        if not isinstance(description, str) or not 1 <= len(description) <= 1024:
            errors.append(f"{path}: missing/oversized description")
        if not parts[2].strip():
            errors.append(f"{path}: empty skill body")
        for file in path.parent.rglob("*.md"):
            for link in re.findall(r"\]\(([^)\s]+)\)", file.read_text()):
                if "://" in link or link.startswith("#"):
                    continue
                target = (file.parent / unquote(link.split("#")[0])).resolve()
                if not target.is_relative_to(path.parent.resolve()) or not target.exists():
                    errors.append(f"{file}: missing or non-portable link: {link}")
    if not skills:
        errors.append("No skills found")
    return skills, errors


if __name__ == "__main__":
    skills, errors = check()
    for error in errors:
        print(error, file=sys.stderr)
    print(f"{len(skills)} skills; {len(errors)} structure errors (not a runtime test)")
    sys.exit(bool(errors))
