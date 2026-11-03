#!/usr/bin/env python3
"""Copy selected skills into a skill root, without overwriting anything."""

import argparse
import os
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = ("engineering", "creation", "design", "thinking")
PROJECT_ROOTS = {
    "codex": ".agents/skills", "pi": ".pi/skills",
    "claude": ".claude/skills", "hermes": ".hermes/skills", "dsh": ".dsh/skills",
}


def user_root(platform):
    home = Path.home()
    return {
        "codex": home / ".agents/skills",
        "pi": Path(os.environ.get("PI_CODING_AGENT_DIR", home / ".pi/agent")) / "skills",
        "claude": Path(os.environ.get("CLAUDE_CONFIG_DIR", home / ".claude")) / "skills",
        "hermes": Path(os.environ.get("HERMES_HOME", home / ".hermes")) / "skills",
        "dsh": Path(os.environ.get("DSH_HOME", home / ".dsh")) / "skills",
    }[platform].expanduser()


def install(names, destination):
    catalog = {}
    for category in CATEGORIES:
        for entry in (ROOT / category).glob("*/SKILL.md"):
            if entry.parent.name in catalog:
                raise ValueError(f"Duplicate skill: {entry.parent.name}")
            catalog[entry.parent.name] = entry.parent
    if len(set(names)) != len(names):
        raise ValueError("Select each skill only once")
    sources = []
    for name in names:
        if name not in catalog:
            raise ValueError(f"Unknown skill: {name}. Available: {', '.join(sorted(catalog))}")
        target = destination / name
        if target.exists() or target.is_symlink():
            raise ValueError(f"Already exists (left unchanged): {target}")
        source = catalog[name]
        if source == destination or source in destination.parents:
            raise ValueError("Destination cannot be inside a source skill")
        sources.append((source, target))
    # Validate all selections before creating the destination or copying files.
    destination.mkdir(parents=True, exist_ok=True)
    for source, target in sources:
        shutil.copytree(source, target)
        print(target)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("platform", choices=PROJECT_ROOTS)
    parser.add_argument("skills", nargs="+", help="Skill names, without category folders")
    scope = parser.add_mutually_exclusive_group()
    scope.add_argument("--project", type=Path, help="Install into this project's native skill root")
    scope.add_argument("--dest", type=Path, help="Override the exact skill root (also useful for testing)")
    args = parser.parse_args()
    destination = args.dest if args.dest is not None else (
        args.project / PROJECT_ROOTS[args.platform] if args.project is not None
        else user_root(args.platform)
    )
    try:
        install(args.skills, destination.expanduser().resolve())
    except (ValueError, OSError) as exc:
        parser.exit(1, f"{exc}\n")
    if args.platform == "hermes" and args.project is not None:
        print("Project skills require trust; review and use `hermes skills trust` in that project.")
    print("Files copied only. Confirm discovery in the target agent; see the platform reference.")


if __name__ == "__main__":
    main()
