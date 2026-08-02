# Process — Judge the Render

Grade the finished image against the quality checklist. **A spec passing is not the render passing** — the whole failure mode this catches is a well-reasoned static that renders with the logo enormous and the hook buried.

Run this on every produced asset, before it goes anywhere.

## The posture

Judge the image as a stranger scrolling, not as the person who designed it. You know what the hook is meant to be; the render either makes that land or it does not. Grade what is in front of you.

Be willing to fail it. A judge that passes everything is decoration.

## The checklist

The canonical list is in `static-ads.md`. Applied to a render:

**Design — the half a spec cannot test**
- Look at the image and name what the eye hits first. Is that the intended hook? If it is the logo, the proof strip, or the product, the render failed regardless of the spec.
- Does the actual read order match the designed one?
- Is every word legible in one pass at feed size? Check at phone scale, not full size.
- Do the levers land — is the hook genuinely largest, is the contrast doing its job, has the white space survived?
- Did the model add anything that was not asked for? Invented badges, garbled text, extra copy, stock-photo affect.
- Are hands, faces, text edges, and product details rendered cleanly enough to run?

**Message**
- Does the headline still pass the stranger test as rendered — including any truncation or line breaking the render introduced?
- Is the copy exactly what was specified, unparaphrased? Image models silently rewrite text.
- Is the clarity-or-curiosity call still legible in the finished thing?

**Integrity**
- Does every stat, claim, and quote on the finished image trace to a verified source?
- Are the compliance rails intact in the rendered copy?
- Is the depicted person, setting, or product within the brand's visual vocabulary, or flagged?

## Execution

1. **View the render.** Actually look at it. A judge that reasons from the prompt rather than the image is judging the spec again.
2. **Name the first-landing element before checking anything else**, so the answer is not contaminated by knowing the intent.
3. **Run the three sections.**
4. **Verdict: ship, fix, or rebuild.**
   - *Ship* — passes all three.
   - *Fix* — a specific, nameable defect with a specific remedy. Say which lever to change.
   - *Rebuild* — the render misunderstood the concept, or the concept fails as an image.
5. **On a fix, name the change, not the dissatisfaction.** "Increase the quote to roughly twice the attribution size" is actionable; "the hierarchy feels off" is not.

## Output content

- What the eye lands on first, stated plainly.
- Pass or fail per section, with the specific failures named.
- The verdict, and for a fix, the exact change.
- Anything the model invented or garbled.

## What never to do

- Judge the prompt instead of the image.
- Pass a render because the reasoning behind it was good.
- Report "looks good" without naming what the eye hits first.
- Give a fix as a feeling rather than a change.
- Skip the legibility check at feed size.
- Let silently rewritten copy through — image models change words, and a paraphrased customer quote breaks the rule the whole static rests on.
