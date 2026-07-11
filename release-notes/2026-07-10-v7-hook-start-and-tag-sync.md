# 2026-07-10 — v7: reliable hook startup and factory tag synchronization

## What shipped

- **Hooks no longer block a session when their scripts are missing.** The shipped settings keep the `git-guard` active when its script exists, while a missing script or off-root launch cleanly fails open instead of being mistaken for an intentional guard block.
- **`/update-brain` now mirrors factory release tags before it compares releases.** It runs `git -C parker-system fetch origin --prune --prune-tags`, which accepts a moved release tag and removes a deleted one. A stale local tag therefore cannot block the update check or be treated as the newest release.
- **Tag cleanup is intentionally not part of normal saves or session start.** A save only needs the brand repo and its checked-out submodule pin. The session-start hook pulls that state and, if its one-hour credential has expired, reports the exact `setup_parker_brain` → `git remote set-url` recovery before any work proceeds.

## Why

Git treats tags as immutable by default. `git fetch --tags` rejects a remote tag that moved and retains tags removed from the remote. That behavior is wrong for the one place Parker compares local tag refs to discover factory releases, but there is no reason to pay for or depend on tag synchronization during ordinary save and pull flows.

## Follow-ups

- Cut the `v7` tag once this merges.
