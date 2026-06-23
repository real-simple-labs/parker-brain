# Spec — Parker favorites database

This specifies `parker-favorites-db`, Parker's own curated set of ads that exemplify specific patterns Parker uses repeatedly in its work. It is smaller, more opinionated, and more rigorously vetted than the global AI-tagged ads database. Where the global DB captures broadly to enable cross-account memory, this database captures narrowly to enable confident, high-frequency retrieval of the patterns Parker keeps reaching for.

Doc type: global database spec plus capture and curate prompts. Scope: ads Parker has used or proposed using across multiple brand engagements that exemplify a durable pattern. Cadence: capture is event-driven on use, curate is quarterly.

---

## Purpose

The Parker favorites DB exists because not every ad in the global DB is one Parker actually pulls. Across a year of brand work, a smaller subset of references gets used repeatedly — the visual hook that keeps working across categories, the messaging archetype that the strategist keeps reaching for, the format that lands in lane after lane. These are Parker's favorites, and surfacing them as a separate, opinionated set saves the retrieval surface from drowning the durable references in the long tail.

Three jobs the database does:

1. **High-frequency retrieval of proven patterns.** When Parker needs a reference fast and confidently, the favorites DB is the first surface searched. It is smaller, so the retrieval is faster and the strategist trusts the result.

2. **Codify Parker's own pattern memory.** The favorites set is the durable record of what Parker has learned works across brands. It is the institutional memory the global DB feeds into and the curate pass distills out.

3. **Enable the high-confidence override.** When the global DB returns a weak match and the favorites DB returns a strong one, the favorites entry wins. The opinionated curation is what earns that override right.

The discipline: a favorites entry must exemplify a pattern Parker has used or proposed using across multiple brand engagements. A first-use is candidate signal; a second-use across a different brand is the threshold for entry.

## Storage and access

The database lives inside Parker. It is not a file on the local filesystem and skills must not look for it at any path on disk. Capture, curate, and retrieval all run through Parker MCP via `askParkerAgent`, passing the active `brand_id` and a tag-formatted query. Skills that need references search Parker; they do not search the filesystem. In the tiered retrieval order — internal favorites, Parker favorites, global AI-tagged DB — this database is the middle tier.

## Schema

Each entry carries the global DB schema plus three additional fields. Entries in the favorites DB are also in the global DB; the favorites DB is the curated subset.

- All fields from `global-ai-tagged-ads-db` — source URL, Parker media links, brand slug, brand category, idea type, format, funnel stage, awareness stage, persona signal, emotional driver, storytelling archetype, objection handled, reason why saved, confidence, capture date, last curated, related entries.
- **use_history** — the list of brand engagements where Parker has used or proposed using this reference, with dates. Mandatory; a favorites entry without use history is not a favorite, it is a candidate.
- **pattern_codified** — the durable pattern this entry exemplifies, stated in one sentence in Parker's own language, brand-agnostic. This is the field that justifies the favorite status — what makes this reference Parker's go-to for this pattern.
- **override_strength** — strong, mixed, or thin, judged against how confidently Parker reaches for this reference when the pattern comes up. A strong override means the favorites entry wins against any global DB match for the same pattern.

## Capture prompt

Run when Parker uses or proposes a reference in a brand engagement for the second time across a different brand. First use is candidate signal that lives in the global DB; second use across a different brand is the threshold for promotion to the favorites DB.

You are evaluating one reference for promotion to the Parker favorites database. Three disciplines hold.

**Use history is the gate.** The entry must have been used or proposed across at least two different brand engagements. A single-use reference, no matter how strong, lives in the global DB until the second use validates it. Check the use history before anything else; if it is not there, the promotion does not happen.

**State the pattern codified, brand-agnostic.** The pattern_codified field has to read as the durable thing Parker keeps reaching for, in Parker's own language, with no brand-specific detail. If the pattern reads as brand-specific, the entry is a strong global DB entry, not a favorite. The favorite-status earns itself only when the pattern is portable.

**Mark the override strength honestly.** A strong override claim has to be defensible: when this pattern comes up, Parker reaches for this entry over any other. A mixed override is reasonable when the entry is one of several strong references for the pattern. A thin override does not earn favorite status; the entry stays in the global DB.

**Tell the research story and carry the evidence picture.** Treat the promotion as context another LLM or strategist may read without reopening the original entry. Show the use history, the cross-brand pattern that emerged, the source details that make the reference durable, and why Parker keeps reaching for it. The pattern_codified field should read like the conclusion, while the surrounding entry should show the evidence that earned the promotion.

Walk the schema and fill each field, leaning on the entry's existing global DB record. Preserve `parker_media_links` exactly from the source/global record. If no Parker media links or media references were available for the entry, write `No Parker media links were available for this entry.` Output the promotion in the schema's shape, ready for insertion into the favorites DB.

## Curate prompt

Run quarterly across the favorites DB. The curate prompt has tighter discipline than the global DB curate, because the favorites set lives or dies on staying small and sharp.

You are running the quarterly curate pass on the Parker favorites database. Three jobs.

**Demote drift.** Walk every entry. For each, check whether the pattern_codified still holds, whether the override_strength is still defensible, whether the use_history still reflects active reaching. An entry that has not been used in three quarters is a candidate for demotion back to the global DB, not because the pattern died but because Parker has moved past it. State the demotion reason.

**Tighten patterns.** Where two or more entries codify the same pattern, the favorites DB has duplication that needs resolving. Either the two entries exemplify the pattern at different funnel stages or for different personas — in which case the pattern_codified fields need sharpening to distinguish them — or one entry is the stronger reference and the other can be demoted.

**Surface boards Parker reaches for repeatedly.** From the favorites set, surface the two to four named boards that group the patterns Parker most often pulls in combination. These boards become the highest-confidence retrieval surfaces for the next quarter.

Output the curate-pass report: entries demoted with reasons, patterns tightened, boards surfaced with their entries.

## Usage hooks

The favorites DB loads into the same Parker skills as the global DB, with the override priority described above.

- **`/Users/jimmyslagle/Parker-skills/skills/scriptwriting/processes/find-reference-ads.md`** — searches the favorites DB first; if a strong-override match exists, it wins. Otherwise falls through to the global DB.
- **`/Users/jimmyslagle/Parker-skills/skills/iterations/processes/frankenstein-stitch.md`** — pulls the highest-confidence visual hook and messaging atoms from the favorites DB to anchor the stitch, then sources additional atoms from the global DB.
- **`/Users/jimmyslagle/Parker-skills/skills/iterations/processes/mashup.md`** — uses the favorites DB to seed the recombination with Parker's most durable patterns, then pulls cross-category candidates from the global DB.
- **`/Users/jimmyslagle/Parker-skills/skills/iterations/processes/hook-iteration.md`** — pulls visual-hook favorites as the first-pass reference set.
- **`/Users/jimmyslagle/Parker-skills/skills/iterations/processes/messaging-angle-iteration.md`** — pulls messaging favorites as the first-pass reference set.
- **`/Users/jimmyslagle/Parker-skills/skills/ai-ad-generation/`** — generation skills ground generation in favorites-set archetypes before reaching to the broader global DB.

The lane-relevance filter still applies. A favorites entry is high-confidence at retrieval but still subject to the lane gate per brand.

## Open loops

Think like a strategist. Ask like a smart 13-year-old. These are database architecture questions, not creative strategy questions. Keep them plain: what does Parker not understand yet, why does it matter, and what decision would change if the team answered it.

- When should a uniquely strong single-use reference be promoted before it reaches the two-engagement threshold?
- How does Parker keep pattern_codified phrasing consistent across engagements?
- When should override_strength be re-evaluated?
- Should the demotion threshold change by category lane?
- Should the curate pass enforce a hard ceiling on favorites so the set stays sharp?
