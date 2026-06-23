# Spec — global AI-tagged ads database

This specifies `global-ai-tagged-ads-db`, the cross-brand library of ads Parker has read, evaluated, and tagged so they can be searched, recombined, and surfaced as references across every brand Parker serves. The database is continuous capture and quarterly curate. Entries are atoms — visual hook, messaging, full concept, CTA — each tagged so they can be filtered, mixed across types, and gated by lane relevance per brand at retrieval time.

Doc type: global database spec plus capture and curate prompts. Scope: every ad Parker reads across every brand's external audit. Cadence: capture is continuous, curate is quarterly.

---

## Purpose

The global AI-tagged ads DB exists because a strategist's edge is cross-account pattern memory — recognizing a pattern that worked on another brand and judging it portable into the current one. A single strategist accumulates this memory through years of reading accounts; Parker accumulates it by reading every ad it encounters and tagging it for later retrieval. Three jobs the database does:

1. **Power reference retrieval for scriptwriting and iteration.** When the scriptwriting skill runs its `find-reference-ads` process or the iterations skill runs `frankenstein-stitch` or `mashup`, the database is the surface they search. Without it, every reference lookup starts from scratch.

2. **Enable cross-account pattern memory with a lane-relevance gate.** A pattern that worked for a household-cleaning brand might or might not port into a feminine-care brand. The database stores the pattern with enough context that the gate can be applied at retrieval, not at capture.

3. **Recombine atoms across types.** A visual hook from one ad, a messaging angle from another, and a CTA from a third can be mashed into a new concept. Storing whole concepts only makes recombination impossible. Storing atoms makes it routine.

The database is brand-agnostic at capture and brand-aware at retrieval. The capture prompt evaluates and tags; the lane-relevance filter runs at retrieval time per brand.

## Storage and access

The database lives inside Parker. It is not a file on the local filesystem and skills must not look for it at any path on disk. Capture, curate, and retrieval all run through Parker MCP via `askParkerAgent`, passing the active `brand_id` and a tag-formatted query. Skills that need references — scriptwriting's find-reference-ads, iterations' frankenstein-stitch, mashup, hook-iteration, messaging-angle-iteration, ai-ad-generation — query Parker; they do not search the filesystem. The schema below is the contract Parker enforces on entries. The capture and curate prompts are what Parker runs against incoming ads and the existing pool.

## Schema

Each entry carries the following fields. The schema is the contract between the capture prompt and the retrieval surface.

- **source_url** — the persistent URL to the ad in its public surface. Mandatory. Without it the entry is unrecoverable for re-reading.
- **parker_media_links** — every Parker media link, media file path, thumbnail path, video URL, ad-library link, post link, source URL, or media reference available for the ad. Preserve each link or path exactly. If no Parker media links or media references were available for the entry, write `No Parker media links were available for this entry.`
- **brand_slug** — the brand the ad belongs to.
- **brand_category** — the product or service category the brand operates in. Drives the lane-relevance filter.
- **idea_type** — one of: visual hook, messaging, full concept, CTA. Atoms are filterable by type so a search can pull just visual hooks across categories.
- **format** — static, video, carousel, UGC-style, branded-studio, partnership. Multiple tags allowed where mixed.
- **funnel_stage** — unaware, problem-aware, solution-aware, brand-aware, most-aware. Inferred from the destination, the awareness level the copy assumes, and the call to action.
- **awareness_stage** — separate from funnel: how aware the ad's audience needs to be of the category itself for the ad to land.
- **persona_signal** — the customer archetype the ad reads as built for, in customer-side language not category jargon. Held as signal, not as defined persona.
- **emotional_driver** — what the ad reaches for emotionally — relief, validation, aspiration, fear, belonging, status. Single primary plus secondary where dominant.
- **storytelling_archetype** — problem-then-solution, transformation, day-in-the-life, testimonial, founder-monologue, listicle, demonstration.
- **objection_handled** — the category objection the ad addresses, in customer-side language. Optional.
- **reason_why_saved** — one to three sentences naming the pattern the entry exemplifies and why it earned a place. This is the field that protects against the database becoming a pile of every ad Parker reads. Mandatory.
- **confidence** — strong, mixed, or thin, judged against how cleanly the ad exemplifies the pattern.
- **capture_date** — when the entry was created.
- **last_curated** — when the entry was last reviewed in a curate pass.
- **related_entries** — the IDs of other entries this ad pairs naturally with, populated during curate, not at capture.

## Capture prompt

Run whenever Parker reads an ad in the course of any external audit or any other surface. The capture prompt decides whether the ad enters the database and what tags to apply.

You are evaluating one ad for entry into the global AI-tagged ads database. Three disciplines hold.

**The pattern, not the ad.** An ad earns entry because it exemplifies a pattern worth retrieving later, not because it exists. A merely competent ad with no distinctive pattern does not enter. Reach for the reason-why-saved field early: if you cannot state in one to three sentences what pattern this ad exemplifies and why it would be useful at retrieval time, do not save it.

**Atoms over whole concepts.** Before saving as full concept, ask whether the visual hook or the messaging is the durable part and whether saving just the atom would serve recombination better. A full concept entry is for ads where the whole construction is the pattern. A visual hook entry is for ads where the opening is the pattern and the rest is replaceable. The same ad can spawn multiple atom entries.

**Preserve the media handles.** Fill `parker_media_links` with every Parker media link, media file path, thumbnail path, video URL, ad-library link, post link, source URL, or media reference that came with the ad. Preserve the original link or path exactly. If none were available, write `No Parker media links were available for this entry.`

**Tell the research story and carry the evidence picture.** Treat the saved entry as context another LLM or strategist may read without reopening the ad. The entry should show what was reviewed, what pattern was seen, why that pattern is worth saving, what source details support it, and what uncertainty remains. For visual sources, the source_read and reason-why-saved together should let the reader picture the ad, understand the reusable pattern, and see why the tag choices were earned.

**Mark how you know each tag.** The funnel stage, persona signal, and emotional driver are inferred from the ad's content; mark them as inference. The format, the source URL, the brand, and any exact media handles are verified when they come from Parker source data.

Walk the schema and fill each field. The reason-why-saved field is the gate: if it is weak, the entry does not save. Confidence is judged against how cleanly the ad exemplifies the pattern, not against how much you like the ad.

Output the entry in the schema's shape, ready for insertion into the database.

## Curate prompt

Run quarterly across the database. The curate prompt reviews entries, prunes drift, recombines by tag, and surfaces boards Parker can hand to the brand work.

You are running the quarterly curate pass on the global AI-tagged ads database. Three jobs.

**Prune drift.** Walk entries last curated more than two quarters ago. For each, check whether the reason-why-saved still holds — the pattern is still durable, the ad still exists at its source URL, the tags still read correctly. Entries whose pattern has been overrun by category saturation, whose source has died, or whose tags now read poorly get archived with the reason. The database stays sharp by losing weight on a cadence.

**Recombine by tag.** Surface clusters of entries that share a tag and were not previously linked. A cluster of visual hooks all tagged transformation in the problem-aware funnel stage is a board candidate. A cluster of messaging entries all tagged with the same emotional driver across different categories is a borrow candidate. Populate the related_entries field on each entry in the cluster.

**Surface boards.** From the clusters, surface two to four named boards per quarter that Parker can hand into the brand work — for example, a board of problem-aware visual hooks for hygiene categories, a board of transformation archetypes across personal-care, a board of objection-handled CTAs for high-price categories. Each board carries the entries it includes and the lane it serves.

Output the curate-pass report: entries archived with reasons, clusters surfaced with the related-entries populated, boards surfaced with their entries and lane.

## Usage hooks

The database loads into several Parker skills at retrieval time. The lane-relevance filter runs per brand at retrieval.

- **`/Users/jimmyslagle/Parker-skills/skills/scriptwriting/processes/find-reference-ads.md`** — the scriptwriting skill's reference-pulling process queries the database by persona signal, funnel stage, and emotional driver, then filters by brand-category lane relevance for the current brand. The reason-why-saved field is what the strategist reads to decide whether an entry is borrowable.
- **`/Users/jimmyslagle/Parker-skills/skills/iterations/processes/frankenstein-stitch.md`** — the iterations skill's stitch process pulls visual-hook entries and messaging entries separately and recombines them, gated on lane relevance. The atoms-over-whole-concepts capture rule is what makes the stitch possible at all.
- **`/Users/jimmyslagle/Parker-skills/skills/iterations/processes/mashup.md`** — the iterations mashup process pulls across categories deliberately, using the database's brand-category field to find far-field borrows worth testing in the current brand's lane.
- **`/Users/jimmyslagle/Parker-skills/skills/iterations/processes/hook-iteration.md`** — pulls visual-hook entries filtered by funnel stage and emotional driver.
- **`/Users/jimmyslagle/Parker-skills/skills/iterations/processes/messaging-angle-iteration.md`** — pulls messaging entries filtered by persona signal and objection handled.
- **`/Users/jimmyslagle/Parker-skills/skills/ai-ad-generation/`** — generation skills query the database for archetypes and persona signals to ground generation in real ad patterns.

The lane-relevance filter is not a hard exclusion. A far-field borrow flagged with the lane delta noted is sometimes the highest-leverage retrieval. The retrieval surface should let the strategist override the filter and see the cross-lane match.

## Open loops

Think like a strategist. Ask like a smart 13-year-old. These are database architecture questions, not creative strategy questions. Keep them plain: what does Parker not understand yet, why does it matter, and what decision would change if the team answered it.

- How strict should the lane-relevance filter be when a brand searches outside its category?
- How does the team decide whether to save the reusable atom of an ad or the full concept?
- How does Parker keep the reason-why-saved field sharp when capture volume gets high?
- How should Parker normalize persona-signal language across brands without losing the customer's original words?
- If a source URL dies, what fallback should Parker store so the entry remains usable?
