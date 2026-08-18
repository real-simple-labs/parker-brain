# v17 — OpenAI Codex support

The brain no longer assumes Claude Code. Every runtime surface — contract, voice, skills, hooks, guardrails — now has a Codex twin, and the two harnesses read the same underlying files wherever the platforms allow it. The contract for all of it is the new `system/codex-support.md`, and every load-bearing claim in it was verified against a real Codex CLI 0.147.0 install with live probes (a marker-emitting hook, a scratch repo, an isolated `CODEX_HOME`), because the third-party writing about Codex contradicts itself.

## What made this cheap: Codex adopted Claude Code's contracts

Two discoveries carried the whole release. First, Codex's hooks engine uses Claude Code's wire format nearly verbatim — same input fields (`hook_event_name`, `tool_name`, `tool_input`, `cwd`, `session_id`), same `hookSpecificOutput.additionalContext` output envelope, same event names. The four brand hooks (session-start mount check, craft-catalog injection, MCP pull log, git guard) run on Codex **unmodified**. Second, Codex discovers skills in the open SKILL.md format from `.agents/skills/`, and it follows symlinks there — so a single committed symlink to `.claude/skills/` gives both harnesses the same skills with nothing to keep in sync, in the factory and in every brand.

## The pieces

- **`templates/brand-routines/codex/config.toml`** — the committed Codex project config, stamped to `.codex/`. Wires the same four hooks with deliberately stable command strings that delegate to the same `.claude/hooks/` scripts (Codex records per-user trust as a hash of each hook definition, so script updates via the normal sync never re-prompt; only config edits do). Its hook block and `.claude/settings.json`'s must move together — both files and `codex-support.md` say so.
- **`mount-guard.py`** (new hook) — Codex has no per-path permission deny rules, so the `parker-system/` read-only guarantee becomes a PreToolUse hook: JSON deny on any Edit/Write/NotebookEdit/apply_patch whose target resolves under the mount.
- **`git-guard.py --codex`** — same guard, same messages, different envelope: Codex ignores the exit-2/stderr block mechanism, so the flag switches blocks to the JSON `permissionDecision: "deny"` form. The guard also now tolerates Codex's shell tool names and argv-list commands.
- **`templates/brand-routines/AGENTS.md`** — stamped to the brain's root. Codex's entry point: routes to `CLAUDE.md` as the operating contract, instructs reading and embodying `.claude/output-styles/parker.md` (Codex has no output-style layer, so the voice ships as instruction rather than system prompt — advisory by nature, and accepted as such), and carries the Codex wiring notes. Brand-neutral on purpose so the sync keeps updating it.
- **Inline review gates.** Codex has no Markdown subagents, so the five creative skills' ship gates gain one shared fallback sentence: with no spawn mechanism, open the agent file and execute its method as its own separate pass that re-reads sources rather than trusting the draft, and fill the same receipts. Weaker than a fresh context, and said so.
- **Factory surface** — `.agents/skills` symlink and a Codex section in the factory `AGENTS.md`, so contributors can work on the factory from Codex too.

This release sits on v16's Parker Desktop layer: the brain runs no git of its own, and the git guard's job on both harnesses is the same — block git and gh aimed at the brand repo (mount operations pass) and teach that saving means writing files.

## Known boundaries, by design

The six standing routines stay Claude Code cloud scheduled agents — from Codex the skills run on demand, and `/setup-routines` says so plainly. Headless `codex exec` silently skips hooks that were never interactively approved, so the one-time trust must happen in the TUI before any Codex automation. And on Windows the symlink needs git symlink support enabled.

## Delivery

`scripts/sync-executable-layer.py`'s bundle map grew the Codex destinations (`codex/` → `.codex/`, `AGENTS.md` → root), and skips the factory's `.agents/` entries — the symlink can't travel as a blob. That one artifact is the reason this ships with real-step **`migrations/v17.md`**: one `ln -s`, which Parker Desktop syncs like any other change, plus a one-sentence heads-up for teammates who use Codex. The onboarding runner stamps all three artifacts on new builds (Phase 0 step 5 gains a "Fifth, the Codex twin" move, and the verification checklist counts it).
