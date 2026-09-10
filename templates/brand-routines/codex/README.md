# `.codex/` — the brand brain on OpenAI Codex

Same brain, same skills, same method as Claude Code. `config.toml` wires the
shared scripts in `.claude/hooks/` through a launcher that finds the brand root,
including when a session starts in a nested folder. On Windows the commands use
`py -3`; install Python with its Windows launcher. The bootstrap uses Git's
nearest worktree root and never searches above it. Outside a repo, or when that
root has no dispatcher, it exits successfully without running a different repo's
hooks. Repair a missing dispatcher before relying on hook protection.

The `parker-brain` filesystem profile extends Codex's workspace defaults and
makes `parker-system/` read-only. `mount-guard` also catches native patches and
common direct shell writes, but is not a complete shell parser. Arbitrary
programs are confined by the filesystem profile, not by that hook.

## First run and upgrades

1. Trust the project so its configuration loads.
2. Approve the hooks interactively, including changed definitions after an
   upgrade. Approval covers the hook definition; script-only updates do not
   require it again. Headless runs need this approval too.
3. Check the effective permission profile before treating the mount as
   protected. A legacy `sandbox_mode` in any loaded config, or `--sandbox`,
   overrides the named profile. Select the shipped profile or configure an
   equivalent mount restriction; hooks alone do not provide filesystem isolation.

Updating the pinned method or syncing protected configuration may require a
scoped maintenance approval. Keep the default protection in place; follow
`/update-brain`. `/disconnect-factory` explains how to remove both the hook and
the profile's mount restriction when the team deliberately takes ownership.

## Skills, review, and schedules

- `.agents/skills` is a committed symlink to `.claude/skills`: both runtimes read
  the same files. On Windows, enable Git symlinks and Developer Mode before
  checkout; a plain-text placeholder does not load skills.
- Root `AGENTS.md` routes to `CLAUDE.md` and supplies the Parker voice.
- Use independent review contexts whenever spawning is available, passing the
  existing `.claude/agents/*.md` instructions. Only use a clearly labeled inline
  fallback when this session cannot spawn; Markdown discovery differences do
  not remove the review gate.
- The six standing schedules use Claude cloud scheduling. Codex onboarding
  records them as deferred and inactive, then completes; the skills work on
  demand. Do not claim background routines are running without registrations.

The tested baseline is Codex CLI 0.154.0. See
`parker-system/system/codex-support.md` for the full contract and verification.
