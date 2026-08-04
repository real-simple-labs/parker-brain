# 2026-08-04 — v15: the agent leaves the credential loop — git auth moves to `@heyparker/sync`

v8 moved the token out of shell commands into `.git/parker-credentials`, and v10 pre-approved the writes — but the agent was still the courier: token in a tool result, through model context, into a file, once an hour, per repo. The platform classifier kept blocking the write most of the time anyway, and the per-repo helper wiring turned toxic the moment anything better existed, shadowing it and breaking pulls with username/password prompts. The fix is to remove the agent from the loop entirely, using the extension point git built for exactly this.

## What shipped

- **Machine-level credential helper.** A one-time `npx @heyparker/sync setup` signs the user into Parker (browser; no GitHub account needed), installs `~/.parker/bin/parker-credential`, and writes a global gitconfig block scoped to `https://github.com/parker-brain/` — blank-entry chain reset (the keychain-misattribution guard, now org-scoped), the helper, and `useHttpPath` so one helper serves every brand. On every git network operation, Parker's backend checks brand membership and mints a ≤1-hour, single-repo, `contents:write` GitHub App token, returned straight to git. Nothing is stored client-side, nothing enters model context, nothing expires mid-work, and revoking a member in Parker cuts their access within the hour.
- **`save-brain` rewritten.** Clone is a plain `git clone --recurse-submodules <plain URL>`; the credential sections collapse to "you never touch them"; a new legacy-cleanup section teaches clean-on-sight for the retired wiring (`git config --local --unset-all credential.helper`, delete `.git/parker-credentials`, strip a pre-v8 tokenized origin); the auth-failure playbook becomes a three-rung ladder (legacy wiring → helper missing → helper refusing).
- **`session-start.py` self-heals.** On an auth-failed pull it now performs the legacy cleanup deterministically (no secrets in any command) and retries once before reporting; its failure message teaches the one-time setup, with the user-present caveat for headless runs.
- **`git-guard.py` re-keyed.** The auth check accepts the machine-level helper (or, mid-transition, a legacy credential file / token-in-origin); plain clones are the standard and only a helper-less machine gets blocked; hand-carried tokens stay blocked; block messages teach the new flow.
- **`settings.json`** drops the credential-write pre-approvals (nothing writes credentials anymore) and pre-approves `npx @heyparker/sync setup` plus the two cleanup commands.
- **Onboarding runner + brand `CLAUDE.md` template + both bundle READMEs** re-pointed: provisioning still comes from `setup_parker_brain`, but the clone step is plain, the helper check happens before it, and the save-to-GitHub step loses the re-mint dance.
- **`migrations/v15.md`** — real steps: the one-time machine setup (interactive; headless runs defer it and keep the legacy flow until then) and the per-repo cleanup, ordered so the old wiring is never removed before the helper exists.

## Cross-repo

- **mevin2 gains `POST /api/git-credential`** (separate PR): reads git's credential-protocol request, authorizes against `parker_brain_repositories` + brand membership (admin fallback for unmapped repos under the org), mints the downscoped installation token via the existing GitHub App service, answers in git credential format with `password_expiry_utc`. Runs behind the existing `/api/*` auth middleware.
- **`@heyparker/sync` npm package** (new, to publish): the setup CLI (device-flow sign-in, helper install, gitconfig wiring) and the ~20-line helper it installs. The tool-message duty from v8 carries forward: once standing brains migrate, `setup_parker_brain` should stop returning `credential_file_line`/`authenticated_clone_url` entirely.

## Follow-ups

- Publish `@heyparker/sync` before cutting the tag — the migration's step 1 depends on it.
- Cut the `v15` tag once this merges and the package is live.
