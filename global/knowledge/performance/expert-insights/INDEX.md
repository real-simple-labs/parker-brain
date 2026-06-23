# Performance (Media Buying) Expert Insights Index

This is the file-backed v1 home for knowledge-source intake in **performance** — Parker's media-buying team. Media buyers are a real and growing share of Parker's users, and this is their expert-signal pipeline. It mirrors the creative-strategy intake system one-for-one; the runtime behavior lives in `skills/expert-signal-intake/SKILL.md` and the signal schema is `prompts/global-databases/expert-signal-db.md`.

This is the second team knowledge tree to come online after creative-strategy. The team is named `performance` in `system/master-file-structure.md` and `system/parker-system-map.md`; "media buying" is the colloquial name for the same team. The canonical performance knowledge docs it feeds are named in the master file structure: `incrementality-and-lift.md`, `attribution-and-privacy.md`, `account-structure-principles.md`, `ad-buying-principles.md`, `scaling-frameworks.md`, `creative-volume-and-fatigue.md`, `testing-frameworks.md`, `platform-mechanics-meta.md`, `pacing-and-budget-rhythms.md`, `reading-mer-and-blended.md`, `diagnosing-a-bad-week.md`, `creative-as-targeting.md`, and `conversion-rate-math.md`.

## How this system works

Intake is **approval-gated and propose-first**. When Jimmy hands Parker a knowledge source, Parker studies it in full, decides which of Parker's four skill components should learn from it — context docs, knowledge docs, tool calls, or processes — and writes the **exact, verbatim change it would make** as a proposal in the review queue, surfacing the same plan to Jimmy. Parker does **not** modify the real surface until Jimmy approves. On approval Parker applies the proposed text exactly; on modify it applies Jimmy's version; on deny nothing is written.

The folders here hold provenance and the review queue, not Parker's working knowledge. Working knowledge lives in the performance knowledge docs themselves, because that is where Parker retrieves it; a knowledge change that only ever lives in this folder is one Parker will never call — which is why an approved proposal gets applied to its real surface, then this folder gets out of the way.

Performance sources carry an extra discipline: **media-buying claims are claims about money.** A "leaked deck," a "99.9% confidence" stat, or a "35% of spend is wasted" figure is `stated` until Parker can ground it in the brand's own account data or a second independent source. The durable *method* (incrementality, lift testing, the measurement stack, signal quality) is often externally grounded even when a specific source's numbers are not — separate the two.

## Current Status

- Created: 2026-06-18
- Automation status: manual upload and draft capture only
- Curate cadence: monthly
- MCP status: file-backed staging, MCP-ready schema
- Team build status: `[partial]` — expert-insights pipeline live; two canonical knowledge docs drafted (`incrementality-and-lift.md` corroborated+extended, `account-structure-principles.md` seeded), the rest named-but-pending

## Entry Locations

- `inbox/` - raw or partially processed user-provided expert videos, links, transcripts, screenshots, and summaries.
- `context-update-candidates/` - the review queue: one pointer per intake to the drafted change at its real surface, marked `[~]` pending Jimmy's review, plus true candidates that await corroboration before any draft is written.
- `[source-id]/source.md` - source profile once a source becomes recurring.
- `[source-id]/[YYYY-WW]/[content-id].md` - saved expert signals from recurring sources.
- `curation/` - monthly and quarterly synthesis passes.

## Active Signals

- [2026-06-18 - Meta Performance Summit playbook (Disruptor School)](inbox/2026-06-18-meta-performance-summit-playbook.md) - mixed-confidence operator-educator signal from a pasted YouTube transcript framed as "the internal Meta Performance Summit decks, free." Durable, externally-grounded spine: incrementality and conversion-lift / holdout testing, "optimize for new customers," the three-layer measurement stack (platform attribution → MTA/MMM → lift) and the weekly/monthly/quarterly measurement rhythm. Plus account-architecture posture (Advantage+ as a state, "simple scales / complex fails," fewer campaigns / more signal), signal-quality plumbing (EMQ, CAPI+pixel dedup, custom conversion events, value optimization, catalog match rate), the performance scorecard / opportunity score, and creative-placement essentials (9x16, safe zone, sound-on) + partnership-ad / creator-briefing rules. Specific stats (34.5% lower CPA, 35% waste, "99.9% confidence," $740B dataset) and the "leaked deck" framing are stated, not shown.

- [2026-06-18 - Marketing Operators ep. 111 — signal engineering + reach (Cody Plofker / Connor MacDonald, inferred)](inbox/2026-06-18-marketing-operators-ep111-signal-engineering-reach.md) - two DTC operators reasoning out loud about reach testing, signal engineering, and a 360 creator activation. Durable, net-new spine: **signal engineering** (conditional vs non-conditional pixels as the literal instruction to Meta; "find a rich customer who likes travel" vs "find a travel customer"; non-category revenue contamination 6%→40% when the wiring loosened), the **AOV-drift diagnostic** ($360→$140 = signal contamination, not a ROAS cliff), the **overlap rule** (separate events at ~6% overlap, consolidate at ~40%), the **attribution-mismatch principle** (optimize non-purchase events on platforms blind to purchases — YouTube/Snapchat), the **tactic-rollout hierarchy** (geo lift → conversion lift → deliberate comparison; scaling raises the testing bar), the **VO cautionary tale**, **per-channel incrementality factors** and their drift, and the **stacking-measurement** framework for upper-funnel (ad spend as a balance-sheet asset). Directional/account-specific: the IA metric signature (CPM↓/CTR↓/ATC↑/conversion↓, contradictory across the two operators). Ephemeral: the spring-2026 7-day-click redefinition (auction arbitrage). All numbers self-reported, single-brand; two operators / one podcast clique.

## Review queue

See `context-update-candidates/README.md` for the live queue.

- [2026-06-18 - Marketing Operators ep. 111 — signal engineering + reach](context-update-candidates/2026-06-18-marketing-operators-ep111-signal-engineering-reach.md) - **2 drafts + 1 candidate.** Corroborated and extended `incrementality-and-lift.md` (per-channel factors + stacking-measurement; status seeded → corroborated) and seeded the net-new `account-structure-principles.md` (signal engineering, AOV-drift diagnostic, overlap rule, attribution-mismatch, rollout discipline, VO tale). Candidate to `platform-mechanics-meta.md`: IA metric signature + 7-day-click redefinition, watching. Numbers `stated`; promote drafts on review, platform-mechanics candidate on a second corroborating account.

- [2026-06-18 - Meta Performance Summit playbook (Disruptor School)](context-update-candidates/2026-06-18-meta-performance-summit-playbook.md) - **seed + candidates.** Seeded the flagship canonical doc `incrementality-and-lift.md` (externally-grounded method, source's unverified stats held out as directional). Remaining themes routed as candidates to their named performance docs: `attribution-and-privacy.md` (click-vs-view, privacy-era measurement), `account-structure-principles.md` (Advantage+ as a state, simplify-to-scale), `platform-mechanics-meta.md` (EMQ/CAPI, partnership ads, reels essentials, scorecard/opportunity score), `pacing-and-budget-rhythms.md` (measurement rhythm). Promote on corroboration (account data or a second media-buying source) or Jimmy's approval.

## Routing Rules

- Save the signal here as provenance (the one pre-approval write), then propose the verbatim change in the review queue. The signal is the receipt; the approved-and-applied change is the deliverable.
- For video sources, prefer Parker Vault's Gemini upload path before link scraping.
- Classify every source against the four components — context docs, knowledge docs, tool calls, processes — before proposing, and propose updating an existing surface rather than creating a new one when the learning fits.
- Never modify the real surface before Jimmy approves. Show the exact change — old → new for edits, full content for new docs — not a summary. A single source can earn a proposed change, but only Jimmy's approval applies it; a mixed-confidence method-changing claim is a watch item until corroborated.
- Treat numeric performance claims as `stated` until grounded in the brand's account data or a second independent source. Separate the durable method (often externally grounded) from a source's self-interested numbers.
- Reusable cross-brand performance patterns route to `global/knowledge/performance/parker-taste/` once that surface is built; brand-specific account moves route to the brand's performance memory.
- Leave exactly one review-queue pointer per intake so Jimmy never has to dig.
