# Contributing & maintaining `parker-brain`

This is the maintainer-facing guidance for the Parker Brain product repo. The public [README](./README.md) is for teams adopting the brain; this file is for the people who curate what ships into it.

`parker-brain` is the versioned product intelligence layer. Every file here should be safe to ship, explainable, and reusable across brands. It is **not** the private workspace where raw experiments live — raw prompt experiments, test-brand outputs, MCP snapshots, planning notes, raw expert inboxes, and private reasoning traces stay in the private workspace unless they have been sanitized and promoted.

## What belongs here

- Production prompts for context docs, audits, personas, voice-of-customer, market reads, and databases.
- Runtime skills.
- Approved system and methodology docs (retrieval, attribution, open-loop, review standards).
- Reusable templates.
- Generalized, cross-brand knowledge.
- Sanitized fixtures and golden examples.
- Evals, review rubrics, and release notes.

## What does not belong here

- Raw customer or brand outputs.
- Private test brands.
- Planning docs and build trackers.
- Raw transcripts and reasoning-layer notes.
- Raw expert-signal inboxes.
- Prompt-review scratch audits.
- Personal working preferences that are not product rules.
- Unsanitized MCP snapshots or source packets.

## Promotion rule

Most learning starts in the private workspace. It enters this repo only after it is generalized, attributed, reviewed, and safe to ship.

1. Develop and test in the private workspace.
2. Validate against real or fixture data.
3. Extract the durable product lesson.
4. Remove private or brand-specific details unless explicitly approved as a sanitized fixture.
5. Update the relevant prompt, skill, system doc, knowledge doc, fixture, or eval here.
6. Record the reason in the commit message, a release note, or a provenance comment.

## Public-release checklist

Before any public or external distribution:

- Confirm `LICENSE.md` matches the intended rights model.
- Keep `.env`, `.env.*`, local settings, build artifacts, logs, and dependency folders ignored.
- Run a tracked-file secret scan.
- Confirm methodology examples, fixtures, and knowledge docs are sanitized — no private brand, customer, prompt-run, MCP snapshot, or reasoning-layer material, and no named-client account data unless its publication has been explicitly approved.
- Replace any private or named-brand training examples with sanitized fixtures.
