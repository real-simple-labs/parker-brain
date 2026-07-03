---
name: self-improve
description: Parker's self-improvement governance for the brand — the disposing half of the living layer. Weekly it curates captured reasoning traces and decides which dreaming proposals get promoted, human in the loop — including the doc-alignment proposals the research cycle files. It is the gate: dreaming and research propose, self-improvement disposes. The loop pipeline itself (roll-up, hypotheses, validations, re-validations) runs in /research-loops. Use weekly as a scheduled routine, or when asked to curate learnings, promote proposals, or self-improve.
---

# Self-improve — the governing half of the living layer

Dreaming and the research cycle generate; **self-improvement governs whether anything becomes canonical.** Nothing they proposed is applied on its own — context edits, skill changes, new workflows, and the research cycle's doc-alignment proposals all route through this pass with the human in the loop. The job is to preserve the *reasoning traces* that should change future behavior, not to remember every chat fragment.

## When it runs

**Weekly** (or before a major prompt/skill refresh). Continuous trace *capture* happens during everyday work; this is the weekly *curation* that promotes carefully.

## First run — scaffold if absent

If `self-improvement/` does not yet exist in this repo, create it: `reasoning-traces/[YYYY-MM]/`, `review-queue.md`, `patterns/INDEX.md`, `applied-changes.md`. This is the routing layer that says what should change and why — not a replacement for brand memory or prompt docs.

## The two jobs of the weekly pass

### 1. Curate reasoning traces

Review new traces in `self-improvement/reasoning-traces/[YYYY-MM]/`, cluster repeated themes, promote repeated or explicitly-approved rules into `applied-changes.md`, update the affected prompts / skills / context docs / brand surfaces, keep unresolved items in `review-queue.md` with a promotion condition, and mark stale or contradicted traces rejected or superseded. **Promotion preserves provenance — cite the trace IDs that caused each change.**

A trace is worth capturing when the user corrects Parker and explains why, says a rule should apply broadly, approves/rejects an output for a named reason, reroutes where content lives, edits a hypothesis or strategic read, or names a repeated failure mode. **Not** for routine status updates, typo fixes, one-off wording, or facts that belong in a brand context doc.

Use the narrowest correct route: a local output issue → fix the output; brand learning → `running-notes/` or brand rules; a prompt/skill behavior → a trace + candidate on the affected skill; a system rule → a trace, and update `CLAUDE.md` *only* when the user explicitly asks or the rule is already clearly approved.

### 2. Dispose of dreaming proposals

Walk `dreaming/proposals/pending/`. For each, decide with the human in the loop:
- **Promote** → apply the change for that bucket (context edit, skill change, schedule, idea, or open loop), move the file to `dreaming/proposals/applied/`, and log it in `applied-changes.md` tied back to the proposal.
- **Dismiss** → move to `dreaming/proposals/dismissed/` with the reasoning preserved (a rejected dream teaches what doesn't land).
A proposed **schedule** in `schedules/proposed/` is promoted into an active `schedules/[slug].md` only on explicit confirmation — and arming its cron is then a `setup-routines` step. A proposed **idea** routes to the idea bank (`harvest-ideas`); a proposed **open loop** is captured in `open-loops/` for the next `/research-loops` roll-up. A **doc-alignment proposal** from the research cycle (a validated finding waiting to be folded into a standing doc) is applied on the user's agreement with its validation provenance intact, or dismissed with the reasoning preserved.

### Where the loop pipeline went

The research work that used to live here — the roll-up, advancing loops into hypotheses, running validations, and due re-validations — is its own standing routine now: **`/research-loops`**, weekly and mid-week, so findings are fresh by the time this pass curates them. This pass stays the governor: it disposes of the alignment proposals research files, and it curates what the week's findings taught into durable learning.

## Hard rules

- **Dreaming and research propose, self-improvement disposes** — and the **human stays in the loop**. Do not silently promote an inferred "why" or incomplete history; ask for a context dump or confirmation before promoting.
- Do not treat one correction as a universal rule unless the user says it's global or the pattern repeats.
- Do not create new docs when an existing living surface can absorb the learning.
- Do not update a prompt or skill from a single trace without explicit user approval.
- Always connect an applied change back to the trace or proposal that caused it; preserve reasoning for rejected items too.
- Do not overwrite brand-specific rules with global rules; mark thin evidence as thin.
- Honor the brand hard rules on anything that touches creative or claims.
- Self-contained: in-repo surfaces only. The global *product-signals* stream (anonymized, cross-brand) lives with the factory, **never** in this brand repo. No factory paths at runtime.

## Deliverable

Curated traces with promotions logged in `applied-changes.md`; dreaming and research proposals moved to applied/dismissed with reasoning, doc alignments applied with their validation provenance; and a short report of what was promoted, what's awaiting the user, and what was dismissed (and why).
