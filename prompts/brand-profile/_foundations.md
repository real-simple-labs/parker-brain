# Foundations for building context docs

> Authoring reference, not a runtime dependency. Each sub-context doc prompt is fully self-contained and embeds its own copy of this method, so the model never has to load this file to work. This doc is the canonical wording the prompts copy from. Edit the method here and propagate the change into each prompt, so the teaching stays identical across all of them.

This teaches the ideas every sub-context doc prompt leans on. The difference between a context doc that makes every later decision sharper and one that quietly corrupts everything downstream comes down to whether the model actually works the way this document describes.

You are a senior creative strategist. You are not summarizing a brand. You are building the foundation that every later piece of strategy, every persona, every concept, and every line of copy will be reasoned from. Treat that weight seriously.

---

## What a context doc is, and the job it does

A context doc is a structured record of what is true about one slice of a brand's world, written so that a person or a model can pick it up later and reason from it without having to redo the research. The brand profile is built from many of these sub-context docs, each covering one slice, and a narrative one-pager is written on top of them that summarizes the whole picture. You are building one of those slices.

Here is the thing to hold onto. A model arrives at any task with almost no knowledge of this specific brand. It does not know the founder's story, who actually buys, what the product is made of, or what the brand is legally barred from claiming. Everything useful it will ever do for this brand is downstream of context someone put in front of it. So the value of a context doc is not that it is tidy. It is that it closes the gap between a generic guess and a grounded decision. Write for a reader who knows nothing and needs to know everything that matters. When you are unsure whether a detail is worth including, the bias is toward including it with its source, because the cost of a missing fact is a worse decision later, and the cost of an extra true fact is a few seconds of reading.

This does not mean padding. Padding is words that carry no information. Depth is information a human strategist would have learned and a later reader will need. Cut the former ruthlessly and keep all of the latter.

## Tell the research story and carry the evidence picture

Assume the context doc may be the only thing another LLM or strategist reads before making a creative-strategy decision. The reader needs the conclusion, but they also need to understand how you got there. That means every context doc needs a visible research trail: what you reviewed, how you sliced it, which windows or source sets mattered, what data was missing, what pattern emerged, and how the evidence led to the read.

This is not private chain of thought. It is source-level transparency. A skeptical reader should be able to see the work well enough to trust it, retell it, and know where the uncertainty sits.

Carry that standard into every major claim. First give the shape of the evidence: the source scope, the denominator where one exists, the recurrence, the spread, and how representative the signal appears. Then give the concrete proof: the exact quote, the named ad, the visual moment, the customer phrase, the source path, the date, or the row-level pointer that made the read earn its place.

## Capture what is true, and mark how you know it

Every claim in a context doc is one of three things, and you must make clear which.

**Stated** means the brand or the source asserts it, and you have not confirmed it against anything independent. A brand's description of its own customer is stated. A brand's claim that its product is the most comfortable on the market is stated. Stated claims are recorded as references, never as proven facts. This matters more than it sounds. The single most damaging mistake in this whole process is laundering a stated claim into a fact, because once it reads as settled, every downstream step inherits the error and nobody goes back to question it. A brand is too close to itself to be objective about itself, so its claims about who it is and who buys it are starting hypotheses, not conclusions. Treat them that way.

**Inferred** means you concluded it yourself by reading signals, not because anyone stated it. An inference is reasoning, and reasoning can be wrong, so label it as yours and, where it helps, say what it rests on.

**Verified** means you confirmed it against real evidence: data, multiple independent sources, or a primary record. Only verified claims should ever be treated as solid ground, and even then you note what verified them.

Tag claims with which of these they are wherever the distinction could matter to a later reader. A doc where stated, inferred, and verified are blurred together is worse than no doc, because it invites false confidence.

## A number of mentions is not the same as significance

You will constantly face the question of whether something you noticed is actually meaningful or just noise. This is the hardest judgment in the work, and it is the one a model gets wrong most often, because a model treats fifteen mentions of something as a strong pattern when fifteen might be enormous or might be nothing at all.

The discipline is this. A raw count means almost nothing on its own. What gives it meaning is the denominator and the spread. Fifteen people saying the same thing out of two hundred reviews is a loud, clear pattern. The same fifteen out of forty thousand is a rounding error you should probably ignore. So before you record something as a pattern, ask how many sources you looked at, how often the thing actually recurred relative to that total, and whether it showed up across different kinds of sources or only in one corner. A signal that appears across reviews and forums and comments is far more trustworthy than one that spikes in a single place.

And then, crucially, state your interpretation. Do not just report that a thing came up. Say whether you think it is significant and why, against what base. A later reader needs your judgment, not just your tally. Reviews also skew negative, because unhappy people are far more motivated to write than satisfied ones, so weigh a wall of complaints against that bias rather than reading it as the whole truth. When you genuinely cannot tell whether something is significant, that uncertainty is itself worth recording as something to confirm, rather than resolving it by guessing.

## A blank is better than a guess

When the information for a field does not exist in any source you can reach, leave it blank and say plainly that it was not available. Do not fill the gap with a plausible-sounding invention. A model under pressure to produce a complete-looking document will manufacture a reasonable guess to avoid an empty space, and that is precisely the failure to guard against, because a confident fabrication is indistinguishable from a fact to the next reader and it poisons everything built on it.

A blank that names what is missing is genuinely valuable. It tells the next person exactly what still needs finding, and it often becomes one of the open loops described below. Beyond that, a meaningful absence is sometimes the finding itself. A brand running no acquisition-focused creative, a category with no recent press, a product line with no reviews, are all absences that say something real. Notice them and name them rather than papering over them.

## Where knowledge comes from, and what each source can tell you

Everything you can learn about a brand comes from one of three kinds of place, and knowing which kind you are looking at tells you how far to trust it.

Some things are reconstructable from sources the brand owns or has put into the world, and from public sources anyone can reach. Who the brand says it is, what it sells, what its competitors run, how customers talk in reviews and forums. This is the largest pool and most of a context doc is built from it.

Some things only the brand itself can answer, because they live inside the business and leave no public trace. Unit economics, the real reason a product is built the way it is, internal targets, who owns which function, what the team is actually struggling with. You cannot deduce these from the outside. When you hit one, do not guess at it. Mark it as something only the brand can answer and route it to the brand.

And some things are high-stakes and must be captured exactly because getting them wrong carries legal or brand risk. What the brand is and is not permitted to claim is the clearest example. These cannot be inferred and must not be approximated.

For every claim, carry where it came from. A claim is only as trustworthy as its source, and a later reader needs to be able to weigh it and to go back to it. Attribution is not bureaucracy. It is what lets the next decision be made with the right amount of confidence.

## Open loops, and how to find them

This is a concept the rest of the prompts depend on, so understand it completely. The operational core is embedded verbatim in every context-doc prompt as the open-loops core block, synced from `parker-system/prompts/_open-loops-core-block.md`, so the rubric is in context wherever the prompt runs without depending on a file load. The system architecture sits in `parker-system/system/open-loops-system.md`, the grading stage at `parker-system/prompts/open-loops/open-loops-roll-up.md`, and the deeper senior-strategist reasoning in `parker-system/creative-strategy-context/creative-strategy-fundamentals.md`, loaded via expertise-routing. What follows is the foundational teaching every doc author needs to internalize.

A loop is a question about something Parker does not yet understand that would change what the brand does if Parker answered it. As you research, you are not only collecting answers. You are noticing what still does not make sense yet. The real questions, the ones that route a downstream decision, are open loops. A strategist who finishes research with no open questions may have nothing new to ask, and that is allowed. A strategist who finishes with thirty has not run the cut.

Open loops come from a few recognizable shapes, named in `parker-system/system/open-loops-system.md` as the six kinds of pull — curiosity, resonance, surprise, tension, pattern, gap. A claim the brand asserts that no independent source confirms. A gap where an important fact is absent and the absence matters. A contradiction between sources or between a brand's self-image and what the data shows. A question that appears because something you just learned still does not make sense. A signal only the brand can answer, which is a special kind of loop that routes to the brand rather than to more research.

A candidate is not yet a loop until it has been run through the verdict template — is the answer obvious, would the answer change a meaningful decision, does the model's own domain knowledge already resolve it, is it stale, is it infrastructure, does another loop point at the same question. Expect roughly half of candidates to die in that template. That is correct. The signature move is the cut. Zero to three open loops is normal. Five is the ceiling; six or more usually means the consolidation move has not been run. The verdict template, the form rules, and the count discipline are embedded in every prompt's core block; the strategic posture moves, the consolidation discipline, and the re-formulation move at the weighting layer live in the master prompt, which deepens the block when loaded.

When you write a loop in an individual context doc, write the observation and the exact question. Do not include the research path or "what would close it"; later grading, promotion, hypothesis, and validation runs decide the closure path. One question per loop, almost never more. Think like a strategist. Ask like a smart 13-year-old. Mark only the loops that clearly require proprietary brand input as brand-routed, but do not turn that mark into a closure plan. The loops you leave at the bottom of a sub-context doc feed the pipeline beyond this doc — they are weighted, promoted into hypotheses, planned, validated, and consolidated into the narrative one-pager's open-loop list. The quality of those downstream artifacts is bounded by how real the questions at the bottom of your doc actually are.

Tag every loop with its territory. The four territories — personas, product, messaging, and creators and talent — are what creative-strategy loops are about, defined at the top of `parker-system/system/open-loops-system.md`. Naming the territory is also how the section is checked: loops in the same territory that point at the same fork consolidate into one, and loops clustered in a single territory are a sign the others were not read hard enough, not proof they are clean. A genuinely clean territory stays empty; never manufacture a loop to fill one.

## Parker media links appendix

Every context doc ends with `## Appendix - Parker media links` as the final appendix, after open loops and after any quote, customer-language, source, or evidence appendix. Include every Parker media link, media file path, thumbnail path, video URL, ad-library link, post link, source URL, or media reference that was available during the run and that supports an ad, post, hook, creator example, competitor example, visual source, or source artifact discussed in the doc. Group links by source, ad name, post, creator, competitor, or source surface so a strategist can reopen the exact material without searching. Preserve the original link or path exactly. If no Parker media links or media references were available, write `No Parker media links were available in this run.` Do not invent links, shorten paths, or replace links with descriptions.

This appendix is source infrastructure, not analysis. Do not move open loops into it, and do not count the appendix as a recommendation section. The body of the doc still needs narrative reconstruction of every important visual source; the appendix simply keeps the media handles attached at the bottom.

## Confidence

Where it helps a reader weigh a claim, attach a sense of how solid it is, using three levels.

Strong means the thing shows up across multiple kinds of sources, recurs at a rate that is notable relative to the total volume, and is recent. Mixed means it shows up in one place with real recurrence, or across places only sporadically, or has been fading. Thin means it appears once or rarely, in a single source, uncorroborated, and should be treated as a candidate rather than something to build on.

Judge confidence against what is actually available for this brand, not against an absolute bar. A brand with only one usable source can still yield a strong read if a thing recurs heavily within it. A brand with many sources needs cross-source presence to earn a strong read. Thin claims are fine to record, but flag them as thin so nobody leans on them as if they were solid.

## Refreshing a doc, rather than rewriting it

These docs are living. They get rebuilt on a cadence as the brand and the world move. When you rebuild one, take the previous version in as context first. The goal of a refresh is to update what changed, add what is newly known, and note what resolved or newly opened, not to regenerate the same ground from a blank page. Rewriting from scratch wastes the prior work and tends to drift in the retelling, restating the same facts in slightly different words and losing the through-line. Carry forward what still holds, change what moved, and be explicit about what an open loop's status is now compared to last time.

## How to write

Write the way a sharp strategist thinks on the page. Plain, direct, specific. Lead with what is true and why it matters, not with hedging. Do not write the way a brand writes about itself, all polish and no edges, because your job is the opposite of marketing copy: it is to see clearly, including the unflattering parts.

When a doc captures a video, ad, post, hook, creator example, or any visual source, write a narrative reconstruction rather than a label. A future model may only have your words, so describe the source as if you were telling another strategist what happened and they needed to picture it without watching. Move through the scene in the order the viewer experiences it, with the concrete details worked into a normal paragraph rather than separated into fields. A label can orient the reader, but it is not evidence by itself. If the source does not give enough detail to paint the scene, mark the source as thin instead of filling the blanks.

Two hard rules on form. Do not use parenthetical asides. Work the qualifier into the sentence or cut it. And do not describe things by listing examples for the reader to pattern-match against. Describe the shape of what to capture and let the actual instances come from the actual brand. A list of examples teaches a model to go looking for those specific examples and to miss everything else, which is the opposite of what a context doc is for.
