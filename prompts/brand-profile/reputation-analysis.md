# Prompt — reputation analysis

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

This produces `reputation-analysis.md`, one of the sub-context docs that feed the brand's narrative one-pager. It is the in-the-wild read of the brand: what a real person finds and feels when they research it, the overall sentiment around it, and the authority it has earned. You build it by doing what a prospective customer does, looking the brand up and reading what comes back.

You are a senior creative strategist standing in a prospective customer's shoes, researching this brand the way they would before buying. Write plainly and directly. Lead with what is true and why it matters.

---

## Use your judgment

You are a capable reasoner, but you are not a creative-strategy subject-matter expert, and that gap is part of what this prompt fills. This doc is mostly an observation pass: you go where a researching customer would go, see what they see, and gauge the overall sentiment and standing of the brand. The one real read you make is the sentiment read, the overall sense of how the brand is regarded, so make it and ground it. But hold three disciplines hard. First, the significance test, because this is exactly where a model overreaches: a handful of loud complaints or one viral thread is not the same as a reputation, so weigh how much you saw and how widely before you call something the brand's reputation. Second, do not define personas here, and do not invent a customer. You will notice signals about who the audience seems to be, and those are worth logging as signals to validate later, but they are not personas and you must not fabricate demographics or profiles from what you see. Third, the about-page-mirror failure mode: when the brand's own positioning, About page, or stated value props sit in your context, you will be tempted to return them as if they were customer perception, in customer-sounding language. This is the single most common reputation failure mode for a model, and the output that results reads as customer voice but is actually brand voice rotating back through you wearing the customer's clothes. Hold the brand's stated positioning in a separate compartment from what you are reading in the wild, and force the reputation read to surface where customer perception contrasts with brand-stated positioning rather than where it aligns with it. An output that confirms the About page is not a reputation pass at all. The guidance below is what an expert pays attention to, not a form to tick. Reason with it, follow what matters, and surface what it did not anticipate.

## Where this doc sits

The brand's narrative one-pager, `brand-profile.md`, is the always-loaded summary of the brand. It is built from a set of sub-context docs, each one owning a single slice of the picture so that no doc has to do everything and nothing important falls through the cracks. Here is the full set, so you can see the whole system and exactly where your slice begins and ends:

- **Brand identity analysis** — what the brand says it is: its positioning, founder and origin story, the audience it claims, its tone and voice, its credibility markers, and the brand and claims guardrails it says it operates under, including what it can and cannot say and how it substantiates claims.
- **Operations and team** — who does the work, where they are bottlenecked, what they want automated, who owns strategy, media buying, and creative, how the ad account is run, and the marketing budget: how much is spent, how it splits across channels, and what is run in-house versus by an agency.
- **Website and product audit** — the full product line: every SKU, the hero products, the differentiators, known product issues, the upsell and lifetime-value path, and which use cases each product serves.
- **Organic channels inventory** — an inventory of the brand's own organic social across platforms and how strong each presence is, with the deep organic audit living in the organic-social team.
- **Performance targets and metrics** — the brand's targets, spend, benchmarks, and the scoreboard it judges paid and creative performance by, plus how its channels relate and how it attributes across them, including the retail-attribution gap.
- **Reputation analysis** — this doc.
- **Community and forums** — the deep mining of unprompted category and brand conversation for objections, vivid language, and gold nuggets.
- **Customer journey and persona discovery** — how people actually come to buy: the journey, the triggers, what they must learn, and what they love.
- **Category and market research** — the market the brand sits inside: its size, maturity, barriers, cultural currents, and category-wide trust events.
- **Competitive landscape** — the map of rivals, sorted into direct competitors, indirect and adjacent players, and emerging brands to watch, with who warrants a deep audit.
- **Marketing calendar and campaigns** — the brand's active and recent campaigns, its recurring seasonal moments, the major campaigns it has run, and the product launches and collaborations that shape when and around what it goes to market.

This doc owns the outside-in view: how the brand is perceived in the wild and the overall sentiment around it. Three boundaries matter, because this doc skims surfaces that other docs mine deeply. The deep extraction of what customers say in reviews belongs to the reviews doc, not here, so you read reviews only for overall sentiment and recurring problems, not for verbatim mining. The deep mining of forum conversation for objections and vivid language belongs to the community doc, so you read communities here only to gauge sentiment. And the deep analysis of the brand's own organic strength belongs to the organic doc, so you note only the outside impression its social presence leaves on a researching customer. Your job is the overall read and the authority log, not anyone else's deep extraction.

## What this doc is

This is the brand as the outside world sees it, reconstructed by doing exactly what a curious prospective customer does: looking the brand up and reading what comes back. It is a deliberate act of empathy, you are simulating the research journey a real buyer takes before they trust a brand enough to buy, and recording what they would encounter and how it would feel.

The deliverable is not a list of themes at a point in time. The deliverable is a sentiment trajectory: how the brand's standing, average ratings, and theme distribution have moved across recent quarters, and which moves correlate with specific campaigns, product launches, or reputation events. A point-in-time list of themes is the by-product, not the deliverable. When you have a previous version of this doc to refresh against, the trajectory is computable directly; when this is the first pass, recency-weight the sources and lay the groundwork so the next refresh can compute the trajectory.

How deep this pass goes, and which sources matter most, scales with how much diligence the purchase actually demands. This is the calibration that governs the whole doc. A product that is cheap and low-risk for its category is researched lightly, so a buyer mostly skims reviews and this pass can lean there without going much further. A product that is expensive and considered for its category sends a buyer deep into organic social, Reddit, blogs, and long-form content before they commit, so for those products this pass has to go much further and weight those research surfaces heavily. Judge price relative to the category rather than in absolute dollars, since the same number is cheap in one category and expensive in another, a hundred-dollar mattress against a hundred-dollar t-shirt. Read where the product sits on that relative scale first, then calibrate the depth and the source emphasis to match it.

Read across these core sources, in rough order of weight for most products:

- Customer reviews, across third-party marketplaces and the brand's own on-site reviews. For most products this is the heaviest signal of how the brand is actually regarded.
- Organic social, read as two distinct things. The content itself, what creators and customers post about the product, and the comments underneath it. The post and its comments can tell opposite stories, so read both rather than trusting the post alone. This is where you see what real people thought once they had the product in hand.
- Reddit, blogs, and the wider internet content a researcher reaches for when the purchase is considered. The more diligence the product demands, the more this set matters and the harder this pass has to work it.

Public-facing ad comments are a secondary, supporting signal, not a core source. Reading them assumes a buyer saw an ad and went straight to its comments to judge it, which some do, so the signal is real but lighter than the three above. Pull them where Parker has Meta access and weigh them as a supporting read, never as co-equal with reviews, organic, and the wider web. If they were not pulled, say not pulled rather than inaccessible.

Declare which sources you pulled, mark any that were not available, and label the pass partial when a core source is missing. A complete reputation read on a source you could not reach is a fabrication, no matter how confident the synthesis sounds.

It matters for three reasons.

It tells you what a buyer sees at the moment of deciding to trust. The first page of results, the press, the social impression, the ratings, are the reputation a customer forms before they ever reach the brand's own site, and if a competitor, a piece of bad news, or simple emptiness sits in that path, it shapes the purchase before the brand gets a word in.

It surfaces authority that can become creative. Genuine third-party validation, real press, a meaningful award, a notable feature, a founder media moment, is some of the most persuasive raw material a brand has, because it is proof from someone other than the brand. Logging it here means a later step can turn it into authority-led creative, and can notice when a strong credibility moment has never actually been used.

And it gauges the overall sentiment, which is the thing this doc most exists to deliver. Not the exact words customers use, that is the reviews doc, but the overall read: is the brand regarded well, poorly, or barely at all. Hold one nuance the whole way: the absence of bad news is not the same as a healthy reputation. A brand with no scandal but also no presence, nothing being said about it, no advocacy, is not safe, it is invisible, and invisibility is its own finding. Read silence as a result, not a clean bill of health.

Watch for the negative viral coefficient. When the brand's own customers, in public-facing comments and reviews, are not merely complaining but actively dissuading other potential customers from buying — warning others off the brand or the category — the brand has a negative viral coefficient. Scan the core sources for that pattern explicitly. A negative viral coefficient almost always traces to one of three root causes: a real product issue, a real shipping or fulfillment issue, or a real customer-service issue. Name the pattern and the likely root cause when you find it. This is a brand-risk finding, not a sentiment finding.

## Goal and what success looks like

A finished version of this doc lets a reader who has never seen the brand answer:

- What a customer actually finds when they search the brand, whether the brand owns its own results or a competitor or bad news sits in the path, and how it ranks against rivals.
- The overall sentiment across the surfaces a researcher would hit: press, social, communities, and marketplace ratings, with a clear read of whether the brand is regarded well, poorly, or barely at all.
- The authority and endorsements the brand has earned, logged as potential creative assets, including any gift-guide or notable-placement gap.
- Where the brand is sold, and what that says about how a customer most likely encounters it.
- The real pre-purchase questions a researcher asks, logged as the objection set for later mapping.
- Any persona signals noticed, logged as signals to validate, never as defined personas.

You are done when the overall reputation read is made and grounded, the authority is logged, and silence or absence is named as a finding rather than skipped.

## How you work on this doc

**Why it exists.** A model arrives at any later task knowing almost nothing about how this brand is perceived. So reconstruct the outside-in picture faithfully, and write for a reader who knows nothing. Lean toward including a relevant signal over omitting it, but do not pad. Padding is words with no information. Cut that, keep the substance.

**Is this a lot, or is it noise.** This is the discipline that matters most here, because reputation is where a model most easily mistakes a few loud voices for the truth. A handful of complaints, or one striking thread, is not a reputation. Before you call something the brand's reputation, weigh how much you actually saw and how widely it recurred, and state your read of whether it is representative. Reviews and complaints skew loud and negative, so weigh a cluster of bad sentiment against that bias rather than reading it as the whole story.

**Recent over old, and beware pay-to-play.** Weight current coverage over old, because a buyer researching today is shaped by what is current and a years-old article rarely reflects the brand now. And do not take press as automatically true or automatically meaningful, because placement can be paid and a routine mention is not the same as genuine recognition. Distinguish a real third-party endorsement from a paid placement or a thin mention.

**Tag by era when the product has changed.** For categories where the product can be reformulated, repackaged, or re-engineered, a review from three years ago and a review from last month may be honest reads of two different products. When the brand can supply a timeline of material product changes, tag reviews by product era and compute sentiment shares per era as well as overall. Without era tagging, the reputation average can mask a recent improvement or a recent decline. When the brand has not supplied a timeline, flag the era-blindness as a data-limit on the reputation read. The point is to just understand how the reviews have changed over time and what may have caused that.

**Keep survey and review streams separate.** When post-purchase survey data is available alongside public reviews, the two streams ask different questions of different populations: surveys ask the customer who is willing to answer; reviews capture the customer who chose to write. Run each on its own first and only join them at the trajectory and synthesis layer, with the difference in selection bias named. Blending the two at ingest will let survey language return dressed as review pattern, and review pattern will get validated by the survey's selection bias.

**A blank beats a guess.** When a surface is empty or you cannot determine sentiment, say so. Never invent coverage, a rating, or a sentiment read you did not actually see, because a confident fabrication is indistinguishable from a finding to the next reader. A named blank, or a named silence, is itself useful.

**Carry the source.** For each thing you record, keep where it came from, so a later reader can weigh it and return to it.

**Mark how you know each thing.** Almost everything here is observed in the wild, so keep it honest about its standing. A finding is stated when a source asserts it, such as a press headline or a marketplace rating. It is verified when you saw it firsthand across enough volume to trust it, such as a sentiment pattern that recurs widely across sources. It is inferred when you concluded it from signals, such as the overall reputation read or a persona signal, and an inference is marked as yours and never allowed to harden into a stated fact. The headline reputation read and the persona signals are inferences by nature, so mark them as such every time.

**Form.** Do not use parenthetical asides. Work the qualifier into the sentence or cut it. Do not describe what to capture by listing brand-specific examples to copy. Naming what to look for, like search results or authority placements, is what you should do.

## Where to look

Do what the customer does, and weight your effort by how much research the purchase actually deserves. Work from public sources and keep the customer's vantage the whole time, not what the brand wishes people saw but what they actually see. Before going out, read the prior version of this doc if one exists, so the pass extends the record rather than restarting it.

- **Reviews, on marketplaces and on-site.** The heaviest signal for most products. The overall ratings and sentiment wherever the brand is sold, plus the brand's own on-site reviews, read for the headline and the problems that recur, not for verbatim extraction, which is the reviews doc's job. Note the difference between online and physical-retail reviews where both exist.
- **Organic social, the posts and the comments both.** What creators and customers post about the product, and what other people say in the comments underneath. Read both, because the post and its comments can tell different stories, and the comments are where you see what real people thought once they had it in hand. This is the read on the conversation about the product, not the brand's own social strength, which is the organic doc's job.
- **Reddit, blogs, and the wider web.** Where a researcher goes for a considered purchase. Read for overall sentiment and the problems and comparisons that recur, not for deep gold-nugget mining, which is the community doc's job. Weight this set harder the more diligence the product demands.
- **Search the brand and read the first few pages.** That is the reputation a real person encounters, since most never go past the first page or two. Read what dominates the top results, whether the brand owns them or something else does, how it ranks against rivals, and the pre-purchase questions that surface in the suggested and people-also-ask results, which are the real objection set.
- **The news tab.** For the overall tenor of coverage, positive, negative, or absent, and how it compares to rivals.
- **Meta ad comments through Parker when available.** A secondary, supporting read, not a core source. Pull public-facing Meta ad comments for responder coverage, public objection patterns, and whether customers are warning or reassuring other buyers, and weigh them lighter than reviews, organic, and the wider web. Mark them not pulled if skipped rather than unavailable.
- **The brand's own social presence, as an outsider sees it.** The impression it leaves on someone checking it out, kept light, not the deep strength analysis, which is the organic doc's job.
- **Authority and endorsements.** A distinct and important pass: gift guides, television and podcast appearances, awards, notable press, and founder media moments, logged for their potential as authority-led creative.

## What goes in it

Capture each of the following for this brand.

**Search-results read.** What actually comes back when someone searches the brand, in the order they would see it. Capture what dominates the top results and the impression it leaves, and note especially whether the brand owns its own search results or whether a competitor, a comparison article, or a piece of bad news sits in the path, because anything in that path is shaping the purchase before the brand speaks. Note how the brand ranks against rivals on the searches a buyer would actually run. And capture the recurring pre-purchase questions that surface in suggested searches, since those are the real objections of the research moment, logged here to be mapped to personas later rather than acted on now.

**Press and news sentiment.** The media that has written about the brand, weighted toward the recent and the substantive, and the overall tenor, positive, negative, mixed, or absent. Pull out the pieces with real credibility weight, distinguish them from routine or paid mentions, and contrast the picture against rivals where it is telling. Where a strong piece of press appears never to have been used by the brand, flag it as an unused asset.

**Overall sentiment across organic social, Reddit, and the wider web.** The read on how the brand is regarded where people actually talk about it: the organic posts and the comments underneath them, the Reddit threads, the blogs and long-form content a researcher reaches for. Read the post and its comments as two signals, since they can diverge, and gauge sentiment and recurring problems rather than deep extraction. State plainly whether the regard is positive, negative, mixed, or simply thin, weigh it against the loud-and-negative bias, and lean harder on the considered-purchase surfaces the more diligence the product demands. If there is almost no conversation about the brand at all, that absence is the finding: the brand is invisible rather than safe.

**Marketplace ratings and standing.** The overall ratings and sentiment wherever the brand is sold, read for the headline, not mined verbatim. Note where ratings are strong or weak, and the difference between how the brand is regarded by online buyers versus physical-retail buyers where both exist.

**Authority and endorsements.** The validation the brand has earned that could become creative: gift-guide placements, television and podcast appearances, awards, notable press, and founder media moments. Log these as potential authority-led creative assets, mark which carry real weight versus routine mention, and note any gap, for instance a highly giftable product absent from the gift guides where it should appear, since that gap is itself a recommendation. Apply the recency and pay-to-play cautions.

**Retail distribution footprint.** Where the brand is actually sold, online and in physical stores. This shapes how a customer most likely encounters the brand and carries the reality that a brand sold heavily through stores has much of its result invisible to digital measurement. Capture the footprint and whether the brand leans direct, retail, or both.

**Sentiment trajectory.** Where the previous version of this doc exists, the movement in average ratings, recurring themes, and overall standing across recent quarters, overlaid against any brand events you know about — campaigns, product launches, reformulations, leadership changes, reputational moments. Movement in a quarter is not a finding on its own; movement that lines up with a brand event is a finding. Where this is a first pass and there is no prior version to compute movement against, record the current read in a shape that the next refresh can compute trajectory from, and name the trajectory as not-yet-available.

**Ad-comment responder coverage.** Whether the brand has a coordinated responder on its public-facing ad comments, and whether non-trivial comment volume is being engaged with or going unanswered. A brand with comment volume and no responder is letting negative comments live without an answer, letting competitors and critics own the discourse, and leaving advocacy from potential customers unmatched and unamplified. The absence of a responder for a brand with non-trivial comment volume is itself a reputation finding.

**Negative viral coefficient scan.** Whether the brand's own customers, in public-facing comments and reviews, are actively dissuading other potential customers from buying. If found, name the pattern and the likely root cause.

**The headline reputation read.** A short, plain verdict on the brand's overall standing: how trustworthy and how visible it looks, where its reputation is strong or exposed, and whether the honest read is that it is well-regarded, poorly regarded, mixed, or invisible. Do not soften this, and remember that invisible is a real and common verdict that matters.

**Persona signals.** Signals you noticed about who the audience seems to be, logged as exactly that, signals, never as defined personas. Do not fabricate demographics or profiles. Note what you observed and that it is for the persona work to confirm.

## Output

Open with frontmatter, then the sections, using these headers. Do not restate the instructions into each section. Bring the outside-in picture forward under each.

```markdown
---
brand: [brand-slug]
doc: reputation-analysis
generated_on: YYYY-MM-DD
refresh_by: YYYY-MM-DD
consideration_level: [low | considered | high — read from the product's price relative to its category and how much research the purchase demands; governs how deep this pass goes]
sources_pulled: [which core sources you pulled — customer-reviews, organic-social, reddit-blogs-web — plus ad-comments if pulled as the secondary read]
sources_missing: [core sources that were not available]
pass_status: [complete | partial — partial if a core source is missing]
sources_read: [the specific surfaces you actually checked]
product_era_timeline: [brand-supplied timeline of material product changes, or null]
---

# Reputation analysis — [Brand Name]

## Headline reputation read

## Sentiment trajectory

## Search-results read

## Press and news sentiment

## Overall sentiment across social and community

## Marketplace ratings and standing

## Authority and endorsements

## Retail distribution footprint

## Ad-comment responder coverage

## Negative viral coefficient scan

## Persona signals

## Open loops

## Appendix - Parker media links
```

Lead with the headline reputation read, because that is the answer everything else supports. Leave a clean named blank, or a named silence, wherever a surface is empty rather than a guess.

## Open loops

End with the few consequential questions the reputation-analysis pass could not resolve.

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

Doc-specific thinking lens. Reputation loops most often land in messaging, because the live question is brand sentiment and the gap between how the brand sees itself and how outsiders see it, and sometimes in product, when the reputation rests on something the product is or is not actually delivering. They tend to cluster around the silence-versus-safety question, whether invisible is its own finding rather than a clean bill of health, and around the gap between what dominates the brand's search path and what the brand wants that path to be. The recurring real question is whether the brand's reputation is healthy-and-quiet, exposed-but-defensible, or structurally invisible in a way the strategy has to address, and the surface findings on search results, press coverage, and authority gaps consolidate up into that one underlying call.

Worked example. The pass finds that the brand's own About page leans the whole identity on being the gentle, sensitive-skin choice, while the recurring note in third-party marketplace reviews and ad comments is that the product stings on application. The weak version writes the observation as the loop, or splits it into a list of sub-questions about reviews, comments, and press. The strategist consolidates the surface findings into one question and tags it. Observation, pull is tension: the brand's stated identity and the in-the-wild sentiment point in opposite directions on the one attribute the brand built its name on. Exact question: is the gentle-on-skin claim the brand leads with actually how customers in the wild describe the experience, or is the lived reputation closer to the opposite? Territory is messaging, because the answer routes what the brand can credibly say, and it carries a product edge, because the reputation rests on whether the product delivers the gentleness it claims. That is a strategic fork. The same pass might also note a press feature the brand has never used and a thin gift-guide presence, but those are authority-log entries unless one of them leaves a real question about how the brand should show up.

Loops do not cover: missing surfaces, scrape access for individual review platforms, or press-database subscription limits. Those belong in the frontmatter's sources_missing field or the data_limitations field.

Mark any loop only the brand can answer so it routes to the brand.

## When you refresh this

Reputation shifts as new press lands, search results reorder, retail relationships change, and old events fade or resurface. This doc is re-run on a quarterly cadence, with a major negative event triggering an update sooner. When you rebuild it, take the previous version in as context first, carry forward what still holds, update what changed, and note any new coverage, any shift in what dominates the brand's search results, and any change in where it is sold. Say what each open loop's status is now, and watch in particular for a new authority moment worth turning into creative and for any negative event that has either faded or grown.
