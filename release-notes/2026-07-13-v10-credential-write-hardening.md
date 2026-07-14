# 2026-07-13 — v10: credential-write hardening after the first field weekend

v8 moved the token out of shell commands into `.git/parker-credentials`, written with the Write tool. Real scheduled runs surfaced two ways that Write itself fails — intermittently, which made git feel unreliable.

## What broke in the field

1. **The Write tool refuses to overwrite a file it hasn't read this session.** First-time setup passed (new file); the hourly *refresh* failed (file exists from the last mint). Agents saw "File has not been read yet" and stalled.
2. **Storage for temporary 1-hour credentials is not reliable**.

## What shipped

- **`rm -f .git/parker-credentials` before every re-Write** — baked into the skill's refresh steps, the session-start recovery message, and the guard's teaching text. The command carries no secret, and it works whether or not the stale file survived (git self-erases rejected lines, so existence isn't predictable).
- **`permissions.allow` rules in the bundle's `.claude/settings.json`** — `Write(.git/parker-credentials)` (both path anchors), the clone-time temp file, and the `rm -f` command. The permitted temporary token location is pre-approved by configuration the user's own repo carries. This is also what makes **headless scheduled runs** work.
- **Fallback guidance in `save-brain`** — "not been read yet" → `rm -f` and retry; a safety-layer block → ask the user in plain words through the question tool ("To save your work to GitHub I need to store a temporary access key (expires in about an hour) in the brain's local settings — OK?") and retry on their yes. Scheduled runs with nobody to ask commit locally and end loudly; the next interactive session finishes the push.
- **`migrations/v10.md`** — no-op for most brains (the re-sync delivers everything); one manual merge of the allow settings only if the team customized their `settings.json`.
- **Self-hosted gating in `session-start.py`** — the auth-failure recovery now applies the same origin test as `git-guard.py`; a self-hosted brain gets pointed at its own team auth instead of Parker's credential flow.
- **`gh` scoped to the actual rule** — the guard blocked every `gh` invocation in a managed repo, including GitHub searches and reads of unrelated repos (field complaint: agents fell back to web search). It now blocks only `gh` aimed at *this* repo: a bare `parker-brain/` org mention, or a repo-context subcommand (pr, issue, release, run, and kin) with no `-R`/`--repo` pointing elsewhere. Everything else passes.

## Follow-ups

- Cut the `v10` tag once this merges.
