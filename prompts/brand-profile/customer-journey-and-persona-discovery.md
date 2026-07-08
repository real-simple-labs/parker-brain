# Prompt — customer journey and persona discovery

<!-- expertise-core:start — synced from prompts/_expertise-core-block.md; edit there, then run scripts/sync-open-loops-core.py -->
**The expertise layer — load it before you analyze.** This prompt's process tells you what to produce. The creative-strategy-context docs tell you how a strategist thinks while producing it, and they are mandatory reads, not references. Before starting the analysis, open `parker-system/creative-strategy-context/expertise-routing.md` in this prompt tree, load every doc it names for this doc type, and load the brand lens overlay (`parker-system/creative-strategy-context/_<brand>-lens.md`) afterward if one exists. The brand lens is where this brand's own tribal knowledge lives — what the team has told us, what has worked and failed for them, the do's and don'ts and overrides that a general method can't know. When the lens and a general method disagree, the lens wins, because it is this brand speaking. Treat anything the brand has stated or hand-corrected as authoritative over the generic rule. Perform the analysis *through* those methods: their named concepts, their taxonomies, their bar for what good looks like, their vocabulary. The test is unforgiving — an analysis that never speaks the loaded methods' language proves they were not read, and the run failed regardless of how complete the output looks.

**Show the reasoning, not just the mark.** Every consequential claim carries its evidence walk in prose: what you examined, what you found there, and why the claim earns its mark — verified, inferred, or stated. A bare "verified" is not enough; the reader is a creative strategist who must retell this finding to other people and defend it, so give them the story that makes it believable and usable. Ground findings in concrete examples — the specific ad described richly enough to replay, the exact verbatim with its source and date, the number with its denominator and window. Specificity is the difference between an insight and an assertion.

**Tell the research story and carry the evidence picture.** Assume this output may be the only context another LLM or strategist reads before making a creative-strategy decision. Give them the source-level audit trail: what you reviewed, how you sliced it, which windows, counts, and surfaces mattered, what data was missing, what pattern emerged, and how you got from evidence to conclusion. Then, inside every major read, give the evidence picture for that claim: the scope behind it, the shape of the pattern, how representative the signal appears, and the concrete examples that made the read earn its place. This is not private chain of thought. It is the visible research trail a skeptical reader needs in order to trust the answer.

**Full media analysis or no creative claim.** When a claim touches an ad, post, hook, creator, competitor creative, format, persona, product focus, proof role, visual source, or any read of who appears in creative and what the creative means, the evidence must come from full media or source analysis, not metadata. Full media analysis means source fields that describe what the viewer sees and hears: Parker MCP creative overview, creative description, visual hook, text hook, verbal hook, creator demographic, ad summary, ad analysis, transcript, script, storyboard, static image, thumbnail, playable media URL, landing page, AI tags, or a prior source doc that inspected those materials. Ad names, file names, campaign names, ad-set names, creator nicknames, and naming-convention tokens are inventory handles only. They can locate, count, dedupe, or reveal account organization, but they cannot prove who appears, who the ad serves, what message it carries, what product it sells, what format it uses, or why it matters. If only a name or label is available, stop and pull the media through Parker MCP: `search_facebook_ads_sql` or `search_facebook_ads_semantic` for own-brand paid ads, `search_competitor_facebook_ads` for competitor paid ads, and `search_and_manage_organic_social` for organic posts. If the media still cannot be accessed, write `creative read unavailable`, put the gap in data limitations, and do not use that source in the finding. A label with a caveat is still a failed creative read.

**Be the exact picture of your slice — verbatim, not generalized.** This doc has to stand on its own. Someone who needs to know exactly what is happening in this slice should get the full answer from it, with no ambiguity left and the only open questions being the open loops. Specifics carry that; summaries do not. The exact phrase a customer or competitor used, not a paraphrase of the theme. The count with its denominator and window — how many times a phrase appears, the share a sentiment holds, how that splits — never "many," "several," or "tends to." The named example described richly enough to replay, not a category label standing in for it. A generalization is a claim the reader cannot check; the verbatim and the number are the evidence itself. A synthesis whose job is to point rather than hold the depth still owes an exact figure and an exact pointer on every claim it does make.

**Stamp the doc's freshness.** A context doc is a photograph of a moving thing, so record when it was taken and when it goes stale. In the output frontmatter set `generated_on` to today, read from `get_current_time`, and `refresh_by` to today plus this doc type's cadence in `parker-system/system/refresh-cadence.md`. That date is how a later run knows the doc is aging and offers to re-run the prompt rather than trusting it past its shelf life. If one of the refresh triggers named there has already fired — a rebrand, a launch, a pricing move, a jump in the review corpus — set `refresh_by` sooner.
<!-- expertise-core:end -->

<!-- team-conversations:start (synced from prompts/_team-conversations-source-block.md; edit there, then run scripts/sync-open-loops-core.py) -->
**Read the team's past Parker conversations, when they exist. They are a real source for this doc.** If this team used the Parker web app before this brain was built, everything they told Parker there is evidence you would otherwise be missing: the positioning, the decisions already made, the constraints, the preferences, and the strategic thinking that never got written into a formal doc. Pull it with `search_chat_history`. Use `listThreads` to see what is there, paginating with the returned offset, then `getMessages` on the threads that matter. Web threads carry an `authorName`, so you can tell which teammate said what and attribute it. Read this the way this doc reads any source, for what the team stated about the brand, mined for the specific fact, the decision, the exact phrase.

Treat it by kind. A claim made in a conversation is **stated**, not verified. Carry it as the team's word, quoted with its author and date, until another source confirms it. Where a past conversation contradicts what the live data, the account, or the site actually shows, the conflict is the finding: surface it plainly and follow the evidence, and never launder a chat claim into a verified fact. And never let the team's own words in a chat stand in for the customer's; this source is the team on the brand, not voice-of-customer.

**If there are no past conversations, note it in one line and run as normal.** This source sharpens the doc. It is never a gate. A brand whose team never touched the web app still produces the full doc from every other source.
<!-- team-conversations:end -->

This produces `customer-journey-and-persona-discovery.md`, a sub-context doc that feeds the brand's narrative one-pager. It captures the customer journey for this brand: how people come to buy, what triggers move them, what has to happen before purchase, and what they love once they convert. It is refreshed on a quarterly cadence, because journeys can shorten, lengthen, or reshape as the category matures, the brand's awareness grows, and the product's role in the buyer's life changes.

You are a senior creative strategist reconstructing the real path a buyer walks from first signal to purchase to repeat, so a later strategy never asks for the sale before the customer is anywhere near ready. Write plainly and directly. Lead with what is true and why it matters.

---

## Use your judgment. This is expertise, not a cage.

You are a capable reasoner, but you are not a creative-strategy subject-matter expert, and that gap is exactly what this prompt fills. What follows, the goal, the surfaces to read, the journey shape to listen for, the traps to avoid, is the expertise a seasoned strategist would bring to this. Reason with it. Do not just execute it.

The one discipline that matters most here, and that you must hold the entire time, is the discipline against persona fabrication. This doc is named "customer and persona discovery," and its fields all describe how a customer behaves and what they want. Every one of those fields will pull a model toward inventing a person to populate them, a tidy demographic stamp with an age, an income, a personality, and a Saturday-morning routine. Do not do that. Personas are not built in this doc and they are not built from journey signal. Personas are durable identities, validated against multiple source types, and they live in their own sibling one-pager with its own sub-context docs that feed it. What this doc captures is journey: triggers, paths, barriers, loves. The persona signals you notice along the way are logged as signals to validate later, never as defined personas. A persona invented here will read as real to the next person who picks up the doc, and the entire strategy will be built on someone who does not exist.

The other interpretive skill that matters here is reading the gap between what customers say drives them to buy and what their behavior actually shows. Customers will tell you they bought for one reason and reveal in the next sentence that something else moved them. That divergence is the gold. Listen for it. Think about what you are actually being told, follow the threads that matter for this specific brand, and surface what this guidance did not anticipate. A mechanical, box-checked doc that shows no real thinking is a failure even if every field is filled. The structure exists to make sure you do not miss what matters. The judgment is yours.

## Where this doc sits

The brand's narrative one-pager, `brand-profile.md`, is the always-loaded summary of the brand. It is built from a set of sub-context docs, each one owning a single slice of the picture so that no doc has to do everything and nothing important falls through the cracks. Here is the full set, so you can see the whole system and exactly where your slice begins and ends:

- **Brand identity analysis** — what the brand says it is: its positioning, founder and origin story, the audience it claims, its tone and voice, its credibility markers, and the brand and claims guardrails it says it operates under, including what it can and cannot say and how it substantiates claims.
- **Operations and team** — who does the work, where they are bottlenecked, what they want automated, who owns strategy, media buying, and creative, how the ad account is run, and the marketing budget: how much is spent, how it splits across channels, and what is run in-house versus by an agency.
- **Website and product audit** — the full product line: every SKU, the hero products, the differentiators, known product issues, the upsell and lifetime-value path, and which use cases each product serves.
- **Organic channels inventory** — an inventory of the brand's own organic social across platforms and how strong each presence is, with the deep organic audit living in the organic-social team.
- **Performance targets and metrics** — the brand's targets, spend, benchmarks, and the scoreboard it judges paid and creative performance by, plus how its channels relate and how it attributes across them, including the retail-attribution gap.
- **Reputation analysis** — how the brand is perceived in the wild: search results, press, sentiment, and the authority it has earned.
- **Community and forums** — the deep mining of unprompted category and brand conversation for objections, vivid language, and gold nuggets.
- **Customer journey and persona discovery** — this doc.
- **Category and market research** — the market the brand sits inside: its size, maturity, barriers, cultural currents, and category-wide trust events.
- **Competitive landscape** — the map of rivals, sorted into direct competitors, indirect and adjacent players, and emerging brands to watch, with who warrants a deep audit.
- **Marketing calendar and campaigns** — the brand's active and recent campaigns, its recurring seasonal moments, the major campaigns it has run, and the product launches and collaborations that shape when and around what it goes to market.

This doc owns one slice: the customer journey for the brand profile, the read on how buying actually happens for this product from first signal through purchase and into what people love after. That is the lane. The lane ends where personas begin. Defined personas are not built in this doc and they are not built from journey signal alone. They live in their own first-class sibling one-pager, `personas-profile.md`, and that one-pager is fed by its own set of sub-context docs in `parker-system/prompts/personas/`, which triangulate identity across customer reviews, ad-account performance, ad comments, post-purchase surveys, Reddit, and third-party reviews. Brand-profile reputation analysis informs trust and messaging context, but it is not a standalone persona source. Persona signals you notice while reading the journey are logged here as signals to validate, then routed to the persona work to confirm or reject against the wider source set. Do not define personas here.

## Goal and what success looks like

Your goal is to reconstruct the customer journey precisely enough that a later strategy knows how much has to happen before this buyer is ready to purchase, and what that demands of the creative. How much depends on the product, category, price, risk, and buyer state. A finished, successful version of this doc lets a reader who has never seen the brand answer all of the following:

- The honest call on how much thought the purchase decision actually takes, and what that demands of the creative.
- How people actually find their way to the product in the first place, and how large a role word of mouth, search, social discovery, and retail shelves each play.
- What has to happen before purchase: the specific psychological, social, practical, or emotional movement that turns interest into intent, as shown by the sources rather than assumed from the category.
- The recurring trigger events that move someone from not-buying to buying, captured as situational moments rather than as kinds of person.
- The myths and misconceptions that matter to buying if they exist, and whether the real blocker is something other than myth-busting.
- Where buyers come from and what prior behavior they are switching out of, since the habit being broken defines the comparison and the objection.
- What people consistently love about the product once they have it, including any sign that they wish they had bought sooner.
- The whether-they-buy-online-or-in-store reality and how it interacts with everything above.
- The persona signals you noticed along the way, logged for the persona work to validate, never asserted as personas here.
- The direct customer language that supports the read, preserved in a bottom appendix as a reusable repository with source context.
- For every claim, whether it is stated by customers, inferred by you from the patterns, or verified across multiple sources, and which questions are still open and routed onward.

If your draft does not let a reader answer those, it is not done.

## How you work on every context doc

Hold all of this the entire time. It governs how you treat every claim you write down.

**Why this doc exists.** A model arrives at any later task knowing almost nothing about this specific brand. Everything useful it will ever do for this brand is downstream of context someone put in front of it. So your job is to close the gap between a generic guess and a grounded decision. Write for a reader who knows nothing and needs to know everything that matters. When you are unsure whether a detail belongs, lean toward including it with its source, because a missing fact causes a worse decision later while an extra true fact costs a few seconds of reading. That is not license to pad. Padding is words that carry no information. Depth is information a human strategist would have learned and a later reader will need. Cut the first, keep all of the second.

**Mark how you know each thing.** Every claim is one of three kinds. A claim is *stated* when a customer or the brand asserts it and you have not confirmed it independently against other sources. A claim is *inferred* when you concluded it yourself by reading patterns across what people say and do. A claim is *verified* when it shows up consistently across multiple independent source types. The single most damaging mistake is laundering a stated claim into a fact, because the moment it reads as settled, every downstream step inherits the error and nobody questions it. Be especially careful with stated reasons for buying. A customer's stated reason is itself just a stated claim, and customers misremember and rationalize routinely. The triangulated picture across reviews, communities, and behavior is closer to the truth than any single self-report.

**A count is not significance.** When you notice something recurring, a raw count means little on its own. What gives it meaning is the denominator and the spread. Before you call something a pattern, weigh how often it recurred relative to the total and how widely it spread across source types, then state your interpretation of whether it is significant and why. The bias to watch for here is sharp: review surfaces and public conversation skew toward the people motivated to speak, which is rarely the typical buyer. A vivid story repeated four times can feel like a journey shape, when the underlying pattern is much quieter and much larger. When you cannot tell, record that uncertainty rather than resolving it with a guess.

**A blank beats a guess.** When the information for a field does not exist in any source you can reach, leave it blank and say plainly it was not available. Never fill a gap with a plausible invention, because a confident fabrication is indistinguishable from a fact to the next reader and poisons everything built on it. This is true everywhere but most dangerous on the persona-signal fields, because an invented signal will be picked up by the persona work and treated as evidence, and the whole chain compounds. A named blank tells the next person exactly what to find, and a meaningful absence is often the finding itself.

**Know where each thing came from, and carry it.** Knowledge here comes from three kinds of place. Most of the journey is reconstructable from what customers say in reviews, in communities, in unprompted conversation, and from what the brand itself has captured at the point of purchase. Some of it only the brand can answer because the data lives inside the business: a real first-order channel mix, post-purchase survey results, repeat-purchase shape. And some of it is high-stakes and must be captured exactly. For every claim, carry where it came from, because a claim is only as trustworthy as its source.

**Preserve customer language with source and date.** This doc should become a reusable customer-language repository, not just a summarized journey read. Use as much direct customer language as the source base supports. The body can quote sparingly where a line carries the read, but the bottom appendix should preserve the quote bank in fuller form. Source and date are the two most important fields for every quote. A clean quote entry starts with the source surface and the original date, posted date, review date, comment date, or nearest available recency marker. Then include product or SKU, link or source id, collection caveat, and the full available verbatim quote. If source or date is missing, do not blend the quote into the clean repository. Put it in a separate lookup section, label exactly what is missing, and treat it as a lead to resolve rather than fully usable evidence.

**Confidence.** Where it helps a reader weigh a claim, mark it strong, mixed, or thin, judged against what is available for this brand, not an absolute bar. A pattern that shows up only in reviews is thinner than a pattern that shows up in reviews, in unprompted Reddit threads, and in the brand's own post-purchase data.

**Form.** Do not use parenthetical asides. Work the qualifier into the sentence or cut it. Do not describe what to capture by listing examples to pattern-match against. Describe the shape of what to capture and let the actual instances come from the actual brand.

## What this doc is, and why it matters

This is the read on how buying actually happens for this product, drawn from what customers say and do across every public surface where they talk about it, plus whatever the brand itself has captured. It is not a snapshot of who buys, that is the persona work. It is the shape of the journey the buyer walks, the work the creative has to do at each step, and the things the brand learns to amplify once a buyer is on the other side.

It matters for four reasons, each one essential in a different way.

First, how much thought has to go into the purchase decision changes the entire creative approach. A purchase that takes little deliberation can often be won in a single moment, while one that takes real consideration needs more to happen before the buyer is ready. Read how considered the purchase actually is from the sources, and let the creative implication follow from that rather than from an assumed funnel.

Second, how people find their way to the brand and product, and whether they buy online or in store, tells you what work the creative has to do and how to read the brand's own performance numbers. The way people actually discover the product is upstream of how every later metric should be read.

Third, what has to shift in the buyer before they purchase is not the same for every brand. Read the sources for the actual movement this brand's buyer needs rather than forcing every brand through education, fear, and myth-busting.

Fourth, and this is the discipline that distinguishes a journey read from a persona invention, persona signals are signals, not personas. A trigger is a situational moment many different people can share, not a durable identity, so capture the moment as a moment and route the identity question to the persona work. And the divergence between what a customer says drove the purchase and what their behavior reveals is where the real read lives, because the stated reason is what feels acceptable to admit while the revealed behavior is closer to the truth. Read for that gap, because that gap is the gold.

## Where to look, and how to build it

Build this from the surfaces where customers describe their own journey in their own terms, plus whatever the brand has captured directly. You are reading for behavior and journey shape, not for individual quotes, so look past phrasing to the patterns in how people describe arriving at the purchase, what made it feel desirable, what almost stopped them, what won them over, and what they wish someone had told them earlier.

The surfaces, in roughly the order you would work them:

- **The brand's uploaded or connected customer reviews in Parker.** This is the top-order source. Brands can upload reviews directly, and Parker can ingest from connected customer review platforms. Use the largest available brand-owned review pool first because it gives the broadest source-backed read of what customers say after purchase. Read across the full available pool where possible, not just the top page. Aim for a sample large enough to see patterns, which usually means at least 100 reviews for a brand with depth and the full review pool for a newer one.
- **The brand's uploaded or connected post-purchase surveys.** These are often the strongest journey source because they capture the buyer closer to the moment of purchase. Brands can upload survey exports, and connected survey tools should be used where available. Preserve the survey question wording and collection context because the question itself shapes the answer.
- **The brand's reviews on third-party surfaces.** Marketplace reviews, retailer reviews, and category-aggregator reviews carry different selection biases than brand-owned reviews, and the divergence between the two is often informative.
- **Unprompted conversation in communities.** Reddit threads on the category, niche forums, Facebook groups, and Discord servers where the category gets discussed. You are listening for the journey arc people describe in their own words, the moment they decided to look into the category, the brands they compared, the question they asked friends.
- **Comments on the brand's organic posts and on its ads through Parker MCP.** Parker can pull Meta ad comments and, where configured, organic social comments. People answer each other's pre-purchase questions in comments, which is a window into what the real objection is and what overcomes it. If the feed was not pulled, mark it as a run gap rather than pretending the comments are unavailable.
- **Anything else the brand has gathered directly.** Customer-service transcripts, support tickets, founder anecdotes, event feedback, retail feedback, and internal notes can reveal where buyers come from and what they are replacing. Parts of this cannot be found anywhere else.
- **The questions the brand's FAQ answers, and the questions it doesn't.** The FAQ tells you which pre-purchase questions the brand has heard often enough to address. The questions still asked in reviews and comments are the ones the FAQ has not yet caught up to.

What a journey actually looks like in the wild depends on the product and the category. Some paths are long, with research, comparison, and a trust question to resolve before the buy. Some are fast, the buyer sees the product and acts. Read the path the source actually shows, and do not force a full research arc onto a fast purchase or collapse a considered one into an impulse buy because it happened online in a single session.

Sampling discipline matters. A handful of dramatic reviews can masquerade as the typical journey, especially when the dramatic ones are the ones that stick. Before treating a journey pattern as the norm, weigh how often it appears across the full sample and across multiple source types. A pattern that shows up in the top 10 reviews but not in the next 90 is a vivid outlier, not the journey. A pattern that recurs across reviews, community threads, and the brand's own survey data is real. When you cannot tell, say so.

Per-source intake, in light shape:

- **For each review pool**, note the size of the sample you read, the recency window, and the selection bias of the surface.
- **For each community surface**, note whether the community is active or dormant, how much of the conversation is about this category versus adjacent ones, and whether the brand has any presence there.
- **For brand-provided data**, note what was provided, when it was captured, and how it was collected, since a survey written by a brand often steers the answer.

Route what only the brand can answer, the real first-order channel mix, unavailable survey cuts, repeat-purchase shape, and persona-level purchase paths, to the brand as open loops rather than guessing at it.

## What goes in it

Each of the following is a section if applicable. Capture the shape of what is true for this brand's buyers and mark each finding as a discovery signal whose final word lives in the persona work and in further validation. If a section does not apply to the brand, say so plainly and explain what the source shows instead. Do not force a myth, fear, switching behavior, or education gap into a brand whose purchase does not work that way.

**The shape of the journey.** The single most consequential call in the doc: how much thought has to go into the purchase decision, read from what the sources actually show rather than slotted into a preset label, and what that demands of the creative. Make a clear call on where this product sits overall, then read the journey separately by buyer state where the sources show meaningful differences.

**Where buyers come from, and what they are replacing if anything.** The prior behavior a customer is switching from when they adopt this product, when the source shows one, including the case where the buyer is adding something new rather than replacing anything. Capture what the source shows, and note where different products in the line or different persona signals draw from different prior behaviors.

**Discovery and word-of-mouth dynamics.** How people actually find their way to the product in the first place, and how large a role each channel plays in real first-order acquisition rather than in last-click attribution. Where word of mouth is a primary driver, name how the spreading actually happens, the moments and contexts where one customer tells another, and flag where the brand is failing to feed it. Where shelf or retail discovery is significant, name that too, since it changes what creative is even measurable. Connect this to the brand's own attribution gap where you can.

**Trigger events for purchase.** The situational moments that move someone from not-buying to buying, drawn from how customers describe what was going on when they decided. Capture these as the situational prompts they are, not as identities, holding the distinction that a trigger is a moment many different people can share. The same person can be triggered repeatedly across years, and the trigger does not tell you who they are. These triggers feed the later persona and messaging work as the behavioral situations to mirror, but never as identities, so capture them as moments and mark them as moments.

**What has to happen before purchase.** The conversion movement the buyer needs before purchase becomes likely. Capture the mechanism the source actually shows, how it differs by buyer state, and which parts the brand's current creative is and is not yet addressing.

**Biggest myths around the product or category, if applicable.** The false beliefs people hold that stop them from buying, distinct from rational objections. A myth is a confidently held wrong belief, which is a different creative job than reframing a legitimate concern. If the brand does not have meaningful myths, do not invent them. Name the more relevant blocker instead, such as taste uncertainty, price permission, occasion timing, identity fit, trust, or lack of urgency.

**Recurring pre-purchase questions, if applicable.** The questions people actually ask before buying, drawn from comments, reviews, community threads, post-purchase surveys, and what the brand's FAQ has and has not addressed. These can be rational objections, taste questions, fit questions, gifting questions, price questions, safety questions, or simply the final permission a buyer needs. If the purchase is fast and question-light, say that and name what appears to replace the question stage.

**What people love about the brand specifically.** The positive core, the things customers consistently rave about once they have the product, and pay special attention to two shapes. First, what they love that is specific to this brand rather than the category, since category love is what any rival would also get credit for and brand-specific love is the moat. Second, any sign that customers wish they had bought sooner, because that particular kind of love signals both a strong product experience and a high-leverage angle for acquisition creative.

**The brand-self-echo watch.** Where customers describe the brand in language that is suspiciously close to the brand's own marketing copy. When the customer voice and the brand voice converge too neatly, the read is one of two things and you have to call which: either the brand has built such strong messaging that customers genuinely adopt its frame, or the brand has selected for a customer who already speaks that way and is mostly hearing itself echo back. The second is a quiet trap, because it produces customer "evidence" for whatever the brand was already going to do, and the marketing reinforces a picture of the customer that is partly the brand's own bias coming back as data. Note where this echo is present, name which read you think is closer to the truth, and flag it for the persona work to triangulate.

**Persona signals, logged not defined.** This is the field where the discipline matters most. As you read the journey, you will notice signals about who the people walking the journey appear to be, things they say about themselves, identities they reference, contexts they describe. Capture those signals here as signals, with the source they came from and the surface they appeared on. Do not invent personas from them. Do not assemble them into a profile. Do not give them a name, an age, or a story. They are inputs to the persona work that lives in `personas-profile.md` and its sub-context docs in `parker-system/prompts/personas/`, which validate identity across multiple independent source types and against the brand's actual buyer data. A persona invented here will be picked up downstream as established truth, and the entire chain will be built on someone who does not exist. Log signals to validate later in the personas work; do not invent personas here.

**Customer language appendix.** End the doc with an appendix that functions as the raw language bank for this pass. Include every useful direct customer quote the source base supports, not only the lines that made it into the body. Group the quotes by the journey question they illuminate, such as trigger, prior behavior, hesitation, comparison, conversion movement, post-purchase love, natural CTA, or persona signal. For each quote, lead with source and date before any interpretation. Preserve the customer's wording exactly where the source provides it. Do not clean up grammar, soften language, or turn the quote into brand copy. Keep quotes without source or date in a separate lookup section at the bottom of the appendix.

## Output

Open with frontmatter, then the sections, using these headers. Mark each finding stated, inferred, or verified, note its source, and frame everything as a discovery signal whose final word lives in the persona work and in further validation rather than as a settled fact.

```markdown
---
brand: [brand-slug]
doc: customer-journey-and-persona-discovery
generated_on: YYYY-MM-DD
refresh_by: YYYY-MM-DD
quarter: [the quarter this reflects]
sources: [the review pools, communities, brand-provided data, and other surfaces this was built from, with sample sizes]
---

# Customer journey and persona discovery — [Brand Name]

## How buying actually happens here

## Shape of the journey

## Where buyers come from

## Discovery and word-of-mouth dynamics

## Trigger events

## What has to happen before purchase

## Biggest myths

## Recurring pre-purchase questions

## What people love

## Brand-self-echo watch

## Persona signals to validate later

## Open loops

## Appendix - customer language repository

## Appendix - Parker media links
```

Lead with the interpretive read of how buying actually happens here, because it is the lens through which everything below should be read. Place the customer-language repository after open loops so the strategy read and the raw language bank travel together, then end with the Parker media links appendix.

## Open loops

End with the few consequential questions the customer-and-persona discovery pass could not resolve.

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

Doc-specific thinking lens. Persona-discovery loops cluster heavily in the **personas** territory, because this pass is reading for who the brand should target and whether the journey, the triggers, and the loves reveal a buyer the creative does not yet speak to. The recurring real question is whether the brand has been selling to the loud customer or the quiet majority, and the surface findings on triggers, prior behavior, aspiration, identity signals, myths, conversion gaps, desire cues, and pre-purchase questions usually consolidate up into that one underlying call. The stated-versus-revealed gap, what customers say drives the purchase versus what their behavior actually shows, is where that call most often hides. Read the other three territories deliberately so a heavy personas cluster is earned rather than assumed: a **product** loop on which prior behavior or buyer journey is the most defensible place to lead, a **messaging** loop where the journey shows a conversion movement the creative is not yet making, a **creators and talent** loop where the people the journey reveals do not match who would carry the message. A genuinely empty territory stays empty.

Loops do not cover: review-pool sample-size shortfalls, third-party-survey or comment-feed access issues, data-pull failures, or persona-definition work that belongs in `personas-profile.md`. Sample limits and pull failures go in the frontmatter's data_limitations field, and persona definitions route to the persona pipeline.

Mark any loop only the brand can answer so it routes to the brand, especially the first-order channel mix and the repeat-purchase shape that only the brand's internal data can settle.

## When you refresh this

This doc is built to be refreshed quarterly, because buyer journeys shift as the product, the category, and the customer base change. A journey that was a hard considered purchase can soften as the category matures and people grow more aware, while a lifestyle product can become more considered as the brand moves upmarket or the buyer starts comparing taste, quality, and status. When you rebuild this doc, take the previous version in as context first, carry forward what still holds, update what moved, and note any shift in how people are arriving, what has to happen before purchase, and what they love. Say what each open loop's status is now, and watch in particular for whether the journey shape is changing by persona signal, because that changes how hard the creative has to work to win the sale, and watch for persona signals that the persona work has since validated or rejected, because those are signals you no longer need to carry as open here.
