#!/usr/bin/env python3
"""Generate the creative-strategy doc catalog from each doc's `summary` frontmatter.

The catalog is descriptive, never prescriptive: it lists every method doc and an
honest 'what's in it', and that's all. It does NOT precompute relevance — no
families, no triggers, no related graph — because relevance is the planner's job.
The planner reads this catalog, reasons like a strategist over the whole set
(generously), and greps the doc bodies for anything a one-liner didn't surface.

Run after adding or editing a knowledge doc:

    python3 scripts/build-doc-map.py
"""
import os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB = os.path.join(ROOT, "global/knowledge/creative-strategy")
CATALOG_DOC = os.path.join(KB, "expertise-routing.md")

# Not method docs — never indexed.
EXCLUDE = {"expertise-routing.md", "meeting-2026-05-19-v2-architecture.md",
           "brand-brain-CLAUDE-template.md"}


def get_summary(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if not text.startswith("---\n"):
        return None
    end = text.index("\n---", 4)
    for ln in text[4:end].splitlines():
        if ln.split(":", 1)[0].strip() == "summary" and ":" in ln:
            return ln.split(":", 1)[1].strip().strip('"').strip("'")
    return None


def main():
    rows = []
    missing = []
    for path in sorted(glob.glob(os.path.join(KB, "*.md"))):
        fn = os.path.basename(path)
        if fn in EXCLUDE:
            continue
        summary = get_summary(path)
        if summary:
            rows.append((fn, summary))
        else:
            missing.append(fn)

    lines = ["| Doc | What it is |", "|---|---|"]
    for fn, summary in rows:
        lines.append(f"| `{fn}` | {summary} |")
    generated = "\n".join(lines) + "\n"

    with open(CATALOG_DOC, encoding="utf-8") as f:
        doc = f.read()
    pattern = re.compile(r"(<!-- DOC-MAP:START -->\n).*?(\n<!-- DOC-MAP:END -->)", re.DOTALL)
    if not pattern.search(doc):
        raise SystemExit("DOC-MAP markers not found in expertise-routing.md")
    doc = pattern.sub(lambda m: m.group(1) + generated + m.group(2), doc)
    with open(CATALOG_DOC, "w", encoding="utf-8") as f:
        f.write(doc)

    print(f"Wrote catalog: {len(rows)} docs.")
    if missing:
        print("WARNING — no summary frontmatter (excluded from catalog):")
        for fn in missing:
            print(f"  {fn}")


if __name__ == "__main__":
    main()
