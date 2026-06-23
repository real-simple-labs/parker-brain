# Refresh-schedule template

> Instantiate this per brand at `running-notes/refresh-schedule.md`. The onboarding runner generates it at build time by reading each standing doc's `generated_on` and `refresh_by` frontmatter, and updates the relevant line every time a prompt is re-run. Fill the `{{slots}}`, keep the doc lines that exist for this brand, and delete this header block.

---

# Refresh schedule — {{BRAND_NAME}}

This is the one place that tracks when every standing doc was last run and when it is due to be re-run. Each doc's own `generated_on` and `refresh_by` frontmatter is the source of truth; this file aggregates them so the whole brain's freshness can be read at a glance instead of opening every doc. The cadence policy — which doc type refreshes how often, and the real-world triggers that override the calendar — lives in `parker-system/system/refresh-cadence.md`.

## How Parker uses this

- When you load this brain or consult a standing doc, read this schedule and compare each `due` date to today from `get_current_time`. A doc whose due date has passed is overdue; one inside roughly two weeks of its due date is due soon.
- Surface what is overdue or due soon plainly, and offer to re-run the generating prompt by name — "your ad-account read is from March and it is now July, want me to refresh it." Do not silently keep using a doc past its due date, and do not re-run without surfacing the recommendation first.
- A refresh is a re-run of the generating prompt. It takes the prior version as context, carries forward what is still true, and re-stamps `generated_on` and `refresh_by`. After a re-run, update that doc's line in this schedule to the new dates.
- The triggers in `parker-system/system/refresh-cadence.md` outrank the calendar. A rebrand, a new SKU, a pricing move, a new competitor, an attribution change, or a validated finding that changes the read makes a doc due early regardless of the date here. When a trigger has fired, flag the doc as due now and note the trigger.
- When two or more sub-context slices have been re-run, `sub-context-docs/brand-profile-narrative.md` is due regardless of its own date, because it is a synthesis of them.

## The schedule, by cadence

### Quarterly — roughly 90 days

- `sub-context-docs/ad-account-evaluation.md` — last run {{date}} — due {{date}}
- `sub-context-docs/performance-targets-and-metrics.md` — last run {{date}} — due {{date}}
- `sub-context-docs/organic-channels-inventory.md` — last run {{date}} — due {{date}}
- `sub-context-docs/visual-vocabulary.md` — last run {{date}} — due {{date}}
- `sub-context-docs/marketing-calendar-and-campaigns.md` — last run {{date}} — due {{date}}
- `strategy/persona-strategy-input.md` — last run {{date}} — due {{date}}
- `strategy/product-priority.md` — last run {{date}} — due {{date}}
- `strategy/messaging-strategy-input.md` — last run {{date}} — due {{date}}
- `strategy/creator-talent-strategy-input.md` — last run {{date}} — due {{date}}
- `strategy/strategic-roadmap.md` — last run {{date}} — due {{date}}

### Semi-annual — roughly 180 days

- `sub-context-docs/reputation-analysis.md` — last run {{date}} — due {{date}}
- `sub-context-docs/customer-journey-and-persona-discovery.md` — last run {{date}} — due {{date}}
- `sub-context-docs/category-and-market-research.md` — last run {{date}} — due {{date}}
- `sub-context-docs/community-and-forums.md` — last run {{date}} — due {{date}}
- `sub-context-docs/website-and-product-audit.md` — last run {{date}} — due {{date}}
- `personas/personas-profile.md` and its source pulls, voice library, lifecycle maps, and bias notes — last run {{date}} — due {{date}}
- `personas/voice-of-customer/voice-of-customer.md` — last run {{date}} — due {{date}}
- `competitors/{{competitor}}/competitor-snapshot.md` — last run {{date}} — due {{date}}

### Annual — roughly 365 days

- `sub-context-docs/brand-identity-analysis.md` — last run {{date}} — due {{date}}
- `sub-context-docs/operations-and-team.md` — last run {{date}} — due {{date}}

### Event-driven — no calendar date, re-run when the trigger fires

- `sub-context-docs/brand-profile-narrative.md` — refreshes when two or more of its input slices do, with a 90-day floor as backstop. Last run {{date}}.
- `idea-bank/evaluation-[YYYY-MM-DD].md` — re-run when the bank grows enough to change the rank or when the roadmap is re-approved. Last run {{date}}.
- Competitor rotation — the constant set refreshes on the semi-annual cadence; affinity and inspiration competitors rotate each audit cycle rather than being re-run.

### Audit cadence — baselined at build, then re-run on each audit's named interval

Generated once at the cold start (Phase-1 branch E) and re-run from each audit's own `generated_on`.

- `audits/[YYYY-Q]/90-day-creative-strategy-audit.md` (anchor) — last run {{date}} — due {{date}} (+90d)
- `audits/[YYYY-Q]/90-day-performance-audit.md` — last run {{date}} — due {{date}} (+90d)
- `audits/[YYYY-Q]/90-day-diversity-audit.md` — last run {{date}} — due {{date}} (+90d)
- `audits/[YYYY-Q]/customer-review-audit.md` — last run {{date}} — due {{date}} (+90d)
- `audits/[YYYY-Q]/quarterly-whitespace-analysis.md` — last run {{date}} — due {{date}} (+90d)
- `audits/[YYYY-MM]/monthly-hook-audit.md`, `monthly-performance-report.md`, `monthly-organic-tiktok-audit.md`, `monthly-tiktok-mining.md` — last run {{date}} — due {{date}} (+30d)
- `audits/[YYYY-MM]/biweekly-iterations-report.md` — last run {{date}} — due {{date}} (+14d)
- `audits/[YYYY-MM]/weekly-performance-snapshot.md` — last run {{date}} — due {{date}} (+7d)
- External cuts under `audits/[…]/external/` follow the same interval as their internal sibling.

### Exempt — self-cadenced or always-on, no entry needed

- The idea bank is captured continuously; briefs are per-campaign artifacts, not refreshed.
