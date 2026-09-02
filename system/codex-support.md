# Codex support — how the brain runs on OpenAI Codex

The brand brain (and this factory repo) is built Claude Code-first, but every
piece of the runtime has a Codex twin, and this doc is the contract for both:
what maps where, what was verified against a real Codex install, what differs
by design, and the maintenance rules that keep the two harnesses from
drifting. Verified against Codex CLI 0.147.0 (August 2026) by direct probes —
hook payloads, skill discovery, and the deny contract were exercised live, not
read off blog posts.

## The mapping

| Surface | Claude Code | Codex |
|---|---|---|
| Operating contract | `CLAUDE.md` | `AGENTS.md` (routes to `CLAUDE.md`, read in full) |
| Voice | `.claude/output-styles/parker.md` + `"outputStyle": "Parker"` in settings | No output-style layer; `AGENTS.md` instructs reading the same style file and speaking it |
| Skills | `.claude/skills/` | `.agents/skills/` — a **committed symlink** to `.claude/skills/`; same SKILL.md files (verified: Codex discovers and follows skills through the symlink; invoke with `$skill-name` or implicit matching) |
| Hooks | `.claude/settings.json` `hooks` block | `.codex/config.toml` `[[hooks.*]]` tables — same events, same scripts, same JSON wire format |
| Mount protection (`parker-system/` read-only) | `permissions.deny` rules | No per-path deny exists; the `mount-guard.py` PreToolUse hook does the job (JSON deny on Edit/Write/NotebookEdit/apply_patch targets under the mount) |
| Git guard block mechanism | exit 2 + stderr | JSON `permissionDecision: "deny"` on stdout (`git-guard.py --codex` switches the envelope; guard logic identical) |
| Review-gate subagents (`.claude/agents/*.md`) | Spawned as subagents | No Markdown subagents; the creative skills execute the same agent files **inline** as a separate pass and fill the same receipts |
| Scheduled routines | Claude Code cloud scheduled agents (`/setup-routines`) | Not armable from Codex; skills run on demand, or external cron + `codex exec` |
| Per-instance config | `.claude/settings.local.json` (gitignored) | the user's own `~/.codex/config.toml` (MCP servers, model — never committed) |

## Verified hook contract (the load-bearing facts)

Codex's hooks engine (stable, on by default in 0.147.0) adopted Claude Code's
wire format nearly verbatim, which is why the brand hooks run unmodified:

- **Input**: JSON on stdin with `hook_event_name`, `cwd`, `session_id`,
  `tool_name`, `tool_input`, `tool_response`, `permission_mode`, `model` —
  the same field names Claude Code sends. Hook cwd is the repo root.
- **Output**: one JSON object on stdout.
  `{"hookSpecificOutput": {"hookEventName": "...", "additionalContext": "..."}}`
  injects context (verified end-to-end for UserPromptSubmit and used by
  SessionStart). PreToolUse denies with `{"decision": "block", "reason": ...,
  "hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision":
  "deny", "permissionDecisionReason": ...}}`. Codex parses stdout as a single
  JSON document when it starts with `{` — anything trailing the object fails
  the whole event, so emit exactly one object and nothing else.
- **Events**: SessionStart, UserPromptSubmit, PreToolUse, PostToolUse,
  PermissionRequest, Stop, SessionEnd, SubagentStart/Stop, Pre/PostCompact.
  The brand bundle uses the same four events as on Claude, plus a second
  PreToolUse entry for the mount guard.
- **Matchers**: regex over tool names, Claude-style names honored (`Bash`,
  `Edit`, `Write`) plus Codex's own (`apply_patch`, shell variants). MCP tools
  keep the `mcp__server__tool` naming, so the `mcp__.*` matcher carries over.
- **Trust**: project-level `.codex/` config loads **only when the project is
  trusted**, and each hook additionally needs a per-user approval — recorded
  in `~/.codex/config.toml` under `[hooks.state]` as a hash of the hook's
  definition. Two consequences the design leans on: hook **command strings
  must stay stable** (they delegate to `.claude/hooks/` scripts, so script
  updates via the normal sync never invalidate trust — only edits to
  `.codex/config.toml` itself trigger re-approval), and **headless `codex
  exec` silently skips never-approved hooks** — the one-time trust has to
  happen interactively (TUI, `/hooks`) before hooks work in any automation.

## Differences that stay differences (by design)

- **The voice is advisory on Codex.** AGENTS.md context is weaker than
  Claude's system-prompt-level output style; expect Parker to hold the voice a
  little less firmly there. Not worth a fork — the full style file is still
  read every session.
- **Gates run inline, not independently.** An inline pass shares context with
  the writer, which is weaker than a fresh subagent. The skills compensate by
  requiring the pass to re-read sources rather than trust the draft. If Codex
  ships Markdown-defined subagents later, revisit.
- **The self-running layer is Claude-first.** Schedules are per-account cloud
  agents; a Codex-only team runs routines manually or wires external cron.
- **Windows:** the `.agents/skills` symlink needs git symlink support
  (`core.symlinks true` + Developer Mode) or Codex sees no skills there.

## Maintenance rules (factory)

- `.claude/settings.json` (brand template) and
  `templates/brand-routines/codex/config.toml` describe the same hook
  behavior. **Change one, change the other in the same PR.**
- Hook scripts live once, in `templates/brand-routines/claude/hooks/`, and
  must keep emitting the shared wire format (single JSON object, or the
  Claude-specific exit-code path guarded behind the default mode). A new hook
  gets wired in both files; a Codex-only hook (like `mount-guard.py`) still
  lives in the shared `hooks/` directory.
- Skills need no dual maintenance — the `.agents/skills` symlink means both
  harnesses read the same files. Never materialize a second copy.
- The brand bundle's Codex pieces travel through `scripts/sync-executable-layer.py`
  (`templates/brand-routines/codex/` → `.codex/`, `AGENTS.md` → `AGENTS.md`),
  so `/update-brain` delivers them on every pin bump. The symlink itself can't
  be synced by that script — onboarding stamps it, and `migrations/v17.md`
  adds it to standing brains.
- When Codex behavior needs re-verifying (a contract doubt, a new Codex
  version): probe against the real binary — a scratch repo, a marker-emitting
  hook, `codex exec` with an isolated `CODEX_HOME` — and update this doc with
  what changed. Blog posts about Codex contradict each other; the binary
  doesn't.
