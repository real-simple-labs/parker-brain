---
name: open-loops-validate
description: Run a hypothesis's test plan, gather the evidence, and honestly resolve the loop into one of the four validation states — validated, invalidated, inconclusive, or insufficient evidence. Use when a hypothesis is approved or proceeding and it is time to test it, or when the user says validate this, run the test, close the loop, or what did the research find.
triggers:
  - validate this hypothesis
  - run the test plan
  - close this loop
  - what did the research find on this loop
  - resolve the open loop
  - run the validation
  - is the hypothesis true
  - test the prediction
---

# Open loops — validate (hypothesis → validation)

## Goal

Run the plan in an approved hypothesis, gather the evidence honestly, and resolve the loop into one of four states: **validated**, **invalidated**, **inconclusive**, or **insufficient evidence**. Write the closure document, file it under the state it landed in, tell the user what was found, and — when the loop validated — add the confirmed insight to the brand profile and schedule its re-validation.

This is the final stage of the loop-to-validation chain: **roll-up promotes → advance plans → validate resolves.** This skill runs the plan and answers the question. It does not form the hypothesis or build the plan — that is `open-loops-advance` — and it does not re-open a resolved loop except through `re-validation`.

## What you are working from

The four states, re-validation, and the file system are defined in `parker-system/system/open-loops-system.md` — read it before resolving anything. The hypothesis doc carries the prediction, the plan, and the evidence bar that was set before any research ran; that bar is the standard you resolve against. When the plan works a source through a method — a review mine, an ad-library read, an organic read — load the method doc `parker-system/creative-strategy-context/expertise-routing.md` names for it, and run the source the way that method says to. Every tool the plan calls must be one Parker can actually pull, per `parker-system/system/parker-tools.md`.

## How this skill runs

1. **Load the canon, the brand, and the hypothesis.** Read `open-loops-system.md` (the four states) and the hypothesis doc — its prediction, its plan, and its pre-set evidence bar. Pull the brand-profile so the finding lands in context. No validation runs without the hypothesis's own bar in hand.

2. **Run the plan, in its order, capturing the evidence exactly.** Work each source the plan names. Capture the evidence the way the finding will have to be defended: the exact phrase a customer used, with its source and date, never a paraphrase of the theme; the count with its denominator and window; the named example described richly enough to replay. A validation built on "customers often mention bloating" cannot be checked; one built on the exact quotes, their count, and where they came from can. This is the verbatim standard, and it is what makes a closure document worth adding to the brand profile.

3. **Run the reverse-evidence step.** The plan included a step that looks for evidence *against* the prediction. Run it as hard as the steps that look for evidence *for* it, and weigh the two honestly. The size of each side — not the side Parker hoped for — decides the state.

4. **Resolve the state against the pre-set bar.** See `processes/resolve-the-state.md`. Measure what the evidence shows against the bar the hypothesis set in advance. Do not move the bar to fit the finding. Inconclusive and insufficient are real, honest outcomes, not failures to be dressed as wins.

5. **Write the closure document and file it.** See `processes/the-closure-document.md`. File it under `validations/[state]/[YYYY-MM]/`.

6. **Implement the finding, spawn the next loops, then inform.** This is the last stage. Based on the finding, go through the brand's docs and make any change it requires, referencing each change and why, citing the validation. Let the finding decide what gets touched: a contradicted recommendation gets corrected in place, the confirmed or refuted insight lands in the always-loaded `brand-profile.md`, and point-in-time audits are left to regenerate on cadence. Change what the finding actually bears on, nothing it doesn't. Then close the cycle: surface the new open loops the finding opens — a result measured in aggregate that may not hold per segment, a mechanism implied but not tested, the next move it raises — and capture them as fresh loops for the next roll-up. Write them to the open-loops generation rubric, not as mini-hypotheses: a loop born from a finding tends to come out test-shaped, so force it back to an open question — What, Why, How, Who, or Where, with the answer not built in — observation first, with no test design and no closure path. Add the resolution to `running-notes/recent-validations.md`, naming the loops it spawned. Either way, tell the user what was found and why, and show them the document.

7. **Schedule re-validation.** See `processes/re-validation.md`. A validated insight is stamped with how fresh it is and when it should be re-checked, so Parker never assumes a past validation holds forever.

## Output

A closure document at `validations/[validated|invalidated|inconclusive|insufficient-evidence]/[YYYY-MM]/[loop-slug].md`. Lead with the finding and the state.

```markdown
---
brand:
doc: validation
source_loop:
source_hypothesis:
territory:
state: validated | invalidated | inconclusive | insufficient-evidence
validated_on:
revalidate_by:
---

# Validation — [the finding in one line] · [STATE]

## What we found

## The evidence

## Evidence against, and how it weighed

## Why this is the verdict
```

## Hard rules that override anything else

1. **The honest answer beats the clean one.** Resolve to the state the evidence supports, not the one that closes the loop neatly or confirms the bet. A forced "validated" poisons every decision built on it.
2. **Do not move the bar.** The hypothesis set what would count as each state before the research ran. Resolve against that bar exactly.
3. **Capture verbatim, never generalized.** Exact phrase, count with denominator and window, named example — the evidence is the quotes and the numbers, not a summary of them. A finding the reader cannot check is not a finding.
4. **The reverse-evidence is weighed, not skipped.** The state reflects the balance of evidence for and against, honestly measured.
5. **Inconclusive and insufficient are valid outcomes.** Strong-both-ways is inconclusive; too-little-data is insufficient. Neither gets dressed as a soft yes.
6. **Only a validated insight enters the brand profile.** Invalidated becomes a known dead-end; inconclusive and insufficient stay in the validations tree. Never promote an unconfirmed finding into the always-loaded profile.
7. **Carry the marks and the freshness.** The confirmed insight carries the evidence's marks and a re-validation date. Nothing is validated forever.
