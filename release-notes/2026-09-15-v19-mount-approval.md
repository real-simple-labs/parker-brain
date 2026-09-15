# v19 — the method mount asks for approval, never copies (2026-09-15)

A field failure the day v18 shipped: the build's `git submodule add` of the public factory was blocked, the agent read Parker Desktop's workspace guide ("do not run git in these folders unless the user asks") as a ban, skipped the mount, and started copying files out of a factory clone. A copied method is frozen: there is no pin for `/update-brain` to move, and every `parker-system/…` path the skills and prompts reference points at nothing.

## What shipped

- **Runner and `/set-up-brain`:** the mount is the sanctioned exception to the workspace guide's git line, and the build's go-ahead is the ask. When the harness still wants a yes (Claude Code raises an approval card in the app; the app's Codex sandbox has no network and can't prompt), the agent asks through the popup form and waits. It never copies the factory in. No mount, no build.
- **Build verification:** a `parker-system/` that `git submodule status` doesn't list is a hard fail.
- **`system/brain-sync.md`:** documents the workspace guide files Parker Desktop writes (`CLAUDE.md` and `AGENTS.md` at the workspace root and under `orgs/`) and two cross-team fixes: name the mount exception in the guide's git line, or attach the mount at provisioning so no agent ever runs `git submodule add`.
- **`system/codex-support.md`:** the app's `codex exec --sandbox workspace-write` has no network and no prompts, so the mount and `/update-brain`'s `git -C parker-system fetch` route to Claude Code or to a sandbox with network.

## Migration

`migrations/v19.md` is a no-op: everything rides the mount and the pin bump's re-sync.
