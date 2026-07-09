#!/usr/bin/env python3
"""SessionStart hook for a brand brain: catch a broken method mount before work starts.

The brain's method (prompts, craft knowledge, system docs) lives at parker-system/,
a git submodule of the public parker-brain factory pinned to a release tag. A clone
made without --recurse-submodules arrives with that directory empty, and every
method reference in the brain dangles until it is initialized. This hook checks the
mount at session start and injects instructions only — it runs no git commands
itself, so nothing touches the network or the working tree without the session
seeing it.

It also carries the standing start-of-session reminder: pull before working, since
cloud routines and teammates push to this repo between sessions.
"""

import json
import subprocess
from pathlib import Path

MOUNT = Path("parker-system")


def mount_state() -> str:
    """'ok', 'empty' (gitlink present but never initialized), or 'absent'."""
    if not MOUNT.exists():
        return "absent"
    if not any(MOUNT.iterdir()):
        return "empty"
    return "ok"


def pinned_tag() -> str:
    try:
        out = subprocess.run(
            ["git", "-C", str(MOUNT), "describe", "--tags", "--exact-match"],
            capture_output=True, text=True, timeout=5,
        )
        return out.stdout.strip() if out.returncode == 0 else ""
    except Exception:
        return ""


state = mount_state()

if state == "ok":
    tag = pinned_tag()
    pin = f" (pinned to factory release {tag})" if tag else ""
    context = (
        f"Session start check: the parker-system/ method mount is initialized{pin}. "
        "Before starting real work, bring the brain current: run "
        "`git pull --recurse-submodules` — the scheduled cloud routines and any "
        "teammates push to this repo between sessions, and working on a stale clone "
        "loses their changes. parker-system/ itself is read-only; factory updates "
        "arrive only through /update-brain moving the pin."
    )
else:
    context = (
        "Session start check: the parker-system/ method mount is "
        + ("EMPTY — this clone was made without --recurse-submodules."
           if state == "empty" else "MISSING.")
        + " The brain's prompts, craft knowledge, and system docs all live in that "
        "mount, so nothing method-driven will work until it is initialized. Fix it "
        "before anything else: run `git submodule update --init parker-system`, "
        "then verify the directory has content. If this repo was never cloned with "
        "the mount, `git pull --recurse-submodules` afterward keeps it current. "
        "The mount is read-only — never edit inside it; /update-brain is how it "
        "updates. Where to read more: this repo's README.md and CLAUDE.md, and the "
        "factory's own README inside the mount once initialized."
    )

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": context,
    }
}))
