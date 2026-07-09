---
name: disconnect-factory
description: Decouple this brain from the public parker-brain factory so the team can develop their own version of the method. Converts the read-only parker-system/ submodule into plain files the team owns and can edit, removes the read-only guardrails, and flips the update posture so /update-brain stops offering pin bumps. Use when the team says they want to customize the method itself, own their prompts and craft docs, disconnect from Parker's updates, or go independent.
---

# Disconnect factory — make the method the team's own

## What this is and when to run it

The standard brain mounts the factory method at `parker-system/` as a read-only submodule pinned to a release: the team gets Parker's improvements by moving the pin, and never edits the method directly. Some teams outgrow that — they want to rewrite prompts, reshape craft docs, and develop their own version of the method. This skill is that decoupling, done cleanly and reversibly-in-git.

This is a real fork in the road, so it starts with a plain confirmation, never runs on inference. Explain what changes before anything happens:

- The method files become theirs to edit, versioned in this repo like everything else.
- They stop receiving factory releases as pin-bump offers. `/update-brain` switches to its decoupled mode: it can still *show* what the factory added and offer individual pieces, but nothing arrives whole anymore, and under full independence it goes quiet unless asked.
- Everything else — their data, skills, routines, schedules — keeps working exactly as before, because every path stays the same.

Then ask which of the two shapes they want (popup question form, one question):

1. **Own factory copy (keeps a road back).** They keep a private copy of the factory as their own repo, and this brain's submodule URL is repointed at it. They edit method there; they can still merge the public factory into their copy whenever they want Parker's improvements. Right for teams who want to customize *and* keep drawing on upstream.
2. **Full absorb (simplest, fully theirs).** The submodule is dissolved and the method files are committed directly into this repo at the same `parker-system/` path. No second repo, no submodule mechanics, no upstream link. Right for teams going fully independent.

## Option 1 — repoint at their own factory copy

1. They need a private copy of the public factory under their own control. A GitHub fork of the public repo cannot be made private, so it's a duplicate: bare-clone the public factory, push it to a new private repo they own. Walk them through it or do it with their credentials.
2. Repoint the submodule: edit the URL in `.gitmodules` to their copy, then `git submodule sync parker-system` and verify `git -C parker-system remote -v`.
3. Update `running-notes/standard-sync.md`: posture `own-factory`, their remote, the release currently pinned, and a line recording the decoupling date and reason.
4. Keep the deny rules **removed only if they ask** — under option 1 many teams still want the mount read-only in the brain and do their method editing in the factory copy itself. Ask; default is keep the rules.
5. Commit as one commit: `Decouple: repoint method at team factory copy`.

## Option 2 — full absorb

All of this lands as **one commit**, so it is one `git revert` away from undone:

1. Capture the pinned state first: note the release tag from `git -C parker-system describe --tags` into the ledger — after the absorb, that line is the only record of which factory version the method forked from.
2. Dissolve the submodule but keep the files in place:
   - `git submodule deinit -f parker-system`
   - `git rm --cached parker-system`
   - remove the `parker-system` entry from `.gitmodules` (delete the file if it's the only entry)
   - `rm -rf .git/modules/parker-system` and delete the inner `parker-system/.git` file
   - `git add parker-system/ .gitmodules` — the method files are now plain tracked content
3. Remove the four `parker-system` deny rules from `.claude/settings.json` — the method is editable now, that's the point.
4. Update `running-notes/standard-sync.md`: posture `independent` (or `own-factory` in spirit if they say they still want offers), the fork-point release, date, reason.
5. Commit: `Decouple: absorb factory <tag> into the brain`.

## After either path

- Tell them plainly what changed and what to expect: `/update-brain` now runs in decoupled mode per its own skill doc, and method edits are theirs to make and version. The session-start hook adjusts itself — it detects the absorbed (non-submodule) state and switches to the decoupled message, dropping the pin and read-only language; no manual hook edit is needed. Under option 1 (repoint) the mount is still a submodule, so the hook keeps its standard message against their own remote.
- Honesty about the road back: reconnecting later is possible but manual — re-adding the submodule is easy, but any method edits they made in the meantime have to be carried over by hand. Say this at the confirmation step, not after.
- Log the decision through `self-improvement-intake` as a reasoning trace: teams decouple for reasons, and the reason is signal.

## Hard rules

- Never run without the explicit confirmation. "Can we edit the prompts?" is a question about this skill, not an instruction to run it — explain first, offer, wait.
- One commit per decoupling, so it reverts clean.
- Never decouple as a side effect of some other task hitting the read-only wall. If an edit inside `parker-system/` gets denied, the answer is to surface *why* it's read-only and mention this skill exists — not to run it.
