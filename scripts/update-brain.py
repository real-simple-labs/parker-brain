#!/usr/bin/env python3
"""Plan and record a brand brain's automatic update, deterministically.

Runs inside a BRAND repo (not the factory), from its root, through the mount:

    python3 parker-system/scripts/update-brain.py plan
    python3 parker-system/scripts/update-brain.py record-migration v41
    python3 parker-system/scripts/update-brain.py record-pin v42
    python3 parker-system/scripts/update-brain.py auto-update off

/update-brain (the routine skill) calls it. It never moves the pin, runs a
migration, or copies a file: the skill does those. It answers one question,
"what may this brain take on its own right now?", and it keeps the ledger
(running-notes/standard-sync.md) honest while the skill works:

  plan              Reads the ledger, the mount, and the factory's release tags
                    (fetch them first: git -C parker-system fetch origin --prune
                    --prune-tags) and prints one JSON object: what an earlier
                    update left unfinished, and the newest release this brain
                    may move to with nobody asked (auto_target), or why not.
  record-migration  Moves "Migrations applied through" to vN, and only when vN
                    is the next migration after the one recorded and the mount
                    has reached it. No migration is ever skipped.
  record-pin        Moves "Pinned release" (and parker_brain_version in
                    parker_config.json) to vN, and only when the mount is
                    checked out at vN.
  auto-update       Turns automatic updates on or off in the ledger.

Which migrations may run with nobody asked: a migration is safe for an
automatic update when it says so on its own line, `**Auto-apply:** yes`, or
when it is the one-line no-op ("Nothing to do; ..."). `**Auto-apply:** no`
always wins. A migration with real steps and no marker needs a person: the
automatic update stops at the release before it, and the skill offers the
rest. migrations/README.md has the contract.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

MOUNT = Path("parker-system")
LEDGER = Path("running-notes/standard-sync.md")
CONFIG = Path("parker_config.json")
RELEASE = re.compile(r"\bv(\d+)\b")
MARKER = re.compile(r"^\s*\**\s*Auto-apply:\s*\**\s*(yes|no)\b", re.IGNORECASE | re.MULTILINE)
NO_OP = re.compile(r"^\**\s*Nothing to do\b", re.IGNORECASE | re.MULTILINE)
STEPS = re.compile(r"^(?:#{2,} |\d+\. )", re.MULTILINE)


class Refusal(Exception):
    """A request the ledger rules don't allow. Nothing was written."""


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(MOUNT), *args],
                          check=check, capture_output=True, text=True)


def number(tag: str | None) -> int | None:
    m = RELEASE.search(tag or "")
    return int(m.group(1)) if m else None


def tag(n: int | None) -> str | None:
    return None if n is None else f"v{n}"


# --- the ledger ------------------------------------------------------------

def field_pattern(name: str) -> re.Pattern:
    return re.compile(rf"^(\s*[-*]\s*\*\*{re.escape(name)}:\*\*)([^\n]*)$",
                      re.IGNORECASE | re.MULTILINE)


def field(text: str, name: str) -> str | None:
    m = field_pattern(name).search(text)
    return m.group(2).strip() if m else None


def set_release(text: str, name: str, version: str) -> str:
    """Point the field's release at `version`, keeping the rest of its line."""
    pat = field_pattern(name)
    m = pat.search(text)
    if not m:
        raise Refusal(f"the ledger has no **{name}:** line")
    value = m.group(2)
    new_value = RELEASE.sub(version, value, count=1) if RELEASE.search(value) else f" {version}"
    return text[:m.start(2)] + new_value + text[m.end(2):]


def posture(text: str) -> str | None:
    value = (field(text, "Posture") or "").lower()
    for name in ("own-factory", "independent", "follow"):
        if name in value:
            return name
    return None


def auto_update(text: str) -> bool:
    """On unless the ledger turns it off. A ledger from before v40 has no
    line, and taking v40 is the team's yes to automatic updates."""
    value = (field(text, "Auto-update") or "").lower()
    return not re.search(r"\boff\b", value)


def write_atomically(path: Path, content: str) -> None:
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as out:
            out.write(content)
        os.replace(tmp, path)
    except BaseException:
        Path(tmp).unlink(missing_ok=True)
        raise


def read_ledger() -> str:
    try:
        return LEDGER.read_text(encoding="utf-8")
    except OSError:
        raise Refusal(f"{LEDGER} is missing or unreadable")


# --- the mount -------------------------------------------------------------

def releases() -> list[int]:
    out = git("tag", "--list", "v*").stdout.split()
    return sorted({int(t[1:]) for t in out if re.fullmatch(r"v\d+", t)})


def mount_release() -> int | None:
    """The highest release tag on the commit the mount is checked out at."""
    out = git("tag", "--points-at", "HEAD", "--list", "v*", check=False).stdout.split()
    found = [int(t[1:]) for t in out if re.fullmatch(r"v\d+", t)]
    return max(found) if found else None


def migration(n: int, at: str) -> str | None:
    shown = git("show", f"{at}:migrations/v{n}.md", check=False)
    return shown.stdout if shown.returncode == 0 else None


def auto_apply(text: str) -> bool:
    marker = MARKER.search(text)
    if marker:
        return marker.group(1).lower() == "yes"
    return bool(NO_OP.search(text)) and not STEPS.search(text)


def first_line(text: str) -> str:
    for line in text.splitlines():
        if line.strip():
            return line.lstrip("# ").strip()
    return ""


# --- plan ------------------------------------------------------------------

def plan() -> dict:
    result: dict = {
        "mode": None, "auto_update": None, "pinned": None, "applied_through": None,
        "mount_at": None, "newest": None,
        "unfinished_migrations": [], "resume_sync_from": None,
        "auto_target": None, "offer_target": None, "stopped_at": None,
        "why_not_auto": [],
    }
    why = result["why_not_auto"]
    text = read_ledger()
    result["mode"] = mode = posture(text)
    result["auto_update"] = auto_update(text)
    if mode != "follow":
        why.append("the brain is decoupled from the factory: updates are offers, never automatic"
                   if mode else "the ledger names no posture")
        return result
    if not (MOUNT / ".git").exists():
        why.append("parker-system/ is not a mounted submodule")
        return result

    pinned = number(field(text, "Pinned release"))
    applied = number(field(text, "Migrations applied through"))
    at = mount_release()
    tags = releases()
    newest = tags[-1] if tags else None
    result.update(pinned=tag(pinned), applied_through=tag(applied),
                  mount_at=tag(at), newest=tag(newest))
    if pinned is None or applied is None:
        why.append("the ledger has no readable Pinned release or Migrations applied through")
        return result
    if newest is None:
        why.append("no release tags in the mount: fetch them first")
        return result
    if at is None:
        why.append("parker-system/ is not checked out at a release tag")
        return result
    if at < pinned:
        why.append(f"parker-system/ is at {tag(at)}, behind the recorded {tag(pinned)}: "
                   "a person needs to look")
        return result
    if at > pinned:
        # The pin moved but the update stopped before recording it. The sync
        # is idempotent: run it again from the recorded pin, then record.
        result["resume_sync_from"] = tag(pinned)
        why.append(f"an earlier update moved parker-system/ to {tag(at)} but didn't finish")

    # Migrations an earlier update left, oldest first, read at the mount.
    for n in range(applied + 1, at + 1):
        body = migration(n, "HEAD")
        if body is None:
            if n in tags:
                result["unfinished_migrations"].append(
                    {"release": tag(n), "auto_apply": False, "missing": True})
            continue
        result["unfinished_migrations"].append(
            {"release": tag(n), "auto_apply": auto_apply(body), "title": first_line(body)})
    if result["unfinished_migrations"]:
        why.append(f"an earlier update didn't finish its migrations (applied through {tag(applied)})")

    if Path("BUILD-STATUS.md").exists():
        why.append("BUILD-STATUS.md is at the root: a build is underway or not closed out")
    if not result["auto_update"]:
        why.append("automatic updates are turned off in the ledger")
    if newest <= at:
        return result

    # The newest release this brain may take with nobody asked: every
    # migration on the way must be safe to run unattended.
    result["offer_target"] = tag(newest)
    reach = None
    for n in range(at + 1, newest + 1):
        body = migration(n, tag(newest))
        if body is None:
            if n in tags:
                result["stopped_at"] = {"release": tag(n), "reason": "its migration file is missing"}
                break
            continue
        if not auto_apply(body):
            result["stopped_at"] = {"release": tag(n), "title": first_line(body),
                                    "reason": "its migration needs a person"}
            break
        if n in tags:
            reach = n
    if reach is not None and not why:
        # Everything up to the first migration that needs a person; the skill
        # offers the rest (offer_target) in the same run.
        result["auto_target"] = tag(reach)
    return result


# --- record ----------------------------------------------------------------

def record_migration(version: str) -> str:
    n = number(version)
    if n is None or version != f"v{n}":
        raise Refusal(f"{version!r} is not a release like v41")
    text = read_ledger()
    applied = number(field(text, "Migrations applied through"))
    if applied is None:
        raise Refusal("the ledger has no readable Migrations applied through")
    if n == applied:
        return f"already recorded: migrations applied through {version}"
    at = mount_release()
    if at is None or n > at:
        raise Refusal(f"parker-system/ is at {tag(at) or 'no release'}; "
                      f"{version} isn't part of it yet")
    gap = [m for m in range(applied + 1, n) if migration(m, "HEAD") is not None]
    if n < applied or gap or migration(n, "HEAD") is None:
        expected = tag(gap[0]) if gap else "the next migration"
        raise Refusal(f"migrations are applied through {tag(applied)}; record {expected} "
                      f"first, never skip one")
    write_atomically(LEDGER, set_release(text, "Migrations applied through", version))
    return f"recorded: migrations applied through {version}"


def record_pin(version: str) -> str:
    n = number(version)
    if n is None or version != f"v{n}":
        raise Refusal(f"{version!r} is not a release like v41")
    head = git("rev-parse", "HEAD").stdout.strip()
    target = git("rev-parse", "--verify", "--quiet", f"{version}^{{commit}}", check=False)
    if target.returncode != 0 or target.stdout.strip() != head:
        raise Refusal(f"parker-system/ is not checked out at {version}")
    text = read_ledger()
    config = None
    if CONFIG.exists():
        try:
            config = json.loads(CONFIG.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            raise Refusal(f"{CONFIG} isn't valid JSON; fix it, then record the pin")
    new_text = set_release(text, "Pinned release", version)
    if new_text != text:
        write_atomically(LEDGER, new_text)
    if isinstance(config, dict) and config.get("parker_brain_version") != version:
        config["parker_brain_version"] = version
        write_atomically(CONFIG, json.dumps(config, indent=2) + "\n")
    return f"recorded: pinned release {version}"


def set_auto_update(state: str) -> str:
    text = read_ledger()
    line = f"- **Auto-update:** {state}"
    pat = field_pattern("Auto-update")
    if pat.search(text):
        new_text = pat.sub(lambda m: m.group(1) + f" {state}", text, count=1)
    else:
        anchor = field_pattern("Posture").search(text)
        if not anchor:
            raise Refusal("the ledger has no **Posture:** line to put the setting under")
        new_text = text[:anchor.end()] + "\n" + line + text[anchor.end():]
    if new_text != text:
        write_atomically(LEDGER, new_text)
    return f"automatic updates: {state}"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="command", required=True)
    sub.add_parser("plan", help="print what this brain may take on its own, as JSON")
    for name in ("record-migration", "record-pin"):
        sub.add_parser(name).add_argument("version")
    sub.add_parser("auto-update").add_argument("state", choices=("on", "off"))
    args = ap.parse_args()

    if not MOUNT.is_dir():
        print("update-brain: run from the brand brain's root folder; parker-system/ not found",
              file=sys.stderr)
        return 2
    if Path("prompts/onboarding-runner.md").exists() and not CONFIG.exists():
        print("update-brain: this looks like the factory, not a brand brain", file=sys.stderr)
        return 2
    try:
        if args.command == "plan":
            print(json.dumps(plan(), indent=2))
        elif args.command == "record-migration":
            print(record_migration(args.version))
        elif args.command == "record-pin":
            print(record_pin(args.version))
        else:
            print(set_auto_update(args.state))
    except Refusal as err:
        print(f"update-brain: {err}. Nothing was written.", file=sys.stderr)
        return 3
    except subprocess.CalledProcessError as err:
        print(f"update-brain: git failed in parker-system/: {(err.stderr or '').strip()}",
              file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
