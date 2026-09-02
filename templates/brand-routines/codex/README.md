# `.codex/` — the brand brain on OpenAI Codex

This directory makes the brand brain work in OpenAI Codex the way `.claude/`
makes it work in Claude Code. Same brain, same skills, same guardrails — only
the harness wiring differs. Nothing here forks the method: every hook in
`config.toml` runs the exact scripts in `.claude/hooks/`, and the skills Codex
loads are the same files Claude loads.

## What's here

- **`config.toml`** — committed Codex project config. Wires the four standing
  hooks (session-start mount check, craft-catalog injection on every prompt,
  MCP pull log, git guard) plus a fifth Codex-only one: `mount-guard`, which
  keeps `parker-system/` read-only because Codex has no per-path permission
  deny rules. Hook commands are deliberately stable strings that delegate to
  `.claude/hooks/` scripts, so factory script updates arrive through the
  normal sync without re-approval.

## The rest of the Codex surface (lives outside this folder)

- **Skills** — Codex discovers skills from `.agents/skills/`, which is a
  committed symlink to `.claude/skills/`. One set of SKILL.md files, both
  harnesses. (On Windows, git needs symlink support enabled —
  `git config core.symlinks true` plus Developer Mode — or the link checks out
  as a plain text file and Codex sees no skills.)
- **Voice and contract** — `AGENTS.md` at the repo root is what Codex reads
  the way Claude Code reads `CLAUDE.md`. It routes to `CLAUDE.md` as the
  operating contract and carries the Parker voice, since Codex has no
  output-style layer.

## First run on Codex (per person, one time)

1. Open the repo in Codex and **trust the project** when asked — untrusted
   projects skip `.codex/` entirely, and none of the guardrails load.
2. **Approve the hooks** when Codex asks (or via `/hooks` in the TUI). The
   approval is stored per-user as a hash of each hook definition; it survives
   factory updates to the hook *scripts* and is only re-asked if
   `config.toml` itself changes.

## Known differences from Claude Code (by design, documented in
`parker-system/system/codex-support.md`)

- **Review gates run inline.** Codex has no Markdown subagents, so the
  creative skills execute `.claude/agents/*.md` as a separate inline pass
  instead of spawning them. The gates still run; the receipts still ship.
- **Scheduled routines don't arm from Codex.** The six standing routines run
  as Claude Code cloud scheduled agents. From Codex, run them by invoking the
  skills (`$refresh-context`, `$dream`, …) manually or on external cron via
  `codex exec`.
- **Headless caveat.** `codex exec` silently skips hooks that were never
  interactively approved — do the one-time trust in the TUI first.
