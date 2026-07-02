#!/usr/bin/env python3
"""UserPromptSubmit hook for a brand brain: put the craft catalog in front of every turn.

A reminder to go read the catalog gets skipped; the catalog itself does not.
This reads the generated DOC-MAP table out of
parker-system/creative-strategy-context/expertise-routing.md (cwd is the repo
root when Claude Code runs hooks) and injects it, so the planner sees the menu
of method docs on every message instead of having to remember one exists.
Falls back to the plain instruction if the file is missing or unreadable.
"""

import json
import re
from pathlib import Path

ROUTING = Path("parker-system/creative-strategy-context/expertise-routing.md")

INSTRUCTION = (
    "The base Claude harness knows nothing about creative strategy, so assume your own "
    "creative-strategy knowledge is thin and ungrounded until you load the craft docs. "
    "For anything touching creative strategy, before you answer: reason over the craft "
    "catalog below generously, open every method doc that would genuinely help, and load "
    "the expert-insights and the brand lens overlay if one exists. Ground every insight "
    "in those methods and speak their vocabulary. Close every substantive answer with its "
    "Sources list and check the receipt before sending: a creative or strategic answer "
    "whose sources name no method doc is presumed under-retrieved. Rebuild it, don't ship it. "
    "Use the vault hard and honor the brand hard rules."
)

FALLBACK_POINTER = (
    " The catalog lives at parker-system/creative-strategy-context/expertise-routing.md; "
    "open it to see every method doc."
)


def catalog() -> str:
    try:
        text = ROUTING.read_text(encoding="utf-8")
        m = re.search(r"<!-- DOC-MAP:START -->\n(.*?)\n<!-- DOC-MAP:END -->", text, re.DOTALL)
        if m:
            return (
                "\n\nThe craft catalog (generated from expertise-routing.md; "
                "paths are relative to parker-system/creative-strategy-context/):\n"
                + m.group(1).strip()
            )
    except OSError:
        pass
    return FALLBACK_POINTER


print(
    json.dumps(
        {
            "hookSpecificOutput": {
                "hookEventName": "UserPromptSubmit",
                "additionalContext": INSTRUCTION + catalog(),
            }
        }
    )
)
