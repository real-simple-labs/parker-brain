# v21 — optional token usage logging

Brain builds previously had no repo-visible usage accounting. Parent work,
separate fidelity reviews, and full retries could not be compared reliably.
Raw transcript sums also inflate totals through repeated streaming records and
cumulative snapshots.

- `usage_logging.enabled: true` in `parker_config.json` opts a repository in.
  Missing config stays off, including after setup or updates.
- A standard-library collector reads available Claude Code and Codex counters,
  deduplicates replay, separates fresh/cache-read/cache-creation input, and treats
  reasoning as an output subset. Unknown counters remain unknown.
- Hooks checkpoint locally; normal saves export metadata-only `.usage/` files.
  Ignored live state prevents Stop/save loops. Final post-save counters travel
  with the next normal save.
- Recovery and reports merge exports from multiple machines for the same actor,
  preserving distinct requests and counting overlapping cache/token usage once.
- Builds can label writers, fidelity reviews, retries, and final verification.
  Reports show parent/worker totals, model/prompt/stage groups, cache hit rates,
  and partial coverage. No extra model calls or dollar-price assumptions.
- Parker Desktop remains the sync owner: export writes files before save
  confirmation, with no staging, commits, pulls, or pushes.
- Both factory and brand wiring ship together. Existing brains receive the
  collector and save step through executable-layer sync; logging remains off.

Validation: sanitized accounting fixtures, actual committed hook commands,
concurrent writers, Git cleanliness, executable-layer upgrades, and an offline
installed-Codex probe with cached and reasoning usage. Transcript formats are
runtime-owned; unavailable transcripts and unknown fork boundaries stay partial.
No marketing-method changes, training-corpus edits, or brand-output reruns.

Contract: `system/usage-logging.md`. Migration: `migrations/v21.md`.
