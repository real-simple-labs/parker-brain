---
name: save-brain
description: How this brain saves, syncs, and clones itself on GitHub — the required procedure for EVERY git push, pull, fetch, clone, commit, or gh command in a Parker Brain repo. Covers the credentials (the setup_parker_brain tool, never the user's own login, never gh), submodules, merge conflicts, and the rare self-hosted exception. Use whenever saving work to GitHub, syncing or updating the repo, cloning the brain, fixing a failed push or auth error, or when asked to save, back up, or share the brain.
---

# Save brain — sync with Parker's credentials, never the user's

Most Parker Brains live in Parker's own GitHub organization (`parker-brain`), created by the `setup_parker_brain` tool. The user usually has no GitHub login of their own wired up here, and even when they do, it must not be used: pushes with personal credentials fail, misattribute changes, or bypass the access Parker manages. The repo is shared — teammates and scheduled routines push to it too — so everything below is about staying in sync without stepping on anyone.

## First: which kind of repo is this?

Run `git remote get-url origin`.

- **Managed (the standard):** the URL is under `github.com/parker-brain/…` — or there's no remote yet but `parker_config.json` exists. Everything below applies.
- **Self-hosted (the rare exception):** the URL is under any other account or org. The team brought their own repo; use their normal auth — their `gh`, their credential helper, their remotes. None of the managed rules below apply, though the sync habits (pull first, commit often, push immediately) are still good advice.

## The managed procedure

**Credentials.** Call the `setup_parker_brain` tool (Parker MCP) with the brand id. Every call returns a fresh `authenticated_clone_url` — a token that lives about **1 hour**, works only on this one repo, and looks like `https://x-access-token:<TOKEN>@github.com/parker-brain/<repo>.git`. That URL is a secret: never print it to the user, never write it into any file in the repo, never commit it.

**Save and push** (the whole loop, in order):

```bash
git add -A && git commit -m "<plain summary of what changed>"   # commit first — rebase refuses a dirty tree
git remote set-url origin <authenticated_clone_url>   # fresh token in
git pull --rebase origin main
git submodule update --init              # keep the method mount populated
git push origin main
git remote set-url origin https://github.com/parker-brain/<repo>.git   # token out, last
```

Always `git push origin main` — spelled out, never a bare `git push` — so nothing depends on upstream config that may not exist. The last line matters: it takes the token back out of the repo's saved settings, so an expired secret never lingers on disk to cause mystery failures next session.

**Clone** with `git clone --recurse-submodules <authenticated_clone_url> <folder>` into a persistent, user-accessible folder — then immediately set the remote to the clean URL as above.

**Commit often, push immediately.** Never leave finished work sitting locally: other people and scheduled routines read this repo, and unpushed work doesn't exist for them. Small commits with plain messages beat one giant end-of-session dump.

**Pull before you read or edit** anything that might have moved — start of session, start of a routine, before a batch of edits. `--rebase`, plus `git submodule update --init`.

**Conflicts: resolve best-effort, prefer keeping both sides.** Brain files are additive — notes, entries, docs — so when both sides changed a file, keeping both changes is almost always right. Never discard a teammate's lines to make a conflict go away, never `git reset --hard` away content you didn't write, and never force-push (there's no branch protection; a force-push can erase someone's work). If a conflict is genuinely unresolvable, commit your side to a clearly named file, push, and tell the user plainly what needs a human eye.

**No branches, no pull requests.** The brain works directly on `main`. Don't create feature branches, don't open PRs, don't use `gh` at all — `gh` runs on the user's personal login, which has no business in a managed repo.

**When auth fails** (403, 401, "could not read Username", token expired): don't retry with other credentials and don't fall back to `gh`. Call `setup_parker_brain` again — it always mints a fresh token — set the remote, and retry once.

## Talking to the user about all this

The user is usually not a git person. Say "saved your brain," "downloaded the latest version," "your teammate's changes came in" — not "pushed to main," "rebased," "resolved a merge conflict." If something went wrong, say what it means for them ("your last hour of notes is safe, but I need a fresh connection to save it — one moment") and fix it.

## Hard rules

- Never the user's own GitHub login on a managed repo. Never `gh`. Never a bare `git push`.
- The token is a secret: not in chat, not in files, not in the saved remote after the push is done.
- Never force-push. Never delete or overwrite a teammate's work to simplify a conflict.
- Clone and pull with submodules, always.
- Commit often, push immediately; finished work never sits local.
- Self-hosted repos are exempt from the credential rules — check the origin before enforcing.
