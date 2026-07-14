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
from pathlib import Path

MANAGED_ORG = re.compile(r"github\.com[:/]parker-brain/", re.I)
TOKEN_MARK = "x-access-token:"
CRED_FILE = Path(".git/parker-credentials")

HOW = (
    "Get fresh 1-hour credentials with the setup_parker_brain tool (Parker MCP; its "
    "brand_id is in parker_config.json at the repo root — read it, don't guess; if "
    "that file is missing, call get_available_brands and use the exact brand_id it "
    "returns for this brand), lift "
    "the token out of its authenticated_clone_url, run `rm -f .git/parker-credentials` "
    "(the Write tool won't overwrite an unread file), and use the Write tool to save "
    "this single line to .git/parker-credentials:\n"
    "  https://x-access-token:<TOKEN>@github.com\n"
    "with origin on the plain URL and the one-time repo wiring in place "
    "(`git config credential.helper \"\"` then `git config --add credential.helper "
    "\"store --file .git/parker-credentials\"` — the blank entry shuts out the user's "
    "own helpers), then retry (always `git push origin main`, never a bare `git push`). "
    "Full procedure: /save-brain (or parker-system/system/brain-git-sync.md)."
)

BLOCK_GH = (
    "This brain lives in Parker's own GitHub (the parker-brain org), and `gh` runs on "
    "the user's personal login, which must never touch this repo — no gh pushes, PRs, "
    "issues, or API calls against it. Repo work here is plain git with Parker's own "
    "credentials. (`gh` pointed anywhere else is fine — name the target explicitly "
    "with -R/--repo or a full owner/repo.) " + HOW
)
BLOCK_AUTH = (
    "This command would hit the brain's private GitHub with the user's own login (or "
    "no login), and it will fail or misattribute the change. " + HOW
)
BLOCK_TOKEN = (
    "Never put the token inside a shell command — not in a clone URL, not in `git "
    "remote set-url`, not in an echo. Claude's safety layer blocks any command "
    "carrying a live token, and the credential file makes it unnecessary. " + HOW
)
BLOCK_CLONE_CREDS = (
    "Cloning a managed Parker Brain needs Parker's credentials, supplied without the "
    "token ever entering the command: Write the credential line to a temp file first, "
    "then `git -c credential.helper= -c credential.helper=\"store --file <temp file>\" "
    "clone --recurse-submodules <plain https URL> <folder>` (the empty first -c shuts "
    "out the user's own helpers), and after the clone move the file to "
    ".git/parker-credentials inside it. Full procedure: /save-brain (or "
    "parker-system/system/brain-git-sync.md)."
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
    if not re.search(r"\b(git|gh)\b", cmd) and TOKEN_MARK not in cmd:
        return 0

    origin = origin_url()
    managed = bool(MANAGED_ORG.search(origin)) or bool(MANAGED_ORG.search(cmd))
    if not managed:
        return 0
    try:
        has_creds = CRED_FILE.is_file() and CRED_FILE.stat().st_size > 0
    except OSError:
        has_creds = False
    has_creds = has_creds or TOKEN_MARK in origin  # legacy token-in-remote, pre-v8

    if TOKEN_MARK in cmd:
        print(BLOCK_TOKEN, file=sys.stderr)
        return 2

    # gh is blocked only when it would touch THIS repo: it names the managed
    # org, or it's a repo-context subcommand (defaults to the current repo)
    # with no -R/--repo pointing elsewhere. gh search/api/gist/... against
    # other targets is the user's business and passes.
    if re.search(r"(^|[;&|(\s])gh\s", cmd):
        repo_context = re.search(
            r"(^|[;&|(\s])gh\s+(pr|issue|release|workflow|run|secret|variable|label|browse)\b",
            cmd,
        )
        retargeted = re.search(r"(\s-R\s|--repo[=\s])", cmd)
        # Org mentions in gh commands come bare (repos/parker-brain/x, -R
        # parker-brain/x), not just as github.com URLs.
        names_org = re.search(r"(^|[\s/:\"'=])parker-brain/", cmd, re.I)
        if names_org or (repo_context and not retargeted):
            print(BLOCK_GH, file=sys.stderr)
            return 2

    if re.search(r"\bgit\b[^;&|]*\bclone\b", cmd):
        if "--recurse-submodules" not in cmd:
            print(BLOCK_CLONE, file=sys.stderr)
            return 2
        # Both entries required: the blank reset (shuts out the user's own
        # helpers, e.g. the macOS keychain) AND the store helper.
        blank_reset = re.search(r"credential\.helper=([\"']\s*[\"'])?(\s|$)", cmd)
        store_helper = re.search(r"credential\.helper=[\"']?store\b", cmd)
        if not (blank_reset and store_helper):
            print(BLOCK_CLONE_CREDS, file=sys.stderr)
            return 2

    if re.search(r"\bgit\b[^;&|]*\bpush\b[^;&|]*(\s--force\b|\s-f\b|\s--force-with-lease\b)", cmd):
        print(BLOCK_FORCE, file=sys.stderr)
        return 2

    network = re.search(r"\bgit\b[^;&|]*\b(push|pull|fetch)\b", cmd)
    if network and "-C parker-system" not in cmd and not has_creds:
        print(BLOCK_AUTH, file=sys.stderr)
        return 2

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)  # fail open: a guard bug must never block all Bash
