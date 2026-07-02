# Brand-profile prompts

The generation prompts for the brand one-pager and its sub-context docs. Each prompt is the thing Parker runs to produce a filled doc. Each one teaches the model the why and the how alongside the what, and each is fully self-contained: it carries its own copy of the working method, so it does not depend on any other file at runtime.

The brand profile is a narrative one-pager, `brand-profile.md`, built on top of a set of sub-context docs. Each sub-context doc covers one slice of the brand. The narrative synthesizes them and rolls up the open loops, which kicks off the open-loops pipeline.

## Files

- **`_foundations.md`** — authoring reference, not a runtime dependency. The canonical wording of the working method that every prompt embeds. Edit it here and propagate into the prompts so the teaching stays identical across all of them.
- **`brand-profile-narrative.md`** — produces `brand-profile.md`, the narrative synthesis across all sub-context docs, including the consolidated open-loops roll-up.

### Sub-context doc prompts

- `brand-identity-analysis.md` — what the brand is, who they say they are, tone, credibility, legal guardrails. The grounding and anti-drift anchor.
- `operations-and-team.md` — team, bottlenecks, what they want automated, who owns what. Mostly brand-only-knowable.
- `website-and-product-audit.md` — full SKU map, differentiators, known issues, LTV vectors, persona-to-SKU mapping, entry-point hypothesis.
- `organic-channels-audit.md` — the brand's own organic across platforms, read through the organic-to-paid mechanism.
- `ad-account-evaluation.md` — the brand's own running ads, audited fresh-eyes first then with performance data, resolved to a two-sentence diagnosis with three creative swings, a double-down list, and a retire list.
- `performance-targets-and-metrics.md` — targets, spend, KPIs, attribution stack, the retail-attribution gap. Refreshed quarterly.
- `reputation-analysis.md` — the consumer's-eye view: search, press, retail footprint, credibility, with sentiment trajectory as the deliverable.
- `community-and-forums.md` — unprompted category conversation, objections, gold nuggets.
- `customer-journey-and-persona-discovery.md` — the buyer journey and behavioral dynamics that feed the persona work.
- `category-and-market-research.md` — category size and maturity, behavioral barriers, trends, industry-wide trust events.
- `competitive-landscape.md` — the map and router of the field: competitor, inspo, affinity, emerging, plus comparison risk tolerance.

### Handled elsewhere

- **Reviews and customer language** is its own full context doc, produced by the customer-review and voice-of-customer audit in `parker-system/prompts/personas/` and `parker-system/prompts/voice-of-customer/`. The brand profile references its output rather than generating it here.
- **brand-notes-from-org** — the running-notes memory doc accumulated from org conversations over time. Part of the memory bundle, adjacent to the brand profile, not a sub-context doc.

## Conventions baked into every prompt

- Teach the model as if it has no prior context, including primitives like what an open loop is and how to find one.
- Mark every claim stated, inferred, or verified, and never launder a stated claim into a fact.
- A count is not significance: weigh recurrence against the denominator and the spread, and state the interpretation.
- A named blank beats a confident guess.
- Carry the source of every claim, and route brand-only-knowable questions to the brand.
- End every doc with an Open loops section written as real, actionable questions.
- Refresh by taking the prior version as context, not by rewriting from scratch.
- No parenthetical asides, and describe the shape of what to capture rather than listing examples to pattern-match against.
