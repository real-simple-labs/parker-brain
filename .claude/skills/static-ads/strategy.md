# Static Ads — Strategy

This document picks which process to run for a given brand and request. The decisions compound: the white-space read constrains which format is worth making, the format constrains which idea path is available, and the idea path constrains what the design has to carry.

## What to load before deciding

- **The white-space read.** This loads first, before anything else. What the account runs by format, persona, awareness stage, and — critically — who the spend actually reaches versus who the creative depicts. `processes/find-white-space.md` produces it.
- **The running static corpus.** The account's top statics by spend, with their headlines, formats, and AI tags. What already wins here is the baseline.
- **The external library.** Top statics by impression rank from tracked competitor, inspo, and affinity brands.
- **Customer language.** Reviews, ad comments, post-purchase surveys. The raw material for every acquisition headline.
- Brand profile, ICP and personas, brand voice, compliance rails, visual vocabulary.

## Decision 1 — Is this a gap-fill or a concept build?

- **Gap-fill.** No concept named. The white-space read chooses the static. This is the default and the stronger path, because the reason to make the ad comes from the account rather than from taste.
- **Concept build.** The user named the angle, review, competitor ad, or format. Build what they asked for, but still run a fast white-space check — if the concept duplicates something already carrying spend, say so before building it.

## Decision 2 — Which gap is worth filling?

Not every gap is worth filling. Rank them:

1. **Demographic-versus-creative mismatch.** The spend lands on a cohort the creative never depicts. Highest value, because the media is already buying that audience and the creative is not speaking to them.
2. **An absent format the brand has unusual assets for.** A brand with tens of thousands of reviews running zero testimonial statics is leaving an asymmetric advantage unused — competitors cannot copy a review corpus.
3. **An under-served awareness stage.** Usually cold. An account concentrated in solution-aware has no acquisition statics.
4. **An absent persona** with real evidence behind it in reviews or surveys.
5. **A format gap with nothing behind it.** Real, but weakest — "we don't run memes" is not a reason to run memes.

## Decision 3 — Which idea path?

Pick the source before the format. A static grounded in something real beats a clever format built on air.

- **`static-from-customer-language`** — a golden nugget from reviews or comments becomes the ad. The default path when the brand has a review corpus. Strongest for testimonial and headline-led formats.
- **`reverse-engineer-winning-static`** — an external static holding a top impression rank is rebuilt with this brand's copy and proof. The default when the brand's own corpus is thin, or when a competitor has clearly found something.
- **`persona-static`** — one persona, named or shown, with the message built only for them. Use when the white-space read surfaced a persona or demographic gap.
- **`make-the-invisible-visible`** — a felt sensation from customer language rendered as an intentionally unrealistic visual. Requires the language to exist first. Strongest for problem/solution brands where the symptom is invisible.
- **`atypical-text-placement`** — the copy written on an unexpected but relevant surface. Requires a surface that makes obvious sense for the category.

More than one can apply. A persona static usually also runs the customer-language path for its copy.

## Decision 4 — Brand type and awareness

Inherited from the headline docs, and it governs the message.

- **Problem/solution.** The customer knows they have a problem. Name it in their words, agitate it, resolve it. Push for emotional depth beyond the surface symptom — what they cannot do because of it, and how it makes them feel about themselves.
- **Lifestyle.** The customer is not in pain; they want elevation, identity, belonging. Signal the tribe.

Awareness stage sets how much can be assumed. Cold and problem-aware statics carry the acquisition burden and need the stranger test most.

## Decision 5 — Clarity or curiosity

Make this explicitly and state it in the output.

- **Clarity** when the selling happens on the ad. The default for top-of-funnel statics.
- **Curiosity** when the ad's only job is the click and an advertorial or long primary text does the selling.

If you cannot say which one this static is, it is stuck in the middle and needs rebuilding.

## Decision 6 — Format

Only now pick the format, from the proven set in `static-ads.md`, named by its `ad-formats/` tag. The format should be the natural vehicle for the idea path already chosen — a golden nugget wants a testimonial or headline-led layout; a before/after wants a comparison; a felt sensation wants a generated hero image.

Do not spend creative effort here. Message beats format.

## The quality gate

Every static passes the checklist in `static-ads.md` before output — message, design, and integrity. `processes/judge-the-render.md` runs it against the finished image rather than the spec, which is the version that counts.

If a static fails the design half, it fails. Strong copy in a layout that buries it is a failed static.

## Common mistakes this strategy exists to prevent

- Generating before reading the account.
- Reading white space by format alone and missing the demographic mismatch.
- Filling a format gap that has no evidence behind it.
- Paraphrasing a customer's line into brand voice.
- Trimming a verbatim quote to satisfy a headline word cap.
- Writing a headline that assumes the reader knows the brand.
- Copying a competitor's surface instead of its mechanism.
- Leaving the clarity/curiosity call implicit.
- Shipping a spec with no read order.
- Generating an unrealistic visual with no customer language behind it.
- Treating a rendered asset as finished without grading it.

## Reasoning log

Static picks the user has accepted, rejected, or adjusted accumulate here as the loop runs. Over time this trains Parker on which gaps this brand considers worth filling, which formats land, and which customer phrasings convert.

*(No entries yet — populated by the fine-tuning loop.)*
