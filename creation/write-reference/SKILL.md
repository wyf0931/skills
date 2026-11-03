---
name: write-reference
description: Write or revise technical reference for APIs, CLI commands, configuration, schemas, or error behavior. Use for precise lookup material and 中文参考文档. Not for guided learning, task walkthroughs, or design-rationale essays.
license: CC-BY-SA-4.0
---

# Write technical reference

Provide facts readers can find and rely on while working. Organize around the documented system's logical structure, using consistent patterns for comparable entries.

## Establish authority and scope

Identify the API, command, setting, schema or other documented surface, its version, and the authoritative code/specification or supplied sources. Separate public guarantees from incidental implementation. Do not infer a contract from a single example or test.

If information is missing, seek a source when available. Otherwise expose the gap to the author; omit unsupported claims from the finished entry or visibly mark its draft status. Never fill in defaults or limits from what similar products usually do.

## Describe what matters

Select relevant details, not a mandatory universal field list:

- Identity, purpose, syntax/signature, and applicable versions.
- Inputs: type, units, accepted values, whether required, omission behavior, null/empty handling and defaults. These are distinct facts.
- Outputs and observable behavior: ordering, pagination, side effects, lifecycle, concurrency or repeat-call behavior where relevant.
- Errors, restrictions, compatibility and boundary cases that affect use.
- Short examples that clarify a specific behavior. State prerequisites needed to interpret them; distinguish snippets from complete runnable programs.

Place information where readers expect it across entries. For a large reference set, group by the documented system and provide navigational aids such as an overview, contents or glossary when they materially improve lookup. Use stable terminology and neutral descriptions. Keep warnings with the behavior they qualify. Link specific guides and explanations instead of embedding a lesson or an entire workflow. An example complements a contract; it does not replace one.

## Chinese lookup quality

For Chinese output, keep machine identifiers and official labels exact, with concise Chinese descriptions. Introduce bilingual search terms when useful. Replace ambiguous pronouns with the object name; avoid decorative synonyms for the same parameter. Tables help compare parallel fields, but do not force long behavioral prose into table cells.

## Verify

Check facts against the declared source/version. Ask questions outside the examples: What happens when the field is omitted? Is zero valid? Can an item appear twice? Only answer questions relevant to the surface. Distinguish observed behavior from documented guarantees. State any unverified scope separately.

Read [practice notes](references/practice.md) for lookup examples and traps.

## Source

Adapted from Daniele Procida's [Diátaxis reference](https://diataxis.fr/reference/), CC BY-SA 4.0; operational and Chinese-language guidance added by this collection. This notice travels with the skill.
