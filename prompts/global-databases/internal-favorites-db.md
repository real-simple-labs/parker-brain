# Spec — internal favorites database

This specifies `internal-favorites-db`, the team-curated gold-standard reference set. Where the global AI-tagged DB captures broadly and the Parker favorites DB codifies what Parker reaches for, the internal favorites DB captures what the human team has hand-selected as the durable reference set — the ads the strategists themselves point to when teaching, scoping, and concepting. It is the team's institutional taste, made retrievable.

Doc type: global database spec plus capture and curate prompts. Scope: ads the team has selected, with a written reason-why-saved attached by a human. Cadence: capture is event-driven on save, curate is quarterly.

---

## Purpose

The internal favorites DB exists because Parker's pattern memory and the team's pattern memory are not the same thing. The team carries strategist-level taste that includes things Parker has not yet learned to value — a specific shot construction the strategists know lands across categories, a hook the team has watched outperform in five accounts in a row, a creator format the team has validated. This database is where that human taste is stored, with the mandatory reason-why-saved that protects the set from becoming a personal moodboard.

Three jobs the database does:

1. **Capture team-level taste before it leaves with a strategist.** A senior strategist's pattern memory is the team's most fragile asset. Codifying it in an entry with reason-why-saved is the durability layer.

2. **Anchor scoping and concepting conversations.** When the team is scoping a new engagement or concepting a campaign, the internal favorites DB is the surface they hand to each other. It is the team's shared vocabulary of what good looks like.

3. **Train Parker against the team's taste over time.** As Parker reads entries with their reason-why-saved, the team's taste becomes part of the context Parker can reason against. Internal favorites entries are higher-signal training material than global DB entries because they carry an explicit human judgment.

The discipline: reason-why-saved is mandatory and is written by a human, not generated. An entry without a human-written reason-why does not enter. This is the gate that separates the gold-standard set from a casual save.

## Storage and access

The database lives inside Parker. It is not a file on the local filesystem and skills must not look for it at any path on disk. Capture, curate, and retrieval all run through Parker MCP via `askParkerAgent`, passing the active `brand_id` and a tag-formatted query. Skills that need references search Parker; they do not search the filesystem. In the tiered retrieval order — internal favorites, Parker favorites, global AI-tagged DB — this database is the top tier. When a query returns a strong match here, search stops and the entry is used.

## Schema

Each entry carries the global DB schema plus four additional fields. The internal favorites entries are also in the global DB; this database is the human-curated subset.

- All fields from `global-ai-tagged-ads-db` — source URL, Parker media links, brand slug, brand category, idea type, format, funnel stage, awareness stage, persona signal, emotional driver, storytelling archetype, objection handled, confidence, capture date, last curated, related entries.
- **reason_why_saved** — mandatory, written by the saving team member in their own words, one to four sentences naming the pattern the entry exemplifies and why the team should keep this reference. The required field. An entry without a human-written reason_why does not save.
- **saved_by** — the team member who saved the entry. Carries accountability for the saved-by judgment when the curate pass reviews.
- **teaching_use** — the contexts the entry is useful for in the team's work — scoping, concepting, persona teaching, hook reference, format reference. Multiple tags allowed.
- **internal_rating** — strong, mixed, or thin, judged by the saving team member against the entry's exemplary quality. Mixed and thin entries are reasonable, but they should carry a sharper reason_why to earn their place.

## Capture prompt

Run when a team member saves an entry to the internal favorites DB. The capture prompt is light — it does not evaluate, because the human has already evaluated. It ensures the schema is filled, the reason_why is human-written and substantive, and the entry is checked into the global DB at the same time.

You are recording one entry the team has selected for the internal favorites database. Three disciplines hold.

**Reason-why-saved is the gate, and it must be human-written.** Confirm the field is filled and reads as substantive — not a single line of category-jargon, not a generated summary. If the field is weak, prompt the saving team member to sharpen it before the entry saves. The reason_why is what makes the entry a team asset; without it, the entry is a personal save.

**Saved-by is mandatory.** The accountability matters for the curate pass.

**Mirror the entry into the global DB.** The internal favorites set is a curated subset of the global DB. Every internal entry is also a global entry, so the global record is populated at the same time, with the same source URL, Parker media links, schema fields, and confidence mark. If no Parker media links or media references were available for the entry, write `No Parker media links were available for this entry.`

**Tell the research story and carry the evidence picture.** Treat the saved entry as context another LLM or strategist may read without reopening the ad or asking the saving team member. The entry should show what was saved, what the human reason_why says, what source details support that reason, what exact visual, hook, or message pattern is being preserved, and what uncertainty remains. Do not replace the human reason_why with Parker's summary, but do add enough source context for the reason to remain useful later.

Walk the schema, confirm each field, and output the entry ready for insertion into both databases.

## Curate prompt

Run quarterly. The curate pass for the internal favorites DB centers on the team — the entries get reviewed by the team that saved them, not by Parker alone. Parker's role is to surface candidates for review and to support the team's call.

You are supporting the quarterly curate pass on the internal favorites database. Three jobs.

**Surface candidates for human review.** Walk entries last curated more than two quarters ago. Flag entries whose source URL has died, whose reason_why now reads as out of date against the brand's strategy shift, or whose pattern has been overrun by category saturation. The team reviews the candidates and decides what to keep, archive, or update.

**Surface clusters by reason_why theme.** Group entries whose reason_why fields read as exemplifying the same underlying pattern, even if their tags differ. This is where the team-language curation adds value the tag-based curation cannot replicate, because the reason_why field captures human-written judgment the tags compress. Surface the clusters for the team to review and potentially codify as a named teaching board.

**Surface saved-by patterns.** Where one team member has saved a disproportionate share of entries in a particular pattern, surface that — the saving pattern is itself team intelligence about who has the strongest taste in which area, which the team can use to route review and concepting work.

Output the curate-pass report: candidates flagged for human review with the flag reasons, clusters surfaced by reason_why theme, saved-by patterns surfaced.

The team makes the final keep-archive-update calls. Parker does not archive an internal favorites entry without human review.

## Usage hooks

The internal favorites DB loads into Parker skills as a high-priority, human-vetted reference surface. The retrieval order across the three databases is: internal favorites first for human-vetted matches, Parker favorites second for Parker's codified patterns, global DB third for the long-tail search.

- **`/Users/jimmyslagle/Parker-skills/skills/scriptwriting/processes/find-reference-ads.md`** — searches the internal favorites DB first; a human-vetted match wins against anything else. The reason_why_saved field is what the strategist reads to decide whether the reference applies to the current brand work.
- **`/Users/jimmyslagle/Parker-skills/skills/iterations/processes/frankenstein-stitch.md`** — anchors stitches in internal favorites entries when available, since the human-written reason_why provides a clearer constraint on what to preserve in the stitch.
- **`/Users/jimmyslagle/Parker-skills/skills/iterations/processes/mashup.md`** — uses internal favorites as the safe seed for the mashup, since the human-vetted entries are higher-confidence ports.
- **`/Users/jimmyslagle/Parker-skills/skills/iterations/processes/hook-iteration.md`** — pulls internal favorites hooks first.
- **`/Users/jimmyslagle/Parker-skills/skills/iterations/processes/messaging-angle-iteration.md`** — pulls internal favorites messaging first.
- **`/Users/jimmyslagle/Parker-skills/skills/ai-ad-generation/`** — generation skills ground generation in internal favorites archetypes when they exist, falling through to Parker favorites and the global DB.
- **Scoping and concepting workflows.** The internal favorites DB is also a surface the team queries directly when scoping a new engagement or concepting a campaign, separately from Parker's automated retrieval.

The lane-relevance filter still applies, but internal favorites entries carry more weight at retrieval because the reason_why and the saved_by field carry human judgment Parker should defer to.

## Open loops

Think like a strategist. Ask like a smart 13-year-old. These are database architecture questions, not creative strategy questions. Keep them plain: what does Parker not understand yet, why does it matter, and what decision would change if the team answered it.

- Should a weak reason-why-saved entry block the save or warn the user?
- Should internal-rating and the global DB confidence field be reconciled or kept separate?
- Can Parker auto-archive dead-URL entries, or does every archive decision need human review?
- How does Parker make saved-by patterns useful without letting one team member's taste dominate the database?
- Who should manage the teaching_use tag vocabulary so it stays tight?
