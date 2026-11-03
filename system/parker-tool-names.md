# Parker tool names — current vs legacy

> Mapper for prompts, skills, and brain docs. Use the **current** name in every new or edited reference. Keep a **legacy** name only when the tool still exists under that id (chat history, old MCP sessions) or when you are reading a historical release note. The live inventory of what each tool does is `system/parker-tools.md`.

When Parker splits a mixed tool into read and write siblings, prompts name the sibling that matches the job. Do not invent a third name.

## Read / write splits (use these)

| Job | Current (use in prompts) | Legacy mixed id (keep if still seen) |
|---|---|---|
| Organic social — posts, stats, reports, tracking roster | `search_organic_social` | `search_and_manage_organic_social` (also formerly labeled `organic-social` as a tool) |
| Organic social — subscribe / unsubscribe / set tracking sources | `manage_organic_social` | same mixed id as above |
| Competitor / inspo Meta Ad Library — ads, discover, brand search, roster | `search_competitor_facebook_ads` | (unchanged for reads; older camelCase: `externalBrandAds`, `external-brand-ads-v2`) |
| Competitor / inspo — follow / unfollow / change relationship | `manage_competitor_facebook_ads` | was folded into `search_competitor_facebook_ads` before the split |
| Brand websites — positioning, ICP, promos, page changes, compare | `search_brand_websites` | `monitor_brand_websites` (also formerly `brand-websites`) |
| Brand websites — subscribe / unsubscribe / change tracking / trigger scrape | `manage_brand_website_tracking` | same mixed id as above |

## Rules

1. **Prompts and skills use current names only.** A creative read of organic posts names `search_organic_social`. Starting organic scrape tracking names `manage_organic_social`. Following a brand for Meta ads names `manage_competitor_facebook_ads`, not the search tool.
2. **Keep legacy if it still exists.** Chat history and older MCP catalogs may still show the mixed ids. Treat them as aliases of the current siblings above — do not delete them from registries that dual-support history. Do not teach the model to prefer them in new work.
3. **If only the legacy name appears in a standing brain doc** (pre-v45 copy that the pin has not refreshed yet), map it with this table before calling a tool. Prefer the read sibling when the ask is research; prefer the write sibling when the ask changes tracking.
4. **Unrelated labels stay.** `organic-social` as a team or `sources_pulled` source type is not a tool name. Leave those alone.

## Older camelCase aliases (pre-snake_case)

Still map if encountered; prompts should already use the snake_case current names from v41:

| Legacy | Current |
|---|---|
| `parkerFileSystem` | `parker_file_system` (chat-only; not on MCP) |
| `webSearch` / `webSearchTool` | `search_web` (chat-only) |
| `askParkerAgent` | `ask_parker_agent` |
| `getContextDocs` | `get_context_docs` (chat-only) |
| `facebookAdsAnalysisReportsSqlSearchTool` / `facebookAdsSQLSearchTool` | `search_facebook_ads_sql` |
| `organic-social` (as a tool id) | `search_organic_social` for reads; `manage_organic_social` for writes |
