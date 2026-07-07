# Refresh cadence — keeping the brand brain from going stale

A context doc is a photograph of a moving thing. The ad account changes weekly, reviews pile up, a competitor enters, the brand relaunches. So every generated doc carries a date by which it should be regenerated, and Parker watches that date so a stale doc gets re-run instead of quietly being trusted past its shelf life.

This is the same mechanism the open-loops pipeline already uses for validations (`revalidate_by`), extended to the foundation and creative-strategy docs.

## How it works

Every context doc a prompt generates stamps two fields in its frontmatter:

- `generated_on:` — the date the doc was produced, from `get_current_time`.
- `refresh_by:` — `generated_on` plus this doc type's cadence below.

Parker reads `refresh_by` whenever it loads a brand doc. If today is past it, Parker says so plainly and offers to re-run the prompt — "your performance read is from March and it's now July, want me to refresh it?" It does not silently keep using a doc past its date, and it does not re-run without surfacing the recommendation first.

A refresh is a re-run of the generating prompt. The prompt's own discipline still holds: it takes the prior version as context, carries forward what is still true, and re-stamps `generated_on` and `refresh_by`.

## The consolidated schedule — one place to watch

Per-doc `refresh_by` stamps are the source of truth, but reading them means opening every doc. So each brand brain carries one aggregated schedule at `running-notes/refresh-schedule.md`, generated from the template at `templates/refresh-schedule-template.md`. It lists every standing doc with its last-run date and its due date, grouped by cadence tier. The onboarding runner builds it at the end of the cold start by reading each doc's frontmatter, and every prompt re-run updates that doc's line.

This is the file Parker actually watches. On load, Parker reads the schedule, compares each due date to today from `get_current_time`, and surfaces what is overdue or due soon — rather than discovering staleness one doc at a time. The schedule is a view over the per-doc stamps, not a second source of truth; when the two disagree, the doc's own frontmatter wins and the schedule line is corrected.

On-load checking covers the weeks someone uses the brain. For the weeks nobody opens it, a **refresh-sweep schedule** runs the same check unattended: it reads this schedule on a clock, finds what is overdue, and re-runs the generating prompt. Schedules are the repo-native cron layer that keeps the brain alive when no one is typing — the refresh sweep is one of them. See `system/schedules.md`.

## The cadence by doc type

These are the dials. Tune them here; the prompts read the cadence from this doc.

**~90 days (quarterly) — the account moves under these.**
- ad-account-evaluation
- performance-targets-and-metrics
- organic-channels-inventory
- visual-vocabulary
- marketing-calendar-and-campaigns
- the four Phase-2 strategy inputs — persona-strategy-input, product-priority, messaging-strategy-input, creator-talent-strategy-input — and the strategic-roadmap they synthesize into (one planning cycle)

**~180 days (semi-annual) — these accumulate, they do not lurch.**
- reputation-analysis
- customer-journey-and-persona-discovery
- category-and-market-research
- community-and-forums
- website-and-product-audit
- personas (personas-profile and its source pulls, voice library, lifecycle, bias notes)
- voice-of-customer
- competitor profiles (the constant set; see the rotation note below)

**~365 days (annual) — identity rarely shifts.**
- brand-identity-analysis
- operations-and-team

**The audit cadence layer — generated at the cold-start baseline, then refreshed on its named interval.** Each audit is produced once during the cold start (Phase-1 branch E) as the t0 baseline and stamps `generated_on`/`refresh_by` exactly like every other doc; its named interval *is* its cadence, so the refresh-sweep re-runs it from its own `generated_on` rather than treating it as exempt. The first run is the baseline the account one-pagers synthesize; every later run is the recurring re-read.
- weekly-performance-snapshot — 7 days
- biweekly-iterations-report — 14 days
- monthly cuts — monthly-hook-audit, monthly-performance-report, monthly-organic-tiktok-audit, monthly-tiktok-mining, and the monthly-external cuts (monthly-creative-landscape, monthly-top-impressions-report) — 30 days
- quarterly cuts — 90-day-creative-strategy-audit, 90-day-performance-audit, 90-day-diversity-audit, customer-review-audit, quarterly-whitespace-analysis, and the quarterly-external cuts (the 90-day-*-external audits, single-competitor-ad-analysis) — 90 days

**Event-driven, not calendar.**
- brand-profile-narrative refreshes when its input slices do — when two or more of its sub-context docs have been re-run, the narrative is due regardless of its own date, because it is a synthesis of them. Hold a 90-day floor as a backstop.
- Competitor rotation: the constant competitors refresh on the semi-annual cadence; affinity and inspiration competitors rotate each audit cycle, so a fresh set replaces them rather than the same ones being re-run.

**Exempt — not calendar-refreshed.**
- The idea bank and briefs. The idea bank is always-on and captured continuously; briefs are per-campaign artifacts, not refreshed.
- idea-evaluation. It is event-driven, not calendar: re-run when the bank grows enough to change the rank or when the roadmap is re-approved, not on a fixed date.
- sprint-plan. It is a per-round artifact — a new one is written for each creative sprint rather than the same one refreshed. Re-plan the current round only if the roadmap is re-approved with shifted priorities before it ships, or if a fresh spend or cadence read changes the size the account can support.

## Triggers that override the calendar

A doc is due early, regardless of its `refresh_by`, when a real-world event has changed the thing it describes:

- a rebrand or repositioning
- a new SKU, product line, or major launch
- a pricing change, the brand's or a key competitor's
- a meaningful jump in the review corpus or a new review surface coming online
- a new competitor entering the set, or one exiting
- an attribution-setting or account-structure change that breaks comparability
- a validated finding that changes the read the doc rests on

When a trigger has fired, set `refresh_by` sooner at generation, or re-run now rather than waiting for the date.
