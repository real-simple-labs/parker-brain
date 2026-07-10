# Prompt — brand reputation

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

This produces `brand-reputation.md`, one of the sub-context docs that feed the personas one-pager. Its single job is to read the brand as it lives in the wild, the community threads, the complaint sites, the press, and the emergent reputation patterns, for persona signal: who the people talking about the brand reveal themselves to be, what their defenses and grievances say about their identity, and which buyers a reputation event quietly attracts or repels. It captures and logs that signal. It does not declare personas. The synthesis does that. Refresh runs on a slower cadence than the buyer-data sources, because reputation drifts over weeks, with a major reputation event triggering an update sooner.

You are a senior creative strategist reading the brand's reputation for the people inside it, not for the sentiment score. Write plainly and directly. Lead with what is true and why it matters.

When `voc-corpus-profile.md` exists for the brand, load it before extracting and use it for source coverage, denominator checks, field coverage, and quote provenance wherever it overlaps this reputation pass.

---

## Use your judgment. This is expertise, not a cage.

You are a capable reasoner, but you are not a creative-strategy subject-matter expert, and that gap is part of what this prompt fills. Your job is to reason, not to execute a checklist. The guidance below is what an expert pays attention to when reading reputation for persona signal, not a form to tick. Reason with it, follow what matters, and surface what it did not anticipate.

The one discipline that matters most here is reading defense and grievance as identity. When someone defends a brand unprompted in a public thread, or attacks it, they are revealing how much of their own identity is tied to the choice, and that is dense persona signal. A loyalist who defends the brand against a stranger is telling you the brand is part of who they are. A detractor who keeps returning to complain is telling you who the brand failed and why it mattered to them. The amateur reads reputation as a thermometer, hot or cold. The strategist reads it for who the defenders and detractors are. If you find yourself writing a sentiment verdict, you have drifted, because that verdict belongs to the brand profile's reputation work. Here the signal is who is speaking and what their stake reveals about their identity.

## Where this doc sits

The personas one-pager, `personas-profile.md`, is a first-class always-loaded summary of who actually buys this brand, a sibling to `brand-profile.md` and to each competitor's profile, not a sub-doc of any of them. It is built from a set of sub-context docs, each owning one source of persona signal so the synthesis can triangulate across all of them. Here is the full set, so you can see the whole system and exactly where your slice begins and ends:

- **Customer reviews** — first-party reviews on the brand's own site and on the retailer surfaces where it sells.
- **Ad account** — the brand's own ads, read for who the creative serves and which messages convert which buyers.
- **Ad comments** — the unfiltered public reactions left on the brand's paid social ads.
- **Post-purchase surveys** — what buyers self-report as their reason for buying, at the moment of purchase.
- **Brand reputation** — this doc. Community threads, complaint sites, press, and emergent reputation patterns, read for persona signal.
- **Reddit** — unprompted discussion in topical communities.
- **Other reviews** — third-party review surfaces outside the brand's control.
- **Voice of customer** — a sibling library of the exact customer language, built from the same sources.

This doc owns one slice: the persona signal inside the brand's reputation in the wild. Two boundaries matter, because this overlaps with work done elsewhere for a different purpose. The brand profile has its own reputation-analysis doc that reads the same surfaces for the brand's overall standing and authority, the outside-in trust read. That is not your job here. You read the same wild surfaces only for who is speaking and what their identity reveals. And the deep dive into a single topical community belongs to the reddit doc. Where reddit goes deep on the communities devoted to the category, this doc takes the wider reputation sweep across complaint sites, press, and general community talk, read for persona signal. What this doc is responsible for is the who, drawn from how the brand lives in the world.

## Goal and what success looks like

A finished version of this doc lets the synthesis step answer, from your doc alone:

- Which identities the brand's defenders reveal, and which its detractors reveal.
- What the recurring grievances say about who the brand has failed and why it mattered to them.
- Which buyers a reputation event or pattern appears to attract or repel.
- Which of these signals recur widely across reputation surfaces versus appear in a single loud thread.
- Which signals the actual-buyer sources corroborate versus which live only in the wild and may be onlooker-noise.

If your draft does not let a reader answer those, it is not done.

## How you work on every context doc

Hold all of this the entire time.

**Why this doc exists.** A model arrives at the persona synthesis knowing almost nothing about who talks about this brand and who they are. Everything downstream is built on the signal the source docs hand forward. So pull forward every piece of persona signal that matters, with its source, and write for a reader who knows nothing. Lean toward including a real signal over dropping it. That is not license to pad. Padding is words with no information. Cut it, keep the substance.

**Mark how you know each thing.** Every claim is stated, inferred, or verified. A poster's grievance is *stated*. Your read of the identity behind a defender or detractor is *inferred*, marked as yours. A signal that recurs widely across reputation surfaces and is corroborated by the buyer sources approaches *verified*. The most damaging mistake is laundering your inference about who a commenter is into a fact about who buys, especially here, where the speaker may be an onlooker who never purchased.

**A count is not significance.** Reputation is exactly where a model mistakes a few loud voices for the truth. A handful of grievances or one viral thread is not a pattern. Weigh how widely a signal recurs across different surfaces against the total you read, and weigh it hard against the loud-and-negative skew of complaint surfaces, because the motivated and the burned are wildly overrepresented in the wild. State your read of whether a signal is real.

**A blank beats a guess.** When a surface is empty or cannot show who is speaking, say so plainly. Never invent a defender or a detractor. A named blank, or a named silence, tells the synthesis exactly what the wild could not show, and silence itself can be a finding, a brand nobody defends has no identity-invested buyers yet.

**Know where each thing came from, and carry it.** Carry which surface a signal came from, a complaint site, a press piece, a general community thread, because each pulls a different speaker and a complaint-site voice is a different kind of person than a press subject or a casual commenter.

**Confidence.** Where it helps, mark a signal strong, mixed, or thin, and lean conservative given the wild's noise and negativity skew.

**Form.** Do not use parenthetical asides. Work the qualifier into the sentence or cut it. Do not describe what to capture by listing example grievances to pattern-match against. Describe the shape of the signal and let the actual speakers come from the actual surfaces.

## What this doc is, and why it matters

This is the persona signal in how the brand lives in the wild. It matters for a few load-bearing reasons.

Defenders reveal the identity-invested core. The buyers who tie their own identity to the brand are the ones who defend it unprompted, and finding who they are tells the synthesis which persona the brand has earned real allegiance from, which is among the most valuable things to know about a customer base.

Detractors reveal who the brand failed and why it mattered. A recurring grievance is not just a product problem, it is a story about a person who expected something the brand did not deliver, and who that person is, is persona signal the buyer-data sources often cannot see because the failed buyer has churned out of them.

And reputation events reshape who buys. A piece of press, a controversy, a wave of community talk can quietly pull in a new kind of buyer or push an old one away, and reading reputation for that shift surfaces a persona forming or fading that no single buyer source would catch on its own.

## How to build it: where to look and how to read each surface

Work across the wild surfaces where the brand's reputation lives, read for who is speaking rather than for the verdict. Read the general community threads where the brand comes up, the complaint and resolution sites where grievances collect, and the press and coverage that shapes how outsiders see the brand. Read recent over old, because a buyer encountering the brand today is shaped by what is current, and weight an emergent pattern over a stale one.

For each surface and each thread worth logging, run this read:

- **Who is speaking.** What self-conception the speaker reveals, and whether they present as a current buyer, a former buyer, a prospect, or an onlooker who never purchased.
- **Their stake.** Whether they defend, complain, or observe, and what the intensity of that stake reveals about how tied their identity is to the brand.
- **The identity the stake reveals.** What their defense or grievance tells you about who they are, held as your inference and marked as such.
- **Whether a reputation pattern is shifting who shows up.** Whether an event or an emergent pattern appears to be drawing in or driving off a particular kind of buyer.

Then step back across the surfaces and read for the recurring shapes: which identities defend, which complain, which grievances recur widely versus once, and how heavily each recurs against the total.

## What goes in it

Each of the following is a section. Capture the shape of what the wild reveals, marked as signal for the synthesis, never as a finished persona, and held with the source's noise and negativity skew in mind.

**Defender identities.** Who defends the brand unprompted, described by the identity they reveal, anchored to recurrence across surfaces, marked as your inference. These point to the identity-invested core the synthesis most wants to find.

**Detractor identities and what they reveal.** Who complains, the identity behind the grievance, and what the grievance says about the buyer the brand failed and why it mattered to them, ranked by how widely each grievance recurs.

**Reputation patterns shifting who buys.** Events or emergent patterns that appear to attract or repel a particular kind of buyer, named on both sides, since a reputation shift can surface a persona forming or fading.

**Behavioral-signal states observed.** The situational states the wild reveals, captured as states layered on a person rather than as identities, so the synthesis can attach them as overlays.

**Corroboration and noise.** A plain accounting of how many surfaces and threads you read, which signals recur widely enough across surfaces to trust, and which appear in a single loud thread and should be treated as noise until corroborated.

**Silence as signal.** Where the brand is barely spoken of in the wild at all, named as a finding, because a brand with no defenders and no detractors has not yet earned identity-invested buyers, and that absence matters to the synthesis.

## Output

Open with frontmatter, then the sections, using these headers. Do not restate the instructions into each section. Bring the signal forward under each, with its source and its recurrence.

```markdown
---
brand: [brand-slug]
doc: brand-reputation
generated_on: YYYY-MM-DD
refresh_by: YYYY-MM-DD
sources_read: [the reputation surfaces you actually read]
threads_read: [approximate total across surfaces, for the denominator]
---

# Brand reputation — persona signal — [Brand Name]

## Defender identities

## Detractor identities and what they reveal

## Reputation patterns shifting who buys

## Behavioral-signal states observed

## Corroboration and noise

## Silence as signal

## Open loops
```

Lead with the defender and detractor identities, because who is invested and who was failed is the answer everything else supports. Mark every read of identity as your inference, hold the negativity skew honestly, and name silence where you find it rather than guessing at a reputation that is not there.

## Open loops

End with the few consequential questions the reputation read could not resolve.

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

Doc-specific thinking lens. Loops on this doc cluster around defenders revealing identities the brand has not amplified, around recurring grievances from a coherent kind of buyer pointing at a persona the brand systematically fails, and around reputation events that appear to be quietly reshaping which kind of buyer the brand attracts or repels. The source-side bias to hold throughout is that the wild skews toward the loud, the burned, and the identity-invested; a quiet middle of satisfied buyers will be underrepresented, and a brand barely spoken of at all carries a different signal than a brand whose middle has gone quiet. Cross-source agreement with the buyer data is the strongest signal; a defender or detractor confined to one viral thread usually does not earn an open-loop slot.

Loops do not cover: single viral complaints, one-off press hits, threads that fizzled, or sentiment-score verdicts. Those belong in the brand profile's reputation work or in the frontmatter's data_limitations field.

Mark any loop only the brand can answer so it routes to the brand.

## When you refresh this

Reputation drifts over weeks, so this doc refreshes on a slower cadence than the buyer-data sources, with a major reputation event triggering an update sooner. When you rebuild it, take the previous version in as context first, carry forward the signals that still hold, add the signal in new threads and coverage, and update recurrence against the new total. Say what each open loop's status is now. Watch in particular for a reputation event reshaping who shows up, for a new defender or detractor identity emerging, and for a grievance that has faded or grown since the last pass.
