#!/usr/bin/env python3
"""Explain mount writes before they reach the filesystem sandbox.

Patch inspection handles the native patch format. Shell inspection catches
direct redirections and common mutations; it is not a shell interpreter.
The permission profile protects against indirect program-driven writes.
"""

import json
import os
from pathlib import Path, PureWindowsPath
import re
import shlex
import sys

ROOT = Path(__file__).resolve().parents[2]
MOUNT = ROOT / "parker-system"
PATCH_PATH = re.compile(r"^\*\*\* (?:(?:Add|Update|Delete) File|Move to): (.+)$")
SHELL_TOOLS = {"Bash", "shell", "local_shell", "exec_command"}
REASON = (
    "parker-system/ is the read-only factory method mount. Brand changes belong "
    "outside it; /update-brain moves its release pin. Use /disconnect-factory "
    "only when the team explicitly wants to own and edit the method."
)


def in_mount(path: str, cwd: Path) -> bool:
    target = Path(path).expanduser()
    if not target.is_absolute():
        target = cwd / target
    return target.resolve().is_relative_to(MOUNT.resolve())


def patch_targets(patch: str):
    for line in patch.splitlines():
        match = PATCH_PATH.match(line)
        if match:
            yield match.group(1)


def shell_targets(command: str, cwd: Path, *, windows: bool = os.name == "nt"):
    """Inspect ordinary commands; the native sandbox handles arbitrary programs."""
    lexer = shlex.shlex(command, posix=not windows, punctuation_chars=";&|<>")
    lexer.whitespace_split = True
    segment = []
    for token in [*lexer, ";"]:
        if token not in (";", "&&", "||", "|", "&"):
            segment.append(token)
            continue
        if not segment:
            continue
        for index, word in enumerate(segment[:-1]):
            if ">" in word and set(word) <= set("><&"):
                yield segment[index + 1].strip("\"'"), cwd
        words = [s.strip("\"'") for s in segment]
        verb = (PureWindowsPath(words[0]) if windows else Path(words[0])).name.lower()
        args = [s for s in words[1:] if not s.startswith("-")]
        if windows and verb == "copy":
            # CMD accepts /A and /B after a destination as well as after sources.
            switches = {"/a", "/b", "/d", "/v", "/n", "/y", "/-y", "/z", "/l"}
            args = [s for s in args if s.lower() not in switches]
        if verb == "cd" and args:
            cwd = (cwd / args[0]).resolve()
        elif verb in {"rm", "rmdir", "unlink", "touch", "mkdir", "truncate",
                      "tee", "mv", "chmod", "chown", "del", "erase", "rd", "move"}:
            for arg in args:
                yield arg, cwd
        elif verb in {"cp", "copy", "install", "ln"} and args:
            # Copying out of the mount is allowed; only its destination mutates.
            if "-t" in words or "--target-directory" in words:
                flag = "-t" if "-t" in words else "--target-directory"
                yield words[words.index(flag) + 1], cwd
            else:
                yield args[-1], cwd
        elif verb in {"sed", "perl"} and any(s.startswith("-i") for s in words[1:]):
            for arg in args:
                yield arg, cwd
        segment = []


def main() -> int:
    data = json.load(sys.stdin)
    tool = data.get("tool_name", "")
    inputs = data.get("tool_input") or {}
    if not isinstance(inputs, dict):
        return 0
    cwd = Path(data.get("cwd") or ROOT).resolve()
    if tool == "apply_patch":
        patch = inputs.get("command") or inputs.get("input") or inputs.get("patch") or ""
        targets = ((path, cwd) for path in patch_targets(patch))
    elif tool in {"Edit", "Write", "NotebookEdit"}:
        path = inputs.get("file_path") or inputs.get("notebook_path")
        targets = [(path, cwd)] if path else []
    elif tool in SHELL_TOOLS:
        command = inputs.get("command") or inputs.get("cmd") or ""
        if isinstance(command, list):
            command = shlex.join(command)
        targets = shell_targets(command, cwd)
    else:
        return 0
    if any(in_mount(path, base) for path, base in targets):
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": REASON,
        }}))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, TypeError, IndexError) as error:
        # The native permission profile still protects the mount on inspection errors.
        print(f"Mount guard could not inspect this call: {error}", file=sys.stderr)
        sys.exit(1)
