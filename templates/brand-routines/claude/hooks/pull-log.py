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
"""

import hashlib
import json
import os
import sys
import tempfile
import time


def log_path() -> str:
    key = hashlib.sha256(os.getcwd().encode()).hexdigest()[:16]
    return os.path.join(tempfile.gettempdir(), f"parker-pull-log-{key}.jsonl")


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        return
    tool = payload.get("tool_name", "")
    if not tool.startswith("mcp__"):
        return
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
