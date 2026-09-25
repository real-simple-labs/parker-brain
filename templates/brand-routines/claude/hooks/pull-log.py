#!/usr/bin/env python3
"""PostToolUse hook: append every MCP tool call to a session pull log.

The grounding gate needs to verify that the data pulls behind a creative
output actually happened — self-reporting is not evidence, because a model
that fabricated a quote can also fabricate having pulled it. This hook is
the record the model cannot write: the harness fires it after every MCP
tool call, and `scripts/grounding-check.py` reads the log back.

The log lives in the OS temp directory, keyed by a hash of the repo path —
never inside the repo, never committed, never visible in any output. It is
plumbing for the reviewer, not a surface for humans.

The same call also clears the `.scaffolded` marker. The build reports every
phase to Parker with `update_parker_brain_setup_status`; the first time it
reports a phase after Phase 0 as completed (or the whole run as completed), the
brain has real content, so the marker that tells Parker's apps "nothing built
yet" comes off right here, in code, instead of waiting for the model to
remember at the end of a multi-hour build.
"""

import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import time


def log_path() -> str:
    key = hashlib.sha256(os.getcwd().encode()).hexdigest()[:16]
    return os.path.join(tempfile.gettempdir(), f"parker-pull-log-{key}.jsonl")


MARKER = Path(".scaffolded")
STATUS_TOOL = "update_parker_brain_setup_status"


def as_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def clears_marker(tool: str, tool_input) -> bool:
    """A setup-status report that means the build has written real content:
    a phase other than Phase 0 reported completed, or the whole run completed."""
    if not tool.endswith("__" + STATUS_TOOL) or not isinstance(tool_input, dict):
        return False
    mode = str(tool_input.get("mode", "")).lower()
    if mode == "complete":
        return str(tool_input.get("run_status", "")).lower() == "completed"
    if mode != "update_phase" or str(tool_input.get("phase_status", "")).lower() != "completed":
        return False
    if re.match(r"\s*phase\s*0(?!\d)", str(tool_input.get("phase_name", "")), re.IGNORECASE):
        return False
    index = as_int(tool_input.get("phase_index"))
    return index is None or index >= 2  # phase 1 of the run is Phase 0


def clear_marker() -> None:
    try:
        if MARKER.is_symlink() or MARKER.is_file():
            MARKER.unlink()
    except OSError:
        pass


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        return
    tool = payload.get("tool_name", "")
    if not tool.startswith("mcp__"):
        return
    if clears_marker(tool, payload.get("tool_input")):
        clear_marker()
    entry = {
        "ts": int(time.time()),
        "session": payload.get("session_id", ""),
        "tool": tool,
    }
    # Keep a hint of what was pulled without storing full payloads: the
    # input's short string values name the query/brand/ad without bulk.
    tool_input = payload.get("tool_input") or {}
    if isinstance(tool_input, dict):
        hints = {
            k: v for k, v in tool_input.items()
            if isinstance(v, (str, int, float)) and len(str(v)) <= 120
        }
        if hints:
            entry["input"] = hints
    try:
        with open(log_path(), "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
