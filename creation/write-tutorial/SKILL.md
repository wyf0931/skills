---
name: write-tutorial
description: Write or revise a hands-on technical tutorial for a guided learning experience. Use for first-project walkthroughs and learning-by-doing lessons, including 中文入门教程. Not for an experienced user's immediate task or API lookup.
license: CC-BY-SA-4.0
---

# Write a tutorial

Deliver a coherent practice experience with a visible outcome. Completing the artifact is evidence of completing the exercise, not proof of mastery.

## Establish the starting point

Use the supplied code and documentation as technical evidence. Identify the learner's observable abilities, environment/version, practice outcome, and skills the exercise is meant to develop. “Beginner” alone is insufficient: new to this tool and new to programming are different starting points. Ask only for information that materially changes the route; state reasonable assumptions otherwise.

If the reader already has a real task and sufficient skills, explain the mismatch briefly and offer a task-focused document. Do not silently change the requested deliverable.

## Design the experience

- Choose one reliable path. Make incidental choices for the learner; leave alternatives and production tuning for later links.
- Give a meaningful result early. Connect actions, expected observations, and subsequent actions so the learner can tell where they are.
- Make file locations, command working directories, required credentials and dependencies explicit where needed. Do not assume a previous page was read.
- At important transitions, say what should change and what to notice. Use authentic output; label illustrative or variable output.
- Keep the explanation needed to act and observe. Move longer theory elsewhere without hiding prerequisites or essential warnings.
- Make common mistakes recoverable. Where useful, explain how to reset or repeat the practice. Place destructive or billable effects before the relevant action.
- Prefer a small example distilled from a real use case. Identify simplifications that make it unsuitable for production. Make code examples correct for the stated environment, easy to understand and reuse, and safe to run; identify side effects and prerequisites. Separate snippets from complete runnable examples and comment only where the code is not self-explanatory.
- For a long tutorial, use task-oriented sections and navigation that help learners resume their place. Introduce prerequisite concepts before relying on them, and defer optional depth without hiding what the learner needs for the promised outcome.

## Write and verify

Use the user's requested language; for Chinese deliverables, default to natural Simplified Chinese. Name concrete objects and actions; introduce necessary search terms without translating code identifiers. Use companionship sparingly rather than beginning every sentence with “我们”. Avoid unsupported claims that a task is easy or takes a fixed time.

Verify the route from its stated starting point when execution is available and authorized. Check the promised results, not just command exit codes. Report the environment and any unverified steps separately from the finished document. Never fabricate results or product behavior to bridge a gap.

For examples and boundary checks, read [practice notes](references/practice.md). They are illustrations, not a mandatory article outline.

## Source

Adapted from Daniele Procida's [Diátaxis tutorials](https://diataxis.fr/tutorials/), CC BY-SA 4.0; operational and Chinese-language guidance added by this collection. This notice travels with the skill.
