#!/usr/bin/env python3
"""PreToolUse guard for git operations in a Parker Brain repo.

A brain that lives in Parker's own GitHub org must sync with the short-lived
credentials the setup_parker_brain tool (Parker MCP) mints — never the user's
personal login, never `gh`. This hook enforces that at the moment of the
mistake: it inspects each Bash command before it runs and blocks the wrong
move with a message that teaches the right one. A brain hosted anywhere else
(the rare self-hosted exception) is untouched — the guard only speaks up when
the repo's origin (or the command itself) points at the parker-brain org.

Runtime procedure: .claude/skills/save-brain/ (/save-brain).
Design and rationale: parker-system/system/brain-git-sync.md.

Fail-open by design: any unexpected error exits 0 so a guard bug can never
brick every Bash call. Exit 2 blocks the tool call and shows stderr to the
model; exit 0 allows silently.
"""

import json
import re
import subprocess
import sys

MANAGED_ORG = re.compile(r"github\.com[:/]parker-brain/", re.I)
TOKEN_MARK = "x-access-token:"

HOW = (
    "Get fresh 1-hour credentials with the setup_parker_brain tool (Parker MCP), then:\n"
    "  git remote set-url origin <authenticated_clone_url>\n"
    "and retry (always `git push origin main`, never a bare `git push`). "
    "Full procedure: /save-brain (or parker-system/system/brain-git-sync.md)."
)

BLOCK_GH = (
    "This brain lives in Parker's own GitHub (the parker-brain org). `gh` runs on the "
    "user's personal login, which must never touch this repo. Use plain git with "
    "Parker's own credentials instead. " + HOW
)
BLOCK_AUTH = (
    "This command would hit the brain's private GitHub with the user's own login (or "
    "no login), and it will fail or misattribute the change. " + HOW
)
BLOCK_FORCE = (
    "Never force-push a Parker Brain: there is no branch protection, and a force-push "
    "can erase a teammate's work. `git pull --rebase` first, resolve conflicts "
    "best-effort (prefer keeping both sides), then `git push origin main` normally."
)
BLOCK_CLONE = (
    "Cloning a Parker Brain needs its method mount: add --recurse-submodules, or the "
    "brain arrives with an empty parker-system/ and none of the method resolves."
)


def origin_url() -> str:
    try:
        r = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            capture_output=True, text=True, timeout=5,
        )
        return r.stdout.strip()
    except Exception:
        return ""


def main() -> int:
    data = json.load(sys.stdin)
    if data.get("tool_name") != "Bash":
        return 0
    cmd = (data.get("tool_input") or {}).get("command") or ""
    if not re.search(r"\b(git|gh)\b", cmd):
        return 0

    origin = origin_url()
    managed = bool(MANAGED_ORG.search(origin)) or bool(MANAGED_ORG.search(cmd))
    if not managed:
        return 0
    has_token = TOKEN_MARK in cmd or TOKEN_MARK in origin

    if re.search(r"(^|[;&|(\s])gh\s", cmd):
        print(BLOCK_GH, file=sys.stderr)
        return 2

    if re.search(r"\bgit\b[^;&|]*\bclone\b", cmd) and "--recurse-submodules" not in cmd:
        print(BLOCK_CLONE, file=sys.stderr)
        return 2

    if re.search(r"\bgit\b[^;&|]*\bpush\b[^;&|]*(\s--force\b|\s-f\b|\s--force-with-lease\b)", cmd):
        print(BLOCK_FORCE, file=sys.stderr)
        return 2

    network = re.search(r"\bgit\b[^;&|]*\b(push|pull|fetch)\b", cmd)
    if network and "-C parker-system" not in cmd and not has_token:
        print(BLOCK_AUTH, file=sys.stderr)
        return 2

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)  # fail open: a guard bug must never block all Bash
