# 2026-07-10 — v8: the token leaves the shell — credentials move to a local file

v6 put the token in the `origin` URL, which made every credential refresh a `git remote set-url origin https://x-access-token:ghs_…` — a live token inside a Bash command. Claude Code's permission classifier now blocks exactly that ("Credential Leakage", regardless of destination trust or how briefly the token is exposed), so the refresh and the tokenized clone both died at the prompt for any brand session on default permissions. The flow had to change shape, not just wording.

## What shipped

- **Credentials live in `.git/parker-credentials`** — git's own store-helper file, one line (`https://x-access-token:<TOKEN>@github.com`), written with the **Write tool** so the token never transits a shell command. `origin` goes back to the plain URL; a one-time two-entry wiring (`git config credential.helper ""` then `git config --add credential.helper "store --file .git/parker-credentials"`) makes git read it. The blank first entry is load-bearing: it clears inherited helpers, so a keychain credential on the user's machine can never answer first and push as *them* — verified live on macOS, where system `osxkeychain` otherwise wins. The refresh on an auth error is now: call `setup_parker_brain`, re-write the file, retry — one Write instead of one `set-url`, same hour-long, single-repo, `contents:write` risk envelope, and the file sits inside never-pushed `.git/`.
- **Clone rides the same rail:** credential line in a temp file, `git -c credential.helper= -c credential.helper="store --file <temp>" clone --recurse-submodules <plain url>`, then the file moves into `.git/` and the repo gets the permanent wiring.
- **`git-guard.py`** now also blocks any command carrying the raw token (`x-access-token:` in the command) — the platform would kill it anyway; the guard teaches the file flow at the moment of the mistake. Its credential check accepts the credential file (new) or a token still in `origin` (legacy, until migrated), and a managed clone must carry both `--recurse-submodules` and the `-c credential.helper` flag.
- **Every git-touching surface re-pointed at the one procedure:** `save-brain` (the canonical rewrite), `session-start.py`'s expired-credential message, the brand `CLAUDE.md` template (both git sections), the onboarding runner's clone and save-to-GitHub steps, both bundle READMEs, and the rationale history in `system/brain-git-sync.md`. Each spot carries at least a pointer to `/save-brain`, since the flow has real steps now.
- **`migrations/v8.md`** — real steps: standing managed brains flip `origin` to the plain URL, wire the helper, and mint the file. The bundle files themselves arrive via the pin bump's normal re-sync.

## Cross-repo follow-up

- The `setup_parker_brain` tool message (mevin2 side) still teaches clone-the-authenticated-URL / `set-url`-on-expiry, which now walks agents straight into the platform block. It should teach the credential-file flow and ideally return the token as its own field so no agent has to parse it out of the URL. Until then, the skill and hooks here override the tool message (noted in `system/brain-git-sync.md`).

## Follow-ups

- Cut the `v8` tag once this merges.
