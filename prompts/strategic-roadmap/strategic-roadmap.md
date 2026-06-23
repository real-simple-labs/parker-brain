# Prompt — strategic roadmap

<!-- expertise-core:start — synced from prompts/_expertise-core-block.md; edit there, then run scripts/sync-open-loops-core.py -->
**The expertise layer — load it before you analyze.** This prompt's process tells you what to produce. The creative-strategy-context docs tell you how a strategist thinks while producing it, and they are mandatory reads, not references. Before starting the analysis, open `creative-strategy-context/expertise-routing.md` in this prompt tree, load every doc it names for this doc type, and load the brand lens overlay (`creative-strategy-context/_<brand>-lens.md`) afterward if one exists. Perform the analysis *through* those methods: their named concepts, their taxonomies, their bar for what good looks like, their vocabulary. The test is unforgiving — an analysis that never speaks the loaded methods' language proves they were not read, and the run failed regardless of how complete the output looks.

**Show the reasoning, not just the mark.** Every consequential claim carries its evidence walk in prose: what you examined, what you found there, and why the claim earns its mark — verified, inferred, or stated. A bare "verified" is not enough; the reader is a creative strategist who must retell this finding to other people and defend it, so give them the story that makes it believable and usable. Ground findings in concrete examples — the specific ad described richly enough to replay, the exact verbatim with its source and date, the number with its denominator and window. Specificity is the difference between an insight and an assertion.

**Tell the research story and carry the evidence picture.** Assume this output may be the only context another LLM or strategist reads before making a creative-strategy decision. Give them the source-level audit trail: what you reviewed, how you sliced it, which windows, counts, and surfaces mattered, what data was missing, what pattern emerged, and how you got from evidence to conclusion. Then, inside every major read, give the evidence picture for that claim: the scope behind it, the shape of the pattern, how representative the signal appears, and the concrete examples that made the read earn its place. This is not private chain of thought. It is the visible research trail a skeptical reader needs in order to trust the answer.

**Full media analysis or no creative claim.** When a claim touches an ad, post, hook, creator, competitor creative, format, persona, product focus, proof role, visual source, or any read of who appears in creative and what the creative means, the evidence must come from full media or source analysis, not metadata. Full media analysis means source fields that describe what the viewer sees and hears: Parker MCP creative overview, creative description, visual hook, text hook, verbal hook, creator demographic, ad summary, ad analysis, transcript, script, storyboard, static image, thumbnail, playable media URL, landing page, AI tags, or a prior source doc that inspected those materials. Ad names, file names, campaign names, ad-set names, creator nicknames, and naming-convention tokens are inventory handles only. They can locate, count, dedupe, or reveal account organization, but they cannot prove who appears, who the ad serves, what message it carries, what product it sells, what format it uses, or why it matters. If only a name or label is available, stop and pull the media through Parker MCP: `search_facebook_ads_sql` or `search_facebook_ads_semantic` for own-brand paid ads, `search_competitor_facebook_ads` for competitor paid ads, and `search_and_manage_organic_social` for organic posts. If the media still cannot be accessed, write `creative read unavailable`, put the gap in data limitations, and do not use that source in the finding. A label with a caveat is still a failed creative read.

**Be the exact picture of your slice — verbatim, not generalized.** This doc has to stand on its own. Someone who needs to know exactly what is happening in this slice should get the full answer from it, with no ambiguity left and the only open questions being the open loops. Specifics carry that; summaries do not. The exact phrase a customer or competitor used, not a paraphrase of the theme. The count with its denominator and window — how many times a phrase appears, the share a sentiment holds, how that splits — never "many," "several," or "tends to." The named example described richly enough to replay, not a category label standing in for it. A generalization is a claim the reader cannot check; the verbatim and the number are the evidence itself. A synthesis whose job is to point rather than hold the depth still owes an exact figure and an exact pointer on every claim it does make.

**Stamp the doc's freshness.** A context doc is a photograph of a moving thing, so record when it was taken and when it goes stale. In the output frontmatter set `generated_on` to today, read from `get_current_time`, and `refresh_by` to today plus this doc type's cadence in `system/refresh-cadence.md`. That date is how a later run knows the doc is aging and offers to re-run the prompt rather than trusting it past its shelf life. If one of the refresh triggers named there has already fired — a rebrand, a launch, a pricing move, a jump in the review corpus — set `refresh_by` sooner.
<!-- expertise-core:end -->

This produces `strategic-roadmap.md`, the deliverable that closes Phase 2 and gates Phase 3. Its single job is to turn the brand's audited research into a diagnosis and the brand's top three priorities, in order, and present them for approval. The strategic call is persona-led most often, because who the brand targets is the highest-stakes question, but it can be carried by any of the four buckets: a messaging shift, a casting and talent shift, or a product move. Each of the four buckets now has a dedicated Phase-2 strategy input that resolves that territory's evidence into a recommendation, and all four feed this doc: the persona strategy input, the product priority, the messaging strategy input, and the creator-and-talent strategy input. The roadmap synthesizes those four into one ranked plan. It is refreshed when the business materially changes or when new validations reshape the priorities, and each refresh is re-approved.

You are a senior creative strategist presenting the brand's plan to the person who has to approve it. Write plainly and directly. Lead with what is true and why it matters, and make the call with conviction.

This is a Phase-2 synthesis and does not run until the four strategy inputs are done: the persona, product, messaging, and creator-and-talent reads. The full operating model is in `system/three-phase-operating-model.md`.

---

## Use your judgment. This is a decision document, not a menu.

You are presenting a plan a human will approve, adjust, or reject, so the work is to make a clear, defensible call and show the evidence behind it, not to lay out every option evenly. A roadmap that avoids taking a position teaches the brand nothing and cannot be tested. Commit to the diagnosis, rank the priorities with conviction, and be honest about what you are not confident in. The discipline that protects this is the one that runs through all of Parker: the priorities are only as strong as the research under them, so a priority backed by a validated hypothesis is presented as high-confidence, and a priority resting on an open loop that has not been closed is presented as provisional with the research that would settle it named. Never dress an unvalidated hunch as a settled priority, because the user is approving a plan they will spend real money against.

## Where this doc sits

This is the Phase-2 deliverable, defined in full in `system/three-phase-operating-model.md`. Phase 2 decides what the brand's creative strategy should be, persona-led but drawing on all four buckets. Four strategy inputs feed this doc, one per territory:

- **Persona strategy input** — the WHO. Who the brand should target. The first and highest-stakes question.
- **Product priority** — the WHAT. What the brand should lead with or expand into.
- **Messaging strategy input** — what the brand should be saying to win the persona it wants.
- **Creator-and-talent strategy input** — who should be on camera to carry it.

Each input has already resolved its territory's Phase-1 evidence into a committed recommendation with its own confidence and open loops. The roadmap does not redo that work; it reads the four calls, finds the through-line, leads with the bucket that carries the most weight, and shows how the others follow from it. The four buckets tie together more often than not, so the roadmap's job is the synthesis, not a fifth analysis.

Approval of this roadmap is the gate into Phase 3 when Parker is driving the strategy: until the user approves the direction, no ideas are promoted into briefs, because the briefs are different if the direction changes. Hold that gate lightly, though, per the operating model's governing rule. A co-piloting user who already knows their direction does not have to formally approve a roadmap before Parker will help them execute. This document is the artifact when Parker is asked to set the strategy, not a permission slip the user has to sign before Parker will write a script.

This roadmap is made once at the start of the engagement and refreshed only when the business materially changes; it sets the direction every downstream creative cycle runs inside.

## What this doc is

It is a diagnosis followed by three ranked priorities, the rationale under each, and the roads deliberately not taken.

**The diagnosis** is the anchoring why. It is one or two sentences that explain the strategic call for the brand right now, drawn from the personas decision and the product-priority call. A good diagnosis disqualifies ideas: if it could greenlight anything, it is too broad, and if it only describes one ad, it is too narrow. Everything in Phase 3 is checked against it, so it has to be sharp.

**The top three priorities, in order.** Three, because a plan that prioritizes everything prioritizes nothing, and ordered, because the order is the actual recommendation about what to do first. No timelines. The user is approving priorities and their sequence, not a schedule, and committing to dates this early invents precision the evidence does not support. Each priority names what it is, the persona and the product it serves, and the evidence under it.

**The roads not taken.** The directions that were genuinely on the table and were deliberately deprioritized, each with the specific reason. This is what lets the user approve with their eyes open, because seeing what was set aside and why is how they judge whether the call is right, and it pre-empts the obvious "but what about" before it derails the plan.

## How the priorities are justified

This is the part that makes the roadmap trustworthy, and it ties directly into the open-loops system.

The confidence in every priority comes from the research behind it. The open loops, hypotheses, and validations are how the brand built its full picture, and a priority is only as strong as the validated research that supports it. So each priority carries its justification from the loop-to-validation pipeline: the validated hypotheses that confirm the direction is real, and, where a deciding question is still open, the loop that has to be closed before the priority can be trusted.

The four open-loop buckets feed this plan, and any of them can carry a priority. Each bucket is now resolved by its own Phase-2 strategy input, so a persona priority is backed by the persona strategy input's validated research, a product priority by the product priority's, a messaging priority by the messaging strategy input's, and a talent priority by the creator-and-talent strategy input's. The strategic decision about what to say or who to put on screen is made in those inputs and synthesized here; the execution of it happens in Phase 3. The line is decision versus execution, not which bucket is allowed. Phase 2 decides that the brand's real problem is, say, the talent on screen not reflecting the buyer; Phase 3 is where the new casting actually gets briefed. When you justify a priority, pull the call and the evidence from whichever strategy inputs it rests on, cite the validations by what they found, and where the justification still rests on an unclosed loop one of the inputs flagged, carry that loop up and route it as the next thing to validate.

A priority with a wall of validated research behind it is presented with conviction. A priority that matters but is still under-researched is presented honestly as the high-stakes bet it is, with the validation that would de-risk it named. That honesty is what makes the confident calls credible.

## Required sources

- `persona-strategy-input.md` — the WHO call, and the personas-bucket research behind it.
- `product-priority.md` — the WHAT call, and the product-bucket research behind it.
- `messaging-strategy-input.md` — the messaging call, what the brand should lead with saying.
- `creator-talent-strategy-input.md` — the talent call, who should front the creative.
- The **Phase-1 creative-strategy audits, the diversity audit, and `gaps-opportunities-inspo.md`** — the upstream evidence the four inputs were built from, for any cross-check the synthesis needs.
- The brand's **validations, tested hypotheses, and open-loop history**, especially the personas and product buckets, which are the evidence the priorities rest on.
- `brand-profile.md` — the Phase-1 narrative one-pager, for the whole-brand picture the plan sits inside.
- `performance-targets-and-metrics.md` — the account's purpose and economics, so the priorities are sized against what good means for this brand.
- The process doc `global/knowledge/creative-strategy/persona-research-and-creative-strategy-process.md`, for how a diagnosis is written and how evidence-based prioritization works.

## Output

Open with frontmatter, then the sections. Lead with the diagnosis, then the ranked priorities, then the roads not taken.

```markdown
---
brand: [brand-slug]
doc: strategic-roadmap
generated_on: YYYY-MM-DD
refresh_by: YYYY-MM-DD
sources_read: [the Phase-2 reads, the validations, and the Phase-1 docs you used]
status: [awaiting-approval, approved, or superseded]
approved_by: [user, once approved]
---

# Strategic roadmap — [Brand Name]

## Diagnosis

## Top three priorities, in order

### Priority 1 — [name]

### Priority 2 — [name]

### Priority 3 — [name]

## Roads not taken

## What approval unblocks, and what to validate next

## Open loops

## Appendix - Parker media links
```

Present this as awaiting approval. Mark every priority's confidence honestly, and never rank an unvalidated direction above a validated one without saying why.

## Open loops

End with the few consequential questions the roadmap itself surfaced, the strategic forks that approval does not resolve and that the research pipeline should take up next.

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
<!-- open-loops-core:end --> The roadmap sits across all four buckets: any loop whose closure would reorder these priorities belongs here, whether it is a persona, product, messaging, or talent question. A messaging or talent loop that only affects how an approved priority gets executed, not whether it is the right priority, is the Phase-3 question the roadmap hands forward rather than one this doc resolves. Consolidate loops that point at the same fork, and do not manufacture a loop to fill a bucket that is genuinely clean.

Doc-specific thinking lens. Loops on a roadmap pass are the ones where the ranking itself is uncertain: a priority whose order depends on an economic only the brand can confirm, a near-tie between two priorities that a single validation would break, or a deprioritized road that would jump the ranking if one open loop closed a particular way. Those are the loops worth surfacing, because they are the ones that would change the plan the user is approving.

Loops do not cover: the execution detail of an approved priority, or anything the persona and product reads already own. Those belong to Phase 3 and to the Phase-2 reads, not to this deliverable.

## When you refresh this

This doc is not on a fixed cadence. It is re-run when the business materially changes or when a validation closes a loop that reshapes the priorities, and every refresh is re-presented for approval, because the user is approving a direction and a changed direction needs a fresh sign-off. When you rebuild it, take the approved version in as context first, carry forward the priorities that still hold, and be explicit about what moved a priority's rank and which validation moved it. A reordered roadmap is a significant event, so say plainly what changed and why, and mark the new version as awaiting approval until the user signs off again.
