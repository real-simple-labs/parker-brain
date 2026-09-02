#!/usr/bin/env python3
"""PreToolUse guard for git operations in a Parker Brain repo.

A managed brain (one living in Parker's own GitHub org) is synced by the
Parker Desktop app: it watches the folder and syncs every change both ways.
The agent's whole job is to write files — running git against the brand repo
(push, pull, commit, clone, gh) means two sync engines fighting over one
folder. This hook blocks those moves at the moment of the mistake and teaches
the right one: save the files, the app does the rest.

Mount operations pass through: parker-system/ is a pinned submodule of the
public factory, and its local/public ops (submodule init, /update-brain's
fetch + checkout pin move) are the agent's job and need no credentials.
A brain hosted anywhere else (the self-managed exception) is untouched —
the guard only speaks up when the repo's origin (or the command itself)
points at the parker-brain org.

Runtime procedure: .claude/skills/save-brain/ (/save-brain).
Design and rationale: parker-system/system/brain-sync.md.

Fail-open by design: any unexpected error exits 0 so a guard bug can never
brick every Bash call. Exit 2 blocks the tool call and shows stderr to the
model; exit 0 allows silently.

Run with --codex (the .codex/config.toml wiring does) and a block is emitted
as the PreToolUse JSON deny on stdout instead — Codex ignores the exit-2
mechanism, and the JSON permissionDecision form is its native contract. Same
guard, same message, different envelope.
"""

import json
import re
import subprocess
import sys

CODEX = "--codex" in sys.argv

MANAGED_ORG = re.compile(r"github\.com[:/]parker-brain/", re.I)

BLOCK = (
    "This brain's folder is synced by the Parker Desktop app — it watches the "
    "folder and syncs every change both ways, so saving means writing files, "
    "nothing more. Never run git (or gh) against this repo: no push, pull, "
    "fetch, clone, or commit — a second sync engine racing the app is how work "
    "gets destroyed. Just finish writing the files; they sync on their own. "
    "Mount operations are the one exception and pass this guard: `git -C "
    "parker-system …` and `git submodule update --init …` are local, "
    "credential-free, and allowed. If you believe this folder is NOT being "
    "synced (no Parker Desktop), don't improvise git — tell the user plainly "
    "and point them at https://app.heyparker.ai/dashboard/parker-desktop, or "
    "let a technical team wire their own git connection. Full picture: "
    "/save-brain (or parker-system/system/brain-sync.md)."
)


def block(msg: str) -> int:
    """Block the tool call in whichever envelope the harness understands."""
    if CODEX:
        print(json.dumps({
            "decision": "block",
            "reason": msg,
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": msg,
            },
        }))
        return 0
    print(msg, file=sys.stderr)
    return 2


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
    # Claude Code reports the shell tool as Bash; Codex mirrors that name in
    # hook payloads but its native shell tools can also surface directly.
    if data.get("tool_name") not in ("Bash", "shell", "local_shell", "exec_command"):
        return 0
    cmd = (data.get("tool_input") or {}).get("command") or ""
    if isinstance(cmd, list):  # Codex shell tools pass argv lists
        cmd = " ".join(str(c) for c in cmd)
    if not re.search(r"\b(git|gh)\b", cmd):
        return 0

    managed = bool(MANAGED_ORG.search(origin_url())) or bool(MANAGED_ORG.search(cmd))
    if not managed:
        return 0

    # Mount operations are the agent's job and pass through. Plain submodule
    # commands (update/init/sync/status/deinit/add) need no carve-out — they
    # carry no denied verb — so there is deliberately no blanket `submodule`
    # pass: it would shield compound commands like `git submodule status;
    # git push` and `git submodule foreach git push`.
    if "-C parker-system" in cmd:
        return 0

    # gh is blocked only when it would touch THIS repo: it names the managed
    # org, or it's a repo-context subcommand (defaults to the current repo)
    # with no -R/--repo pointing elsewhere. gh search/api/gist/... against
    # other targets is the user's business and passes.
    if re.search(r"(^|[;&|(\s])gh\s", cmd):
        # gh repo subcommands that MUTATE default to the current repo too;
        # plain `gh repo clone/view <target>` names its target and passes.
        repo_context = re.search(
            r"(^|[;&|(\s])gh\s+(pr|issue|release|workflow|run|secret|variable|label|browse"
            r"|repo\s+(rename|delete|archive|unarchive|edit|sync|set-default))\b",
            cmd,
        )
        retargeted = re.search(r"(\s-R\s|--repo[=\s])", cmd)
        names_org = re.search(r"(^|[\s/:\"'=])parker-brain/", cmd, re.I)
        if names_org or (repo_context and not retargeted):
            return block(BLOCK)

    # Cloning a managed-org repo is the app's job; cloning anything ELSE
    # (the public factory for /update-brain's decoupled compare, a reference
    # repo) is fine even from inside a managed brain.
    if re.search(r"\bgit\b[^;&|]*\bclone\b", cmd):
        if MANAGED_ORG.search(cmd):
            return block(BLOCK)
        return 0

    # Everything that moves history, the network, or the working tree on the
    # brand repo is the app's territory: push, pull, commit, and friends —
    # including the destructive local ops (restore, checkout, clean, stash)
    # whose results the app would faithfully sync.
    if re.search(
        r"\bgit\b[^;&|]*\b(push|pull|fetch|commit|rebase|merge|reset|restore"
        r"|checkout|clean|stash|cherry-pick|revert|am|remote\s+set-url"
        r"|branch\s+(-[a-zA-Z]*[dDmMfcC]|--delete|--move|--force|--copy))\b",
        cmd,
    ):
        return block(BLOCK)

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)  # fail open: a guard bug must never block all Bash
