#!/usr/bin/env python3
"""voice-lint: deterministic scan for mechanical AI-writing tells in creative copy.

The mechanical layer of the two-layer check defined in
global/knowledge/creative-strategy/ai-writing-tells.md (shipped to brand
brains as creative-strategy-context/ai-writing-tells.md). Sign inventory
generalized from Wikipedia: Signs of AI writing, retrieved 2026-07-03.

Scope: creative deliverables only — scripts, headlines, hooks, overlay and
static copy, ad-prompt spoken lines, iteration copy. Never run it against
context docs, prompts, or system docs.

This layer is deterministic on purpose: it cannot be talked out of a flag.
A judgment pass (the creative-voice-review agent) decides which flags are
real — customer verbatims are exempt, the brand's corpus outranks the list,
one hit is noise and clustering is signal.

Usage:
    python3 voice-lint.py DRAFT_FILE
    cat draft.txt | python3 voice-lint.py -

Exit code 0 = clean at the mechanical layer, 1 = flags found.
"""
import re
import sys

# ---- AI vocabulary tiers (density matters, not one hit) ----
# Families: importance-inflators, texture words, transformation verbs,
# brochure adjectives. Update here first when the tier list drifts;
# ai-writing-tells.md points at this list as the maintained copy.

FLAGGED_WORDS = {
    # importance-inflators
    "pivotal", "crucial", "testament", "vital", "paramount", "indelible",
    # texture words
    "vibrant", "meticulous", "meticulously", "intricate", "intricacies",
    "seamless", "seamlessly", "robust", "holistic", "tapestry", "interplay",
    "nuanced", "multifaceted",
    # transformation verbs
    "elevate", "elevates", "elevating", "unlock", "unlocks", "unlocking",
    "empower", "empowers", "empowering", "transformative", "revolutionize",
    "revolutionary", "streamline", "supercharge", "harness", "unleash",
    # brochure adjectives and verbs
    "renowned", "unparalleled", "groundbreaking", "boasts", "boasting",
    "nestled", "enduring", "effortlessly", "curated", "bespoke",
    "delve", "delves", "foster", "fosters", "fostering", "garner",
    "garnered", "bolster", "bolstered", "underscore", "underscores",
    "underscoring", "showcase", "showcases", "showcasing", "synergy",
    "landscape", "realm", "game-changer", "game-changing",
}

# ---- Pattern families (name, regex, note) ----

PATTERNS = [
    ("negative parallelism", re.compile(
        r"(\b(it|this|that|these|those|they)('?s|'?re| is| are| was| were)?"
        r"\s*n[o']t\s+(just|only|merely|simply)\b"
        r"|\bnot\s+only\b.{3,80}\bbut(\s+also)?\b"
        r"|\bmore\s+than\s+just\s+a?\b"
        r"|\bno\s+\w+[,.]\s*no\s+\w+[,.]\s*just\b"
        r"|\bisn'?t\s+(just|only|merely)\b|\baren'?t\s+(just|only|merely)\b"
        r"|\bwasn'?t\s+(just|only|merely)\b)", re.I),
     "the 'not just X, it's Y' frame — signature AI construction"),
    ("inflated significance", re.compile(
        r"\b(stands?\s+as|serves?\s+as|is\s+a\s+testament|"
        r"plays?\s+a\s+(vital|crucial|key|pivotal|significant)\s+(role|part)|"
        r"marks?\s+a\s+(shift|turning\s+point|new)|key\s+turning\s+point|"
        r"(ever-)?evolving\s+landscape|indelible\s+mark|deeply\s+rooted|"
        r"represents?\s+a\s+breakthrough|setting\s+the\s+stage|"
        r"a\s+whole\s+new\s+(way|level))\b", re.I),
     "importance-inflation instead of a plain claim"),
    ("participle tail", re.compile(
        r",\s+(highlighting|underscoring|emphasizing|ensuring|reflecting|"
        r"symbolizing|showcasing|demonstrating|solidifying|cementing|"
        r"reinforcing|elevating|fostering|contributing|signaling|"
        r"cultivating|embodying)\b", re.I),
     "sentence trailing into an unattributed '-ing' synthesis"),
    ("vague attribution", re.compile(
        r"\b(experts?\s+(say|agree|argue|recommend)|studies\s+show|"
        r"research\s+(shows|suggests)|industry\s+(reports?|insiders)|"
        r"observers\s+(have\s+)?not(e|ed)|many\s+(believe|agree)|"
        r"customers\s+rave|scientists\s+(say|agree)|doctors\s+agree)\b",
        re.I),
     "weasel attribution with no named source — also a compliance risk"),
    ("puffery register", re.compile(
        r"\b(commitment\s+to\s+(excellence|quality)|rich\s+heritage|"
        r"in\s+the\s+heart\s+of|natural\s+beauty|diverse\s+array|"
        r"wide\s+(range|variety)\s+of|premium\s+(experience|feel|quality)|"
        r"luxuriously|expertly[- ]crafted|thoughtfully\s+designed|"
        r"crafted\s+with\s+(care|precision)|attention\s+to\s+detail)\b",
        re.I),
     "brochure register no human says out loud"),
    ("signposted transition", re.compile(
        r"\b(but\s+here'?s\s+the\s+(thing|kicker|catch|best\s+part)|"
        r"here'?s\s+why(\s+it\s+works)?[:.]|that'?s\s+where\s+\w+"
        r"(\s+\w+)?\s+comes?\s+in|enter\s+[A-Z]\w+|look\s+no\s+further|"
        r"the\s+best\s+part\??|say\s+goodbye\s+to|say\s+hello\s+to|"
        r"the\s+secret\s+to|the\s+result\??|gone\s+are\s+the\s+days)\b",
        re.I),
     "formulaic bridge — real speech cuts, it doesn't signpost"),
    ("pristine CTA", re.compile(
        r"\b(don'?t\s+wait|order\s+yours?\s+today|shop\s+now\s+and|"
        r"experience\s+the\s+difference|what\s+are\s+you\s+waiting\s+for|"
        r"treat\s+yourself|you\s+(deserve|owe\s+it\s+to\s+yourself)|"
        r"join\s+(the\s+)?thousands|elevate\s+your)\b", re.I),
     "command-close ad-speak CTA — close like a friend instead"),
    ("copula avoidance", re.compile(
        r"\b(features?\s+an?\s+|offers?\s+an?\s+(range|variety|selection|"
        r"array)|provides?\s+an?\s+(range|variety|seamless|unmatched)|"
        r"delivers?\s+(unmatched|unparalleled|exceptional))", re.I),
     "'features/offers/delivers a' where 'is/has' belongs"),
    ("rhetorical self-question", re.compile(
        r"(\b(sound\s+familiar|crazy,?\s+right|guess\s+what|"
        r"you\s+know\s+what('?s)?\s+(crazy|wild|funny)|"
        r"want\s+to\s+know\s+the\s+(best|craziest)|"
        r"and\s+the\s+craziest\s+part)\s*\?"
        r"|\b(honestly|seriously|the\s+truth|real\s+talk)\s*\?)", re.I),
     "a question the speaker isn't actually asking — humans don't "
     "interview themselves; allowed only as a deliberate question hook "
     "in the opener"),
    ("throat-clearing", re.compile(
        r"\b(in\s+today'?s\s+(fast-paced|busy|modern|digital)|"
        r"when\s+it\s+comes\s+to|in\s+a\s+world\s+(where|of)|"
        r"we\s+all\s+know\s+(that|the\s+feeling)|let'?s\s+face\s+it|"
        r"picture\s+this[:.])", re.I),
     "opener spent on nothing — the first line is the expensive one"),
    ("audience enumeration", re.compile(
        r"\bwhether\s+you'?re\s+(a\s+)?\w+([\s\w]*)\s+or\s+(a\s+)?\w+",
        re.I),
     "'whether you're X or Y' — names everyone, lands with no one"),
]


def check_line(line):
    flags = []
    low = line.lower()
    words = re.findall(r"[a-z'-]+", low)
    hits = sorted({w for w in words if w in FLAGGED_WORDS})
    if hits:
        flags.append(("AI vocabulary", ", ".join(hits),
                      "flagged-word hit — judge density, not one hit"))
    for name, rx, note in PATTERNS:
        m = rx.search(line)
        if m:
            flags.append((name, m.group(0).strip(), note))
    # em-dash cadence: two or more dash breaks in one line
    if line.count("—") + line.count(" - ") + line.count(" – ") >= 2:
        flags.append(("em-dash cadence", "—…—",
                      "stacked dramatic clauses on dashes"))
    # balanced triplet: "X, Y, and Z" of short, matching-weight items
    trip = re.search(r"\b([\w-]+),\s+([\w-]+),\s+and\s+([\w-]+)\b", line)
    if trip and all(len(g) <= 13 for g in trip.groups()) \
            and len({g.lower() for g in trip.groups()}) == 3:
        flags.append(("balanced triplet", trip.group(0),
                      "smooth rule-of-three — repeat a word or break the "
                      "balance if the list is real"))
    # curly/straight quote mix within one piece of copy
    if ("“" in line or "‘" in line) and ('"' in line or "'" in line):
        flags.append(("curly-quote mix", "mixed quote styles", "pick one"))
    return flags


def main(argv):
    if len(argv) != 2:
        print(__doc__.strip().splitlines()[0])
        print("usage: voice-lint.py DRAFT_FILE  (or '-' for stdin)")
        return 2
    if argv[1] == "-":
        text = sys.stdin.read()
    else:
        with open(argv[1], encoding="utf-8") as f:
            text = f.read()
    total, report = 0, []
    lines = text.splitlines()
    for i, line in enumerate(lines, 1):
        if not line.strip():
            continue
        for name, evidence, note in check_line(line):
            total += 1
            report.append(f'  L{i} [{name}] "{evidence}" — {note}')
    n_lines = max(1, sum(1 for l in lines if l.strip()))
    print(f"voice-lint: {total} flag(s) across {n_lines} non-empty lines "
          f"(density {total / n_lines:.2f})")
    for r in report:
        print(r)
    if total == 0:
        print("  clean at the mechanical layer — the judgment pass "
              "still applies")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
