# [brand] Schedules

Repo-native cron routines that run **inside this brain** to keep its docs current without anyone asking — the nightly dreaming pass, a weekly idea harvest, a refresh sweep over stale docs. Clone this repo into a Claude Code instance and the schedules are what run against it on the back end.

**Schedules are not workflows.** Workflows (`../workflows/`) are the Parker-MCP product surface and call out to the hosted product. A schedule needs nothing but this repo and a Claude Code runner. Full concept: the Parker brain's `parker-system/system/schedules.md`.

Schedules act on the **refresh cadence**, not instead of it: each doc stamps a `refresh_by` (the clock); a refresh schedule is the worker that wakes up, reads what's overdue, and re-runs the generating prompt.

## Structure

- `[schedule-slug].md` — an active, confirmed routine: task, cron cadence, what it runs, what it reads/updates, what it delivers, status, origin.
- `proposed/[schedule-slug].md` — dreaming-suggested routines awaiting user confirmation. A proposed schedule does not run until you confirm it and it moves out of `proposed/`.

## The standing routines

Six routines ship with this brain (jobs committed and live; the build arms the cron automatically at its stamp step — a brain cloned onto a *new* instance arrives un-armed, since schedules are per-account, so run `/setup-routines` there to register them):

- **`dream.md`** — daily, 05:00. Runs `/dream` over the day's comms → five-bucket proposals.
- **`research-loops.md`** — weekly, Wed 06:00. Runs `/research-loops`: rolls up the loops, advances them into hypotheses, runs the validations and due re-validations, aligns the docs with the findings.
- **`self-improve.md`** — weekly, Fri 16:00. Runs `/self-improve`: curates traces, disposes dreaming and research proposals.
- **`ideas-weekly.md`** — weekly, Mon 07:00. Runs `/harvest-ideas` then `/evaluate-ideas`.
- **`refresh-context.md`** — weekly, Mon 06:00. Runs `/refresh-context` over docs past their `refresh_by`.
- **`update-brain.md`** — weekly, Mon 05:30. Runs `/update-brain`: compares the brain against the current factory standard and its own canonical build, and writes the offer list — never applies without the user.

## The routine log

Every routine here prepends one entry to `running-notes/routine-log.md` each time it runs — scheduled or manual. That file is the append-only history of what the brain did on its own: what fired, when, what it changed, what it left, and why. It answers "did the weekly routine actually run, and what did it do," which a live due-date view (`refresh-schedule.md`) cannot. The log is stamped empty at build from `parker-system/templates/routine-log-template.md`; routines create it on first run if it is missing.

## The runner

Routines run as Claude Code scheduled agents (the `/schedule` skill / cron). This repo carries the *definition* of each schedule; the Claude Code instance carries the *execution*. The file here is the source of truth for what the routine is supposed to do — `/setup-routines` is the guided installer that arms the cron.
