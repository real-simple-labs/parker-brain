# 2026-07-10 — v5: the git procedure

Agents kept mishandling git in brand brains: pushing with the user's own login, reaching for `gh`, bare `git push` with no upstream, clones without submodules, and stale 1-hour tokens left in the saved remote causing next-session 403 mysteries. v5 gives every brain one procedure and enforces it.

## What shipped

- **`save-brain` skill** (routine bundle) — the canonical procedure: credentials always minted fresh from `setup_parker_brain` (≤1h, single-repo, secret); every push is `git push origin main`, bracketed by token-in (`git remote set-url origin <authenticated_clone_url>`) and token-out (set-url back to the clean URL); clone and pull with submodules; commit often, push immediately; conflicts best-effort preferring both sides; never `gh`, never force-push, no branches or PRs; plain non-git language with the user. The self-hosted exception is detected from the origin URL: anything not under `github.com/parker-brain/` uses the team's own auth and skips the credential rules.
- **`git-guard.py`** (routine bundle, new PreToolUse hook on Bash) — deterministic enforcement at the moment of the mistake: on managed repos it blocks `gh`, credential-less `push`/`pull`/`fetch`, all force-pushes, and clones missing `--recurse-submodules`, with a block message that teaches the correct flow. Mount operations (`git -C parker-system …`) pass through; self-hosted repos are untouched; the hook fails open so a bug can never brick Bash. Registered in the shipped `.claude/settings.json` (deliberately without the `2>/dev/null || true` wrapper).
- **Brand `CLAUDE.md` template** — always-loaded "How this brain saves itself" section pointing at `/save-brain`; `migrations/v5.md` stamps it into standing brains and patches team-customized `settings.json`.
- **`system/brain-git-sync.md`** — maintainer doc: the MCP-server facts (App installation token, org, no branch protection), the token-hygiene rationale, the detection rule, and the four-layer enforcement stack.

## Why

Instructions alone don't survive contact — the failure mode is a reflexive `git push` mid-routine, not a considered decision. A named skill catches the deliberate moments; the hook catches the reflexive ones, free (no tokens, local process) and exactly when it matters.

## Follow-ups

- Cut the `v5` tag once this merges — nothing reaches a standing brain until the tag exists.
- Mevin2 side (cross-repo): align `setup_parker_brain`'s returned message with the clean-remote bracket — after teaching the authenticated clone, add "then set the remote back to the clean URL; put the token back in just before each push" so sessions outside the repo (claude.ai onboarding) learn the same pattern.
