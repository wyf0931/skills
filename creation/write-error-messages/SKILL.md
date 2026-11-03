---
name: write-error-messages
description: Write or revise user-facing or developer-facing technical error messages. Use when a failure needs clear diagnosis, actionable recovery, or audience-appropriate wording; not for implementing an error-handling model or logging system.
license: CC-BY-SA-4.0
---

# Write useful error messages

Help the affected reader understand what failed and what they can do next. Treat a message as part of the product's behavior: preserve the actual failure semantics and never claim a cause or remedy that evidence does not support.

## Establish audience and evidence

Identify who sees the message, what they know, what action they were attempting, and what the system can reliably observe. Separate user-correctable input from internal faults, transient conditions and conflicts. Confirm the expected behavior and constraints from supplied product evidence; ask or flag a gap when the cause or recovery is unknown.

## Write the message

- Name the specific problem and, when useful and safe, the offending value or resource. Explain the applicable requirement with concrete bounds or format only when known.
- Give a next step the reader can take. Make it specific and feasible; do not tell users to fix an internal defect or retry when retry safety is unknown.
- Use terms familiar to the audience and consistent with the product. Include an example when it makes valid input easier to recognize.
- Keep the message concise, direct and respectful. Avoid blame, double negatives, unexplained jargon, jokes and excessive apology. Prefer a positive instruction when it states the fix more clearly.
- Put detail near the failure. Link to longer guidance when the reader needs it; include a stable error code or identifier when the product defines one and the audience can use it.
- Keep internal diagnostics, logs and error identifiers distinct from user-facing prose. Do not expose secrets or sensitive internals.

## Review

Check that the message states the real problem, preserves uncertainty, gives a supported recovery path, and suits the reader. Check terminology against neighboring messages when available. For Chinese, express conditions and recovery steps in natural Chinese, preserve exact identifiers, and avoid translating English sentence structure mechanically. A wording review does not validate the implementation or its error model.

## Source

Adapted from Google's [Writing Helpful Error Messages course](https://developers.google.com/tech-writing/errors), shared under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Condensed and adapted for Chinese; not an official Google skill. Source and license checked 2026-11-03.
