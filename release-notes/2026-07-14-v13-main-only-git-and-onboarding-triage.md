# 2026-07-14 — v13: everything lands on main, and onboarding checks what exists first

Two field fixes. Hosted sessions were stranding brain work on harness-assigned branches, and onboarding was pitching a multi-hour build to people whose brain already existed.

## What shipped

- **Everything lands on `main` — the explicit permission hosted harnesses ask for.** Hosted Claude Code sessions (cloud builds, the scheduled routines) arrive with a harness instruction like "develop on branch `claude/…`; NEVER push to a different branch without explicit permission." The brain's docs said "no branches, no PRs" but never granted that permission, so agents obeyed the harness and parked work on side branches nobody would ever review or merge. The `/save-brain` canonical rule now grants it in writing: work on the assigned branch if the harness insists, then deliver every commit with `git push origin HEAD:main`. Same grant added to the brand `CLAUDE.md` template (the always-loaded contract — the one surface guaranteed to be in context alongside the harness instruction), the onboarding runner's save step, and both routine-bundle README summaries. The framing does the teaching: branch-parked work is not "awaiting review," it is lost — invisible to every other session, routine, and teammate, exactly like unpushed work.
- **Onboarding detects an existing built brain before the build pitch** (#53, merged separately). New runner section ahead of the orientation: resolve the brand quietly (no "is this the right brand?" question when it's unambiguous), call `setup_parker_brain` (idempotent; `reused_existing: true` reveals a repo), clone, and route — fully built brains get retrieved and handed to `/get-started` with no multi-hour pitch and no go/no-go, mid-builds get the resume offer, only a real cold start gets the orientation and gate. The `set-up-brain` skill's step 0 carries the same triage, and its description now names retrieval as a trigger so a pasted "Retrieve my existing Parker brain" prompt routes there.

`/save-brain` and the READMEs ride the copied bundle; the runner rides the mount; the `CLAUDE.md` template and skill-description changes shape new builds only. `migrations/v13.md` is a no-op.

## Follow-ups

- Cut the `v13` tag once this merges.
- Dashboard (outside this repo): swap the copiable kickoff prompt to "Retrieve my existing Parker brain for <brand>" once the backend sees a completed setup run — the skill description already routes that phrasing.
