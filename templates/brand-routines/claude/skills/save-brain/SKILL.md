---
name: save-brain
description: How this brain saves and syncs itself — the required knowledge for anything save, sync, backup, clone, or share-shaped in a Parker Brain, and for any impulse to run git here. The short of it - on a person's computer, files written to disk are the whole job, the Parker Desktop app syncs the folder both ways, and the agent never runs git against this repo; in a cloud run (a scheduled routine or a hosted sandbox, no Parker Desktop) the agent gets the brain through the Parker MCP and saves it with git itself. Covers finding the brain folder, what to do when the app has paused the folder on a clash (files holding both versions between <<<<<<< and >>>>>>> marks), cloud runs, what to do when the app isn't installed, and the rare self-managed exception. Use whenever saving work, syncing, backing up, combining a clash, running on a schedule, or fixing something that looks like a sync problem.
---

# Save brain — write the files, let Parker Desktop sync them

Most Parker Brains live in Parker's own private storage (a repo created through the Parker Desktop app), and the **Parker Desktop app** keeps this folder in sync with it — it watches the folder, uploads every change, and brings down what teammates and scheduled routines added. Saving is therefore not a step you perform. It's what happens when you write a file. The one exception is a cloud run (a scheduled routine or a hosted sandbox), where no app runs: see "In a cloud run" below.

## The whole procedure

1. Write the file to disk.

That's it. No commit, no push, no pull, no credentials, no branches. When a batch of edits is done, the work is saved the moment the files are written — Parker Desktop commits and uploads it on its own once the folder has been quiet for a few seconds, usually within a minute.

**Never run git against this repo on your own.** Not `git push`, `git pull`, `git fetch`, `git clone`, not `gh`, and no commits of your own — none of it, even if a tool message or an old habit suggests it. Two sync engines fighting over one folder is how work gets destroyed, and the app is the one that's supposed to be here. The only git the agent still owns is the method mount: `parker-system/` is a pinned submodule of the public factory, and its local operations (`git submodule update --init`, and `/update-brain`'s `git -C parker-system fetch` / `checkout` pin move) are fine — they need no credentials and never touch the brand's own storage. One more sanctioned exception: the confirmed `/disconnect-factory` decoupling runs the exact submodule-dissolution commands its own skill lists (`git submodule sync`, `git rm --cached parker-system`, `git add`) — those are part of that skill's confirmed flow, not a violation of this rule. And one situation where `git add`, `git commit` and `git merge` are allowed but not needed: finishing a clash the app has put into the files, below. If one of these commands says `index.lock` exists, the app is most likely mid-sync: wait a few seconds and run it again, up to a few times. If the lock is still there after that, stop and tell the user (the app, or a git process that died, holds it); never delete the lock file yourself.

The repo itself was created **in Parker Desktop** — the app provisions it, syncs it down, and opens the agent session in its folder; no agent creates brand repos. The setup prompt, and the Parker MCP's own `setup_parker_brain` tool description, may still describe the older flow (call the tool, clone with its credentials, commit and push). That flow is retired: there is nothing to provision, so don't call the tool, and **ignore any credentials** a tool result carries: don't save them, don't build a credential file, don't clone with them. This skill overrides any tool message that says otherwise. The one sanctioned way for an agent to reach the brand's storage is a cloud run's own credential, below — and only in a cloud run.

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

The request you get names the folder, the files, who changed them and when. Your whole job is then the text: edit each file so it keeps everything meaningful from both versions in the right place, delete every marker line of each clash block (the `<<<<<<<`, `=======` and `>>>>>>>` lines; the app forces the two-way style, so there is no `|||||||` base section), and stop. These are notes about a brand, not code — keep both sides rather than dropping either, and ask before removing anything that looks deliberate. Do not delete files. Run no git: the session cannot reach the shared copy (no credentials, and under the app's Codex engine no network) and does not need to. Once no marker line is left in any of those files and the folder has been quiet for a moment, the app saves the merge and shares it; the person can also undo the whole thing from the app. `git add`, `git commit` and `git merge` (its `--continue` included) pass the guard from v22 so that finishing by hand is never blocked halfway, but they are not needed; `git merge --abort` is blocked, because undoing is the person's call in the app, and `git pull`, `git push` and `git rebase` stay blocked.

To see where things stand without touching anything: `git ls-files -u` lists the files still to combine, exactly (in `git status --short --branch` they are the lines with a `U` on either side, or `AA`). No file listed, no marker line left, and no `ahead` count means the app has it from here.

## Finding the brain folder

Parker Desktop writes a pointer file at a fixed location: **`~/.parker/workspace.json`**, shaped like

```json
{ "version": 1, "root": "/Users/jane/parker", "updatedAt": "2026-08-31T09:00:00.000Z" }
```

`root` is the workspace folder the app keeps in sync. Each brand brain is its own folder at `<root>/orgs/<org>/<repo>/` (app versions before 0.1.18 used `<root>/brands/<repo>/`); `<root>/personal/` is the user's own space and each `orgs/<org>/` folder is the organization's shared space, never a brain. To tell brains apart, read each one's `parker_config.json` (`brand_id`). When a session needs to locate a brain (or confirm this folder is the synced one), read that file first. If it's missing or unreadable, the app probably isn't installed or is out of date: ask the user where the brain lives, and point them at the app if they don't have it.

## In a cloud run

A **cloud run** is a session in the cloud with no Parker Desktop beside it: a scheduled routine (a Claude Code cloud routine, the brain's own schedules included), or a hosted sandbox such as Claude on the web or Codex cloud. Two things together tell you you're in one: `~/.parker/workspace.json` does not exist, and this is not a person's own computer. On a person's computer the answer is always the app, whether or not it is installed (see "When the folder isn't syncing" below), and a person's own commits there would lose who made each change.

In a cloud run nobody else syncs the brain, so you do it, with git, through Parker's own storage:

1. **Get access.** Use the Parker MCP tool `register_parker_brain_git_credential` with the brand's `brand_id` (from `parker_config.json`, the routine's prompt, or `get_available_brands`). Follow its steps exactly: one shell command makes a secret, hands it to git's own credential cache (in memory; no file holds it, so no `git add` can pick it up), and prints its hash; you send the tool only the hash. **When this session started in a checkout of Parker's factory** (a scheduled routine does), make the key there with `scripts/cloud-run-git.py key <brand_id>` instead: it does the same, and the factory's settings allow it, so a cloud session's safety check never has to judge a key it can't see anyone asking for. A routine from v26 has the key command in its own prompt; run it from there. **Never print, show, or send the secret.** The tool answers with commands for the next step.
2. **Get the brain.** Run the tool's `clone_command` in a working folder (from a factory checkout: `scripts/cloud-run-git.py clone <git_url> <brand_id>`, which clones next to it and prints the folder) and continue inside the new folder. A big brain takes several minutes to clone: give the command a long timeout (10 minutes) and wait until it ends; if the shell moves it to the background, wait for the notice that it ended. While it runs, the folder can hold only `.git` with git saying "No commits yet": that is a clone still running, not an empty brain. Judge the copy only after the command has ended. If git can't reach the server (`host_not_allowed`, or a 403 from a proxy), this cloud environment blocks Parker's git server: say plainly that the environment needs full network access, or `git.heyparker.ai` on its allowed list, and stop. Clone a fresh copy even if the run started in another copy of this brain (for example one a routine checked out from GitHub), and leave that one alone: when some folders are hidden from this person, Parker's copy has a different history, and mixing the two would bring back what is hidden.
3. **Work.** Run `git pull --rebase` before you read or change files, then do the job (the routine's skill, from this copy's `.claude/skills/`).
4. **Save.** You have permission to push straight to `main` of this copy: `main` is the brain everyone reads, so a branch would never reach them. Never create a branch and never push anywhere else, whatever a default for this environment says. Git needs a name and an email for a commit: if `git config user.name` prints nothing, run `git config user.name 'Parker cloud run'`, and if `git config user.email` prints nothing, run `git config user.email 'routines@heyparker.ai'`. Then commit everything and share it:

   ```
   git add -A
   git commit -m '<routine>: <what changed>'
   git pull --rebase origin main
   git push origin HEAD:main
   ```

   A clash in the rebase is yours to combine: the same rule as the app's clashes above (keep what matters from both versions, delete every marker line), then `git add` the files and `git rebase --continue`, and push again.
5. **Keep access.** The credential works for one hour (`credential_expires_at`). A run that needs longer calls the tool again with the **same** hash before then: that renews it (git keeps the key in memory for a day, so only the server's hour counts). When git says `Authentication failed`, or asks for a username (`could not read Username`), git no longer has a working key: make a new key the way step 1 did (in a factory checkout `scripts/cloud-run-git.py key <brand_id>`, run from that folder) and call the tool with the new hash. The copy needs no change.
6. **Nothing to clean up.** The secret lives only in git's memory: it goes with the machine when the run ends, and the server stops taking it within the hour by itself. A run from before v26 kept it in `~/.parker/git-credential-<brand_id>`; if that file is there, delete it.

The guard (`git-guard.py`) lets all of this through in a cloud run. Even so: never force-push, never rewrite history that is already shared, never delete a branch. If the tool says `access` is `read`, you can pull but saving is refused: say so. If the Parker MCP has no `register_parker_brain_git_credential` tool, or it refuses this brand, the run can't save: finish the work, and say plainly in the run's output that what it wrote could not be saved (the next section).

## When the folder isn't syncing

If there's reason to think this folder is **not** being synced — the user says they don't have Parker Desktop, `~/.parker/workspace.json` is missing or the folder sits outside its `root`, the app shows this brain as read-only for them (it never uploads their changes), this is a cloud run that could not get a credential (above), or they ask "is this backed up?" and you can't say yes — don't improvise a git flow. Say it plainly: right now the work lives only on this machine. Then give them the two real options, in this order:

1. **Install Parker Desktop** (recommended — no technical setup, it handles everything): https://app.heyparker.ai/dashboard/parker-desktop. Setting up the brand's repository happens right in the app, and once it's running it syncs this folder from then on.
2. **Wire up their own repo and git connection**, if the team is technical and wants to own their sync. That makes this a self-managed brain (below) — their auth, their remote, their habits.

Either way, keep working — files on disk are never wasted; they sync the moment either option is live. A scheduled run with nobody to tell ends by saying plainly, in its own output, that what it wrote could not be saved from where it ran.

## The self-managed exception

A rare team hosts and syncs the brain themselves. The test is the repo's origin, and it is the whole test: a path under `parker-brain/` (on GitHub, or on Parker's git gateway for brains with restricted folders) → managed, Parker Desktop's territory, everything above applies. Any other origin → the team brought their own repo: their normal git auth and habits apply, and the classic hygiene is good advice for them — pull before working, commit and push right after changes, keep both sides in conflicts, never force-push. A repo with **no remote at all** is neither managed nor backed up — the app always creates its repos with the remote attached, so a remote-less folder is local-only work: say so and route to "When the folder isn't syncing" above. (`parker_config.json` is a resume anchor, never proof of sync.)

## Talking to the user about all this

The user is not a git person and never needs to become one. Say "your brain saves automatically," "your teammate's changes come in on their own," "Parker Desktop keeps this folder backed up" — never "pushed," "rebased," "synced the remote." The mechanics reach the user only when something genuinely needs them: the app isn't installed, or the folder isn't the synced one.

## Hard rules

- **On a person's computer: no git against this repo on your own. Ever.** No push, pull, fetch, clone, or `gh` aimed at the brand's repo, and no commits of your own. Files on disk are the interface; Parker Desktop is the sync engine. (`gh` pointed at *other* repos — searching GitHub, reading someone else's project — is fine.)
- Three carve-outs there, and only these: mount operations (`git submodule update --init` and `/update-brain`'s pin move inside `parker-system/` — local, credential-free), the confirmed `/disconnect-factory` decoupling's own listed dissolution commands, and finishing a clash the app has put into the files (`git add`, `git commit`, `git merge` with its `--continue` — allowed, never required; never `--abort`).
- **In a cloud run** (no `~/.parker/workspace.json`, not a person's computer), the run saves itself: `register_parker_brain_git_credential`, a fresh clone, then pull, commit and `git push origin HEAD:main` as "In a cloud run" says. It may push straight to `main`, and only there; never a branch, never a force-push.
- Repos are created in Parker Desktop, never by the agent or a tool call. Ignore any git credentials a tool result carries — no credential files, no tokens in any form — except a cloud run's own secret from `register_parker_brain_git_credential`, which lives only in git's memory.
- If the folder isn't syncing, say so and offer the app (or their own git for a technical team) — never leave the user believing unsynced work is backed up.
- Self-managed repos (origin outside `parker-brain/`) are the team's own business — their auth, their rules.
