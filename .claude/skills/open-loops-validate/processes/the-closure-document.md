# The closure document

The closure document is the record of what the research found and why the loop resolved the way it did. It is written so a reader who never ran the research can trust the verdict, and — when validated — so the insight can move into the brand profile intact.

## What it carries

- **The finding and the state, up front.** One line: what we now know, and which of the four states the loop landed in.
- **The evidence, verbatim.** The exact quotes with their source and date, the counts with their denominators and windows, the named examples. This is the body the verdict rests on. A closure doc that summarizes its evidence instead of showing it cannot be checked and should not enter the brand profile. Write it as prose, never a table: name each cohort or metric, give its number with the unit, and carry the contrast in the same sentence.
- **The evidence against, and how it weighed.** What the reverse-evidence step found, and why the for-evidence outweighed it, or did not. Skipping this is how a forced validation hides.
- **Why this is the verdict.** The reasoning that connects the evidence to the state, measured against the hypothesis's pre-set bar.
- **Provenance and freshness.** The source loop, the source hypothesis, the date validated, and — when validated — the re-validation date.

## Where it goes, and what it updates

File the document under the state it landed in: `validations/validated/[YYYY-MM]/`, `validations/invalidated/[YYYY-MM]/`, `validations/inconclusive/[YYYY-MM]/`, or `validations/insufficient-evidence/[YYYY-MM]/`.

Then propagate by state:

- **Validated** → add the confirmed insight to `brand-profile.md`, carrying its verbatim evidence and its date, and add a line to `running-notes/recent-validations.md`. This is the only path by which a finding enters the always-loaded profile. Mark it the way the evidence earned — verified where the data is direct, inferred where the read connects sources.
- **Invalidated** → record the known dead-end in the brand profile so the question is not re-opened blind, and note what evidence closed it.
- **Inconclusive / insufficient** → stay in the validations tree. They do not touch the brand profile, because nothing was confirmed. They remain available so a later pass inherits the reasoning rather than starting cold.

## Tell the user

Whatever the state, bring it back to the user plainly: here is what we set out to test, here is what the research found, here is the verdict and why. Show them the document. A validated insight is good news delivered with the evidence; an invalidated one is delivered just as plainly, with the dead-end named so the brand stops spending attention on it.
