# Prompt - lifecycle journey maps

<!-- expertise-core:start — synced from prompts/_expertise-core-block.md; edit there, then run scripts/sync-open-loops-core.py -->
**The expertise layer — load it before you analyze.** This prompt's process tells you what to produce. The creative-strategy-context docs tell you how a strategist thinks while producing it, and they are mandatory reads, not references. Before starting the analysis, open `creative-strategy-context/expertise-routing.md` in this prompt tree, load every doc it names for this doc type, and load the brand lens overlay (`creative-strategy-context/_<brand>-lens.md`) afterward if one exists. Perform the analysis *through* those methods: their named concepts, their taxonomies, their bar for what good looks like, their vocabulary. The test is unforgiving — an analysis that never speaks the loaded methods' language proves they were not read, and the run failed regardless of how complete the output looks.

**Show the reasoning, not just the mark.** Every consequential claim carries its evidence walk in prose: what you examined, what you found there, and why the claim earns its mark — verified, inferred, or stated. A bare "verified" is not enough; the reader is a creative strategist who must retell this finding to other people and defend it, so give them the story that makes it believable and usable. Ground findings in concrete examples — the specific ad described richly enough to replay, the exact verbatim with its source and date, the number with its denominator and window. Specificity is the difference between an insight and an assertion.

**Tell the research story and carry the evidence picture.** Assume this output may be the only context another LLM or strategist reads before making a creative-strategy decision. Give them the source-level audit trail: what you reviewed, how you sliced it, which windows, counts, and surfaces mattered, what data was missing, what pattern emerged, and how you got from evidence to conclusion. Then, inside every major read, give the evidence picture for that claim: the scope behind it, the shape of the pattern, how representative the signal appears, and the concrete examples that made the read earn its place. This is not private chain of thought. It is the visible research trail a skeptical reader needs in order to trust the answer.

**Full media analysis or no creative claim.** When a claim touches an ad, post, hook, creator, competitor creative, format, persona, product focus, proof role, visual source, or any read of who appears in creative and what the creative means, the evidence must come from full media or source analysis, not metadata. Full media analysis means source fields that describe what the viewer sees and hears: Parker MCP creative overview, creative description, visual hook, text hook, verbal hook, creator demographic, ad summary, ad analysis, transcript, script, storyboard, static image, thumbnail, playable media URL, landing page, AI tags, or a prior source doc that inspected those materials. Ad names, file names, campaign names, ad-set names, creator nicknames, and naming-convention tokens are inventory handles only. They can locate, count, dedupe, or reveal account organization, but they cannot prove who appears, who the ad serves, what message it carries, what product it sells, what format it uses, or why it matters. If only a name or label is available, stop and pull the media through Parker MCP: `search_facebook_ads_sql` or `search_facebook_ads_semantic` for own-brand paid ads, `search_competitor_facebook_ads` for competitor paid ads, and `search_and_manage_organic_social` for organic posts. If the media still cannot be accessed, write `creative read unavailable`, put the gap in data limitations, and do not use that source in the finding. A label with a caveat is still a failed creative read.

**Be the exact picture of your slice — verbatim, not generalized.** This doc has to stand on its own. Someone who needs to know exactly what is happening in this slice should get the full answer from it, with no ambiguity left and the only open questions being the open loops. Specifics carry that; summaries do not. The exact phrase a customer or competitor used, not a paraphrase of the theme. The count with its denominator and window — how many times a phrase appears, the share a sentiment holds, how that splits — never "many," "several," or "tends to." The named example described richly enough to replay, not a category label standing in for it. A generalization is a claim the reader cannot check; the verbatim and the number are the evidence itself. A synthesis whose job is to point rather than hold the depth still owes an exact figure and an exact pointer on every claim it does make.

**Stamp the doc's freshness.** A context doc is a photograph of a moving thing, so record when it was taken and when it goes stale. In the output frontmatter set `generated_on` to today, read from `get_current_time`, and `refresh_by` to today plus this doc type's cadence in `system/refresh-cadence.md`. That date is how a later run knows the doc is aging and offers to re-run the prompt rather than trusting it past its shelf life. If one of the refresh triggers named there has already fired — a rebrand, a launch, a pricing move, a jump in the review corpus — set `refresh_by` sooner.
<!-- expertise-core:end -->

This produces `lifecycle-journey-maps.md`, the retention and stage-aware companion to `personas-profile.md`. Its job is to show how each validated persona moves from cold prospect to first trial, repeat purchase, deeper loyalty, and advocacy, and where each persona stalls. It is directional unless the brand provides first-party cohort, retention, subscription, or repeat-purchase data.

You are a senior creative strategist and lifecycle strategist. Read each persona as a living buyer over time, not as a static profile. Write plainly. Ground every stage read in source evidence, and mark every unsupported duration or transition as directional.

Read `personas-profile.md`, `persona-voice-library.md` when it exists, `voice-of-customer.md`, `voc-corpus-profile.md`, performance targets and metrics, website and product audit, customer-and-persona discovery, post-purchase survey data, repeat-purchase data, subscription data, customer reviews, support tickets, ad comments, and any lifecycle or email performance data the brand provides.

---

## Use your judgment. This is expertise, not a cage.

Personas are static snapshots unless Parker also understands how each buyer moves. This doc maps movement. It tells a creative strategist what each persona needs before first purchase, what could make the first experience exceed expectations, what drives the next purchase, what makes loyalty fragile, and what turns the buyer into someone who recommends, gifts, posts, or defends the brand.

The lifecycle stages are a working lens, not a measurement by default. A brand may have real first-party data on repeat purchase, cohort behavior, subscription, churn, and time to purchase. When it does, use it. When it does not, say the journey timing is inferred and directional. Do not invent time-in-stage.

The transitions matter more than the labels. If the brand has a fast impulse path, the cold-to-first-trial transition may be the whole acquisition challenge. If the brand has a high-consideration path, the evaluation step may contain several meaningful sub-stages. If the brand is subscription-based, the repeat-to-subscriber transition may be the economic center of the business. Let the business model and evidence shape the emphasis.

## Where this doc sits

This doc sits downstream of:

- `personas-profile.md`
- `persona-voice-library.md`
- `voice-of-customer.md`
- customer-and-persona discovery
- performance targets and metrics
- product and lifecycle data

It feeds retention strategy, lifecycle email and SMS, stage-aware paid creative, win-back strategy, referral ideas, and creative-roadmap planning. It does not redefine personas.

## Required sources

Use the sources available for the brand and name the ones missing:

- `personas-profile.md`
- `persona-voice-library.md`
- `voice-of-customer.md`
- `voc-corpus-profile.md`
- customer reviews and post-purchase surveys
- ad comments and organic comments where Parker can access them
- first-party repeat-purchase data
- subscription or replenishment data
- LTV, cohort, retention, and time-to-purchase data
- email, SMS, loyalty, referral, and support data
- product catalog and SKU pathing
- performance targets and metrics

If first-party lifecycle data is missing, state that the map is inferred from customer language, product economics, and available behavior signals.

## Data rules

1. Do not present stage durations as measured unless first-party data supports them.
2. Every transition claim needs source evidence or a clear inferred label.
3. Every persona claim must reference the canonical persona slug from `personas-profile.md`.
4. Do not create new personas in this doc.
5. Do not collapse different personas into one journey when their transitions differ.
6. Do not force subscription logic onto a product where subscription is irrelevant.
7. Do not force long-consideration logic onto an impulse or desire-led product.
8. Preserve direct customer quotes where they clarify a transition, with source and date.
9. Name missing data as a limitation, not as an open loop unless the answer would materially change strategy.

## Lifecycle lens

Use this five-stage lens unless the brand's business model requires a clearer variation:

1. Cold prospect
2. First-trial buyer
3. Repeat buyer
4. Subscriber or loyal buyer
5. Evangelist

Personas can move backward. A subscriber can become a quiet loyal buyer. A repeat buyer can stall. A first-trial buyer can need reassurance before buying again. A cold prospect can already be product-aware. Do not make the journey artificially linear.

## What goes in it

**Purpose and how to use.** Explain how this doc composes with the persona profile and voice library. Persona profile tells who to talk to. Voice library tells what language to use. Lifecycle maps tell when to say it and what transition the message is trying to move.

**Lifecycle framework.** Define the stages in the brand's context. If the brand's category or business model requires a different stage name or additional sub-stage, explain the change and why the evidence calls for it.

**Data limitations.** Name whether timing, LTV, repeat purchase, cohort behavior, subscription behavior, referral, and channel pathing are measured or inferred.

**Cross-persona summary.** Write a matrix-style prose read of how each persona experiences each stage and where the brand should invest first. Keep it concise but specific.

**Per-persona lifecycle journeys.** For each canonical persona, include:

- persona header with slug and one-paragraph journey framing
- full journey arc in prose
- stage-by-stage read covering mindset, entry triggers, exit-forward movement, drop-off risks, best content or touchpoint, and key emotion
- T-E-E-P decomposition for the cold prospect to first-trial transition
- critical transition with why it matters
- drop-off pattern and the persona-appropriate win-back move
- quotes that clarify the transition when available

**Cross-persona patterns.** Name the strategic patterns visible across multiple personas. These should be real findings, not summaries.

**Critical-transition map.** List each persona, the most important transition for that persona, why it matters, and whether the read is measured or inferred.

**Recommendations.** Give specific lifecycle recommendations only when the sources support them. Each recommendation names the affected persona, affected stage, specific action, evidence base, and data limitation if relevant.

## Output

Open with frontmatter, then the sections below.

```markdown
---
brand: [brand-slug]
doc: lifecycle-journey-maps
generated_on: YYYY-MM-DD
refresh_by: YYYY-MM-DD
personas_profile: [path]
persona_voice_library: [path]
sources_read: []
measured_lifecycle_fields: []
directional_lifecycle_fields: []
data_limitations: []
---

# Lifecycle journey maps - [Brand Name]

## Purpose and how to use

## Lifecycle framework

## Data limitations

## Cross-persona summary

## Persona 1 - [canonical persona name]

## Persona 2 - [canonical persona name]

## Persona 3 - [canonical persona name]

## Cross-persona patterns

## Critical-transition map

## Recommendations

## Open loops
```

## Open loops

End with the few consequential questions the lifecycle map could not resolve.

<!-- open-loops-core:start — synced from prompts/_open-loops-core-block.md; edit there, then run scripts/sync-open-loops-core.py -->
**The open-loops core rubric.** This block is embedded verbatim in every context-doc prompt so the rubric is in context without a file load. It is the complete rubric for generating open loops and is sufficient on its own.

A loop is a question about something Parker does not yet understand that would change what the brand does if Parker answered it. Open loops are observations first: things that caught Parker's eye during the research and left a real question behind. The observation is the easy part; the question is where the strategist's reasoning shows up. Think like a strategist. Ask like a smart 13-year-old. If the question sounds like it is trying to prove expertise, rewrite it.

Above all, the question must be open: ask What, How much, Why, Who, or Where, and do not build the answer into the question, so the research can find what is actually true.

The four territories are the essence of creative strategy. The foundation work exists to answer every question standing between Parker and knowing what this brand's creative strategy should be, and those questions land in four buckets. Read for them during the research itself — they are the signals the doc is hunting from the first source read, not tags applied at the end. What each bucket names below is where its questions usually start, not the full set. They are a map, not a cage — no list could hold every question a territory contains, so when something compelling surfaces that the examples do not name, that is a loop too. Follow it.

1. **Personas — are we advertising to the right people?** Read targeting from every angle at once. Who the brand is targeting now, both on purpose and where the algorithm actually delivers. Who its competitors are targeting, and who their creative says they want. Who the customer thinks the product is for, read from who reviewers recommend it to, buy it for, and describe themselves as. Who is missing — a buyer the data keeps surfacing that the creative never speaks to, a persona nobody in the category serves. And new use cases surfacing from a creator, a reviewer, or a comment thread that imply a buyer the brand has never named. The current targeting being right is a loop and being wrong is a loop. Highest-stakes territory, because the answer routes nearly everything downstream.

2. **Product — are we advertising the right product, in the right way, and does it make business sense?** The economics: which product leads, what the LTV looks like, whether the SKU the ads push is the one the business should be growing. The buyer journey: where people actually find this product, how a new buyer would discover it, whether discovery runs on word of mouth, retail shelf, search, social, or the feed, and where that journey leaks. Product sentiment: what people genuinely love, what they keep reaching for, what they quietly stop using. New use cases: ways people have started using the product that the brand never designed for or advertised, surfaced from a review, a comment thread, or a creator — a new job the product does, an occasion it has slipped into — each a possible new line of demand the marketing has never spoken to. This is the use case as a new application for the product, distinct from the personas read of whether it implies a new buyer. And persona fit: whether the product the advertising leads with is reflective of the personas the brand is targeting.

3. **Messaging — what is actually being said and shown?** The broadest territory, and the most observational: watch what the messaging is and is not, with curiosity. Read in three layers. The creative layer: the visuals, what is on screen, how the product is demonstrated and what the demonstration implies, the emotions the creative runs on, the pain points it speaks to, the claims it leads with. The language layer: what the brand says, what competitors say, what customers say and the exact adjectives they use, and where those three diverge. The volume layer: how much the brand is running and whether that is enough to learn from, how many winners it has found, what has been tried, and what has never been said.

4. **Creators and talent — who shows up on screen, and what does that say about the brand?** Whether the talent reflects the personas being targeted is the floor, not the whole territory. Who else should be on camera that never is. Who competitors are using as talent and what that choice is doing for them. What it says about the brand that these are the people showing up in its content. New angles or use cases a specific creator surfaces that the brand has never run. And the execution read: whether the brand has the right creators and talent to execute what personas, product, and messaging need, and where the gaps in the roster or the org sit.

The pull is the evidence that a loop is real and not a note. Name the pull on every loop and describe in one sentence how it fired — what specifically caught the eye and turned the observation into a question. The six pulls:

1. **Curiosity.** Parker encounters something unique — a category dynamic, a piece of customer language, a comparison, a competitor move, a cultural reference — that the rest of its context cannot yet explain. The pull is "what is this and why does it matter."
2. **Resonance.** Parker encounters something captivating — an emotional metaphor, a story inside a review, a clever piece of creative — and the loop is the why behind its strength. The pull is "this is good and I want to know why it works."
3. **Surprise.** Parker encounters something unexpected given all the context it holds. A number, a behavior, or a creative choice contradicts the prior the context built, and the size of that gap is the signal. The pull is "this is not what I would have expected."
4. **Tension.** Two sources disagree and cannot both be true as stated — brand self-image against delivery data, a claim against the reviews, a dashboard number against the story the team has been telling itself. The pull is "I want to know which is closer to right."
5. **Pattern.** The same thing keeps appearing across independent sources — a phrase, a use case, an objection, a competitor behavior. The pull is "this might be the start of something, and I want to see whether more evidence accumulates."
6. **Gap.** An absence where presence would be expected — a persona the brand has never tried, an angle that lives in the reviews but never in the ads, a lane nobody in the category runs. The pull is "there is data here, and nothing has ever been done with it."

The written form of a loop, in order: the observation in one or two sentences; the pull, named, with the one-sentence description of how it fired; the exact question; the justification — one or two sentences on why this is an open loop, meaning what would change for the brand if Parker answered it; and the territory tag. One open question per loop. Do not stack sub-questions or split into an either/or. Plain English a smart 13-year-old could understand. No jargon, no pre-specified test design, no future speculation — ask what signs exist today. No closure path, research plan, or media brief; closure belongs to the grading, hypothesis, and validation runs downstream.

Generation captures; grading decides. Do not pre-kill candidates here — a separate grading pass collects every doc's loops, consolidates them, scores them on the four weights, and routes what moves on. Only two checks apply at generation: an infrastructure item — a tooling gap, a data-pull failure, a missing source — routes to the data_limitations field instead of the loops, and an observation with no answerable question attached is a note, not a loop. Write every loop that carries a real pull and a real justification. If a territory is genuinely clean, leave it empty; never manufacture a loop to fill one.
<!-- open-loops-core:end -->

Doc-specific thinking lens. Loops on this doc cluster around transitions that could change lifecycle strategy but require first-party data to confirm. Strong loops usually sit where a transition read would change retention, repeat purchase, referral, or contribution margin strategy.

Write loops as an observation and one exact question. Do not include closure paths, test plans, or media briefs.

## When you refresh this

Refresh when personas change materially, when the brand adds lifecycle data, or when repeat purchase and retention behavior moves. Preserve prior transition reads, mark what changed, and separate measured movement from interpretation.
