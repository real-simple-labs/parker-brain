---
name: self-improve
description: Parker's self-improvement governance for the brand — the disposing half of the living layer. Weekly it curates captured reasoning traces, decides which dreaming proposals get promoted (human in the loop), advances weighted open loops into hypotheses via the roll-up, and runs any re-validations that have come due. It is the gate: dreaming proposes, self-improvement disposes. Use weekly as a scheduled routine, or when asked to curate learnings, promote proposals, advance open loops, or self-improve.
---

# Self-improve — the governing half of the living layer

Dreaming generates; **self-improvement governs whether anything becomes canonical.** Nothing dreaming proposed is applied on its own — context edits, skill changes, new workflows, promoted loops, and re-validations all route through this pass with the human in the loop. The job is to preserve the *reasoning traces* that should change future behavior, not to remember every chat fragment.

## When it runs

**Weekly** (or before a major prompt/skill refresh). Continuous trace *capture* happens during everyday work; this is the weekly *curation* that promotes carefully.

## First run — scaffold if absent

If `self-improvement/` does not yet exist in this repo, create it: `reasoning-traces/[YYYY-MM]/`, `review-queue.md`, `patterns/INDEX.md`, `applied-changes.md`. This is the routing layer that says what should change and why — not a replacement for brand memory or prompt docs.

## The four jobs of the weekly pass

### 1. Curate reasoning traces

Review new traces in `self-improvement/reasoning-traces/[YYYY-MM]/`, cluster repeated themes, promote repeated or explicitly-approved rules into `applied-changes.md`, update the affected prompts / skills / context docs / brand surfaces, keep unresolved items in `review-queue.md` with a promotion condition, and mark stale or contradicted traces rejected or superseded. **Promotion preserves provenance — cite the trace IDs that caused each change.**

A trace is worth capturing when the user corrects Parker and explains why, says a rule should apply broadly, approves/rejects an output for a named reason, reroutes where content lives, edits a hypothesis or strategic read, or names a repeated failure mode. **Not** for routine status updates, typo fixes, one-off wording, or facts that belong in a brand context doc.

Use the narrowest correct route: a local output issue → fix the output; brand learning → `running-notes/` or brand rules; a prompt/skill behavior → a trace + candidate on the affected skill; a system rule → a trace, and update `CLAUDE.md` *only* when the user explicitly asks or the rule is already clearly approved.

### 2. Dispose of dreaming proposals

Walk `dreaming/proposals/pending/`. For each, decide with the human in the loop:
- **Promote** → apply the change for that bucket (context edit, skill change, schedule, idea, or open loop), move the file to `dreaming/proposals/applied/`, and log it in `applied-changes.md` tied back to the proposal.
- **Dismiss** → move to `dreaming/proposals/dismissed/` with the reasoning preserved (a rejected dream teaches what doesn't land).
A proposed **schedule** in `schedules/proposed/` is promoted into an active `schedules/[slug].md` only on explicit confirmation — and arming its cron is then a `setup-routines` step. A proposed **idea** routes to the idea bank (`harvest-ideas`); a proposed **open loop** is captured in `open-loops/` and weighted in job #3 below.

### 3. Advance open loops → hypotheses (the roll-up)

Collect every open loop across the context docs and `open-loops/`, run the kill list, consolidate, score, and promote.

- **Kill** a loop if: the answer is obvious from owned channels; no one buys on it; the brand's own domain knowledge already resolves it (e.g. a corporate-owned brand can't put "kept me out of the ER" in paid creative — claims/compliance kill it before research); it's stale (18+ months, not in current data); or it's infrastructure, not strategy (route to the operational owner). Expect ~half of candidates killed or consolidated — that's correct; the strategist's signature move is the cut.
- **Re-formulate before scoring.** The first question is rarely the best. Look for the deeper question the observation points at, and the question that consolidates several observations into one underlying fork. Score the re-formulated question.
- **Score** each surviving loop on **Stakes, Confidence, Researchability, Novelty** (1–5 each, /20). Score Researchability generously — the brand's own running creative already passed its compliance loop and answers most "what can we say" questions; score 1–2 only when the answer lives in proprietary, never-published data.
  - **17–20 Tier 1** → immediate hypothesis queue. **14–16 Tier 2** → backlog. **Below 14** → archived with reasoning (a known dead-end-at-this-bar). **Stakes ≥4 AND Researchability ≤2** → brand-routed (overrides total): bring to the user for the proprietary input.
- For promoted Tier-1 loops, turn the question into a **hypothesis**: a prediction plus a plan to test it that is within Parker's actual capabilities. Write it to `hypotheses/awaiting-user/[YYYY-MM]/` (proposed to the user) or `hypotheses/tested/[YYYY-MM]/` (Parker runs it). Loops the user declines go to `hypotheses/denied/[YYYY-MM]/` with reasoning preserved. Archive killed loops under `open-loops/archived/[YYYY-MM]/`, promote survivors under `open-loops/promoted/[YYYY-MM]/`.

### 4. Run due re-validations

Nothing stays true forever. Check `re-validations/scheduled/` for any confirmed insight whose re-check date has passed (read today from `get_current_time`). Re-run the validation, write the outcome to `re-validations/results/[YYYY-MM]/`, and update the brand profile if the finding moved. A validation resolves to one of four states — **validated / invalidated / inconclusive / insufficient-evidence** — stored under the matching `validations/` folder. A finding almost always opens new questions: capture those as new loops in `open-loops/` for the next roll-up, so the chain feeds itself.

## Hard rules

- **Dreaming proposes, self-improvement disposes** — and the **human stays in the loop**. Do not silently promote an inferred "why" or incomplete history; ask for a context dump or confirmation before promoting.
- Do not treat one correction as a universal rule unless the user says it's global or the pattern repeats.
- Do not create new docs when an existing living surface can absorb the learning.
- Do not update a prompt or skill from a single trace without explicit user approval.
- Always connect an applied change back to the trace or proposal that caused it; preserve reasoning for rejected items too.
- Do not overwrite brand-specific rules with global rules; mark thin evidence as thin.
- A handful of strategic loops beats a dozen tactical ones. Don't manufacture filler loops to fill a territory.
- Honor the brand hard rules on anything that touches creative or claims.
- Self-contained: in-repo surfaces only. The global *product-signals* stream (anonymized, cross-brand) lives with the factory, **never** in this brand repo. No factory paths at runtime.

## Deliverable

Curated traces with promotions logged in `applied-changes.md`; dreaming proposals moved to applied/dismissed with reasoning; an open-loops roll-up that promoted Tier-1 loops into `hypotheses/`; due re-validations run with results filed; and a short report of what was promoted, what's awaiting the user, and what was killed or archived (and why).
