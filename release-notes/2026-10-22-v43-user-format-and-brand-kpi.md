# v43 — the user's format and the brand's own KPI come first (2026-10-22)

Two things kept going wrong in live chats. A user gave Parker their own brief template, said to use it from now on, and still got the method's script brief back, four times in one session. And a brand that measures its ads on its own conversion event (not purchases) had to remind Parker in most chats not to use purchase CPA, which was many times higher than their real cost per result.

## What shipped

- **The user's format wins for the deliverable they gave it for.** The scriptwriting skill's "Output contract precedence" now starts with the user's format: a brief or script template from the conversation or a standing rule is delivered as given, with the skill's work inside it. The skill's own structure is the default for when they haven't given one. The What it's built from, Grounding Review and Voice Review blocks still follow as they are, and compliance still wins over the user's wording. A brief template doesn't reshape other deliverables: a 1:1 adaptation still ships the four parts from `adapting-scripts.md`.
- **Kept "from now on" where the deliverable looks.** A brief template goes word for word into `briefs/_brief-template.md`, which every brief already follows. Any other standing format goes through `self-improvement-intake`, which picks brand or personal scope.
- **The same rule in the voice, with its limits.** The Parker output style adds one bullet: a format the user gives is used for that kind of deliverable. It never drops what a skill requires every output to carry (review blocks, Brand Context Applied, the closing line), and it doesn't apply to the weekly creative report (fixed schema) or to 1:1 recreations.
- **The brand's own KPI, not purchase CPA by default.** `creative-strategy-context/ad-account-analysis.md` section 2 finds the KPI in order: the user's ask, a standing rule (the north star in `running-notes/brand-rules.md`, `running-notes/success-definition.md`, the user profile, `performance-targets-and-metrics.md`), the brand's custom metrics (`list_custom_metrics`), then the brand context. When several custom metrics could be the goal and nothing names the primary one, Parker asks and records the answer as the north star in `brand-rules.md`. Purchase CPA (and NC CPA) is the fallback only when none exists. Parker says which KPI it used and never swaps the brand's KPI for purchase CPA because it is easier to pull. The profitability table reads the brand's own event in place of purchases when that is the KPI.
- **The ad-account-analysis skill follows it.** The skill's profitability lens, `strategy.md`, and the account-audit and single-ad-diagnosis inputs ask for the brand's primary KPI (purchases and CPA only when that is the KPI) instead of "target CPA or NC CPA".

Not changed: the gates, the sign-off lines and the Brand Context Applied blocks.

## Migration

`migrations/v43.md` is a no-op: every changed file is a method doc or a copied bundle file that the re-sync delivers.
