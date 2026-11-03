---
name: write-how-to
description: Write or revise a technical how-to guide for a concrete task, troubleshooting goal, or operational checklist. Use for 中文操作指南 and readers applying existing skills. Not a first-learning lesson, API catalog, or long conceptual discussion.
license: CC-BY-SA-4.0
---

# Write a how-to guide

Help a capable reader achieve a practical goal in their own environment.

## Define the task

Identify the goal, applicable starting conditions, assumed abilities, relevant versions, and completion criterion from the supplied material. Inspect an existing guide before creating a duplicate page. Ask about missing conditions only when they would change the solution or make it unsafe; otherwise state assumptions.

Name the document after the reader's goal, not just a feature. “Rotate an API key without interrupting requests” is more useful than “API keys”. If the request is for guided first learning, flag the difference rather than stretching a task guide into a lesson.

## Build an actionable route

- Start and stop where the task needs. Do not repeat basic training the intended reader already has.
- Order actions by dependencies and the reader's workflow. Include working directory, file, scope, or target when ambiguity would cause a mistake.
- Put decision conditions before the action they select. Explain how to choose, not merely “select the appropriate option”.
- Use branches or a checklist when the task is not linear. Include only relevant variants; link full option catalogs separately.
- Place consequences, permissions and required backups before the affected operation. Include recovery or rollback when the task requires it and evidence supports it.
- Give a concrete completion check. For troubleshooting, connect symptoms to discriminating checks and conditional remedies; do not list unrelated commands.
- Keep brief reasons needed for a correct decision. Link substantial background rather than interrupting the task.
- For a multi-part guide, use task-oriented headings and navigation. Present prerequisite and setup information before dependent steps, and disclose optional or advanced branches where readers can find them without interrupting the main route.

## Write and verify

Use the requested language; default to natural Simplified Chinese for Chinese work. Prefer explicit conditions and verbs to nominal phrases such as “进行配置的应用”. Keep parameter names and interface labels exact. Do not use “适当”“按需” to hide a required judgment.

Verify supported paths when practical and authorized, especially alternative starting states. If facts, credentials or a test environment are missing, identify the resulting gap; do not invent commands, paths or successful execution. Keep validation notes separate from reader-facing steps unless the reader needs them.

Read [practice notes](references/practice.md) for concrete examples and a checklist-shaped alternative.

## Source

Adapted from Daniele Procida's [Diátaxis how-to guides](https://diataxis.fr/how-to-guides/), CC BY-SA 4.0; operational and Chinese-language guidance added by this collection. This notice travels with the skill.
