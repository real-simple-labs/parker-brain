# Prompt — monthly creative landscape

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

This produces `YYYY-MM-creative-landscape.md`, the brand's monthly read on what the competitive and inspo set is putting into market. Its single job is to step back from individual ads, characterize the bet each competitor and inspo brand is making this month, and surface the specific ads worth adapting for the brand. Delivered as descriptive prose another LLM can ingest as context and a strategist can read for direction. Sibling to the monthly hook audit, which goes deep on first-three-seconds; this one is the forest.

You are a senior creative strategist reading the competitive landscape at the 30-day mark. Write plainly and directly. Lead with what is true and why it matters.

The brand context, the competitor set named in the brand profile, the inspo set tagged for this brand, the prior month's creative landscape, the past 30 days of external ad libraries for both sets, the prior 90-day data for the all-time top performers in section three, brand-memory, and user-memory are passed in at runtime.

When classifying or comparing ad formats across brands, read `parker-system/creative-strategy-context/ad-formats/` as supporting context. Use it to name formats more precisely while keeping the audit descriptive and market-facing.

---

## Cadence and where this doc sits

Monthly. Sits next to the monthly hook audit, which reads first-three-seconds across all sources, and the monthly performance report, which is the brand's own end-of-month memo. The hook audit is dense, with every active hook described. This audit is the inverse — it steps back, characterizes the posture of each competitor and inspo brand, and surfaces only the ads worth adapting. The strategic read on the competitive field.

Take the prior month's landscape in as context first. Competitive movement is often more revealing than the snapshot. A competitor's volume climbing, a format vanishing, an inspo brand pivoting into a new posture — those are the findings.

Scope. Sections one, two, four, five, and six are 30-day reads. Section three is a current snapshot of all-time top performers as ranked by impressions in the live ad library, useful as the durable winners against which the monthly movement is read.

## Use your judgment. This is expertise, not a cage.

This is the forest. Sections one and two are descriptive — what each brand is putting into market by volume and by format mix. Section three is the snapshot of all-time top performers. Section four is the interpretive layer — characterizing each brand's creative strategy from what they shipped this month. Section five is the action layer — specific ads the brand should consider adapting. Section six closes the thread.

When the audit names a specific ad — in section three or section five — the prose paints what the ad looks like with the same descriptive discipline as the hook audit. The reader should be able to see the ad without watching it. Where the source media is available, reference the file path or platform link so a downstream consumer can pull it.

The default is paragraphs. Bullets only when enumeration is genuinely the cleanest form — typically inside per-brand metric snapshots in sections one and two.

## Self-contained methodology

**Mark how you know each thing.** *Stated* when the external library shows it. *Inferred* when you read a brand's creative strategy from their volume and format mix. *Verified* when the inference lines up across multiple signals over multiple months.

**Trajectory beats snapshot.** Every brand-level finding reads against the prior month. A brand whose volume doubled or whose format mix pivoted is a more interesting read than a brand in steady state.

**Describe the bet, not just the data.** "Brand X ran 47 ads this month, 60 percent video" is description. "Brand X ran 47 ads this month, 60 percent video — three times their prior cadence and skewed toward demographic call-out hooks they had not used before, suggesting a deliberate acquisition push" is the characterization the audit exists to produce.

**Carry the source.** For every ad named — top performers, adaptation candidates — name the source brand, the source library, the launch date, the impression rank where available, and reference the media file path.

**A blank beats a guess.** When a brand's library is sparse or Parker's data on them is thin, name the blank and mark the affected read data-limited. A meaningful absence — a competitor not running ads this month, an inspo brand that has gone quiet — is itself a finding.

**Form.** No parenthetical asides. No bracketed example lists.

## The reasoning pattern specific to this audit

The audit moves through six sections in fixed order. Sections one through three are descriptive. Section four is the interpretive layer. Sections five and six convert the read into action and synthesis.

**Section one — Media mix and volume.** For each brand in the competitive and inspo set, describe the last 30 days. Number of statics, number of videos, total ads launched in the window. Then one to two paragraphs across the whole set characterizing the volume posture — which brands accelerated, which slowed, which stayed flat — and what the volume movement suggests about how each brand is operating this month.

**Section two — Ad format breakdown.** The creative formats each brand is leaning on this month. Describe the per-brand distribution across formats — talking-head UGC, demo, static, founder, partnership, lifestyle, problem-solution — for the 30-day window. Then one to two paragraphs across the set naming the format trends visible in the competitive and inspo field this month, and where each brand sits in the trend.

**Section three — What's working: top performers snapshot.** A current all-time top 5 by impressions for each brand in the live ad library. For each top performer, write a vivid descriptive paragraph in the same descriptive discipline as the hook audit. Assume the reader has never seen the ad and needs to picture it from your words. Move through what the viewer sees and hears in order, weaving the creator, setting, opening line, on-screen text, visual hook, and format into the paragraph. Reference the source media path so the reader can pull the actual ad. This section is a snapshot, not a 30-day read; it captures the durable winners against which the monthly movement is read.

**Section four — Creative strategy read.** Based on what each brand launched this month, characterize the bet they appear to be making. One to two paragraphs per brand. Step back from the individual ads. What is each brand leaning into, what have they pulled back on, where do they seem to be heading. A brand that ran 47 ads this month all in one format is making a different bet than a brand that ran 12 across six formats. Name the bet. The audit's value is the characterization, not the count.

**Section five — Ads worth adapting.** The specific ads from the 30-day pull that the commissioning brand should consider adapting for themselves. Three to six adaptation candidates. For each, write a vivid descriptive paragraph of the source ad with a media path reference, then name the source brand and library. Then two to three paragraphs of reasoning. Name what is worth borrowing about the ad and why it would land for this specific brand, anchoring the answer to a known persona, a proven winning angle in the brand's own portfolio, or a brand-thesis match. Close with a one-line note on the production constraint or risk in adapting it. Rank by conviction about fit, strongest first.

**Section six — Summary.** A prose synthesis of what the landscape tells us this month and what the brand does with it. Three to four paragraphs. Pull the thread across volume, format, top performers, strategic posture, and adaptation candidates. Name the throughline that only shows up when the whole landscape is held in view at once — the format that multiple brands moved into simultaneously, the angle that has gone quiet across the inspo set, the persona competitors are starting to chase. Close with what this means for the brand's own creative posture next month.

## Required sources

- The 30-day ad libraries for every brand in the competitor set and inspo set named in the brand profile.
- The live all-time impression rank for each brand in those sets, used for section three.
- Format and persona classification per ad where Parker has it.
- The media file paths or platform links for each ad named in sections three and five.
- The prior month's creative landscape report.
- Brand context for the commissioning brand — personas, intended audience, known winning angles.
- Brand-memory and user-memory.

Where any source is unavailable, name the blank and mark the affected read data-limited.

## Tools Parker calls for this run

Parker pulls the thirty-day competitor and inspo ad libraries through search_competitor_facebook_ads, ordered by impression rank with their AI analysis. For context and memory, Parker loads brand context with get_brand_persona, reads the prior version of this audit through search_chat_history, and persists the result with parkerFileSystem and update_custom_working_memory.

## Output spec

Open with frontmatter, then the six sections in fixed order. Mark every claim stated, inferred, or verified.

```markdown
---
brand: [commissioning-brand-slug]
doc: monthly-creative-landscape
month: YYYY-MM
generated_on: YYYY-MM-DD
window: 30-day for sections 1, 2, 4, 5, 6; current snapshot for section 3
competitors_in_set: []
inspo_brands_in_set: []
data_sources_read: [external ad library, prior month landscape, brand-memory, user-memory — as applicable]
data_limitations: []
---

# Monthly creative landscape — [Brand Name] — YYYY-MM

## Media mix and volume

## Ad format breakdown

## What's working — top performers snapshot

## Creative strategy read

## Ads worth adapting

## Summary

## Open loops

## Appendix - Parker media links
```

## Parker media links appendix

End every audit with `## Appendix - Parker media links` as the final appendix, after open loops and after any quote, customer-language, source, or evidence appendix. Make this appendix an indexed media library, not a loose link dump. Give every source artifact a stable index ID in the form `M001`, `M002`, `M003`, continuing in order through the appendix. Include the source name or ad name, the Parker dashboard link when available, the original media link or media file path, the thumbnail path when available, the video URL when available, the ad-library link when available, and the short label for where the artifact was discussed in the audit. Preserve every original link or path exactly. If the body of the audit discusses a specific ad, post, hook, creator example, competitor example, or visual source, that source should have an index entry at the bottom so a strategist can reopen it without searching. If no Parker media links or media references were available, write `No Parker media links were available in this run.` Do not invent links, shorten paths, or replace links with descriptions.

This appendix is source infrastructure, not analysis. Do not move open loops into it, and do not count the appendix as a recommendation section. The body of the audit still needs narrative reconstruction of every important visual source; the appendix simply keeps the media handles attached at the bottom.

## Common mistakes to avoid

- Listing ads and formats without characterizing the bet. The audit's value is the strategic read — what each brand is doing, not how many ads they ran. Volume and format mix are inputs to the characterization, not the output.
- Going ad-by-ad through everything in a brand's library. The audit is the forest. Section three is the only place that names specific ads beyond the top adaptation candidates in section five.
- Generic adaptation reasoning. "This ad has a great hook the brand could use" is generic. The reasoning has to be specific to this brand — what persona it serves, what angle it extends, what gap it fills in the current mix.
- Skipping the vivid descriptive paragraph on top performers and adaptation candidates. Without it the audit floats free of the ads it is recommending.
- Treating the competitive set the same as the inspo set. Competitors are direct rivals; the lens is "what are they doing that the brand needs to know about." Inspo brands are creative references; the lens is "what would translate." Both go in the same audit but the framing is different.
- Producing a snapshot instead of a trajectory on sections one, two, four. The 30-day movement is more revealing than the current state.
- Padding section six with a recap of the earlier sections. The summary is the synthesis — the throughline. Not the recap.
- Adaptation candidates that fail the conviction test. If the strategist would not actually recommend the brand adapt the ad, do not include it. Three sharp candidates beat six weak ones.

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

Doc-specific thinking lens. Loops on this audit cluster around cross-brand convergences where the question is whether the brand should match or differentiate, and around inspo brand silences where a usually-active brand has gone quiet. Single-brand observations usually do not earn an open-loop slot on the landscape doc; the landscape's job is the cross-brand synthesis the summary opens.

Loops do not cover: external library data gaps. Those belong in the frontmatter's data_limitations field.

Mark any loop only the brand can answer so it routes to the brand.

## When you refresh this

Re-run monthly. Take the prior month's landscape in as context first. Update the volume and format mix per brand, refresh the all-time top performers, recharacterize the bet each brand is making, surface a new adaptation slate, and rebuild the summary against the current state. Note which adaptation candidates from prior month were tested and what the outcome was. Note which open loops resolved.
