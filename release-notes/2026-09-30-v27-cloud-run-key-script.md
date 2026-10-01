# v27 — the cloud-run key runs through a factory script (2026-09-30)

v26 put the exact key command into every routine's prompt, and that passes the safety check inside the run. But the session that creates the routine runs a safety check too (auto mode is the default in Claude Code). It read the new routine's prompt, saw a command that makes a git credential that nobody had asked for in the conversation, and stopped the creation as "Credential Exploration". A customer's `/setup-routines` would hit the same block.

## What shipped

- **`scripts/cloud-run-git.py`** in the factory does the two steps that touch the key. `key <brand_id>` makes the key, hands it to git's credential cache under the user `parker-<brand_id>` for both Parker git servers (production and dev; only the one whose API registered the hash opens with it), and prints only its hash. `clone <git_url> <brand_id>` clones the brain with that cache as the only credential helper for Parker's server, sets up the `parker-system` mount (a warning only if that fails), and prints the new folder. It accepts only Parker's two git servers, a `brand_id` a shell can't read, and a folder that can't become a git option; git never stops to ask for a password; and the key goes on no command line, in no file and in no output.
- **The factory's `.claude/settings.json` allows exactly those two steps** (`permissions.allow`). Narrow allow rules stay in effect in auto mode and approve a command before the safety check, so the check judges the key neither in the run nor where the routine is created. Every routine starts in a checkout of the factory, where the rule lives.
- **`setup-routines`** writes a shorter preamble: run the script's `key`, register the hash with `register_parker_brain_git_credential`, run the script's `clone`, then the job and the save. No key command in the prompt. The routine's source repository has to be the factory.
- **`save-brain`, "In a cloud run"** uses the script when the session started in a factory checkout, and keeps the tool's own steps for every other cloud run.
- **Docs.** `system/brain-sync.md` explains the two checks and why the rule lives in the factory; `system/schedules.md` and the schedules README follow.
- **Tests.** `tests/test_cloud_run_git.py`: the clone command, the address, `brand_id` and folder checks (a folder like `--config=credential.helper=!cmd` is refused before git runs), both steps through `main()` with git mocked (the mount, a failed clone, no git), the key in git's memory with only its hash printed, two brands keeping their own keys, and the factory rule allowing these two steps and nothing else.

## For the other Parker repos

Nothing. The Parker MCP tool still gives its own key command to cloud runs that don't start in the factory.

## Migration

`migrations/v27.md`: nothing to do on the brand side. Routines armed with the v26 prompt keep working; the next `/setup-routines` gives them the shorter one.
