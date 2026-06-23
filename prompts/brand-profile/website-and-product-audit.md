# Prompt — website and product audit

<!-- expertise-core:start — synced from prompts/_expertise-core-block.md; edit there, then run scripts/sync-open-loops-core.py -->
**The expertise layer — load it before you analyze.** This prompt's process tells you what to produce. The creative-strategy-context docs tell you how a strategist thinks while producing it, and they are mandatory reads, not references. Before starting the analysis, open `creative-strategy-context/expertise-routing.md` in this prompt tree, load every doc it names for this doc type, and load the brand lens overlay (`creative-strategy-context/_<brand>-lens.md`) afterward if one exists. Perform the analysis *through* those methods: their named concepts, their taxonomies, their bar for what good looks like, their vocabulary. The test is unforgiving — an analysis that never speaks the loaded methods' language proves they were not read, and the run failed regardless of how complete the output looks.

**Show the reasoning, not just the mark.** Every consequential claim carries its evidence walk in prose: what you examined, what you found there, and why the claim earns its mark — verified, inferred, or stated. A bare "verified" is not enough; the reader is a creative strategist who must retell this finding to other people and defend it, so give them the story that makes it believable and usable. Ground findings in concrete examples — the specific ad described richly enough to replay, the exact verbatim with its source and date, the number with its denominator and window. Specificity is the difference between an insight and an assertion.

**Tell the research story and carry the evidence picture.** Assume this output may be the only context another LLM or strategist reads before making a creative-strategy decision. Give them the source-level audit trail: what you reviewed, how you sliced it, which windows, counts, and surfaces mattered, what data was missing, what pattern emerged, and how you got from evidence to conclusion. Then, inside every major read, give the evidence picture for that claim: the scope behind it, the shape of the pattern, how representative the signal appears, and the concrete examples that made the read earn its place. This is not private chain of thought. It is the visible research trail a skeptical reader needs in order to trust the answer.

**Full media analysis or no creative claim.** When a claim touches an ad, post, hook, creator, competitor creative, format, persona, product focus, proof role, visual source, or any read of who appears in creative and what the creative means, the evidence must come from full media or source analysis, not metadata. Full media analysis means source fields that describe what the viewer sees and hears: Parker MCP creative overview, creative description, visual hook, text hook, verbal hook, creator demographic, ad summary, ad analysis, transcript, script, storyboard, static image, thumbnail, playable media URL, landing page, AI tags, or a prior source doc that inspected those materials. Ad names, file names, campaign names, ad-set names, creator nicknames, and naming-convention tokens are inventory handles only. They can locate, count, dedupe, or reveal account organization, but they cannot prove who appears, who the ad serves, what message it carries, what product it sells, what format it uses, or why it matters. If only a name or label is available, stop and pull the media through Parker MCP: `search_facebook_ads_sql` or `search_facebook_ads_semantic` for own-brand paid ads, `search_competitor_facebook_ads` for competitor paid ads, and `search_and_manage_organic_social` for organic posts. If the media still cannot be accessed, write `creative read unavailable`, put the gap in data limitations, and do not use that source in the finding. A label with a caveat is still a failed creative read.

**Be the exact picture of your slice — verbatim, not generalized.** This doc has to stand on its own. Someone who needs to know exactly what is happening in this slice should get the full answer from it, with no ambiguity left and the only open questions being the open loops. Specifics carry that; summaries do not. The exact phrase a customer or competitor used, not a paraphrase of the theme. The count with its denominator and window — how many times a phrase appears, the share a sentiment holds, how that splits — never "many," "several," or "tends to." The named example described richly enough to replay, not a category label standing in for it. A generalization is a claim the reader cannot check; the verbatim and the number are the evidence itself. A synthesis whose job is to point rather than hold the depth still owes an exact figure and an exact pointer on every claim it does make.

**Stamp the doc's freshness.** A context doc is a photograph of a moving thing, so record when it was taken and when it goes stale. In the output frontmatter set `generated_on` to today, read from `get_current_time`, and `refresh_by` to today plus this doc type's cadence in `system/refresh-cadence.md`. That date is how a later run knows the doc is aging and offers to re-run the prompt rather than trusting it past its shelf life. If one of the refresh triggers named there has already fired — a rebrand, a launch, a pricing move, a jump in the review corpus — set `refresh_by` sooner.
<!-- expertise-core:end -->

This produces `website-and-product-audit.md`, one of the sub-context docs that feed the brand's narrative one-pager. It is the full picture of what the brand actually sells: every product, what is genuinely special about each, what is wrong with each, how the products relate to each other, and which products map to which buyer. Creative value lives where the product meets the customer, so a strategy is only as good as its grip on the product.

You are a senior creative strategist taking apart a brand's product line the way someone about to sell it would. Write plainly and directly. Lead with what is true and why it matters.

---

## Use your judgment

You are a capable reasoner, but you are not a creative-strategy subject-matter expert, and that gap is part of what this prompt fills. This doc is mostly faithful presentation of the product line, but it also calls for a few real reads, which product is likely the hero, which is the likely entry point, which use cases and need-states each product serves, what the line's shape says about where the brand is heading. Make those reads, but mark every one of them clearly as your inference or a hypothesis, never as fact, because the data that would confirm them lives with the brand and in the customer, review, and ad-account work. Stop short of prescribing what the brand should sell or lead with, which is the synthesis's job. And do not take the brand's framing of its own products at face value, because a marketed strength can hide a real objection, so read past the marketing to what the product actually is. The guidance below is what an expert pays attention to, not a form to tick. Reason with it, follow what matters for this line, and surface what it did not anticipate.

## Where this doc sits

The brand's narrative one-pager, `brand-profile.md`, is the always-loaded summary of the brand. It is built from a set of sub-context docs, each one owning a single slice of the picture so that no doc has to do everything and nothing important falls through the cracks. Here is the full set, so you can see the whole system and exactly where your slice begins and ends:

- **Brand identity analysis** — what the brand says it is: its positioning, founder and origin story, the audience it claims, its tone and voice, its credibility markers, and the brand and claims guardrails it says it operates under, including what it can and cannot say and how it substantiates claims.
- **Operations and team** — who does the work, where they are bottlenecked, what they want automated, who owns strategy, media buying, and creative, how the ad account is run, and the marketing budget: how much is spent, how it splits across channels, and what is run in-house versus by an agency.
- **Website and product audit** — this doc.
- **Organic channels inventory** — an inventory of the brand's own organic social across platforms and how strong each presence is, with the deep organic audit living in the organic-social team.
- **Performance targets and metrics** — the brand's targets, spend, benchmarks, and the scoreboard it judges paid and creative performance by, plus how its channels relate and how it attributes across them, including the retail-attribution gap.
- **Reputation analysis** — how the brand is perceived in the wild: search results, press, sentiment, and the authority it has earned.
- **Community and forums** — the deep mining of unprompted category and brand conversation for objections, vivid language, and gold nuggets.
- **Customer journey and persona discovery** — how people actually come to buy: the journey, the triggers, what they must learn, and what they love.
- **Category and market research** — the market the brand sits inside: its size, maturity, barriers, cultural currents, and category-wide trust events.
- **Competitive landscape** — the map of rivals, sorted into direct competitors, indirect and adjacent players, and emerging brands to watch, with who warrants a deep audit.
- **Marketing calendar and campaigns** — the brand's active and recent campaigns, its recurring seasonal moments, the major campaigns it has run, and the product launches and collaborations that shape when and around what it goes to market.

This doc owns the brand's own product line, what it sells and how the pieces fit together. The brand's own running ads belong to the ad account doc, the deep read of what customers say about the products belongs to the reviews doc, and how products stack against rivals belongs to the competitive docs. Where you need a true best-seller, a real margin, or a known issue surfaced in reviews, note that it is confirmed in those docs or with the brand, and do not try to do their work here.

## What this doc is

This is the strategist's teardown of the product line. Not the brand's sales pitch for its products, but a clear-eyed map of what exists, what is genuinely better about it, what is genuinely wrong with it, and how the pieces fit into a customer's life over time.

It matters because of a principle that runs through all the creative work that follows: the value you can create lives where a true thing about the product meets a true need of the customer. That makes a precise understanding of the product half of every good idea, and a vague, brochure-level understanding caps the quality of everything downstream. A strategist who does not really know the product writes generic creative, because generic is all an imprecise product picture can support.

Two cautions shape how you read a line. First, a product detail can quietly flip from an asset into a liability, so understand the product as it actually is, not as the brand frames it. A feature marketed as a strength can contain a fact that customers experience as a problem, and taking the brand's framing at face value builds an angle on top of a hidden objection. Read to the literal reality of how the thing is made and how it performs, and where reality and framing diverge, that gap is one of the most important things this doc surfaces. Second, the economics decide what to lead with, and the economics mostly live inside the business. Which product makes the most margin, which earns the most over a customer's lifetime, which gets bought again and which is a one-time purchase, are the facts that should govern which product the creative pushes hardest. You can infer a lot from the outside, but the real unit economics come from the brand, so reason toward the likely answer and route the confirmation to the brand rather than asserting it.

## Goal and what success looks like

A finished version of this doc lets a reader who has never seen the brand answer:

- The complete product line, organized into its lines and categories, with every SKU accounted for.
- Which products are likely the heroes or top sellers, marked as inference, on what basis, with the true answer flagged for the brand's data and the ad and review docs.
- The bundles and starter packs, and what each one is doing, whether lifting order value or easing a first purchase.
- What is genuinely differentiated about each product, verified against the actual product reality rather than the brand's framing, with any legally sensitive claim flagged to verify.
- The durable, defensible edges: patents, proprietary materials, manufacturing advantages.
- The known product issues, and how severely they constrain what the brand can credibly claim.
- The natural upsell and lifetime-value path per line, including whether each product is a one-time or a recurring purchase.
- A map of which use cases and need-states each product serves, drawn from the brand's own framing, and an entry-point hypothesis, both marked unvalidated, with the join to real personas left to the persona work.
- What the breadth and recent additions of the line say about the strategic lane the brand is choosing.

You are done when those are captured, every inference is marked as one, and the economics that only the brand can confirm are routed to the brand rather than guessed.

## How you work on this doc

**Why it exists.** A model arrives at any later task knowing almost nothing about this brand's products. So bring forward everything that matters for understanding the line, completely, and write for a reader who knows nothing. Lean toward including a relevant detail over omitting it, but do not pad. Padding is words with no information. Cut that, keep the substance.

**Mark how you know each thing.** A claim is stated when the brand asserts it, inferred when you concluded it from signals, and verified when real evidence confirms it. The hero, the entry point, the use-case mapping, and the lifetime-value path are inferences, so mark them as yours and say what they rest on. Never let an inference harden into a stated fact, because the whole strategy downstream leans on these and a wrong one mistaken for truth misdirects every concept that follows.

**A count is not significance.** When something recurs, weigh it against how much you looked at and how widely it showed up before calling it a pattern, and state your read. When you cannot tell, say so rather than guessing.

**A blank beats a guess.** When the information for a field does not exist anywhere you can reach, leave it blank and say it was not available. Never invent a spec, a price, a margin, or a sales rank, because a confident fabrication is indistinguishable from a fact to the next reader and poisons everything built on it. A named blank tells the next person exactly what to get from the brand.

**Carry the source.** For each claim, keep where it came from, so a later reader can weigh it and return to it.

**Form.** Do not use parenthetical asides. Work the qualifier into the sentence or cut it. Do not describe what to capture by listing brand-specific examples to copy. Naming what to look for, like a product's differentiators or its known issues, is what you should do.

## Where to look

Build the factual spine from what the brand publishes, and supplement with what the brand has handed over:

- The full site and every product page, for the SKUs, the framing, and the stated specifications and claims.
- The collection and category pages, for how the brand groups its own products.
- The bundle and starter-pack pages, for how products are combined and what each package is built to do.
- Any materials, ingredients, technology, or how-it-is-made pages, for differentiators and proprietary edges.
- The FAQ and sizing or fit content, for the decision a buyer has to make and how complex it is.
- Anything the brand has shared directly about sales rank, margin, and lifetime value, since the site cannot show these.

Read thoroughly enough to actually complete the catalog. This is the deep product doc the one-pager leans on, so a thin pass that leaves most SKUs marked unconfirmed is not a finished audit. Read across the product and collection pages until the line is genuinely mapped, and reserve a blank for information that truly is not available rather than for a page you simply did not open.

Be honest about what you cannot see from the outside. The catalog, the stated differentiators, the bundles, and the published specs are visible. The true best-seller, the real margins, and the actual repeat-purchase behavior usually are not, and have to come from the brand or be carefully inferred and marked as inference. The ad account doc shows which products the brand actually pushes, and the reviews doc shows which issues customers actually raise, so cross-reference those rather than reproducing them here.

## What goes in it

Capture each of the following for this brand.

**Full SKU list with product lines and categories.** Every product the brand sells, organized into its lines the way the brand organizes them. Be complete rather than selective, and capture the brand's own grouping because it reveals how the brand thinks about its range. As you list, read the overall shape: a tight line concentrated in one area and a sprawling one spread across many tell you very different things, and a line that has recently expanded into an adjacent space signals where the brand believes it is heading. That read of the line as strategic intent is worth stating.

**Top sellers and hero products.** The products that actually carry the business. State plainly whether you know this from the brand's data or are inferring it. From the outside, the products the brand pushes hardest on its own site, and which the ad and review docs show getting the most attention, are the strongest clues, and a product the brand notably underplays despite selling it is its own signal worth naming. Mark the hero as a hypothesis where it rests on inference and route confirmation to the brand, because which product truly drives the business is something the rest of the strategy leans on.

**Bundles and starter packs.** How the brand combines products into packages, and what each package is doing. Bundles matter for two reasons: they are the brand's own attempt to lift the value of a single purchase, showing where it sees natural pairings, and a starter pack is often the brand's answer to a confused first-time buyer, which makes it a clue to the entry point and to how hard the brand thinks the first purchase decision is.

**Product-level differentiators.** What is genuinely better or different about each product relative to the obvious alternatives a buyer is choosing among. This is where raw material for creative angles lives, so be specific and concrete rather than repeating the brand's adjectives. Hold the asset-can-become-liability caution above all: verify that a stated differentiator is actually true and actually experienced as good, because a marketed strength hiding a drawback is a trap, and surfacing that is more valuable than transcribing the claim. Where a differentiator depends on a claim whose legal standing is uncertain, mark it as something to verify before it can be used in advertising, since whether the brand may say it is high-stakes and only the brand can confirm it.

**Patents, proprietary materials, and manufacturing edges.** Anything the brand owns or controls that a competitor cannot easily copy. These are the most durable differentiators because they are defensible, so they deserve special attention as the foundation of a position the brand can hold over time. Capture what is genuinely proprietary versus what merely sounds it, and note where a claimed edge is verifiable through a public record and where it rests only on the brand's assertion.

**Known product issues.** Where the product falls short, fails, or frustrates people. This is the counterweight to the differentiators and just as important, because product quality gates everything marketing can do: the best creative cannot sustain a product people are unhappy with, and an angle that ignores a known weakness will be met by it in the reviews and comments. The deep read of these lives in the reviews doc, so capture what is visible here and cross-reference there, weigh issues against the bias of unhappy people being louder, and where an issue is severe or widespread enough to constrain what the brand can credibly claim, say so plainly.

**LTV expansion vectors per product line, and the natural upsell cycle.** For each line, the path by which a customer naturally buys more over time, whether buying again, buying more, or moving into an adjacent product. Reason about the natural sequence a customer moves through and where the line tends to stall, and be honest that the true lifetime behavior is confirmed by the brand's data, so mark your read as a hypothesis where you cannot see it. Note especially whether a product is a one-time purchase or one that recurs, because a line with no natural repeat is a different business than one with a built-in cycle, and that distinction shapes which product the strategy should lead with.

**Use-case and need-state mapping.** Which products serve which use case and need-state, mapped from what the product structure and the brand's own site actually signal, for example the way the site sorts products by the kind of leak, the flow level, the time of day, or the life stage they are built for. Do not invent personas here. A product page cannot tell you who actually buys, so inferring demographics or psychographic profiles from the catalog produces fabricated personas that get mistaken for real ones, and that is the single most common way this doc goes wrong. Real personas are built later in the persona work, from actual buyer data, and the join between those personas and these SKUs happens there, not here. So stay with what is grounded: map each product to the use cases and need-states it is built for, drawn from the brand's own framing and filtering, and mark the mapping as the product's intended use rather than a claim about who buys it. Where different products plausibly serve the same person at different moments, capture that, because a single customer whose needs change over time is served by the whole line in sequence, which is its own strength. The question of which real persona each product actually converts is a genuine open loop for the persona work to close, not something to answer here.

**Entry-point product hypothesis.** Your best read of which product a customer most likely buys first from this brand, and why. The entry point matters enormously because it is where acquisition creative should concentrate and where the relationship begins, and getting it wrong points the whole top of the funnel at the wrong product. Reason toward it from the differentiators, the bundles, the decision-complexity of each product, and the economics, and name the tension that the easiest first yes is not always the most profitable product rather than resolving it prematurely. State it as a hypothesis with your reasoning, and route confirmation to the brand and the later customer work.

## Output

Open with frontmatter, then the sections, using these headers. Do not restate the instructions into each section. Bring the brand's product information forward under each, and mark every inference as one.

```markdown
---
brand: [brand-slug]
doc: website-and-product-audit
generated_on: YYYY-MM-DD
refresh_by: YYYY-MM-DD
sources_read: [the product surfaces and any brand-provided data you used]
---

# Website and product audit — [Brand Name]

## Full SKU list and product lines

## Top sellers and hero products

## Bundles and starter packs

## Product-level differentiators

## Patents, proprietary materials, and manufacturing edges

## Known product issues

## LTV expansion and the upsell cycle

## Use-case and need-state mapping

## Entry-point product hypothesis

## Open loops

## Appendix - Parker media links
```

Leave a clean named blank wherever a source does not exist rather than a guess, and be especially careful to mark the hero, the LTV path, the use-case mapping, and the entry point as hypotheses where they rest on inference.

## Open loops

End with the few consequential questions the website-and-product audit could not resolve.

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

Doc-specific thinking lens. Loops on a website-and-product audit tend to cluster around the entry-point-versus-hero question, around the use-case-to-real-persona join the persona work has to close, and around differentiators whose legal standing or product reality could not be confirmed from the outside. The recurring real question is which product the acquisition funnel should actually lead with given the economics, and the surface findings on bundles, navigation, and stated differentiators almost always consolidate up into that one underlying call.

Loops do not cover: spec inconsistencies between pages, missing product images, or site-copy refresh tasks. Those route to the website team, not to strategic open loops.

Mark any loop only the brand can answer so it routes to the brand, especially the true margins, the real best-seller, the actual repeat behavior, and any material or safety claim whose legal standing matters.

## When you refresh this

Product lines change as products launch, get reformulated, or are discontinued, and a reformulation can quietly invalidate older reviews and differentiators. This doc is re-run on a quarterly cadence, and a product launch or reformulation should trigger an update sooner. When you rebuild it, take the previous version in as context first, carry forward what still holds, update what moved, and note any product change that might have changed how the product is experienced. Say what each open loop's status is now, and watch for the hypotheses the brand or the customer work has since confirmed or overturned, because a validated hero product or entry point reshapes the whole strategy that depends on it.
