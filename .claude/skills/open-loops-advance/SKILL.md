---
name: open-loops-advance
description: Turn a promoted open loop into a hypothesis — a falsifiable prediction plus the few complementary pulls that together settle it, triangulated across the ad account, reviews, and competitors as the question needs and runnable with Parker's tools. Use when advancing a Tier-1 (or activated Tier-2) loop from the open-loops roll-up into the testing queue, or when the user says advance the open loops, form a hypothesis, or plan how to test a loop.
triggers:
  - advance the open loops
  - advance this loop
  - form a hypothesis
  - turn this loop into a hypothesis
  - plan how to test this loop
  - what's the hypothesis on this open question
  - move the Tier 1 loops into testing
  - what should we investigate next
---

# Open loops — advance (loop → hypothesis)

## Goal

Take a loop the open-loops roll-up already promoted and turn it into a hypothesis: the loop's open question becomes a falsifiable prediction, and the **test that would settle it** — the few complementary pulls that each see a different angle, within Parker's reach — is named. The output is a short hypothesis document routed either to the user for approval or straight into the testing queue. The discipline is the strategist's cut on depth, not breadth: triangulate the full picture from a few sources, but don't over-build any one of them into a research study.

This is the middle stage of the loop-to-validation chain: **roll-up promotes → advance plans → validate resolves.** This skill does the planning only. It does not re-score the loop, and it does not run the research. If the loop has not been graded and promoted yet, that is the roll-up's job (`prompts/open-loops/open-loops-roll-up.md`); if the plan is ready to run, that is `open-loops-validate`.

## What you are working from

The full lifecycle, the four territories, the six pulls, and the four validation states are defined in `parker-system/system/open-loops-system.md` — read it before you plan. The senior-strategist frame that shapes a good hypothesis lives in `parker-system/creative-strategy-context/creative-strategy-fundamentals.md`. When the plan will lean on a research method — an ad-library read, a review mine, an organic read — load the method doc `parker-system/creative-strategy-context/expertise-routing.md` names for it, so the plan is built the way a strategist would actually run it.

## How this skill runs

1. **Load the canon and the brand.** Read `open-loops-system.md` (the lifecycle and the hypothesis + validation definitions) and `creative-strategy-fundamentals.md` (the strategist's frame). Pull the brand-profile and the loop history in `open-loops/promoted/` and `open-loops/archived/`, so a loop already moving through the pipeline is not re-opened and an archived dead-end is not re-litigated. No hypothesis is formed without this loaded.

2. **Take the promoted loop, do not re-grade it.** Read the loop from `open-loops/promoted/[YYYY-MM]/` or the Tier-1 list of the latest `[date]-consolidated-roll-up.md`. Carry forward its four parts verbatim — the observation, the pull named and described, the exact question, the justification — plus its territory, its score, and the stated/inferred/verified marks on its evidence. The roll-up already decided this loop is worth running; the score is inherited, never recomputed here.

3. **Turn the question into a falsifiable prediction.** The loop's open question becomes a prediction the research can confirm or refute, stated plainly. "Does a GLP-1 actually cause bloating?" becomes "A GLP-1 does cause bloating, and our product would reduce that effect, which would make it an angle worth promoting." The prediction is Parker's, marked as a hypothesis, never as a fact, and it has to be falsifiable — if no evidence could come back that proves it wrong, it is not a hypothesis yet.

4. **Design the test — triangulate the full picture, not a single pull and not a research study.** See `processes/build-the-test-plan.md`. Pick the few complementary sources that each add a *different* angle — typically the ad account (what the brand has run), customer reviews (whether the demand is real), and competitors (whether it works in market), as the question needs. No single source sees the whole thing, and the ad account is blind to what it has never tested, so a question about whether something is a *good opportunity* almost always needs reviews or competitors alongside the account. The cut is depth, not breadth: read each source at the depth its angle needs and stop — no confound-separations, time-series, or mechanism sub-studies piled onto one pull. Read the evidence against the prediction as hard as the evidence for it, in the same sources. If the loop could only be settled by something Parker cannot reach, mark it unvalidatable rather than faking a plan.

5. **Run the approval gate.** See `processes/the-approval-gate.md`. Brand-routed loops and novel high-stakes loops whose plan needs the user go to `awaiting-user`; otherwise Parker proceeds on its own latitude and the hypothesis enters the testing queue.

6. **Write the hypothesis document and route it.** Use the output spec below. Route to `hypotheses/awaiting-user/[YYYY-MM]/` when it needs the user, or leave it ready for `open-loops-validate` when Parker is proceeding.

## Output

A **short** hypothesis document at `hypotheses/awaiting-user/[YYYY-MM]/[loop-slug].md` (awaiting approval) or the testing queue (proceeding). A strategist's one-pager, not a research brief — if it runs much past a page, it is overcomplicated. Lead with the prediction.

```markdown
---
brand:
doc: hypothesis
source_loop:
territory:
score:
state: awaiting-user | proceeding
last_updated:
---

# Hypothesis — [the prediction in one line]

## The prediction

## The test

## What each outcome would mean
```

**The prediction** is one or two sentences — the bet, marked as Parker's. **The test** is the few complementary pulls that together settle it — the ad account, reviews, competitors as the question needs — each naming its Parker tool and the specific pull, with the disconfirming read folded in. A few clean angles that see the full picture, not a single source and not a numbered multi-step study. Reference the source loop by its id in frontmatter; do not reproduce it verbatim. **What each outcome would mean** states, before any research runs, what evidence makes this **validated**, **invalidated**, **inconclusive**, or **insufficient** — a line or two each, so the validation step has a bar set honestly in advance.

## Hard rules that override anything else

1. **Do not re-grade.** The roll-up owns scoring, tiering, and the kill list. This skill inherits the score and plans; it never recomputes the weight or re-opens the verdict.
2. **Do not run the research.** Forming the plan is the job. Running it is `open-loops-validate`. A hypothesis doc that already contains findings has skipped a stage.
3. **The prediction must be falsifiable.** If nothing could come back that refutes it, it is not a hypothesis.
4. **The plan must be within Parker's reach, or the loop is marked unvalidatable.** A plan that depends on a real-world test or proprietary data Parker cannot get is named as such, not faked.
5. **Triangulate a few complementary sources — not one pull, and not a research agenda.** See the full picture from a few different angles — the ad account (what's been run), reviews (whether the demand is real), competitors (whether it works in market) — because one source has blind spots and the account cannot speak to what it never tested. The failure mode is over-engineering, not breadth: a single pull split into six steps of confound-separations, time-series, and mechanism sub-cuts. Cut the over-engineering; keep the triangulation.
6. **Look for what would prove you wrong — inside the test, not as a separate study.** The test reads the evidence against the prediction as hard as the evidence for it, in the same pull. That is a lens on the direct test, not a multi-pull sub-study bolted on.
7. **One hypothesis per loop.** If the loop turns out to carry two predictions, it was two loops — split it and send the second back to the roll-up rather than stacking them here.
8. **Carry the marks.** A prediction built on an inferred loop is itself inferred. Never launder the loop's uncertainty into a confident hypothesis.
