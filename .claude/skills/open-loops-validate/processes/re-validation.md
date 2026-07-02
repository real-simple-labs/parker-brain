# Re-validation

A validated insight is true as of the date it was confirmed, not forever. Markets move, rivals reposition, customer language drifts, and a finding that was solid a quarter ago can quietly go stale. Re-validation is how Parker keeps the brand profile from carrying confident insights that have aged out.

## Stamp freshness when a loop validates

Every validated insight is written with two dates: when it was validated, and when it should be re-checked. The re-check date is set by how volatile the thing is:

- **Fast-moving** — a competitor's positioning, what is winning in the feed, live customer sentiment — re-checks sooner, because the ground under it shifts in weeks.
- **Slow-moving** — a structural fact about the category, a durable customer truth, the brand's own product economics — re-checks later, because it changes on the order of quarters.

The point is not a fixed interval; it is that every confirmed insight in the brand profile shows how fresh it is, so a reader knows which parts of the picture are current and which are due for a look.

## How a re-validation runs

A scheduled re-validation re-runs the original test against current data and compares. Three outcomes:

- **Still holds** — the evidence is current; re-stamp the insight with a new date and a new re-check date. Nothing else changes.
- **Shifted** — the evidence has moved. The insight is updated to what is true now, the change is recorded, and the brand profile reflects the new read. A shift is itself a finding worth telling the user about.
- **No longer holds** — the evidence has reversed or evaporated. The insight is retired from the brand profile and moved to a dead-end with the date it stopped being true, so the brand stops relying on it.

## Where it lives

Scheduled re-validations live in `re-validations/scheduled/`; their results are stored in `re-validations/results/[YYYY-MM]/`. The freshness of every confirmed insight is visible from its date stamp in the brand profile and in `running-notes/recent-validations.md`, so the maturity of the brand's understanding is always legible — what is freshly confirmed, what is holding, and what is due for another look.
