# 2026-07-10 — v4: the fast update

A routine `/update-brain` run was taking 5+ minutes: the agent hand-diffed every copied skill after the pin bump and turned each difference into a long question. Now the copied executable layer is re-synced by a script and the whole update is one short question and one short summary.

## What shipped

- **`scripts/sync-executable-layer.py`** — deterministic re-sync of everything the build copied out of the mount (craft + routine skills, review-gate agents, hooks, checker scripts, schedule recipes). Hash-compares each brand copy against the *old* pinned tag: untouched → refresh silently, team-edited → theirs, listed; team-deleted → stays deleted; nothing is ever removed. `--dry-run` feeds the scheduled digest. The bundle map inside it is the machine-readable twin of the onboarding-runner's copy list — change one, change both.
- **`/update-brain` template** — the on-a-yes step calls the script instead of hand-diffing; a new "Keep it quick" contract caps the exchange at one short question (Take it / Skip / What changed?) and a ≤5-line summary; the canonical-build hole walk is now a silent existence check that lands as one digest line, with generation only on explicit ask. Offers-only doctrine for scheduled runs is unchanged.
- **`migrations/README.md`** — division of labor so migrations never fight the script: migrations run first and never touch bundle-map paths; the script runs once at the end.
- **Brand `CLAUDE.md` guidance** (template + stamped by `migrations/v4.md`) — brand adaptations go in brand docs first, not in copied skill files, so the team-edited pile stays small and updates stay quick.

## Why

The pin-move architecture already made the method delivery atomic; the interactive per-file resync and the every-run hole walk were the leftover slow parts. Mechanizing them turns a no-op release bump into a two-minute exchange.

## Follow-ups

Cut the `v4` tag after merge — nothing reaches a standing brain until the tag exists.
