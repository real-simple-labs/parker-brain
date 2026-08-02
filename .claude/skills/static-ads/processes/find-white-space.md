# Process — Find the White Space

Read the account for what it is **not** saying. This runs before any static is generated. The static worth making is the one that is missing, and that is a data question, not a taste question.

## When to pick

- **Always**, on any open ask. Also as a fast check when the user named a concept — a concept that duplicates a current top spender should be flagged before it is built.
- **Skip only** when the user has explicitly already done this read and handed you the gap.

## The four reads

Run all four. The fourth is the one most often skipped and the one that most often produces the finding.

### 1. Format concentration

Pull the account's statics over a 30–90 day window, sorted by spend, with AI format tags. Compute what share of static spend each format tag carries.

What you are looking for: concentration and absence. An account with two formats carrying 80% of static spend has real gaps. Note which proven formats from `static-ads.md` do not appear **at all** — absence is a stronger signal than low share, because it usually means the format was never tried rather than tried and beaten.

### 2. The asset check

For each absent format, ask whether the brand has an unusual asset that format would exploit. A brand with tens of thousands of reviews and zero testimonial statics is the clearest case — the review corpus is an advantage competitors cannot copy, sitting unused. Note the counts, with denominators.

An absent format with no asset behind it is a weak gap. Do not recommend a meme static because memes are missing.

### 3. Awareness and angle

Read the awareness-stage distribution across static spend. Accounts concentrated in solution-aware and most-aware have no acquisition statics — everything assumes the reader already knows the brand. That is the gap the stranger test exists to close.

Also read the angles the running statics work: which benefits, which objections, which use cases. Note what the reviews talk about constantly that no static mentions.

### 4. Demographics against the creative

**This read is mandatory and it is the highest-value one.**

Pull the spend distribution by age and gender. Then look at the actual top statics — who is depicted, what age they read as, what body they have, what situation they are in.

Compare the two. A mismatch means the media is already buying an audience the creative does not speak to. An account whose spend lands 70% on men over 45 while every static depicts a man in his twenties has a gap that no amount of format auditing would surface, and closing it usually costs nothing but a different model.

The same read applies to gender, and to platform when creative is placement-agnostic.

## Execution

1. Pull statics by spend with format tags, demographics, and awareness tags. Use a window long enough to be stable — 30 days minimum, 90 preferred.
2. Compute format share of spend, not share of ad count. Ten cheap tests and one scaled winner are not the same signal.
3. Look at the top statics themselves. Do not read tags alone — the demographic read requires seeing who is in the frame.
4. Cross-reference absent formats against the brand's assets.
5. Rank the gaps by the ordering in `strategy.md`.

## Output content

- Format concentration, with the share and the window. Name the absent formats.
- The asset check — which absences the brand is equipped to fill, with counts.
- Awareness distribution and the angles nothing is working.
- **The demographic-versus-creative read**, stated plainly, with the spend split and a description of who the top creative depicts.
- The ranked gaps, and which one this run will fill.

## What never to do

- Skip the demographic read because the format read already found something.
- Read share of ad count instead of share of spend.
- Recommend filling a format gap with no asset or evidence behind it.
- Report a gap without its denominator and window. "We under-index on testimonials" is not a finding; "zero of $41.3k in static spend over 30 days, against 41,883 reviews" is.
- Conclude from tags alone that you know who the creative depicts.
