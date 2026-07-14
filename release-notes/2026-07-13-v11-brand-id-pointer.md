# 2026-07-13 — v11: faster, quieter cold starts — brand_id, mount drift, silent refresh

Field fixes for the slow, chatty start-of-thread experience: agents were rediscovering the brand_id, tripping over mount drift, and narrating the whole credential dance to the user.

## What shipped

- **brand_id from `parker_config.json`, not guesswork.** The `save-brain` skill and both hook messages (`session-start.py`, `git-guard.py`) now say it plainly: **read `brand_id` from `parker_config.json` at the repo root** — the onboarding runner has always stamped it there — and never guess it from the repo name. `get_available_brands` is only the fallback when the file is missing (very old builds).
- **Mount drift cleared, never committed.** A `parker-system` checkout that drifted from the recorded pin breaks `git pull --rebase` ("cannot rebase with locally recorded submodule modifications") — and worse, the loop's `git add -A` would have committed the drift as an accidental pin move. The save loop now re-aligns the mount (`git submodule update --init --recursive`) *before* committing, the skill carries the recovery for the staged case, and `session-start.py` clears drift-only trees itself instead of reporting them as unsaved work. Functionally tested with a real drifted submodule.
- **Credential refreshes are invisible maintenance.** New rule in `save-brain` and the session-start recovery text, with the exact line the user hears: **"I'll check for any new info first, then get you your answer."** Never tokens, credentials, git, or pulls.
- **The hook does the busywork itself.** On an expired-credential pull failure, `session-start.py` now deletes the dead credential file (no `rm -f` step, no Write-tool overwrite refusal) and reads the `brand_id` out of `parker_config.json`, handing the agent a recovery message with the id inlined — one MCP call, one Write, one combined pull command.
- **Refresh runs in parallel with the user's work.** Both the hook message and `save-brain` now instruct: fire `setup_parker_brain` and the local reads for the user's actual question in the same turn — only the pull waits on the fresh credential, and only the final answer waits on the pull. Sync-before-answer stays mandatory (a brain another process pushed to two days ago must not be read stale); it just stops being the user's problem.
- **`credential_file_line` support.** The server tool (mevin PR #710) now returns the ready-to-write credential line; the skill and hook prefer it, with lifting the token from `authenticated_clone_url` as the older-server fallback.

All changes live in the copied bundle; the pin bump's re-sync delivers them.

## Follow-ups

- Cut the `v11` tag once this merges.
- The mevin2 tool description could say the same thing ("brand_id is stored in parker_config.json in the brain repo") so sessions outside the repo learn it too.
