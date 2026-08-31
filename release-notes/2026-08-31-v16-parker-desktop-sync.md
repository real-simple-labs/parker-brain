# v16 — Parker Desktop owns the sync (2026-08-31)

The whole git layer a brand brain used to carry — minted tokens, credential files, pull-first hooks, push-immediately mandates, three revisions of ceremony (v5 → v8) — is retired. The **Parker Desktop app** (https://app.heyparker.ai/dashboard/parker-desktop) now creates the brand's repo, syncs its folder to the team's machines, and keeps every change flowing both ways. The agent's job shrinks to the thing it was always actually doing: writing files.

## What shipped

- **Repo creation moves into the app.** Teams set up the brand's repository in Parker Desktop directly; the app then opens a Claude session inside the synced folder to continue the setup. There is no provisioning tool call in the flow anymore — if an older Parker MCP still exposes `setup_parker_brain`, agents don't provision through it and ignore any credentials any tool result carries.
- **`save-brain` rewritten** (routine bundle) — from a git procedure to a one-step truth: write the file, the app syncs it. Covers finding the brain folder via the **`PARKER_BRAIN_DIR`** environment variable the app sets (one subfolder per brand; fallback is asking the user), what to do when the folder isn't syncing (point at the app, or a technical team wires its own git), and the self-managed exception, still detected from the origin URL.
- **`git-guard.py` simplified** (routine bundle) — on managed repos it now blocks *all* git and `gh` aimed at the brand repo (push, pull, fetch, clone, commit, rebase, merge, reset, set-url), because two sync engines racing over one folder is how work gets destroyed. Mount operations (`git -C parker-system …`, `git submodule …`) pass — they're local, credential-free, and still the agent's job for `/update-brain`'s pin move and the empty-mount heal.
- **`session-start.py` simplified** (routine bundle) — no more start-of-session pull or credential recovery; it checks the method mount and states the sync model in one line.
- **`settings.json`** (routine bundle) — the four credential-write `allow` rules are gone; the deny rules keeping the mount read-only stay.
- **Brand `CLAUDE.md` template** — "How this brain saves itself" and the git ground-truth bullet rewritten to the no-git model.
- **Onboarding rewritten around the app** — the runner and `/set-up-brain` now start from the folder Parker Desktop opened, never clone, never touch credentials, and end by confirming the sync is live instead of pushing to GitHub. The factory `README.md` quickstart sends people to the app first.
- **`update-brain` / `disconnect-factory`** — pin moves and decouples no longer stage or commit; the changed files save like any other change.
- **`system/brain-git-sync.md` → `system/brain-sync.md`** — the maintainer doc rewritten for the new model, including the open cross-team duties (the app must set `PARKER_BRAIN_DIR`; the old tool message still teaches the retired flow until the tool is retired).

## Migration

`migrations/v16.md` carries real steps: delete the stale credential file, introduce the team to Parker Desktop honestly (work is local-only until the app adopts the folder), strip the retired `allow` rules from a team-edited `settings.json`, and refresh the two git sections in the brand's root `CLAUDE.md`. Everything else rides the pin bump's re-sync.
