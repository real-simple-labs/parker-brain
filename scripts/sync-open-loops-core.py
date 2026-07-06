#!/usr/bin/env python3
"""sync-open-loops-core.py — keep the marker-delimited shared blocks in step.

A handful of blocks live in exactly one source file and are embedded verbatim in
many other files. This script copies each source's canonical text into every
target that carries the matching marker pair, so a fix to the source lands
everywhere at once. The registry of what syncs where is system/system-of-records.md.

Four blocks are synced:

  - open-loops-core  <- prompts/_open-loops-core-block.md
        embedded in every context-doc-generating prompt
  - expertise-core   <- prompts/_expertise-core-block.md
        embedded in the same prompts
  - parker-voice     <- prompts/_parker-voice-block.md
        embedded in the brand-brain CLAUDE.md files (here: the template)
  - brand-intake     <- prompts/_brand-intake-context-block.md
        embedded in a targeted subset of generating prompts (audits, account
        reads, strategy inputs, brief creation, personas, competitor syntheses)

How a block is delimited:
  - In the SOURCE file, the canonical text sits between `<!-- BLOCK-START -->`
    and `<!-- BLOCK-END -->` (marker lines excluded).
  - In each TARGET file, it sits between `<!-- NAME:start ... -->` and
    `<!-- NAME:end -->`. The start marker keeps its descriptive suffix; only the
    text between the markers is replaced. The result is byte-identical to the
    source.

The source is always anchored to THIS repo (the factory canon). What changes is
where targets are looked for: by default the script's own repo, but `--scan` can
point it at another tree — e.g. a brand brain whose root CLAUDE.md carries the
parker-voice markers. propagate-to-brand-brains.sh uses this to refresh each
brain's CLAUDE.md from the factory source after it mirrors the bundle.

Usage:
    scripts/sync-open-loops-core.py                     # write: sources -> targets in this repo
    scripts/sync-open-loops-core.py --check             # report drift in this repo, write nothing, exit 1 if any
    scripts/sync-open-loops-core.py --scan PATH         # write: factory sources -> targets found under PATH
    scripts/sync-open-loops-core.py --check --scan PATH # report drift under PATH

`--scan` is repeatable. Targets are discovered by scanning for the marker pair,
so a new embed is picked up automatically once it carries the markers.
"""

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# block name (== marker name) -> source file, relative to repo root
BLOCKS = {
    "open-loops-core": "prompts/_open-loops-core-block.md",
    "expertise-core": "prompts/_expertise-core-block.md",
    "parker-voice": "prompts/_parker-voice-block.md",
    "brand-intake": "prompts/_brand-intake-context-block.md",
    "team-conversations": "prompts/_team-conversations-source-block.md",
}

SOURCE_RE = re.compile(r"<!-- BLOCK-START -->\n(.*?)\n<!-- BLOCK-END -->", re.DOTALL)


def read_source_payload(source_path: Path) -> str:
    """Return the canonical text between BLOCK-START and BLOCK-END (markers excluded)."""
    text = source_path.read_text(encoding="utf-8")
    m = SOURCE_RE.search(text)
    if not m:
        raise SystemExit(
            f"ERROR: no <!-- BLOCK-START -->/<!-- BLOCK-END --> pair in {source_path}"
        )
    return m.group(1)


def target_re(name: str) -> re.Pattern:
    """Match a target's marker pair. group(1)=start marker line incl. newline,
    group(2)=current inner text, group(3)=newline + end marker line."""
    return re.compile(
        r"(<!-- " + re.escape(name) + r":start\b.*?-->\n)"
        r"(.*?)"
        r"(\n<!-- " + re.escape(name) + r":end -->)",
        re.DOTALL,
    )


def discover_targets(name: str, scan_roots: list[Path]) -> list[Path]:
    """Every .md file under the scan roots that carries this block's start marker.
    The factory source file itself is never a target (it uses BLOCK markers)."""
    needle = f"<!-- {name}:start"
    source = REPO / BLOCKS[name]
    found = []
    seen = set()
    for root in scan_roots:
        for path in sorted(root.rglob("*.md")):
            if ".git" in path.parts or path == source or path in seen:
                continue
            try:
                if needle in path.read_text(encoding="utf-8"):
                    found.append(path)
                    seen.add(path)
            except (UnicodeDecodeError, OSError):
                continue
    return found


def parse_args(argv: list[str]) -> tuple[bool, list[Path]]:
    check = False
    scan_roots: list[Path] = []
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg == "--check":
            check = True
        elif arg == "--scan":
            i += 1
            if i >= len(argv):
                raise SystemExit("ERROR: --scan needs a directory path")
            root = Path(argv[i]).resolve()
            if not root.is_dir():
                raise SystemExit(f"ERROR: --scan path is not a directory: {root}")
            scan_roots.append(root)
        elif arg.startswith("--scan="):
            root = Path(arg.split("=", 1)[1]).resolve()
            if not root.is_dir():
                raise SystemExit(f"ERROR: --scan path is not a directory: {root}")
            scan_roots.append(root)
        else:
            raise SystemExit(__doc__)
        i += 1
    if not scan_roots:
        scan_roots = [REPO]
    return check, scan_roots


def main() -> int:
    check, scan_roots = parse_args(sys.argv[1:])

    drift = []  # (name, path) pairs out of step
    written = []  # (name, path) pairs updated

    for name, rel in BLOCKS.items():
        payload = read_source_payload(REPO / rel)
        pattern = target_re(name)

        for path in discover_targets(name, scan_roots):
            text = path.read_text(encoding="utf-8")
            if not pattern.search(text):
                # marker present but malformed (missing :end, or out of order)
                raise SystemExit(
                    f"ERROR: {path} has a {name}:start marker but no well-formed "
                    f"{name}:start/{name}:end pair"
                )

            new_text = pattern.sub(
                lambda m: m.group(1) + payload + m.group(3), text
            )
            if new_text == text:
                continue  # already in step

            drift.append((name, path))
            if not check:
                path.write_text(new_text, encoding="utf-8")
                written.append((name, path))

    if check:
        if drift:
            print("DRIFT: the following embeds are out of step with their source:")
            for name, path in drift:
                print(f"  [{name}] {path}")
            print(f"\n{len(drift)} block embed(s) drifted. Run scripts/sync-open-loops-core.py to fix.")
            return 1
        print("Clean: every synced block matches its source.")
        return 0

    if written:
        print("Synced:")
        for name, path in written:
            print(f"  [{name}] {path}")
        print(f"\nUpdated {len(written)} block embed(s).")
    else:
        print("Nothing to do: every synced block already matches its source.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
