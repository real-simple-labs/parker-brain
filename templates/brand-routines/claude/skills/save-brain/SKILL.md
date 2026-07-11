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

**Credentials.** The remote already carries them: the repo is cloned with the `authenticated_clone_url` that `setup_parker_brain` (Parker MCP) returns, so the token lives in `origin` and plain git commands just work. The token lasts about **1 hour**, works only on this one repo, and looks like `https://x-access-token:<TOKEN>@github.com/parker-brain/<repo>.git`. When it expires, any pull or push fails with an auth error (403, 401, "could not read Username") — that is normal, not a problem. The fix is always the same two lines:

```bash
# call setup_parker_brain (Parker MCP) to get a fresh authenticated_clone_url, then:
git remote set-url origin <authenticated_clone_url>
# retry the command that failed
```

Never print the token to the user, never write it into any file in the repo, never commit it. (It sitting inside `.git/config` is fine — that file is local and never pushed.)

**Save and push** (the whole loop, in order):

```bash
git add -A && git commit -m "<plain summary of what changed>"   # commit first — rebase refuses a dirty tree
git pull --rebase origin main
git submodule update --init --recursive  # the pull can move the mount's pin; this makes the checkout follow it
git push origin main
```

Always `git push origin main` — spelled out, never a bare `git push` — so nothing depends on upstream config that may not exist. If the pull or push hits an auth error, refresh the credentials as above and retry; don't switch to any other auth.

**Clone** with `git clone --recurse-submodules <authenticated_clone_url> <folder>` into a persistent, user-accessible folder.

**Commit and push immediately — every time, without being asked and without asking.** The moment a batch of edits is done, run the save-and-push loop. Do not wait for the end of the session, do not accumulate work locally, and never ask the user "should I commit/save this?" — the yes they gave to the work *is* the yes to saving it; an unsaved brain is a broken promise, not a pending question. Other people and scheduled routines read this repo: unpushed work doesn't exist for them, and two sessions editing unpushed copies is how work gets destroyed. Small commits with plain messages, pushed right away. Before ending any turn that touched a file, check yourself: if the tree is dirty or a commit is unpushed, the turn isn't finished — run the loop, then reply. The one exception is the user themselves: if they explicitly say not to commit or not to push, honor that — and close your reply with one plain line that the changes are unsaved until they say the word, so it never silently becomes permanent.

**Pull before you read or edit** anything that might have moved — start of session, start of a routine, before a batch of edits. `git pull --rebase origin main`, always followed by `git submodule update --init --recursive` — the pull alone can advance the `parker-system/` pin while leaving the old files checked out, which means reading stale method. The session-start hook attempts this pull for you when the working tree is clean; if it reports a failure, fixing the pull is the first job of the session, before any other work.

**Conflicts: resolve best-effort, prefer keeping both sides.** Brain files are additive — notes, entries, docs — so when both sides changed a file, keeping both changes is almost always right. Never discard a teammate's lines to make a conflict go away, never `git reset --hard` away content you didn't write, and never force-push (there's no branch protection; a force-push can erase someone's work). If a conflict is genuinely unresolvable, commit your side to a clearly named file, push, and tell the user plainly what needs a human eye.

**No branches, no pull requests.** The brain works directly on `main`. Don't create feature branches, don't open PRs, don't use `gh` at all — `gh` runs on the user's personal login, which has no business in a managed repo.

**When auth fails** (403, 401, "could not read Username", token expired): don't retry with other credentials and don't fall back to `gh`. Call `setup_parker_brain` again — it always mints a fresh token — `git remote set-url origin <authenticated_clone_url>`, and retry once.

## Talking to the user about all this

The user is usually not a git person. Say "saved your brain," "downloaded the latest version," "your teammate's changes came in" — not "pushed to main," "rebased," "resolved a merge conflict." If something went wrong, say what it means for them ("your last hour of notes is safe, but I need a fresh connection to save it — one moment") and fix it.

## Hard rules

- Never the user's own GitHub login on a managed repo. Never `gh`. Never a bare `git push`.
- The token is a secret: not in chat, not in any committed file. Living in the remote URL is fine — that's the design.
- Never force-push. Never delete or overwrite a teammate's work to simplify a conflict.
- Clone and pull with submodules, always.
- **Every change is committed and pushed the moment it's done. No batching for later, no ending the turn dirty, and never asking the user for permission to save — saving is part of the work, not a separate favor.** Only an explicit "don't commit/push" from the user overrides this; then say plainly, at the end of the turn, that the work sits unsaved.
- Auth error → `setup_parker_brain` → `git remote set-url origin <fresh url>` → retry. That's the whole playbook.
- Self-hosted repos are exempt from the credential rules — check the origin before enforcing.
