# Brain git sync — how a brand brain talks to GitHub, and how we make agents do it right

The runtime procedure lives in the routine bundle as the `save-brain` skill (`templates/brand-routines/claude/skills/save-brain/SKILL.md`, shipped to brains at `.claude/skills/save-brain/`). This doc is the maintainer's side: the facts the procedure rests on, the enforcement stack that makes agents actually follow it, and why each piece exists. Change the procedure there, check the reasoning here.

## The facts underneath (from the Parker MCP server)

- Managed brains live in the **`parker-brain` GitHub org** (server env `GITHUB_PARKER_ORG`), one private repo per brand, named `<org>-<brand>` or `<brand>`, provisioned by `setup_parker_brain`.
- Every `setup_parker_brain` call re-mints a **GitHub App installation token**: ≤1 hour, scoped to that single repo, `contents: write` only. It arrives embedded in `authenticated_clone_url` as `https://x-access-token:<TOKEN>@github.com/parker-brain/<repo>.git`. There is no rotation — expired means call the tool again.
- Human collaborators are added at write permission via the same tool (`github_username` param, invitation flow). Their personal auth is for *their* clones on *their* machines — never for the agent.
- Repos have **no branch protection** and the default branch is whatever the first push created (`main`). This is why the procedure bans force-pushes and branches outright rather than relying on GitHub to stop them.

## Why the agent must never use the user's auth or `gh`

The user usually has no working GitHub auth in the session at all (they were invited, or never touched GitHub). When they *do*, using it misattributes commits, sidesteps the access Parker manages, and — for `gh` specifically — habituates a tool that will be missing or wrongly-logged-in in most brand sessions. One credential path means one failure mode and one fix: re-call the tool.

## Token hygiene: why the remote gets cleaned

Cloning or pushing with the token-embedded URL makes git store that URL — secret included — in `.git/config`. An hour later the token is dead and every future `git push origin main` fails with a 403 that looks like a permissions mystery. So the procedure brackets each sync: fresh token in (`git remote set-url origin <authenticated_clone_url>`), `git push origin main`, token out (`set-url` back to the clean URL). Explicit `origin main` on every push so nothing depends on upstream config that a fresh clone doesn't have.

## Detecting the self-hosted exception

A rare team hosts the brain in their own GitHub instead of the managed org. Detection is the origin URL: `github.com/parker-brain/…` → managed, anything else → theirs, their auth, `gh` allowed. A repo with no remote yet counts as managed when `parker_config.json` exists (mid-build). Both the skill and the guard hook use exactly this test, so the exception needs no configuration.

## The enforcement stack (instructions alone don't survive contact)

1. **`git-guard.py`** — PreToolUse hook on Bash in the shipped `.claude/settings.json`. Deterministic: on managed repos it blocks `gh`, credential-less `push`/`pull`/`fetch`, any force-push, and clones missing `--recurse-submodules`; its block message teaches the correct three-line flow at the moment of the mistake. Ops on the public mount (`git -C parker-system …`) pass through. It fails open internally, and its settings entry must never get the `2>/dev/null || true` wrapper the other hooks use — exit code 2 and stderr are the mechanism.
2. **The `save-brain` skill** — the full procedure, discoverable by name and description for anything save/sync/clone-shaped, and the reference the guard's messages point to. Self-contained on purpose: git trouble often happens exactly when the mount is empty.
3. **The brand `CLAUDE.md` section** ("How this brain saves itself") — always loaded, a few lines, points at the skill.
4. **The tool's own returned message** (mevin2 side) — the one channel that reaches sessions outside the repo, e.g. claude.ai during onboarding. It should teach the same clean-remote bracket; keeping it consistent with the skill is a cross-repo duty.

Layers 1–3 travel in the routine bundle, so `sync-executable-layer.py` delivers them to standing brains on a pin bump; only a team-customized `settings.json` needs the migration's manual merge.
