# Routine-log template

> Instantiate this per brand at `running-notes/routine-log.md`. The onboarding runner stamps it empty at build time; every standing routine appends one entry each time it runs, newest first. Fill the `{{slots}}`, delete this header block. This is a running history, not a live view — the due-date view is `refresh-schedule.md`.

---

# Routine log — {{BRAND_NAME}}

The append-only record of everything the brain did on its own. Each standing routine (`/refresh-context`, `/research-loops`, `/dream`, `/harvest-ideas` + `/evaluate-ideas`, `/self-improve`, `/update-brain`) writes one entry here every time it runs, scheduled or manual, newest at the top. This is the history — what fired, when, what it changed, what it left, and why. It is distinct from `refresh-schedule.md`, which tracks only current due-dates; this file is never overwritten, only appended.

Read it to answer "what has the brain been doing," to see whether a scheduled routine actually fired, and to trace when a doc last changed and which run changed it.

## Entry shape

Each entry is one dated block. Keep it short — the routine's own deliverable holds the detail; this is the ledger line.

```
### {{YYYY-MM-DD HH:MM}} · {{routine}} · {{scheduled | manual}}
- **Checked:** what the run examined (e.g. 24 standing docs against refresh_by + the phase spine).
- **Did:** what it changed (docs re-run and re-stamped, loops advanced, ideas captured, proposals filed) — name each, or "nothing due."
- **Left:** what it deliberately did not do, and why (fresh, awaiting user, gated).
- **Surfaced:** any open loop, idea, conflict, or proposal it raised for a downstream routine or the user.
```

## Log

<!-- newest entries at the top; routines prepend here -->
