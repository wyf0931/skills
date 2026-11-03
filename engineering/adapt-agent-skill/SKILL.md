---
name: adapt-agent-skill
description: Create or adapt a portable Agent Skill for Codex, pi, Claude Code, Hermes Agent, or DeepSeek Harness (dsh). Use when authoring a skill, checking host compatibility, or resolving discovery and invocation differences. Not for migrating credentials or whole agent configurations.
license: CC-BY-SA-4.0
---

# Adapt an agent skill

Keep one useful workflow and the smallest host-specific surface. Preserve the user's task, authorization and chosen platform.

## Inspect before adapting

Identify the intended workflow, target hosts and versions, skill directory, supporting files and real tool dependencies. When a target is unspecified, use portable instructions as the default. Read [platform differences](references/platforms.md) for supported discovery paths and host-specific behavior; recheck first-party documentation when a version or claim matters.

## Portable core

- Use a directory with `SKILL.md` and standard YAML `name` and `description`. Use a unique lowercase hyphenated name matching its folder. Say when the skill applies, including a useful boundary.
- Keep each skill independently installable. Bundle its required references/scripts/assets and link them relative to its own directory. Do not rely on repository-level `AGENTS.md` or sibling skills at runtime.
- Define decisions, outcomes and meaningful checks. Move substantial conditional detail into references. Avoid ceremony, fixed article outlines or approval gates without a task-specific need.
- Describe tool capabilities in ordinary language: read a file, run an available command, search first-party sources. Resolve actual host tool names at runtime. If a required capability is unavailable, state the gap or use a supported fallback; never claim an action occurred.
- Do not embed Claude-only argument substitutions, shell interpolation, subagent settings or permission declarations in the shared core. Do not assume MCP, browsing, delegation, a specific shell, internet access or a specific model.
- Add platform metadata/config only when the user needs the feature. Explain that extensions are optional or supply a separately named host-specific variant; do not maintain five duplicate bodies.
- A skill cannot bypass the host's permission system. Do not broaden execution permissions to make a port work.

## Install and check

Install the individual skill folder directly beneath a supported skill root; category folders are repository organization, not a discovery contract. Copy the whole folder for the portable baseline. Do not overwrite an existing skill without reviewing the conflict. Respect configured home/root overrides.

Verify three different things and report them separately:

1. **Structure:** valid metadata, unique name, self-contained references, declared dependencies, no accidental host-only syntax.
2. **Discovery:** the actual host/version lists or loads the installed skill. Refresh/restart only as documented. If no native installation is possible, explicitly ask the agent to read the full `SKILL.md`; label this manual use, not native discovery.
3. **Behavior:** a realistic task and an edge case produce the promised outcome without relying on another skill or an absent tool. Format validation is not a cross-platform execution test.

When working inside this collection, run its repository checks and keep the bilingual catalogs consistent. Outside it, use the target project's equivalent checks; this skill does not require the collection's scripts.

For adaptations, summarize what changed, retained dependencies, tested host/version, and untested limitations. Keep compatibility claims no stronger than the evidence.
