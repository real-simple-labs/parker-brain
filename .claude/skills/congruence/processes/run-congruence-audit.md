# Run a Congruence audit

## Inputs

- The locked unit of analysis from `strategy.md`.
- The complete creative and customer-facing copy.
- Age, gender, or combined age-and-gender delivery with outcomes.
- Relevant brand strategy, personas, customer language, and performance targets when a Parker Brain is present.
- The exact destination URL, rendered mobile page, and page copy.

## Step 1: Build the ad audience assumption

Watch or inspect the complete ad before reading delivery. Capture:

- the problem, desire, trigger, or job named;
- the product, offer, promise, proof, and action;
- awareness level and assumed prior knowledge;
- the person shown, their apparent presentation, their role in the story, and whether they read as peer, authority, founder, caregiver, spokesperson, or contrast;
- voice, pace, language, setting, format, visual style, and accessibility signals;
- the person the ad appears to invite to say, `This is for me.`

Do not use the ad name or campaign taxonomy as evidence for the creative claim. When visual presentation is ambiguous, describe the signal rather than asserting an identity.

Compare the creative-implied audience with any stated audience from the brief or brand Brain. Keep the conflict visible.

## Step 2: Read actual delivery and performance

For the exact ad and date window:

1. Calculate each age-and-gender group's share of delivery using spend or impressions.
2. Read the objective outcome by the same groups. Use purchases, leads, qualified leads, landing-page views, or the actual optimization event rather than forcing purchase metrics onto every campaign.
3. Compare cost and rate metrics only when denominators and attribution match.
4. Separate the group receiving the most delivery from the group producing the best meaningful outcome.
5. Note low-volume groups and suppressed rows. Do not let a tiny group with one conversion become the winner.
6. Account for objective, budget, placements, account structure, auction conditions, and the breakdown effect before claiming the creative caused the distribution.

State what the data verifies, what it suggests, and what remains unresolved.

## Step 3: Inspect the landing-page experience

Follow the ad's actual URL through redirects. Inspect the rendered mobile page first, then desktop when it changes the experience. Read:

- first-screen headline, subhead, visual, person, product, offer, proof, and call to action;
- whether the same problem, desire, promise, product, and offer continue from the ad;
- whether the tone, language, awareness level, and amount of explanation fit the people receiving the ad;
- whether the page's imagery and social proof help the delivered audience recognize themselves or trust the claim;
- readability, contrast, type size, tap targets, load or interaction problems, and other friction that changes the experience;
- any destination mismatch, generic homepage handoff, missing offer, changed SKU, contradictory claim, or lost context.

Do not grade the whole website. Judge whether this exact page continues this exact ad for the people actually reaching it.

## Step 4: Score each seam

Use the anchors in `creative-strategy-context/congruence.md`. Scores may use one decimal when the evidence supports the distinction.

### Ad message and person shown, 20%

Judge whether the person, role, voice, setting, and primary visual make the message more believable and recognizable for the implied audience. If no person appears, use the primary visual subject.

### Intended audience and actual delivery, 30%

Judge how closely delivery concentration and meaningful outcomes match the audience the ad appears built for. Profitable spillover can be an opportunity rather than a penalty; score the clarity and consistency of the match, not obedience to the brief.

### Ad promise and landing page, 25%

Judge continuity of problem, desire, promise, product, offer, proof, tone, awareness level, and next action.

### Delivered audience and landing-page experience, 25%

Judge whether the page is easy to understand, trust, and use for the demographic groups that receive meaningful delivery and outcomes. Do not rely on age or gender stereotypes; point to the actual page and data.

For every score, cite two or three decisive pieces of evidence and one reason it is not higher. A score without those receipts is invalid.

## Step 5: Calculate the weighted score

Run the bundled `score_congruence.py` script with the four seam scores. Use the returned overall score exactly. Do not round it again or replace it with a label.

If any seam cannot be scored, do not run the calculator and do not issue an overall score.

## Step 6: Find the largest leak

Use weighted point loss, not the lowest raw score alone:

```text
weighted loss = weight × (10 - seam score)
```

The largest weighted loss is the first place to improve unless a legal, factual, or severe usability problem makes another fix more urgent.

Recommend the smallest change that repairs the seam. Examples include changing the person or first frame, making the message more specific, routing the ad to a matching page, carrying the promise into the first screen, changing the proof, or improving mobile readability. Do not prescribe targeting exclusions from age or gender alone.

## Step 7: Decide and build the mockup

Read the calculator's `landing_page_mockup_required` value. If it is `true`, or the page is a clearly generic handoff that drops the ad's core audience, promotion, product, or promise, run `build-landing-page-mockup.md` before formatting the final report. A score-triggered mockup is a required deliverable, not a suggestion.

If both landing-page seam scores are above 6.0 and no generic handoff is present, skip the mockup unless the user explicitly asks for one.

## Step 8: Format and source the report

Use `references/report-template.md`. Keep the score visible at the top. End with the exact tools, IDs, date window, attribution, URLs, creative sources, calculations, and limitations that shaped the result.

When `visuals.md` shaped the analysis, include its required closing line exactly once before the sources appendix: `this is based on everything I have learned about visuals in advertising`.
