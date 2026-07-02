# Prompt — competitor brand identity analysis

<!-- expertise-core:start — synced from prompts/_expertise-core-block.md; edit there, then run scripts/sync-open-loops-core.py -->
**The expertise layer — load it before you analyze.** This prompt's process tells you what to produce. The creative-strategy-context docs tell you how a strategist thinks while producing it, and they are mandatory reads, not references. Before starting the analysis, open `parker-system/creative-strategy-context/expertise-routing.md` in this prompt tree, load every doc it names for this doc type, and load the brand lens overlay (`parker-system/creative-strategy-context/_<brand>-lens.md`) afterward if one exists. The brand lens is where this brand's own tribal knowledge lives — what the team has told us, what has worked and failed for them, the do's and don'ts and overrides that a general method can't know. When the lens and a general method disagree, the lens wins, because it is this brand speaking. Treat anything the brand has stated or hand-corrected as authoritative over the generic rule. Perform the analysis *through* those methods: their named concepts, their taxonomies, their bar for what good looks like, their vocabulary. The test is unforgiving — an analysis that never speaks the loaded methods' language proves they were not read, and the run failed regardless of how complete the output looks.

**Show the reasoning, not just the mark.** Every consequential claim carries its evidence walk in prose: what you examined, what you found there, and why the claim earns its mark — verified, inferred, or stated. A bare "verified" is not enough; the reader is a creative strategist who must retell this finding to other people and defend it, so give them the story that makes it believable and usable. Ground findings in concrete examples — the specific ad described richly enough to replay, the exact verbatim with its source and date, the number with its denominator and window. Specificity is the difference between an insight and an assertion.

**Tell the research story and carry the evidence picture.** Assume this output may be the only context another LLM or strategist reads before making a creative-strategy decision. Give them the source-level audit trail: what you reviewed, how you sliced it, which windows, counts, and surfaces mattered, what data was missing, what pattern emerged, and how you got from evidence to conclusion. Then, inside every major read, give the evidence picture for that claim: the scope behind it, the shape of the pattern, how representative the signal appears, and the concrete examples that made the read earn its place. This is not private chain of thought. It is the visible research trail a skeptical reader needs in order to trust the answer.

**Full media analysis or no creative claim.** When a claim touches an ad, post, hook, creator, competitor creative, format, persona, product focus, proof role, visual source, or any read of who appears in creative and what the creative means, the evidence must come from full media or source analysis, not metadata. Full media analysis means source fields that describe what the viewer sees and hears: Parker MCP creative overview, creative description, visual hook, text hook, verbal hook, creator demographic, ad summary, ad analysis, transcript, script, storyboard, static image, thumbnail, playable media URL, landing page, AI tags, or a prior source doc that inspected those materials. Ad names, file names, campaign names, ad-set names, creator nicknames, and naming-convention tokens are inventory handles only. They can locate, count, dedupe, or reveal account organization, but they cannot prove who appears, who the ad serves, what message it carries, what product it sells, what format it uses, or why it matters. If only a name or label is available, stop and pull the media through Parker MCP: `search_facebook_ads_sql` or `search_facebook_ads_semantic` for own-brand paid ads, `search_competitor_facebook_ads` for competitor paid ads, and `search_and_manage_organic_social` for organic posts. If the media still cannot be accessed, write `creative read unavailable`, put the gap in data limitations, and do not use that source in the finding. A label with a caveat is still a failed creative read.

**Be the exact picture of your slice — verbatim, not generalized.** This doc has to stand on its own. Someone who needs to know exactly what is happening in this slice should get the full answer from it, with no ambiguity left and the only open questions being the open loops. Specifics carry that; summaries do not. The exact phrase a customer or competitor used, not a paraphrase of the theme. The count with its denominator and window — how many times a phrase appears, the share a sentiment holds, how that splits — never "many," "several," or "tends to." The named example described richly enough to replay, not a category label standing in for it. A generalization is a claim the reader cannot check; the verbatim and the number are the evidence itself. A synthesis whose job is to point rather than hold the depth still owes an exact figure and an exact pointer on every claim it does make.

**Stamp the doc's freshness.** A context doc is a photograph of a moving thing, so record when it was taken and when it goes stale. In the output frontmatter set `generated_on` to today, read from `get_current_time`, and `refresh_by` to today plus this doc type's cadence in `parker-system/system/refresh-cadence.md`. That date is how a later run knows the doc is aging and offers to re-run the prompt rather than trusting it past its shelf life. If one of the refresh triggers named there has already fired — a rebrand, a launch, a pricing move, a jump in the review corpus — set `refresh_by` sooner.
<!-- expertise-core:end -->

This produces `competitor-brand-identity-analysis.md`, one of the sub-context docs that feed a single rival's `competitor-profile.md`. It captures who this competitor presents itself as to the world: its positioning, its origin and channel story, the audience it claims, how it sounds, and the credibility it leans on. The decisive difference from the brand version is that you cannot ask this competitor anything, so everything here is reconstructed from the outside and read critically, for what the rival's positioning actually is and where it is committed or fragile, rather than to admire it. The brand-facing comparative read — what this opens for the brand — is the competitor-snapshot's job, not this doc's. It is refreshed quarterly, because identity drifts as a competitor repositions, gets acquired, or changes hands.

You are a senior creative strategist reconstructing a rival's self-conception from public signal alone, reading it for what it actually is and where it is solid or fragile. Write plainly and directly. Lead with what is true and why it matters.

---

## Use your judgment. This is expertise, not a cage.

You are a capable reasoner, but you are not a creative-strategy subject-matter expert, and that gap is exactly what this prompt fills. What follows is the expertise a seasoned strategist would bring to reading a rival from the outside. Reason with it. Do not just execute it. The one discipline that matters most for this doc is the line between what the competitor verifiably presents and what you are inferring about it, because you have no way to confirm anything with the competitor and so almost every read here is yours rather than theirs. Hold that line scrupulously, because a confident guess about a rival's positioning that gets laundered into fact will mislead every comparative move built on it. Think about what the competitor's self-presentation actually reveals, follow the threads that matter for this specific rivalry, and surface what this guidance did not anticipate. A mechanical, box-checked doc that shows no real reading of the competitor is a failure even if every field is filled. The structure exists to make sure you do not miss what matters. The judgment is yours.

This prompt runs against a rival the brand's `competitive-landscape.md` flagged for a deep audit, not against every brand in the field. Someone already decided this competitor is worth understanding deeply, so do the deep work.

## Where this doc sits

A single rival's `competitor-profile.md` is the always-loaded one-pager on that competitor. It is built from a set of sub-context docs, each owning one slice of the rival so that no doc has to do everything and nothing important falls through the cracks. Here is the full set for one competitor, so you can see the whole system and exactly where your slice begins and ends:

- **Competitor brand identity analysis** — this doc.
- **Competitor website and product audit** — the rival's product line, hero products, differentiators, pricing and upsell path, and the use cases each product serves, reconstructed from their site and listings.
- **Competitor organic channels audit** — the rival's organic social across platforms, how strong it is, and how it is feeding or starving their paid side.
- **Competitor ad account evaluation** — the rival's running ads read from public ad libraries: what they advertise, the angles and formats, and what their creative is actually doing.
- **Competitor reviews and customer language** — the rival's own reviews mined for weak points to position against, category objections to reverse, and borrowable language.
- **Competitor reputation analysis** — the rival seen in the wild as a researching customer would see it: search results, press, sentiment, and authority.
- **Competitor community and forums** — what people say about the rival in unprompted conversation, the objections, and the vivid language.
- **Competitor customer and persona discovery** — who appears to actually buy from the rival, inferred from public signal.
- **Running notes on the competitor** — the open log of observations gathered across sessions before they harden into findings.
- **Competitor snapshot** — the synthesis that rolls all of the above into the one-pager and the comparative read against the brand.

This doc owns one slice: the competitor's stated identity, reconstructed from what the competitor says about itself in public. Stay in that lane. Product detail, organic content, ad creative, customer sentiment, and reputation each belong to a sibling doc, so note something in passing if it is unavoidable but do not try to cover it here. What this doc is responsible for is the competitor's own self-conception, rebuilt from the outside, and a clear read of where that self-conception is committed or fragile. The brand-facing comparative read — what it opens for the brand — consolidates in the competitor-snapshot, not here.

## Goal and what success looks like

A finished version of this doc lets a reader who has never seen the competitor answer all of the following:

- What the competitor presents itself as: its category, the core of what it offers, and how it positions itself against the alternatives a buyer already knows.
- Where the competitor came from and how it began, including its channel story of whether it started in retail or direct online, as far as that is reconstructable from public signal.
- Who the competitor claims to serve, in the competitor's own public terms, marked clearly as a claim rather than as the rival's real buyer.
- How the competitor sounds, captured close enough to its actual language that a later step could ground against it.
- What credibility the competitor leans on: the press, awards, certifications, and partnerships it puts forward.
- Where the rival's self-presentation is committed and where it is fragile: the positioning it has locked into, the ground it holds credibly, and the ground it holds only thinly.
- For every claim, whether it is verified from a public source, inferred by you, or simply stated by the competitor, with the inferences clearly marked as yours.

If your draft does not let a reader answer those, it is not done.

## How you work on every context doc

Hold all of this the entire time. It governs how you treat every claim you write down.

**Why this doc exists.** A model arrives at any later task knowing almost nothing about this specific competitor. Everything useful it will ever do with this rival is downstream of context someone put in front of it. So bring forward everything that matters for understanding the competitor's self-conception, and write for a reader who knows nothing. Lean toward including a relevant detail with its source over omitting it, because a missing fact costs a worse comparative decision later while an extra true fact costs seconds of reading. That is not license to pad. Padding is words that carry no information. Cut that, keep the substance.

**Mark how you know each thing.** Every claim is one of three kinds. A claim is *stated* when the competitor asserts it about itself in public and you have not confirmed it. A claim is *inferred* when you concluded it yourself by reading signals. A claim is *verified* when real evidence confirms it. For competitor work this balance leans hard toward inferred and verified-from-public-signal, because you cannot ask the rival anything, and the single most damaging mistake is laundering your own inference about a rival into a settled fact. Mark inferences as yours and say what they rest on.

**A count is not significance.** When something recurs across the competitor's surfaces, a raw count means little on its own. What gives it meaning is how widely it recurs relative to what you looked at. Before you call a self-presentation a consistent identity, weigh how consistently it actually showed up across the rival's surfaces, and state your read.

**A blank beats a guess.** When something is not present anywhere you can find it in the competitor's public materials, leave it blank and say so. Never fill a gap with a plausible invention, because a confident fabrication about a rival is indistinguishable from a real finding to the next reader and poisons every comparative move built on it. A meaningful absence is often the finding itself: a competitor with no stated mission or no founder presence is telling you something about how it is built.

**Know where each thing came from, and carry it.** Almost everything here is reconstructable from sources the competitor owns or has put into the world. For every claim, carry the public surface it came from, so a later reader can return to it and weigh it. A claim is only as trustworthy as its source.

**Confidence.** Where it helps a reader weigh a claim, mark it strong, mixed, or thin, judged against what is publicly available for this competitor, not an absolute bar.

**Form.** Do not use parenthetical asides. Work the qualifier into the sentence or cut it. Do not describe what to capture by listing brand-specific examples to copy. Naming what to look for, like the competitor's voice or its certifications, is what you should do.

## What this doc is, and why it matters

This is the competitor's picture of itself, rebuilt from the outside. It is not the brand's picture of the competitor, and it is not the truth about the competitor as its buyers experience it. It is what the rival presents about who it thinks it is, reconstructed from the public surfaces it controls, and then read for what that presentation reveals about the brand's own opportunity.

It matters for a few core reasons.

First, you cannot understand the field without understanding how each rival has decided to show up. A competitor's stated positioning is the lane it has chosen, and knowing the lane each rival has taken is what lets the brand find the lane no one is occupying. Read enough rival self-conceptions and the shape of the open ground emerges.

Second, the read here is critical, never admiring. The point of reconstructing a rival's identity is not to be impressed by it. It is to locate where the rival has committed hard to a positioning, where it holds credible ground, and where its self-presentation is weaker or fuzzier than it thinks — all as facts about the rival. A rival that leans its whole identity on a single message is running a fragile, single-point positioning, and naming that fragility is this doc's job. What the brand does with that — leans into the opening, goes at it directly, or leaves it alone — is the competitor-snapshot's call, not this doc's.

Third, the origin and channel story is one of the few things about a rival that genuinely shapes everything downstream and is hard to learn anywhere else. Whether a competitor began in retail or direct online predicts how it acquires, how it advertises, and where it is structurally strong or weak, so reconstruct it as far as the public record allows, and where it is unrecoverable, name that plainly.

One discipline runs through the whole doc and is the hardest part of the job. You are working entirely from the outside, with no way to confirm anything with the competitor, so the temptation to fill in a coherent identity the rival has not actually earned is constant. Resist it. Where the competitor's self-presentation is sharp, record it sharply. Where it is fuzzy or scattered across its surfaces, present it as fuzzy, because the fuzziness is accurate information about where the rival stands. Never tidy a rival into more coherence than its public materials show.

## Where to look, and how to reconstruct it

Work from the surfaces the competitor owns or has put into the world about itself, because this doc is the competitor on the competitor, rebuilt from the outside. Read each of these and carry where each claim came from:

- The competitor's home page and its about or our-story page, for the plainest statement of who it says it is.
- The product and collection pages, for how it frames what it sells and against what.
- The mission, values, and impact or sustainability pages, if present, and note their absence if not.
- The press, as-seen-in, and awards section the competitor displays about itself.
- The FAQ and any education or how-it-works content, for how it sounds and what it claims.
- Founder interviews, podcast appearances, and press the competitor itself points to, for the origin and channel story, since this is where a retail-first or DTC-first beginning usually surfaces.
- The competitor's own social profiles, read here only for how the rival describes and presents itself, since the deep organic read is a sibling doc.

Where a source does not exist, note it, because a competitor with no founder presence or no stated mission is itself telling you how it is built. Read the competitor on its own terms first, before you have absorbed the crowd's verdict on it, since that lives in the reputation and community docs.

## What goes in it

Capture each of the following from the competitor's own public surfaces, reconstructed from the outside, and read each comparatively for what it reveals about the brand.

**What the competitor presents itself as.** The plainest statement of the rival's business: the category, the core of what it offers, and how it positions itself. Capture how the competitor itself describes what it is and what it does for someone, and how it frames itself against the alternatives a buyer already knows. Then add the positioning read: what lane has this rival committed to, and where that commitment is solid or exposed — as an observation about the rival, not a move for the brand. If the rival's own positioning is scattered or unclear across its surfaces, present it that way rather than resolving it into something sharper than the rival has earned.

**Founder and origin story, and the channel story.** Where the competitor came from and how it began, reconstructed from public interviews, press, and its own telling. Capture the origin and, importantly, the channel story of whether the rival began by being discovered in stores or by selling directly online, since that single fact predicts much of how it acquires and advertises and is hard to learn any other way. Capture whether the founder is a visible, recurring presence in the rival's public content or absent from it, since an absent founder is itself a structural read. Where the public record does not establish the origin, mark it as unrecoverable from the outside rather than inventing a plausible story.

**Claimed audience.** Who the competitor says it is for, in the competitor's own public terms. Capture only the audience the rival itself claims, marked clearly as the rival's claim rather than as who actually buys from it. Do not build personas here and do not infer a rich buyer the rival has not stated, because the real read of who buys from this competitor is the customer-and-persona-discovery sibling doc, built from public buyer signal. If the rival claims many different audiences, capture that breadth as stated, since how wide or focused a rival's own sense of its audience is, is exactly the kind of self-conception this doc records.

**Tone and voice.** How the competitor sounds in its own public language. Capture the rival's own description of its voice if it offers one, kept close to its exact wording, and capture a representative line or two of the rival's actual public copy so the voice is shown rather than labeled. This matters comparatively, because a later step deciding how the brand should sound against this rival needs the rival's actual register grounded, not paraphrased.

**Credibility markers.** The press, awards, certifications, active partnerships, and collaborations the competitor puts forward as its validation. Capture what the rival claims, and note plainly which markers are owned by the rival and which are borrowed from a partner, and which are genuine third-party recognition versus routine mentions, since those are facts about the markers rather than judgments. The read that matters here: a rival leaning heavily on a single borrowed credibility marker has a fragile, single-point-of-failure validation.

**Website and brand identity beyond words.** What the competitor's site presents about who it thinks it is beyond the copy: the register, the aesthetic, and the kind of customer it visually speaks to. Describe what the site actually presents. Where the visual identity and the stated identity point in different directions, record both as you observed them rather than resolving the difference, since a mismatch in a rival is a tell.

## Output

Open with frontmatter, then the sections, using these headers. Do not pad each section with a restatement of the instructions above. Bring the competitor's reconstructed self-presentation forward under each, mark every claim verified, inferred, or stated, and close each with the positioning read — where the rival is committed or exposed — where it earns one. The brand-facing comparative judgment is the competitor-snapshot's, not this doc's.

```markdown
---
brand: [brand-slug]
competitor: [competitor-slug]
doc: competitor-brand-identity-analysis
generated_on: YYYY-MM-DD
refresh_by: YYYY-MM-DD
sources_read: [the competitor's public surfaces you actually read]
---

# Competitor brand identity analysis — [Competitor Name], for [Brand Name]

## What the competitor presents itself as

## Founder, origin, and channel story

## Claimed audience

## Tone and voice

## Credibility markers

## Website and brand identity

## Open loops

## Appendix - Parker media links
```

Mark anything that is your own inference rather than a verified public claim, and leave a clean named blank wherever a source does not exist rather than a guess.

## Open loops

End with the few consequential questions the competitor brand-identity reconstruction could not resolve.

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

Doc-specific thinking lens. Loops on this audit cluster around tensions between what the rival presents and what its other surfaces actually show — a stated mission that no recent creative carries, a claimed audience that the imagery and language miss, a credibility marker the rival leans on that is borrowed and fragile. The audit stays observational on the competitor; the loops surface the open question the rival's identity raises for the brand's strategy, in the open form the rubric requires — never a directive about what the brand itself should do.

Loops do not cover: missing public sources or thin reconstruction surfaces. Those belong in the frontmatter's sources_read field as named gaps.

Mark any loop only the brand can answer so it routes to the brand.

## When you refresh this

A competitor's identity drifts as it repositions, gets acquired, changes founders, or shifts channels, so the right read today may be wrong in a quarter. This doc is re-run on a quarterly cadence. When you rebuild it, take the previous version in as context first, carry forward what still holds, update what the rival has changed about how it presents itself, and say what each open loop's status is now. Watch especially for a change of ownership or a repositioning, since either can make stale public material actively misleading. Do not regenerate from a blank page, because that wastes the prior work and drifts in the retelling.
