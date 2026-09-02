#!/usr/bin/env python3
"""PreToolUse guard (Codex): keep the parker-system/ method mount read-only.

On Claude Code the mount is protected by the permissions.deny rules in
.claude/settings.json. Codex has no per-path deny rules, so this hook is the
same protection expressed as a PreToolUse deny: any edit or write whose target
resolves under parker-system/ is blocked with the standing explanation — the
mount is a pinned submodule of the factory, and updates arrive only through
/update-brain moving the pin.

Wired only in .codex/config.toml (Claude Code never needs it, but running it
there would be harmless — it emits the JSON deny both harnesses understand).
Fails open: any unexpected error exits 0 so a guard bug can never block all
edits.
"""

import json
import re
import sys

MOUNT = "parker-system/"

REASON = (
    "parker-system/ is the read-only factory method mount — a pinned submodule "
    "of the public parker-brain repo. Never edit inside it; updates arrive only "
    "through /update-brain moving the pin. Anything brand-specific belongs at "
    "the repo root (brand-lens.md, expert-insights/, the vault docs), never in "
    "the mount."
)

# apply_patch hunk headers that carry file paths.
PATCH_PATH = re.compile(
    r"^(?:\*\*\* (?:Add|Update|Delete) File: |--- a/|\+\+\+ b/|--- |\+\+\+ )(.+)$"
)


def targets(tool: str, tool_input: dict):
    if tool in ("Edit", "Write", "NotebookEdit"):
        path = tool_input.get("file_path") or tool_input.get("notebook_path") or ""
        if path:
            yield path
    elif tool == "apply_patch":
        patch = tool_input.get("input") or tool_input.get("patch") or ""
        for line in str(patch).splitlines():
            m = PATCH_PATH.match(line)
            if m and m.group(1) != "/dev/null":
                yield m.group(1)


def in_mount(path: str) -> bool:
    p = path.lstrip("./")
    return p.startswith(MOUNT) or f"/{MOUNT}" in path


def main() -> int:
    data = json.load(sys.stdin)
    tool = data.get("tool_name", "")
    tool_input = data.get("tool_input") or {}
    if not isinstance(tool_input, dict):
        return 0
    for path in targets(tool, tool_input):
        if in_mount(path):
            print(json.dumps({
                "decision": "block",
                "reason": REASON,
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": REASON,
                },
            }))
            return 0
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)  # fail open: a guard bug must never block all edits
