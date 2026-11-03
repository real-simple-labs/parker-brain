# v45 — prompts and docs use split Parker tool names (2026-11-03)

Parker split three mixed MCP tools into read and write siblings. Prompts and skills that still named the mixed ids would call a tool that is no longer the preferred surface (and, for organic and websites, is kept only as a legacy alias for chat history).

## What shipped

Every research reference to the old mixed organic tool now reads as the read sibling. The inventory lists both siblings for organic, competitor follow, and brand websites. A mapper keeps the legacy mixed ids so standing brains and registries that dual-support chat history still know how to map them.

| Job | Current name | Legacy (keep if still seen) |
|---|---|---|
| Organic posts / stats / reports / roster | `search_organic_social` | `search_and_manage_organic_social` (`organic-social` as a tool) |
| Organic subscribe / unsubscribe / set sources | `manage_organic_social` | same mixed id |
| Competitor Meta Ad Library reads | `search_competitor_facebook_ads` | (reads unchanged; follow was folded in before) |
| Competitor follow / unfollow | `manage_competitor_facebook_ads` | was part of the search tool |
| Brand website intelligence | `search_brand_websites` | `monitor_brand_websites` (`brand-websites`) |
| Brand website tracking / scrape | `manage_brand_website_tracking` | same mixed id |

- **`system/parker-tool-names.md`** — new mapper: current vs legacy for the splits, plus the older camelCase aliases from v41.
- **`system/parker-tools.md`** — inventory rows for the six current tools; competitor search no longer claims it subscribes; legacy mixed ids called out at the bottom.
- **Prompts, expertise-core, harvest-ideas, script-from-organic-niche** — `search_and_manage_organic_social` → `search_organic_social` wherever the ask is a creative or research read.

Left as they are: `organic-social` as a team or source-type label; release notes and the v41 system-map row, which record what was true at the time.

## Migration

`migrations/v45.md`: no-op. The changed files are method files the pin bump delivers, plus skill files the re-sync copies.
