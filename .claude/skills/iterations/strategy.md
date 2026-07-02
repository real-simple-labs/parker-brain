# Iterations — Strategy

This document is how Parker decides which iteration processes to recommend for a given ad. It runs after brand context and ad data are loaded, and before any process file is executed. Its output is a diagnosis and a ranked list of iteration processes to run.

## What this document is for

Choosing iterations is a strategic decision, not a menu pick. The same ad can support very different iteration sets depending on the brand, the data, the iteration history, and what the brand defines as a "win." This document holds the reasoning Parker uses to make that call.

## What to load before deciding

The canonical creative-strategy reads behind this decision are inventoried in the skill's "What you are working from" section. The three that govern the diagnosis itself:

- `iterations.md` — the doctrine. The optimization hierarchy, the signal-change ladder, the dual-lens diagnosis, and the high-confidence list below all execute it.
- `ad-account-analysis.md` — the method that turns metrics into a read. The bottleneck call below grades against its floors, not against vague intuition: hook rate good above 30%, hold rate working at 12% and above, outbound CTR wanted above 1%, frequency 1.2 or lower before the ad is just re-serving the same people. It also names the top-spender-is-the-most-potent-ad principle and the warning that a high ROAS on low spend usually dries out fast — the higher-spend, lower-ROAS ad is the real winner to iterate on.
- `killer-performance-ads.md` — the bar the winner is graded against, so the working element you protect is the right one. Read the ad against the golden rules before deciding what not to touch.

Then load:

- Brand profile, competitive landscape, ICP/personas, voice of customer, marketing calendar, compliance rules.
- The ad itself — actually study it. Do not work from the metadata.
- Performance data: CTR, hook rate, hold rate, CvR, CPA, ROAS, spend, frequency.
- Iteration history if available. An ad that has been through five rounds of hook swaps has very different remaining opportunities than a first-time iteration.
- The user's KPI definition if known. "Lowest CPA at scale" and "highest ROAS on cold traffic" lead to different prioritization.

If performance data is missing, ask for it. If the user cannot provide it, you can still recommend creative-first iterations but flag in the output that adding data would meaningfully sharpen the recommendations.

## The dual-lens diagnosis

Every iteration recommendation comes from looking at the ad through both lenses simultaneously. Skipping either lens produces shallow recommendations.

### The data lens

Find the bottleneck. Read every metric through `ad-account-analysis.md`, against its floors — hook rate below 30% flags a stop-scroll problem, hold rate under 12% flags a body that loses people, outbound CTR under 1% flags a weak CTA or offer, frequency above 1.2 flags fatigue from re-serving the same audience. A metric is the bottleneck when it is the one sitting below its floor while the others hold. Internally answer all four questions before moving on. Do not put these in the output.

1. What is the main bottleneck — CTR, hook rate, hold rate, CvR, spend ceiling? Name the metric and where it sits relative to its floor and the account average.
2. Is the ad tailored to cold or warm traffic? The messaging will tell you. `killer-performance-ads.md` frames this as the awareness level the ad serves — unaware, problem-aware, solution-aware, product-aware, most-aware — which sets how far up the funnel an iteration can push.
3. Is the goal to scale further or regain efficiency? This changes which iterations make sense. Confirm the ad is a real winner first: per `ad-account-analysis.md`, the top spender is usually the most potent ad, and a high ROAS on low spend tends to dry out fast — do not iterate on a low-spend ad that just picked the low-hanging fruit.
4. What are the strongest working elements — hook, creator, message, format, visuals?

### The creative lens

Set the data aside for a moment. Watch the ad as a viewer encountering it in the wild. What is the angle? What is the hook doing? What emotional journey does it run? What human desire is it activating? What is the concept at its core?

Grade what you see against the killer-performance bar in `killer-performance-ads.md` — which emotion or mindstate the ad targets, the promise it makes, the proof it shows, whether it earns the first second, and whether it would convert a cold audience or only works because it is being served to warm, already-aware people. The element the ad nails against that bar is the one you protect. If the ad only works on warm audiences, that itself points the iteration toward broader hooks and more educational messaging to reach further up the funnel.

The creative lens prevents iteration paralysis — the failure mode where data-only optimization makes every iteration converge on the same narrow patterns and the entire account ends up looking the same.

### Working vs. underperforming elements

From both lenses, write down two internal lists. Do not output these.

- **Working elements** to preserve. Do not touch what works.
- **Underperforming elements** to iterate on. Be forensically specific. "The hook is weak" is not specific enough. "The hook visual is a talking-head in a kitchen that is not stopping the scroll, but the hook copy is strong because CTR is low while CvR is high" is.

## Common data patterns and where they point

These are diagnostic shortcuts, not rigid rules. They are the patterns named in `iterations.md`; read each through the `ad-account-analysis.md` floors above so "low" and "rising" mean a number relative to a benchmark, not a feeling. Always pair with the creative lens and brand context.

- **Low CTR, high CvR.** The message converts once engaged but is not earning attention. Iterate on hooks, headlines, visual attention-grabbers. The body is the strongest element — protect it.
- **Strong CTR, low hold rate.** The hook lands but something after it loses viewers. Look at pacing, length, the transition from hook to body, and whether the product introduction comes too late.
- **CPA rising over time.** Typically audience fatigue. Same people seeing the same creative too often. Reach new pockets — new creator archetypes, format changes, messaging angle shifts.
- **Frequency rising with ROAS declining.** Creative fatigue setting in. Creator iterations, format switches, messaging angle changes.
- **Good metrics, not scaling further.** The current audience-format combo is tapped. Break into new segments — format changes, archetype changes, awareness-level shifts.
- **High video completion, low CTR.** People watch but do not click. The content engages but the CTA or offer is weak. Try urgency, social proof, a stronger CTA, or ask whether the ad feels too much like content and not enough like a click-worthy ad.

## The optimization hierarchy

In the Andromeda era, the algorithm targets shopping behavior and interests on its own. That changes the order you should optimize in:

- **Level 1 — Theme.** The broad category your messaging lives in. Optimize within the theme first.
- **Level 2 — Angle.** The specific emotional or motivational lens inside the theme. Iterations that change angle stay inside the same theme.
- **Level 3 — Format.** Once angles within the theme are exhausted, change the delivery format.
- **Level 4 — Avatar.** The persona/creator demographic. Avatar changes last — the algorithm is now sophisticated enough to match the right audience if you provide the right puzzle pieces. Changing avatar too early effectively creates a new ad.

This hierarchy is the default operating sequence. The data overrides it when it should.

## The signal-change ladder

When choosing how big a swing to take, this is the magnitude of algorithmic signal each lever creates, from loudest to quietest:

- **Format.** Static to UGC to high-production video. Fundamentally changes how the algorithm classifies and serves the ad. Use when plateauing or when fresh distribution is the goal.
- **Vehicle.** Founder story, green screen, testimonial, listicle, podcast clip, reaction. Same message, different entry point. Use when scaling a proven message across new creative structures.
- **Persona.** Creator archetype swap. Shifts who the algorithm targets and how the audience relates to the ad. Use when expanding total addressable audience.
- **Hook.** A new opening can read as effectively new creative to the algorithm while preserving the converting body. Use when the ad is fatiguing but the core message still converts.
- **Messaging.** Script tweaks, CTA, copy adjustments. Smallest signal change. Pull this lever for fine-tuning, not for breaking into new territory.

The hierarchy guides strategic sequence. The ladder guides how big a swing each individual recommendation represents. Use both together.

## High-confidence-first selection

Some iteration types have historically performed more consistently than others. The first one or two recommendations should come from the high-confidence list IF they address the actual diagnosis. Do not pick from this list just because the iteration type is historically strong — it must match the diagnosis.

The historically high-confidence processes:

- `frankenstein-stitch` — winning hook from Ad A onto the body of Ad B. Lowest-risk because every component is already validated.
- `creator-reshoot-same-script` — proven script, new face. Hardest part is the script, and that is already solved.
- `format-swap` — winning message in a new format. The loudest signal lever on the ladder.
- `human-desire-swap` — swap the fundamental desire the ad activates while keeping product, format, and structure. The only high-confidence iteration that targets the emotional engine underneath the ad.
- `mashup` — combine best moments from multiple winners. Requires multiple winners to exist.
- `hook-iteration` — pulling specific high-confidence hook moves like hook headlines, open loop hooks, or hook stacking on a proven body.

Choose from the broader process menu (see INDEX) when the diagnosis does not fit any of these or when prior iteration history has already exhausted them.

## How to think about each process — the menu

Each process below has a "best for" and "worst for" so Parker can pick what fits the diagnosis. The full execution playbook lives in the process file itself; this section is the decision layer.

### frankenstein-stitch

- **What it does:** Lifts a proven hook from one winning ad and stitches it onto the body of another winning ad. Both source elements are already validated, so the risk is the seam, not the components.
- **Best for:** Multiple winners exist in the account. A clear hook-to-body pairing is identifiable. Energy, pacing, and visual style at the cut point are compatible. Low-to-medium effort, high reward.
- **Worst for:** Only one winning ad exists. No clean stitch point. The two source ads have clashing tone or visual energy at the proposed cut.

### creator-reshoot-same-script

- **What it does:** Sends the proven script to a new creator. Message is preserved; only the face changes. Can be the same demographic for a fresh face or a different demographic to reach a new archetype.
- **Best for:** Script is converting. Creator is fatiguing or the brand needs to test a new demographic against the same proven message. Medium effort, high reward.
- **Worst for:** Script itself is the bottleneck. Creator is clearly the strongest element and swapping risks killing what works.

### format-swap

- **What it does:** Take the winning message and rebuild it in a different format — video to static, static to video, video to carousel, static to motion. Loudest signal change on the ladder.
- **Best for:** Message is converting. Concept has not yet been tested in this other format. Need to break into new placements or refresh distribution. Medium effort, high reward.
- **Worst for:** Message itself is not yet converting. The brand has already tested the same message across formats without lift.

### human-desire-swap

- **What it does:** Identify the human desire the ad is currently activating — beauty, romance, power, family, status, belonging, curiosity, FOMO — and rebuild the same product/format/structure around a different desire. Steven Reiss identified 16 fundamental desires; this iteration targets the emotional engine while keeping every other element intact.
- **Best for:** Winning ad with a clearly identifiable single desire driving it. Brand has not yet tested other desires. Medium effort, high reward.
- **Worst for:** The current desire is the one the brand has built its whole positioning around. Cannot identify the current desire clearly enough to know what to swap to.

### mashup

- **What it does:** Combine the best moments from multiple winning ads into one compilation. Stack back-to-back; strip individual CTAs so they flow.
- **Best for:** Multiple winners already exist. Pace changes and social proof are an advantage. Medium effort, high reward.
- **Worst for:** Only one winner exists. The moments do not flow together energetically.

### hook-iteration

- **What it does:** Modify only the first three seconds while preserving the proven body. Covers hook headlines, hook visual swaps, hook stacking, open loop hooks, comment bubble hooks, format swaps within the hook, and the full 20-hook-format playbook.
- **Best for:** Body is converting (high CvR or high hold rate after the hook) but CTR or hook rate is the bottleneck. Or the ad is fatiguing but the core message still works. Low effort, high reward when chosen well.
- **Worst for:** The body itself is losing viewers — fixing the hook only delays the drop-off. The current hook is what is working and the rest is fatiguing.

### messaging-angle-iteration

- **What it does:** Keep visuals and structure mostly intact; rewrite the script around a different angle, awareness level, or framing. Includes problem agitation, problem swap, awareness-level shift, story arc, listicle structure, identity messaging, negative vs positive framing.
- **Best for:** Visuals work but the message is not converting. Need to address a different awareness stage or persona without rebuilding from scratch. Medium effort, high reward.
- **Worst for:** Message is already converting and the brand has not yet exhausted easier iterations.

### audience-iteration

- **What it does:** Audience-targeted creator changes that go beyond a same-script reshoot — demographic swap, authority vs peer creator swap, voiceover swap, aspirational vs relatable creator, persona variant, gender variant, language translation.
- **Best for:** Need to expand into a new audience segment. Creator is fatiguing across the current audience. Medium effort, high-to-medium reward.
- **Worst for:** Current creator is the driving element of performance. Brand has not yet tested same-script reshoots, which carry less risk.

### static-headline-iteration

- **What it does:** Headline-driven iteration on a static ad. Test a different headline structure — rejection, identity signal, metaphor, question, contrast, social proof, problem setup, badge value — while keeping layout and visual intact.
- **Best for:** Static ad. Headline is the bottleneck — current structure is feature-focused or stuck at surface-level emotional depth. Low effort, medium-to-high reward.
- **Worst for:** Visual is the bottleneck, not the headline. The current headline is converting and the brand has not yet tested supporting copy or layout changes.

### edit-pacing-iteration

- **What it does:** Low-risk edit refreshes. Pacing acceleration or deceleration, cold open, length trim, length extension, b-roll refresh, caption style, captions on/off, burned-in headline, music swap or removal, sound effect layering, ASMR treatment, press mention overlay.
- **Best for:** Quick refresh on a long-running winner. Mid-ad drop-off when pacing is the suspected cause. Want to add a low-effort lever to a recommendation set that also includes bigger swings. Low effort, low-to-medium reward.
- **Worst for:** Pacing or edit style is clearly not the bottleneck. The brand needs a bigger swing to break a real plateau.

## How to choose the recommended set

After diagnosis, choose the iteration processes that best fit. Apply these rules in order:

1. **Match diagnosis first.** Every recommendation must address the bottleneck or the strategic goal. If it does not, drop it.
2. **Protect working elements.** Do not iterate on what is converting. If the message converts, do not propose messaging changes as the first move.
3. **Lead with high-confidence when it fits.** If a high-confidence process matches the diagnosis, lead with it. Do not force it when it does not match.
4. **Mix at least one quick win.** Include at least one low-effort iteration that could move the needle — only if it makes sense for the diagnosis.
5. **Diversify across the hierarchy.** When recommending three or more iterations, ideally at least one addresses a different level of the optimization hierarchy than the others. Diversified tests give the brand more paths to learning.
6. **Look for Frankenstein opportunities before building net-new.** Before recommending anything that requires fresh production, check whether existing winners can be recombined.
7. **Match swing size to spend.** Ads with a large amount of spend typically need bigger swings — the audience has been saturated and small tweaks will not move the needle. Quickly scaling ads benefit more from smaller, lower-risk iterations that protect the trajectory.
8. **Do not over-cluster.** If two of the proposed iterations are essentially the same lever (two hook-only iterations on the same ad), drop one and use the slot for a different lever.
9. **Respect prior iteration history.** If the ad has already been through five hook swaps, the sixth hook swap is unlikely to be the right call. Build on what previous iterations taught us, do not repeat them.
10. **Honor brand-specific overrides.** If the brand context, persona work, or prior fine-tuning has established that this brand responds outsized to a specific lever, weight that lever higher.

## Common mistakes to avoid

- Iterating on losing ads. Iterations are for winners and healthy performers only.
- Changing too many variables in a single iteration recommendation. One variable per iteration so the test produces a learning.
- Suggesting iterations that conflict with the working elements.
- Vague recommendations. "Change the hook" is not an iteration — "pull the clip at 0:15 where she shows the before/after and move it to 0:00" is.
- Predicting specific performance outcomes. Never promise numbers.
- Treating the menu as a checklist. The menu is options. The job is picking the two-to-four highest-confidence fits for this specific ad and brand.
- Only iterating from data. Pair every data signal with a creative read.

## Edge cases

- **Ad performs well across every metric.** Bottleneck is not a weak metric — it is the eventual risk of fatigue. Recommend iterations that unlock new audiences and refresh creative without disturbing what is currently working.
- **Strict compliance.** If the ideal iteration requires a claim the brand cannot make, substitute the closest compliant equivalent that achieves the same strategic intent.
- **Multiple ads provided.** Diagnose each independently. Do not blend. If a shared pattern emerges across ads, surface it as a note but still give specific recommendations per ad.
- **User asks for more iterations than there are strong options.** Give the strong options only and explain why you stopped there.

## Final quality audit before output

Run this checklist internally before delivering. Every answer must be yes.

- Did I choose the right number of iterations?
- Is each iteration grounded in both the data AND the creative analysis?
- Did I explain how each iteration flows with the rest of the ad?
- Did I reference proven patterns where relevant?
- Did I avoid predicting specific metric improvements?
- Are these genuinely the highest-confidence iterations for THIS ad given THIS brand, THIS data, THIS prior history?
- Does each iteration clearly serve squeezing-more or unlocking-new-audiences?
- Did I protect the working elements?
- Is each iteration specific enough to execute without follow-up questions?
- Did I run every recommendation through the brand context — compliance, tone, ICP, competitive landscape?

If any answer is no, fix it before delivering.

---

## Reasoning log

This section accumulates past picks and the reasoning behind them as the loop runs. Each entry is a short paragraph capturing the diagnosis, the chosen iterations, why those were chosen over alternatives, and any user feedback that adjusted the picks. Over time, this log becomes the strongest signal for Parker on how this specific brand thinks about iteration choice — patterns the rest of this document cannot capture.

When Parker fine-tunes on user feedback, the durable edits land here and in the per-process files, not in SKILL.md.

*(No entries yet — populated by the fine-tuning loop.)*
