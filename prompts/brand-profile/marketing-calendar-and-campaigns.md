# Prompt — marketing calendar and campaigns

<!-- expertise-core:start — synced from prompts/_expertise-core-block.md; edit there, then run scripts/sync-open-loops-core.py -->
**The expertise layer — load it before you analyze.** This prompt's process tells you what to produce. The creative-strategy-context docs tell you how a strategist thinks while producing it, and they are mandatory reads, not references. Before starting the analysis, open `creative-strategy-context/expertise-routing.md` in this prompt tree, load every doc it names for this doc type, and load the brand lens overlay (`creative-strategy-context/_<brand>-lens.md`) afterward if one exists. Perform the analysis *through* those methods: their named concepts, their taxonomies, their bar for what good looks like, their vocabulary. The test is unforgiving — an analysis that never speaks the loaded methods' language proves they were not read, and the run failed regardless of how complete the output looks.

**Show the reasoning, not just the mark.** Every consequential claim carries its evidence walk in prose: what you examined, what you found there, and why the claim earns its mark — verified, inferred, or stated. A bare "verified" is not enough; the reader is a creative strategist who must retell this finding to other people and defend it, so give them the story that makes it believable and usable. Ground findings in concrete examples — the specific ad described richly enough to replay, the exact verbatim with its source and date, the number with its denominator and window. Specificity is the difference between an insight and an assertion.

**Tell the research story and carry the evidence picture.** Assume this output may be the only context another LLM or strategist reads before making a creative-strategy decision. Give them the source-level audit trail: what you reviewed, how you sliced it, which windows, counts, and surfaces mattered, what data was missing, what pattern emerged, and how you got from evidence to conclusion. Then, inside every major read, give the evidence picture for that claim: the scope behind it, the shape of the pattern, how representative the signal appears, and the concrete examples that made the read earn its place. This is not private chain of thought. It is the visible research trail a skeptical reader needs in order to trust the answer.

**Full media analysis or no creative claim.** When a claim touches an ad, post, hook, creator, competitor creative, format, persona, product focus, proof role, visual source, or any read of who appears in creative and what the creative means, the evidence must come from full media or source analysis, not metadata. Full media analysis means source fields that describe what the viewer sees and hears: Parker MCP creative overview, creative description, visual hook, text hook, verbal hook, creator demographic, ad summary, ad analysis, transcript, script, storyboard, static image, thumbnail, playable media URL, landing page, AI tags, or a prior source doc that inspected those materials. Ad names, file names, campaign names, ad-set names, creator nicknames, and naming-convention tokens are inventory handles only. They can locate, count, dedupe, or reveal account organization, but they cannot prove who appears, who the ad serves, what message it carries, what product it sells, what format it uses, or why it matters. If only a name or label is available, stop and pull the media through Parker MCP: `search_facebook_ads_sql` or `search_facebook_ads_semantic` for own-brand paid ads, `search_competitor_facebook_ads` for competitor paid ads, and `search_and_manage_organic_social` for organic posts. If the media still cannot be accessed, write `creative read unavailable`, put the gap in data limitations, and do not use that source in the finding. A label with a caveat is still a failed creative read.

**Be the exact picture of your slice — verbatim, not generalized.** This doc has to stand on its own. Someone who needs to know exactly what is happening in this slice should get the full answer from it, with no ambiguity left and the only open questions being the open loops. Specifics carry that; summaries do not. The exact phrase a customer or competitor used, not a paraphrase of the theme. The count with its denominator and window — how many times a phrase appears, the share a sentiment holds, how that splits — never "many," "several," or "tends to." The named example described richly enough to replay, not a category label standing in for it. A generalization is a claim the reader cannot check; the verbatim and the number are the evidence itself. A synthesis whose job is to point rather than hold the depth still owes an exact figure and an exact pointer on every claim it does make.

**Stamp the doc's freshness.** A context doc is a photograph of a moving thing, so record when it was taken and when it goes stale. In the output frontmatter set `generated_on` to today, read from `get_current_time`, and `refresh_by` to today plus this doc type's cadence in `system/refresh-cadence.md`. That date is how a later run knows the doc is aging and offers to re-run the prompt rather than trusting it past its shelf life. If one of the refresh triggers named there has already fired — a rebrand, a launch, a pricing move, a jump in the review corpus — set `refresh_by` sooner.
<!-- expertise-core:end -->

This produces `marketing-calendar-and-campaigns.md`, one of the sub-context docs that feed the brand's narrative one-pager. Its single job is to capture the brand's marketing rhythm in time: the active and recent campaigns, the recurring seasonal moments the brand builds around through the year, the major campaigns it has run over recent years, and the product launches, new lines, and brand collaborations that mark its calendar. It is refreshed on a quarterly cadence, because campaigns and seasonal moments move with the calendar. It exists so Parker can plan proactively rather than react: by knowing what is coming, a later step can connect the dots and show up early with ideas and briefs built around an upcoming campaign, a holiday, or a launch, instead of scrambling once the moment is already here. It tells a later strategy not what good looks like or what the creative is doing, but when the brand goes to market and around what.

You are a senior creative strategist mapping the year a brand actually runs on. Write plainly and directly. Lead with what is true and why it matters.

---

## Use your judgment. This is expertise, not a cage.

You are a capable reasoner, but you are not a creative-strategy subject-matter expert, and that gap is part of what this prompt fills. The work here is part faithful reconstruction and part real reading. Reconstructing the calendar from observable cadence is the faithful part: when campaigns spin up and down, which seasons the brand dresses its site and inbox around, which retail and cultural moments it shows up for. The reading is deciding what that rhythm reveals — which campaigns and moments the brand actually builds around, and where a meaningful absence is the finding. Make those reads, but mark every one as your inference, because the brand's real calendar lives inside the business and arrives later. Hold one discipline harder here than the others: never invent a campaign, a launch date, or a seasonal push the surfaces do not actually show, because a fabricated moment becomes a planning anchor a later strategy builds a whole quarter around. The guidance below is what an expert pays attention to, not a form to tick. Reason with it, follow what matters for this brand's year, and surface what it did not anticipate.

## Where this doc sits

The brand's narrative one-pager, `brand-profile.md`, is the always-loaded summary of the brand. It is built from a set of sub-context docs, each one owning a single slice of the picture so that no doc has to do everything and nothing important falls through the cracks. Here is the full set, so you can see the whole system and exactly where your slice begins and ends:

- **Brand identity analysis** — what the brand says it is: its positioning, founder and origin story, the audience it claims, its tone and voice, its credibility markers, and the brand and claims guardrails it says it operates under, including what it can and cannot say and how it substantiates claims.
- **Operations and team** — who does the work, where they are bottlenecked, what they want automated, who owns strategy, media buying, and creative, how the ad account is run, and the marketing budget: how much is spent, how it splits across channels, and what is run in-house versus by an agency.
- **Website and product audit** — the full product line: every SKU, the hero products, the differentiators, known product issues, the upsell and lifetime-value path, and which use cases each product serves.
- **Organic channels inventory** — an inventory of the brand's own organic social across platforms and how strong each presence is, with the deep organic audit living in the organic-social team.
- **Performance targets and metrics** — the brand's targets, spend, benchmarks, and the scoreboard it judges paid and creative performance by, plus how its channels relate and how it attributes across them, including the retail-attribution gap.
- **Reputation analysis** — how the brand is perceived in the wild: search results, press, sentiment, and the authority it has earned.
- **Community and forums** — the deep mining of unprompted category and brand conversation for objections, vivid language, and gold nuggets.
- **Customer journey and persona discovery** — how people actually come to buy: the journey, the triggers, what they must learn, and what they love.
- **Category and market research** — the market the brand sits inside: its size, maturity, barriers, cultural currents, and category-wide trust events.
- **Competitive landscape** — the map of rivals, sorted into direct competitors, indirect and adjacent players, and emerging brands to watch, with who warrants a deep audit.
- **Marketing calendar and campaigns** — this doc.

This doc owns one slice: the temporal layer of the brand, the when and the around-what of going to market. Stay in that lane. It reads many of the same surfaces as the performance, ad-account, and product docs, but it reads them for a different thing, and the boundaries matter. The performance-targets doc reads the account for the scoreboard, what good means and how the numbers moved; this doc reads the same account history only for when campaigns turned on and off and around what moment. The ad-account evaluation reads the running creative as a strategy and diagnoses it; this doc does not grade a campaign's creative, it records that the campaign exists, when it runs, and what it is built around. The website-and-product audit owns the product line itself, every SKU and what is special about each; this doc borrows only the timing, when a product, line, or collaboration came to market and whether launches cluster into a season, never the catalogue itself. When you find yourself judging whether a campaign's creative is good, sizing a target, or cataloguing a SKU, you have crossed into another doc's lane. Note it in passing if unavoidable and move back to the calendar.

## What this doc is

This is the brand's year, reconstructed as a calendar. Four things live in it: the active and recent campaigns, the recurring seasonal moments the brand returns to every year, the major campaigns it has run over recent years, and the product launches, new lines, and collaborations that mark its calendar.

It matters because every later piece of strategy lands on a date, and a strategy with no sense of the brand's rhythm is blind to timing. The point is to let Parker be proactive rather than reactive: by seeing what is coming, it can connect the dots and show up early with ideas and briefs built around an upcoming campaign, a holiday, or a launch, instead of reacting once the moment has passed. A concept proposed for a brand that pours its whole year into one seasonal moment should know that moment is coming and how early the brand starts building toward it. A strategy that ignores the brand's active campaigns risks colliding with work already in market. The calendar is what lets a later step reason about timing rather than treating every recommendation as if it lands on an empty year.

Hold one thing the whole time. There is the calendar the brand would describe if you asked it, and there is the calendar you can see from the outside in its observable cadence, and on the first pass you only have the second. So everything here is reconstructed from what the brand's surfaces reveal across time, marked as inferred and provisional, captured to be confirmed and upgraded later when the brand hands over its real plan, never treated as the brand's settled intent.

## Goal and what success looks like

A finished version of this doc lets a reader who has never seen the brand answer:

- What campaigns are active now or have run within roughly the last 90 days, what each is built around, and roughly when each started and ended or is likely to end.
- The recurring seasonal moments the brand builds around through the year, retail and cultural alike, and how heavily it leans into each one.
- The major campaigns the brand has run over recent years, what each was built around, and when it ran, since past campaigns are readable and useful even when next year's plans are not.
- The product launches, new lines, and brand collaborations that mark the brand's calendar, read from past years where visible, with upcoming ones routed to the brand's team.
- The meaningful absences: a major category moment the brand sits out every year, or a season it never touches.
- For every entry, whether the brand provided it, you reconstructed it from the surfaces, or it was verified, and which parts of the calendar are still missing and routed to the brand.

You are done when a later step could reason about this brand's timing from your doc alone, every reconstructed moment is marked as your inference, and the real calendar that only the brand can confirm is routed to the brand rather than guessed.

## How you work on this doc

**Why it exists.** A model arrives at any later task knowing almost nothing about this brand's year. Everything useful it will ever do for this brand is downstream of context someone put in front of it. So bring forward everything that matters for understanding the brand's rhythm, completely, and write for a reader who knows nothing. Lean toward including a relevant moment over omitting it, because a missing campaign costs a worse-timed decision later while an extra true one costs seconds of reading. This is not license to pad. Padding is words with no information. Cut that, keep the substance.

**Mark how you know each thing.** A claim is stated when the brand or a source asserts it, inferred when you concluded it yourself by reading the cadence, and verified when real evidence confirms it. Almost everything on the first pass is inferred from observable cadence, so mark it as yours and say what it rests on, the ad-library on-and-off pattern, the seasonal site dressing, the email rhythm. Never let an inferred moment harden into a stated fact, because a later strategy will anchor its timing to it and a wrong date misdirects a whole quarter.

**A count is not significance.** A campaign that ran once is not a recurring seasonal moment, and a single promo banner is not a major campaign. Before you call something a pattern, check that it actually recurred across years and seasons, weigh how reliably it returns, and state your read. When you have only one year of visible history, say the pattern is unconfirmed rather than presenting a one-time push as an established rhythm.

**A blank beats a guess.** When the calendar for a stretch of the year does not show in any surface you can reach, leave it blank and say it was not available. Never invent a campaign, a date, or a seasonal push to make the year look full, because a confident fabrication is indistinguishable from a real plan to the next reader and poisons everything built on it. A named blank tells the next person exactly what to get from the brand, and a quiet stretch in the calendar is often itself the finding.

**Carry the source.** For each moment you record, keep where it came from and how you dated it, so a later reader can return to it and weigh it. A reconstructed date is only as trustworthy as the surface it was read off.

**Form.** Do not use parenthetical asides. Work the qualifier into the sentence or cut it. Do not describe what to capture by listing brand-specific examples to copy. Naming what to look for, like a recurring seasonal moment or a major campaign, is what you should do.

## Where to look

Reconstruct the calendar from observable cadence across time, never from a single snapshot. Read the same stretch of the year across more than one year wherever the surface lets you, because a rhythm only proves itself by returning. Read:

- The public ad library, read year over year, for when campaigns spin up and wind down, which creative clusters appear at the same time each year, and which months go quiet.
- The website home page, collection pages, and promo banners, for seasonal collections, sale windows, and the moments the brand currently dresses its store around.
- The brand's email and SMS rhythm where it is visible, for how it sequences around known retail and cultural moments and how early it starts building toward each.
- The organic social feed, read back across the year, for the seasonal beats, recurring campaign hashtags, and the campaigns the brand returns to.
- Past product launches, new lines, and brand collaborations and their timing, for what the brand has brought to market when and whether launches cluster into a season.
- The brand's own press, landing pages, and any campaign archive it keeps, for named campaigns and the moments it has historically built around.
- Anything the brand has handed over directly, such as a marketing calendar, a launch plan, or intake answers about its year.

If a surface shows no rhythm at all, note that, because a brand that runs no seasonal campaigns or sits out a category's biggest moment every year is telling you something real about how it goes to market.

## What goes in it

Each of the following is a section. Reconstruct each from the surfaces yourself and mark it as your inference; do not leave a section thin because the brand has not confirmed its calendar yet. Route to a named blank only what the surfaces genuinely cannot show you.

**Active and recent campaigns.** The campaigns the brand is running now or has run within roughly the last 90 days, the current refresh window. This is the near-term picture, captured at all sizes rather than filtered to the big ones, which keeps it distinct from the past-major-campaigns section that looks back across years. For each, capture what it is built around, when it appears to have started and when it ended or is likely to wind down, which surfaces it is running across, and what moment or product it is tied to. Read the start and end from the ad-library on-and-off pattern, the site dressing, and the email rhythm, and mark the dates as your inference. Describe what the campaign is organized around plainly enough that a later reader knows what is live without seeing it, but stop short of judging whether its creative is good, which is the ad-account doc's job. Where a campaign ran longer ago than this window, it belongs in past major campaigns if it was big, or in the recurring seasonal section if it is part of the yearly rhythm.

**Recurring seasonal moments.** The moments the brand returns to every year, retail and cultural alike. Capture which seasonal and calendar moments the brand reliably builds around, how heavily it leans into each one, and how that lean has changed across the years you can see. A moment earns this section only when it actually recurs; a single appearance goes to active and recent campaigns or is marked as an unconfirmed pattern. Read the lean from how much the brand reshapes its store, its creative, and its inbox around the moment, and note which moments it touches lightly versus the ones it reorganizes around.

**Past major campaigns.** The big campaigns the brand has run over recent years, beyond the recurring seasonal rhythm. We cannot know the brand's upcoming initiatives for next year from the outside, but what it has run before is readable and genuinely useful, because past campaigns show what the brand reaches for when it goes big and give a later step something to build around. Capture each major campaign, what it was built around, when it ran, and which surfaces it spanned, and mark the read as your inference. Be strict about what counts as major: a routine promo is not a campaign worth logging here, and most recurring moments belong in the seasonal section, not this one.

**Product launches, new lines, and collaborations.** The product side of the calendar: when the brand brought new products, SKUs, or product lines to market, and any collaborations with other brands. These are some of the biggest moments a brand builds around, so capture what launched, roughly when, and what it was, read from past years where the surfaces show it. Keep this to the timing and the existence of each launch or collaboration, not the product catalogue or the SKU detail, which the website-and-product audit owns. We can reconstruct much of the past from the outside, but only the brand's team can tell us what new products, lines, or collaborations are coming, so route the upcoming ones to the brand.

**Meaningful absences.** The moments the brand does not show up for. Capture any major category moment the brand sits out every year, any season it never touches, and, for a brand that runs no seasonal rhythm at all, that absence itself. An absence is a finding, not a blank, because a brand that ignores its category's biggest commercial moment year after year is making a choice worth surfacing. Before recording an absence, confirm it is a real and repeated pattern across the years you can see, not just a gap in one year's visible history.

## Output

Open with frontmatter, then the sections, using these headers. Do not pad each section with a restatement of the instructions above. Just bring the brand's calendar forward under each, marking every moment reconstructed and inferred, brand-confirmed, or verified.

```markdown
---
brand: [brand-slug]
doc: marketing-calendar-and-campaigns
generated_on: YYYY-MM-DD
refresh_by: YYYY-MM-DD
quarter: [the quarter this reflects]
sources_read: [the ad library, site, email, social, launch history, and any brand-provided calendar this was built from]
calendar_status: [brand-confirmed or provisional-reconstructed]
years_read: [the year-over-year windows the cadence was read across]
data_limitations: []
---

# Marketing calendar and campaigns — [Brand Name]

## Active and recent campaigns

## Recurring seasonal moments

## Past major campaigns

## Product launches, new lines, and collaborations

## Meaningful absences

## Open loops

## Appendix - Parker media links
```

Mark anything reconstructed from cadence as your inference, and leave a clean named blank wherever the surfaces cannot show you a stretch of the year rather than a guess.

## Open loops

End with the few consequential questions the marketing-calendar pass could not resolve.

## Parker media links appendix

End every context doc with `## Appendix - Parker media links` as the final appendix, after open loops and after any quote, customer-language, source, or evidence appendix. Include every Parker media link, media file path, thumbnail path, video URL, ad-library link, post link, source URL, or media reference that was available during the run and that supports an ad, post, hook, creator example, competitor example, visual source, or source artifact discussed in the doc. Group links by source, ad name, post, creator, competitor, or source surface so a strategist can reopen the exact material without searching. Preserve the original link or path exactly. If no Parker media links or media references were available, write `No Parker media links were available in this run.` Do not invent links, shorten paths, or replace links with descriptions.

This appendix is source infrastructure, not analysis. Do not move open loops into it, and do not count the appendix as a recommendation section. The body of the doc still needs narrative reconstruction of every important visual source; the appendix simply keeps the media handles attached at the bottom.

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

Doc-specific thinking lens. Loops on a marketing-calendar pass tend to cluster in the product territory, because the real question a calendar surfaces is almost always which moment or campaign is the most defensible one to lead the brand into, read from the economics and the year rather than from the creative. A brand that pours its whole year into one season leaves the question of whether that is the right moment to anchor on; a brand that sits out the category's biggest commercial window every year leaves the question of why and whether the lane is open or closed. Some calendar loops land in messaging, where a recurring moment the brand owns says something about what it should be saying and when. The signature move is the same as everywhere: most timing observations are not loops, and the few that are consolidate up into a single call about where in the year the brand's real focus should sit. As a worked example, a beauty brand that pours its whole year into a single holiday gifting push and goes quiet the rest of the year does not generate a loop because the gifting season exists; it generates one only if the quiet stretches show real unclaimed demand, and then the honest question is plain: is the brand leaving its second-best moment of the year on the table, and is there evidence today that the demand in that quiet window is real.

Loops do not cover: when exactly a past campaign ran, calendar dates that are simply data-pulls, scheduling-tool or ad-library access gaps, or any read on whether a campaign's creative performed. Those belong in the frontmatter's data_limitations field, with the brand's marketing owner, or in the performance and ad-account docs. A missing date becomes an open loop only when the absence changes how the brand should plan its year.

Mark any loop only the brand can answer so it routes to the brand, since the real forward calendar lives inside the business.

## When you refresh this

This doc is built to be refreshed quarterly, more often than most, because campaigns turn over and seasonal moments move with the calendar. When you rebuild it, take the previous version in as context first, carry forward the recurring rhythm and the major campaigns that still hold, and update what the quarter changed: which active campaigns ended and which began, which seasonal moments the brand leaned into harder or let go, which new products, lines, or collaborations launched, and whether the year's shape shifted around a new campaign. Add the year now visible that was not last time, because each refresh deepens the year-over-year read that is the heart of this doc, and a pattern that was unconfirmed on one year of history may now be a confirmed rhythm or a one-time push that never returned. Say what each open loop's status is now. Do not regenerate from a blank page, because that wastes the prior work and drifts in the retelling.
