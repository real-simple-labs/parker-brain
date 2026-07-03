#!/usr/bin/env python3
"""grounding-check: deterministic scan for ungrounded creative/strategy output.

The mechanical layer of the grounding gate. The judgment layer is the
context-grounding-review agent (.claude/agents/context-grounding-review.md),
which runs this first and then decides what the findings mean.

Three checks, all cold:

1. VERBATIM TRACE — every quoted phrase in the output is searched for across
   the brain's markdown. TRACED means it exists in the vault (a real customer
   phrase, a real corpus line). UNTRACED means it appears nowhere on disk —
   either it came from a live tool pull in this session (the reviewer
   verifies that) or it was invented (fabrication). The check cannot tell
   those apart; it exists so no invented quote passes silently as sourced.

2. SOURCE EXISTENCE — every backticked file path the output claims as a
   source must exist on disk, tried against the layout prefixes (factory
   and brand-brain paths). A named source that resolves nowhere is a
   decorative citation.

3. RECEIPT PRESENCE — the output contracts require visible receipts
   (Brand Context Applied, Voice Review, the sign-off stamps). Reports
   which are present and which are absent; the reviewer knows which the
   deliverable type requires.

Usage:
    python3 grounding-check.py OUTPUT_FILE [BRAIN_ROOT]

BRAIN_ROOT defaults to the current directory. Exit 0 = nothing flagged,
1 = findings for the judgment layer.
"""
import hashlib
import json
import os
import re
import sys
import tempfile
import time

RECEIPTS = [
    "Brand Context Applied",
    "Voice Review",
    "This is everything I know about",
    "This is based on everything",
]

# Layout prefixes a cited path may resolve under: factory and brand-brain shapes.
PATH_PREFIXES = [
    "",
    "parker-system/",
    "creative-strategy-context/",
    "parker-system/creative-strategy-context/",
    "global/knowledge/creative-strategy/",
]


def norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def load_vault(root, skip):
    """Read every .md in the brain into one normalized haystack per file."""
    vault = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".git")
                       and d != "node_modules"]
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            p = os.path.join(dirpath, fn)
            if os.path.abspath(p) == skip:
                continue
            try:
                with open(p, encoding="utf-8") as f:
                    vault[os.path.relpath(p, root)] = norm(f.read())
            except OSError:
                pass
    return vault


def main(argv):
    if len(argv) < 2:
        print("usage: grounding-check.py OUTPUT_FILE [BRAIN_ROOT]")
        return 2
    out_path = os.path.abspath(argv[1])
    root = os.path.abspath(argv[2]) if len(argv) > 2 else os.getcwd()
    with open(out_path, encoding="utf-8") as f:
        text = f.read()
    findings = 0
    vault = load_vault(root, out_path)

    # 1. Verbatim trace: quoted phrases of 4+ words.
    quotes = re.findall(r'[""]([^""]{10,300})[""]|"([^"]{10,300})"', text)
    quotes = [a or b for a, b in quotes]
    quotes = [q for q in quotes if len(q.split()) >= 4]
    print(f"verbatim trace: {len(quotes)} quoted phrase(s) of 4+ words")
    for q in quotes:
        nq = norm(q)
        hit = next((path for path, hay in vault.items() if nq in hay), None)
        if hit:
            print(f'  TRACED   "{q[:70]}" -> {hit}')
        else:
            findings += 1
            print(f'  UNTRACED "{q[:70]}" — not in the vault; verify it '
                  f"came from a live pull this session, else it is invented")

    # 2. Source existence: backticked paths.
    cited = set(re.findall(r"`([\w./ -]+\.(?:md|py|json|sh))`", text))
    print(f"source existence: {len(cited)} cited path(s)")
    for c in sorted(cited):
        base = os.path.basename(c)
        resolved = None
        for pre in PATH_PREFIXES:
            for cand in (pre + c, pre + base):
                if os.path.exists(os.path.join(root, cand)):
                    resolved = cand
                    break
            if resolved:
                break
        if resolved:
            print(f"  EXISTS   `{c}`")
        else:
            findings += 1
            print(f"  MISSING  `{c}` — cited but resolves nowhere in this "
                  f"brain; a decorative citation")

    # 3. Session pulls: the hook-written log the model cannot fake.
    # (.claude/hooks/pull-log.py appends every MCP call; entries from the
    # last 24h for this repo are the verifiable pull record.)
    key = hashlib.sha256(root.encode()).hexdigest()[:16]
    plog = os.path.join(tempfile.gettempdir(), f"parker-pull-log-{key}.jsonl")
    pulls = []
    if os.path.exists(plog):
        cutoff = time.time() - 86400
        try:
            with open(plog, encoding="utf-8") as f:
                for line in f:
                    try:
                        e = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if e.get("ts", 0) >= cutoff:
                        pulls.append(e)
        except OSError:
            pass
        print(f"session pulls (hook-logged, last 24h): {len(pulls)}")
        for e in pulls[-40:]:
            hint = ""
            if e.get("input"):
                hint = " " + json.dumps(e["input"], ensure_ascii=False)[:100]
            print(f"  {time.strftime('%H:%M', time.localtime(e['ts']))} "
                  f"{e['tool']}{hint}")
    else:
        print("session pulls: no hook log found — the pull-log hook is not "
              "installed or no MCP call has run; pull claims are unverified")

    # 4. Receipt presence.
    print("receipts:")
    for r in RECEIPTS:
        mark = "present" if r.lower() in text.lower() else "ABSENT"
        print(f"  {mark:8} {r}")
    # Absence is reported, not counted — the reviewer knows which receipts
    # this deliverable type requires.

    print(f"grounding-check: {findings} finding(s) for the judgment layer")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
