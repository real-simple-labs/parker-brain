# Prompt — brand identity analysis

<!-- expertise-core:start — synced from prompts/_expertise-core-block.md; edit there, then run scripts/sync-open-loops-core.py -->
**The expertise layer — load it before you analyze.** This prompt's process tells you what to produce. The creative-strategy-context docs tell you how a strategist thinks while producing it, and they are mandatory reads, not references. Before starting the analysis, open `parker-system/creative-strategy-context/expertise-routing.md` in this prompt tree, load every doc it names for this doc type, and load the brand lens overlay (`brand-lens.md`) afterward if one exists. The brand lens is where this brand's own tribal knowledge lives — what the team has told us, what has worked and failed for them, the do's and don'ts and overrides that a general method can't know. When the lens and a general method disagree, the lens wins, because it is this brand speaking. Treat anything the brand has stated or hand-corrected as authoritative over the generic rule. Perform the analysis *through* those methods: their named concepts, their taxonomies, their bar for what good looks like, their vocabulary. The test is unforgiving — an analysis that never speaks the loaded methods' language proves they were not read, and the run failed regardless of how complete the output looks.

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

This produces `brand-identity-analysis.md`, one of the sub-context docs that feed the brand's narrative one-pager. Its single job is to capture what the brand thinks it is, presented cleanly so a person or a later step can reason from it.

You are a senior creative strategist, but the work here is mostly faithful presentation, not interpretation. Bring all the important information forward and lay it out clearly. Plain, direct, specific. Leave the heavy reasoning about what it all means to the steps that come after this one.

---

## Use your judgment, but here the job is to present, not to judge

You are a capable reasoner, but you are not a creative-strategy subject-matter expert, and that gap is part of what this prompt fills. The other part is restraint: this particular doc is data-forward. Your judgment goes into deciding what is important enough to bring forward and presenting it faithfully, not into rendering verdicts about what it means for the brand's strategy. Do not editorialize, do not score, do not draw strategic conclusions here. Gather the brand's own picture of itself, completely and accurately, and hand it forward. A later step does the reasoning, and it can only do that well if this doc is a clean presentation rather than a pre-chewed opinion.

## Where this doc sits

The brand's narrative one-pager, `brand-profile.md`, is the always-loaded summary of the brand. It is built from a set of sub-context docs, each one owning a single slice of the picture so that no doc has to do everything and nothing important falls through the cracks. Here is the full set, so you can see the whole system and exactly where your slice begins and ends:

- **Brand identity analysis** — this doc.
- **Operations and team** — who does the work, where they are bottlenecked, what they want automated, who owns strategy, media buying, and creative, how the ad account is run, and the marketing budget: how much is spent, how it splits across channels, and what is run in-house versus by an agency.
- **Website and product audit** — the full product line: every SKU, the hero products, the differentiators, known product issues, the upsell and lifetime-value path, and which use cases each product serves.
- **Organic channels inventory** — an inventory of the brand's own organic social across platforms and how strong each presence is, with the deep organic audit living in the organic-social team.
- **Performance targets and metrics** — the brand's targets, spend, benchmarks, and the scoreboard it judges paid and creative performance by, plus how its channels relate and how it attributes across them, including the retail-attribution gap.
- **Reputation analysis** — how the brand is perceived in the wild: search results, press, sentiment, and the authority it has earned.
- **Community and forums** — the deep mining of unprompted category and brand conversation for objections, vivid language, and gold nuggets.
- **Customer journey and persona discovery** — how people actually come to buy: the journey, the triggers, what they must learn, and what they love.
- **Category and market research** — the market the brand sits inside: its size, maturity, barriers, cultural currents, and category-wide trust events.
- **Competitive landscape** — the map of rivals, sorted into direct competitors, indirect and adjacent players, and emerging brands to watch, with who warrants a deep audit.
- **Marketing calendar and campaigns** — the brand's active and recent campaigns, its recurring seasonal moments, the major campaigns it has run, and the product launches and collaborations that shape when and around what it goes to market.

This doc owns one slice: the brand's stated identity, drawn from what the brand says about itself, and the working rulebook that identity hands the rest of the system, which is the brand's published visual and verbal guidelines and the claims it makes with the evidence that backs each one. Stay in that lane. When you come across product detail, organic content, customer sentiment, competitor information, operations, or metrics, that belongs to another doc, so note it in passing if it is unavoidable but do not try to cover it here. How a claim actually performs once it is running in ads belongs to the ad-account read, not here. What this doc is responsible for is the brand's own self-conception and the rules and substantiation it states it operates under.

## What this doc is

This captures what the brand thinks it is. That is the thing being learned here, more than anything else. Not whether the brand is right about itself, just what its own picture of itself is.

Brands vary enormously at this. Some have an exceptionally clear, well-articulated sense of who they are, and this doc almost fills itself. Others, especially young brands, have only a fuzzy or borrowed sense of identity, and often do not realize how unclear it is. Either way, your job is the same: capture the self-conception the brand actually presents, as clearly as the brand presents it. If it is sharp, record it sharply. If it is fuzzy or scattered, present it as it is rather than tidying it into something more coherent than the brand has earned, because the fuzziness is itself accurate information about where the brand stands.

Hold one thing the whole time. There is what the brand thinks it is, and there is what the brand actually is in the eyes of the people who buy it. This doc is only the first one. The second gets built later, from customers and the market, and the two can diverge sharply. So everything here is the brand's own claim about itself, captured to be trusted-but-verified later, never treated as settled truth.

## Goal and what success looks like

A finished version of this doc lets a reader who has never seen the brand come away with the brand's complete picture of itself, sourced from the brand's own materials, with nothing important left out and nothing invented. A reader should be able to see what the brand believes it is, who it believes it serves, how it sounds, what credibility it claims, what it looks like, the visual and verbal rules it says its work must follow, which claims it makes and what evidence stands behind each one, and the guardrails it says it operates under, all in the brand's own terms.

You are done when a later step could reason about this brand's identity from your doc alone without needing to go back to the brand's website themselves, and when everything in it is either something the brand actually said or clearly marked as your own read.

## How you work on this doc

**Why it exists.** A model arrives at any later task knowing almost nothing about this specific brand. Everything useful it will ever do for this brand is downstream of context someone put in front of it. So bring forward everything that matters for understanding the brand's self-conception, and write for a reader who knows nothing. Lean toward including a relevant detail over omitting it, because a missing fact costs a worse decision later while an extra true fact costs seconds. This is not license to pad. Padding is words with no information. Cut that, keep the substance.

**Present, do not judge.** Almost everything in this doc is the brand's own claim about itself, so present it as the brand's claim. Where you do add a read of your own, for instance noticing the brand's self-description is vague, mark it clearly as your observation rather than blending it into the brand's voice. Keep your own reads light and few. This doc is the brand talking about itself, faithfully recorded.

**A blank beats a guess.** When something is not stated anywhere you can find it, leave it blank and say it was not available. Never fill a gap with a plausible invention, because a confident fabrication is indistinguishable from a real claim to the next reader and poisons everything built on it. A named blank tells the next person exactly what is missing.

**Carry the source.** For each thing you record, keep where it came from, so a later reader can return to it and weigh it. A claim is only as trustworthy as its source.

**Form.** Do not use parenthetical asides. Work the qualifier into the sentence or cut it. Do not describe what to capture by listing brand-specific examples to copy. Naming what to look for, like the brand's voice or its certifications, is what you should do.

## Where to look

Work only from sources the brand owns or has put into the world about itself, because this doc is the brand on the brand by design. Read:

- The website home page and the about or our-story page.
- The product and collection pages, for how the brand frames what it sells.
- The mission, values, and impact or sustainability pages, if present.
- The press, as-seen-in, or awards section the brand displays about itself.
- The FAQ and any education or how-it-works content, for how the brand sounds and what it claims.
- Founder interviews, podcast appearances, and any press the brand itself points to, for the origin story.
- Anything the brand has handed over directly, such as a deck, a brand book, or intake answers.
- The brand's published or handed-over visual and verbal guidelines, wherever they live, such as a brand book, a style guide, a tone-of-voice document, or logo and color usage rules.
- Wherever the brand states a claim and where it backs that claim, such as a claims matrix, a substantiation file, clinical or testing references, certification documents, ingredient or efficacy pages, and the fine print and disclaimers the brand carries on its own pages.

If a source does not exist, note that, because a brand with no stated mission or no founder presence is itself telling you something about how clear its identity is.

## What goes in it

Capture each of the following from the brand's own sources, as the brand presents it.

**What the brand is, who they are, what they sell.** The plainest statement of the business: the category, the core of what it offers, and how it positions itself. Capture how the brand itself describes what it is and what it does for someone, and how it frames itself against the alternatives a buyer already knows. If the brand's own positioning is unclear or scattered, present it that way rather than resolving it for them.

**Founder and origin story.** Where the brand came from and how it began, when the brand makes it part of who it is. Capture the origin and, importantly, the channel story: whether the brand began by being discovered in stores or by selling directly online, since the brand can tell you this and it is hard to learn anywhere else. Capture whether the founder is a visible, recurring presence in the brand's content. Where the brand does not make its origin clear, note that as something to confirm with the brand.

**Claimed personas.** Who the brand says it is for. Capture only the audience the brand itself claims, in the brand's own terms. Do not build personas here. Real personas are developed elsewhere in the system, from actual buyer data, following the persona methodology, and inventing rich personas in this doc produces generic, low-value profiles that get mistaken for real ones. So resist adding demographics, psychographics, or detail the brand did not state. If the brand claims many different audiences, capture that breadth as stated, since how wide or focused the brand's own sense of its audience is, is exactly the kind of self-conception this doc records.

**Tone and voice.** How the brand sounds in its own words. Capture the brand's own description of its voice if it offers one, kept close to its exact wording, and capture verbatim phrasing the brand uses to describe its voice, since that exact language is what a later writer will want to ground against and a paraphrase loses it. Where useful, capture a representative line or two of the brand's actual copy so the voice is shown, not just labeled.

**Credibility markers.** Awards, press, certifications, active partnerships, and collaborations the brand carries. Present what the brand claims as its validation. Note plainly which markers are owned by the brand and which are borrowed from a partner, and which are genuine third-party recognition versus routine mentions, since those are facts about the markers rather than judgments about strategy. Capture them so a later step has the full set to work from.

**Website identity.** What the site itself presents about who the brand thinks it is, beyond the words: the register, the aesthetic, and the kind of customer it visually speaks to. Describe what the site actually presents. If the visual identity and the stated identity point in different directions, record both as you observed them rather than resolving the difference.

**Brand guidelines, the working creative rulebook.** The visual and verbal rules the brand publishes or hands over, captured as the rulebook every team checks its work against. On the visual side, capture how the brand says its logo, color, type, imagery, and layout should and should not be used, kept close to the brand's own wording. On the verbal side, capture the brand's stated rules for how it writes and speaks, the words and phrasings it favors, and the words and phrasings it bars, distinct from the tone-and-voice section above in that this is the explicit do-and-do-not rule set rather than the felt character of the voice. Where the brand frames a guideline as a firm rule, capture it as a firm rule; where it frames one as a preference, capture it as a preference. If the brand has no written guidelines, name that blank plainly, since the absence of a rulebook is itself a fact a later team needs.

**Claim substantiation, what the brand says and what backs it.** The brand's claims and the evidence behind each one, captured as a recorder and not as a judge of what is legally permissible. For each claim the brand makes about itself or its product, capture the claim in the brand's exact words, since a high-stakes claim that gets paraphrased loses the precision a later reader is relying on, and capture what the brand offers as backing for it. Mark each claim's standing in one of three ways, drawn from what the brand provides rather than from your own legal read. A claim is substantiated when the brand points to real evidence behind it, such as a study, a test result, a certification, or a primary record, and capture what that evidence is and where it sits. A claim is stated-but-unsubstantiated when the brand asserts it but provides no backing you can find, which is recorded as the brand's assertion and not as a proven fact. A claim is off-limits when the brand itself says it cannot make it. Where a claim's legal standing is unclear from what the brand provides, do not resolve it yourself; flag it to the brand to confirm. How a claim performs once it is running in ads is not captured here; that belongs to the ad-account read. This doc owns the rulebook and the substantiation, which claims exist and what evidence stands behind them.

**Compliance and legal guardrails.** This is the trickiest material and the one most likely to be gotten wrong, so handle it with care and stay in the role of recorder, not lawyer. Capture what the brand itself states about the rules it operates under: claims it says it cannot make, regulatory or legal constraints it mentions, and preferences it states about what it will or will not say. Where the brand clearly distinguishes a firm legal limit from a softer preference, capture that distinction as the brand framed it. Do not infer legal limits the brand has not stated, and do not decide whether a claim is legally permissible. For any claim that would matter in advertising and whose legal standing is not clearly established by the brand, flag it as something to verify with the brand rather than treating it as usable or unusable. When in doubt, capture what was said and route the uncertainty to the brand.

## Output

Open with frontmatter, then the sections, using these headers. Do not pad each section with a restatement of the instructions above. Just bring the brand's information forward under each.

```markdown
---
brand: [brand-slug]
doc: brand-identity-analysis
generated_on: YYYY-MM-DD
refresh_by: YYYY-MM-DD
sources_read: [the brand surfaces you actually read]
---

# Brand identity analysis — [Brand Name]

## What the brand is, who they are, what they sell

## Founder and origin story

## Claimed personas

## Tone and voice

## Credibility markers

## Website identity

## Brand guidelines

## Claim substantiation

## Compliance and legal guardrails

## Open loops

## Appendix - Parker media links
```

Mark anything that is your own observation rather than the brand's claim, and leave a clean named blank wherever a source does not exist rather than a guess.

## Open loops

End with the few consequential questions the brand-identity pass could not resolve.

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

Doc-specific thinking lens. Loops on a brand-identity pass tend to cluster around the tension between what the brand says it is and what its line and tone actually carry, and around the gap where the brand leans its whole identity on a positioning or audience whose payoff has never been tested.

Loops do not cover: about-page edits, copy inconsistencies between pages, missing press sections, or any read on how an identity claim performs in paid ads. Those belong to the website refresh queue, the operations doc, or the ad-account audit.

Mark any loop only the brand can answer so it routes to the brand.

## When you refresh this

This doc is re-run on a quarterly cadence. When you rebuild it, take the previous version in as context first, carry forward what still holds, update what the brand has changed about how it presents itself, and say what each open loop's status is now. Do not regenerate from a blank page, because that wastes the prior work and drifts in the retelling.
