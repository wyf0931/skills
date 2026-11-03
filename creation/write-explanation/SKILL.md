---
name: write-explanation
description: Write or revise a technical explanation of concepts, mechanisms, design choices, or trade-offs. Use for why/how-it-works discussions and 中文原理与概念说明. Not a procedural guide, API lookup entry, or unsupported opinion piece.
license: CC-BY-SA-4.0
---

# Write an explanation

Help readers connect facts into an understanding they can use beyond the example.

## Frame the question

Identify a concrete question or misconception, the reader's existing knowledge, the intended change in understanding, and a useful stopping boundary. Explain the chosen topic rather than expanding into everything adjacent. An expert in another field is not necessarily a beginner in all fields.

Use supplied sources and inspect relevant code or first-party material when available. Separate evidence, inferred mechanism, historical rationale and your judgment. Do not invent why a designer made a decision just because the choice has a plausible benefit.

## Develop the reasoning

- Start with a phenomenon or question that motivates the concept, or a concise model when it suits the audience. No fixed essay outline is required.
- Make causal steps explicit. Explain what connects an observation to a conclusion; naming a mechanism is not an explanation of it.
- Introduce unfamiliar concepts in a usable order. Check that knowledge assumptions remain consistent throughout.
- Prefer examples that expose the relevant relationship. From real code or incidents, remove unrelated detail and mark simplifying assumptions.
- Consider alternatives, counterexamples and constraints when they help explain a choice. Say under which conditions the conclusion changes.
- Use an analogy for a specific relationship, then return to the actual mechanism. State its limits when the analogy could mislead.
- Keep commands and interface facts only as evidence or illustration. Link a separate procedure or reference when readers need to act or look up details.

## Chinese adaptation

For Chinese deliverables, rebuild the reasoning in natural Simplified Chinese rather than translating sentence order. Turn stacked abstract nouns into concrete subjects and causal verbs. Retain useful technical terms and English search terms on introduction; preserve code identifiers. Avoid filler such as “显而易见”“只需轻松地”. Explain the actual difficulty instead of judging the reader.

## Verify understanding and truth

Check whether the explanation covers the original question and handles a changed condition without contradiction. A subject expert can check truth; a target reader can expose missing prerequisites. AI review can suggest gaps but is not real user testing. Report unavailable evidence or testing honestly.

Read [practice notes](references/practice.md) for examples of causal repair and counterexamples.

## Source

Adapted from Daniele Procida's [Diátaxis explanation](https://diataxis.fr/explanation/), CC BY-SA 4.0; operational and Chinese-language guidance added by this collection. This notice travels with the skill.
