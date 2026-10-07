# v33 — a cloud run saves through the factory script (2026-10-06)

Four production test routines ran on 2026-10-06. One of them, with a plain prompt ("Update the competitor notes in the Parker AI brain ... and save them to the brain") and the factory as its source, wrote its notes, committed and pushed. The push was refused (`fetch first`): someone had saved to the brain while the run worked. That is normal and harmless, and the fix is to take in their save and push again. But the run's safety check stopped the `git fetch` that followed as "Out-of-Place Publication" (git traffic to a repository other than the one the session started in), so nothing was saved. The same evening, a dream run and a `refresh-context` run both added an entry at the top of `running-notes/routine-log.md`, so a clash in the rebase is common too.

## What shipped

- **`scripts/cloud-run-git.py save <folder> -m <message>`.** One command for the whole save: it commits everything, runs `pull --rebase origin main`, pushes `HEAD:main`, and tries again (up to five times) while the push is refused because someone saved in between. It never forces a push. It pushes only a copy whose every origin address, for fetch and for push, is Parker's git server with the brand's user in it (what `clone` makes), so the allowed command can't push anywhere else, and it runs no git hook from the copy. A pull or push that moves no data for ten minutes gives up instead of holding the run. On a machine with no git name or email it commits as "Parker cloud run". On a clash it pushes nothing, leaves the rebase open and names the files: the agent combines them (file edits only) and runs `save` again, which finishes the rebase and pushes. It prints `saved <commit>` when the brain has it.
- **`.claude/settings.json`** allows `save` like `key` and `clone`, so the safety check never judges a scheduled run's git steps.
- **`setup-routines`** (both copies): the cloud-run preamble saves with `scripts/cloud-run-git.py save <folder> -m "<what changed>"` instead of `git push origin HEAD:main`, and says what to do on a clash.
- **`save-brain`, "In a cloud run" step 4:** from a factory checkout, save with that command. Anywhere else, the plain git steps stay, and a push refused as `non-fast-forward` or `fetch first` only means someone saved in the meantime: pull with rebase and push again.
- **`save-brain` step 3** no longer pulls before work: the copy from step 2 is fresh, and `save` takes in what others saved. The brand `CLAUDE.md` template and `AGENTS.md` no longer name the raw push in their cloud-run sentence.
- **`system/brain-sync.md`** records why.
- **Tests.** `tests/test_cloud_run_git.py` runs `save` against a real local origin: a plain save, a teammate's save taken in first, a save that lands between the pull and the push, a clash that pushes nothing, the second `save` after the files are combined, marker lines left in a file, keeping only the teammate's version, a machine with no git identity, plain markers whatever the machine's conflict style, a push address elsewhere refused, a planted hook that never runs, and a check that it never forces a push.

## For the other Parker repos

The Parker MCP tool `register_parker_brain_git_credential` names `scripts/cloud-run-git.py` for the key and the clone, but still says to save with plain git. A routine with a plain prompt follows that text, so the tool should name `save` too, once this release is on `main` (a mevin change).

## Migration

`migrations/v33.md`: one step. The brain's `CLAUDE.md` (a seed the re-sync never touches) loses the raw `git push origin HEAD:main` from its cloud-run sentence and points to `/save-brain` instead; the template already says so. Routines armed with an older prompt keep working with plain git; the next `/setup-routines` gives them the `save` step.
