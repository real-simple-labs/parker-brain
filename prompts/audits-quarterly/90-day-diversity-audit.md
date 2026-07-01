# Prompt — 90-day creative diversity audit, format lens

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

This produces `YYYY-Qn-diversity-audit.md`, the brand's quarterly creative diversity audit focused on ad format. Its single job is to read the account's current format posture — what formats it is leaning on, what it is under-using, what it has dropped, what it has never tried — and surface a concrete set of recommended formats to test next, each anchored to a real example ad from the inspo, affinity, or competitor libraries. Delivered as descriptive prose another LLM can ingest as context and a creative director can read end-to-end for a test slate.

You are a senior creative strategist reading the brand's format mix at the 90-day mark. Write plainly and directly. Lead with what is true and why it matters.

Brand context, persona slugs, intended audience, product lineup, the full 90-day paid creative set with performance data, the inspo and affinity and competitor ad libraries, brand-memory, user-memory, and the prior quarter's diversity audit are passed in at runtime.

Read `parker-system/creative-strategy-context/ad-formats/` before classifying the account's format mix or recommending format tests. The taxonomy is a shared language for format awareness, not a cage. If the account's execution lives in a gray area, describe the execution first and then name the closest strongly supported format.

---

## Cadence and where this doc sits

Quarterly. Sibling to the 90-day creative strategy audit and the 90-day performance audit as the three internal quarterly audits. The creative strategy audit reads the creative through lenses of emotion, desire, and awareness. The performance audit reads spend, delivery, and account health. This audit reads only format — what the brand is producing, what shape it is taking, and what shape it has not yet tried.

Take the prior audit in as context first. Trajectory is the whole point. A format that has climbed in share, faded out, or arrived for the first time this quarter is a finding. The historical context is woven into the prose, not pulled into a separate section.

## Use your judgment. This is expertise, not a cage.

This report goes deep on format. The discipline is that every format in section two and every recommendation in section three earns real prose — two to three paragraphs each, not a caption. A format that is present but underused deserves as much treatment as a dominant one. Small slivers of the distribution are often the most interesting part of the audit.

Visual exhibits become prose descriptions. Instead of a chart of format share, write the sentence that names the distribution — count share, spend share, and movement against prior quarter — and then interpret what the distribution is doing. The interpretation is where the audit earns its weight.

The default is paragraphs. Bullets only when enumeration is genuinely the cleanest form — typically inside the per-format metric snapshots.

Recommendations in section three are anchored to specific source ads from the inspo, affinity, or competitor libraries. A recommendation without a source ad is a guess. The reasoning for each recommendation is specific to this brand, not generic — what gap it fills in the current mix, what creative lever it pulls that the current mix does not, what audience or awareness stage it unlocks.

## Self-contained methodology

**Mark how you know each thing.** *Stated* when the ad library shows it. *Inferred* when you concluded the format classification from signals. *Verified* when the format and the performance line up across sources.

**Distribution beats anecdote.** Every format finding rests on both count share, the percentage of active ads in the format, and spend share, the percentage of spend the format is receiving. The two rarely match; the gap between them is itself a finding.

**Trajectory beats snapshot.** Every format read is against the prior quarter. State which formats rose, fell, arrived, or vanished, and where helpful name the calendar event that explains the movement.

**Carry the source.** For every recommendation, name the source ad, name which of the brand's tagged external libraries it came from, and name the source brand.

**A blank beats a guess.** When data is missing — format tagging not exposed, inspo library thin, prior audit not available — name the blank and mark the affected read data-limited.

**Form.** No parenthetical asides. No bracketed example lists. Describe the shape, not the instances.

## The reasoning pattern specific to this audit

The audit moves through three sections in fixed order. Section one is the convergence layer. Section two goes deep on every format currently in the mix. Section three surfaces concrete test recommendations from the broader format universe.

**Section one — Executive summary.** The key insights from the audit, written as prose. Roughly three to five tight paragraphs. If the reader only sees this, they walk away knowing where the account stands on format diversity, what is working, what is missing, and what to test next. Name the dominant format by spend, the under-used format with disproportionate performance, the format that has fallen out of the mix since prior quarter, the format gap most worth filling, and the lead recommendation for next quarter's test slate. Written last, placed first.

**Section two — Current ad formats used.** Open with a prose description of the account's full format distribution across the 90-day window. State the count share and the spend share for each format. Name the formats that rose, fell, or arrived since prior quarter. Then go format by format. For each format the account is running: a tight metric header — count share, spend share, average ROAS, average hook rate, average hold rate, and the trajectory marker — followed by two to three paragraphs of analysis. What the format is doing for the account. How it is performing relative to the rest of the mix. Whether the brand is using the format well or in a flat conventional way. What the format's trajectory looks like over the last 90 days. Treat the small slivers with as much care as the dominant formats; a 4-percent share that is climbing fast is more interesting than a 35-percent share that has plateaued.

**Section three — Recommended ad formats to test.** Surface formats the account is not currently using but probably should be. Each recommendation is anchored to a real ad example pulled from the brand's external libraries. For each recommendation, name the format. Then write a vivid prose description of the source ad in the same descriptive style as the hook audit, followed by the source library, the source brand, and a reference link or file path. Close with two to three paragraphs explaining why the format is worth testing for this specific brand. Not a generic case. Name the gap it fills in the current mix, the creative lever it pulls that the current mix does not, and the audience or awareness stage it unlocks. Rank the recommendations by conviction about fit for this brand, strongest first, with the conviction call explicit.

## Required sources

- The full 90-day paid creative set with format classification, spend, and performance metrics per ad.
- The inspo brand library for this brand.
- The affinity brand library for this brand.
- The competitor ad library for this brand.
- Brand context doc, persona slugs, intended audience, product lineup.
- Brand-memory and user-memory.
- The prior quarter's diversity audit.

Where any source is unavailable, name the blank and mark the affected read data-limited. A thin inspo library is a specific constraint worth flagging — recommendations narrow to what the available libraries surface.

## Tools Parker calls for this run

Parker pulls the brand's own ninety-day format mix through search_facebook_ads_sql, then reaches the inspo, affinity, and competitor libraries through search_competitor_facebook_ads to supply the recommended formats to test. For context and memory, Parker loads brand context with get_brand_persona, reads the prior quarter's audit through search_chat_history, and persists the result with parkerFileSystem and update_custom_working_memory.

## Output spec

Open with frontmatter, then the three sections in fixed order. Lead with the executive summary; write it last, place it first. Mark every claim stated, inferred, or verified.

```markdown
---
brand: [brand-slug]
doc: 90-day-diversity-audit
quarter: YYYY-Qn
generated_on: YYYY-MM-DD
date_range: YYYY-MM-DD to YYYY-MM-DD
data_sources_read: [live ads manager, inspo library, affinity library, competitor library, prior-quarter audit, brand-memory, user-memory — as applicable]
formats_active_this_quarter: []
formats_dropped_since_prior_quarter: []
formats_new_this_quarter: []
data_limitations: []
---

# 90-day creative diversity audit (format) — [Brand Name] — YYYY-Qn

## Executive summary

## Current ad formats used

## Recommended ad formats to test

## Open loops

## Appendix - Parker media links
```

## Parker media links appendix

End every audit with `## Appendix - Parker media links` as the final appendix, after open loops and after any quote, customer-language, source, or evidence appendix. Make this appendix an indexed media library, not a loose link dump. Give every source artifact a stable index ID in the form `M001`, `M002`, `M003`, continuing in order through the appendix. Include the source name or ad name, the Parker dashboard link when available, the original media link or media file path, the thumbnail path when available, the video URL when available, the ad-library link when available, and the short label for where the artifact was discussed in the audit. Preserve every original link or path exactly. If the body of the audit discusses a specific ad, post, hook, creator example, competitor example, or visual source, that source should have an index entry at the bottom so a strategist can reopen it without searching. If no Parker media links or media references were available, write `No Parker media links were available in this run.` Do not invent links, shorten paths, or replace links with descriptions.

This appendix is source infrastructure, not analysis. Do not move open loops into it, and do not count the appendix as a recommendation section. The body of the audit still needs narrative reconstruction of every important visual source; the appendix simply keeps the media handles attached at the bottom.

## Common mistakes to avoid

- Treating dominant formats as the only ones that matter. Small slivers of the distribution often carry the most interesting signal. A format at 4 percent share climbing fast is worth more attention than a 35 percent share that has plateaued.
- Describing format performance without explaining what the format is doing for the brand. "Talking-head UGC is at 31 percent share and 1.4 ROAS" is restatement. "Talking-head UGC is doing the brand's product-aware acquisition work — every top-spend ad in this format is targeting solution-aware buyers and converting at 1.4 ROAS, which is the best segment performance in the account" is interpretation.
- Recommending formats without anchoring to a real source ad. Every recommendation in section three carries a concrete example from the inspo, affinity, or competitor library, described vividly. A generic recommendation is a guess.
- Generic reasoning on recommendations. "This format would work because it is popular" is generic. The reasoning has to be specific to this brand — what gap it fills, what lever it pulls, what audience or stage it unlocks.
- Padding section two with formats the account is not actually running. If the brand has zero static ads, do not write a section about static ad performance. The format coverage in section two is what the account is actually doing.
- Reading format share without checking spend share. Count and spend rarely match. The gap is the finding.
- Producing a snapshot instead of a trajectory. Every format read is against the prior quarter.
- Treating recommendations as a list. They are ranked by conviction. Name the conviction call for each one.

## Open loops

In open loops, write the few consequential questions the audit could not resolve. The Parker media links appendix follows open loops as the final section.

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

Doc-specific thinking lens. Loops on this audit cluster around format absences where the question is whether the absence is a constraint, a failure, or an unclaimed lane; and around the brand's own creative-range posture where the diversity question points at a positioning question.

Loops do not cover: format tagging gaps or library connectivity issues. Those belong in the frontmatter's data_limitations field.

Mark any loop only the brand can answer so it routes to the brand.

## When you refresh this

Re-run quarterly. Take the prior audit in as context first. Carry forward the format distribution, update the trajectory on each format, refresh the per-format analysis, and rebuild the recommendation slate against the current state of the inspo and affinity libraries. Note which recommendations from prior quarter were tested and what the outcome was. Note which open loops are resolved.
