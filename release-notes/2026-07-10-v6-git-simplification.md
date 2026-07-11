# 2026-07-10 — v6: simpler git flow, enforced pull-first and push-always

v5's procedure was correct but too ceremonial, and two failure modes survived it: agents skipped the start-of-session pull, and agents ended turns with work uncommitted, unpushed, or held hostage to a "want me to commit this?" question.

## What shipped

- **Credentials live in the remote.** The token-in/token-out `set-url` bracket around every push is gone. The repo keeps the `authenticated_clone_url` in `origin`; plain `git pull --rebase origin main` and `git push origin main` just work, and an auth error means the two-line refresh: `setup_parker_brain` → `git remote set-url origin <fresh url>` → retry. Rationale for the reversal in `system/brain-git-sync.md`: the ceremony caused skipped pushes, while the secret it protected is local-only, single-repo, `contents:write`, and dead within the hour.
- **`session-start.py` now pulls instead of reminding.** On the standard layout, with a clean tree and a remote present, it runs `git pull --rebase origin main` + submodule update itself (never interactive, fails loud with the exact fix — expired-credential failures get the two-line refresh spelled out, a dirty tree gets "commit and push this first").
- **Never-ask mandate, prompt-level by design.** `save-brain` and the brand `CLAUDE.md` template now state it as an absolute: every change is committed and pushed the moment it's done, asking the user for permission to save is itself a failure — their yes to the work was the yes to saving it — and every turn that touched a file ends with a self-check that the tree is clean and pushed. The single override: the user explicitly says not to commit/push, in which case the reply closes with a plain "this is unsaved until you say so." (A Stop-hook enforcer was built and deliberately dropped: a blocking guard risks trapping turns behind a persistent git error and can't see an explicit "don't commit.")
- **Factory policy: every release ships a `migrations/vN.md`.** No more absence-means-nothing: a release with no brand-side work ships a one-liner no-op, so an updating brain never guesses whether a missing file means "nothing to do" or "someone forgot." `migrations/README.md`, `CLAUDE.md`, and `update-parker-skill` step 9 updated together (this also retired the stale ".claude bundle changes need a migration" trigger from before the sync script existed).

## Why

Enforcement has to sit where the failure happens: the pull was skipped at session start, so the session-start hook now does it; the push was skipped at turn end, so the Stop hook now catches it; the procedure was skipped for being complicated, so it got simple.

## Follow-ups

- Cut the `v6` tag once this merges.
