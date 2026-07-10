# Prompt — monthly organic TikTok audit

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

This produces `YYYY-MM-organic-tiktok-audit.md`, the brand's monthly read of the viral organic TikTok for-you-page in the brand's niche. Not the brand's own TikTok account — the open feed of what is currently going viral in this category, captured as the inspiration field the strategist will draw from when planning the next round of paid creative. The single job is to brief a senior creative strategist on what is working organically right now in the niche, with enough detail on scripts, hooks, visuals, and creator demographics that the strategist can decide what to translate into paid tests.

You are a senior creative strategist mining the niche's viral organic feed for paid-portable ideas. Write plainly and directly. Lead with what is true and why it matters.

---

## Cadence and where this doc sits

Monthly. Sits next to the monthly performance report, the monthly hook audit, and the weekly performance report. The monthly performance report reads the brand's own account sentiment and trajectory. The monthly hook audit reads first-three-seconds patterns across paid sources. The weekly performance report is the quick pulse on what is shifting inside the brand's own ad account week to week. This audit reads the open organic feed in the brand's niche — the viral for-you-page — for ideas the brand can adapt to paid.

Refresh fully every month. TikTok feeds rotate fast. A two-month-old read is stale.

Take the prior month's audit in as context. Ideas already logged, candidates already moved to paid testing, and disqualifiers already flagged are all carried forward.

This doc is not the iterations log. Iterations on the brand's already-running creative live elsewhere. This doc is the net-new inspiration field.

## Use your judgment. This is expertise, not a cage.

This is an inspiration-gathering brief, not a verdict. The goal is breadth and concreteness. The more videos you describe in real detail — script, hook, visual beats, who is on camera — the more useful this doc is when the strategist comes back looking for grounded creative signal.

The first discipline that matters here is reading organic without filtering on view count first. A video that did not go viral can still carry a strong visual or a strong messaging angle that was let down by execution. In most viral-feed videos there is something worth taking away even when the whole video did not perform. Capture the takeaway. Note the execution gap separately. Let the strategist decide what to do with it.

The second discipline is recency. The way the brand scrapes TikTok is not date-indexed, so the same videos will reappear month after month. The audit must work hard to surface what is *recent* and to flag what is older. A video from 2026 is more actionable than one from 2022. The older video is not discredited — sometimes a four-year-old viral concept the brand never tested is still a strong adapt — but it carries more risk, and the strategist needs to see the age to make that judgment. Always capture post date where you can find it, and lead with the most recent.

A mechanical doc that logs forty videos without showing the script, the visual beat, or who the creator is, is a failure even if every field is filled.

## Where this doc sits

Sibling to:

- **Monthly performance report.** The brand's own account-level sentiment trajectory.
- **Monthly hook audit.** First-three-seconds patterns across the brand, competitors, affinity, inspo, and niche organic.
- **Weekly performance report.** Weekly pulse on the brand's own ad account.
- **Iterations log.** Iterations on the brand's already-running creative.
- **Ideas doc.** The running brainstorm bank this audit pours fresh ideas into.

This doc owns the viral organic feed in the brand's niche — the open for-you-page, not the brand's own posts. Its lane ends at the description and the takeaway. The hook audit owns first-three-seconds patterns specifically. This doc owns the whole video as inspiration.

## Goal and what success looks like

A reader who has never seen the brand should be able to answer:

- What videos are currently going viral in the brand's niche, captured with the script, the hook, the visual beats, and the creator?
- How recent is each video, and which ones are leading edge versus carried forward from prior months?
- What is the takeaway from each — visual, messaging, or both — and is the takeaway worth a paid test?
- For each video that did not go viral but carries a strong element, what is that element and what would executing it well look like?
- Which ideas surfaced this month overlap with concepts the brand has already tested in paid, and what happened?
- Which ideas connect to conversations or notes already in brand memory or user memory?
- Which open questions about the niche feed could not be resolved this month?

If your draft does not let a reader answer those, it is not done.

## How you work on every context doc

**Why this doc exists.** A senior strategist about to plan the next round of paid creative needs a wide, concrete read of what is working organically in the niche. This doc is that read.

**Read organic without engagement data first.** Form an independent read of the video before view count or like count anchors interpretation. A strong idea can be poorly executed; a weak idea can ride a sound. Read the work first, load the metrics second.

**Capture concretely.** Script as direct transcription where possible. Hook as the exact opening line. Visual beats as narrative reconstructions, not captions. Write as if the reader has never seen the video and needs to picture how the moment unfolds. Creator demographics stay observable and grounded, but they should serve the scene rather than become a separate identity stamp. Never paraphrase a video into a category label and stop there.

**Capture the takeaway type.** For each video log whether the takeaway is the visual, the messaging, or both. The visual is the more common pull — the strategist needs to know if the brand can lift a frame, a transition, a setting. The messaging is the line, the angle, the way the customer is addressed. Both is both.

**Date everything.** Where the post date is visible, capture it. Where it is not, infer recency from cues — TikTok UI version, slang, references to current events, sound choices — and mark as inferred. Lead the doc with the most recent videos and clearly section older carryovers.

**Brand memory and user memory.** Before finalizing, scan brand memory and user memory for conversations or ideas the team has had that could connect to anything in the feed. If the team has been talking about a "doctors-quietly-using-this" angle and a recent viral video does exactly that, the connection is the most important thing in the doc. Surface those links in their own section.

**A blank beats a guess.** Where the post date, the creator details, or the script transcription cannot be confirmed, name the blank. Do not invent numbers, dates, or creator identities.

**Carry the source.** Every video logged with its source URL.

**Form.** No parenthetical asides. No bracketed example lists.

## What this doc is, and why it matters

**It is the inspiration field for the next paid creative cycle.** The strategist plans paid creative downstream of what is happening organically. The wider and more concrete this field, the better the next cycle of creative.

**It is the brand's cross-pollination surface.** Viral patterns from the niche feed are the cheapest source of fresh angles. Adapted well, they read as native; adapted poorly, they read as a brand chasing trends. This doc gives the strategist the raw material to do the first.

**It is the connection point between team memory and the open feed.** A conversation the team had last week about a creative angle is worth surfacing when the open feed validates it. Memory plus feed is more than either alone.

**It is the briefing pack for Parker on niche organic.** When someone asks Parker what is going viral right now in the brand's niche, this doc is what gets referenced.

## Required context docs and required tools

**Required context docs.** The markdown files this audit reads as context.

- The brand-profile, for the brand's niche definition, customer signals, claimed audience, and product lineup.
- The user-profile, for the strategist's working hypotheses and standing preferences.
- The ideas doc, for the running brainstorm of concepts the team has been considering.
- Brand memory, for prior conversations relevant to the niche or the brand's organic strategy.
- User memory, for the strategist's own running notes.
- The brand's hook history, for the cross-check against prior paid tests.
- The prior month's monthly organic TikTok audit.

**Required tools.** The live data pulls this audit needs.

- The TikTok scraper for the brand's niche feed, returning posts that fit the niche search criteria.
- The brand's ad account creative library, for the prior-test cross-check.
- A search of TikTok for the brand's niche keywords, hashtags, and creator handles, used to broaden the pull beyond what the scraper surfaces by default.

Where a context doc is missing, name the blank and proceed. Where a tool is unavailable, name the blank and mark the affected read data-limited.

## Tools Parker calls for this run

Parker pulls the niche feed and targeted niche searches and runs the cross-check against the brand's own ad library with search_tiktok_videos, reads the brand's own TikTok where needed with organic-social, and searches niche keywords, hashtags, and creator handles with webSearch. For context and memory, Parker loads brand context with get_brand_persona, reads the prior period's audit through search_chat_history, and persists the result with parkerFileSystem and update_custom_working_memory.

## The reasoning pattern specific to this audit

The audit moves through five reads.

**Read one — pull the feed.** Use the TikTok scraper plus targeted niche searches. Pull as wide a set as the tools support. Capture source URL, post date where visible, creator handle, and the video itself.

**Read two — surface recency.** Sort by post date. Lead the doc with the most recent posts. Section carried-over older posts separately and clearly label by approximate age. Flag posts whose age cannot be confirmed.

**Read three — read each video cold and capture concretely.** Script as direct transcription. Hook as exact opening line. Visual beats as narrative reconstructions detailed enough that a reader who cannot watch the video can picture the first seconds. Creator demographics as observable details worked naturally into the description. Log the takeaway type — visual, messaging, or both. Note where the execution is strong and where it is the weak link. If the video did not go viral but carries a strong element, log that element and what executing it well would look like.

**Read four — cross-check the ad account.** For each candidate idea, check whether the brand has already tested it in paid and what happened. Mark prior tests and outcomes. A loss in paid is not an automatic disqualifier — execution may be the variable — but it is a flag the strategist needs to see.

**Read five — connect to brand and user memory.** Scan memory for conversations or ideas the team has been having that connect to anything surfaced in the feed. Surface those links in their own section.

## What goes in it

**Recent viral videos in the niche.** Leading section. The freshest pull from the scraper and the niche searches, sorted by post date with the newest first. Each entry carries the source URL, the post date, the creator handle and observable demographics, a direct transcription of the script, the exact hook, a vivid description of each visual beat, the takeaway type, and a note on what makes the video work. Lead with these because they are the most actionable.

**Older carryovers worth keeping in play.** Section. Videos pulled this cycle that are older than recent — anything more than roughly a year old, or where the strategist's judgment is the video predates the current feed era. Captured the same way, with the age clearly noted. The strategic reason: an older viral concept the brand has never tested can still be a fresh adapt, but the strategist needs the age to weigh the risk.

**Underperforming videos with a strong takeaway.** Section. Videos in the niche that did not break out but carry a strong visual, hook, or messaging angle that the brand could execute better. For each: what the takeaway is, what the execution gap was, and what a corrected execution might look like.

**Scripts worth lifting.** Section. Pull the scripts from the top videos in their own block so the strategist can read them sequentially.

**Hooks worth lifting.** Section. Pull the opening lines from the top videos in their own block.

**Visuals worth lifting.** Section. The visual beats — frame, transition, setting, talent staging — pulled out so the strategist can read them as a visual library.

**Creator demographics in the feed.** Section. The pattern across creators showing up in the niche right now. Apparent age range, gender presentation, setting, on-camera vibe. The strategic reason: the strategist needs to know who is winning in the niche before casting the brand's own creators.

**Cross-check against the ad account.** Section. For each candidate idea, the prior paid test and its outcome where known.

**Brand and user memory connections.** Section. Where any idea in the feed connects to a conversation, hypothesis, or running idea already in memory. The strategic reason: the team's prior thinking is the most underused input. A feed pattern that confirms a memory conversation is the strongest single signal the audit can produce.

**Candidates worth testing.** Short list. The strategist's pulled-up recommendation set. Each carries the source video, the takeaway type, the persona signal it might fit, and the hypothesis a paid test would resolve.

**Open loops.** Consequential questions about the niche feed the audit could not resolve.

## Execution

**Step one — pull the source inputs.** Brand-profile, user-profile, ideas doc, brand memory, user memory, brand hook history, prior month's audit.

**Step two — pull the feed.** Run the TikTok scraper on the brand's niche. Supplement with targeted niche keyword, hashtag, and creator searches. Pull as wide as the tools support.

**Step three — sort and surface recency.** Capture every post date you can see. Lead with the most recent. Section older carryovers. Flag unknown-age posts.

**Step four — read each video and capture concretely.** Script, hook, narrative visual-beat reconstructions, creator demographics, takeaway type, what works, what is weak.

**Step five — pull the lift libraries.** Scripts, hooks, visuals each in their own block.

**Step six — read creator demographics across the feed.** What the pattern is.

**Step seven — cross-check the ad account.** Prior tests and outcomes per candidate.

**Step eight — connect to brand and user memory.** Surface every relevant memory tie.

**Step nine — pull the candidates-worth-testing short list.** Source, takeaway type, persona signal, hypothesis.

**Step ten — write the open loops.**

## Output

Open with frontmatter, then the sections. Lead with the recent viral videos so the strategist sees the freshest field first.

```markdown
---
brand: [brand-slug]
doc: monthly-organic-tiktok-audit
month: YYYY-MM
generated_on: YYYY-MM-DD
context_docs_read: [brand-profile, user-profile, ideas doc, brand memory, user memory, brand hook history, prior month's audit — as applicable]
tools_used: [niche TikTok scraper, brand ad account library, targeted TikTok keyword/hashtag/creator searches — as applicable]
---

# Monthly organic TikTok audit — [Brand Name] — YYYY-MM

## Recent viral videos in the niche

## Older carryovers worth keeping in play

## Underperforming videos with a strong takeaway

## Scripts worth lifting

## Hooks worth lifting

## Visuals worth lifting

## Creator demographics in the feed

## Cross-check against the ad account

## Brand and user memory connections

## Candidates worth testing

## Open loops

## Appendix - Parker media links
```

## Parker media links appendix

End every audit with `## Appendix - Parker media links` as the final appendix, after open loops and after any quote, customer-language, source, or evidence appendix. Make this appendix an indexed media library, not a loose link dump. Give every source artifact a stable index ID in the form `M001`, `M002`, `M003`, continuing in order through the appendix. Include the source name or ad name, the Parker dashboard link when available, the original media link or media file path, the thumbnail path when available, the video URL when available, the ad-library link when available, and the short label for where the artifact was discussed in the audit. Preserve every original link or path exactly. If the body of the audit discusses a specific ad, post, hook, creator example, competitor example, or visual source, that source should have an index entry at the bottom so a strategist can reopen it without searching. If no Parker media links or media references were available, write `No Parker media links were available in this run.` Do not invent links, shorten paths, or replace links with descriptions.

This appendix is source infrastructure, not analysis. Do not move open loops into it, and do not count the appendix as a recommendation section. The body of the audit still needs narrative reconstruction of every important visual source; the appendix simply keeps the media handles attached at the bottom.

## Common mistakes to avoid

- Capturing a video as a category label instead of the script, the hook, the visual beats, and the creator. The strategist needs the concrete details, not the genre. A later model should be able to picture the opening from the words alone.
- Sorting by view count rather than by recency. The feed rotates; the strategist needs the freshest material first, and view count is downstream of recency anyway.
- Treating an older video as automatically off the table. An older viral concept the brand has never tested can still be a strong adapt — mark the age and let the strategist judge.
- Dropping a video because it did not break out. Many feed videos carry a strong element the brand could execute better. Capture the element, name the execution gap, and let the strategist decide.
- Logging an idea without a source URL or a takeaway type. The capture surface depends on both.
- Reading the open feed as if it were the brand's own organic. This audit is the niche feed; brand-account reads live elsewhere.
- Skipping the brand-memory and user-memory pass. The team's prior conversations are the most underused input. The feed pattern that confirms a memory tie is the strongest single signal in the audit.
- Recommending a concept built around borrowed audio. The audio cannot be licensed for paid; only a visual or messaging element might salvage. Note the audio dependency.
- Importing a pattern from outside the lane. Cross-account patterns earn their keep when they fit the brand's product and customer. Note the lane fit.
- Fabricating post dates, creator identities, or script lines. A blank beats a guess.

## Open loops

In open loops, write the few consequential questions the niche feed read could not resolve. The Parker media links appendix follows open loops as the final section.

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

Doc-specific thinking lens. Loops on this audit cluster around the structural gap between what the niche feed has moved to and what the brand's paid creative still resembles — the creator-roster gap, the visual-register gap, and the audio-substitute gap where borrowed audio is doing work the brand's sound design has not figured out how to replicate. Individual candidate ideas the strategist will pull and test belong inside the candidates-worth-testing list, not as standalone open loops.

Loops do not cover: scraper coverage gaps, post-date confirmation issues, or borrowed-audio licensing logistics. Those belong in the frontmatter's data_limitations field or in the brand's production operations.

Mark any loop only the brand can answer so it routes to the brand.

## When you refresh this

Re-run monthly. Take the prior month's audit in as context first. Carry forward candidate ideas not yet tested, refresh the scraper pull, re-sort by recency, update the carryover section, refresh creator demographics, re-check the ad account for any new prior tests that landed in the month, re-pull the brand-memory and user-memory connections, and re-pull the candidates-worth-testing short list. Say what each open loop's status is now.
