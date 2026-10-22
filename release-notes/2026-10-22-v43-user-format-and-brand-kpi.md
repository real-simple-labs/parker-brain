# v43 — the user's format and the brand's own KPI come first (2026-10-22)

Two things kept going wrong in live chats. A user gave Parker their own brief template, said to use it from now on, and still got the method's script brief back, four times in one session. And a brand that measures its ads on its own conversion event (not purchases) had to remind Parker in most chats not to use purchase CPA, which was many times higher than their real cost per result.

## What shipped

- **The user's format wins over a skill's output structure.** The scriptwriting skill's "Output contract precedence" now starts with the user's format: a template in the conversation or a standing rule in their user profile is delivered as given, with the skill's work inside it. The skill's own structure is the default for when they haven't given one. The Grounding Review and Voice Review blocks still follow as they are, and compliance still wins over the user's wording.
- **The same rule for every skill, in the voice.** The Parker output style adds one line: a format the user gives for a deliverable is the one to use; a skill's structure is only the default. Gates and closing lines still apply.
- **The brand's own KPI, not purchase CPA by default.** `creative-strategy-context/ad-account-analysis.md` section 2 now finds the KPI in order: the user's ask, a standing rule (user profile, running notes, `performance-targets-and-metrics.md`), the brand's custom metrics (`list_custom_metrics`), then the brand context. Purchase CPA (and NC CPA) is the fallback only when none exists. Parker says which KPI it used and never swaps the brand's KPI for purchase CPA because it is easier to pull.
- **The ad-account-analysis skill** measures the profitability lens on that KPI.

Not changed: the gates, the sign-off lines and the Brand Context Applied blocks.

## Migration

`migrations/v43.md` is a no-op: all four files are method docs or copied bundle files that the re-sync delivers.
