#!/usr/bin/env python3
"""SessionStart hook for a brand brain: catch a broken method mount before work starts.

The brain's method (prompts, craft knowledge, system docs) lives at parker-system/,
a git submodule of the public parker-brain factory pinned to a release tag. A folder
that arrives without it (or with it empty) leaves every method reference dangling
until it is initialized. This hook checks the mount at session start.

Syncing is NOT this hook's job: the Parker Desktop app watches the brain's folder
and syncs every change both ways, so the hook only reminds the model of the model —
files save to disk, the app does the rest, never run git against this repo.
"""

import json
import subprocess
from pathlib import Path

MOUNT = Path("parker-system")

SYNC_LINE = (
    " How this brain saves itself: the Parker Desktop app syncs this folder both "
    "ways — write files to disk and they're saved; teammates' and routines' changes "
    "arrive on their own. Never run git against this repo (no push, pull, commit, "
    "clone, or gh) — see /save-brain. Mount operations (`git -C parker-system …`, "
    "`git submodule …`) are the one exception and are fine."
)


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

# A submodule checkout carries a .git *file* inside the mount. Plain tracked
# files there mean one of two very different things: the team deliberately
# decoupled (/disconnect-factory stamps posture own-factory/independent in the
# ledger), or this is a legacy brain still carrying the old vendored copy and
# not yet migrated. Only the ledger's posture separates them — never assume
# decoupled without it.
is_submodule = (MOUNT / ".git").exists()


def decoupled_by_choice() -> bool:
    try:
        ledger = Path("running-notes/standard-sync.md").read_text(encoding="utf-8")
    except OSError:
        return False
    for line in ledger.splitlines():
        if "posture" in line.lower():
            return "own-factory" in line or "independent" in line
    return False


if state == "ok" and not is_submodule and decoupled_by_choice():
    context = (
        "Session start check: parker-system/ holds this team's own copy of the "
        "method (this brain is decoupled from the factory — no submodule, no pin). "
        "It is theirs to edit and versions with the repo. /update-brain runs in "
        "decoupled mode here, per running-notes/standard-sync.md." + SYNC_LINE
    )
elif state == "ok" and not is_submodule:
    context = (
        "Session start check: parker-system/ carries the method as an older "
        "vendored copy (plain files, no submodule) — this brain predates the "
        "current layout and has not been migrated. That's fine to work with "
        "today, but don't edit inside parker-system/ (updates would overwrite "
        "it), and don't treat this as a decoupled brain. The current standard "
        "mounts the factory as a pinned submodule; /update-brain can offer the "
        "v1 migration that converts this brain." + SYNC_LINE
    )
elif state == "ok":
    tag = pinned_tag()
    pin = f" (pinned to factory release {tag})" if tag else ""
    context = (
        f"Session start check: the parker-system/ method mount is initialized{pin}. "
        "parker-system/ itself is read-only; factory updates arrive only through "
        "/update-brain moving the pin." + SYNC_LINE
    )
else:
    context = (
        "Session start check: the parker-system/ method mount is "
        + ("EMPTY — it was never initialized here."
           if state == "empty" else "MISSING.")
        + " The brain's prompts, craft knowledge, and system docs all live in that "
        "mount, so nothing method-driven will work until it is initialized. Fix it "
        "before anything else: run `git submodule update --init parker-system`, "
        "then verify the directory has content (this is a local, credential-free "
        "operation against the public factory — allowed and expected). The mount "
        "is read-only — never edit inside it; /update-brain is how it updates. "
        "Where to read more: this repo's README.md and CLAUDE.md, and the "
        "factory's own README inside the mount once initialized." + SYNC_LINE
    )

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": context,
    }
}))
