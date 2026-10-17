# v42 — the brain says what Claude Code uses in place of chat-only tools (2026-10-16)

Parker's chat agent (web, Slack, scheduled runs) has tools that the Parker MCP does not expose: `get_current_time`, `get_webpage`, `search_web`, `parker_file_system`, `update_custom_working_memory`, `get_context_docs`, and, on a separate MCP endpoint, `ask_parker_agent`. A Claude Code session (a build, a routine, everyday work in a brain) never has them, but 88 files of the method told it to use them. `system/parker-tools.md` even listed three of them as Parker MCP tools.

## What shipped

- **`system/parker-tools.md`.** `get_current_time`, `get_webpage` and `update_custom_working_memory` are out of the Parker MCP table. The "Chat-only tools" note is now a table with each chat tool, what it does, and what Claude Code uses instead: the session's own date, Claude Code's `WebFetch` and `WebSearch`, the brain's own files for saves and memory, the brain's own context docs. "In Claude Code" covers a Codex session too, with Codex's own date and web tools. The ad databases behind `ask_parker_agent` (internal favorites, Parker favorites, the global AI-tagged ads DB) have no stand-in: a skill may fall back to `search_facebook_ads_semantic`, `search_competitor_facebook_ads` or `search_swipe_file`, but names the corpus it searched and never reports a result as a hit in those databases. The doc's opening line no longer says the MCP can fetch a known page. The build-harness section now allows a prompt to send Claude Code to its own tool, but only through that table, and named as Claude Code's.
- **The date.** The freshness line in the shared expertise-core block (embedded in 73 prompts) and 10 more lines in `system/refresh-cadence.md`, `system/parker-system-map.md`, the `refresh-context` and `research-loops` skills and the two brain templates now say "(in Claude Code, the session's own date)" after `get_current_time`.
- **Saves.** The tool paragraph of the 17 audit prompts says that in Claude Code the save is writing the output into the brain's files.
- **Web.** The 3 audit lines that use `search_web` or `get_webpage` name Claude Code's own `WebSearch` and `WebFetch`. `harvest-ideas` no longer lists `get_webpage` as a Parker MCP tool (it already listed `WebSearch` and `WebFetch` as Claude Code's).
- **Context docs and ad databases.** `ai-static-ad-generation.md` points Claude Code at the brain's own context docs. The three ad-database specs say they are out of reach in Claude Code. The scriptwriting `find-reference-ads` process keeps its tier order for `ask_parker_agent` only; in Claude Code it searches the fallback corpora with no tiers and names where each candidate came from, and `adapt-existing-script` says the reference can come from that corpus.

Not changed: the open-loops rule that a loop answerable only by open-web search is constrained. That's a method call, not a tool name.

## Migration

`migrations/v42.md` (**Auto-apply:** yes): two exact sentence swaps in the brain's own files, the root `CLAUDE.md` and `running-notes/refresh-schedule.md`, each skipped where the team changed the sentence.
