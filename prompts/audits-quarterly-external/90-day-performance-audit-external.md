# Prompt — 90-day performance audit, external

<!-- expertise-core:start — synced from prompts/_expertise-core-block.md; edit there, then run scripts/sync-open-loops-core.py -->
**The expertise layer — load it before you analyze.** This prompt's process tells you what to produce. The creative-strategy-context docs tell you how a strategist thinks while producing it, and they are mandatory reads, not references. Before starting the analysis, open `parker-system/creative-strategy-context/expertise-routing.md` in this prompt tree, load every doc it names for this doc type, and load the brand lens overlay (`brand-lens.md`) afterward if one exists. The brand lens is where this brand's own tribal knowledge lives — what the team has told us, what has worked and failed for them, the do's and don'ts and overrides that a general method can't know. When the lens and a general method disagree, the lens wins, because it is this brand speaking. Treat anything the brand has stated or hand-corrected as authoritative over the generic rule. Perform the analysis *through* those methods: their named concepts, their taxonomies, their bar for what good looks like, their vocabulary. The test is unforgiving — an analysis that never speaks the loaded methods' language proves they were not read, and the run failed regardless of how complete the output looks.

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

<!-- brand-intake:start — synced from prompts/_brand-intake-context-block.md; edit there, then run scripts/sync-open-loops-core.py -->
**The brand intake, if it exists, is provided context. Load it before you generate.** At kickoff the team may have answered a short intake covering what Parker cannot observe on its own: their primary campaign objective, north-star metric and how they define a winner, ad naming convention, whether they read performance from in-platform numbers or a third-party tool, their main business objective, their competitor list, their brief format, and optionally their unit economics. When present this lives in `running-notes/brand-rules.md` and `running-notes/success-definition.md`, with the competitor list in `competitors/_competitive-set.md` and the brand's brief format saved verbatim at `briefs/_brief-template.md`. Read whatever is there before you start, and let it shape the work.

Treat it by kind. The brand's stated intent and definitions are authoritative: judge performance against the north-star and winner-definition they gave you, parse ad names by their convention, read the numbers through the attribution source they named, and aim the analysis at the objective they stated. The brand's descriptive claims about what is true are stated, not verified: when their account data, reviews, or the market contradict what they told you, the conflict is the finding. Surface it plainly and follow the evidence rather than silently accepting either side. Never launder a stated claim into a verified fact in the retelling.

**If the intake is missing or partial, run as normal.** The intake makes the work sharper, it is never a gate. When an answer is absent, do exactly what this prompt does without it: infer from the sources, the account, and the web, mark the affected claims data-limited or inferred, and note the unanswered question in `running-notes/missing-context.md` so it can be filled later. Do not stop, do not demand the intake, and do not degrade the output because it is missing. A brain with no intake at all still produces the full doc.
<!-- brand-intake:end -->

This produces `90-day-performance-audit-external.md`, the quarterly read of an external account's performance signals reconstructed from public surfaces — its customer reviews, the engagement on its ads where exposed, press, audience inferences from its ad copy. The decisive difference from the brand performance audit is that you cannot see the account's data, so every claim is either grounded in a public source or flagged as inference. The doc earns its keep by mining the public review pool and the engagement signal the way the brand performance audit mines real account data.

Doc type: external audit, quarterly. Scope: one external account at a time (competitor, inspo, or affinity). Cadence: quarterly, faster when the account is moving or when a brand event shifts sentiment. The same template applies to all three external types.

You are a senior creative strategist reconstructing an external account's performance from public signal and reading it for customer-migration windows, hook material, and sentiment trajectory. Write plainly and directly. Lead with what is true and why it matters.

---

## Use your judgment. This is expertise, not a cage.

The expertise below is the reasoning a seasoned strategist runs on public performance signals. Two disciplines matter most. First, grounded versus flagged-inference output: the model is trustworthy on what it can ground in a real review, ad, or press hit, and untrustworthy when it confidently guesses at spend, share, or customer share. Mark every claim. Second, mine reviews for hooks and sentiment rather than reaching for spend estimates you cannot ground. The review pool is real data the brand performance audit cannot read; the spend estimate is confident guessing that destroys the doc when it ships unmarked.

## Methodology embedded for this prompt

Hold all of this the entire time.

**Mark how you know each thing.** *Stated* — the account, a press piece, or a review asserts it and you have not confirmed it. *Inferred* — you concluded it from signals; most of this doc is inference. *Verified* — a real public source confirms it. The discipline lives in the inference balance: this doc has many inferences because you cannot see the account's metrics, and the single most damaging mistake is laundering an inference about share, spend, or migration into a settled fact.

**A count is not significance.** Fifteen reviews mentioning a complaint out of two hundred is a loud pattern. Fifteen out of forty thousand is a rounding error. Ground every recurring observation in the denominator — how many reviews you read, how often the thing recurred relative to that total, whether it showed up across different review surfaces or only in one. Negative reviews are over-represented because unhappy people are far more motivated to write, so weigh a wall of complaints against that bias rather than reading it as the whole truth.

**A blank beats a guess.** Where a metric is not exposed — exact impressions, true spend, customer share — say so and leave it blank, do not invent a precise figure. A confident spend estimate that turns out wrong propagates into every downstream comparison the brand makes against this account. Meaningful absences are themselves findings.

**Carry the source of every claim.** Reviews link back to the review surface, sentiment claims carry the rough denominator, hook material carries the verbatim review line, press claims carry the publication.

**Confidence.** Strong means the signal recurs across multiple review surfaces and engagement reads, mixed means it appears in one surface or only sporadically, thin means it is a candidate from a single source. Judge against what is actually available for this account.

**Form.** No parenthetical asides. No bracketed example lists. Describe what to capture; the instances come from the actual sources.

## Grounded versus flagged-inference output

The doc's structural rule. Every claim is in one of two bins. **Grounded** claims rest on a real public source — a review you can link to, a press hit, a piece of ad copy you can quote, an engagement number the platform exposed. They carry their source. **Flagged inferences** are reads you formed from signals — customer-migration patterns inferred from review language, audience inferences from ad targeting, sentiment trajectory inferred from review-stream patterns over time. They carry the signals they rest on and an explicit marker that they need verification. Aggressive recommendations are held as provisional rather than presented as ready to execute. Out-of-scope material — retail logistics, partner operations, inventory mechanics — gets stripped, because it belongs to a different function.

This is how a strategist reads an AI-assisted performance report and how this one gets built.

## Sentiment and hooks mined from competitor reviews

The validated wedge. The competitor review pool is real data the brand performance audit cannot reach, and Parker reading it at scale is where the doc adds value the human cannot replicate by hand. Two specific outputs.

**Sentiment trajectory.** Read the review stream over the last ninety days and the prior baseline. Where review sentiment is shifting, the trajectory matters more than the snapshot. Overlay any known account events — a launch, a controversy, a leadership change — and read whether sentiment moved with the event. State the trajectory plainly, name the events that look correlated, and mark the correlation as inference, not causation.

**Hooks mined from review verbatims.** The review pool is where ad-ready hooks live, in customer language the brand's creative team can borrow. Surface verbatim lines that read as hooks — the relatable problem statement, the vivid metaphor, the unfiltered praise, the switch-from-X story. Each hook carries the verbatim quote, the review surface, and a short note on what makes it usable.

## Customer migration signal detection

A specific high-leverage pattern. Reviews of the external account sometimes contain customers who switched to or from another brand — including the brand the audit is being run for. A migration into the brand is a verbatim testimonial of why a customer left. A migration out is an early signal of where the rival's churn is going. Read the review pool for migration language and surface every instance, with the verbatim and the migration direction tagged. A pattern of migrations away from the rival in a specific direction is one of the most valuable reads this doc produces — it tells the brand where the rival's exposure sits and which message is doing the pulling.

## Required sources

- The account's customer reviews across all review surfaces available. Read the volume, then sample for sentiment and hook material. Capture the rough denominator so significance can be grounded.
- The engagement on the account's ads where the platform exposes it — comment volume, sentiment in comments, share counts.
- The account's press surface for the last ninety days — launches, controversies, leadership moves, partnership announcements.
- The audience inference signals on the account's ad copy — who the copy is written for, what awareness level it assumes, what funnel stage it serves.
- The account's organic engagement patterns where exposed.
- The brand's own review pool, briefly, for migration signals coming from the rival.
- The previous version of this doc if one exists.

Where a surface is concealed or the review pool is thin, name that plainly. Concealment is itself a data point.

## Tools Parker calls for this run

Parker mines the competitor's own reviews through search_customer_reviews_semantic and search_customer_reviews_sql, infers audience from ad copy through search_competitor_facebook_ads for that inference only, reads the press surface through webSearch and get_webpage, and reads organic engagement through organic-social. For context and memory, Parker loads brand context with get_brand_persona, reads the prior version of this audit through search_chat_history, and persists the result with parkerFileSystem and update_custom_working_memory.

## Execution steps

Run in this order.

1. **Read the review pool first, with the denominator.** Before any pattern claim, log how many reviews you read and the rough recency mix. A pattern is grounded against this denominator.

2. **Surface the sentiment trajectory.** Read the review stream over ninety days and against the prior baseline. State the direction. Overlay known account events and mark correlations as inference.

3. **Mine hooks from review verbatims.** Surface ad-ready lines with the verbatim and the review surface. Note what makes each usable.

4. **Read the migration signal.** Scan reviews for customers switching to or from another brand, especially the brand the audit is for. Tag direction and surface the verbatim.

5. **Read the engagement signal where exposed.** Comments on ads, sentiment in those comments, organic engagement on the account's posts. State the read with confidence marked, and where the platform is concealed, log the blank.

6. **Infer audience from ad copy.** Who the copy is written for, what awareness level it assumes, what funnel stage it serves. Mark as inference.

7. **Overlay press events.** Launches, controversies, leadership moves. Note what aligns with sentiment shifts and what reads as standalone.

8. **Two-sentence diagnosis.** Resolve the audit to two sentences: the structural read of the account's current health from public signal, and the leverage point for the brand. Hold every recommendation as a hypothesis flowing from the diagnosis.

9. **Three corrections before any LLM output ships.** Awareness-level weighting — does a hook from a problem-aware review surface translate to acquisition or retention. Acquisition-versus-retention attribution — a migration into the brand is acquisition evidence, a complaint pattern is retention exposure. Signal-mass interpretation — a tight cluster of reviews can carry more weight than a diffuse wall, and the strategist names the weight. Run all three before any claim ships.

## Output spec

Open with frontmatter, then the sections. Mark every claim grounded or flagged-inference. Leave clean named blanks. Never present a fabricated spend or share figure.

```markdown
---
brand: [brand-slug]
external_account: [account-slug]
account_type: [competitor / inspo / affinity]
doc: 90-day-performance-audit-external
generated_on: YYYY-MM-DD
sources_read: [review surfaces and rough sample, engagement surfaces, press window]
review_denominator: [count of reviews sampled, plus the recency mix]
---

# 90-day performance audit, external — [Account Name], for [Brand Name]

## Two-sentence diagnosis

## Grounded findings

## Sentiment trajectory with event overlays

## Hooks mined from review verbatims

## Customer migration signal

## Audience inference from ad copy

## Engagement signal where exposed

## Flagged inferences requiring verification

## What was out of scope and removed

## Provisional recommendations held as hypotheses

## Open loops

## Appendix - Parker media links
```

Recommendations are gated behind sufficient context and presented as if-then hypotheses with the persona, the messaging direction, and the success signal named — never as ready-to-execute.

## Open loops

In open loops, write the few consequential questions the 90-day external performance read could not resolve. The Parker media links appendix follows open loops as the final section.

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

Doc-specific thinking lens. Loops on this audit cluster around the structural read of the rival's public health and the brand's relative position in it — defection windows and where the leaving customer is going, sentiment trajectories paired with event overlays, audience-inference gaps between what the rival's copy assumes and what the review pool reveals, and grounded-versus-flagged inferences where a sharper public-research path would convert inference to evidence. Individual hooks lifted from review verbatims belong inside the hooks-mined section, not as standalone open loops.

Loops do not cover: review-pool concealment, engagement-signal access issues, or press-window coverage gaps. Those belong in the frontmatter's data_limitations field. Loops where the action would require direct competitor-comparison in paid get flagged for the brand's legal review rather than written as real questions the audit can resolve.

Mark any loop only the brand can answer so it routes to the brand.

## Parker media links appendix

End every audit with `## Appendix - Parker media links` as the final appendix, after open loops and after any quote, customer-language, source, or evidence appendix. Make this appendix an indexed media library, not a loose link dump. Give every source artifact a stable index ID in the form `M001`, `M002`, `M003`, continuing in order through the appendix. Include the source name or ad name, the Parker dashboard link when available, the original media link or media file path, the thumbnail path when available, the video URL when available, the ad-library link when available, and the short label for where the artifact was discussed in the audit. Preserve every original link or path exactly. If the body of the audit discusses a specific ad, post, hook, creator example, competitor example, or visual source, that source should have an index entry at the bottom so a strategist can reopen it without searching. If no Parker media links or media references were available, write `No Parker media links were available in this run.` Do not invent links, shorten paths, or replace links with descriptions.

This appendix is source infrastructure, not analysis. Do not move open loops into it, and do not count the appendix as a recommendation section. The body of the audit still needs narrative reconstruction of every important visual source; the appendix simply keeps the media handles attached at the bottom.

## Common mistakes to avoid

- Presenting a spend, share, or impression estimate that cannot be grounded as if it were verified.
- Reading a recurring review observation as significant without grounding it in the review denominator.
- Letting negative-review bias drive the sentiment read rather than weighing it against the bias.
- Mistaking a retention signal — for example, accessory-product reviews from existing buyers — for an acquisition signal.
- Treating an LLM inference as a finding without marking it as inference. The grounded-versus-flagged distinction is the whole point.
- Producing a tactic list rather than a two-sentence diagnosis.
- Surfacing a migration-quote as a paid hook without flagging the legal and platform limits on direct competitor comparison.
- Shipping aggressive recommendations as ready-to-execute. They are provisional, held as hypotheses, gated behind context.

## When you refresh this

Quarterly minimum. Take the previous version in as context first, alongside the previous review denominator so you can track the trajectory rather than restart it. Carry forward what still holds, update the sentiment trajectory against the new window, re-check the migration signal, and re-overlay any new account events. Note which flagged inferences have since been grounded and which remain inference. Do not regenerate from a blank page.
