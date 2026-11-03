# Skills

[English](README.md) · [简体中文](README.zh-CN.md)

Scott 的个人 Agent skills。小而独立，一份核心正文，按需适配平台。

| 分类 | Skills |
| --- | --- |
| **Engineering · 工程** | [adapt-agent-skill](engineering/adapt-agent-skill/SKILL.md) — 创建与适配跨平台 skill |
| **Creation · 内容创作与技术写作** | [write-tutorial](creation/write-tutorial/SKILL.md) 教程 · [write-how-to](creation/write-how-to/SKILL.md) 操作指南 · [write-reference](creation/write-reference/SKILL.md) 参考 · [write-explanation](creation/write-explanation/SKILL.md) 解释 |
| **Design · 产品设计与 UI/UX** | 预留 |
| **Thinking · 思维方式与问题解决** | 预留 |

## 使用

使用 [Skills CLI](https://github.com/vercel-labs/skills) 快速安装（需要 Node.js）：

```sh
npx skills add https://github.com/wyf0931/skills --skill write-tutorial
```

一次安装四个写作 skill：

```sh
npx skills add https://github.com/wyf0931/skills --skill write-tutorial --skill write-how-to --skill write-reference --skill write-explanation
```

将技能名换成 `adapt-agent-skill`，即可安装平台适配 skill。
CLI 会提示选择目标 Agent；添加 `-g` 可全局安装。
查看可用技能：`npx skills add https://github.com/wyf0931/skills --list`。

也可以克隆仓库，使用 Python 安装器：

```sh
git clone https://github.com/wyf0931/skills.git
cd skills
python3 scripts/install.py codex write-tutorial write-how-to write-reference write-explanation
```

将 `codex` 换成 `pi`、`claude`、`hermes` 或 `dsh`。仓库工具需要 Python 3.10+，
纯写作 skill 不依赖 Python。添加 `--project /path/to/project` 安装到项目，
或用 `--dest /path/to/skills` 指定已配置的目录。已有 skill 不会被覆盖。
Hermes 项目技能需审阅后信任；安装器不修改 Agent 配置。

也可以手动复制完整 skill 文件夹。安装单个 **skill**，不要直接安装整棵分类目录。
让 Agent 使用对应名称，或明确要求它读取 `SKILL.md`。

采用 Agent Skills 格式；各平台的目录、调用和信任机制有区别，详见
[平台差异与来源](engineering/adapt-agent-skill/references/platforms.md)。
尚未完成五个平台的运行实测，已做检查见[验证记录](docs/validation.md)。

## 维护

遵循 [AGENTS.md](AGENTS.md)。保持 skill 自包含，按需读取平台资料，同步维护两份 README。

```sh
python3 scripts/check.py
python3 -m unittest discover -s tests
```

写作 skills 基于 Diátaxis 与社区实践，中文适配覆盖信息顺序和推理关系。
[实践研究](docs/research/community-practices.md) ·
[中文适配](docs/research/skill-practice-synthesis.md) · [来源声明](NOTICE.md)。

[CC BY-SA 4.0](LICENSE)。
