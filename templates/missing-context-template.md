# Missing-context template

> Status: `[~]` drafted 2026-06-11, pending Jimmy's review. Canonical home per brand: `running-notes/missing-context.md` (standalone brains) / `z-brands/[brand]/running-notes/missing-context.md`. This is the running list of everything Parker needs from the brand to do creative strategy at full awareness — the single surface a brand contact can be handed as "answer these and Parker gets dramatically smarter."

## What this surface is

Every sub-context doc names its blanks in `data_limitations` frontmatter, and the open-loops grading pass routes brand-only questions to the brand-routed section. Both of those live scattered across the vault. This doc is their consolidation: one living intake agenda, ordered by what unblocks the most.

It is maintained, not regenerated: every doc refresh that discovers a new gap adds it here in the same pass; every intake answer or newly connected data source moves its item to the resolved log with a date and a pointer to where the answer now lives. The movement history is the record of the brand becoming fully known.

## Structure

```
---
brand:
doc: missing-context
last_updated:
sources: data_limitations across all docs + the brand-routed section of the latest open-loops roll-up
---

# Missing context — what the brand has not yet told us

## Data sources not connected

## Intake questions — ordered by what they unblock

## Per-doc named blanks

## Resolved — with date and where the answer lives
```

**Data sources not connected** — the platform-level gaps: review feeds, post-purchase surveys, non-Meta ad channels, analytics, sales/LTV exports. Each entry: what is missing, which docs it starves, what becomes possible when connected.

**Intake questions** — the questions only the brand can answer, consolidated from brand-routed loops and operational blanks. Each entry: the question in plain language a brand contact can answer cold, why it matters in one sentence, which docs and loops it unblocks. Group related questions into batteries a call can walk through: economics and measurement, audience intent, claims and legal posture, team and capacity, calendar and roadmap.

**Per-doc named blanks** — the residual blanks that are neither a data source nor an intake battery, listed per doc so a refresh knows what it is still missing.

**Resolved** — append-only. When an answer lands, move the item here with the date, the answer's new home, and which loops or docs it unblocked.

## Rules

1. Plain language a brand contact understands cold — no internal jargon, no loop IDs without the question spelled out.
2. Order by leverage: the question that unblocks five docs and three Tier 1 loops outranks the question that polishes one blank.
3. Never let it silently drift from the vault: the open-loops roll-up refresh and this doc refresh happen in the same pass.
4. An unanswered question that stops mattering gets retired to Resolved with the reason, not deleted.
