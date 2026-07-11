#!/usr/bin/env python3
"""Stop hook for a brand brain: never end a turn with unsaved work.

Teammates and scheduled routines share this repo; work that isn't committed AND
pushed doesn't exist for them, and two sessions editing unpushed copies is how
work gets destroyed. So when a turn is about to end on a managed repo
(origin under the parker-brain org) with uncommitted changes or unpushed
commits, this hook blocks the stop once and tells the agent to run the
/save-brain loop.

Loop safety, two layers:
- `stop_hook_active` true means a Stop hook already blocked this turn once —
  we let the turn end (whatever went wrong needs the user, not an infinite
  loop) and just describe the leftover state.
- A fingerprint of the unsaved state (dirty files + HEAD + unpushed count) is
  remembered in the OS temp dir after every block. If the exact same state
  comes back on a later turn — a persistent git error nobody can fix right
  now — the guard stays silent instead of taxing every turn with a doomed
  retry. Any new work changes the fingerprint and re-arms it, and the
  session-start hook independently reports a dirty tree next session.

Fail-open by design: any unexpected error exits 0. Like git-guard, the
settings entry must NOT get the `2>/dev/null || true` wrapper — exit code 2
and stderr are the mechanism.
"""

import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

MANAGED_ORG = re.compile(r"github\.com[:/]parker-brain/", re.I)

MARKER = Path(tempfile.gettempdir()) / (
    "parker-commit-guard-"
    + hashlib.sha1(str(Path.cwd()).encode()).hexdigest()[:12]
)


def git(*args: str) -> subprocess.CompletedProcess:
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0")
    return subprocess.run(["git", *args], capture_output=True, text=True,
                          timeout=10, env=env)


def main() -> int:
    data = json.load(sys.stdin)

    origin = git("remote", "get-url", "origin")
    if origin.returncode != 0 or not MANAGED_ORG.search(origin.stdout):
        return 0  # self-hosted or remote-less: the team's own workflow governs

    dirty = git("status", "--porcelain").stdout.strip()
    unpushed = ""
    ahead = git("rev-list", "--count", "origin/main..HEAD")
    if ahead.returncode == 0 and ahead.stdout.strip() not in ("", "0"):
        unpushed = ahead.stdout.strip()

    if not dirty and not unpushed:
        MARKER.unlink(missing_ok=True)  # saved state reached; re-arm for future work
        return 0

    head = git("rev-parse", "HEAD").stdout.strip()
    fingerprint = hashlib.sha1(f"{dirty}\n{head}\n{unpushed}".encode()).hexdigest()
    already_demanded = MARKER.exists() and MARKER.read_text().strip() == fingerprint
    if already_demanded:
        return 0  # we blocked for exactly this state before; a persistent error
                  # shouldn't tax every turn with a doomed retry

    state = []
    if dirty:
        state.append("uncommitted changes")
    if unpushed:
        state.append(f"{unpushed} commit(s) never pushed")
    described = " and ".join(state)

    if data.get("stop_hook_active"):
        # Already blocked once this turn; don't loop. Remember the state so an
        # unfixable error doesn't re-block every following turn, and surface it.
        MARKER.write_text(fingerprint)
        print(f"Note: the turn is ending with {described}. If a push failed, tell "
              "the user plainly and leave the fix at the top of the next session.",
              file=sys.stderr)
        return 0

    MARKER.write_text(fingerprint)

    print(
        f"This brain has {described} — finish the save before ending the turn, "
        "without asking the user (saving is part of the work): "
        "`git add -A && git commit -m \"<plain summary>\"`, "
        "`git pull --rebase origin main`, `git submodule update --init --recursive`, "
        "`git push origin main`. "
        "On an auth error, call setup_parker_brain (Parker MCP), "
        "`git remote set-url origin <fresh authenticated url>`, and retry. "
        "Full procedure: /save-brain.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)  # fail open: a guard bug must never trap the session
