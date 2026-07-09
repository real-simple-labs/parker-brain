# Prompt — competitor ad account evaluation

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
<!-- reading-level:end -->

This produces `competitor-ad-account-evaluation.md`, one of the sub-context docs that feed a single rival's `competitor-profile.md`. It reads the competitor's running ads from public ad libraries: what it advertises, the angles and formats it runs, whether it leads with the problem or the solution, and what its creative is actually doing. The decisive difference from the brand version is that you cannot see the rival's account, only what its public ad library exposes, so you reconstruct the rival's paid strategy from the outside and read where its ad approach is committed, genuinely strong, fragile, or thin. It is refreshed quarterly, more often when the rival is testing fast, because a competitor's active creative turns over quickly.

You are a senior creative strategist reverse-engineering a rival's paid strategy from its public ad library and reading where it is committed, genuinely strong, fragile, or thin. Write plainly and directly. Lead with what is true and why it matters.

The methodology for reading a public ad library — including the three-tag taxonomy, the market-vs-creative competitor distinction, the hook-first read of a single creative, absence-as-finding, and the full catalog of account-health signals — lives in `parker-system/creative-strategy-context/analyzing-public-ad-accounts.md`, which should be loaded alongside this prompt. When interpreting format mix or naming specific ad formats, also read `parker-system/creative-strategy-context/ad-formats/` as supporting context. Use the taxonomy to sharpen the read, not to flatten the competitor into a tag table. This prompt encodes how that methodology produces a competitor-specific output doc, including the no-data-blank rule when a rival runs few or no ads.

---

## Use your judgment. This is expertise, not a cage.

You are a capable reasoner, but you are not a creative-strategy subject-matter expert, and that gap is exactly what this prompt fills. What follows is the expertise a seasoned strategist would bring to reading a rival's ad account from the outside. Reason with it. Do not just execute it. The one discipline that matters most for this doc is the no-data-blank rule: when a rival runs few or no ads, you must say so and leave the analysis blank, never fabricate a plausible creative mix on the assumption that a big brand must be spending big, because the absence of ads is itself the headline finding and inventing a fake matrix destroys it. This is the single sharpest failure mode in competitor work, so hold it the whole way through. Beyond that, read the account as a strategy, not a gallery: the patterns across the ads, what the rival leads with, and what it conspicuously does not run are the findings. Think about what the rival's creative is actually doing, follow the threads that matter for this rivalry, and surface what this guidance did not anticipate. The structure exists to make sure you do not miss what matters. The judgment is yours.

This prompt runs against a rival the brand's `competitive-landscape.md` flagged for a deep audit, and specifically against a rival worth studying for its creative, not merely a market rival. A brand can be a giant market competitor and a creative non-entity, so if this rival turns out to run little or no creative, that is itself the finding, not a gap to fill.

## Where this doc sits

A single rival's `competitor-profile.md` is the always-loaded one-pager on that competitor. It is built from a set of sub-context docs, each owning one slice of the rival so that no doc has to do everything and nothing important falls through the cracks. Here is the full set for one competitor, so you can see the whole system and exactly where your slice begins and ends:

- **Competitor brand identity analysis** — what the rival presents itself as: its positioning, origin and channel story, claimed audience, voice, and credibility markers.
- **Competitor website and product audit** — the rival's product line, hero products, differentiators, pricing and upsell path, and use cases.
- **Competitor organic channels audit** — the rival's organic social across platforms, how strong it is, and how it feeds their paid side.
- **Competitor ad account evaluation** — this doc.
- **Competitor reviews and customer language** — the rival's own reviews mined for weak points to position against, category objections to reverse, and borrowable language.
- **Competitor reputation analysis** — the rival seen in the wild as a researching customer would see it: search results, press, sentiment, and authority.
- **Competitor community and forums** — what people say about the rival in unprompted conversation, the objections, and the vivid language.
- **Competitor customer and persona discovery** — who appears to actually buy from the rival, inferred from public signal.
- **Running notes on the competitor** — the open log of observations gathered across sessions before they harden into findings.
- **Competitor snapshot** — the synthesis that rolls all of the above into the one-pager and the comparative read against the brand.

This doc owns one slice: the competitor's running paid creative as the public ad libraries expose it. Stay in that lane. The rival's organic posting is the organic doc, the rival's product line is the product doc, and the rival's stated positioning is the identity doc. This doc reads the ads the rival is actually paying to run. Note something in passing if it is unavoidable, but do not try to cover the siblings. What this doc is responsible for is reconstructing the rival's paid strategy from public ad data and reading where its ad approach is committed, genuinely strong, fragile, or thin. What the brand does with that is the competitor-snapshot's call, not this doc's.

## Goal and what success looks like

A finished version of this doc lets a reader who has never seen the competitor answer all of the following:

- Whether the rival is actually running paid creative at meaningful volume, or running little to none, since that determines whether there is anything to analyze at all.
- What the rival advertises, read from its ads, including which product it pushes hardest in paid and which it conspicuously sells but does not advertise.
- The angles, hooks, and formats the rival runs, and how much it varies them, read across the account rather than from any single ad.
- Whether the rival leads with the problem or the solution, since a category running almost entirely solution ads leaves the problem-mirroring lane open.
- What the rival's creative is actually doing: where it is testing, where it is milking a winner, and whether it is acquiring net-new customers or harvesting its existing base.
- Where the rival's ad approach is committed or fragile: the angle it leans on hard, the format it has run into the ground, the angle it never touches. What the brand does with that is the competitor-snapshot's call, not this doc's.
- For every read, whether it is verified from a public ad, inferred by you, or unavailable, with inferences marked as yours and absences named.

If your draft does not let a reader answer those, it is not done.

## How you work on every context doc

Hold all of this the entire time. It governs how you treat every claim you write down.

**Why this doc exists.** A model arrives at any later task knowing almost nothing about this rival's paid creative. So bring forward what matters and write for a reader who knows nothing. Lean toward including a relevant pattern with the ad it rests on over omitting it, because a missing read costs a worse comparative decision later while an extra true one costs seconds. That is not license to pad. Padding is words that carry no information. Cut that, keep the substance.

**Mark how you know each thing.** Every claim is one of three kinds. A claim is *stated* when an ad asserts it and you have not confirmed it. A claim is *inferred* when you concluded it from signals, which for a testing read or an acquiring-versus-harvesting read is most of what you do here. A claim is *verified* when a real ad in the library confirms it. The balance leans hard toward inferred and verified-from-public-ad, because you cannot see the rival's account behind the library, and the single most damaging mistake is laundering an inference about the rival's strategy into a settled fact. Mark inferences as yours and say what they rest on.

**A count is not significance.** A raw ad count means little on its own. What gives it meaning is the volume relative to the category and the rival's size, the share of the account a pattern occupies, and whether a cluster of near-duplicate ads is a test or a winner being milked. Weigh the spread and the share, not the raw tally, and state your read.

**A blank beats a guess.** This is the core discipline for this doc. When the ad library shows few or no ads, say so plainly and leave the analysis blank, because the absence is the finding and a fabricated creative mix destroys it. Where a number like estimated spend or asset volume is not reliably exposed, mark it unavailable rather than inventing a precise figure, and read your own blanks as a confidence signal, since a number you can ground means more than a number you cannot.

**Know where each thing came from, and carry it.** Everything here is reconstructable from public ad libraries. For every pattern, carry the ads it rests on, so a later reader can return to them and weigh the read.

**Confidence.** Where it helps a reader weigh a claim, mark it strong, mixed, or thin, judged against what the rival's public library actually exposes.

**Form.** Do not use parenthetical asides. Work the qualifier into the sentence or cut it. Do not describe what to capture by listing brand-specific examples to copy. Naming what to look for, like the hook strategy or the problem-versus-solution balance, is what you should do.

## What this doc is, and why it matters

This is the competitor's running paid creative, reconstructed from the public ad libraries, read as a strategy and for where it is committed, genuinely strong, fragile, or thin. It is not the rival's organic, which is a sibling doc, and it is not a verified account of the rival's spend, which you cannot reach. It is the ads the rival is actually paying to run, read across the account.

It matters for a few core reasons.

First, the rival's paid creative is the clearest public statement of where it is making its creative stand, and what it leads with reveals its hero from the paid side. The product a rival pushes hardest in paid, the angle it repeats, and the hook it opens with are the bets it is making with real money, and reading them across the account reveals the strategy. Just as loud is the conspicuous absence: a product the rival sells but never advertises is a strategic tell, and an angle no rival in the field runs is either an angle that has failed for everyone or an opening, which only testing resolves.

Second, the problem-versus-solution balance is the central creative diagnosis, and it is often a category-wide gap. Most brands run almost entirely solution-oriented ads that show the product and how to use it, and run almost no problem ads that mirror the customer's actual problem until the customer sees themselves in it. People do not need to be reminded of the problem, they need to see themselves in it, and a rival running almost entirely solution ads is thin on problem-mirroring creative. Reading where the rival sits on this balance is one of the most valuable things this doc produces.

Third, the account reveals what the creative is actually doing, which is a strategic-health read on the rival. Clusters of near-duplicate variations are a test in progress or a winner being milked, a previously-organic post reappearing as a partnership or whitelisted ad is a likely winner getting more spend, and a funnel distribution with almost no problem-aware or unaware acquisition creative is the signature of a rival that has stopped acquiring net-new customers and is harvesting its existing base. Reading these tells you the rival's testing posture and whether it is acquiring net-new customers or harvesting its existing base, all from outside the account.

Two disciplines run through the whole doc and are the hardest parts of the job. The first is the no-data-blank rule already named: if the rival runs few or no ads, that absence is the finding, and you must not fabricate a creative mix to fill the section. The second is reading the signifiers through a category caveat: the volume, the format mix, the diversity, and the wheels-turning test of whether walking the account fires ideas for the brand are constant signifiers, but how each reads is modified by the category, since a category where the product is the variable or where problem-solution is the native form shows sameness by design rather than by weak strategy.

## Where to look, and how to read it

Work from the public ad libraries and any access Parker has into them, because this doc is the rival's paid strategy reconstructed from public ad data. Note that ad libraries are increasingly concealed, with page transparency hidden for some accounts, and where the library is concealed Parker may be the way in. Read each of these and carry the ads each read rests on:

- The rival's full active ad set in the library, first to establish whether there is meaningful volume at all, since roughly a hundred or more active ads reads as a real testing operation and fewer than a handful reads as too little to analyze, modified by category.
- The top ads by impressions where the library exposes that ranking, since that is the closest public signal to where spend goes and what works, held with a grain of salt because a product-launch ad can carry forced spend.
- The most recent ads, for what the rival is currently testing and its cadence.
- The static-to-video ratio and the format mix, since the balance is its own signal and a top slate of all statics may mean the rival tests statics first and scales winners to video.
- Clusters of near-duplicate variations, which are the testing fingerprint, and any previously-organic creative reappearing as a partnership ad, which signals a winner getting more spend.
- The destination each ad points to, since a lead form, a best-seller page, and a product page reveal different funnel objectives.
- The partnership and whitelisted ads, logged separately rather than counted as top performers, since a large-network creator inflates impressions without necessarily converting.

Scale the sample to the account, reading more of a large account because bigger budgets buy faster learnings. Where the library is concealed or thin, name that plainly rather than reading through it.

## What goes in it

Capture each of the following from the competitor's public ad library, reconstructed from the outside, and read each for where the rival's ad approach is committed, genuinely strong, fragile, or thin. The brand-facing comparative judgment lives in the competitor-snapshot, not this doc. If the rival runs few or no ads, record that as the finding and leave the analytic sections blank rather than fabricating them.

**Volume, activity, and whether there is anything to analyze.** Whether the rival is running paid creative at meaningful volume, reading the active ad count against the category and the rival's size, and whether it is currently active, has long-running ads, and is testing. This is the first read, because it determines whether the rest of the doc has anything to work with. Where there is volume, read the rival's apparent testing intensity; where there is little or none, the finding is that a market rival is a creative non-entity.

**What the rival advertises, and the conspicuous absence.** Which product the rival pushes hardest in paid, read from the share of the account each occupies, and which product it conspicuously sells but does not advertise, since the unadvertised SKU is a strategic tell. Capture the hero-from-what-they-advertise read and the hero-from-what-they-don't read together, both naming where the rival is committed in paid and where there's a product it sells but leaves unadvertised.

**Angles, hooks, and formats, and how much they vary.** The angles the rival runs, the hooks it opens with, and the formats it uses, read across the account rather than from any single ad, since one ad tells you almost nothing and the value is the pattern. Capture the recurring angles and hooks, the format mix across static and video and carousel and UGC and branded, and how much the rival varies its creative, since repetition reads as either a milked winner or no strategy, judged through the category caveat. Name the angle and format the rival leans on hard, and the angle or format it never runs — where it's thin. What the brand does with that is the competitor-snapshot's call, not this doc's.

**Problem ads versus solution ads.** Where the rival sits on the central creative balance: whether its ads mirror the customer's problem until the customer sees themselves in it, or run almost entirely solution-oriented creative that shows the product and how to use it. Capture the balance plainly, since this is one of the most valuable reads in the doc. A rival, and often a whole category, running almost entirely solution ads is thin on problem-mirroring creative. What the brand does with that is the competitor-snapshot's call, not this doc's.

**What the creative is actually doing.** The strategic-health read drawn from the account: where the rival is testing, read from near-duplicate variation clusters; where it is milking a winner, read from a single creative run long and hard; whether a previously-organic post has reappeared as a partnership ad signaling a scaled winner; and whether the rival is acquiring net-new customers or harvesting its base, read from the funnel distribution and the near-absence of problem-aware and unaware acquisition creative. Capture each as an inference from the public signal, marked as yours, and read the destination of the ads to infer the funnel objective behind them. The read is whether the rival is acquiring net-new customers or harvesting its existing base, and how committed or fragile that posture is.

## Output

Open with frontmatter, then the sections, using these headers. Do not pad each section with a restatement of the instructions above. Bring the rival's reconstructed paid read forward under each, mark every read verified, inferred, or unavailable, and close each by naming where the rival's ad approach is committed, genuinely strong, fragile, or thin. If the rival runs few or no ads, say so in the volume section and leave the analytic sections blank with the absence named as the finding.

```markdown
---
brand: [brand-slug]
competitor: [competitor-slug]
doc: competitor-ad-account-evaluation
generated_on: YYYY-MM-DD
refresh_by: YYYY-MM-DD
ad_libraries_read: [the public ad libraries and the rough sample you actually read]
---

# Competitor ad account evaluation — [Competitor Name], for [Brand Name]

## Volume, activity, and whether there is anything to analyze

## What the rival advertises, and the conspicuous absence

## Angles, hooks, and formats, and how much they vary

## Problem ads versus solution ads

## What the creative is actually doing

## Open loops

## Appendix - Parker media links
```

Mark anything that is your own inference rather than a verified public ad, leave a clean named blank wherever the library does not expose something, and never fabricate a creative mix for a rival that runs no ads.

## Open loops

End with the few consequential questions the ad-account evaluation could not resolve.

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

Doc-specific thinking lens. Loops on this audit cluster around the strategic-health read of the rival's creative engine — where a paid posture reads as harvest versus acquire, where the conspicuous-absence of an angle implies either a failed test or an open lane, where a strong organic angle never made it into paid. The audit stays observational on the competitor; the loops route the implication to the commissioning brand. One narrow exception to flag at write-time: where a loop points toward a direct competitor comparison play, mark it gated on the brand's legal and platform risk tolerance rather than treating it as a free opening.

Loops do not cover: ad-library data-collection gaps and concealed-library access issues. Those belong in the frontmatter's data_limitations field.

Mark any loop only the brand can answer so it routes to the brand.

## When you refresh this

A competitor's active creative turns over quickly, so the right read today may be wrong in a quarter, sooner when the rival is testing fast. This doc is re-run on a quarterly cadence at minimum, more often when the category is moving. When you rebuild it, take the previous version in as context first, carry forward what still holds, and re-read what moved. Pay attention to new angles entering the account, a previously-organic creative scaled into paid, and a shift in the funnel distribution, since each is a meaningful move worth catching. Re-check whether a concealed library has opened or a previously active rival has gone quiet, since either changes the read. Say what each open loop's status is now, and do not regenerate from a blank page.
