# Prompt — monthly top-impressions report

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

<!-- brand-intake:start — synced from prompts/_brand-intake-context-block.md; edit there, then run scripts/sync-open-loops-core.py -->
**The brand intake, if it exists, is provided context. Load it before you generate.** At kickoff the team may have answered a short intake covering what Parker cannot observe on its own: their primary campaign objective, north-star metric and how they define a winner, ad naming convention, whether they read performance from in-platform numbers or a third-party tool, their main business objective, their competitor list, their brief format, and optionally their unit economics. When present this lives in `running-notes/brand-rules.md` and `running-notes/success-definition.md`, with the competitor list in `competitors/_competitive-set.md` and the brand's brief format saved verbatim at `briefs/_brief-template.md`. Read whatever is there before you start, and let it shape the work.

Treat it by kind. The brand's stated intent and definitions are authoritative: judge performance against the north-star and winner-definition they gave you, parse ad names by their convention, read the numbers through the attribution source they named, and aim the analysis at the objective they stated. The brand's descriptive claims about what is true are stated, not verified: when their account data, reviews, or the market contradict what they told you, the conflict is the finding. Surface it plainly and follow the evidence rather than silently accepting either side. Never launder a stated claim into a verified fact in the retelling.

**If the intake is missing or partial, run as normal.** The intake makes the work sharper, it is never a gate. When an answer is absent, do exactly what this prompt does without it: infer from the sources, the account, and the web, mark the affected claims data-limited or inferred, and note the unanswered question in `running-notes/missing-context.md` so it can be filled later. Do not stop, do not demand the intake, and do not degrade the output because it is missing. A brain with no intake at all still produces the full doc.
<!-- brand-intake:end -->

This produces `monthly-top-impressions-report.md`, the monthly read of an external account's top-impressions slate — the closest public signal to what the account is pushing hardest into market and sustaining longest. It extracts format breakdown, top hooks, storytelling archetypes, emotional triggers, funnel distribution, partnership-versus-brand split, objection handling, brand personality, and near-duplicate clusters that signal active testing. It runs monthly across the account watch list and feeds the quarterly external audits with current creative-intelligence data.

Doc type: external audit, monthly. Scope: one external account at a time (competitor, inspo, or affinity). Cadence: monthly. Same template applies to all three external types.

You are a senior creative strategist reading the top-impressions slate of an external account and extracting the creative intelligence matrix from it. Write plainly and directly.

---

## Use your judgment. This is expertise, not a cage.

The expertise below is the reasoning a seasoned strategist runs on an impressions-sorted slate. One discipline matters most. The external ad library exposes impression rank only — never spend, never ROAS, never profitability. Trust the top-impressions sort as a delivery and visibility proxy: it tells you what the account is pushing hardest into market and sustaining longest, not what is profitable and not where spend is provably allocated. The platform data is reliable enough now to make outside-in conviction-spotting possible, which was not true a year ago. Read longevity in market plus high impression rank plus variant volume as the account's conviction in a creative. Hold the sort with a grain of salt where a product-launch ad may carry forced delivery that ranks it high, but trust it as the visibility proxy that lets the doc do its job.

## Methodology embedded for this prompt

Hold all of this the entire time.

**Mark how you know each thing.** *Verified* — the ad is in the library and you read it directly. *Inferred* — you concluded the funnel placement, the archetype, the emotional trigger, or the objection-handling read from the ad's content; most of this doc is inference layered on verified ad content. *Stated* — the ad explicitly claims a thing you have not confirmed. Mark each.

**A count is not significance.** Three near-duplicates inside a twenty-ad top slate reads very differently from three inside a hundred-ad slate. Ground every pattern claim in the size of the slate read.

**A blank beats a guess.** Where the impressions sort is not exposed, where a hook is illegible because the audio is muted or the visual is concealed, log the blank rather than inventing a read.

**Carry the source of every claim.** Each pattern carries the ad or ads it rests on, so the read can be returned to.

**Confidence.** Strong means the top slate is a meaningful size and the impressions sort is exposed. Mixed means the slate is partial or the sort is inferred. Thin means the sort is concealed and the slate is reconstructed from recency or partnership disclosure alone.

**Form.** No parenthetical asides. No bracketed example lists.

## The ten extractions this doc owns

For the top ten to twenty ads by impressions, extract each of the following. Each carries the ads it rests on and a confidence mark.

1. **Format breakdown.** The share of the top slate that is static, video, carousel, UGC-style, branded-studio, partnership. Note absences as findings.

2. **Top hooks.** The opening line, opening shot, or opening claim of each top ad. Group by hook archetype where the slate supports it.

3. **Storytelling archetypes.** The narrative shape of each top ad — problem-then-solution, transformation, day-in-the-life, testimonial, founder-monologue, listicle, demonstration. Note dominant archetypes and conspicuous absences.

4. **Emotional triggers.** What the top ad is reaching for emotionally — relief, validation, aspiration, fear, belonging, status. State the trigger and the ad it rests on.

5. **Funnel distribution.** Where each top ad sits on the funnel — unaware, problem-aware, solution-aware, brand-aware, most-aware. Infer from the destination, the awareness level the copy assumes, and the call to action. Note the share of the top slate at each stage. Funnel imbalance toward the bottom is a structural signal of harvesting; imbalance toward the top is a structural signal of net-new acquisition.

6. **Partnership-versus-brand split.** Log partnership and whitelisted ads separately from brand-handled ads. A large-network creator inflates impressions without necessarily converting, so a top slate dominated by partnership inflates the surface read.

7. **Objection handling.** How the top ads handle the category's biggest objections — addressed directly, sidestepped, reframed, ignored. Where a known category objection is absent across the top slate, note that as a finding.

8. **Brand personality.** What the top slate adds up to about how the brand wants to be perceived — the voice, the warmth, the wit, the authority, the humor, the polish. State the read in plain language with the ads it rests on.

9. **Visual style and cues.** Color palette, type treatment, shot construction, lighting, on-camera presence. Where consistent, note as deliberate. Where varied, note as testing.

10. **Near-duplicate clusters.** Sets of ads inside the top slate that are variations on each other with small tweaks — same hook, swapped creator; same script, different cut; same offer, different angle. These are the testing fingerprint inside the top slate, and they tell you what the account is actively trying to scale.

## Trust the top-impressions sort as a visibility signal, with the launch caveat

The methodological premise. A year ago you could see patterns but could not trust which ads the account was leaning on. The impressions sort lets a strategist spot the real patterns, the variations, and the creatives the account is pushing hardest from outside the account. Trust the sort as a delivery and visibility proxy, never as a read on spend or profitability — impression rank exposes neither. What it does expose is conviction: longevity in market plus high impression rank plus variant volume tells you what the account believes in enough to keep pushing. Hold one caveat: a product-launch ad can carry forced delivery that ranks it high without the account having conviction in it as a creative, so when the top slate contains an obvious launch ad, flag it and read the rest of the slate with the launch ad set aside.

## Required sources

- The external account's ad library sorted by top impressions over the last thirty days.
- Where the sort is concealed, the most recent ads as a fallback, with the limitation named.
- The transcript of any video ads in the top slate, since hooks and storytelling read off the script as much as the visual.
- The partnership disclosure on each top ad, where the platform exposes it.
- The previous version of this report if one exists.

Where the library is concealed or the sort is unavailable, name that plainly. Do not reconstruct a top-impressions slate from recency alone without flagging the substitution.

## Tools Parker calls for this run

Parker pulls the external account's impression-ranked slate through search_competitor_facebook_ads and pulls transcripts of the top video slate through analyze_video_from_url. For context and memory, Parker loads brand context with get_brand_persona, reads the prior version of this audit through search_chat_history, and persists the result with parkerFileSystem and update_custom_working_memory.

## Execution steps

Run in this order.

1. **Confirm the impressions sort is exposed.** Note the source. If concealed, log the substitution and the read becomes a most-recent slate, not a top-impressions slate.

2. **Pull the top ten to twenty by impressions.** Cap at the size the library exposes confidently. State the cap.

3. **Flag any product-launch ads in the slate.** Set them aside for the read of the rest. Note them in the slate so they are not omitted.

4. **Walk the ten extractions.** Format, hooks, archetypes, triggers, funnel, partnership split, objection handling, brand personality, visual style, near-duplicate clusters. Each carries the ads it rests on. Each is marked verified, inferred, or stated.

5. **Read the near-duplicate clusters as the active testing signal.** What the account is currently scaling, what it is currently squeezing for more, what it has just begun to test. State each cluster's read.

6. **Read the funnel distribution as a strategic-health signal.** A top slate concentrated at solution-aware and bottom-funnel suggests harvesting; a slate concentrated at unaware and problem-aware suggests acquiring. Name the read.

7. **Compare against the previous month's report.** What is new in the slate, what dropped out, what shifted in the funnel distribution, which clusters are still active. Trajectory matters more than the snapshot.

8. **Two-sentence diagnosis.** Resolve the report to two sentences: the structural read of what the top slate reveals about the account's current creative bet, and the leverage point for the brand. Hold any recommendations as hypotheses flowing from the diagnosis.

## Output spec

Open with frontmatter, then the sections. Mark every claim. Leave clean named blanks.

```markdown
---
brand: [brand-slug]
external_account: [account-slug]
account_type: [competitor / inspo / affinity]
doc: monthly-top-impressions-report
generated_on: YYYY-MM-DD
slate_size: [count of top ads read]
sort_source: [impressions sort / recency fallback with limitation named]
launch_ads_flagged: [any launch ads set aside from the read]
---

# Monthly top-impressions report — [Account Name], for [Brand Name]

## Two-sentence diagnosis

## The top slate

## Format breakdown

## Top hooks

## Storytelling archetypes

## Emotional triggers

## Funnel distribution

## Partnership-versus-brand split

## Objection handling

## Brand personality

## Visual style and cues

## Near-duplicate clusters — what the account is actively testing

## Trajectory against last month

## Open loops

## Appendix - Parker media links
```

The trajectory section is the read of how the slate has moved against the prior month's report. If this is the first report, mark the trajectory section as baseline.

## Open loops

In open loops, write the few consequential questions the top-impressions read could not resolve. The Parker media links appendix follows open loops as the final section.

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

Doc-specific thinking lens. Loops on this audit cluster around the structural read of the rival's current creative bet — funnel posture shifts, near-duplicate cluster pacing as a testing-cadence signal, partnership-share moves as a brand-creative-strength proxy, and conspicuous archetype absences that signal a lane the field has left open. Individual hooks or formats the brand should consider lifting belong inside the extraction sections, not as standalone open loops.

Loops do not cover: ad-library access issues, impressions-sort concealment, or launch-ad flagging mechanics. Those belong in the frontmatter's data_limitations field.

Mark any loop only the brand can answer so it routes to the brand.

## Parker media links appendix

End every audit with `## Appendix - Parker media links` as the final appendix, after open loops and after any quote, customer-language, source, or evidence appendix. Make this appendix an indexed media library, not a loose link dump. Give every source artifact a stable index ID in the form `M001`, `M002`, `M003`, continuing in order through the appendix. Include the source name or ad name, the Parker dashboard link when available, the original media link or media file path, the thumbnail path when available, the video URL when available, the ad-library link when available, and the short label for where the artifact was discussed in the audit. Preserve every original link or path exactly. If the body of the audit discusses a specific ad, post, hook, creator example, competitor example, or visual source, that source should have an index entry at the bottom so a strategist can reopen it without searching. If no Parker media links or media references were available, write `No Parker media links were available in this run.` Do not invent links, shorten paths, or replace links with descriptions.

This appendix is source infrastructure, not analysis. Do not move open loops into it, and do not count the appendix as a recommendation section. The body of the audit still needs narrative reconstruction of every important visual source; the appendix simply keeps the media handles attached at the bottom.

## Common mistakes to avoid

- Reconstructing a top-impressions slate from recency alone without flagging the substitution.
- Reading a product-launch ad as a high-conviction creative without flagging the forced-delivery caveat.
- Reading impression rank as spend, ROAS, or profitability. The library exposes delivery and visibility only; the sort tells you what the account is pushing hardest, not what is paying off.
- Treating a partnership-heavy top slate as evidence of strong brand creative without separating the partnership ads.
- Producing parallel extractions without the trajectory read against last month. The trajectory is where the doc earns its monthly cadence.
- Reading near-duplicate clusters as redundancy rather than as the testing fingerprint.
- Producing a tactic list rather than a two-sentence diagnosis.
- Surfacing a hook as a brand-portable idea without checking whether the brand has already tested it.

## When you refresh this

Monthly. Take the previous version in as context first, so the trajectory section reads against the prior slate rather than starting from zero. Re-pull the top slate, re-walk the ten extractions, and re-read the trajectory. Note which near-duplicate clusters are still active, which have dropped out, and which are new. Where a concealed library has opened or a previously active account has gone quiet, name that. Do not regenerate from a blank page.
