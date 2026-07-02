---
name: research-loops
description: The weekly research cycle — runs the open-loops pipeline end to end so the brand's strategic questions actually get answered instead of piling up. Rolls up and grades the open loops, advances the promoted ones into hypotheses, runs the validations in the testing queue, runs due re-validations, reports what was learned, and then aligns the standing docs with the confirmed findings so the brain never says the old thing after the research says otherwise. Use weekly as a scheduled routine, or when asked to run the research, advance the loops, work the testing queue, or "what have we learned".
---

# Research loops — the weekly research cycle

The brain collects open loops constantly: every audit, every persona read, every dreaming run leaves behind real strategic questions. A question that never gets researched is just a well-written worry. This routine is the engine that moves the whole chain on a cadence — **loop → hypothesis → validation → the docs updated** — the same way dreaming moves thinking and the idea cycle moves ideas. Roll-up promotes, advance plans, validate resolves, and alignment folds what was learned back into what the brain believes.

## When it runs

**Weekly** as a scheduled routine, mid-week on purpose: Monday's refresh and idea cycle feed it current docs, and Friday's `self-improve` then curates the week's finished findings into durable learning. Also runnable on demand whenever the user wants the research worked.

## The method it runs on

The lifecycle, the four territories, the six pulls, and the four validation states live in `parker-system/system/open-loops-system.md` — read it before anything resolves. The three working pieces are already in this repo: the roll-up prompt at `parker-system/prompts/open-loops/open-loops-roll-up.md`, and the `open-loops-advance` and `open-loops-validate` skills in `.claude/skills/`. This routine orchestrates them in order; it does not re-invent their methods.

## The six steps of the weekly pass

### 1. Roll up — collect, kill, score, promote

Run the roll-up prompt: gather every open loop across the context docs, `open-loops/`, and dreaming's captured proposals; kill what doesn't deserve research; re-formulate; score on Stakes, Confidence, Researchability, Novelty; promote Tier-1 to the hypothesis queue, backlog Tier-2, archive the rest with reasoning. The roll-up prompt carries the full rubric — follow it exactly, never a summary of it.

### 2. Advance — promoted loops become hypotheses

For each promoted Tier-1 loop (and any Tier-2 the user activated), run the `open-loops-advance` skill: the question becomes a falsifiable prediction with a test plan Parker can actually run. Honor the skill's approval gate exactly as written — brand-routed and novel high-stakes loops go to `hypotheses/awaiting-user/` and into the digest; everything else proceeds on Parker's latitude, or waits if the user has set propose-first.

### 3. Validate — run the testing queue

This is the step that most needs a schedule, because it is the one nobody remembers to ask for. Run the `open-loops-validate` skill on **every hypothesis that is cleared to run** — proceeding on Parker's latitude, or approved by the user since the last pass. Each resolves honestly into its state: validated, invalidated, inconclusive, or insufficient evidence, filed with its closure document. Don't skip inconvenient verdicts; an invalidated hypothesis is a finding, not a failure.

### 4. Re-validate — nothing stays true forever

Check `re-validations/scheduled/` for any confirmed insight whose re-check date has passed (read today from `get_current_time`). Re-run those validations, file the outcomes in `re-validations/results/[YYYY-MM]/`, and treat a finding that moved as a fresh finding for steps 5 and 6.

### 5. Report — the research digest

One plain digest, in Parker's voice: what got promoted and why, what's waiting on the user (each with its one question), what resolved and to which state, what a finding means for the work, and what new loops the research itself opened. Findings carry their evidence and their marks; a verdict without its "therefore" isn't done.

### 6. Align the docs — the brain believes what the research found

A validated finding that never reaches the standing docs is drift by design: the validation folder says one thing while the brand profile, a persona, or a sub-context doc still says the old thing, and every later answer built on those docs repeats the outdated read. So close the loop:

- **Draft the alignment.** For each finding from steps 3 and 4 (validated, invalidated, or a moved re-validation), name every standing doc it touches — the brand profile, the sub-context slice, the persona, the voice-of-customer entry, the strategy doc — and draft the specific update, carrying the validation's ID, date, and verdict as provenance so the doc says *why* it changed. Brand-specific rules and hard-won do's and don'ts also land in the brand lens (`parker-system/creative-strategy-context/_<brand>-lens.md`), the designed home for this brand's tribal knowledge.
- **Get the agreement, then apply.** In an interactive run, present the drafted updates with the findings and apply what the user agrees to, on the spot. In a scheduled run with nobody there, file each drafted update as a pending proposal in `dreaming/proposals/pending/` (the context-update bucket) and flag it in the digest — `self-improve` disposes of it with the human in the loop, so nothing rewrites the brain silently. Two hard exceptions that always wait for the user regardless of latitude: anything touching `strategy/` (a finding that moves the roadmap is a strategy conversation, not an edit), and anything touching the brand hard rules.
- **Update the doc properly, not just textually.** A folded-in finding updates the claim and its mark (a validated claim is now **verified**, with its source), re-stamps the doc's `refresh_by` when the change is material, updates the doc's line in `running-notes/refresh-schedule.md`, and regenerates a folder INDEX if one is affected. When a finding reshapes a doc rather than amending it, recommend re-running the doc's generating prompt from `parker-system/prompts/` with the validation as context instead of patching it line by line.
- **Route the generalizable upward, don't write it here.** A lesson that is true beyond this brand belongs to the factory's knowledge layer, not this repo's craft docs — capture it as a promotion candidate via `self-improvement-intake`, and leave the shipped method docs untouched. Brand truth lives in the brand's docs and lens; product truth is promoted deliberately.

## Hard rules

- **Run the pieces, don't paraphrase them.** The roll-up prompt and the two skills carry the method; this routine sequences them. Full fidelity, per the brain's standing rule to never scope down a prompt.
- **Honor the gates.** The approval gate in advance, the user's latitude setting, and the always-ask exceptions in step 6 are not optional under a schedule. A scheduled run proposes where a human would be needed; it never substitutes for them.
- **Verdicts are honest.** The four states exist so a weak result has somewhere true to land. Never round inconclusive up to validated.
- **Alignment is provenance-first.** Every doc edit names the validation that caused it. No silent rewrites, ever.
- **Audits are snapshots — never retro-edit them.** A finding changes the standing docs, not the dated record of what an audit saw at the time.
- Honor the brand hard rules on anything that touches creative or claims.
- Self-contained: in-repo surfaces and live data only. No factory paths at runtime.

## Deliverable

The loop agenda rolled up and current, promoted loops advanced into hypotheses (with awaiting-user ones surfaced), the testing queue run with every verdict filed in its state, due re-validations done, the research digest delivered, and the standing docs aligned with the confirmed findings — applied where the user agreed, proposed where they weren't there to ask.
