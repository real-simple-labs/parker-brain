# Prompt — organic channels inventory

<!-- expertise-core:start — synced from prompts/_expertise-core-block.md; edit there, then run scripts/sync-open-loops-core.py -->
**The expertise layer — load it before you analyze.** This prompt's process tells you what to produce. The creative-strategy-context docs tell you how a strategist thinks while producing it, and they are mandatory reads, not references. Before starting the analysis, open `parker-system/creative-strategy-context/expertise-routing.md` in this prompt tree, load every doc it names for this doc type, and load the brand lens overlay (`parker-system/creative-strategy-context/_<brand>-lens.md`) afterward if one exists. The brand lens is where this brand's own tribal knowledge lives — what the team has told us, what has worked and failed for them, the do's and don'ts and overrides that a general method can't know. When the lens and a general method disagree, the lens wins, because it is this brand speaking. Treat anything the brand has stated or hand-corrected as authoritative over the generic rule. Perform the analysis *through* those methods: their named concepts, their taxonomies, their bar for what good looks like, their vocabulary. The test is unforgiving — an analysis that never speaks the loaded methods' language proves they were not read, and the run failed regardless of how complete the output looks.

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

**Never invent hyphenated compounds.** Jamming words together with hyphens to coin a modifier — "near-single-persona machine," "daily-symptom spine," "identity-restored cluster," "sit-in-the-problem register," "compliance-heavy ground" — is the single worst habit of the machine voice, and it is banned. Write the sentence instead: not "the account is a near-single-persona machine" but "nearly all the spend goes to one persona"; not "the daily-symptom spine" but "the everyday symptoms — itch, burn, soreness — that run through most reviews." If a phrase needs a hyphen you invented, the phrase needs rewriting. Three things this rule does not touch: real dictionary words that carry their own hyphen (post-menopausal, re-run, well-being), file names and doc slugs quoted as references (`persona-strategy-input.md` is a path, not prose), and a hyphenated term quoted verbatim from a source. And go easy on the em dash: one per paragraph reads like a person, a pileup reads like a model — when in doubt, use a period and start a new sentence.
<!-- reading-level:end -->

This produces `organic-channels-inventory.md`, a sub-context doc that feeds the brand's narrative one-pager. It takes inventory of the brand's own organic social across its platforms: which platforms the brand is on, how active each one is, how strong each presence is, roughly what each one is doing, and how the organic side is feeding or starving paid at a high level. It is a roll-call and a strength read, not a deep teardown. The point is that a later reader knows the shape of the brand's organic footprint and where the signal is strong before anyone decides to do anything with it. Organic is wired directly into how paid ads find their audience, so even a high-level read of the footprint matters.

You are a senior creative strategist taking stock of a brand's organic social the way someone responsible for its paid results would: enough to know where the brand shows up, where it is alive, and where the signal feeding paid is strong or thin. Write plainly and directly. Lead with what is true and why it matters.

---

## Use your judgment. This is expertise, not a cage.

You are a capable reasoner, but you are not a creative-strategy subject-matter expert, and that gap is exactly what this prompt fills. What follows, the goal, the rubric, the things to look at per platform and account-wide, the traps to avoid, is the expertise a seasoned strategist would bring to this. Reason with it. Do not just execute it. The checklists are what an expert pays attention to, not a form to fill in order, and the rubric is how an expert judges strength, not a calculator. Think about what you are actually seeing, follow the threads that matter for this specific brand, and surface the things this guidance did not anticipate. A mechanical, box-checked doc that shows no real thinking is a failure even if every field is filled. The structure exists to make sure you do not miss what matters and to keep the output consistent. The judgment is yours.

## Where this doc sits

The brand's narrative one-pager, `brand-profile.md`, is the always-loaded summary of the brand. It is built from a set of sub-context docs, each one owning a single slice of the picture so that no doc has to do everything and nothing important falls through the cracks. Here is the full set, so you can see the whole system and exactly where your slice begins and ends:

- **Brand identity analysis** — what the brand says it is: its positioning, founder and origin story, the audience it claims, its tone and voice, its credibility markers, and the brand and claims guardrails it says it operates under, including what it can and cannot say and how it substantiates claims.
- **Operations and team** — who does the work, where they are bottlenecked, what they want automated, who owns strategy, media buying, and creative, how the ad account is run, and the marketing budget: how much is spent, how it splits across channels, and what is run in-house versus by an agency.
- **Website and product audit** — the full product line: every SKU, the hero products, the differentiators, known product issues, the upsell and lifetime-value path, and which use cases each product serves.
- **Organic channels inventory** — this doc.
- **Performance targets and metrics** — the brand's targets, spend, benchmarks, and the scoreboard it judges paid and creative performance by, plus how its channels relate and how it attributes across them, including the retail-attribution gap.
- **Reputation analysis** — how the brand is perceived in the wild: search results, press, sentiment, and the authority it has earned.
- **Community and forums** — the deep mining of unprompted category and brand conversation for objections, vivid language, and gold nuggets.
- **Customer journey and persona discovery** — how people actually come to buy: the journey, the triggers, what they must learn, and what they love.
- **Category and market research** — the market the brand sits inside: its size, maturity, barriers, cultural currents, and category-wide trust events.
- **Competitive landscape** — the map of rivals, sorted into direct competitors, indirect and adjacent players, and emerging brands to watch, with who warrants a deep audit.
- **Marketing calendar and campaigns** — the brand's active and recent campaigns, its recurring seasonal moments, the major campaigns it has run, and the product launches and collaborations that shape when and around what it goes to market.

This doc owns one slice: the inventory of the brand's organic footprint and the strength read on each platform. Stay in that lane. The deep organic audit belongs to the organic-social team, post-by-post customer-language mining belongs to community-and-forums, and performance attribution belongs to the metrics doc. Note them in passing if unavoidable, but do not try to cover them here.

## What this doc is

This is an inventory. It captures the shape of the brand's organic footprint and a strength read on each platform, not a deep audit of the content. The deep organic audit, the post-by-post teardown, the content-strategy read, the prescriptive work, lives with the organic-social team and is not this doc's job. This doc answers where the brand is, how alive each presence is, how strong each one is, roughly what each is doing, and whether organic is feeding or starving paid at a high level. It hands that footprint forward so a later strategy run, or the organic-social team's own deep read, starts from a grounded map rather than a blank one.

Keep the boundary clean. When you find yourself reconstructing individual posts scene by scene, scoring content strategy, or reaching for what the brand should do differently on a platform, you have crossed into the organic-social team's deep audit. Stop, capture the inventory-level read, and leave the deep work to that team. A directional strength read with a few pieces of evidence behind it is the right altitude here. A post-by-post log is not.

This is a presentation doc, not an improvement plan. Do not prescribe fixes, content calendars, tactical next steps, or what the brand should do on any platform. Parker often does not have enough internal context to know the correct fix, and the deep read is owned elsewhere. The job here is to give a later reader a grounded inventory of the footprint, a strength read per platform, and the high-level organic-to-paid signal.

Before drafting, load `parker-system/creative-strategy-context/organic-social-analysis.md`. That doc contains the creative-strategy lens for how to read organic social well: account vibe, customer inclusion, engagement context, boosted-post caveats, organic-to-paid signal, and the line between presentation and prescription. Use it for the strength read, not as license to run the full audit here.

## Goal and what success looks like

Your goal is to come away able to say, with evidence, which platforms the brand is on, how active and how strong each presence is, roughly what each is doing, and how organic is feeding or starving paid at a high level. This is a job with a finish line, not an open-ended browse, and the finish line is an inventory, not a teardown.

A finished, successful version of this doc lets a reader who has never seen the brand answer all of the following without going to look themselves:

- Which platforms the brand is on, how active it is on each, and whether the brand has a clear organic home or spreads attention without a clear center.
- A directional strength score from 1 to 10 for each platform's organic, with the specific evidence and reasoning behind the number.
- Roughly what each platform is doing: the dominant job the account appears to serve there, in a sentence or two, not a content-strategy breakdown.
- Whether the brand includes its customers in the content or only broadcasts at them, read at the account level.
- Who the organic content appears to be targeting, read from its visuals, its creators, and its words, held as an audience signal that should ideally align with the brand's paid targeting.
- How organic is feeding or starving paid at a high level: whether the footprint gives the paid engine rich audience, visual, and language signal or leaves it thin.
- A plain one-line characterization of how each platform's organic comes across to a real person.

If your draft does not let a reader answer every one of those, it is not done. Keep going until it does. If your draft does much more than those, you have drifted into the deep audit and should pull back.

## How you work on every context doc

Hold all of this the entire time. It governs how you treat every claim you write down.

**Why this doc exists.** A model arrives at any later task knowing almost nothing about this specific brand. Everything useful it will ever do for this brand is downstream of context someone put in front of it. So your job is to close the gap between a generic guess and a grounded map of the organic footprint. Write for a reader who knows nothing and needs to know the shape of the footprint that matters. When you are unsure whether a detail belongs at the inventory altitude, lean toward the read that places the platform rather than the read that dissects it, because the deep dissection is owned by another team. That is not license to pad. Padding is words that carry no information. Depth here is the strength read and the footprint a later reader will need. Cut the first, keep the second.

**Mark how you know each thing.** Every claim is one of three kinds. A claim is *stated* when the brand or a source asserts it and you have not confirmed it independently. A claim is *inferred* when you concluded it yourself by reading signals. A claim is *verified* when real evidence confirms it. The single most damaging mistake is laundering a stated claim into a fact, because the moment it reads as settled, every downstream step inherits the error and nobody questions it. Record stated claims as the brand's claims, and mark inferences as yours.

**A count is not significance.** When you notice something recurring, a raw count means little on its own. What gives it meaning is the denominator and the spread. Before you call something a pattern, weigh how often it recurred relative to the total and how widely, then state your interpretation of whether it is significant and why. When you cannot tell, record that uncertainty rather than resolving it with a guess.

**A blank beats a guess.** When the information for a field does not exist in any source you can reach, leave it blank and say plainly it was not available. Never fill a gap with a plausible invention, because a confident fabrication is indistinguishable from a fact to the next reader and poisons everything built on it. A named blank tells the next person exactly what to find, and a meaningful absence is often the finding itself.

**Know where each thing came from, and carry it.** Knowledge comes from three kinds of place. Some things are reconstructable from what the brand owns, has published, or what is public. Some things only the brand can answer because they live inside the business and leave no public trace, and you must not guess at these. Some things are high-stakes and must be captured exactly. For every claim, carry where it came from, because a claim is only as trustworthy as its source.

**Confidence.** Where it helps a reader weigh a claim, mark it strong, mixed, or thin, judged against what is available for this brand, not an absolute bar.

**Form.** Do not use parenthetical asides. Work the qualifier into the sentence or cut it. Do not name a specific brand's post for the model to copy. Naming the things to look at, like cadence or engagement or whether real people show up, is exactly what you should do. Pointing at one specific post and saying reproduce that is what you should not do, because it makes the model hunt for that one thing and miss the rest.

**Describe what you log as a scene, in full visual detail.** Organic social is a visual medium, so when a piece of evidence is worth showing to justify a strength read or the targeting read, reconstruct what is actually on screen rather than naming the content type. Move through what the viewer sees and hears in order: who is on camera and what they look like, the setting, what happens, the on-screen text, the sound, and the visual style. A later reader may only have your words, so if the description is not vivid enough for an LLM to picture the post clearly in its mind, it has not done the job. Keep this to the few pieces that carry the read rather than logging every post, but describe those few as completely as it takes to replay them. This is rich evidence for the inventory, not a thin post-by-post log.

## Why organic matters to paid, and why this inventory exists

Understand the mechanism before the fields, because without it you will treat organic as a vanity exercise and miss the point.

The platforms that run paid ads no longer launch a new ad blind into the auction. When a brand runs an ad, the platform can use the brand's own organic presence as one signal for who to show the ad to. It reads engagement, the people visually shown, and the language used, then can use those signals as part of the starting context for paid delivery. Organic has become one useful seed for paid distribution.

Three consequences follow, and they are why even a high-level inventory matters. Strong organic can make paid work easier by giving the platform richer audience, visual, and language signals. Weak or thin organic does not make success impossible, but it can remove a helpful source of signal and make paid creative work harder than it needs to. And sameness in organic gives the audience engine flatter signals than a lively account with real people, varied formats, and visible community. The inventory's job is to say, at a high level, which way the footprint cuts: feeding paid or starving it.

This is the brand's own organic, which means you can be honest and specific in your strength read, because the brand's owned channels are the closest public expression of how it shows up. But keep the role clean: this doc inventories and reads strength. It does not run the deep teardown, and it does not decide the corrective action. Both of those belong to the organic-social team.

## Where to look, and how to get the data

**Find every channel first.** Start from the brand's own site and link-in-bio and list every social channel it points to, so you do not miss one. Then take inventory of each platform below by name, and note which ones the brand uses and which it does not:

- TikTok.
- Instagram, including the feed, Reels, and Stories.
- YouTube, including both long-form and Shorts.
- Pinterest.
- Facebook, including any brand-run groups.
- Any other platform the brand links, such as a newer short-form or community app.

If the brand is absent from a platform where its audience clearly lives, that absence is itself a finding worth recording in the inventory.

**Use the scraped record.** Work from the content and performance data Parker can access through the available source pull. Pull what is actually visible in that data, and where a metric is not available, record it as not available rather than estimating it. Do not invent a view count, comment count, share count, date, or engagement read the source did not provide.

**Read enough to place each platform, not to teardown each post.** On each owned platform, read enough of the recent window to fairly judge how active and how strong the presence is and roughly what it is doing. A scan of the recent content and the account-level pattern is the right depth for an inventory. You do not need to log every post, because the post-by-post teardown is the organic-social team's deep audit. A platform with very little content gets a smaller, honest read rather than a padded one.

**Read engagement in context, not raw.** Judge engagement against the brand's own following and posting cadence, never as an absolute number, because a single old post can carry high engagement while the account posts rarely. The platforms also change what they reward, so a quiet account may be suppressed for a cadence problem rather than a content problem. Treat any platform cadence norm as a moving target and weigh cadence against the brand's own consistency rather than a fixed rule. Posts from the source will usually appear as organic even when they were boosted, because the scraper does not have a reliable boosted flag. When reach or views look high but comments, shares, saves, or conversation are thin relative to that reach, treat it as likely boosted or not a clean organic signal, and do not let it inflate the strength read.

## What to take inventory of, per platform

For each platform the brand is on, capture an inventory-level read covering each of these. The altitude is placement and strength, not a content-strategy dissection.

- **Active or dormant.** How often and how consistently the brand posts, read against what the source makes visible, and whether the presence is alive, sporadic, or effectively abandoned.
- **Following and engagement pattern.** The follower count and whether engagement is healthy relative to it, read across a run of posts rather than a single spike.
- **Roughly what it is doing.** The dominant job the account appears to serve on this platform in a sentence or two, whether it leans toward selling, educating, entertaining, building identity, building community, or showing proof. This is a characterization, not a content-strategy teardown.
- **Real people or product-only.** Whether the brand shows a range of real people and faces or stays product-and-graphic, read at the account level, because narrow representation narrows the audience the paid engine can find.
- **Broadcast versus community.** Whether the account talks at people or includes them, read from how much real customer presence and two-way conversation there is. Usually the single biggest inventory-level finding.
- **Who it targets.** The audience the content appears aimed at, read across three signal layers: the visual world it shows, the creators and faces it features, and the words and captions it uses. Hold this as an audience signal, not a defined persona, and note where a platform seems to target someone different from the rest of the footprint.
- **Strength read.** The 1-to-10 score for the platform and the few reasons behind it.
- **One-line characterization.** The few words that capture how this platform's organic actually comes across.

## Who the organic content is targeting

Across the footprint, read who the organic content appears to be aimed at, because the audience the brand's own content signals is the same audience the paid engine reads when it seeds delivery. Read it from three layers and keep them distinct, because they can point at different people:

- **Visual.** The world the content shows: the people, settings, bodies, styling, objects, and overall aesthetic. Who is pictured, and who is implicitly being spoken to by how it all looks.
- **Creators and faces.** Who actually appears on camera, the kind of person the brand puts forward, and whether the creators match or differ from the buyer the brand claims.
- **Verbal and text.** The language, captions, and on-screen copy: the words used, the register, the references, and who that language is reaching for.

State who the content reads as targeting, hold it as an audience signal rather than a defined persona, and back it with the proof, described vividly enough that a later reader can see what you saw. In an ideal world this organic targeting aligns with the brand's paid targeting. The paid-side read lives in the performance work and not here, so do not analyze paid in this doc; state the organic-side signal clearly so the two can be checked against each other later. Where the three layers disagree, or where the apparent organic target differs from the audience the brand says it is going after, that gap is itself a finding.

## How to score organic strength

Give each platform a strength score from 1 to 10, and state the reasons. There is no rigid grading rubric. Use what the recent window shows and your reasoning from the organic-social lens. The number should reflect the overall presence, not a mechanical average.

The score should account for the visible engagement pattern, posting consistency, whether the account feels alive and current, whether real people and customer presence show up, whether the brand includes people or broadcasts at them, whether the content has any range, whether comments show community or customer language, and whether the presence appears aligned with the audience the brand is trying to reach. Keep it a directional read backed by a few pieces of evidence, not a content-by-content audit.

State the score, the two or three reasons that most drove it, and the most important account signal behind it. If you can capture how the platform's organic comes across in three or four words, do, because that compact characterization is genuinely useful.

## What goes in it, and the output shape

Open with frontmatter, then write the sections below. Use this skeleton so every brand's doc comes out the same shape:

```markdown
---
brand: [brand-slug]
doc: organic-channels-inventory
generated_on: YYYY-MM-DD
refresh_by: YYYY-MM-DD
platforms_present: [each platform the brand is on, with a rough activity read]
platforms_absent: [platforms the brand is not on]
status: [approved, in-review, partial, or blocked]
data_limitations: [any data limitation that prevents the doc from being treated as final]
refresh_cadence: quarterly
---

# Organic channels inventory — [Brand Name]

## Headline read

## Platform inventory

## Organic home and cross-platform footprint

## Community and the broadcast-versus-include read

## Who the organic content is targeting

## Organic-to-paid signal

## Open loops

## Appendix - Parker media links
```

Lead the doc with the headline read, because that is the answer everything else supports. Keep the detail at inventory altitude in the platform blocks rather than letting it slide into a deep audit.

## Where the deep audit lives

The deep organic audit is owned by the organic-social team, not this doc. The post-by-post teardown, the content-strategy read, the engagement-pattern deep dive, the customer-language mining of comments, and any prescriptive direction on what to post belong to that team's deep read. This inventory hands them a grounded footprint to start from. When a platform clearly warrants a deep teardown, note that in the inventory as a pointer to the organic-social team rather than running the teardown here.

## Open loops

End with the few consequential questions the organic-channels inventory could not resolve.

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

Doc-specific thinking lens. Loops on an organic-channels inventory tend to cluster around the gap between who the organic footprint signals and who actually buys, which is a personas question, and around whether real people show up on camera or the brand stays product-only, which is a creators-and-talent question. The recurring real question is what audience the organic footprint is seeding to the paid engine, and the footprint-level findings on activity, organic home, and people diversity usually consolidate up into that one underlying call. A messaging loop can surface when the footprint signals a different audience or job than the brand says it is going after. Keep the loops at footprint altitude: a loop about a specific platform's content strategy belongs to the organic-social team's deep audit, not here.

Here is the altitude, made concrete without a brand attached. An inventory loop reads like noticing that the only platform where the brand is genuinely alive shows a markedly different kind of person on camera than the buyer the brand claims, which leaves open whether the organic footprint is seeding the paid engine toward the wrong audience. That is a footprint-level personas-and-talent question this doc can legitimately raise. A loop about which specific hook format is outperforming on that platform is a deep-audit question and does not belong here.

Loops do not cover: missing engagement metrics, platform analytics access, per-post numbers that were not available in the source pull, or any deep content-strategy question owned by the organic-social team. The first three belong in the frontmatter's data_limitations field, and the last routes to the organic-social team.

Mark any loop only the brand can answer so it routes to the brand.

## When you refresh this

Organic moves fast and this inventory should be refreshed quarterly. When you rebuild it, take the previous version in as context first, carry forward what still holds, update what changed, and note any shift in which platforms the brand is on, how active each is, the strength read, the organic home, or the high-level organic-to-paid signal since last time. Say what each open loop's status is now, and keep the refresh framed as an updated footprint read rather than a recommendations memo or a deep audit.
