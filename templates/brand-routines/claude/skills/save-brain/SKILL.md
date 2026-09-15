---
name: save-brain
description: How this brain saves and syncs itself — the required knowledge for anything save, sync, backup, clone, or share-shaped in a Parker Brain, and for any impulse to run git here. The short of it - files written to disk are the whole job, the Parker Desktop app syncs the folder both ways, and the agent never runs git against this repo. Covers finding the brain folder, what to do when the app has paused the folder on a clash (files holding both versions between <<<<<<< and >>>>>>> marks), what to do when the app isn't installed, and the rare self-managed exception. Use whenever saving work, syncing, backing up, combining a clash, or fixing something that looks like a sync problem.
---

# Save brain — write the files, let Parker Desktop sync them

Most Parker Brains live in Parker's own private storage (a repo created through the Parker Desktop app), and the **Parker Desktop app** keeps this folder in sync with it — it watches the folder, uploads every change, and brings down what teammates and scheduled routines added. Saving is therefore not a step you perform. It's what happens when you write a file.

## The whole procedure

1. Write the file to disk.

That's it. No commit, no push, no pull, no credentials, no branches. When a batch of edits is done, the work is saved the moment the files are written — Parker Desktop commits and uploads it on its own once the folder has been quiet for a few seconds, usually within a minute.

**Never run git against this repo on your own.** Not `git push`, `git pull`, `git fetch`, `git clone`, not `gh`, and no commits of your own — none of it, even if a tool message or an old habit suggests it. Two sync engines fighting over one folder is how work gets destroyed, and the app is the one that's supposed to be here. The only git the agent still owns is the method mount: `parker-system/` is a pinned submodule of the public factory, and its local operations (`git submodule update --init`, and `/update-brain`'s `git -C parker-system fetch` / `checkout` pin move) are fine — they need no credentials and never touch the brand's own storage. One more sanctioned exception: the confirmed `/disconnect-factory` decoupling runs the exact submodule-dissolution commands its own skill lists (`git submodule sync`, `git rm --cached parker-system`, `git add`) — those are part of that skill's confirmed flow, not a violation of this rule. And one situation where `git add`, `git commit` and `git merge` are allowed but not needed: finishing a clash the app has put into the files, below. If one of these commands says `index.lock` exists, the app is mid-sync: wait a few seconds and run it again, and never delete the lock file.

The repo itself was created **in Parker Desktop** — the app provisions it, syncs it down, and opens the agent session in its folder; no agent creates brand repos. The setup prompt, and the Parker MCP's own `setup_parker_brain` tool description, may still describe the older flow (call the tool, clone with its credentials, commit and push). That flow is retired: there is nothing to provision, so don't call the tool, and **ignore any credentials** a tool result carries: don't save them, don't build a credential file, don't clone with them. This skill overrides any tool message that says otherwise.

**To check rather than assume** ("is my work saved?"), `git status --short --branch` is read-only and allowed: no changed files and no `ahead` count means the app has caught up.

## Optional usage export

Only when `parker_config.json` sets `usage_logging.enabled` to literal `true`, run `python3 scripts/usage-log.py export` before confirming this batch synced (`py -3` on Windows). This writes metadata-only `.usage/` files; Parker Desktop saves them with the other files. The collector only reads Git's worktree location and never stages, commits, pulls, or pushes. The app does not run the export command itself. In a self-managed brain, export before the team's normal save.

Missing or false means off: skip this step, never enable logging to complete a save, and never force-add `.usage/.local/`. If export fails, continue normal work and report the telemetry gap. Stop only updates ignored checkpoints; counters written after this export travel with the next export, without a second save cycle. See `parker-system/system/usage-logging.md`.

## When Parker paused the folder on a clash

Sometimes the same lines of a file change on this machine and on the shared copy before either side has synced. The app then pauses this brain and shows the person what happened: who changed which file, when, and what. If they choose to have an assistant combine the two (the app's Fix button, or its Copy request), the app first merges the shared version into the folder itself, so each clashing file holds both versions between git's marks:

```
<<<<<<< HEAD
this machine's version of the lines
=======
the teammate's version of the lines
>>>>>>> origin/main
```

The request you get names the folder, the files, who changed them and when. Your whole job is then the text: edit each file so it keeps everything meaningful from both versions in the right place, delete the marker lines, and stop. These are notes about a brand, not code — keep both sides rather than dropping either, and ask before removing anything that looks deliberate. Do not delete files. Run no git: the session cannot reach the shared copy (no credentials, and under the app's Codex engine no network) and does not need to. Once no marker line is left in any of those files and the folder has been quiet for a moment, the app saves the merge and shares it; the person can also undo the whole thing from the app. `git add`, `git commit` and `git merge --continue` pass the guard from v22 so that finishing by hand is never blocked halfway, but they are not needed, and `git pull`, `git push` and `git rebase` stay blocked.

To see where things stand without touching anything: `git status --short --branch`. `UU` lines are files still to combine; none left and no `ahead` count means the app has it from here.

## Finding the brain folder

Parker Desktop writes a pointer file at a fixed location: **`~/.parker/workspace.json`**, shaped like

```json
{ "version": 1, "root": "/Users/jane/parker", "updatedAt": "2026-08-31T09:00:00.000Z" }
```

`root` is the workspace folder the app keeps in sync. Each brand brain is its own folder at `<root>/orgs/<org>/<repo>/` (app versions before 0.1.18 used `<root>/brands/<repo>/`); `<root>/personal/` is the user's own space and each `orgs/<org>/` folder is the organization's shared space, never a brain. To tell brains apart, read each one's `parker_config.json` (`brand_id`). When a session needs to locate a brain (or confirm this folder is the synced one), read that file first. If it's missing or unreadable, the app probably isn't installed or is out of date: ask the user where the brain lives, and point them at the app if they don't have it.

## When the folder isn't syncing

If there's reason to think this folder is **not** being synced — the user says they don't have Parker Desktop, `~/.parker/workspace.json` is missing or the folder sits outside its `root`, the app shows this brain as read-only for them (it never uploads their changes), this is a hosted or scheduled cloud run on a copy with no Parker Desktop beside it, or they ask "is this backed up?" and you can't say yes — don't improvise a git flow. Say it plainly: right now the work lives only on this machine. Then give them the two real options, in this order:

1. **Install Parker Desktop** (recommended — no technical setup, it handles everything): https://app.heyparker.ai/dashboard/parker-desktop. Setting up the brand's repository happens right in the app, and once it's running it syncs this folder from then on.
2. **Wire up their own repo and git connection**, if the team is technical and wants to own their sync. That makes this a self-managed brain (below) — their auth, their remote, their habits.

Either way, keep working — files on disk are never wasted; they sync the moment either option is live. A scheduled run with nobody to tell ends by saying plainly, in its own output, that what it wrote could not be saved from where it ran.

## The self-managed exception

A rare team hosts and syncs the brain themselves. The test is the repo's origin, and it is the whole test: a path under `parker-brain/` (on GitHub, or on Parker's git gateway for brains with restricted folders) → managed, Parker Desktop's territory, everything above applies. Any other origin → the team brought their own repo: their normal git auth and habits apply, and the classic hygiene is good advice for them — pull before working, commit and push right after changes, keep both sides in conflicts, never force-push. A repo with **no remote at all** is neither managed nor backed up — the app always creates its repos with the remote attached, so a remote-less folder is local-only work: say so and route to "When the folder isn't syncing" above. (`parker_config.json` is a resume anchor, never proof of sync.)

## Talking to the user about all this

The user is not a git person and never needs to become one. Say "your brain saves automatically," "your teammate's changes come in on their own," "Parker Desktop keeps this folder backed up" — never "pushed," "rebased," "synced the remote." The mechanics reach the user only when something genuinely needs them: the app isn't installed, or the folder isn't the synced one.

## Hard rules

- **No git against this repo on your own. Ever.** No push, pull, fetch, clone, or `gh` aimed at the brand's repo, and no commits of your own. Files on disk are the interface; Parker Desktop is the sync engine. (`gh` pointed at *other* repos — searching GitHub, reading someone else's project — is fine.)
- Three carve-outs, and only these: mount operations (`git submodule update --init` and `/update-brain`'s pin move inside `parker-system/` — local, credential-free), the confirmed `/disconnect-factory` decoupling's own listed dissolution commands, and finishing a clash the app has put into the files (`git add`, `git commit`, `git merge --continue` — allowed, never required).
- Repos are created in Parker Desktop, never by the agent or a tool call. Ignore any git credentials a tool result carries — no credential files, no tokens in any form.
- If the folder isn't syncing, say so and offer the app (or their own git for a technical team) — never leave the user believing unsynced work is backed up.
- Self-managed repos (origin outside `parker-brain/`) are the team's own business — their auth, their rules.
