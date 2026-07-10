#!/usr/bin/env python3
"""Re-sync a brand brain's copied executable layer after a parker-system pin bump.

Runs inside a BRAND repo (not the factory), after /update-brain has checked out
the new release tag in the parker-system/ submodule:

    python3 parker-system/scripts/sync-executable-layer.py --from v3 [--dry-run]

It applies /update-brain's "three piles" deterministically, using the submodule's
own git history to answer "did the team touch this file?" — no manifest needed:

  - brand copy matches the OLD tag's version  -> team never touched it: refresh silently
  - brand copy matches the NEW tag's version  -> already current: skip (idempotent)
  - brand copy matches neither                -> team-edited: leave it, list it (theirs wins)
  - file is new in this release               -> add it
  - file existed at the old tag but the brand deleted it -> leave it deleted, list it
  - file removed by the factory               -> never delete; list it

The BUNDLE_MAP below is the machine-readable twin of the copy list in
prompts/onboarding-runner.md (Phase 0 step 5 and the routine-bundle stamp step).
The two must move together: change one, change the other in the same PR.
Migrations must never copy or diff paths this map owns — see migrations/README.md.

Schedule recipes (schedules/*.md) get one normalization: the `- **Status:**` line
that /setup-routines stamps per-account is ignored when comparing, and the brand's
stamped line is preserved when copying, so an armed schedule doesn't read as edited.
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

MOUNT = Path("parker-system")
STATUS_LINE = re.compile(r"^- \*\*Status:\*\*", re.MULTILINE)
SKIP_NAMES = {"__pycache__", ".DS_Store"}


def git(*args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(MOUNT), *args],
        check=True, capture_output=True, text=True,
    ).stdout


def tree(tag: str) -> dict[str, str]:
    """path -> blob hash for every file at the tag."""
    out = git("ls-tree", "-r", tag)
    entries = {}
    for line in out.splitlines():
        meta, path = line.split("\t", 1)
        mode, otype, sha = meta.split()
        if otype == "blob":
            entries[path] = sha
    return entries


def blob(tag: str, path: str) -> bytes:
    raw = subprocess.run(
        ["git", "-C", str(MOUNT), "show", f"{tag}:{path}"],
        check=True, capture_output=True,
    ).stdout
    return raw


def hash_file(path: Path) -> str:
    return subprocess.run(
        ["git", "-C", str(MOUNT), "hash-object", "--", str(path.resolve())],
        check=True, capture_output=True, text=True,
    ).stdout.strip()


def skippable(path: str) -> bool:
    parts = path.split("/")
    return any(p in SKIP_NAMES for p in parts) or path.endswith(".pyc")


def safe_dest(dest: str) -> bool:
    """A destination this script may touch: a relative path confined to the
    brand repo, no symlinked component anywhere in it, and nothing but a
    regular file (or nothing at all) at the end. Anything else — a symlink,
    a directory where a file should be, a path that escapes the repo — is
    treated as team-owned and left alone."""
    p = Path(dest)
    if p.is_absolute() or ".." in p.parts:
        return False
    cur = Path(".")
    for part in p.parts[:-1]:
        cur = cur / part
        if cur.is_symlink():
            return False
    if p.is_symlink():
        return False
    if p.exists() and not p.is_file():
        return False
    return True


def bundle_map(factory: dict[str, str]) -> dict[str, str]:
    """factory source path -> brand destination path, for one tag's tree.

    Mirrors onboarding-runner Phase 0 step 5: craft skills and review-gate agents
    from the factory's .claude/, the routine bundle from templates/brand-routines/
    (claude/ -> .claude/, schedules/ -> schedules/), and the two checker scripts.
    On a skill name collision the routine bundle wins (the `dream` rule).
    """
    routine_prefix = "templates/brand-routines/claude/"
    schedule_prefix = "templates/brand-routines/schedules/"
    routine_skills = {
        p[len(routine_prefix) + len("skills/"):].split("/", 1)[0]
        for p in factory
        if p.startswith(routine_prefix + "skills/")
    }
    mapping: dict[str, str] = {}
    for path in factory:
        if skippable(path):
            continue
        if path.startswith(routine_prefix):
            mapping[path] = ".claude/" + path[len(routine_prefix):]
        elif path.startswith(schedule_prefix):
            mapping[path] = "schedules/" + path[len(schedule_prefix):]
        elif path.startswith(".claude/skills/"):
            name = path[len(".claude/skills/"):].split("/", 1)[0]
            if name not in routine_skills:  # routine bundle wins the name
                mapping[path] = path
        elif path.startswith(".claude/agents/"):
            mapping[path] = path
        elif path in ("scripts/voice-lint.py", "scripts/grounding-check.py"):
            mapping[path] = path
    return mapping


def is_schedule(dest: str) -> bool:
    return dest.startswith("schedules/") and dest.endswith(".md")


def normalized(text: bytes) -> bytes:
    """Schedule-recipe comparison form: drop the per-account Status line."""
    lines = [l for l in text.decode("utf-8", "replace").splitlines()
             if not l.startswith("- **Status:**")]
    return "\n".join(lines).encode()


def merge_status(new_text: bytes, brand_text: bytes) -> bytes:
    """New factory recipe, carrying the brand's stamped Status line if it has one."""
    brand_status = [l for l in brand_text.decode("utf-8", "replace").splitlines()
                    if l.startswith("- **Status:**")]
    if not brand_status:
        return new_text
    out = []
    replaced = False
    for l in new_text.decode("utf-8", "replace").splitlines():
        if l.startswith("- **Status:**") and not replaced:
            out.append(brand_status[0])
            replaced = True
        else:
            out.append(l)
    if not replaced:
        out.append(brand_status[0])
    text = "\n".join(out)
    if not text.endswith("\n"):
        text += "\n"
    return text.encode()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--from", dest="old_tag",
                    help="release tag the brain was pinned to before this bump "
                         "(default: parker_brain_version in parker_config.json)")
    ap.add_argument("--to", dest="new_tag", default="HEAD",
                    help="release now checked out in parker-system/ (default: HEAD)")
    ap.add_argument("--dry-run", action="store_true",
                    help="report what would change without writing anything")
    args = ap.parse_args()

    if not (MOUNT / ".git").exists() and not (MOUNT / ".git").is_file():
        print("error: run from the brand repo root — parker-system/ submodule not found",
              file=sys.stderr)
        return 2
    if Path("prompts/onboarding-runner.md").exists() and not Path("parker_config.json").exists():
        print("error: this looks like the factory repo, not a brand brain — refusing to sync",
              file=sys.stderr)
        return 2

    old_tag = args.old_tag
    if not old_tag:
        try:
            old_tag = json.loads(Path("parker_config.json").read_text())["parker_brain_version"]
        except (OSError, KeyError, json.JSONDecodeError):
            print("error: pass --from <old-tag>; could not read parker_brain_version "
                  "from parker_config.json", file=sys.stderr)
            return 2

    old = tree(old_tag)
    new = tree(args.new_tag)
    old_map = bundle_map(old)
    new_map = bundle_map(new)

    updated, added, edited, deleted_by_team, removed, current = [], [], [], [], [], []
    writes: list[tuple[Path, bytes]] = []

    # destination -> source view of each tag
    old_by_dest = {d: s for s, d in old_map.items()}
    new_by_dest = {d: s for s, d in new_map.items()}

    for dest, src in sorted(new_by_dest.items()):
        dest_path = Path(dest)
        old_src = old_by_dest.get(dest)
        if not safe_dest(dest):
            edited.append(dest)  # symlink / dir / escaping path: theirs, never touch it
            continue
        if not dest_path.exists():
            if old_src:
                deleted_by_team.append(dest)   # was shipped before; deleted is a decision
            else:
                added.append(dest)             # genuinely new in this release
                writes.append((dest_path, blob(args.new_tag, src)))
            continue
        b = hash_file(dest_path)
        n = new[src]
        o = old.get(old_src) if old_src else None
        if b == n:
            current.append(dest)
            continue
        if is_schedule(dest):
            brand_text = dest_path.read_bytes()
            old_text = blob(old_tag, old_src) if old_src else None
            new_text = blob(args.new_tag, src)
            if normalized(brand_text) == normalized(new_text):
                current.append(dest)
            elif old_text is not None and normalized(brand_text) == normalized(old_text):
                updated.append(dest)
                writes.append((dest_path, merge_status(new_text, brand_text)))
            else:
                edited.append(dest)
            continue
        if o is not None and b == o:
            updated.append(dest)
            writes.append((dest_path, blob(args.new_tag, src)))
        else:
            edited.append(dest)

    for dest, src in sorted(old_by_dest.items()):
        if dest in new_by_dest or not Path(dest).exists():
            continue
        removed.append(dest)  # factory dropped it; never delete, just say so

    if not args.dry_run:
        root = Path.cwd().resolve()
        for path, content in writes:
            # belt and braces: re-verify confinement at write time
            if not safe_dest(str(path)) or not (root / path).resolve().is_relative_to(root):
                edited.append(str(path))
                if str(path) in updated:
                    updated.remove(str(path))
                if str(path) in added:
                    added.remove(str(path))
                continue
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
            if path.suffix == ".py" or path.parts[0] == "scripts":
                path.chmod(path.stat().st_mode | 0o755)

    refreshed_label = "would refresh" if args.dry_run else "refreshed"
    added_label = "would add" if args.dry_run else "added"
    print(f"sync-executable-layer {old_tag} -> {args.new_tag}"
          f"{' (dry run)' if args.dry_run else ''}")
    print(f"  {refreshed_label}: {len(updated)}   {added_label}: {len(added)}"
          f"   already current: {len(current)}")
    for label, paths in ((added_label, added), (refreshed_label, updated)):
        for p in paths:
            print(f"    {label}: {p}")
    if edited:
        print(f"  left alone — the team changed these, theirs wins ({len(edited)}):")
        for p in edited:
            print(f"    {p}")
    if deleted_by_team:
        print(f"  left deleted — shipped before, the team removed them ({len(deleted_by_team)}):")
        for p in deleted_by_team:
            print(f"    {p}")
    if removed:
        print(f"  removed in the factory, kept here ({len(removed)}):")
        for p in removed:
            print(f"    {p}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
