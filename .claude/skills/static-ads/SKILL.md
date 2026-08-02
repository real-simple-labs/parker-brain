---
name: static-ads
description: The full flow for making static ads — find the white space in the account, pick a proven format, write the message from real customer language, design the visual hierarchy, and produce the asset. Use when the ask is "make me a static", "what statics should we make", or a specific static concept needs building.
triggers:
  - make me a static
  - make some statics
  - create static ads
  - what statics should we make
  - we need new statics
  - static ad ideas
  - build a static for this angle
  - design a static
  - what static should we test next
  - recreate this static for us
  - our statics aren't working
  - we need top of funnel statics
  - fill the gaps in our static rotation
  - turn this review into a static
---

# Static Ads

## Goal

Make static ads that work on people who have never heard of the brand. The flow runs in three phases — decide what static the account is missing, write the message from what real customers said, then design and produce it so the message actually gets read.

This skill owns the whole loop, including production. It calls into other skills for the parts they own rather than re-implementing them.

## What this skill does not own

- **Headline craft** → the `headlines` skill. This skill decides what the headline must *do*; `headlines` writes the line.
- **Image-model prompt construction** → `ai-ad-generation`. This skill produces the static spec; that skill turns a spec into prompt text.
- **Iterating a proven winner** → `iterations`. If the ad already works and the ask is to extend it, that is a different job.
- **Diagnosing account performance** → `ad-account-analysis`. This skill reads the account for *gaps*, not for a performance verdict.
- **Video** → `scriptwriting`, `hooks`, `ai-ad-generation`.

## Which phase to enter

- **Open ask** — "make us some statics," "what should we test," no concept named. Start at **Phase A**.
- **Concept named** — the user has the angle, the review, the competitor ad, or the format. Skip to **Phase B**, but still run a fast white-space check so the concept is placed against what is already running.
- **Spec in hand** — the static is already specified and the ask is to build it. Go to **Phase C**.

## What you are working from

The craft is canonical, not improvised. Reason in these docs' named concepts — work that never speaks their vocabulary proves they were not opened.

- `global/knowledge/creative-strategy/static-ads.md` — **the doctrine, and the spine of this skill.** The proven format set, the assume-no-one-knows-or-cares test, customers-as-copywriters, the clarity/curiosity call, the visual-hierarchy principles, and the quality checklist. End any output that used it with its required line.
- `ad-account-analysis.md` and `ad-account-analysis-method.md` — Phase A. Reading the account, including the demographic breakdown the white-space read depends on.
- `public-ad-library-analysis.md` — Phase A. Impression rank as a proxy, and what it does and does not support.
- `customer-review-mining-method.md` — Phase B. Golden nuggets, denominators, the two governors on every nugget.
- `ad-formats/static/index.md` and `ad-formats/both/index.md` — both phases. Name real format tags; do not invent blends.
- `static-ad-recreation.md` — when the play is recreating a specific external static.
- `ai-static-ad-generation.md` — Phase C. The prompt-template library.
- `visual-vocabulary-method.md` — Phase C. In-play / adjacent / out-of-play. A static that only works over an invented shot is not grounded.
- `lifestyle-headline-generator.md` / `problem-solution-headline-writer.md` — routed by brand type when the headline is written.

Account data, reviews, comments, and the external library pull through the Parker tools inventoried in `system/parker-tools.md`.

---

## Phase A — Find the white space

Never open with "what static would be good." Open with "what is this account not saying."

1. **Load brand context.** Brand profile, ICP and personas, voice of customer, brand voice, compliance, calendar. No output without this loaded. Where the brand vault is thin or absent, say so — the output is weaker and the user should know which parts are ungrounded.

2. **Read the account for gaps.** Run `processes/find-white-space.md`. It covers all four dimensions — format, persona, angle/awareness, and the demographic-versus-creative read. Do not skip the fourth; it surfaces findings the others structurally cannot.

3. **Read what is working elsewhere.** Pull the top statics of tracked competitor, inspo, and affinity brands by impression rank. Run `processes/reverse-engineer-winning-static.md` when a specific external static is worth rebuilding.

4. **Name the play and checkpoint.** State the gap, the format that fills it, and the persona it serves — two to four sentences, before building anything. This is a human-in-the-loop moment. Skip only when the user asked to run straight through.

## Phase B — Write the message

5. **Pick the idea source.** Run `strategy.md`. It routes between the customer-language path, the recreation path, the persona path, and the visual-invention paths.

6. **Execute the chosen process.** Each process in `processes/` carries its own playbook and required inputs.

7. **Run the assume-no-one-knows-or-cares test on every headline candidate.** A stranger to the brand must find it immediately relevant. Candidates that fail die here, however good they sound.

8. **Make the clarity-or-curiosity call explicitly.** Name where the selling happens — on the ad, or after the click. Do not leave it implied.

## Phase C — Design and produce

9. **Design the hierarchy.** Run `processes/design-the-hierarchy.md` on every static, without exception. It sets the read order and assigns the three levers. A spec that lists copy and product without a read order is not finished.

10. **Ground the visual.** Source the frame from the brand's visual vocabulary. Mark anything out-of-play as a production dependency, in plain terms — a shot the brand does not have is a real cost, not a footnote.

11. **Produce the asset.** Run `processes/produce-the-static.md`. It renders through a connected image-generation MCP when one is available and degrades to prompt text when not, naming what is missing either way.

12. **Judge the render.** Run `processes/judge-the-render.md` against the finished image. Grading a spec is not grading a static.

13. **Deliver.** `processes/deliver-to-slack.md` when the user wants it in a channel.

---

## Output structure

### The Static

For each static:

- **The play** — the gap it fills, in one line. Format tag, persona, awareness stage.
- **The copy** — every word that appears on the ad, exactly as it will appear. Headline, supporting lines, attribution, proof strip, CTA if there is one.
- **The source** — where the copy came from. The review, the comment, the competitor ad, the winning headline it adapts. Named, quoted, dated. Every static traces to something real in this account.
- **The read order** — what the eye lands on first, second, third, and which of the three levers enforces each step.
- **The frame** — what is depicted, sourced from the visual vocabulary, with out-of-play elements flagged.
- **Aspect ratio** and placement.

### White Space Read

Two to four sentences on what the account is and is not running — the format concentration, the demographic-versus-creative read, and the gap this static fills. Quantify: the number, its denominator, the window.

### Production Notes

What it takes to actually make this. Whether the asset was rendered or specified, what shots are missing, what stats need verifying.

### Brand Context Applied

- **What I used:** ICP, personas, customer language, voice of customer, brand voice, compliance, calendar.
- **What I avoided:** compliance walls, forbidden terms, off-brand language. If a request would have violated compliance, name what was flagged and what was offered instead.
- **Why this fits:** two to four sentences on the brand's current creative moment.

End with: *"This is based on everything I know about making static ads"*.

### How many

If the user named a number, use it. Otherwise default to three, each filling a different gap. If only N are genuinely strong, give N and say why you stopped. Padding wastes production budget.

---

## Hard rules

- **White space first.** Never generate before reading what the account is missing. The static worth making is the one that is not already running, and that read is not optional.
- **Read demographics against the creative.** Who the spend reaches versus who the creative depicts. This is the highest-value finding the read produces and it is invisible to a format-only audit.
- **Every headline passes the stranger test.** Immediately relevant to someone who does not know or care about this brand. The narrow exception is a deliberate bottom-funnel offer static.
- **Never paraphrase a customer.** Golden nuggets go on the ad as written, ungrammatical and all. Tidying a customer's line into brand voice destroys the reason it works.
- **Verbatim quote formats are exempt from the headline word cap.** The under-ten-words rule governs headline-led formats. A testimonial carries the customer's sentence at the customer's length; trimming it to fit the cap is paraphrasing, which is forbidden. Let the design carry the length.
- **Pick clarity or curiosity, and say which.** The middle is no man's land.
- **Every static has a designed read order.** Hook, qualifier, product, proof — or another order chosen on purpose. Copy plus a product shot is not a static.
- **Use proven formats, named by their tag.** No invented blends. Message beats format; do not spend the effort there.
- **No fabricated stats, percentages, or claims.** Everything traces to brand context, reviews pulled via tools, ad comments, or user-provided data. If a number would help and none is verified, write `[STAT NEEDED — verify before publishing]` and leave the gap. A review count you did not pull is not a verified review count.
- **Compliance is a wall, not a guideline.** Forbidden terms stay forbidden even when asked. Push back, explain, offer a compliant alternative with the same strategic intent.
- **Flag out-of-play visuals as production dependencies.** A static requiring a shot the brand has never taken carries a real cost. Say so plainly rather than burying it.
- **Prose, not grids, and replay every ad.** No tables in output. Describe every static — the brand's and the competitor's — narratively, in the order the eye takes it, so a reader who never saw it can picture it.
