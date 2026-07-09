#!/usr/bin/env python3
"""verify-brain.py — the one Phase-0 harness verification for a brand brain.

Run from the brain's root (or pass the path). Checks that everything the brain
needs to actually run — skills, reviewer agents, checkers, hooks, settings,
craft docs, path resolution, git tracking — exists and executes. Every line
prints PASS or FAIL; any FAIL exits non-zero, and a build with a FAIL is not
done. The onboarding runner runs this as the final act of Phase 0, get-started
runs it during the tour, and anyone can run it any time:

    python3 scripts/verify-brain.py [brain-root]
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()

ROUTINE_SKILLS = [
    "dream", "self-improve", "research-loops", "update-brain", "harvest-ideas",
    "evaluate-ideas", "refresh-context", "setup-routines", "get-started",
]
CRAFT_SKILLS = [
    "scriptwriting", "hooks", "headlines", "iterations", "ai-ad-generation",
    "ad-account-analysis", "brand-idea-bank-maintenance",
    "open-loops-advance", "open-loops-validate",
    "improve-system", "self-improvement-intake", "expert-signal-intake",
]
AGENTS = ["creative-voice-review.md", "context-grounding-review.md"]
SCRIPTS = ["voice-lint.py", "grounding-check.py", "normalize-brain-paths.py"]
CRAFT_DOCS = ["expertise-routing.md", "ai-writing-tells.md", "spoken-script-voice.md"]
HOOK_SCRIPTS = ["craft-context.py", "pull-log.py"]
# Files allowed to mention factory paths (descriptive prose, inert in a brain).
STALE_PATH_ALLOW = {".claude/skills/propagate-craft/SKILL.md"}

failures = 0


def report(ok: bool, label: str, detail: str = "") -> None:
    global failures
    mark = "PASS" if ok else "FAIL"
    if not ok:
        failures += 1
    print(f"  {mark}  {label}" + (f" — {detail}" if detail else ""))


def main() -> int:
    print(f"verify-brain: {ROOT}")

    print("\n[1] Skills registered where Claude Code loads them (.claude/skills/<name>/SKILL.md)")
    for name in ROUTINE_SKILLS + CRAFT_SKILLS:
        f = ROOT / ".claude/skills" / name / "SKILL.md"
        report(f.is_file(), f"skill: {name}", "" if f.is_file() else f"missing {f.relative_to(ROOT)}")

    print("\n[2] Reviewer agents (the ship gates)")
    for a in AGENTS:
        f = ROOT / ".claude/agents" / a
        report(f.is_file(), f"agent: {a}")

    print("\n[3] Checkers exist and execute")
    for s in SCRIPTS:
        f = ROOT / "scripts" / s
        report(f.is_file(), f"script: {s}")
    lint = ROOT / "scripts/voice-lint.py"
    if lint.is_file():
        r = subprocess.run(
            [sys.executable, str(lint), "-"],
            input="This isn't just a check — it's a revolution. Sound familiar?",
            capture_output=True, text=True,
        )
        caught = r.returncode == 1 and "flag" in (r.stdout + r.stderr)
        report(caught, "voice-lint fires on a known slop line",
               "" if caught else f"exit {r.returncode}: {(r.stdout or r.stderr)[:80]}")
    gc = ROOT / "scripts/grounding-check.py"
    if gc.is_file():
        r = subprocess.run([sys.executable, str(gc)], capture_output=True, text=True)
        usable = "usage" in (r.stdout + r.stderr).lower() or r.returncode in (1, 2)
        report(usable, "grounding-check executes (prints usage with no args)")

    print("\n[4] Hooks and settings")
    settings = ROOT / ".claude/settings.json"
    cfg = None
    if settings.is_file():
        try:
            cfg = json.loads(settings.read_text())
        except json.JSONDecodeError as e:
            report(False, "settings.json parses", str(e))
    report(cfg is not None, "settings.json present and valid JSON")
    if cfg is not None:
        hooks = cfg.get("hooks", {})
        report("UserPromptSubmit" in hooks, "UserPromptSubmit hook configured (craft-catalog injection)")
        report("PostToolUse" in hooks, "PostToolUse hook configured (session pull log)")
    for h in HOOK_SCRIPTS:
        f = ROOT / ".claude/hooks" / h
        ok = f.is_file()
        if ok:
            ok = subprocess.run([sys.executable, "-m", "py_compile", str(f)],
                                capture_output=True).returncode == 0
        report(ok, f"hook script: {h}" + ("" if ok else " (missing or does not compile)"))

    print("\n[5] Craft knowledge layer")
    craft = None
    for cand in ("parker-system/creative-strategy-context", "creative-strategy-context"):
        if (ROOT / cand).is_dir():
            craft = ROOT / cand
            break
    report(craft is not None, "craft layer directory found",
           str(craft.relative_to(ROOT)) if craft else "neither parker-system/creative-strategy-context nor creative-strategy-context exists")
    if craft:
        for d in CRAFT_DOCS:
            report((craft / d).is_file(), f"craft doc: {d}")

    print("\n[6] Path resolution in .claude/ (no factory paths)")
    stale = []
    for f in (ROOT / ".claude").rglob("*.md"):
        rel = str(f.relative_to(ROOT))
        if rel in STALE_PATH_ALLOW:
            continue
        if "global/knowledge/creative-strategy" in f.read_text(encoding="utf-8", errors="replace"):
            stale.append(rel)
    report(not stale, "no unresolvable factory paths in skills/agents",
           "; ".join(stale[:5]) if stale else "")

    print("\n[7] Git actually carries .claude/ (catches .gitignore and dotfile misses)")
    r = subprocess.run(["git", "-C", str(ROOT), "ls-files", ".claude/"],
                       capture_output=True, text=True)
    if r.returncode == 0:
        n = len([l for l in r.stdout.splitlines() if l.strip()])
        report(n >= 20, f".claude/ tracked in git ({n} files)",
               "" if n >= 20 else "tracked count suspiciously low — check .gitignore and how the copy was made")
    else:
        report(True, "not a git repo here — skipping tracking check (verify after the initial push)")

    print()
    if failures:
        print(f"RESULT: FAIL — {failures} check(s) failed. The build is not done; fix and re-run.")
        return 1
    print("RESULT: PASS — the harness is fully scaffolded.")
    print("One thing no script can check: workspace trust. On first open, Claude Code asks")
    print("whether to trust this folder — the answer must be yes, or none of this activates.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
