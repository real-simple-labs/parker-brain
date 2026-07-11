#!/usr/bin/env python3
"""SessionStart hook for a brand brain: catch a broken method mount before work starts.

The brain's method (prompts, craft knowledge, system docs) lives at parker-system/,
a git submodule of the public parker-brain factory pinned to a release tag. A clone
made without --recurse-submodules arrives with that directory empty, and every
method reference in the brain dangles until it is initialized. This hook checks the
mount at session start.

On the standard layout it also DOES the start-of-session pull itself when that is
safe — working tree clean, remote present — because cloud routines and teammates
push to this repo between sessions and sessions were skipping the pull when it was
only a reminder. A dirty tree, an expired credential, or any other failure is never
papered over: the hook reports it loudly and makes fixing it the session's first
job. Non-interactive throughout (GIT_TERMINAL_PROMPT=0), so it can never hang
waiting for a password.
"""

import json
import os
import subprocess
from pathlib import Path

MOUNT = Path("parker-system")
AUTH_SIGNS = ("authentication failed", "403", "401", "could not read username",
              "terminal prompts disabled", "invalid username or token")


def git(*args: str, timeout: int = 45) -> subprocess.CompletedProcess:
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0")
    return subprocess.run(["git", *args], capture_output=True, text=True,
                          timeout=timeout, env=env)


def attempt_pull() -> str:
    """Run the start-of-session pull when safe; return the story for the model."""
    try:
        if git("remote", "get-url", "origin", timeout=5).returncode != 0:
            return ("No `origin` remote is configured, so nothing was pulled. If this "
                    "brain lives on GitHub, wire the remote per /save-brain before working.")
        dirty = git("status", "--porcelain", timeout=10).stdout.strip()
        if dirty:
            return ("PULL SKIPPED — the working tree has uncommitted changes (likely a "
                    "previous session that ended without saving). First job of this "
                    "session, before anything else: commit and push those changes per "
                    "/save-brain (`git add -A && git commit`, `git pull --rebase origin "
                    "main`, `git push origin main`), refreshing credentials via "
                    "setup_parker_brain if a step hits an auth error.")
        pulled = git("pull", "--rebase", "origin", "main")
        if pulled.returncode == 0:
            git("submodule", "update", "--init", timeout=60)
            summary = (pulled.stdout or "").strip().splitlines()
            tail = summary[-1] if summary else "done"
            return f"Pulled the latest before starting: {tail}."
        err = (pulled.stderr or "").lower()
        if any(s in err for s in AUTH_SIGNS):
            return ("PULL FAILED — the saved credentials have expired (they last about "
                    "an hour; this is normal). First job of this session, before any "
                    "other work: call setup_parker_brain (Parker MCP) for a fresh "
                    "authenticated URL, run `git remote set-url origin <that url>`, then "
                    "`git pull --rebase origin main` and `git submodule update --init`.")
        detail = (pulled.stderr or pulled.stdout or "").strip().splitlines()
        return ("PULL FAILED — not an auth problem: "
                + (detail[-1] if detail else "unknown error")
                + ". Resolve it per /save-brain before editing anything; teammates and "
                  "scheduled routines push to this repo between sessions.")
    except Exception as exc:  # noqa: BLE001 — a hook must never crash the session
        return f"PULL SKIPPED — the automatic pull hit an unexpected error ({exc}); run it by hand per /save-brain."


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
        "It is theirs to edit and versions with the repo. Before starting real "
        "work, bring the brain current: run `git pull` — the scheduled cloud "
        "routines and any teammates push to this repo between sessions. "
        "/update-brain runs in decoupled mode here, per running-notes/standard-sync.md."
    )
elif state == "ok" and not is_submodule:
    context = (
        "Session start check: parker-system/ carries the method as an older "
        "vendored copy (plain files, no submodule) — this brain predates the "
        "current layout and has not been migrated. That's fine to work with "
        "today, but don't edit inside parker-system/ (updates would overwrite "
        "it), and don't treat this as a decoupled brain. The current standard "
        "mounts the factory as a pinned submodule; /update-brain can offer the "
        "v1 migration that converts this brain. Before real work, run `git pull` "
        "— cloud routines and teammates push to this repo between sessions."
    )
elif state == "ok":
    tag = pinned_tag()
    pin = f" (pinned to factory release {tag})" if tag else ""
    context = (
        f"Session start check: the parker-system/ method mount is initialized{pin}. "
        + attempt_pull() +
        " parker-system/ itself is read-only; factory updates arrive only through "
        "/update-brain moving the pin. Standing rule: every change this session makes "
        "gets committed and pushed immediately per /save-brain — never left local, "
        "never held for a 'should I save?' question."
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
