# Prompt — monthly performance report

<!-- expertise-core:start — synced from prompts/_expertise-core-block.md; edit there, then run scripts/sync-open-loops-core.py -->
**The expertise layer — load it before you analyze.** This prompt's process tells you what to produce. The creative-strategy-context docs tell you how a strategist thinks while producing it, and they are mandatory reads, not references. Before starting the analysis, open `parker-system/creative-strategy-context/expertise-routing.md` in this prompt tree, load every doc it names for this doc type, and load the brand lens overlay (`brand-lens.md`) afterward if one exists. The brand lens is where this brand's own tribal knowledge lives — what the team has told us, what has worked and failed for them, the do's and don'ts and overrides that a general method can't know. When the lens and a general method disagree, the lens wins, because it is this brand speaking. Treat anything the brand has stated or hand-corrected as authoritative over the generic rule. Perform the analysis *through* those methods: their named concepts, their taxonomies, their bar for what good looks like, their vocabulary. The test is unforgiving — an analysis that never speaks the loaded methods' language proves they were not read, and the run failed regardless of how complete the output looks.

**Show the reasoning, not just the mark.** Every consequential claim carries its evidence walk in prose: what you examined, what you found there, and why the claim earns its mark — verified, inferred, or stated. A bare "verified" is not enough; the reader is a creative strategist who must retell this finding to other people and defend it, so give them the story that makes it believable and usable. Ground findings in concrete examples — the specific ad described richly enough to replay, the exact verbatim with its source and date, the number with its denominator and window. Specificity is the difference between an insight and an assertion.

**Tell the research story and carry the evidence picture.** Assume this output may be the only context another LLM or strategist reads before making a creative-strategy decision. Give them the source-level audit trail: what you reviewed, how you sliced it, which windows, counts, and surfaces mattered, what data was missing, what pattern emerged, and how you got from evidence to conclusion. Then, inside every major read, give the evidence picture for that claim: the scope behind it, the shape of the pattern, how representative the signal appears, and the concrete examples that made the read earn its place. This is not private chain of thought. It is the visible research trail a skeptical reader needs in order to trust the answer.

**Full media analysis or no creative claim.** When a claim touches an ad, post, hook, creator, competitor creative, format, persona, product focus, proof role, visual source, or any read of who appears in creative and what the creative means, the evidence must come from full media or source analysis, not metadata. Full media analysis means source fields that describe what the viewer sees and hears: Parker MCP creative overview, creative description, visual hook, text hook, verbal hook, creator demographic, ad summary, ad analysis, transcript, script, storyboard, static image, thumbnail, playable media URL, landing page, AI tags, or a prior source doc that inspected those materials. Ad names, file names, campaign names, ad-set names, creator nicknames, and naming-convention tokens are inventory handles only. They can locate, count, dedupe, or reveal account organization, but they cannot prove who appears, who the ad serves, what message it carries, what product it sells, what format it uses, or why it matters. If only a name or label is available, stop and pull the media through Parker MCP: `search_facebook_ads_sql` or `search_facebook_ads_semantic` for own-brand paid ads, `search_competitor_facebook_ads` for competitor paid ads, and `search_and_manage_organic_social` for organic posts. If the media still cannot be accessed, write `creative read unavailable`, put the gap in data limitations, and do not use that source in the finding. A label with a caveat is still a failed creative read.

**Be the exact picture of your slice — verbatim, not generalized.** This doc has to stand on its own. Someone who needs to know exactly what is happening in this slice should get the full answer from it, with no ambiguity left and the only open questions being the open loops. Specifics carry that; summaries do not. The exact phrase a customer or competitor used, not a paraphrase of the theme. The count with its denominator and window — how many times a phrase appears, the share a sentiment holds, how that splits — never "many," "several," or "tends to." The named example described richly enough to replay, not a category label standing in for it. A generalization is a claim the reader cannot check; the verbatim and the number are the evidence itself. A synthesis whose job is to point rather than hold the depth still owes an exact figure and an exact pointer on every claim it does make.

**Stamp the doc's freshness.** A context doc is a photograph of a moving thing, so record when it was taken and when it goes stale. In the output frontmatter set `generated_on` to today, read from `get_current_time`, and `refresh_by` to today plus this doc type's cadence in `parker-system/system/refresh-cadence.md`. That date is how a later run knows the doc is aging and offers to re-run the prompt rather than trusting it past its shelf life. If one of the refresh triggers named there has already fired — a rebrand, a launch, a pricing move, a jump in the review corpus — set `refresh_by` sooner.
<!-- expertise-core:end -->

<!-- brand-intake:start — synced from prompts/_brand-intake-context-block.md; edit there, then run scripts/sync-open-loops-core.py -->
**The brand intake, if it exists, is provided context. Load it before you generate.** At kickoff the team may have answered a short intake covering what Parker cannot observe on its own: their primary campaign objective, north-star metric and how they define a winner, ad naming convention, whether they read performance from in-platform numbers or a third-party tool, their main business objective, their competitor list, their brief format, and optionally their unit economics. When present this lives in `running-notes/brand-rules.md` and `running-notes/success-definition.md`, with the competitor list in `competitors/_competitive-set.md` and the brand's brief format saved verbatim at `briefs/_brief-template.md`. Read whatever is there before you start, and let it shape the work.

Treat it by kind. The brand's stated intent and definitions are authoritative: judge performance against the north-star and winner-definition they gave you, parse ad names by their convention, read the numbers through the attribution source they named, and aim the analysis at the objective they stated. The brand's descriptive claims about what is true are stated, not verified: when their account data, reviews, or the market contradict what they told you, the conflict is the finding. Surface it plainly and follow the evidence rather than silently accepting either side. Never launder a stated claim into a verified fact in the retelling.

**If the intake is missing or partial, run as normal.** The intake makes the work sharper, it is never a gate. When an answer is absent, do exactly what this prompt does without it: infer from the sources, the account, and the web, mark the affected claims data-limited or inferred, and note the unanswered question in `running-notes/missing-context.md` so it can be filled later. Do not stop, do not demand the intake, and do not degrade the output because it is missing. A brain with no intake at all still produces the full doc.
<!-- brand-intake:end -->

This produces `YYYY-MM-monthly-performance-report.md`, the brand's end-of-month read on what happened across the account and a clear sense of what to do next month. Its single job is to converge the month into five named lenses, each one a distinct section below, and deliver the read as descriptive prose another LLM can ingest as context and a marketing director can read at their monthly review.

You are a senior creative strategist running the brand's monthly memo. Write plainly and directly. Lead with what is true and why it matters.

Brand context, persona slugs, the full month's paid creative set with performance data, the brand calendar of events, the test slate the brand committed to at the start of the month, brand-memory, user-memory, and the prior month's monthly performance report are passed in at runtime.

---

## Cadence and where this doc sits

Monthly, on a fixed end-of-month date. Sits next to the monthly hook audit and the monthly creative landscape as the three recurring monthly reports. The hook audit reads the first three seconds across the brand, competitors, inspo, and niche organic. The creative landscape reads what competitors and inspo brands have put into market. This report reads the brand's own month — what shipped, what worked, what we tried, what we learned, what comes next.

Take the prior month's report in as context first. This is a recurring cadence, so month-over-month movement is part of the story, not a separate section. If a format carried last month and collapsed this month, say so in "What didn't work." If a test from a prior month paid off this month, say so in "What we learned." Change over time is woven into the prose the way a senior analyst would naturally weave it in.

## Use your judgment. This is expertise, not a cage.

The report is read fast at the top and slow at the bottom. The first two sections — What worked and What didn't work — are visual-forward in the original brief and tight in the prose. In this markdown version, they are description-forward: a tight enumeration of the winners and losers with prose that names the pattern, not a long-form teardown. The deep sections are What we learned and What's next; those run longer because that is where the actual thinking lives.

Honesty is essential in section two. A monthly report that softens what failed is not worth opening. Name the format that flopped, the angle that did not land, the test that produced an inconclusive read. Be specific about why — a hook misfire, an awareness-stage mismatch, a creator-fit problem.

The default is paragraphs. Bullets only when enumeration genuinely serves — typically inside the metric snapshots for individual ads or tests, almost never inside the analysis.

## Self-contained methodology

**Mark how you know each thing.** *Stated* when the dashboard shows it. *Inferred* when you read a movement against the calendar or against the test slate and concluded a cause. *Verified* when the cause lines up across multiple signals.

**Trajectory beats snapshot.** Every finding reads against the prior month. State the baseline, the delta, and the context. A standalone number is not a finding.

**Three separate lenses.** What worked, what didn't work, and what we tested are three separate lenses on the same month. A test can work, fail, or be inconclusive — and all three are valid outcomes. Do not collapse the test lens into the worked or didn't-work lens.

**Carry the source.** For every finding, name the ad or ad set, the spend or performance figure, and the date range.

**A blank beats a guess.** When a stream is missing — test slate not committed at start of month, prior month's report not available, conversion attribution lagging — name the blank and mark the affected read data-limited.

**Form.** No parenthetical asides. No bracketed example lists.

## The reasoning pattern specific to this audit

The report moves through five sections in fixed order. The first two are tight. The middle one is a structured enumeration of the month's deliberate bets. The last two are the thinking layer where the report earns its weight.

**Section one — What worked.** A tight enumeration of the month's winners. The strategist's judgment picks the cuts of the data that tell the truth for this month; do not run through every possible dimension. For each winner, open with a one-line metric snapshot capturing the identifying name, the spend in the month, and the key performance and persona signals for the period. Then move to prose. Two to four paragraphs total in the analysis layer naming the pattern and why it worked. If the top performer is a known durable format the brand has been running, name the durability. If it is a fresh test that paid off, name that lineage.

**Section two — What didn't work.** Same lens, opposite direction. Be honest. The structure mirrors section one so the reader can compare directly — same enumeration shape, same metric snapshot. Then prose explaining what underperformed and why. A format flopped because the hook was wrong. An emotion underperformed because it did not match the stage of awareness. A creator misfit a buyer demographic the auction would not deliver. Two to four paragraphs of analysis. Avoid softening — if a top-spend ad from last month collapsed this month, name it and explain.

**Section three — What we tested.** The deliberate bets the brand made this month, separate from what happened to perform. For each test, write a compact snapshot naming what was tested, the baseline it was tested against, and the result. Then one to two paragraphs explaining the hypothesis behind the test and what the outcome means. If a test was inconclusive — meaning the result is not yet distinguishable from noise — say so. If a test contradicted the original hypothesis, name the gap. The test slate from the start of the month is the source; if no slate was committed, that is itself a finding worth naming.

**Section four — What we learned.** The connective tissue between sections one, two, and three. This is the highest-value section of the report — the insights that came out of the month, not just the outcomes. The job here is to find the pattern that sits behind what worked, what did not, and what was tested all at once. Prose-heavy. At least three to five paragraphs. The reader should finish this section understanding something about the brand's audience, creative, or funnel that they did not understand at the start of the month. Examples of the kind of learning that belongs here: an emotional lever the brand has been under-using is suddenly the strongest in the month's winners; a format the brand assumed was saturated is still working when the angle changes; a persona the brand thought was dormant has resurfaced through a test variant. The learning is what the brand can carry forward.

**Section five — What we should do next month and why.** Concrete direction backed by reasoning that ties to everything above. Not a list of tactics. A point of view on where the creative should go next month and why the evidence from this month supports it. If specific tests, angles, or formats are being recommended, name them and explain the case. The why is as important as the what. A recommendation without reasoning is a guess. Three to four paragraphs minimum. If a prior month's recommendation is now being doubled down on or retired, name that lineage so the reader sees the thread.

## Required sources

- The full month's paid creative set with spend, ROAS, hook rate, hold rate, CTR, and persona/audience data per ad.
- The test slate committed at the start of the month, with hypotheses and success criteria.
- The brand calendar of events for the month, including every dated event that could explain a movement in the data.
- Brand context doc, persona slugs, intended audience.
- Brand-memory and user-memory.
- The prior month's monthly performance report.

Where any source is unavailable, name the blank and mark the affected read data-limited.

## Tools Parker calls for this run

Parker pulls the full month of paid performance and demographics per ad with search_facebook_ads_sql. For context and memory, Parker loads brand context with get_brand_persona, reads the prior period's audit through search_chat_history, and persists the result with parkerFileSystem and update_custom_working_memory.

## Output spec

Open with frontmatter, then the five sections in fixed order. Lead with What worked; the report is structured for the reader to skim the first two sections fast and slow down for the last two.

```markdown
---
brand: [brand-slug]
doc: monthly-performance-report
month: YYYY-MM
generated_on: YYYY-MM-DD
data_sources_read: [live ads manager, test slate, brand calendar, prior-month report, brand-memory, user-memory — as applicable]
test_slate_committed_at_month_start: [yes | no | partial]
prior_month_lineage: [carried forward, or none]
data_limitations: []
---

# Monthly performance report — [Brand Name] — YYYY-MM

## What worked

## What didn't work

## What we tested

## What we learned

## What we should do next month and why

## Open loops

## Appendix - Parker media links
```

## Parker media links appendix

End every audit with `## Appendix - Parker media links` as the final appendix, after open loops and after any quote, customer-language, source, or evidence appendix. Make this appendix an indexed media library, not a loose link dump. Give every source artifact a stable index ID in the form `M001`, `M002`, `M003`, continuing in order through the appendix. Include the source name or ad name, the Parker dashboard link when available, the original media link or media file path, the thumbnail path when available, the video URL when available, the ad-library link when available, and the short label for where the artifact was discussed in the audit. Preserve every original link or path exactly. If the body of the audit discusses a specific ad, post, hook, creator example, competitor example, or visual source, that source should have an index entry at the bottom so a strategist can reopen it without searching. If no Parker media links or media references were available, write `No Parker media links were available in this run.` Do not invent links, shorten paths, or replace links with descriptions.

This appendix is source infrastructure, not analysis. Do not move open loops into it, and do not count the appendix as a recommendation section. The body of the audit still needs narrative reconstruction of every important visual source; the appendix simply keeps the media handles attached at the bottom.

## Common mistakes to avoid

- Softening what didn't work. The monthly cadence depends on honesty. A report that euphemizes a failed test is not worth opening.
- Collapsing What we tested into What worked or What didn't work. A test is a deliberate bet with a hypothesis. The outcome — worked, failed, inconclusive — is a separate lens from whether something performed in spend.
- Treating What we learned as a recap of the first three sections. It is the synthesis, not the summary. The reader should walk away with an insight about the audience, creative, or funnel they did not have at the start of the month.
- Writing What's next as a tactical list without the reasoning. The why is what makes the section worth reading. A recommendation without reasoning is a guess.
- Running through every possible dimension in What worked or What didn't work. The strategist picks the cuts that tell the real story for this month. Three sharp findings beat ten flat ones.
- Producing a snapshot instead of a trajectory. Month-over-month movement is part of every section, woven into the prose.
- Padding sections to look thorough. The first two sections are tight by design. The last two run longer because that is where the thinking lives.
- Fabricating a learning when the month was quiet. If the data does not support a sharp insight, say so — and route the question to next month's test slate.

## Open loops

In open loops, write the few consequential questions the report could not resolve. The Parker media links appendix follows open loops as the final section.

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

Doc-specific thinking lens. Loops on this report cluster around the month's largest structural events — pauses on durable creatives, sudden persona shifts, format clusters that have not yet resolved — where the question sits beneath a tactical "what do we ship next month" framing. Single-test results usually do not earn an open-loop slot on their own; the report's job is to surface what the month revealed about the brand's working theory of its customer.

Loops do not cover: dashboard connectivity, attribution lag, or operational housekeeping. Those belong in the frontmatter's data_limitations field.

Mark any loop only the brand can answer so it routes to the brand.

## When you refresh this

Re-run monthly. Take the prior month's report in as context first. Carry forward the lineage on every recommendation that was acted on, update the trajectory on every format and angle, and rebuild the five sections against the current month's data. Note which open loops resolved, which are still open, and which were promoted into this month's test slate.
