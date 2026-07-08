---
trace_id: 2026-07-03-grounding-check-facts-not-flavor
date_captured: 2026-07-03
source: brand_output_review
source_ref: Jimmy watched the grounding gate bounce a TPJ script 3 times / ~5 min trying to trace every customer-voice line to an exact source
trigger_type: correction
scope: skill
brand: global
team: creative-strategy
confidence: strong
status: applied
target_surfaces:
  - .claude/agents/context-grounding-review.md
  - scripts/grounding-check.py
  - .claude/skills/scriptwriting/SKILL.md
  - .claude/skills/headlines/SKILL.md
  - .claude/skills/hooks/SKILL.md
  - .claude/skills/ai-ad-generation/SKILL.md
  - .claude/skills/iterations/SKILL.md
promotion_condition: already applied — explicit correction and approval in the same session
---

**What happened:** The grounding gate bounced a script three times over ~5 minutes trying to prove every customer-voice line traced to an exact source. Two of the three bounces were false: the model pulled real ad lines live, but the pull-log receipt hook isn't wired in that brain, so the gate saw the quotes as fabricated. Jimmy: chill on verbatim source-tracing — as long as a line sounds like a real review / Reddit / comment and we label it as not-a-verified-quote, that's fine. But one bounce was a real catch: a wrong waist-size floor (26 vs 28 for the built-guy fits) — a fact.

**Decision context:** The line that matters is facts vs flavor. Facts — numbers, sizes, specs, prices, named results, product/health claims — must be right and trace; the wrong-size catch is exactly what the gate is for, and it stays strict. Customer-voice flavor — review/comment/thread-sounding lines — no longer bounces for being untraceable; it is accepted if it reads authentic and fits the brand register, and the output labels it illustrative in one line so no made-up quote runs as a real testimonial (which also covers the compliance risk of fake testimonials). This also dissolves the missing-receipt false-bounce entirely: if voice lines don't need a receipt, the absent pull log stops causing bounces. `grounding-check.py` now treats untraced quotes as a labeling note, not a counted finding; the agent bounces facts, not flavor, and its return shape splits FABRICATED FACTS (bounce) from UNVERIFIED VOICE (label). Applied to all five creative skills. The peer-strategist method-doc read stays — Jimmy's complaint was the line-by-line verbatim tracing, not the quality review.

**Why it matters:** A gate that blocks for five minutes over the source of a review-flavored sentence trains people to turn it off. Pointing it at facts keeps the value (a wrong number is a real miss) and drops the paranoia (an illustrative voice line, labeled, is honest and useful). Speed and trust both recover.

**Inferred rule:** Verification effort follows stakes. Facts get checked hard; voice/flavor gets a plausibility-and-label pass, not a source hunt. A verification gate that punishes unverifiable flavor as if it were an unverifiable fact is miscalibrated and will be bypassed.

**Scope judgment:** Facts stay strict across all creative skills; the illustrative-label requirement is a hard rule so voice lines are never silently passed off as real testimonials. Does not touch the voice gate (that was fine) or the method-doc reading (the quality half Jimmy asked for earlier).

**Routing:** Agent recalibrated (step 2 facts-vs-flavor, step 5 pulls-for-facts, split return fields, grounded definition), grounding-check.py softened, all five skills got the facts-not-flavor rule + illustrative-label output. Re-shipped to the TPJ brain same session. Factory canon on the creative-review-gates branch (PR #17).
