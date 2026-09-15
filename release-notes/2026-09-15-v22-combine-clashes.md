# v22 — clashes are combined in the files (2026-09-15)

When the same lines of a brain file change on someone's machine and on the shared copy, Parker Desktop pauses that brain. Until now the app asked the assistant to fix that with `git pull --rebase` and a push - which never worked for a customer: the assistant holds no credentials on a managed brain, Codex's sandbox has no network, and from v18 the guard blocked those commands anyway.

The release after Parker Desktop 0.15.4 does the git part itself. Its Fix button merges the shared version into the folder, which leaves both versions in each clashing file between git's marker lines (`<<<<<<<`, `=======` and `>>>>>>>`), and hands Claude Code or Codex a request to edit the files until none of those three lines is left in any clash block. Once that is done, the app saves and shares the result. Files nobody needs to read (a picture, a file deleted on one side) are settled by the app on the spot, and an Undo puts everything back.

## What shipped

- **`git-guard.py`:** `git add`, a plain `git commit` and `git merge` pass on a managed brain, so an assistant that finishes a combine by hand is not blocked halfway. `push`, `pull`, `fetch`, `rebase`, `commit --amend`, `merge --abort` and `merge --quit` (undoing is the person's call, in the app) stay blocked. The block message names the clash flow.
- **`save-brain`:** a new section, "When Parker paused the folder on a clash": what the marks mean, what to do, what not to do, and how to check where things stand.
- **Brand `AGENTS.md`, `session-start.py`, the brand `CLAUDE.md` template:** the same rule in one sentence each - edit the marked files until no mark is left and stop; the app saves and shares.
- **`system/brain-sync.md`:** the maintainer contract gains a "Clashes" section (the app does the git, the assistant does the text) and the guard's verb list is updated. **`system/codex-support.md`:** combining needs no network.
- **Tests:** the guard's allowed and blocked lists cover the new verbs.

## Migration

`migrations/v22.md` is a no-op: the bundle re-sync delivers everything.
