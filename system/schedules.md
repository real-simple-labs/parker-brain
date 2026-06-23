# Schedules — keeping a brand brain running on its own

A brand brain is a repository. Clone it into a Claude Code instance and it is a living thing that can run jobs against itself. A **schedule** is one of those jobs: a cron routine that runs inside the cloned brain to keep its docs current without anyone asking. The nightly dreaming pass, a weekly idea harvest, a refresh sweep over stale docs — each is a schedule.

This is the repo-native answer to "how does the brain stay alive when no one is typing." Dreaming proposes schedules (the third of its five buckets); self-improvement creates, edits, pauses, and removes them; and the routines themselves run on the back end against the repo.

## Schedules are not workflows

Keep these two apart — they look similar and are not the same thing.

- **Workflows** are a **Parker-MCP product** concept: a recurring task a user hands to the hosted Parker product, which runs it through the MCP surface. They live in `workflows/` and call out to the MCP.
- **Schedules** are **repo-native**: cron routines that run inside *this brand brain repo*, in a Claude Code instance, against the files in the repo. They do not call the Parker MCP. If you cloned the brain to your own machine and pointed Claude Code at it, the schedules are what would run to update the docs.

The distinction matters because the brand brain is meant to be portable. A workflow assumes the hosted product is in the loop; a schedule assumes only the repo and a Claude Code runner. When in doubt: if it keeps the *repo's own docs* fresh and needs nothing but the repo to run, it is a schedule.

## Schedules and the refresh cadence

`system/refresh-cadence.md` says *when* a doc goes stale — every doc stamps a `refresh_by`, and the aggregated view lives at `running-notes/refresh-schedule.md`. That is the **clock**. A schedule is the **worker that acts on the clock**: a refresh schedule wakes up, reads `running-notes/refresh-schedule.md`, finds what is overdue, and re-runs the generating prompt. Refresh cadence decides what is due; the schedule does the re-running. The two are complementary — cadence without a schedule still needs a human to notice and re-run; a schedule without cadence has nothing to check against.

Not every schedule is a refresh job. The other common ones:

- **Dreaming** — run the daily dreaming pass over the day's comms and write the proposals (see `self-improvement/dreaming-system.md`).
- **Idea harvest** — scan the configured inspo sources on a weekly cadence and log new `[~]` ideas to the bank.
- **Open-loops roll-up** — collect, weight, and route open loops on the roll-up cadence.
- **Refresh sweep** — re-run docs past their `refresh_by`.

## The `schedules/` folder

Each brand brain carries a `schedules/` folder, one file per routine, mirroring the shape of `workflows/`:

```
z-brands/[brand]/schedules/
    README.md
    [schedule-slug].md          ← an active, confirmed routine
    proposed/[schedule-slug].md ← dreaming-suggested, awaiting user confirmation
```

Each schedule file states:

- **Task** — what the routine does, in one line.
- **Cadence** — the cron expression and a plain-English reading of it ("0 6 * * * — every day at 6am").
- **Runs** — the prompt or skill it invokes.
- **Reads / updates** — the data sources it reads and the docs it writes.
- **Delivers** — what the user gets when it finishes (a proposal set, a refreshed doc, a notification).
- **Status** — proposed, active, paused, or retired.
- **Origin** — the dreaming run or conversation that proposed it.

A proposed schedule does not run until the user confirms it and it moves out of `proposed/`. Pausing a schedule keeps the file and flips its status; removing one archives the file with its reasoning, so a retired routine still teaches what was tried.

## The runner

The routines run as **Claude Code scheduled agents** — the `/schedule` skill and the cron machinery behind it. The repo carries the *definition* of each schedule (the `schedules/` file); the Claude Code instance the brain is cloned into carries the *execution*. Standing up a schedule means writing its file here and registering the matching cron routine in the instance; the two stay in sync, with the file as the source of truth for what the routine is supposed to do.
