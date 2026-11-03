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
