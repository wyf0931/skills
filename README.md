# Skills

[English](README.md) · [简体中文](README.zh-CN.md)

Scott's personal agent skills. Small, independent workflows; one portable core.

| Category | Skills |
| --- | --- |
| **Engineering** | [adapt-agent-skill](engineering/adapt-agent-skill/SKILL.md) — author and adapt skills across agent platforms |
| **Creation** | [write-tutorial](creation/write-tutorial/SKILL.md) · [write-how-to](creation/write-how-to/SKILL.md) · [write-reference](creation/write-reference/SKILL.md) · [write-explanation](creation/write-explanation/SKILL.md) |
| **Design** | Product design and UI/UX — reserved |
| **Thinking** | Reasoning and problem solving — reserved |

## Use

Clone this repository, then copy selected skills to your agent's skill directory:

```sh
git clone https://github.com/wyf0931/skills.git
cd skills
python3 scripts/install.py codex write-tutorial write-how-to write-reference write-explanation
```

Replace `codex` with `pi`, `claude`, `hermes`, or `dsh`. Python 3.10+ is needed
only for repository tools. Use `--project /path/to/project` for project scope or
`--dest /path/to/skills` for a configured root. Existing skills are never overwritten.
Hermes project skills require trust after review. No agent configuration is changed.

Alternatively, copy a complete skill folder yourself. Install the **skill**, not
the category tree. Ask the agent to use its name, or explicitly read its `SKILL.md`.

The skills follow Agent Skills format. Paths, invocation and trust differ by host;
see [platform differences and sources](engineering/adapt-agent-skill/references/platforms.md).
Five-host runtime compatibility has **not** been established. See [validation](docs/validation.md).

## Contribute

Follow [AGENTS.md](AGENTS.md). Keep skills self-contained, reference platform
differences only when needed, and keep both READMEs in sync.

```sh
python3 scripts/check.py
python3 -m unittest discover -s tests
```

Writing skills build on Diátaxis and practical community experience, with Chinese
adaptation beyond literal translation. [Research](docs/research/community-practices.md) ·
[Chinese adaptation](docs/research/skill-practice-synthesis.md) · [Attribution](NOTICE.md).

[CC BY-SA 4.0](LICENSE).
