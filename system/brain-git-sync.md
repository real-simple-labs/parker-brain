# Brain git sync — how a brand brain talks to GitHub, and how we make agents do it right

The runtime procedure lives in the routine bundle as the `save-brain` skill (`templates/brand-routines/claude/skills/save-brain/SKILL.md`, shipped to brains at `.claude/skills/save-brain/`). This doc is the maintainer's side: the facts the procedure rests on, the enforcement stack that makes agents actually follow it, and why each piece exists. Change the procedure there, check the reasoning here.

## The facts underneath (from the Parker MCP server)

- Managed brains live in the **`parker-brain` GitHub org** (server env `GITHUB_PARKER_ORG`), one private repo per brand, named `<org>-<brand>` or `<brand>`, provisioned by `setup_parker_brain`.
- Every `setup_parker_brain` call re-mints a **GitHub App installation token**: ≤1 hour, scoped to that single repo, `contents: write` only. It arrives embedded in `authenticated_clone_url` as `https://x-access-token:<TOKEN>@github.com/parker-brain/<repo>.git`. There is no rotation — expired means call the tool again.
- Human collaborators are added at write permission via the same tool (`github_username` param, invitation flow). Their personal auth is for *their* clones on *their* machines — never for the agent.
- Repos have **no branch protection** and the default branch is whatever the first push created (`main`). This is why the procedure bans force-pushes and branches outright rather than relying on GitHub to stop them.

## Why the agent must never use the user's auth or `gh`

The user usually has no working GitHub auth in the session at all (they were invited, or never touched GitHub). When they *do*, using it misattributes commits, sidesteps the access Parker manages, and — for `gh` specifically — habituates a tool that will be missing or wrongly-logged-in in most brand sessions. One credential path means one failure mode and one fix: re-call the tool.

## Credentials live in the remote (and why we stopped cleaning them out)

The repo is cloned with the token-embedded `authenticated_clone_url`, and that URL simply stays in `origin`. Plain `git pull --rebase origin main` and `git push origin main` work for the token's hour; when one fails with an auth error, the playbook is two lines — call `setup_parker_brain` again, `git remote set-url origin <fresh url>` — and retry. Explicit `origin main` on every push so nothing depends on upstream config that a fresh clone doesn't have.

An earlier revision bracketed every sync with token-in/token-out `set-url` calls so no secret lingered in `.git/config`. In practice the ceremony was worse than the risk: agents found the sequence complicated enough to skip pushes entirely or stall asking the user, which loses real work — while the "secret" it protected is local-only (`.git/config` is never pushed), scoped to this one repo, `contents:write` only, and dead within the hour. An expired token in the remote now costs exactly one clear auth error followed by the two-line refresh, which is the same recovery a clean remote needed anyway. Simplicity won.

## Detecting the self-hosted exception

A rare team hosts the brain in their own GitHub instead of the managed org. Detection is the origin URL: `github.com/parker-brain/…` → managed, anything else → theirs, their auth, `gh` allowed. A repo with no remote yet counts as managed when `parker_config.json` exists (mid-build). Both the skill and the guard hook use exactly this test, so the exception needs no configuration.

## The enforcement stack (instructions alone don't survive contact)

1. **`git-guard.py`** — PreToolUse hook on Bash in the shipped `.claude/settings.json`. Deterministic: on managed repos it blocks `gh`, credential-less `push`/`pull`/`fetch`, any force-push, and clones missing `--recurse-submodules`; its block message teaches the two-line credential refresh at the moment of the mistake. Ops on the public mount (`git -C parker-system …`) pass through. It fails open internally, and its settings entry must never get the `2>/dev/null || true` wrapper the other hooks use — exit code 2 and stderr are the mechanism.
2. **`session-start.py`** — the pull-first enforcement. On session start it *runs* `git pull --rebase origin main` + submodule update itself when the working tree is clean, instead of only reminding; on a dirty tree or a failure (expired token, offline) it reports loudly and makes fixing the pull the session's first job.
3. **`commit-guard.py`** — Stop hook, the push-always enforcement. When a turn is about to end on a managed repo with uncommitted changes or commits that never got pushed, it blocks the stop once and tells the agent to run the save-and-push loop. The `stop_hook_active` flag prevents loops: the second stop passes with the warning logged rather than re-blocking.
4. **The `save-brain` skill** — the full procedure, discoverable by name and description for anything save/sync/clone-shaped, and the reference every guard message points to. Self-contained on purpose: git trouble often happens exactly when the mount is empty.
5. **The brand `CLAUDE.md` section** ("How this brain saves itself") — always loaded, carries the two absolutes: pull first, and commit-and-push immediately without ever asking the user for permission to save.
6. **The tool's own returned message** (mevin2 side) — the one channel that reaches sessions outside the repo, e.g. claude.ai during onboarding. It should teach the same keep-credentials-in-the-remote flow; keeping it consistent with the skill is a cross-repo duty.

Layers 1–5 travel in the routine bundle, so `sync-executable-layer.py` delivers them to standing brains on a pin bump; only a team-customized `settings.json` needs the migration's manual merge.
