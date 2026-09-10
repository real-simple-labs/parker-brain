# v17 — runtime compatibility fixes

This release repairs the Codex support shipped in v16. Native patches now read
the actual hook payload, including move destinations, and resolve paths and
symlinks correctly. Direct shell mutations receive the same mount explanation.
A default filesystem permission profile protects the method mount against
indirect writes; legacy sandbox settings can override that profile, so verify
the effective permissions when setting up a brain.

Both runtimes launch the shared hooks from the brand root, including subfolder
sessions. Windows has explicit Python launcher commands. The craft catalog has
an explicit context allowance with a bounded user-profile section and a visible
full-read fallback for oversized sources. Independent creative reviewers run
where spawning is available; inline review is reserved for runtimes without it.

Codex onboarding can finish with scheduling explicitly deferred. The walkthrough
describes observed schedule state, and disconnecting the factory updates both
runtimes' mount restrictions and root contracts. Absorbing the method no longer
deinitializes the submodule and deletes its working files; it retains the files
and recovery metadata before converting them to ordinary tracked content.

## Delivery and verification

Runtime changes arrive through the normal executable-layer re-sync;
`migrations/v17.md` adds a scheduling-capability guard to the brand-authored root
`CLAUDE.md`. Changed hook definitions need fresh per-user approval. Team-edited
copies remain untouched and appear in the sync report. Native mount protection
can require a scoped approval for a release-pin update; do not disable daily
protection to perform maintenance.

The standard-library runtime suite exercises native payloads, patch moves,
symlinks, shell writes, nested startup, catalog budgets, pull-log identity, and
both git-guard envelopes, v16 upgrade convergence, idempotence, preservation of
team overrides, and safe submodule absorption. CI runs it on Linux, macOS, and Windows. The optional
Codex 0.154.0 integration probe uses fixed localhost responses and temporary
repos to verify patch denial, shell and indirect-write denial, normal nested
edits, method reads, and complete catalog delivery without model inference.

Claude cloud scheduling remains unavailable from Codex. Hooks remain guardrails,
not a complete shell security boundary. The full contract and verification
commands are in `system/codex-support.md`.
