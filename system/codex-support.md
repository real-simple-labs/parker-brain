# Codex support

The factory and its brand brains share one method across Claude Code and OpenAI
Codex. The supported verification baseline is Codex CLI 0.154.0. Runtime tests
live in `tests/test_runtime_hooks.py`; the optional local-binary probe is
`tests/probe_codex_runtime.py`. Run them when changing the runtime.

## What loads where

- `AGENTS.md` routes Codex to the root `CLAUDE.md` and the shared voice file at
  `.claude/output-styles/parker.md`. Codex has no Claude output-style switch.
- `.agents/skills` is a committed symlink to `.claude/skills`. Both runtimes read
  the same skills. On Windows, enable Git symlinks and Developer Mode before
  cloning; verify that the entry is a resolving symlink, not a text file.
- `.codex/config.toml` wires the same four standing hooks as Claude, plus the
  mount guard. `run-hook.py` executes each shared script from the brand root,
  including when the session starts in a subfolder. The command bootstrap asks
  Git for the nearest worktree root and loads only that root's dispatcher;
  outside a repo or without the dispatcher it exits 0, never searching a parent
  repo for a replacement. A missing dispatcher still needs repair before relying
  on the hooks. Windows commands use
  `py -3`; other platforms use `python3`. Install Git and Python 3.11+.
  The factory itself does not install the brand hooks.
- Independent creative reviewers read `.claude/agents/context-grounding-review.md`
  and `.claude/agents/creative-voice-review.md` as their instructions. The parent
  supplies those paths, the task, draft, brand root, and pull receipts through
  the runtime's spawning tool. Automatic discovery of Claude's Markdown agent
  definitions is not required. Only when spawning is unavailable may the parent
  execute each method inline, re-read the sources, and label the receipt inline.
  Grounding always runs; voice review follows the skill's customer-facing-copy
  condition. The receipts describe the review that actually ran.
- Claude cloud schedules are armed only where the scheduling capability exists.
  Codex builds ship the recipes with scheduling explicitly deferred and the
  skills available on demand. This is a complete Codex build. External cron is
  a separate team setup; never mark a recipe active without an observed schedule.

## Hook contract

Hooks receive one JSON object on stdin and emit at most one JSON object on stdout.
`hookSpecificOutput.additionalContext` injects context. PreToolUse denies with
`hookSpecificOutput.permissionDecision: "deny"`; exit 2 with stderr also blocks
on the verified Codex version. The git guard retains `--codex` for its JSON
envelope, while Claude keeps the exit-code envelope.

Codex normalizes shell calls, including `exec_command`, to `tool_name: "Bash"`.
Both Bash and `apply_patch` carry their text in **`tool_input.command`**. Edit and
Write are matcher aliases for patches; the payload still says `apply_patch`.
MCP tools retain `mcp__server__tool` names and their arguments. The payload's
`cwd` is the session directory, not necessarily the repo root. Patch paths are
resolved against that directory, while shared hook scripts run from the brand
root so catalog reads, Git checks, and pull-log identity remain consistent.

The catalog hook uses an explicit context allowance. Its output has a bounded
user-profile section and checks the full instruction-plus-catalog size; if the
catalog cannot fit, it emits a visible instruction to read it in full before
answering. No catalog rows are silently removed. The complete context is capped
at 16,000 UTF-8 bytes, a conservative ceiling for the 16,000-token allowance
without a tokenizer dependency. Profile text uses only the remaining budget;
larger profiles become explicit full-file reads so they do not displace a catalog
that otherwise fits. Tests cover multibyte text and both limits together.

## Mount protection and its limits

The default `parker-brain` permission profile extends Codex's `:workspace`
baseline and makes `parker-system/` read-only. This is the filesystem protection
for shell commands and tools, including script-driven writes. It preserves the
baseline restrictions on `.git/`, `.agents/`, and `.codex/`. Updating a submodule
pin or the copied configuration may therefore need an approval.

The mount hook supplies the explanation before native patches and recognizable
shell mutations run. It handles patch additions, updates, deletions and moves,
normalizes parent traversal, and follows symlinks. It is a guardrail, not a shell
interpreter or a security sandbox: indirect commands and specialized tool paths
cannot all be inferred from their text.

Permission profiles do not compose with legacy `sandbox_mode` settings. A user
config, CLI `--sandbox`, a managed policy, or an explicit permission override can
replace the shipped profile. Check the effective permissions when setting up the
brain; a hook alone is not an unconditional read-only guarantee. Keep the normal
policy active for daily work and approve only the specific maintenance command
needed by `/update-brain` or `/disconnect-factory`.

Parker Desktop runs Codex as `codex exec --sandbox workspace-write`, which has no
network and cannot prompt. On app versions that don't attach the mount themselves (before
real-simple-labs/parker-desktop#362), the build's one network git step, the `git submodule add`
of the public factory, cannot run there; `/update-brain`'s `git -C parker-system
fetch` never can. The runner asks the user to run that step in Claude
Code or to switch the tab's sandbox to one with network access, and never
substitutes a copied factory for the mount.

After an approved `/disconnect-factory`, update both runtimes' restrictions and
the root contract. Fully absorbed, independent brains own their method. A team
factory submodule stays read-only unless the team explicitly requests otherwise.

## Trust and delivery

Trust the project and approve its hooks interactively before relying on them,
including in headless jobs. Unapproved hooks may be skipped. Trust is per user
and tied to the hook definitions; changed commands need fresh approval. Updating
a delegated script alone does not change its command's trust hash. Missing
context can also mean a startup error or oversized input, so inspect the hook
diagnostic instead of assuming the user forgot approval.

`scripts/sync-executable-layer.py` delivers the shared scripts, `.codex/`, and
root `AGENTS.md` on a pin bump. The v16 migration supplies the skills symlink.
v17 re-sync delivers the runtime fixes; its migration also adds the scheduling
capability guard to the brand-authored root `CLAUDE.md`. v18 re-sync delivers the
Parker Desktop sync model (`git-guard.py`, `session-start.py`, `save-brain`, root
`AGENTS.md`); in a Parker Desktop folder, saving needs no `.git/` write from the
sandbox, because the app commits outside it. Its migration updates the root `CLAUDE.md`.
Team-edited files remain theirs and are listed by the sync; report any retained
override that prevents a runtime fix from taking effect.

Maintain both configurations together whenever shared hook behavior changes.
Keep review methods in the existing Markdown files; never duplicate the doctrine
for a second runtime. Keep onboarding, disconnect, setup-routines, update-brain,
and this contract aligned. No marketing-output re-run is required solely by a
runtime wiring update.

## References

- [Codex hooks](https://learn.chatgpt.com/docs/hooks): payloads, context limits,
  command overrides, cwd, and trust.
- [Codex permissions](https://learn.chatgpt.com/docs/permissions): named profiles,
  workspace-relative paths, inheritance, and legacy-setting precedence.
- [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents):
  independent reviewers and runtime capability.
