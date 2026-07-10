#!/usr/bin/env python3
"""Normalize method-doc paths in a shipped brand brain's .claude/ layer.

The factory's skills and agents reference the craft layer by factory paths
(global/knowledge/creative-strategy/..., system/<runtime-doc>.md). A shipped
brand brain keeps that layer somewhere else — parker-system/creative-strategy-context/
in the current (nested) layout, creative-strategy-context/ at the root in the
legacy flat layout — so a straight copy leaves every skill pointing at docs
that do not exist. This script rewrites the copies so every reference resolves.

Called by prompts/onboarding-runner.md at ship time (Phase 0) and by
scripts/propagate-to-brand-brains.sh on every re-ship. Idempotent.

Usage: normalize-brain-paths.py <brain-dir> <nested|flat>
"""
import sys
from pathlib import Path

# The runtime system docs that ship into a brain (onboarding-runner Phase 0).
# Only these get the system/ -> parker-system/system/ rewrite; anything else
# under system/ is factory-internal and never shipped.
RUNTIME_SYSTEM_DOCS = [
    "parker-tools.md",
    "three-phase-operating-model.md",
    "open-loops-system.md",
    "refresh-cadence.md",
    "schedules.md",
    "growing-the-brain.md",
]

P_CSC = "\x00PSC\x00"   # placeholder: parker-system/creative-strategy-context/
P_SYS = "\x00PSY\x00"   # placeholder: parker-system/system/


def rewrite(text: str, layout: str) -> str:
    # Protect already-correct nested paths so no rule double-fires.
    text = text.replace("parker-system/creative-strategy-context/", P_CSC)
    text = text.replace("parker-system/system/", P_SYS)

    if layout == "nested":
        text = text.replace("global/knowledge/creative-strategy/", P_CSC)
        text = text.replace("creative-strategy-context/", P_CSC)
        for doc in RUNTIME_SYSTEM_DOCS:
            text = text.replace(f"system/{doc}", f"{P_SYS}{doc}")
        text = text.replace(P_CSC, "parker-system/creative-strategy-context/")
        text = text.replace(P_SYS, "parker-system/system/")
    elif layout == "flat":
        text = text.replace("global/knowledge/creative-strategy/", "creative-strategy-context/")
        text = text.replace(P_CSC, "creative-strategy-context/")
        text = text.replace(P_SYS, "system/")
    else:
        raise SystemExit(f"unknown layout: {layout!r} (want nested|flat)")
    return text


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit(__doc__.strip().splitlines()[-1])
    brain, layout = Path(sys.argv[1]), sys.argv[2]
    if not brain.is_dir():
        raise SystemExit(f"not a directory: {brain}")

    changed = 0
    for sub in (".claude/skills", ".claude/agents"):
        root = brain / sub
        if not root.is_dir():
            continue
        for f in sorted(root.rglob("*.md")):
            original = f.read_text(encoding="utf-8")
            updated = rewrite(original, layout)
            if updated != original:
                f.write_text(updated, encoding="utf-8")
                changed += 1
                print(f"  normalized: {f.relative_to(brain)}")
    print(f"normalize-brain-paths: {changed} file(s) rewritten ({layout} layout)")


if __name__ == "__main__":
    main()
