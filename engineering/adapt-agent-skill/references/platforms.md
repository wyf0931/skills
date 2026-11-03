# Agent platform differences

Checked against first-party documentation/source on **2026-11-03**. These are documentation findings, not five successful runtime tests. Paths below assume default homes; configuration and environment overrides take precedence. `pi` means the Pi coding agent, not a similarly named fork.

## Discovery and invocation

| Host | User skill root | Project skill root | Explicit use / refresh |
| --- | --- | --- | --- |
| Codex | `~/.agents/skills/` | `.agents/skills/` from cwd up to repo root | `$name` or skill picker; detects changes, restart if absent |
| Pi | `~/.pi/agent/skills/`, also `~/.agents/skills/` | `.pi/skills/`, also `.agents/skills/` | `/skill:name`; `/reload` after edits |
| Claude Code | `~/.claude/skills/` | `.claude/skills/` | `/name`; current docs describe watched skill files; restart older clients if absent |
| Hermes Agent | `~/.hermes/skills/` | repo `.hermes/skills/`, also `.agents/skills/` | `/name`, or `skills_list` / `skill_view`; `/reload-skills` refreshes slash commands |
| DeepSeek Harness (`dsh`) | `<dshHome>/skills/`, `<agentsHome>/skills/` | repo `.dsh/skills/`, also `.agents/skills/` | model-facing `skill` loader; current local provider watches catalog changes |

**Install individual bundles directly under the chosen root.** Pi and Hermes support nested skill categories. dsh explicitly does not recursively discover `**/SKILL.md`. Do not rely on category recursion in a shared installation. Codex, Pi and Claude document symlink support; copying a complete folder is this collection's conservative, cross-OS baseline.

Hermes project skills require `hermes skills trust`; review before trusting. Its user-level `~/.agents/skills` requires `skills.external_dirs` configuration rather than assumed discovery. Pi project resources also have a trust gate. Existing host policies still apply everywhere.

## Project instructions and extension boundaries

| Host | Project guidance | Host features not assumed by portable skills |
| --- | --- | --- |
| Codex | `AGENTS.md`, nearer guidance wins | `agents/openai.yaml` UI/policy/dependencies; Codex-specific tools |
| Pi | AGENTS family and CLAUDE fallback; same-directory priority matters | Extensions and TypeScript tools; no assumed built-in delegation or plan mode |
| Claude Code | `CLAUDE.md`; newer versions can load `AGENTS.md` | Argument substitutions, dynamic shell injection, `context: fork`, tool grants |
| Hermes Agent | Hermes-specific files precede AGENTS, then other fallbacks | `metadata.hermes` gating/config; `platforms` means OS, not agent brands |
| dsh | Default instruction candidates include AGENTS and CLAUDE | Cordis providers/plugins, `skill` tool, exact invocation-policy keys |

The repository uses `AGENTS.md` as its source and a one-line `CLAUDE.md` importing it for older Claude clients. Claude's current documentation puts native AGENTS support at v2.1.277+, conditional on other instruction files/settings. dsh does not interpret the Claude import convention as a shared standard; its AGENTS candidate supplies the real instructions. Never duplicate or diverge those instructions.

Use standard `name` and `description` metadata. Optional standard fields are not guaranteed to have identical semantics on every host; this collection also includes `license`. In particular, do not equate Claude's invocation controls, Codex's policy YAML, Hermes metadata and dsh's provider policy. Tool permissions remain host configuration, not a portable promise.

These five instruction-only skills need ordinary text/file access. The repository installer/checker separately need Python 3.10+. Network access is needed only when a task requires new research. Do not hard-code model IDs, unavailable MCP tools or another host's API into a skill.

## Evidence and version limits

- [Agent Skills specification](https://agentskills.io/specification): baseline bundle, metadata and relative references.
- [OpenAI skills](https://learn.chatgpt.com/docs/build-skills) and [customization](https://learn.chatgpt.com/docs/customization/overview): Codex discovery, invocation, guidance and optional metadata. Pages are live documentation.
- [Claude skills](https://code.claude.com/docs/en/skills) and [project memory](https://code.claude.com/docs/en/memory): native paths, extensions and AGENTS version boundary. Pages are live documentation; installed older clients may differ.
- Pi snapshot `0c7c7419886ba1879564e20eaaf44ffbf01ffc75`: [skills](https://github.com/earendil-works/pi/blob/0c7c7419886ba1879564e20eaaf44ffbf01ffc75/packages/coding-agent/docs/skills.md), [configuration](https://github.com/earendil-works/pi/blob/0c7c7419886ba1879564e20eaaf44ffbf01ffc75/packages/coding-agent/docs/configuration.md), [loader](https://github.com/earendil-works/pi/blob/0c7c7419886ba1879564e20eaaf44ffbf01ffc75/packages/coding-agent/src/core/skills.ts).
- Hermes snapshot `5b526a53189072c34349eb357803f4cc039505a7`: [skills guide](https://github.com/NousResearch/hermes-agent/blob/5b526a53189072c34349eb357803f4cc039505a7/website/docs/user-guide/features/skills.md), [authoring](https://github.com/NousResearch/hermes-agent/blob/5b526a53189072c34349eb357803f4cc039505a7/website/docs/developer-guide/creating-skills.md), [instruction loading](https://github.com/NousResearch/hermes-agent/blob/5b526a53189072c34349eb357803f4cc039505a7/agent/prompt_builder.py).
- dsh snapshot `ce7073d51254c26cd63b22a60835b8f948deb447`: [loader](https://github.com/deepseek-ai/deepseek-harness/blob/ce7073d51254c26cd63b22a60835b8f948deb447/packages/skill/skill-filesystem/src/index.ts), [instruction candidates](https://github.com/deepseek-ai/deepseek-harness/blob/ce7073d51254c26cd63b22a60835b8f948deb447/packages/context/agent-instructions/src/config.ts), [live skills reference](https://deepseek-harness.github.io/deepseek-harness/en/reference/subsystems/skills).

## Verification record

Local CLI version inspection: Codex `0.166.0`, Pi `1.4.0`, Claude Code `2.1.150`, dsh `0.2.1-rc.3`; Hermes CLI was not found on PATH. Version inspection does not establish loading or task execution. Structure checks and temporary-directory bundle copies are recorded separately in the repository's validation notes. Recheck actual host discovery after installation.
