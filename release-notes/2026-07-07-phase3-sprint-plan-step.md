# 2026-07-07 Phase-3 sprint-plan step + sprints as the round container

Added the concept-planning layer that Phase 3 was missing. Between grading the pile and building briefs, a senior strategist sizes the round, splits it across SKUs and personas, sets variation counts, and maps every concept — the eight hours of a concepting session that was unencoded. Grounding source: multi-part June 2026 concepting transcripts of a senior creative strategist planning a full creative round end to end, plus a real creative-tracker template.

Phase 3 is now **four** prompts: capture → evaluate → **plan the round** → build.

## New prompt

- `prompts/ideas-and-briefs/sprint-plan.md` — takes the ranked shortlist from `idea-evaluation.md` and shapes it into a planned round. Sizes the round from the account's real spend and net-new-**evergreen** cadence (promotional creative stripped out first), sets it as a deliberate multiple gated by account confidence, and holds the hard rule that every concept names a hypothesis. Splits across SKU lanes (scale the hero + double down on what works, with both guardrails), allocates across personas by confidence (dropping a persona is a named choice), sets variation counts, and emits the **concept map** — one row per concept with persona, doorway, leading emotion, format, asset type, and variation count. Embeds the expertise-core and brand-intake synced blocks like its sibling `brief-creation`. Output: `z-brands/[brand]/sprints/[YYYY-MM-DD]-[sprint-slug]/sprint-plan.md`.

## Layout change — a sprint is the container, briefs nest under it

The brand `briefs/` surface became `sprints/`. Each `sprints/[YYYY-MM-DD]-[sprint-slug]/` holds `sprint-plan.md`, a nested `briefs/` folder, and a `retro.md` that feeds the next round's sizing. Ad-hoc co-pilot briefs with no planned round behind them land in `sprints/_unplanned/briefs/`.

## Rewired

- `prompts/ideas-and-briefs/idea-evaluation.md` — now hands its ranked shortlist to `sprint-plan` rather than straight to briefs. Its call is the rank (which ideas are strongest, in order); sizing and splitting the round is explicitly the plan step's job, not the evaluation's.
- `prompts/ideas-and-briefs/brief-creation.md` — now builds one row of the concept map, not a raw pick. Output path moved under the sprint folder; frontmatter gained `sprint` and `concept_id`. Added: a concept can be a pure message-and-persona play with **no inspo source** (do not manufacture one); message-first vs format-first is gated by account maturity; the **doorway** (switch / awakening / discovery) is carried through alongside TEEP and the emotional shift; variation count comes from the plan; talent casting and sensitive-topic CTA discipline honor the plan's flags; ship results feed the sprint `retro.md`.

## Expertise-doc backport (source of truth)

- `global/knowledge/creative-strategy/ideation-and-brainstorming.md` — added the concept-planning method: sizing the round from spend + evergreen cadence, the SKU/lane split, persona allocation by confidence, variation counts, and the concept-map/creative-tracker artifact. Also added message-first-vs-format-first-by-account-maturity (and that a concept needs no inspo source), the two live reads (what's working → double down, what's been tried/failed → avoid), the **doorway** concept, talent as the make-or-break unlock, and sensitive-topic CTA discipline. Broadened the grounding source and the `summary`. Regenerated the doc catalog via `scripts/build-doc-map.py`.

## Propagation

- `prompts/README.md` — Phase 3 renumbered to four prompts; sprint-plan inserted as step 15.
- `system/three-phase-operating-model.md` — Phase 3 now runs in four stages; added the "plan the round" paragraph and updated the output surfaces.
- `prompts/onboarding-runner.md` — the Phase-3 strict line, the phase-name list, and the make-the-work list all carry the sprint-plan step.
- `system/master-file-structure.md` — Phase-3 tree restructured to the sprints container with nested briefs, plus `evaluation-[date].md` under idea-bank.
- `system/parker-system-map.md` — `briefs/` surface renamed to `sprints/` and rewritten; changelog row added.
- `global/knowledge/creative-strategy/expertise-routing.md` — added the sprint-plan doc-type's mandatory reads.
- `system/refresh-cadence.md` — sprint-plan classified as a per-round artifact.
- `system/system-of-records.md` — sprint-plan added to the brand-intake synced-block subset.
- `fixtures/creative-tracker-example.csv` + `fixtures/README.md` — the shared creative tracker saved as a marked fixture, tied to sprint-plan and the ideation method.

## Fixture note

The creative-tracker CSV is illustrative, not a schema. The prompt teaches the column semantics and the planning/execution seam; when a brand supplies its own tracker or brief format at intake, that governs.

## Method enrichment from the ideation + persona transcripts

A second pass folded more of the senior strategist's reasoning — how an idea gets judged good, and how personas get built — into the source-of-truth knowledge docs, so the model learns the judgment, not just the process shape.

- `global/knowledge/creative-strategy/ideation-and-brainstorming.md` — added **the articulation test**: when a source stops her she can name the winning element and its brand fit in a breath, and that fast, tacit read is the log signal; when she has to *force* the fit, that strain is the signal to drop it, not push harder. Do not manufacture a fit. Also added the tracker-is-brand-specific guidance (below).
- `global/knowledge/creative-strategy/persona-research-and-creative-strategy-process.md` — two clear gaps filled. **Confidence scales with the data you have**: the evidence hierarchy (post-purchase survey > first-party reviews > Shopify > retail reviews > organic > competitor signal), naming each persona's confidence and what would raise it, inferred-vs-verified discipline (demographics inferred from review voice are never facts), the LLM-sampling caveat (a review corpus is sampled per query, so two runs rank differently — stake the human claim on the overlap), and the three brand states (never-run / thinks-it-knows / locked-in) that change the whole job. **Personas, overlays, and what is not a persona**: a persona is a trigger-anchored identity; behavioral overlays (deal-motivated, gifting, travel) and identity overlays (a life stage) cut across personas and must not be promoted into them — the exact error Parker kept making. Plus **the non-linear buyer journey** (the real path is see→forget→organic→abandon→off-platform emotional trigger→buy; the trigger is usually off-platform and emotional) and a pointer to the category's own truth / product-landscape as a live research need. Failure modes and quality gates updated to match; catalog regenerated.

## Tracker is the brand's, not ours

Per Jimmy: the creative tracker is different for every brand — don't assume our shape is the way. Both `sprint-plan.md` and the ideation method now say to write the concept map into the surface the team already tracks creative in (Airtable, Google Sheet, Notion) by connecting it as a tool the brain can see and update on the back end, rather than handing back a parallel tracker; if none is connected, recommend they connect theirs.

## Known follow-up

- Run `/prompt-review` on `sprint-plan.md` for the independent audit pass.
- **Proposed new sub-context doc: `product-landscape`.** This surfaced in the transcripts — the category's own truth distinct from the competitor set: the old way / legacy player, the emerging alternatives, and the science, studies, and trends behind the problem (tampon toxicity, perfume note-building, GLP-1→peptides, electrolyte history). It is live research a persona's message often depends on. Flagged here as a proposal rather than built, since it is a new brand-profile slice with its own prompt and propagation; noted as a research need in the persona doc for now.
- No new runtime skill was added — sprint-plan is a prompt, parity with `brief-creation`. A `plan-sprint` one-command skill is an optional second pass if wanted.
- Standing brand brains built before today get the new prompt + layout via `propagate-craft` / the propagation script; existing `briefs/` folders in a live brain would migrate under `sprints/` at that time.
