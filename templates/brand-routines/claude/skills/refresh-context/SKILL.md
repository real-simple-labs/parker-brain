---
name: refresh-context
description: Keep the brand brain from going stale. Reads running-notes/refresh-schedule.md and each standing doc's refresh_by frontmatter, surfaces what is overdue or due soon, and re-runs the generating prompt for each — carrying the prior version forward and re-stamping the dates. Use weekly as a scheduled routine, or whenever asked to refresh, re-run, or check the freshness of the brand brain or any context doc.
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

## Process

1. **Read the schedule.** Open `running-notes/refresh-schedule.md`. If it is missing (a fresh brain may not have one yet), build it: walk every standing doc, read its `generated_on` / `refresh_by` frontmatter, and write one line per doc grouped by cadence tier. This becomes the file watched from here on.
2. **Compare to today.** Read today from `get_current_time`. Mark each doc `overdue`, `due soon` (within ~2 weeks), or `fresh`. Then scan for fired override triggers — if one has fired, the doc is due regardless of its date.
3. **Surface before acting.** List what is overdue / due-soon with one line each — "your performance read is from March and it's now June; want me to refresh it?" In an interactive run, wait for the go-ahead. In a scheduled run, refresh the overdue set automatically and report what was done.
4. **Re-run each due doc.** A refresh is a re-run of the *generating prompt*, not a patch. Take the prior version as context, carry forward what is still true, re-read the live sources the doc rests on (Parker MCP reads, the brand's own surfaces, web), and re-stamp `generated_on` and `refresh_by`. Honor the brand hard rules and load the `creative-strategy-context/` docs the doc type requires per the routing table in `CLAUDE.md`.
5. **Update the schedule line** for every doc re-run, so `refresh-schedule.md` stays a true aggregate.
6. **Refresh the folder indexes.** If a refresh added, removed, or materially changed a competitor profile or an audit, regenerate that folder's `INDEX.md` (`competitors/INDEX.md`, `audits/INDEX.md`) — one line per doc, filename plus what it is, newest audit noted as the present tense. These are the generated maps the always-loaded `brand-profile.md` points to so the planner can see everything in the growing folders without the one-pager enumerating it. Keep them in sync with the folder; they are pointers, never restated findings.
7. **Close the loop.** If a refresh surfaced something new — a shift the old read missed — capture it as an open loop in `open-loops/` for the next roll-up, and note any idea worth keeping for `harvest-ideas`.

## Hard rules

- Never silently keep using a doc past its `refresh_by`, and never re-run without first surfacing the recommendation in an interactive session.
- A refresh re-runs the prompt with the prior version as context — it does not hand-edit a stale doc in place.
- The doc's own frontmatter is the source of truth; the schedule is a view. Correct the schedule to the doc, never the reverse.
- Honor the brand hard rules (see `CLAUDE.md` and `running-notes/brand-notes-from-org.md`) on every regenerated doc.
- Self-contained: read only in-repo surfaces and live data sources. Do not depend on factory (`parker-brain`) paths — they do not exist in a cloned instance.

## Deliverable

The due docs re-run and re-stamped, `running-notes/refresh-schedule.md` updated, and a short report of what was refreshed, what was left (and why), and any open loops or ideas the refresh surfaced.
