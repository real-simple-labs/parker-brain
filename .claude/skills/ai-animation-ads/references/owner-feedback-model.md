---
summary: "The owner-preference model (RLHF corpus) TEMPLATE: how each brand brain learns its owner's taste. Every graded feedback event from the brand's owner gets appended same-session; the creative-critic agent reads this file to predict the owner's grade BEFORE delivery. Ships empty of brand data; seeds itself from the first real feedback."
---

# Owner Feedback Model (the RLHF corpus)

**RULE:** This corpus is append-only, living, and PER-BRAND. Every time the brand's owner grades or corrects creative work, add an event entry THE SAME SESSION: date, format, the verdict verbatim, root cause, the fix that passed, the generalized rule. The `creative-critic` agent reads this file before grading anything; a stale corpus is a blind critic. This template ships with no brand data: the brand's own corpus grows here from its first delivery onward.

**How the loop works:** generate → internal gates → `creative-critic` predicts the owner's grade using this corpus + the doctrine docs → anything below predicted A+ gets revised or regenerated (max 3 iterations, then deliver best-with-flags) → the owner grades the delivery → their verdict is ingested here same-session. The owner IS the reward signal, permanently; the critic exists to catch obvious misses before delivery, never to replace the owner's grading. If the owner ever corrects the same thing twice, the corpus entry failed: strengthen it, don't apologize.

## Event schema (append under "Graded events")

`E<N> · <format tag> · "<owner's verdict, verbatim>" → <root cause>. Rule: <the generalized, brand-agnostic version of the lesson>.`

Format tags: static / video / copy / design / strategy / claims / process. When the owner REWRITES copy themselves, ingest it verbatim as an **A+ EXEMPLAR** with a one-line analysis of why it works: owner-written lines are the calibration gold standard.

## Graded events (per-brand; starts empty)

_(none yet: seed from the first owner feedback)_

## Starter rule set (production-derived, brand-agnostic; treat as active until the brand's own events override them)

- **Claims truth (SKU-truth gate):** any creative naming a specific ingredient, capability, or replacement must verify it is literally true of the SKU shown, at the level a label-reading buyer accepts. The comment section is the enforcement mechanism.
- **Motive truth:** an ad's emotional driver must trace to evidenced buy-motives (VoC, surveys, verified strategy concepts), never to psychology the strategist invented. If you constructed the motive, the ad argues with nobody.
- **Pattern-interrupt headlines** are the shortest possible curiosity bomb; the reveal lives in the body. Recreations keep the reference's MECHANICS, not just its layout.
- **Pixel-fidelity for native UI:** never freehand-draw OS chrome; composite onto a real template or generate the UI with the image model. Post-set text is for plates and photos, not for simulating operating systems.
- **The art-direction gate (type-led ads):** layout mechanics are not design. Specify the brand's color fields, typographic craft (display + pairing, tracking, scale contrast), texture and depth, and the product integrated (cropped, shadowed), never text floating on a void. Test: "would a senior brand designer put this in their portfolio?"
- **The hierarchy ladder is designed, not assumed:** rank every element (hook → reveal → punchline → product) and verify the visual weights produce that order; a heavy product mass can silently outrank the message. One accent treatment belongs on the money line; monochrome type does zero hierarchy work.
- **The hook rank is a copy decision:** the line that implicates the reader takes rank 1 in type; a beautiful money-shot visual supports it, never demotes it.
- **Visual metaphors must agree with the copy's semantics** (arrows, symbols, and order can silently reverse the claim), and the "before" side of any comparison must carry felt weight.
- **Field color is a stop-scroll decision:** light fields blend into light feeds; choose deliberately and test both.

## What owners consistently reward (update per-brand as evidence accumulates)

Whitespace with structural ownership over me-too polish · lines a media buyer would screenshot · one-glance clarity · real customer language TRANSFORMED through doctrine, never transplanted · receipts (ranks, CPAs, denominators, lineage) · autonomy that delivers finished, gated work · every lesson permanently encoded the same session.

## The critic's standing objection checklist (predict these before the owner says them)

1. "Would a media buyer screenshot this line?" (copy below A+)
2. "Why this format / why this messaging?" (unjustified selection)
3. "Is that reference actually good, for OUR buyer?" (reference-fit scorecard)
4. "That's hard to read / takes effort" (one-channel, one-second)
5. "That looks AI" (perfection kill, reality pass, AI-isms)
6. "That number argues against you" (self-defeating stats)
7. "Is this what the field is already doing?" (whitespace check)
8. "Did you read the knowledge doc for this?" (routing: if a doctrine doc exists for the task, it must be loaded and cited)
9. "Are these real people / real quotes?" (talent + attribution rules)
10. "Did you encode the lesson?" (skill/corpus updated same session)

## Calibration ledger (the get-better-over-time metric; per-brand, starts empty)

Every delivery appends one row AFTER the owner responds: batch, per-artifact critic predictions, the owner's actual verdict, HIT or MISS. A MISS means the corpus failed: same session, write the missing rule as a new event and note which checklist item should have caught it. Metrics audited by the brain's weekly self-improve pass: **agreement rate** (critic vs owner), **first-pass A+ rate**, **repeat-correction count** (target: zero, always).

| date | batch | critic predictions | owner verdict | hit/miss | corpus action |
|---|---|---|---|---|---|

## Weekly tuning (wire into the brain's self-improve schedule)

Each pass: (1) audit the ledger, compute the three metrics, log the trend; (2) promote CANDIDATE RULES from critic outputs into numbered events; (3) tighten any rule that produced a MISS; (4) check the brand's whitespace map refresh triggers; (5) prune rules the owner has overridden. The corpus is a model: it gets trained weekly or it decays.
