# Working on this repository

Personal, portable agent skills. Keep changes small and useful.

- Categories: `engineering/`, `creation/`, `design/`, `thinking/`.
- Each skill lives in `<category>/<name>/SKILL.md`; names are unique across categories.
- Before creating or adapting a skill, read `engineering/adapt-agent-skill/SKILL.md` and its platform reference when needed.
- Use standard `name` and `description` frontmatter. Add optional fields only for a concrete need. Keep descriptions precise about when to trigger.
- Each installed skill must work on its own. References and scripts must stay inside its folder. Do not depend on this file, sibling skills, or repository docs at runtime.
- Prefer instructions about outcomes and decisions over rigid templates. Read references only when relevant. Do not add a script when prose is sufficient.
- Keep the core independent of tool names, shell dialects, absolute paths, model names, slash commands, MCP servers, and platform-only substitutions. Declare real dependencies and give a fallback where possible.
- A skill cannot grant permissions. Follow the active host's approval, filesystem, network, and execution policy. Do not require delegation or unavailable tools.
- Preserve user language and intent. Chinese technical writing needs reconstructed information order and explicit relationships, not sentence-by-sentence translation. Preserve exact technical identifiers.
- Preserve source attribution and license notices. Mark invented examples and unverified technical behavior.
- Keep `README.md` and `README.zh-CN.md` catalogs and installation instructions consistent.
- Check platform claims against first-party docs or source. Record a date/version. Distinguish format checks, discovery checks, and real task execution.

## Checks

Run `python3 scripts/check.py` and `python3 -m unittest discover -s tests` from the repository root. For meaningful skill changes, also run or document a realistic task and an edge case; format checks alone do not prove usefulness. Never label an untested host as tested.
