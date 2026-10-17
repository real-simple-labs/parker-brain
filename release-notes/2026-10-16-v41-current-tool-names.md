# v41 — prompts and docs use Parker's current tool names (2026-10-16)

Some prompts and docs still named Parker's tools by their old names, from before the tools got their current snake_case names. A model that reads `parkerFileSystem` or `getContextDocs` looks for a tool that doesn't exist under that name, so Parker's chat had to carry its own list of old names to new ones.

## What shipped

Every old name now reads as the tool's current name:

| Old name | Current name | Where |
|---|---|---|
| `parkerFileSystem` | `parker_file_system` | the tool paragraph of all 17 audit prompts |
| `webSearch` | `search_web` | monthly hook audit, monthly organic TikTok audit, 90-day performance audit (external) |
| `organic-social` (as a tool) | `search_and_manage_organic_social` | 90-day creative strategy, diversity and performance audits (external), monthly organic TikTok audit |
| `askParkerAgent` | `ask_parker_agent` | the three global ad database docs, the scriptwriting skill's `find-reference-ads` process |
| `getContextDocs` | `get_context_docs` | `creative-strategy-context/ai-static-ad-generation.md` |
| `facebookAdsAnalysisReportsSqlSearchTool` | `search_facebook_ads_sql` | `creative-strategy-context/ai-static-ad-generation.md` |

`system/parker-tools.md` said it was unconfirmed whether Parker's chat can search the open web. It now says what is true: the chat agent has `search_web` for teams that have it turned on, and the MCP doesn't expose it.

Left as they are: `organic-social` where it names the team or a source type (the organic-social team, the `sources_pulled` labels); `listThreads` and `getMessages`, which are the current mode values of `search_chat_history`; release notes and reasoning traces, which record what was true at the time.

## Migration

`migrations/v41.md`: no-op. The changed files are method files that the pin bump delivers, plus one skill file the re-sync copies.
