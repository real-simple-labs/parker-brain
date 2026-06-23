# 2026-06-18 Phase-2 four-input model + Phase-3 idea-evaluation

Backported the methodology the Grüns 2026-06-17 buildout ran ahead of, and closed two factory gaps in the strategy and ideation phases. Source of truth for the new shapes: the Grüns brand brain (`strategy/`, `idea-bank/evaluation-2026-06-18.md`) and its `CLAUDE.md` Phase-2/Phase-3 spec.

## New prompts

- `prompts/ideas-and-briefs/idea-evaluation.md` — the missing middle of the Phase-3 split. Capture (`brand-idea-bank`) → **evaluate** (this) → build (`brief-creation`). Grades the whole captured pile against the approved roadmap: priority served, lever pulled, evidence band confidence-first, roads-not-taken kill list. Output is a ranked shortlist plus a brief-first handoff and a coverage read of what the bank is starving for.
- `prompts/strategic-roadmap/persona-strategy-input.md` — the WHO call.
- `prompts/strategic-roadmap/messaging-strategy-input.md` — what the brand should lead with saying.
- `prompts/strategic-roadmap/creator-talent-strategy-input.md` — who should be on camera.

The three strategy inputs complete the four-input Phase-2 model alongside the existing `product-priority.md`. Each resolves one territory's Phase-1 evidence into a committed recommendation with its own confidence and open loops, mirroring `product-priority.md`'s shape.

## Rewired

- `prompts/strategic-roadmap/strategic-roadmap.md` — now synthesizes all four strategy inputs rather than reading personas-profile and product-priority directly. Updated the intro, "Where this doc sits," "How the priorities are justified," and "Required sources."
- `prompts/ideas-and-briefs/brief-creation.md` — now takes the ranked shortlist from `idea-evaluation.md` rather than a raw idea-bank entry.
- `prompts/README.md` — build order now runs the four Phase-2 inputs before the roadmap, and the Phase-3 capture → evaluate → build spine, renumbered.
- `global/knowledge/creative-strategy/expertise-routing.md` — added the Phase-2 strategy-inputs routing block (persona, messaging, creator-and-talent) and the idea-evaluation routing.

## Expertise-doc backports (Grüns was ahead of the factory)

- `ideation-and-brainstorming.md` — added "Capture is a transfer, not a summary."
- `customer-review-mining-method.md` — added the date-on-every-quote rules; stamped 2026-06-17.

## Onboarding runner + refresh schedule

- `prompts/onboarding-runner.md` — the executable cold-start: scaffolds the flat standalone brand-brain layout, ships the craft layer in as `creative-strategy-context/`, maps each prompt's `z-brands/[brand]/…` output path to the flat path, runs the prompts in dependency order, holds the approval gates, and stamps `CLAUDE.md`/`README.md`/`refresh-schedule.md`. CLAUDE.md and `prompts/README.md` now point at it.
- `templates/refresh-schedule-template.md` — the consolidated per-brand schedule, instantiated at `running-notes/refresh-schedule.md`. Aggregates every standing doc's `generated_on`/`refresh_by` into one place grouped by cadence tier, so Parker watches one file instead of opening every doc to find staleness.
- `system/refresh-cadence.md` — added the four Phase-2 strategy inputs to the quarterly tier, idea-evaluation as event-driven, and a section describing the consolidated schedule and how Parker uses it.
- `templates/brand-brain-CLAUDE-template.md` — added the on-load instruction to watch `refresh-schedule.md` and surface overdue/due-soon docs, plus the map entry.

## Freshness-slot standardization sweep

The "Stamp the doc's freshness" instruction was in 72 prompts, but the actual frontmatter slot was inconsistent: 58 prompts emitted the legacy `last_updated:` while only the 4 new ones used `generated_on:`/`refresh_by:`. Since the refresh-schedule reads `generated_on`/`refresh_by`, this was standardized tier-aware:

- 39 standing-cadence docs (brand-profile, personas, VoC corpus, competitor, market-synthesis, strategy) now carry `generated_on:` + `refresh_by:`.
- 18 self-cadenced docs (the audits family and one monthly persona doc) carry `generated_on:` only — exempt from `refresh_by` by design.
- `open-loops-roll-up` and `idea-evaluation` are event-driven: `generated_on:` only.
- `brief-creation` keeps `last_updated:` (per-campaign artifact, exempt).

Result: 62 prompts stamp `generated_on`, 42 stamp `refresh_by`, no audit carries `refresh_by`, no orphaned `refresh_by`.

## Refresh wiring

- `system/master-file-structure.md` — added `running-notes/refresh-schedule.md` to the always-loaded set, so Parker has the freshness view in context on every turn rather than having to open it. This is what makes the on-load staleness check actually fire.
- The unattended path is the **refresh-sweep schedule** under the repo-native schedules system (`system/schedules.md`): it reads the same schedule on a clock and re-runs overdue docs. The earlier standalone notify-only notifier doc was dropped as redundant with that system; `refresh-cadence.md` now points at `schedules.md`.

## Deliberately not done

- `content-pipeline/` is Grüns-only and was not promoted into the factory.

## Known follow-up

- Run `/prompt-review` on the four new prompts for the independent audit pass.
- `_competitive-set.md` still has no dedicated generator (small).
- The onboarding runner that sequences this full set and maps factory `z-brands/` output paths to the flat standalone brand-brain layout is the next build.
