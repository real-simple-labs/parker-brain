# Global Database Prompts

These specs define Parker's database-like memory systems. The specs are local contracts for schema, capture, curation, and retrieval behavior. Runtime storage may live inside Parker MCP or in a file-backed staging layer while the MCP version is being built.

## Files

- `global-ai-tagged-ads-db.md` - cross-brand ad atoms Parker can retrieve for scripts, hooks, iterations, and generation.
- `internal-favorites-db.md` - internal favorite ads and concepts.
- `parker-favorites-db.md` - Parker's curated favorite references.
- `expert-signal-db.md` - expert content signals that keep Parker aware of market, platform, category, creative, and operating changes.
- `brand-idea-bank.md` - one brand's living idea bank, maintained from docs, research, conversations, ideas-tab saves, and routed expert signals.
