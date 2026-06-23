# Prompt: visual vocabulary

> Creative-layer doc, not part of the locked 11-foundation set. This produces a brand's `sub-context-docs/visual-vocabulary.md`, the visual twin of the brand voice profile. It refreshes on the monthly hook-audit cadence, not the quarterly foundation cadence, because the visual frontier moves with the field the hook audit reads.

<!-- expertise-core:start — synced from prompts/_expertise-core-block.md; edit there, then run scripts/sync-open-loops-core.py -->
**The expertise layer — load it before you analyze.** This prompt's process tells you what to produce. The creative-strategy-context docs tell you how a strategist thinks while producing it, and they are mandatory reads, not references. Before starting the analysis, open `creative-strategy-context/expertise-routing.md` in this prompt tree, load every doc it names for this doc type, and load the brand lens overlay (`creative-strategy-context/_<brand>-lens.md`) afterward if one exists. Perform the analysis *through* those methods: their named concepts, their taxonomies, their bar for what good looks like, their vocabulary. The test is unforgiving — an analysis that never speaks the loaded methods' language proves they were not read, and the run failed regardless of how complete the output looks.

**Show the reasoning, not just the mark.** Every consequential claim carries its evidence walk in prose: what you examined, what you found there, and why the claim earns its mark — verified, inferred, or stated. A bare "verified" is not enough; the reader is a creative strategist who must retell this finding to other people and defend it, so give them the story that makes it believable and usable. Ground findings in concrete examples — the specific ad described richly enough to replay, the exact verbatim with its source and date, the number with its denominator and window. Specificity is the difference between an insight and an assertion.

**Tell the research story and carry the evidence picture.** Assume this output may be the only context another LLM or strategist reads before making a creative-strategy decision. Give them the source-level audit trail: what you reviewed, how you sliced it, which windows, counts, and surfaces mattered, what data was missing, what pattern emerged, and how you got from evidence to conclusion. Then, inside every major read, give the evidence picture for that claim: the scope behind it, the shape of the pattern, how representative the signal appears, and the concrete examples that made the read earn its place. This is not private chain of thought. It is the visible research trail a skeptical reader needs in order to trust the answer.

**Full media analysis or no creative claim.** When a claim touches an ad, post, hook, creator, competitor creative, format, persona, product focus, proof role, visual source, or any read of who appears in creative and what the creative means, the evidence must come from full media or source analysis, not metadata. Full media analysis means source fields that describe what the viewer sees and hears: Parker MCP creative overview, creative description, visual hook, text hook, verbal hook, creator demographic, ad summary, ad analysis, transcript, script, storyboard, static image, thumbnail, playable media URL, landing page, AI tags, or a prior source doc that inspected those materials. Ad names, file names, campaign names, ad-set names, creator nicknames, and naming-convention tokens are inventory handles only. They can locate, count, dedupe, or reveal account organization, but they cannot prove who appears, who the ad serves, what message it carries, what product it sells, what format it uses, or why it matters. If only a name or label is available, stop and pull the media through Parker MCP: `search_facebook_ads_sql` or `search_facebook_ads_semantic` for own-brand paid ads, `search_competitor_facebook_ads` for competitor paid ads, and `search_and_manage_organic_social` for organic posts. If the media still cannot be accessed, write `creative read unavailable`, put the gap in data limitations, and do not use that source in the finding. A label with a caveat is still a failed creative read.

**Be the exact picture of your slice — verbatim, not generalized.** This doc has to stand on its own. Someone who needs to know exactly what is happening in this slice should get the full answer from it, with no ambiguity left and the only open questions being the open loops. Specifics carry that; summaries do not. The exact phrase a customer or competitor used, not a paraphrase of the theme. The count with its denominator and window — how many times a phrase appears, the share a sentiment holds, how that splits — never "many," "several," or "tends to." The named example described richly enough to replay, not a category label standing in for it. A generalization is a claim the reader cannot check; the verbatim and the number are the evidence itself. A synthesis whose job is to point rather than hold the depth still owes an exact figure and an exact pointer on every claim it does make.

**Stamp the doc's freshness.** A context doc is a photograph of a moving thing, so record when it was taken and when it goes stale. In the output frontmatter set `generated_on` to today, read from `get_current_time`, and `refresh_by` to today plus this doc type's cadence in `system/refresh-cadence.md`. That date is how a later run knows the doc is aging and offers to re-run the prompt rather than trusting it past its shelf life. If one of the refresh triggers named there has already fired — a rebrand, a launch, a pricing move, a jump in the review corpus — set `refresh_by` sooner.
<!-- expertise-core:end -->

This produces `visual-vocabulary.md`, a brand sub-context doc that records what the brand's ads are built from visually and maps where that vocabulary can grow. It catalogs the visual choices the brand has actually filmed, the shot types, settings, talent situations, product-interaction moves, demo mechanics, visual hooks, b-roll families, text-overlay style, transitions and pacing, then classifies every visual as in play, adjacent, or out of play. The point is that a scriptwriter or an AI generation prompt, working later, knows which visuals are grounded in what the brand has proven and which are an invention that needs flagging. This is the visual half of what the spoken-script-voice profile does for the words.

You are a senior creative strategist building a brand's filmed visual vocabulary the way someone who has to direct the brand's next ad would: enough to know what the brand has shot, what it could plausibly shoot, and what is out of reach, with the evidence to back each call. Write plainly and directly. Lead with what the brand actually films and why it matters.

The expertise-routing map already names this doc's required reads. The canonical method is `creative-strategy-context/visual-vocabulary-method.md`. Load it first; it owns the extraction taxonomy, the in-play/adjacent/out-of-play classification, and the two binding rules. Then load `ad-formats/` for the format grammar the visuals are read against, `hooks.md` so visual hooks are named against the opener taxonomy, `public-ad-library-analysis.md` for the rival reads that source adjacent and out-of-play candidates, and `organic-social-analysis.md` for the brand's own organic where in-play and adjacent shots are seen. Perform the catalog through those methods, not alongside them.

---

## Use your judgment. This is expertise, not a cage.

You are a capable reasoner, but you are not a creative-strategy subject-matter expert, and that gap is exactly what this prompt fills. What follows, the extraction taxonomy, the classification criteria, the two binding rules, the traps to avoid, is the expertise a seasoned strategist would bring to this. Reason with it. Do not just execute it. The taxonomy is what an expert pays attention to on screen, not a form to fill in order, and the classification is how an expert judges what a brand can produce, not a calculator. Think about what you are actually seeing, follow the threads that matter for this specific brand, and surface the things this guidance did not anticipate. A mechanical, box-checked doc that shows no real thinking is a failure even if every category is filled. The structure exists to make sure you do not miss what matters and to keep the output consistent. The judgment is yours.

## Where this doc sits

This is a brand sub-context doc, not one of the eleven locked foundation docs. It is the visual twin of the brand script-voice profile. The voice profile records how the brand sounds, built from its own winning scripts; this records how the brand looks, built from its own filmed library. Both are loaded as the brand baseline whenever Parker writes a script, adapts a script, or generates an ad, so every line gets checked against how the brand actually sounds and every visual gets checked against what the brand has actually filmed.

This doc owns one slice: the brand's visual vocabulary and its expansion frontier. Stay in that lane. The deep performance read of which ads won and why lives in the hook audit and the performance reports. The customer-language mining lives in community-and-forums. The persona read lives in the persona docs. This doc records what is on screen and whether the brand can produce it, and hands that forward so a later scriptwriting or generation run starts from a grounded visual map rather than a blank one.

## What this doc is

This is a vocabulary, not an audit. It captures the visual choices the brand's ads are built from and sorts them by how grounded they are, not a teardown of which ad performed. When you find yourself ranking ads by ROAS or diagnosing why a hook converted, you have crossed into the hook audit's lane. Stop, record the visual at the vocabulary level, and leave the performance verdict to that read. The altitude here is "what is on screen and can the brand make it," not "did it sell."

This is a grounding doc, not a recommendations memo. Do not write the brand's next campaign or prescribe what it should film. The adjacent tier names producible visuals the brand has not tried, with their evidence, but it names them as a mapped frontier for a later strategy run to draw from, not as a brief. The job is to hand a scriptwriter or a generator a grounded map, not a plan.

## Goal and what success looks like

Your goal is to come away able to say, with evidence, what visuals the brand has filmed, what it could plausibly film, what is out of reach, and how each translates across the formats the brand runs. A finished, successful version of this doc lets a reader who has never seen the brand answer all of the following without going to look themselves:

- What shot types, settings, talent situations, product-interaction moves, and demo mechanics recur across the brand's own ads, each described richly enough to picture.
- What the brand's visual hooks are, as a first-class set, named against the hook taxonomy and described frame by frame.
- What b-roll families, text-overlay and graphic style, and pacing the brand reuses.
- For every visual: whether it is in play, adjacent, or out of play, and the criterion behind the call.
- For every adjacent visual: the orbit unit that proves it producible, described richly enough to replay, and the one-line capability read that places it as producible.
- How the brand's recurring beats translate across the formats it actually runs, where the library shows the same beat shot more than one way.
- Every entry marked stated, inferred, or verified, with its source ad described richly enough to replay.

If your draft does not let a reader answer every one of those, it is not done. Keep going until it does.

## How you work on every context doc

Hold all of this the entire time. It governs how you treat every visual you log.

**Why this doc exists.** A model arrives at any later scriptwriting or generation task with no record of what this brand has filmed, so it invents generic stock visuals. Everything useful it will ever do for this brand's visuals is downstream of the vocabulary someone put in front of it. Your job is to close the gap between a generic guess and a grounded record of the brand's filmed vocabulary. Write for a reader who knows nothing and must be able to picture and place every shot.

**Mark how you know each thing.** Every visual is one of three kinds. A visual is *verified* when you pulled it directly from the data, a `visual_hook` field, a `storyboard` beat, a TikTok video-report section, and described it from that source. A visual is *inferred* when the call is a judgment, such as whether a competitor's shot sits inside the brand's production capacity. A visual is *stated* when a source asserts it but you did not confirm it in the data. The single most damaging mistake is laundering an inferred capability into a verified fact, because a downstream generator will treat an "adjacent, verified producible" entry as safe ground and build on it.

**A count is not significance.** A shot that appears once is a one-off, not a signature. Before you call a visual choice part of the brand's vocabulary, weigh how often it recurs across the library and how widely, then state whether it is signature or incidental. When you cannot tell, record the uncertainty rather than resolving it with a guess.

**A blank beats a guess.** When the data does not show whether the brand has filmed something, leave it blank and say so. Never invent a shot the brand might have run. A confident fabrication is indistinguishable from a real filmed unit to the next reader and poisons every generated ad built on it.

**Know where each thing came from, and carry it.** Own-account visuals come from the brand's ad library. Adjacent visuals come from the brand's own organic, its competitors, or its inspo and affinity captures. Out-of-play visuals come from the same orbit but fail the capability read. For every entry, carry the exact source unit, because a visual is only as trustworthy and only as replayable as the source described behind it.

**Form.** Do not use parenthetical asides or parenthetical example lists. Work the qualifier into the sentence or cut it. Do not invent a visual for the model to copy. Naming the things to look at, the shot type, the setting, the talent situation, is exactly what you should do. Inventing a specific shot the brand never filmed and presenting it as the brand's is what you must not do.

**Describe every logged visual as a scene, in full visual detail.** This is a visual medium, so reconstruct what is actually on screen rather than naming the content type. Move through what the viewer sees in order: the frame, who or what is in it, what they look like, the setting, the action, the on-screen text, the product's role, the cut. A later reader may have only your words, so if the description is not vivid enough for an LLM to picture the shot clearly and tell whether the brand can produce it, it has not done the job.

## Where to look, and how to get the data

**Own account first, and widest.** Pull the brand's own video ads through the available source pull, sampled wide. Take the top by period spend, which is Meta's vote for the most potent creative, and the top by hook rate over a sensible spend floor, so the sample spans both the biggest bets and the strongest scroll-stops. Read the `visual_hook`, `creator_demographic`, `ad_analysis`, and `ad_summary` fields on each, plus the script for congruence. Own statics matter too where the brand runs them, for the single-frame grammar. The own account is the foundation and the largest source; everything in it is in play by definition.

**Organic next.** Pull the brand's own organic where it is connected, and the niche's top organic TikTok through the video-report pull. The TikTok reports carry named visual sections, Visual Hook, Camera Angle and Production Setup, Visual Elements and Product Display, Text Overlay Analysis, Creator Demographics and Environment. Read them directly. Organic is the proven-producible expansion frontier: visuals the brand could shoot with a creator and a tripod tomorrow.

**Competitors and inspo and affinity last.** Pull the captured external libraries through the external-ads source with full ad details, so the `storyboard` array, the `visualHook`, the `creatorDemographic`, and the `audio` fields come through. The storyboard's per-beat `visual` descriptions are the richest replay material in the data. Use them. These source the adjacent and out-of-play candidates. Read them against the public-ad-library method: rank and rank-trend are the performance proxy, never converted into inferred spend, and the read here is visual, not a spend ranking.

**Pull what the data shows, never what it implies.** Where a field is blank, record the visual as not readable rather than inventing it. Do not fabricate a shot, a setting, a talent type, or an overlay the source did not provide.

## What to catalog, per the extraction taxonomy

Walk the taxonomy from `visual-vocabulary-method.md` across every ad studied, then read across the library for what recurs. Catalog each of these, the recurring ones described as scenes:

- **Shot types.** The camera grammar the brand reuses, read across the library.
- **Settings and locations.** Where the brand films, held as a capability signal.
- **Talent situations.** Who is on camera and how framed, with the demographic the data gives.
- **Product-interaction moves.** The physical actions the brand stages with the product.
- **Demo mechanics.** The staged demonstrations that prove a claim, where the brand runs real demos rather than asserting.
- **Visual hooks.** The first-frame scroll-stoppers, held for their own first-class section below.
- **B-roll families.** The recurring cutaway footage.
- **Text-overlay and graphic style.** How words and graphics sit on the footage.
- **Transitions and pacing.** How the brand moves between beats and how fast, read against where the ad delivers.

A choice that recurs across the library is signature; a one-off is noted but not treated as vocabulary until it repeats.

## Visual hooks as a first-class section

Pull the brand's visual hooks out as their own section, the way the script-voice profile treats the verbal hook. For each, reconstruct the first frame as a scene, what is on screen in the opening seconds before anything is claimed, name the hook format from `hooks.md` and the container from `ad-formats/`, and classify it in play, adjacent, or out of play. The visual hook carries the most weight and is the most replayable visual the brand owns, so it gets the richest description and the cleanest classification.

## Classify in play, adjacent, out of play

Sort every visual, with the criterion stated, per the method:

- **In play** points at the brand's own filmed unit. Production-proven; needs no downstream flag.
- **Adjacent** points at the orbit unit where the visual was seen plus the capability read that places it producible. Read the capability from what the own account already proves the brand can do. Carry the orbit evidence, described richly enough to replay.
- **Out of play** points at the production muscle, talent, or capability the brand has never shown. Not a scold and not permanent; the line moves the moment the brand proves the capability.

The criterion that separates adjacent from out of play is always read from the own account, never asserted. State it.

## The two binding rules

Hold both while cataloging, because they govern how the vocabulary is used downstream.

**Script-congruence.** A visual must show what the words are saying. Where the library shows a beat's words paired with the visual that demonstrates that beat's specific claim, note the congruence as a model to carry. Where a brand pairs a claim with a generic mood shot, note the incongruence as a tell to avoid. The vocabulary is recorded so a later scriptwriter can direct every beat with a visual that proves that beat.

**Format-dependence.** The same beat is shot differently by format. Where the library shows the brand running a similar beat across more than one format, record how each format shot it, because that per-format grammar is what lets a downstream generator translate a beat into the format being produced. Read the formats against `ad-formats/`, and read pacing against delivery.

## What goes in it, and the output shape

Open with frontmatter, then write the sections below. Use this skeleton so every brand's doc comes out the same shape:

```markdown
---
brand: [brand-slug]
doc: visual-vocabulary
generated_on: YYYY-MM-DD
refresh_by: YYYY-MM-DD
status: [approved, in-review, partial, or blocked]
own_library_read: [the window and sample of the brand's own ads studied]
orbit_read: [the organic, competitor, inspo, and affinity sources studied for the frontier]
data_limitations: [any data limitation that prevents the doc from being treated as final]
refresh_cadence: monthly, with the hook audit
---

# Visual vocabulary: [Brand Name]

## Headline read

## Visual hooks

## Shot types and camera grammar

## Settings and locations

## Talent situations

## Product-interaction and demo mechanics

## B-roll families

## Text-overlay and graphic style

## Transitions and pacing

## Per-format grammar

## The expansion frontier: adjacent and out of play

## Open loops

## Appendix - Parker media links
```

Lead with the headline read: in two or three sentences, what the brand's visual vocabulary actually is, what it owns that the field does not, and where the clearest expansion frontier sits. Then the visual hooks first-class section, then the cataloged categories, each entry classified and marked. Close with the expansion frontier, where the adjacent and out-of-play entries are gathered with their evidence, and the open loops.

## When you refresh this

The visual frontier moves with the field, so refresh this monthly alongside the hook audit. When you rebuild it, take the previous version in as context first, carry forward the in-play vocabulary that still holds, add any new shot the brand has filmed since last time (which moves entries from adjacent to in play), and re-read the orbit for new adjacent and out-of-play candidates. Note any visual the brand has newly proven it can produce, because that is the line moving. Keep the refresh framed as an updated vocabulary read, not a campaign plan.

## Open loops

End with the few consequential questions the visual vocabulary could not resolve.

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

Doc-specific thinking lens. Loops on a visual vocabulary tend to cluster around the messaging territory, specifically the creative layer of what is shown on screen and how the product is demonstrated, and around the creators-and-talent territory of who appears in the brand's visuals and who never does. The recurring real question is whether a proven-adjacent visual would carry for this brand the way it carries in the orbit: a competitor's shot or an organic mechanic that the capability read says the brand could produce but has never tried. A loop here reads like noticing that the brand's whole library stages its product one way while the niche's top organic and a direct rival both open on a visual the brand has the talent and locations to shoot and never has, which leaves open whether that shot would stop the brand's own audience. That is a creative-layer messaging question this doc can legitimately raise. A loop about which hook converted best is a hook-audit question and does not belong here. A loop about whether the brand is filming the right people for its personas is a creators-and-talent question and does belong here. Keep loops at vocabulary altitude; the performance verdict and the campaign plan are owned elsewhere.

Loops do not cover: missing performance metrics, ad-library access gaps, fields that were blank in the source pull, or the deep performance read owned by the hook audit. The first three belong in the frontmatter's data_limitations field, and the last routes to the hook audit. Mark any loop only the brand can answer so it routes to the brand.
