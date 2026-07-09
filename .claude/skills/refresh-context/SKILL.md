---
name: refresh-context
description: Keep the brand brain from going stale. Reads running-notes/refresh-schedule.md and each standing doc's refresh_by frontmatter, surfaces what is overdue or due soon, walks the Phase 1→2→3 dependency spine to catch docs made stale by upstream changes even when their own date is fine, and re-runs the generating prompt for each — carrying the prior version forward and re-stamping the dates. Use weekly as a scheduled routine, or whenever asked to refresh, re-run, or check the freshness of the brand brain or any context doc.
argument-hint: "[optional: a doc name or cadence tier to refresh; default = everything overdue]"
---

# Refresh context — keep the brain from going stale

A context doc is a photograph of a moving thing. The ad account moves weekly, reviews pile up, a competitor enters, the brand relaunches. Every standing doc carries a `refresh_by` date; this routine watches those dates so a stale doc gets re-run instead of quietly being trusted past its shelf life. It does **not** silently re-run without surfacing the recommendation first.

## When it runs

**Weekly** as a scheduled check. The check is cheap — it only re-runs docs that are actually due. Most weeks it surfaces a short list; some weeks nothing is due.

## The freshness mechanism

Every context doc stamps two frontmatter fields: `generated_on` (the day it was produced, from `get_current_time`) and `refresh_by` (`generated_on` + the doc type's cadence). One aggregated view lives at `running-notes/refresh-schedule.md` — the file to watch. It is a *view* over the per-doc stamps, not a second source of truth; when the two disagree, the doc's own frontmatter wins and the schedule line is corrected.

### The cadence by doc type (the dials)

- **~90 days (quarterly)** — the account moves under these: `ad-account-evaluation`, `performance-targets-and-metrics`, `organic-channels-inventory`, `visual-vocabulary`, `marketing-calendar-and-campaigns`, the four Phase-2 strategy inputs (persona / product-priority / messaging / creator-talent) and the `strategic-roadmap` they synthesize.
- **~180 days (semi-annual)** — these accumulate, they don't lurch: `reputation-analysis`, `customer-journey-and-persona-discovery`, `category-and-market-research`, `community-and-forums`, `website-and-product-audit`, personas (profile + sources + voice library + lifecycle + bias notes), `voice-of-customer`, the constant competitor profiles.
- **~365 days (annual)** — identity rarely shifts: `brand-identity-analysis`, `operations-and-team`.
- **Event-driven, not calendar** — `brand-profile-narrative` is due when ≥2 of its sub-context docs have been re-run (90-day floor as backstop); competitor rotation refreshes constants semi-annually and rotates affinity/inspiration each cycle.
- **Exempt** — the `audits-*` family (cadence is in the name), the idea bank and briefs, and `idea-evaluation` (event-driven; see the `evaluate-ideas` skill).

### Triggers that override the calendar (refresh early)

A rebrand or repositioning, a new SKU/line/launch, a pricing move (the brand's or a key competitor's), a meaningful jump in the review corpus or a new review surface, a new competitor entering or one exiting, an attribution/account-structure change that breaks comparability, or a validated finding that changes the read the doc rests on.

### Dependency staleness — the phase spine

A doc can be stale while its own date is fine, because what it was built *from* moved. The three phases are a dependency chain and freshness flows down it: Phase 1 (audits, foundation sub-context docs, personas, voice-of-customer, competitors) → Phase 2 (the four strategy inputs → the strategic roadmap) → Phase 3 (idea evaluation, briefs). When an upstream doc's read materially changes on a re-run, every downstream doc synthesized from it is stale-by-dependency regardless of its calendar date. The edges: a Phase-1 change hits the Phase-2 strategy input(s) that rest on it; any Phase-2 strategy input change hits the `strategic-roadmap`; a roadmap change makes `idea-evaluation` due. The two event-driven rules above (`brand-profile-narrative`, `idea-evaluation`) are the same principle. See `parker-system/system/refresh-cadence.md` for the doctrine.

## Process

1. **Read the schedule.** Open `running-notes/refresh-schedule.md`. If it is missing (a fresh brain may not have one yet), build it: walk every standing doc, read its `generated_on` / `refresh_by` frontmatter, and write one line per doc grouped by cadence tier. This becomes the file watched from here on.
2. **Compare to today.** Read today from `get_current_time`. Mark each doc `overdue`, `due soon` (within ~2 weeks), or `fresh`. Then scan for fired override triggers — if one has fired, the doc is due regardless of its date.
3. **Walk the phase spine for dependency staleness.** After the date pass, check the Phase 1→2→3 chain: for each downstream doc (the four Phase-2 strategy inputs, the `strategic-roadmap`, `idea-evaluation`), read the `generated_on` of the upstream docs it was built from. If any upstream is newer than the downstream *and* that upstream's last re-run materially changed the read — not a carry-forward-unchanged refresh — the downstream is `stale by dependency`, regardless of its own date. Judge materiality by reading the two versions, not by the file's timestamp alone; a touched-but-unchanged upstream does not cascade. This is what catches a roadmap built on a performance read that has since moved.
4. **Surface before acting.** List what is overdue / due-soon / stale-by-dependency with one line each — "your performance read is from March and it's now June; want me to refresh it?" or "the messaging strategy input predates the customer-review audit that just changed the read it rests on." Name the reason (date vs dependency) so the recommendation is legible. In an interactive run, wait for the go-ahead. In a scheduled run, refresh the overdue-and-material set automatically and report what was done and why.
5. **Re-run each due doc, and note whether the read changed.** A refresh is a re-run of the *generating prompt*, not a patch. The prompt lives in this brain at `parker-system/prompts/<path>.md` (or in the brain's own root `prompts/` folder, for generators the brain authored itself per growing-the-brain) — it travels with the brain for exactly this, so re-run the doc's own generating prompt rather than improvising a regeneration. Take the prior version as context, carry forward what is still true, re-read the live sources the doc rests on (Parker MCP reads, the brand's own surfaces, web), and re-stamp `generated_on` and `refresh_by`. Honor the brand hard rules and load the `parker-system/creative-strategy-context/` docs the doc type requires per the routing table in `CLAUDE.md`, including the brand lens overlay.
   - **Preserve what the brand put there.** A re-run regenerates from sources, so it can quietly erase tribal knowledge the brand or the team hand-added to a doc — a corrected fact, a note in their own words, a constraint they typed in, an insight they appended. That is the brand teaching Parker, and it outranks a fresh generic pass. Before overwriting, diff the new version against the prior one: anything brand-authored or hand-corrected carries forward, reconciled into the new doc, not dropped. If the live data now genuinely contradicts a brand-stated line, do not silently overwrite it — surface the conflict and offer the update, the same way a tool-sourced contradiction is handled. And when a refresh turns up a durable brand preference or correction worth keeping beyond this one doc, add it to `brand-lens.md` so it shapes every future output, not just this re-run.
6. **Update the schedule line** for every doc re-run, so `refresh-schedule.md` stays a true aggregate. When a re-run materially changed the read, note that on the line — it is the signal the phase-spine walk reads next cycle to decide whether downstream docs cascade.
7. **Refresh the folder indexes.** If a refresh added, removed, or materially changed a competitor profile or an audit, regenerate that folder's `INDEX.md` (`competitors/INDEX.md`, `audits/INDEX.md`) — one line per doc, filename plus what it is, newest audit noted as the present tense. These are the generated maps the always-loaded `brand-profile.md` points to so the planner can see everything in the growing folders without the one-pager enumerating it. Keep them in sync with the folder; they are pointers, never restated findings.
8. **Close the loop.** If a refresh surfaced something new — a shift the old read missed — capture it as an open loop in `open-loops/` for the next roll-up, and note any idea worth keeping for `harvest-ideas`.
9. **Log the run.** Prepend one entry to `running-notes/routine-log.md` (create it from `parker-system/templates/routine-log-template.md` if it does not exist yet): the date and time, `refresh-context`, whether the run was scheduled or manual, what was checked (docs against `refresh_by` plus the phase spine), what was re-run and re-stamped, what was left fresh, and anything surfaced. This is the append-only history — never overwrite it, and never overwrite the due-date view in `refresh-schedule.md` with it; they are two different files. It is what proves the weekly routine actually fired and what it did each week.

## Hard rules

- Never silently keep using a doc past its `refresh_by`, and never re-run without first surfacing the recommendation in an interactive session.
- A refresh re-runs the prompt with the prior version as context — it does not hand-edit a stale doc in place.
- The doc's own frontmatter is the source of truth; the schedule is a view. Correct the schedule to the doc, never the reverse.
- Honor the brand hard rules (see `CLAUDE.md` and `running-notes/brand-notes-from-org.md`) on every regenerated doc.
- Never let a re-run erase brand-authored content. Tribal knowledge, hand-corrections, and notes the brand or team added carry forward into the new version; a genuine data contradiction is surfaced and offered, never silently overwritten.
- Re-run the doc's own generating prompt from its home: `parker-system/prompts/` for the factory generators (they travel in the mount for exactly this), or the brain's own root `prompts/` for generators the brain authored itself per growing-the-brain. Those two are the whole contract — no third location. Self-contained otherwise: read only in-repo surfaces and live data sources. Do not depend on factory (`parker-brain`) paths — they do not exist in a cloned instance.
- Dependency staleness cascades only on a *material* change, and only downstream along the phase spine. A carry-forward-unchanged refresh does not force the chain to re-run; surface stale-by-dependency docs as recommendations, never auto-cascade the whole spine on a touch.

## Deliverable

The due docs re-run and re-stamped, `running-notes/refresh-schedule.md` updated, one entry appended to `running-notes/routine-log.md`, and a short report of what was refreshed, what was left (and why) — separating date-overdue from stale-by-dependency — and any open loops or ideas the refresh surfaced.
