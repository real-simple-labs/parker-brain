#!/usr/bin/env python3
"""UserPromptSubmit hook for a brand brain: put the craft catalog in front of every turn.

A reminder to go read the catalog gets skipped; the catalog itself does not.
This reads the generated DOC-MAP table out of
parker-system/creative-strategy-context/expertise-routing.md (cwd is the repo
root when Claude Code runs hooks) and injects it, so the planner sees the menu
of method docs on every message instead of having to remember one exists.
Falls back to the plain instruction if the file is missing or unreadable.
"""

import glob
import json
import re
from pathlib import Path

# The standard layout mounts the craft layer at parker-system/ (a pinned
# submodule of the factory); legacy flat brains keep it at the repo root.
# Check both so the same script works in either.
_CANDIDATES = [
    Path("parker-system/creative-strategy-context/expertise-routing.md"),
    Path("creative-strategy-context/expertise-routing.md"),
]
ROUTING = next((p for p in _CANDIDATES if p.exists()), _CANDIDATES[0])

INSTRUCTION = (
    "The base Claude harness knows nothing about creative strategy, so assume your own "
    "creative-strategy knowledge is thin and ungrounded until you load the craft docs. "
    "For anything touching creative strategy, before you answer: reason over the craft "
    "catalog below generously, open every method doc that would genuinely help, and load "
    "the expert-insights (expert-insights/ at the repo root) and the brand lens "
    "(brand-lens.md at the repo root) if they exist. Ground every insight "
    "in those methods and speak their vocabulary. The vault says what was true; only a "
    "pull says what is true — any claim about the current state of the account or market "
    "comes from a fresh Parker MCP pull, not from memory of a doc or an old audit. "
    "Close every substantive answer with its "
    "Sources list and check the receipt before sending: a creative or strategic answer "
    "whose sources name no method doc is presumed under-retrieved. Rebuild it, don't ship it. "
    "Use the vault hard and honor the brand hard rules. "
    "And creative deliverables have no casual path: any words a customer will read or hear "
    "— a script, a headline, a hook, ad copy, even a quick one — route through their skill "
    "in .claude/skills/ and ship with both gate receipts (Grounding Review, Voice Review). "
    "An inline answer carrying customer-facing copy without those receipts skipped the "
    "gates; route it through the skill instead."
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
                f"paths are relative to {ROUTING.parent}/):\n"
                + m.group(1).strip()
            )
    except OSError:
        pass
    return FALLBACK_POINTER


def user_profile() -> str:
    """Inject the profile of the person Parker is working with, if one exists.

    The profile grows from usage, so early on there may be none — that's fine,
    inject nothing. When it exists, put the whole thing in front of every turn
    (a reminder to read it gets skipped; the content does not) so the person's
    standing rules and working preferences shape the reply, not just the what.
    """
    matches = sorted(glob.glob("users/*/user-profile.md"))
    if not matches:
        return ""
    try:
        body = Path(matches[0]).read_text(encoding="utf-8").strip()
    except OSError:
        return ""
    if not body:
        return ""
    return (
        "\n\nWho you're working with — honor this on every reply, their standing "
        "rules and preferences govern how you answer, not just what:\n" + body
    )


print(
    json.dumps(
        {
            "hookSpecificOutput": {
                "hookEventName": "UserPromptSubmit",
                "additionalContext": INSTRUCTION + user_profile() + catalog(),
            }
        }
    )
)
