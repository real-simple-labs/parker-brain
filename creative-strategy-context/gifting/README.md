# Gifting — year folders

This folder holds **year-scoped reads** on the gifting season. It is provenance and moment-in-time context, not method.

The method lives in `creative-strategy-context/gifting-and-q4-creative.md`, at the top level, alongside its parent `seasonality.md`. That separation is deliberate and it is enforced by the tooling: `scripts/build-doc-map.py` globs `creative-strategy-context/*.md` non-recursively, so **nothing inside this folder appears in the doc catalog** that the planner reasons over. A durable principle filed here is one the brain will not retrieve.

So the rule is:

- **Durable principle** — something true across years, about how gifting creative works → goes in `gifting-and-q4-creative.md`.
- **Year-specific read** — market conditions, competitive dynamics, platform behavior, or format trends particular to one season → goes in `[year]/`.

Each year folder holds the read for that season and any source captures behind it. When a year-specific observation turns out to hold across several years, promote it into the durable doc and leave the original in place as the record of where it came from.

## Layout

```
gifting/
  README.md          ← this file
  2026/
    2026-q4-read.md  ← the year's conditions and what they change
```

## Sourcing

Entries carry their source surface and date per `system/attribution-principle.md`. Where a source is a private conversation or a client account, generalize it before it lands here — this repository is public, and the rule in `CLAUDE.md` is that private brand, customer, and source details are removed or explicitly approved.
