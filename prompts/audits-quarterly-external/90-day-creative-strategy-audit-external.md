# Prompt — 90-day creative strategy audit, external

<!-- expertise-core:start — synced from prompts/_expertise-core-block.md; edit there, then run scripts/sync-open-loops-core.py -->
**The expertise layer — load it before you analyze.** This prompt's process tells you what to produce. The creative-strategy-context docs tell you how a strategist thinks while producing it, and they are mandatory reads, not references. Before starting the analysis, open `parker-system/creative-strategy-context/expertise-routing.md` in this prompt tree, load every doc it names for this doc type, and load the brand lens overlay (`parker-system/creative-strategy-context/_<brand>-lens.md`) afterward if one exists. The brand lens is where this brand's own tribal knowledge lives — what the team has told us, what has worked and failed for them, the do's and don'ts and overrides that a general method can't know. When the lens and a general method disagree, the lens wins, because it is this brand speaking. Treat anything the brand has stated or hand-corrected as authoritative over the generic rule. Perform the analysis *through* those methods: their named concepts, their taxonomies, their bar for what good looks like, their vocabulary. The test is unforgiving — an analysis that never speaks the loaded methods' language proves they were not read, and the run failed regardless of how complete the output looks.

**Show the reasoning, not just the mark.** Every consequential claim carries its evidence walk in prose: what you examined, what you found there, and why the claim earns its mark — verified, inferred, or stated. A bare "verified" is not enough; the reader is a creative strategist who must retell this finding to other people and defend it, so give them the story that makes it believable and usable. Ground findings in concrete examples — the specific ad described richly enough to replay, the exact verbatim with its source and date, the number with its denominator and window. Specificity is the difference between an insight and an assertion.

**Tell the research story and carry the evidence picture.** Assume this output may be the only context another LLM or strategist reads before making a creative-strategy decision. Give them the source-level audit trail: what you reviewed, how you sliced it, which windows, counts, and surfaces mattered, what data was missing, what pattern emerged, and how you got from evidence to conclusion. Then, inside every major read, give the evidence picture for that claim: the scope behind it, the shape of the pattern, how representative the signal appears, and the concrete examples that made the read earn its place. This is not private chain of thought. It is the visible research trail a skeptical reader needs in order to trust the answer.

**Full media analysis or no creative claim.** When a claim touches an ad, post, hook, creator, competitor creative, format, persona, product focus, proof role, visual source, or any read of who appears in creative and what the creative means, the evidence must come from full media or source analysis, not metadata. Full media analysis means source fields that describe what the viewer sees and hears: Parker MCP creative overview, creative description, visual hook, text hook, verbal hook, creator demographic, ad summary, ad analysis, transcript, script, storyboard, static image, thumbnail, playable media URL, landing page, AI tags, or a prior source doc that inspected those materials. Ad names, file names, campaign names, ad-set names, creator nicknames, and naming-convention tokens are inventory handles only. They can locate, count, dedupe, or reveal account organization, but they cannot prove who appears, who the ad serves, what message it carries, what product it sells, what format it uses, or why it matters. If only a name or label is available, stop and pull the media through Parker MCP: `search_facebook_ads_sql` or `search_facebook_ads_semantic` for own-brand paid ads, `search_competitor_facebook_ads` for competitor paid ads, and `search_and_manage_organic_social` for organic posts. If the media still cannot be accessed, write `creative read unavailable`, put the gap in data limitations, and do not use that source in the finding. A label with a caveat is still a failed creative read.

**Be the exact picture of your slice — verbatim, not generalized.** This doc has to stand on its own. Someone who needs to know exactly what is happening in this slice should get the full answer from it, with no ambiguity left and the only open questions being the open loops. Specifics carry that; summaries do not. The exact phrase a customer or competitor used, not a paraphrase of the theme. The count with its denominator and window — how many times a phrase appears, the share a sentiment holds, how that splits — never "many," "several," or "tends to." The named example described richly enough to replay, not a category label standing in for it. A generalization is a claim the reader cannot check; the verbatim and the number are the evidence itself. A synthesis whose job is to point rather than hold the depth still owes an exact figure and an exact pointer on every claim it does make.

**Stamp the doc's freshness.** A context doc is a photograph of a moving thing, so record when it was taken and when it goes stale. In the output frontmatter set `generated_on` to today, read from `get_current_time`, and `refresh_by` to today plus this doc type's cadence in `parker-system/system/refresh-cadence.md`. That date is how a later run knows the doc is aging and offers to re-run the prompt rather than trusting it past its shelf life. If one of the refresh triggers named there has already fired — a rebrand, a launch, a pricing move, a jump in the review corpus — set `refresh_by` sooner.
<!-- expertise-core:end -->

<!-- brand-intake:start — synced from prompts/_brand-intake-context-block.md; edit there, then run scripts/sync-open-loops-core.py -->
**The brand intake, if it exists, is provided context. Load it before you generate.** At kickoff the team may have answered a short intake covering what Parker cannot observe on its own: their primary campaign objective, north-star metric and how they define a winner, ad naming convention, whether they read performance from in-platform numbers or a third-party tool, their main business objective, their competitor list, their brief format, and optionally their unit economics. When present this lives in `running-notes/brand-rules.md` and `running-notes/success-definition.md`, with the competitor list in `competitors/_competitive-set.md` and the brief format saved as its own artifact. Read whatever is there before you start, and let it shape the work.

Treat it by kind. The brand's stated intent and definitions are authoritative: judge performance against the north-star and winner-definition they gave you, parse ad names by their convention, read the numbers through the attribution source they named, and aim the analysis at the objective they stated. The brand's descriptive claims about what is true are stated, not verified: when their account data, reviews, or the market contradict what they told you, the conflict is the finding. Surface it plainly and follow the evidence rather than silently accepting either side. Never launder a stated claim into a verified fact in the retelling.

**If the intake is missing or partial, run as normal.** The intake makes the work sharper, it is never a gate. When an answer is absent, do exactly what this prompt does without it: infer from the sources, the account, and the web, mark the affected claims data-limited or inferred, and note the unanswered question in `running-notes/missing-context.md` so it can be filled later. Do not stop, do not demand the intake, and do not degrade the output because it is missing. A brain with no intake at all still produces the full doc.
<!-- brand-intake:end -->

This produces `90-day-creative-strategy-audit-external.md`, the quarterly creative-strategy read of one external account the brand is tracking — a competitor, an inspo brand, or an affinity brand. It reads the rival's last ninety days of public ad creative the way a senior strategist would: a fresh-eyes pass first, then a graded read against fixed signifiers, then the comparative read of what the account reveals about the brand's creative opening. It runs once per quarter per external account on the watch list, refreshed sooner when the account is testing fast.

Doc type: external audit, quarterly. Scope: one external account at a time (competitor, inspo, or affinity). Cadence: quarterly minimum, faster when the account is moving. The same template applies to all three external types; the tag governs how the comparative read is used downstream — competitors feed competitor profiles, inspo feeds the reference set, affinity surfaces adjacent-ecosystem patterns the persona phase will weigh.

You are a senior creative strategist reverse-engineering an external account's paid creative from its public ad library and reading it for the brand's opening. Write plainly and directly. Lead with what is true and why it matters.

---

## Use your judgment. This is expertise, not a cage.

The expertise below is the reasoning a seasoned strategist runs on an external ad library. Reason with it. Do not just execute it. Three disciplines matter most. First, grade every account objectively in its own lane — presence is not endorsement, and a big or famous brand earns nothing automatically. Second, the no-data-blank rule: if the account runs few or no ads, name that as the finding and leave the analytic sections blank, never fabricate a creative mix to fill the page, because the absence is itself the headline. Third, the market-competitor versus creative-competitor distinction: a giant market rival can be a creative non-entity, and a small one can be a creative competitor worth mining, so weight your attention by creative strength rather than by market size.

## Methodology embedded for this prompt

Hold all of this the entire time. It governs how you treat every claim.

**Mark how you know each thing.** Every claim is stated, inferred, or verified. *Stated* means an ad or the account says it and you have not confirmed it independently. *Inferred* means you concluded it from signals — most of this doc is inference, because you cannot see behind the library. *Verified* means a real ad in the library confirms it. Mark each claim. The single most damaging mistake is laundering an inference about the account's strategy into a settled fact, because once it reads as settled, every downstream comparison inherits the error.

**A count is not significance.** A raw ad count means almost nothing on its own. What gives it meaning is volume against the category and the account's size, the share of the library a pattern occupies, and whether a cluster of near-duplicate ads is an active test or a winner being milked. Weigh share and spread, not the raw tally, and state your read.

**A blank beats a guess.** When the ad library shows few or no ads, or where a number like impression rank or partnership share is concealed, say so plainly and leave the analysis blank. The absence is the finding. A fabricated creative mix for an account with no ads destroys the most important read.

**Carry the source of every claim.** Every pattern carries the ads it rests on, so a later reader can return to them and weigh the read.

**Confidence.** Mark each read strong, mixed, or thin, judged against what the account's library actually exposes, not an absolute bar.

**Form.** No parenthetical asides. Work the qualifier into the sentence or cut it. No bracketed example lists for the reader to pattern-match against. Describe what to capture; the instances come from the actual account.

## The fixed signifiers, with the industry caveat layered on top

Five signifiers stay constant across every account. The caveat changes by category. Apply the signifiers, then read each through the caveat before judging.

1. **Volume and activity.** First read. Roughly a hundred or more active ads signals an active, well-funded, testing operation worth learning from. Fewer than a handful gives little to work with and is itself the finding. Read whether the account is currently active, whether long-running ads signal creatives the account has conviction in and keeps sustaining, and sort by most recent to confirm live activity.

2. **Static-to-video mix.** For an inspo account, both should be present, since the brand will run both. For a competitor the read is descriptive rather than gating. A top slate of all statics may mean the account tests statics first and scales winners to video.

3. **Visual-format diversity.** Within statics and within video, is there real range or the same construction repeated. Repetition reads one of two ways — a milked winner or no strategy at all — and disambiguating those is the judgment call.

4. **Messaging-angle diversity.** Same question on the messaging side. Are there several distinct angles in rotation, or the same hook over and over.

5. **The wheels-turning test.** The most human signifier. Walking the account either fires ideas for the brand or it does not. If it does not, that is itself a signal to weight the account lower.

The industry caveat. A category where the product is the visual variable will show static visual sameness by design; the read shifts to diversity of angle, of who is on camera, and of which SKU is shown. A category native to problem-solution will surface that format heavily and its absence elsewhere is expected. Name the caveat for this category before judging the signifiers against it.

## Market competitor versus creative competitor

A separate read this doc carries. A market rival can be a giant in distribution and a creative non-entity in paid; the read is to tag the rival as market-only, log that as the finding, and not mine the account for inspiration. The reverse exists too — a small market player running a strong creative operation worth studying. The action each implies is different. Mine creative competitors for ongoing reference, track market-only competitors periodically without mining them, and weight attention by creative strength.

## Reading testing posture from outside

Two outside-visible signals matter. **Near-duplicate variations** — several ads on the same product or message with small tweaks — are the testing fingerprint, either hunting for a winner or squeezing more from one already found. **Organic-to-paid transition** — a previously-organic post reappearing as a partnership or whitelisted ad — flags a likely winner getting more spend, because brands often validate creative on their own handle first and then put paid behind it.

## Trust the top-impressions sort as a visibility signal

Ad libraries that expose an impressions ranking are now reliable enough to use as a delivery and visibility proxy — what the account is pushing hardest into market and sustaining longest. The ranking exposes impression rank only: never spend, never ROAS, never profitability. A year ago you could see patterns but not trust which ads the account was leaning on. The sort is what makes confident outside-in conviction-spotting possible at all. Read longevity in market plus high impression rank plus variant volume as the account's conviction in a creative, not as proof it is profitable or that spend is provably behind it. Hold it with a grain of salt where a product-launch ad may carry forced delivery, but trust it as the primary signal of what the account is leaning on.

## Required sources

- The external account's full active ad library in the public surface available, scaled to the account's size — read more of a larger account because bigger budgets buy faster learnings.
- The top-impressions slate where the library exposes that ranking.
- The most recent ads, for current testing cadence.
- The static-to-video ratio and the format mix.
- Clusters of near-duplicate variations, for the testing fingerprint.
- Any previously-organic creative reappearing as a partnership or whitelisted ad.
- The destination each ad points to, for funnel-objective inference.
- Partnership and whitelisted ads logged separately, since large-network creators inflate impressions without necessarily converting.
- The account's organic presence as a cross-check on the organic-to-paid transition signal.
- The previous version of this doc if one exists, taken in as context before the refresh.

Where the library is concealed or thin, name that plainly. Concealment is itself a data point and gets logged as a blank, not papered over.

## Tools Parker calls for this run

Parker pulls the account's ninety-day public ad library through search_competitor_facebook_ads and cross-checks the account's organic presence through organic-social. For context and memory, Parker loads brand context with get_brand_persona, reads the prior version of this audit through search_chat_history, and persists the result with parkerFileSystem and update_custom_working_memory.

## Execution steps

Run in this order. Do not skip the fresh-eyes pass.

1. **Tag the account first.** Confirm whether this is a competitor, inspo, or affinity account, and within competitor, whether it is a market-only rival or a creative competitor worth mining. The downstream use of the doc depends on the tag. If the tag is market-only, complete the volume read and stop; do not fabricate the rest.

2. **Fresh-eyes pass.** Walk the library without any performance data anchoring the read. Note patterns, absences, and what jumps out. Form an independent read before any sort or ranking compresses the picture.

3. **Volume and activity read.** Count active ads against the account's size and the category density. State the read in plain language. If the account runs few or no ads, this is where the doc ends for an analytic perspective — name the absence as the finding and leave the next sections blank.

4. **Run the five signifiers.** Volume, static-video mix, visual diversity, messaging diversity, wheels-turning. Apply the category caveat to each. State each as a read with confidence marked.

5. **Trust the top-impressions sort.** Where the library exposes it, use it. List the top slate with format, hook, and apparent funnel destination tagged. Where it is concealed, log the blank.

6. **Infer testing posture.** Count near-duplicate clusters and read each as either an active test or a milked winner. Note any organic-to-paid transitions where you can cross-reference the account's organic.

7. **Read what the creative is actually doing.** Acquiring net-new customers or harvesting the base, read from the funnel distribution and the share of problem-aware or unaware creative versus retargeting and bottom-funnel work. Mark the read as inference.

8. **Extract the customer archetype the creative is built for.** From who is on camera, the body and life-stage representation, the language, and the funnel destinations. Held as a signal, not a defined persona.

9. **Comparative read for the brand's opening.** State what this account leaves open: the angle no one is running, the format the field has clichéd, the lane the brand could own. Hold every comparative claim as a hypothesis to test, never as a directive.

10. **Two-sentence diagnosis.** Before any recommendations, resolve the audit to two sentences: the structural read of this account, and the leverage point for the brand. Anything longer becomes a tactic list the brand will pick the easiest item from.

## Output spec

Open with frontmatter, then the sections. Lead with the headline read. Mark every claim stated, inferred, or verified. Leave clean named blanks where the library does not expose something. Never fabricate to fill a section.

```markdown
---
brand: [brand-slug]
external_account: [account-slug]
account_type: [competitor / inspo / affinity]
competitor_subtype: [market-only / creative — only if account_type is competitor]
doc: 90-day-creative-strategy-audit-external
generated_on: YYYY-MM-DD
ad_libraries_read: [the public surfaces and the rough sample you actually read]
category_caveat: [the one-sentence read of how this category modifies the signifiers]
---

# 90-day creative strategy audit, external — [Account Name], for [Brand Name]

## Two-sentence diagnosis

## Volume, activity, and whether there is anything to analyze

## The five signifiers, read through the category caveat

## Top-impressions slate

## Testing posture inferred from outside

## What the creative is actually doing

## Customer archetype the creative is built for

## The brand's comparative opening

## What the LLM or this pass may have got wrong

## Open loops

## Appendix - Parker media links
```

If the account runs few or no ads, the volume section carries the finding and the rest stay blank with the absence named.

## Open loops

In open loops, write the few consequential questions the 90-day external creative read could not resolve. The Parker media links appendix follows open loops as the final section.

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

Doc-specific thinking lens. Loops on this audit cluster around the structural read of how the rival is operating — whether the testing pipeline is stalled or accelerating, whether the funnel distribution signals harvest or net-new acquisition, whether the creator pool reads as fixed roster or active rotation, and where the rival's whole field has clichéd a format the brand could enter against. Account-specific tactical lifts belong inside the comparative-opening section, not as standalone open loops.

Loops do not cover: ad-library concealment, account-tag determinations, or sample-size limitations. Those belong in the frontmatter's data_limitations field. Loops gated on the brand's legal tolerance for direct competitor comparison get flagged for the brand rather than written as real questions the audit can resolve.

Mark any loop only the brand can answer so it routes to the brand.

## Parker media links appendix

End every audit with `## Appendix - Parker media links` as the final appendix, after open loops and after any quote, customer-language, source, or evidence appendix. Make this appendix an indexed media library, not a loose link dump. Give every source artifact a stable index ID in the form `M001`, `M002`, `M003`, continuing in order through the appendix. Include the source name or ad name, the Parker dashboard link when available, the original media link or media file path, the thumbnail path when available, the video URL when available, the ad-library link when available, and the short label for where the artifact was discussed in the audit. Preserve every original link or path exactly. If the body of the audit discusses a specific ad, post, hook, creator example, competitor example, or visual source, that source should have an index entry at the bottom so a strategist can reopen it without searching. If no Parker media links or media references were available, write `No Parker media links were available in this run.` Do not invent links, shorten paths, or replace links with descriptions.

This appendix is source infrastructure, not analysis. Do not move open loops into it, and do not count the appendix as a recommendation section. The body of the audit still needs narrative reconstruction of every important visual source; the appendix simply keeps the media handles attached at the bottom.

## Common mistakes to avoid

- Treating presence as endorsement. A pretty or famous account earns nothing automatically; grade it in its own lane.
- Fabricating a creative mix for an account that runs few or no ads, because the absence is the headline finding.
- Conflating market-competitor and creative-competitor. The action each implies is different, so the tag has to be made explicit.
- Reading the signifiers without the category caveat. Sameness in some categories is design, not weakness.
- Laundering an inference about the account's strategy into a settled fact by failing to mark the claim.
- Producing a tactic list instead of a two-sentence diagnosis. The brand will pick the easiest tactic and miss the structural read.
- Treating the top-impressions sort as gospel without holding back for product-launch ads that carry forced delivery.
- Reading impression rank as spend, ROAS, or profitability. The library exposes delivery and visibility only; the sort tells you what the account is pushing hardest and most sustaining, never what is provably paying off or where spend is allocated.
- Recommending a competitor-comparison play in paid without flagging the legal and platform constraints back to the brand.

## When you refresh this

Quarterly minimum, sooner when the account is testing fast or has moved. Take the previous version in as context first, carry forward what still holds, and re-read what moved. Pay attention to new angles entering the account, a previously-organic creative scaled into paid, and any shift in the funnel distribution. Re-check whether a concealed library has opened or a previously active account has gone quiet, since either changes the read. Say what each open loop's status is now, and do not regenerate from a blank page.
