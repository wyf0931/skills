# Validation

Date: 2026-11-03.

## Completed

- Collection structure checker: 5 skills, 0 errors. Names, descriptions, bundled links and independent resource paths checked.
- Skill Creator's `quick_validate.py`: all 5 skills passed metadata validation.
- Installer unit tests: 4 passed. Complete bundle copy, preflight conflict handling, unknown names and broken symlink conflicts covered.
- Project installation smoke check: all 5 bundles copied to temporary roots for Codex, Pi, Claude Code, Hermes and dsh. Included each skill's references. No real user skill directories or agent settings changed.
- README and repository-local Markdown links checked for existing targets; link anchors and remote URLs are not covered by that check.
- Author desk review: each writing skill distinguishes its reader task, treats missing product facts as unknown, and keeps Chinese adaptation and practice notes inside the installed bundle. This is not an independent behavior evaluation.

## Not established

- Native discovery and execution on any of the five hosts. CLI version inspection alone is not a discovery test.
- Real reader usability or learning outcomes.
- Independent behavior evaluation: attempted but unavailable because the agent model was at capacity. Do not count it as a pass.

## Small next checks

After installation, confirm native discovery with the actual host/version and run a realistic task plus an edge case. Record the host, version, loading method, result and limitations here.

Useful cases: a local tutorial for someone who can run Python but is new to timeouts; a retry how-to with only a parameter name supplied; reference material with unknown defaults; an explanation of duplicate side effects without supplied design history. Check respectively for a connected practice route, honest information gaps, no fabricated contracts, and evidence-based reasoning.

## write-clearly author exercise (2026-11-03)

Manual desk exercise in this repository; not native discovery or an independent host execution test. The examples are invented, not product claims.

- Realistic editing task: for readers who know HTTP but not this service, revise “启用缓存后它会处理请求，过期时更新。TTL 决定这个过程。” The source does not say what “它”, “过期” or “更新” refers to. The skill calls for retaining those uncertainties and asking what expires and who updates what, rather than producing a fluent but invented cache contract. This checks reader knowledge, terminology and ambiguity together.
- Edge case: “仅当响应包含 `Retry-After` 时，客户端可以重试；否则不得重试。” A clarity edit must retain the condition, permission and prohibition, and keep `Retry-After` exact. Do not shorten it to “客户端可以重试” or infer an automatic retry. This checks that fluency does not weaken a technical constraint.

Both are author desk checks of the instructions and expected decisions, not observed reader outcomes. Collection checker: 6 skills, 0 errors; installer unit tests: 4 passed. Native discovery and execution remain untested.


## Google technical writing skill updates (2026-11-03)

The series inventory covered 47 local course articles across foundational writing, intermediate writing, accessibility and error messages. Introductory, summary and exercise pages were used to map scope; topic lessons informed rule extraction. No course examples or images were copied into the skills.

Desk checks (invented scenarios, not product claims):

- `write-clearly`: revise “启用缓存后它会处理请求，过期时更新。TTL 决定这个过程。” The source omits the referents and behavior, so the skill should flag the unknowns instead of inventing a cache contract. Edge case: preserve the exact condition and prohibition in “仅当响应包含 `Retry-After` 时，客户端可以重试；否则不得重试。”
- `write-error-messages`: for “附件太大”, ask for or verify the product limit and offer a supported next step; do not invent a size threshold. Edge case: if retry safety is unknown, do not recommend retrying.
- `write-accessible-content`: for a chart that distinguishes failure states only by red and green, call for text labels or another redundant cue. Edge case: do not claim contrast compliance from source markup without rendered colors and a measurement.
- `write-tutorial`: distinguish a complete runnable sample from a snippet and disclose environment and side effects. Edge case: do not claim the sample was executed if no environment is available.
- Existing how-to, reference and explanation additions were desk-checked for task route, lookup navigation and explanatory scope respectively; no fixed outline is imposed.

These are author desk checks of expected decisions, not independent behavior evaluation, user research or native host discovery/runtime tests.
