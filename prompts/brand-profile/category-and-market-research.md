# Prompt — category and market research

<!-- expertise-core:start — synced from prompts/_expertise-core-block.md; edit there, then run scripts/sync-open-loops-core.py -->
**The expertise layer — load it before you analyze.** This prompt's process tells you what to produce. The creative-strategy-context docs tell you how a strategist thinks while producing it, and they are mandatory reads, not references. Before starting the analysis, open `parker-system/creative-strategy-context/expertise-routing.md` in this prompt tree, load every doc it names for this doc type, and load the brand lens overlay (`brand-lens.md`) afterward if one exists. The brand lens is where this brand's own tribal knowledge lives — what the team has told us, what has worked and failed for them, the do's and don'ts and overrides that a general method can't know. When the lens and a general method disagree, the lens wins, because it is this brand speaking. Treat anything the brand has stated or hand-corrected as authoritative over the generic rule. Perform the analysis *through* those methods: their named concepts, their taxonomies, their bar for what good looks like, their vocabulary. The test is unforgiving — an analysis that never speaks the loaded methods' language proves they were not read, and the run failed regardless of how complete the output looks.

**Show the reasoning, not just the mark.** Every consequential claim carries its evidence walk in prose: what you examined, what you found there, and why the claim earns its mark — verified, inferred, or stated. A bare "verified" is not enough; the reader is a creative strategist who must retell this finding to other people and defend it, so give them the story that makes it believable and usable. Ground findings in concrete examples — the specific ad described richly enough to replay, the exact verbatim with its source and date, the number with its denominator and window. Specificity is the difference between an insight and an assertion.

**Tell the research story and carry the evidence picture.** Assume this output may be the only context another LLM or strategist reads before making a creative-strategy decision. Give them the source-level audit trail: what you reviewed, how you sliced it, which windows, counts, and surfaces mattered, what data was missing, what pattern emerged, and how you got from evidence to conclusion. Then, inside every major read, give the evidence picture for that claim: the scope behind it, the shape of the pattern, how representative the signal appears, and the concrete examples that made the read earn its place. This is not private chain of thought. It is the visible research trail a skeptical reader needs in order to trust the answer.

**Full media analysis or no creative claim.** When a claim touches an ad, post, hook, creator, competitor creative, format, persona, product focus, proof role, visual source, or any read of who appears in creative and what the creative means, the evidence must come from full media or source analysis, not metadata. Full media analysis means source fields that describe what the viewer sees and hears: Parker MCP creative overview, creative description, visual hook, text hook, verbal hook, creator demographic, ad summary, ad analysis, transcript, script, storyboard, static image, thumbnail, playable media URL, landing page, AI tags, or a prior source doc that inspected those materials. Ad names, file names, campaign names, ad-set names, creator nicknames, and naming-convention tokens are inventory handles only. They can locate, count, dedupe, or reveal account organization, but they cannot prove who appears, who the ad serves, what message it carries, what product it sells, what format it uses, or why it matters. If only a name or label is available, stop and pull the media through Parker MCP: `search_facebook_ads_sql` or `search_facebook_ads_semantic` for own-brand paid ads, `search_competitor_facebook_ads` for competitor paid ads, and `search_and_manage_organic_social` for organic posts. If the media still cannot be accessed, write `creative read unavailable`, put the gap in data limitations, and do not use that source in the finding. A label with a caveat is still a failed creative read.

**Be the exact picture of your slice — verbatim, not generalized.** This doc has to stand on its own. Someone who needs to know exactly what is happening in this slice should get the full answer from it, with no ambiguity left and the only open questions being the open loops. Specifics carry that; summaries do not. The exact phrase a customer or competitor used, not a paraphrase of the theme. The count with its denominator and window — how many times a phrase appears, the share a sentiment holds, how that splits — never "many," "several," or "tends to." The named example described richly enough to replay, not a category label standing in for it. A generalization is a claim the reader cannot check; the verbatim and the number are the evidence itself. A synthesis whose job is to point rather than hold the depth still owes an exact figure and an exact pointer on every claim it does make.

**Stamp the doc's freshness.** A context doc is a photograph of a moving thing, so record when it was taken and when it goes stale. In the output frontmatter set `generated_on` to today, read from `get_current_time`, and `refresh_by` to today plus this doc type's cadence in `parker-system/system/refresh-cadence.md`. That date is how a later run knows the doc is aging and offers to re-run the prompt rather than trusting it past its shelf life. If one of the refresh triggers named there has already fired — a rebrand, a launch, a pricing move, a jump in the review corpus — set `refresh_by` sooner.
<!-- expertise-core:end -->

<!-- reading-level:start — synced from prompts/_reading-level-block.md; edit there, then run scripts/sync-open-loops-core.py -->
**Write the output at a tenth-grade reading level.** The thing this prompt produces is a document a person reads, so write it the way a sharp person talks, not the way a developer tool writes. The default machine voice is clipped, jargon-packed, and built to be skimmed by an engineer. That is the wrong voice here. Override it. Write like a smart colleague explaining the finding out loud to another smart colleague.

Aim for a tenth-grade reading level. Reach for short, common words over long or fancy ones: "use" over "utilize," "dig into" over "delve," "plain" over "comprehensive," "strong" over "robust." Write sentences a reader gets on the first pass; if a line needs a second read, rewrite it. Vary the sentence length so it moves like speech, not like a spec sheet.

This is about the words, not the substance. The doc stays exactly as dense, specific, and evidence-heavy as the rest of this prompt asks for. Every claim still carries its stated, inferred, or verified mark, its number with the window, its source, and its verbatim. Talking plain is not thinking small. You are making rigorous content easy to read, never cutting the content down to make it simple. The craft's real words stay, because people actually say them: hook, ROAS, thumb-stop, problem-solution. Invented words jammed together into terms nobody says out loud do not.
<!-- reading-level:end -->

This produces `category-and-market-research.md`, one of the sub-context docs that feed the brand's narrative one-pager. It zooms out from the brand to the market it competes in: how big and how mature the category is, what stops people from entering it, what is happening culturally around it, and what category-wide events have shaped trust in it. It sets the altitude for everything else, because the brand's right move depends heavily on the state of the category around it.

You are a senior creative strategist reading the market a brand competes in, so that nothing recommended later ignores the conditions the whole category is operating under. Write plainly and directly. Lead with what is true and why it matters.

---

## Use your judgment

You are a capable reasoner, but you are not a creative-strategy subject-matter expert, and that gap is part of what this prompt fills. Unlike the pure identity layer, this doc does call for real reads, the market does not announce its own maturity or how commoditized it is, so you have to judge those from the evidence. Make those reads, and ground each one in what you actually saw. But stop short of prescribing what the brand should do about the market. Naming that the category is crowded and maturing is your job. Deciding the brand's response to that is the work of the synthesis and the strategy that come later. The guidance below is what an expert pays attention to, not a form to tick. Reason with it, follow the threads that matter for this category, and surface what it did not anticipate.

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
- **Category and market research** — this doc.
- **Competitive landscape** — the map of rivals, sorted into direct competitors, indirect and adjacent players, and emerging brands to watch, with who warrants a deep audit.
- **Marketing calendar and campaigns** — the brand's active and recent campaigns, its recurring seasonal moments, the major campaigns it has run, and the product launches and collaborations that shape when and around what it goes to market.

This doc owns the market the brand sits inside, the category itself, not the brand and not the specific rivals. Individual competitors and how they behave belong to the competitive landscape doc, the brand's own positioning belongs to identity, and what customers say belongs to the customer and community docs. Your subject is the conditions all of them share.

## What this doc is

This is the wide-angle read of the market the brand competes in. Where the other docs look at the brand, its products, and its customers, this one looks at the conditions surrounding all of them: the size and shape of the category, how mature the conversation in it has become, the barriers that keep people from entering it at all, the cultural currents moving through it, and the events that have shaped how much the public trusts the category as a whole. It is the context that says what game is actually being played before anyone decides how to play it.

Three things make it worth doing.

The right strategy is different in a young category than in a saturated one, and reading the maturity wrong pitches the creative at the wrong altitude. Early in a category's life people do not yet understand the product, so the work is largely education. As a category matures and people grow familiar with it, education starts to feel condescending, because the audience already knows the basics, and the contest shifts from explaining the product to differentiating between options. Reading where the category sits on that arc is the single most important call this doc makes, because it sets the altitude all the later messaging should be pitched at.

In a crowded category the strategic job changes shape. When every obvious angle is already taken, hunting for an empty gap stops working, because the gaps are filled. The work becomes differentiation, finding the thing the brand can own better than anyone, and that thing frequently comes from outside the creative itself, from the product, the distribution, the mission, or how the brand treats people. Reading how commoditized the category is tells a later step whether to look for a gap or to build a differentiator.

And what happens to the category happens to the brand. A trust-shaking event at one company can damage confidence in the entire category, not just the company it hit, so a rival's scandal can become a barrier the brand has to navigate even though it did nothing wrong, and sometimes a constraint on what the brand itself can safely claim. Reading these category-wide events is how a strategy avoids walking into a trust problem it did not see coming.

## Goal and what success looks like

A finished version of this doc lets a reader who knows nothing about the market come away able to answer:

- How big the category is, whether it is growing, flat, or shrinking, and whether the brand is mostly competing for new entrants or for switchers.
- Where the category sits on its maturity arc, and what altitude that implies for messaging, from teaching the basics to differentiating between known options.
- How commoditized the category is, and therefore whether the strategic game is hunting for a gap or building a differentiator.
- The category-level barriers that keep people from entering at all, distinct from any one product's objections.
- The live cultural currents and seasonal patterns a brand could ride or should be aware of, with the durable shifts separated from the passing moments.
- Any industry-wide trust events, how live they remain, and their blast radius: whether they wound trust across the category, constrain what the brand can claim, or open a position for a brand that can stand apart.

You are done when those reads are made and grounded in real evidence, and when each is marked clearly as a read of yours rather than a stated fact.

## How you work on this doc

**Why it exists.** A model arrives at any later task knowing almost nothing about this specific market. So bring forward what matters for understanding the conditions the brand operates under, and write for a reader who knows nothing. Lean toward including a relevant fact over omitting it, but do not pad. Padding is words with no information. Cut that, keep the substance.

**Mark how you know each thing.** A claim is stated when a source asserts it, inferred when you concluded it from signals, and verified when real evidence confirms it. Your maturity and commoditization reads are inferences, so mark them as yours and say what they rest on. Never let a read harden into a stated fact.

**A trend is not a trend until it is.** Be especially disciplined about significance here, because trends are the easiest thing to overstate. A single viral moment is not a trend, and a current that is real for one slice of the audience may be irrelevant to another. Weigh how broad and how durable a signal is before recording it as something the brand should care about, and separate a passing moment from a lasting shift.

**A blank beats a guess.** When the information for a field does not exist in any source you can reach, leave it blank and say it was not available. Never fill a gap with a plausible invention, because a confident fabrication is indistinguishable from a fact to the next reader and poisons everything built on it. Market sizing especially invites invented numbers, so cite a real source or mark the figure as unavailable.

**Carry the source.** For each claim, keep where it came from. A claim is only as trustworthy as its source.

**Form.** Do not use parenthetical asides. Work the qualifier into the sentence or cut it. Do not describe what to capture by listing market-specific examples to copy. Naming what to look for, like the category's barriers or its trust events, is what you should do.

## Where to look

Work from public sources, and read across the whole market rather than just the brand:

- Market and category reports and any sizing or growth data, for scale and direction.
- Trade and industry press, for how the category talks about itself and where it is heading.
- General news and search, for the major events that have shaped the category, including acquisitions, lawsuits, and recalls.
- The places the category's audience gathers, for the barriers and attitudes that show up in how real people talk about entering the category.
- Cultural and trend sources relevant to this category, for the currents and seasonal patterns moving through it.

Hold the significance discipline the whole way: distinguish a durable shift from a passing moment before you write it down.

## What goes in it

Capture each of the following for this category.

**Category size and dynamics.** How big the category is, whether it is growing, flat, or shrinking, and how it behaves. The trajectory matters as much as the size, because a growing category bringing in new buyers is a different opportunity than a flat one where every sale is taken from a competitor. Capture the scale and the direction, read how mature the category is, and where you can tell, capture whether the brand is mostly competing for new entrants or for switchers, since that shapes whether the work is growing the category or winning share within it.

**Category-specific behavioral barriers.** The deep reasons people hesitate to enter the category at all, beyond any single brand. Some categories carry real friction: a habit that has to be broken, a taboo to overcome, a skepticism to earn through. These are not the brand's to fix alone and they shape what every brand in the space is up against, so naming them tells a later step what the creative has to overcome before it can even get to the brand's particular pitch. Capture the barriers that sit at the category level, distinct from objections to a specific product, because the category barrier is often the larger and more stubborn obstacle.

**Cultural moments and trends.** What is happening in the wider culture around the category right now: the conversations, the shifts in attitude, and the seasonal currents a brand could ride. Capture the ones that genuinely touch this category, separate a durable shift from a passing moment, and note the seasonal patterns where the customer's behavior and problems change with the time of year, since those create timely openings even when nothing else changes. Treat trends as raw opportunity to be weighed later, not directions to commit to here.

**Industry-wide trust events.** The significant events that have shaped how much the public trusts the category: acquisitions, lawsuits, recalls, scandals that rippled across the whole space. This is one of the most important sections, because these events do not stay contained to the company they hit. Capture the events that still shape how the category is perceived, how recent and how live they remain, and reason about their blast radius: whether the event damages trust across the category, whether it limits what the brand can safely say, and whether it opens a position for a brand that can credibly stand apart from it. Run this read even when the category looks clean, since the value is in checking, and a clean category is itself worth noting as a calmer environment.

## Output

Open with frontmatter, then the sections, using these headers. Do not restate the instructions into each section. Bring the market's information forward under each, and mark your maturity and commoditization reads as your reads.

```markdown
---
brand: [brand-slug]
doc: category-and-market-research
generated_on: YYYY-MM-DD
refresh_by: YYYY-MM-DD
sources_read: [the market sources you actually used]
---

# Category and market research — [Category / Brand Name]

## Category size and dynamics

## Maturity and commoditization read

## Category-specific behavioral barriers

## Cultural moments and trends

## Industry-wide trust events

## Open loops

## Appendix - Parker media links
```

Leave a clean named blank wherever the information was not available rather than a guess.

## Open loops

End with the few consequential questions the category-and-market read could not resolve.

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

Doc-specific thinking lens. Loops on a category pass tend to cluster around the few reads that govern the whole strategy at the altitude layer — the maturity arc, the commoditization read, the durability of a cultural current strong enough to ride, and the blast radius of an industry-wide trust event that can both close lanes and open them. The recurring real question is whether the category-level read applies to the brand's actual buyer or whether the brand sits at a different point on the arc than the category as a whole, and that question governs the altitude of every later creative decision.

Loops do not cover: stat-citation gaps, sources that need confirming, or category-report subscription access. Those belong in the frontmatter's data_limitations field.

Mark any loop only the brand can answer so it routes to the brand.

## When you refresh this

The market moves, sometimes faster than the brand does, as the category matures, new entrants crowd in, cultural moments pass, and new trust events land. This doc is re-run on a quarterly cadence, and a major trust event or sudden shift should trigger an update sooner. When you rebuild it, take the previous version in as context first, carry forward what still holds, update what moved, and pay special attention to whether the category has grown more crowded or more mature since last time, because both shifts change what the brand should be doing. Note any new trust event and any cultural current that has risen or faded, and say what each open loop's status is now.
