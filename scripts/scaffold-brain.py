#!/usr/bin/env python3
"""Scaffold an empty brand brain: every file a new brain starts with, no AI involved.

Three commands:

  init      Run inside a brand folder whose parker-system/ mount is attached.
            Writes every scaffold file that is missing and never overwrites one.
              python3 parker-system/scripts/scaffold-brain.py init \\
                  --brand-name "Acme" --brand-id 123
            With --restore-copies it instead puts back the pinned release's
            version of every method copy that is missing or was edited, on any
            brain, and touches nothing else (the build verification's repair).

  manifest  Run in a factory checkout. Writes the scaffold for one release as
            GitHub tree entries (brain-scaffold.json), so a backend can create a
            scaffolded brand repo with three write calls and no git. CI runs this
            on every published release and attaches the file to it.
              python3 scripts/scaffold-brain.py manifest --tag v23 --out brain-scaffold.json

  push      Test helper. Applies a manifest to a fresh GitHub repo exactly the way
            the backend does: create the tree, create the commit, move the branch.
            Refuses any repo that already holds more than GitHub's first commit.
              GITHUB_TOKEN=... python3 scripts/scaffold-brain.py push \\
                  --manifest brain-scaffold.json --repo owner/name \\
                  --brand-name "Acme" --brand-id 123

What a new brain starts with is defined in exactly two lists:

  - bundle_map() in scripts/sync-executable-layer.py: method files copied in
    verbatim (skills, agents, hooks, checker scripts, schedules, the Codex twin).
    /update-brain refreshes them on every pin bump.
  - SEEDS below: brand-owned starting files, written once and never touched by
    the update sync.

A file every brain needs belongs in one of the two, or it never reaches a new
brain. system/brain-scaffold.md is the full contract.
"""

import argparse
from dataclasses import dataclass
from datetime import date
import json
import os
from pathlib import Path
import re
import runpy
import subprocess
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request

HERE = Path(__file__).resolve().parent
FACTORY_REMOTE = "https://github.com/real-simple-labs/parker-brain"
MOUNT = "parker-system"
MARKER = ".scaffolded"
SKILLS_LINK = ".agents/skills"
SKILLS_LINK_TARGET = "../.claude/skills"
MANIFEST_FORMAT = 1

# The only placeholders a scaffold carries. The backend substitutes them in every
# file of the manifest; bundle files are checked to contain none of them.
TOKENS = {
    "{{BRAND_NAME}}": "the brand's display name",
    "{{BRAND_ID}}": "the Parker brand id",
    "{{GITHUB_REPO_URL}}": "the brand repo's URL, e.g. https://github.com/parker-brain/acme",
    "{{CREATED_AT}}": "the scaffold date, YYYY-MM-DD",
}
# Files whose placeholder values must be JSON-string-escaped before substitution.
JSON_PATHS = ("parker_config.json",)

_sync = runpy.run_path(str(HERE / "sync-executable-layer.py"))
bundle_map = _sync["bundle_map"]
wants_exec = _sync["wants_exec"]
safe_dest = _sync["safe_dest"]
is_schedule = _sync["is_schedule"]
normalized = _sync["normalized"]
merge_status = _sync["merge_status"]

NOT_CAPTURED = "Not captured yet."

CLAUDE_PHASE_STATUS = (
    "Right now this brain is scaffolded, not built: no phase has run, nothing is "
    "approved, and there is no committed strategy yet. A Phase-2 or Phase-3 ask gets "
    "the work, plus the honest caveat that no audit or roadmap sits behind it yet."
)

CLAUDE_BUILD_STATUS = """\
**Not built yet.** This brain was scaffolded on {{CREATED_AT}}. The method library, the skills, the routines, and empty running notes are in place, but none of the brand's own knowledge has been written: no brand profile, no personas, no audits, no competitor reads, no strategy. The `.scaffolded` file at the root marks this state until the build starts writing real docs: a hook takes it off when the build reports its first finished phase after Phase 0, and the build's closeout removes it if it's still there. Don't delete it yourself. If a build is under way (a `BUILD-STATUS.md` at the root), the docs it has written so far are real: use them, and `/set-up-brain` resumes the rest. Otherwise the line at the top of this file that says the homework is here isn't true yet. Until it is:

- **Most of the map above doesn't exist yet.** Check before you cite a doc, and don't treat a missing one as a failed read. What's real is `running-notes/`, `brand-lens.md`, and anything the team has added since.
- **Lean on live pulls.** For anything about the account, the customers, or the competitors, pull it fresh through the Parker MCP and label every claim honestly. With no vault to check a pull against, say what one pull can and can't tell you.
- **Save what the team teaches you where it piles up:** team, process, and current work in `running-notes/brand-notes-from-org.md`; how they define winning in `running-notes/brand-rules.md`; the business goal in `running-notes/success-definition.md`; voice, claims rules, and what has worked in `brand-lens.md`; what's still missing in `running-notes/missing-context.md`. Source and date every line.
- **Don't hand-write the standing docs.** `sub-context-docs/`, `personas/`, `competitors/`, `audits/`, and `strategy/` each come from their own prompt in `parker-system/prompts/`, and the build writes them in order.
- **Offer the build, don't push it.** When an answer would be much sharper with the real audit behind it, say so once and offer `/set-up-brain`. Never hold a specific ask back for it.
- **Hold off on the routines.** Dreaming, the idea cycle, and the refresh sweep need a built vault to work on, so don't offer to schedule them until the build is done.

`running-notes/missing-context.md` is the live list of what the brain still doesn't know."""

MARKER_TEXT = """\
This brand brain is scaffolded, not built.

It was set up on {{CREATED_AT}} from the Parker method library at release {tag}.
The method, the skills, and the routines are in place; the brand's own knowledge
hasn't been written yet. Parker still works here: it pulls live data and saves
what the team tells it into running-notes/ and brand-lens.md.

Parker's apps read this file's presence as "nothing built yet". It comes off on
its own once the full build (/set-up-brain) reports its first finished phase
after Phase 0, and the build's closeout removes it if it's still there. Don't
delete it by hand unless the brain really has been built.
"""

GITMODULES = (
    f'[submodule "{MOUNT}"]\n'
    f"\tpath = {MOUNT}\n"
    f"\turl = {FACTORY_REMOTE}\n"
)


@dataclass(frozen=True)
class Seed:
    """A brand-owned starting file, written once from a factory template.

    strip: "none", "rule" (drop the template header through its first `---`
    line), "blockquote" (drop the `>` note under the title), or "structure"
    (the file is the fenced block under the template's `## Structure`).
    slots: regex -> replacement, each of which must match at least once.
    blank_slots: replace every remaining {{slot}} with NOT_CAPTURED.
    """
    dest: str
    source: str
    strip: str = "none"
    slots: tuple = ()
    blank_slots: bool = False


SEEDS = (
    Seed("CLAUDE.md", "templates/brand-brain-CLAUDE-template.md", "rule", (
        (r"\{\{BRAND_HARD_RULES\b[^{}]*\}\}\n\n", ""),
        (r"\{\{PHASE_STATUS\b[^{}]*\}\}", CLAUDE_PHASE_STATUS),
        (r"\{\{BUILD_STATUS\b[^{}]*\}\}", CLAUDE_BUILD_STATUS),
    )),
    Seed("README.md", "templates/brand-scaffold/README.md"),
    Seed("open-loops/README.md", "templates/brand-scaffold/open-loops/README.md"),
    Seed("hypotheses/README.md", "templates/brand-scaffold/hypotheses/README.md"),
    Seed("validations/README.md", "templates/brand-scaffold/validations/README.md"),
    Seed("re-validations/README.md", "templates/brand-scaffold/re-validations/README.md"),
    Seed("dreaming/README.md", "templates/brand-scaffold/dreaming/README.md"),
    Seed("workflows/README.md", "templates/brand-scaffold/workflows/README.md"),
    Seed("brand-lens.md", "templates/brand-lens-template.md", "rule", blank_slots=True),
    Seed("running-notes/standard-sync.md", "templates/standard-sync-template.md", "blockquote", (
        (r"\{\{FACTORY_REMOTE\b[^{}]*\}\}", FACTORY_REMOTE),
        (r"(\*\*Posture:\*\* `follow`) \{\{[^{}]*\}\}", r"\1"),
        (r"\{\{TAG\b[^{}]*\}\}", "{tag}"),
        (r"\{\{DATE\}\}", "{{CREATED_AT}}"),
        (r"\{\{NEWEST TAG SEEN\}\}", "{tag}"),
        (r"\{\{(No offers yet[^{}]*)\}\}", r"\1"),
    )),
    Seed("running-notes/brand-rules.md", "templates/brand-rules-template.md", "blockquote",
         blank_slots=True),
    Seed("running-notes/success-definition.md", "templates/success-definition-template.md",
         "blockquote", blank_slots=True),
    Seed("running-notes/missing-context.md", "templates/missing-context-template.md", "structure", (
        (r"(?m)^brand:$", "brand: {{BRAND_NAME}}"),
        (r"(?m)^last_updated:$", "last_updated: {{CREATED_AT}}"),
    )),
    Seed("running-notes/brand-notes-from-org.md", "templates/brand-notes-from-org-template.md",
         "structure", (
        (r"(?m)^brand:$", "brand: {{BRAND_NAME}}"),
        (r"(?m)^last_updated:$", "last_updated: {{CREATED_AT}}"),
        (r"(?m)^(# Brand notes from org — )\[brand\]$", r"\1{{BRAND_NAME}}"),
    )),
    Seed("running-notes/routine-log.md", "templates/routine-log-template.md", "rule"),
)


class ScaffoldError(Exception):
    pass


def git(repo: Path, *args: str) -> str:
    result = subprocess.run(["git", "-C", str(repo), *args],
                            capture_output=True, text=True)
    if result.returncode != 0:
        raise ScaffoldError(f"git {' '.join(args)} failed in {repo}: {result.stderr.strip()}")
    return result.stdout


class Factory:
    """The factory at one commit, read from git objects (never the working tree),
    so a scaffold is the same wherever it is built."""

    def __init__(self, repo: Path, ref: str):
        self.repo = repo
        self.commit = git(repo, "rev-parse", "--verify", f"{ref}^{{commit}}").strip()
        self.entries: dict[str, tuple[str, str]] = {}
        for record in git(repo, "ls-tree", "-r", "-z", self.commit).split("\0"):
            if not record:
                continue
            meta, path = record.split("\t", 1)
            mode, otype, sha = meta.split()
            if otype == "blob":
                self.entries[path] = (mode, sha)
        self._cache: dict[str, bytes] = {}

    def read(self, path: str) -> bytes:
        if path not in self.entries:
            raise ScaffoldError(f"{path} is not in the factory at {self.commit[:12]}")
        if path not in self._cache:
            self._cache[path] = subprocess.run(
                ["git", "-C", str(self.repo), "cat-file", "blob", self.entries[path][1]],
                check=True, capture_output=True,
            ).stdout
        return self._cache[path]

    def text(self, path: str) -> str:
        try:
            return self.read(path).decode("utf-8")
        except UnicodeDecodeError:
            raise ScaffoldError(f"{path} is not UTF-8 text; the scaffold only carries text files")


@dataclass(frozen=True)
class Entry:
    path: str
    kind: str          # "file", "symlink", or "gitlink"
    content: str = ""  # file text (with placeholders) or symlink target
    sha: str = ""      # gitlink commit
    executable: bool = False
    origin: str = ""   # "bundle", "seed", or "generated"


def strip_header(text: str, how: str, source: str) -> str:
    lines = text.split("\n")
    if how == "rule":
        try:
            end = lines.index("---")
        except ValueError:
            raise ScaffoldError(f"{source}: expected a `---` line closing the template header")
        if not any(line.startswith(">") for line in lines[:end]):
            raise ScaffoldError(f"{source}: expected a `>` template note before the first `---`")
        rest = lines[end + 1:]
    elif how == "blockquote":
        if not lines[0].startswith("# "):
            raise ScaffoldError(f"{source}: expected a `# ` title on the first line")
        i = 1
        while i < len(lines) and not lines[i].strip():
            i += 1
        if i >= len(lines) or not lines[i].startswith(">"):
            raise ScaffoldError(f"{source}: expected a `>` template note under the title")
        while i < len(lines) and lines[i].startswith(">"):
            i += 1
        while i < len(lines) and not lines[i].strip():
            i += 1
        rest = [lines[0], ""] + lines[i:]
    elif how == "structure":
        # The first fenced block after the `## Structure` heading, with no other
        # section starting in between (the block itself holds `## ` headings).
        try:
            start = lines.index("## Structure") + 1
            fence = next(i for i in range(start, len(lines)) if lines[i].startswith("```"))
            close = next(i for i in range(fence + 1, len(lines)) if lines[i].startswith("```"))
        except (ValueError, StopIteration):
            raise ScaffoldError(f"{source}: expected a fenced block under `## Structure`")
        if any(line.startswith("## ") for line in lines[start:fence]):
            raise ScaffoldError(f"{source}: expected a fenced block under `## Structure`")
        return "\n".join(lines[fence + 1:close]).strip("\n") + "\n"
    else:
        return text
    while rest and not rest[0].strip():
        rest.pop(0)
    return "\n".join(rest)


def render_seed(seed: Seed, factory: Factory, tag: str) -> str:
    text = strip_header(factory.text(seed.source), seed.strip, seed.source)
    for pattern, replacement in seed.slots:
        replacement = replacement.replace("{tag}", tag)
        text, count = re.subn(pattern, lambda m: m.expand(replacement), text)
        if not count:
            raise ScaffoldError(f"{seed.source}: slot /{pattern}/ not found; "
                                "update SEEDS in scripts/scaffold-brain.py to match the template")
    if seed.blank_slots:
        text = re.sub(r"\{\{(?!(?:BRAND_NAME|BRAND_ID|GITHUB_REPO_URL|CREATED_AT)\}\})[^{}]*\}\}",
                      NOT_CAPTURED, text)
    if seed.strip != "none":
        for line in text.split("\n"):
            if re.match(r"> (Status|Template for|Instantiate)", line):
                raise ScaffoldError(f"{seed.source}: template note survived into {seed.dest}")
    if seed.dest == "CLAUDE.md" or seed.blank_slots or seed.strip == "blockquote":
        leftover = [s for s in re.findall(r"\{\{[^{}]*\}\}", text) if s not in TOKENS]
        if leftover:
            raise ScaffoldError(f"{seed.dest}: unfilled template slots {leftover[:3]}")
    return text


def plan(factory: Factory, tag: str) -> list[Entry]:
    """Every entry of an empty brain, placeholders unrendered."""
    entries: list[Entry] = []
    seen: set[str] = set()

    def add(entry: Entry):
        if entry.path in seen:
            raise ScaffoldError(f"{entry.path} is produced twice; the bundle map and SEEDS overlap")
        seen.add(entry.path)
        entries.append(entry)

    for src, dest in sorted(bundle_map(factory.entries).items(), key=lambda item: item[1]):
        mode = factory.entries[src][0]
        if mode not in ("100644", "100755"):
            raise ScaffoldError(f"{src} has git mode {mode}; the bundle only carries regular files")
        text = factory.text(src)
        found = [token for token in TOKENS if token in text]
        if found:
            raise ScaffoldError(f"{src} contains {found[0]}; bundle files are copied verbatim and "
                                "must not carry scaffold placeholders")
        add(Entry(dest, "file", text, executable=wants_exec(dest), origin="bundle"))

    for seed in SEEDS:
        add(Entry(seed.dest, "file", render_seed(seed, factory, tag), origin="seed"))

    config = {
        "brand_id": "{{BRAND_ID}}",
        "brand_name": "{{BRAND_NAME}}",
        "github_repo_url": "{{GITHUB_REPO_URL}}",
        "parker_brain_version": tag,
        "created_at": "{{CREATED_AT}}",
        "usage_logging": {"enabled": False},
    }
    add(Entry("parker_config.json", "file", json.dumps(config, indent=2) + "\n", origin="generated"))
    add(Entry(MARKER, "file", MARKER_TEXT.replace("{tag}", tag), origin="generated"))
    add(Entry(SKILLS_LINK, "symlink", SKILLS_LINK_TARGET, origin="generated"))
    add(Entry(".gitmodules", "file", GITMODULES, origin="generated"))
    add(Entry(MOUNT, "gitlink", sha=factory.commit, origin="generated"))
    return entries


TOKEN_PATTERN = re.compile(r"\{\{(?:BRAND_NAME|BRAND_ID|GITHUB_REPO_URL|CREATED_AT)\}\}")


def render(text: str, values: dict[str, str], path: str) -> str:
    """One pass over the text, so a value can never smuggle in another placeholder."""
    if path in JSON_PATHS:
        values = {token: json.dumps(value, ensure_ascii=False)[1:-1] for token, value in values.items()}
    return TOKEN_PATTERN.sub(lambda match: values[match.group(0)], text)


def without_credentials(url: str) -> str:
    """Drop any user:token@ from an http(s) URL. A clone made with a token has
    one in its origin, and parker_config.json is committed and shared."""
    parts = urllib.parse.urlsplit(url.strip())
    if parts.scheme in ("http", "https") and "@" in parts.netloc:
        parts = parts._replace(netloc=parts.netloc.rsplit("@", 1)[1])
    return urllib.parse.urlunsplit(parts)


def token_values(brand_name: str, brand_id: str, repo_url: str, created_at: str) -> dict[str, str]:
    if not brand_name.strip():
        raise ScaffoldError("--brand-name is required")
    if not str(brand_id).strip():
        raise ScaffoldError("--brand-id is required")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", created_at):
        raise ScaffoldError("--created-at must be YYYY-MM-DD")
    return {
        "{{BRAND_NAME}}": brand_name.strip(),
        "{{BRAND_ID}}": str(brand_id).strip(),
        "{{GITHUB_REPO_URL}}": without_credentials(repo_url),
        "{{CREATED_AT}}": created_at,
    }


# ---------------------------------------------------------------- init

def release_tag(mount: Path, override: str | None) -> str:
    if override:
        head = git(mount, "rev-parse", "HEAD").strip()
        at = git(mount, "rev-parse", "--verify", f"{override}^{{commit}}").strip()
        if at != head:
            raise ScaffoldError(f"--tag {override} is {at[:12]}, but parker-system/ is at {head[:12]}; "
                                "the files come from the mount, so the recorded release must match it")
        return override
    result = subprocess.run(["git", "-C", str(mount), "describe", "--tags", "--exact-match", "HEAD"],
                            capture_output=True, text=True)
    tag = result.stdout.strip()
    if result.returncode != 0 or not tag:
        raise ScaffoldError(
            "parker-system/ isn't checked out at a release tag. Run "
            "`git -C parker-system fetch --tags` and check out the newest vN tag, "
            "or pass --tag if it already is.")
    return tag


_UMASK = os.umask(0)
os.umask(_UMASK)


def fsync_dir(folder: Path):
    """Make a rename in this folder durable. POSIX only; Windows can't open a folder."""
    if os.name == "nt":
        return
    fd = os.open(folder, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def replace_atomically(path: Path, data: bytes, executable: bool = False, sync_dir: bool = False):
    """Write to a new, exclusively created sibling temp file, then swap it into
    place. A failure leaves the old file (or no file) behind, never a short one a
    later run would take as done, and a planted file or symlink can't redirect the
    write. An existing file keeps its permissions; a new one gets the usual mode."""
    fd, name = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.", suffix=".scaffold-tmp")
    tmp = Path(name)
    try:
        try:
            mode = path.stat().st_mode & 0o7777
        except FileNotFoundError:
            mode = 0o666 & ~_UMASK
        if executable:
            mode |= 0o111 & ~_UMASK
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            tmp.chmod(mode)  # before the fsync, so the mode is as durable as the bytes
            os.fsync(handle.fileno())
        os.replace(tmp, path)
        if sync_dir:
            fsync_dir(path.parent)
    except BaseException:
        try:
            tmp.unlink()
        except OSError:
            pass
        raise


def merge_config(path: Path, rendered: str) -> tuple[str, bool]:
    """Add the scaffold's keys an existing parker_config.json lacks; change nothing else.
    Returns (what happened, whether it needs attention)."""
    try:
        current = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        return (f"isn't readable JSON ({error}); left as is. Fix or remove it and run this again "
                "so the brain's identity and pinned release get recorded"), True
    if not isinstance(current, dict):
        return ("isn't a JSON object; left as is. Fix or remove it and run this again so the "
                "brain's identity and pinned release get recorded"), True
    added = [key for key in json.loads(rendered) if key not in current]
    if not added:
        return "kept", False
    for key in added:
        current[key] = json.loads(rendered)[key]
    try:
        replace_atomically(path, (json.dumps(current, indent=2) + "\n").encode("utf-8"))
    except OSError as error:
        raise ScaffoldError(f"couldn't update parker_config.json: {error}")
    return "added " + ", ".join(added), False


def check_mount(mount: Path):
    if Path("prompts/onboarding-runner.md").exists() and not mount.exists():
        raise ScaffoldError("this looks like the factory repo, not a brand folder")
    if Path(".gitmodules").exists() and mount.is_dir() and not any(mount.iterdir()):
        raise ScaffoldError(
            "parker-system/ is attached but empty. Run `git submodule update --init "
            f"{MOUNT}` (local and credential-free), then run this again.")
    if not (mount / ".git").exists() or not Path(".gitmodules").exists():
        raise ScaffoldError(
            "the method library isn't attached here yet. Attach it first (Phase 0 step 3 of "
            f"prompts/onboarding-runner.md): git submodule add {FACTORY_REMOTE} {MOUNT}, then "
            "check out the newest release tag inside it.")


def recorded_release() -> str | None:
    try:
        return json.loads(Path("parker_config.json").read_text(encoding="utf-8")).get("parker_brain_version")
    except (OSError, json.JSONDecodeError, AttributeError):
        return None


def link_skills(entry: Entry, dry_run: bool, written: list, kept: list, problems: list):
    path = Path(entry.path)
    if path.is_symlink() or path.exists():
        kept.append(entry.path)
        return
    written.append(entry.path)
    if dry_run:
        return
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        os.symlink(entry.content, path, target_is_directory=True)
    except OSError as error:
        written.remove(entry.path)
        problems.append(
            f"couldn't create the {entry.path} link to {entry.content} ({error}). Claude "
            "Code works without it; Codex needs it. On Windows, turn on Developer Mode and "
            "git's symlink support, then run this again.")


def write_file(entry: Entry, data: bytes):
    path = Path(entry.path)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        # the marker's folder entry must be durable before any later file's is
        replace_atomically(path, data, entry.executable, sync_dir=entry.path == MARKER)
    except OSError as error:
        raise ScaffoldError(f"couldn't write {entry.path}: {error}. Fix that and run the same "
                            "command again; it picks up where it stopped.")


def cmd_init(args) -> int:
    if args.only and not args.restore_copies:
        raise ScaffoldError("--only works with --restore-copies")
    target = Path(args.target).resolve()
    os.chdir(target)
    mount = Path(MOUNT)
    check_mount(mount)
    tag = release_tag(mount, args.tag)
    factory = Factory(mount, "HEAD")
    if args.restore_copies:
        return restore_copies(factory, tag, args)

    scaffolded = Path(MARKER).exists()
    if not scaffolded:
        started = [p for p in ("CLAUDE.md", "BUILD-STATUS.md", "prompts-run-log") if Path(p).exists()]
        if started:
            raise ScaffoldError(
                f"this brain is already built or a build has started here ({started[0]} exists "
                f"and there is no {MARKER}). The scaffold only sets up new brains; "
                "/update-brain refreshes the method files of a standing one, and --restore-copies "
                "puts back method files a build edited by mistake.")
    if not args.brand_name or not args.brand_id:
        raise ScaffoldError("--brand-name and --brand-id are required")
    repo_url = args.repo_url
    if repo_url is None:
        origin = subprocess.run(["git", "remote", "get-url", "origin"], capture_output=True, text=True)
        repo_url = origin.stdout.strip() if origin.returncode == 0 else ""
    values = token_values(args.brand_name, args.brand_id, repo_url,
                          args.created_at or date.today().isoformat())

    written, kept, notes, problems = [], [], [], []
    recorded = recorded_release()
    if recorded and recorded != tag:
        problems.append(
            f"parker_config.json records {recorded} but parker-system/ is at {tag}. The copies "
            f"already here came from {recorded}; finish the move the /update-brain way: "
            f"`python3 parker-system/scripts/sync-executable-layer.py --from {recorded}`, then record "
            f"{tag} in parker_config.json and running-notes/standard-sync.md.")
    entries = plan(factory, tag)
    # The marker goes first: a run that dies partway must leave a folder the next
    # run recognizes as scaffolded and finishes, not one it mistakes for a built brain.
    entries.sort(key=lambda entry: entry.path != MARKER)
    for entry in entries:
        if entry.kind == "gitlink" or entry.path == ".gitmodules":
            continue  # the mount is already attached
        if entry.kind == "symlink":
            link_skills(entry, args.dry_run, written, kept, problems)
            continue
        path = Path(entry.path)
        text = render(entry.content, values, entry.path)
        if path.exists() or path.is_symlink():
            if entry.path == "parker_config.json" and not args.dry_run:
                outcome, broken = merge_config(path, text)
                (problems if broken else notes).append(f"parker_config.json: {outcome}")
            else:
                kept.append(entry.path)
            continue
        if not safe_dest(entry.path):
            problems.append(f"skipped {entry.path}: a symlink or folder is in the way")
            continue
        written.append(entry.path)
        if not args.dry_run:
            write_file(entry, text.encode("utf-8"))

    verb = "would write" if args.dry_run else "wrote"
    print(f"scaffold-brain init ({tag}){' (dry run)' if args.dry_run else ''}: "
          f"{verb} {len(written)} files, kept {len(kept)} that already existed")
    if args.verbose:
        for label, paths in ((verb, written), ("kept", kept)):
            for p in paths:
                print(f"  {label}: {p}")
    elif kept and scaffolded:
        print("  this folder was already scaffolded; only missing files were added")
    for note in notes:
        print(f"  {note}")
    for problem in problems:
        print(f"  needs attention: {problem}")
    return 1 if problems else 0


def restore_copies(factory: Factory, tag: str, args) -> int:
    """Put back the pinned release's version of every method copy (the bundle map)
    that is missing or differs. Never touches the brand's own files or the marker.
    For repairing a build that edited copies by mistake; on a standing brain it
    overwrites the team's edits, so /update-brain is the tool there."""
    recorded = recorded_release()
    if recorded and recorded != tag:
        raise ScaffoldError(
            f"parker_config.json records {recorded} but parker-system/ is at {tag}; "
            "restoring now would mix releases. Finish that move with /update-brain first.")
    entries = [entry for entry in plan(factory, tag) if entry.origin == "bundle" or entry.kind == "symlink"]
    only = {path.replace("\\", "/").strip("/") for path in args.only or ()}
    restored = []
    problems = [f"{path} isn't a method copy this release ships; nothing restored there"
                for path in sorted(only - {entry.path for entry in entries})]
    for entry in entries:
        if only and entry.path not in only:
            continue
        if entry.kind == "symlink":
            link_skills(entry, args.dry_run, restored, [], problems)
            continue
        path = Path(entry.path)
        wanted = entry.content.encode("utf-8")
        if path.is_file() and not path.is_symlink():
            current = path.read_bytes()
            if is_schedule(entry.path):
                if normalized(current) == normalized(wanted):
                    continue
                wanted = merge_status(wanted, current)  # keep the armed Status line
            elif current == wanted:
                continue
        if not safe_dest(entry.path):
            problems.append(f"skipped {entry.path}: a symlink or folder is in the way")
            continue
        restored.append(entry.path)
        if not args.dry_run:
            write_file(entry, wanted)
    verb = "would restore" if args.dry_run else "restored"
    print(f"scaffold-brain init --restore-copies ({tag}): {verb} {len(restored)} method files")
    for p in restored:
        print(f"  {verb}: {p}")
    for problem in problems:
        print(f"  needs attention: {problem}")
    return 1 if problems else 0


# ---------------------------------------------------------------- manifest

def build_manifest(factory: Factory, tag: str) -> dict:
    tree = []
    for entry in plan(factory, tag):
        if entry.kind == "gitlink":
            tree.append({"path": entry.path, "mode": "160000", "type": "commit", "sha": entry.sha})
        elif entry.kind == "symlink":
            tree.append({"path": entry.path, "mode": "120000", "type": "blob", "content": entry.content})
        else:
            tree.append({"path": entry.path, "mode": "100755" if entry.executable else "100644",
                         "type": "blob", "content": entry.content})
    return {
        "format": MANIFEST_FORMAT,
        "factory": {"remote": FACTORY_REMOTE, "tag": tag, "commit": factory.commit},
        "placeholders": TOKENS,
        "json_escaped_paths": list(JSON_PATHS),
        "marker": MARKER,
        "tree": tree,
    }


def cmd_manifest(args) -> int:
    repo = Path(args.factory).resolve() if args.factory else HERE.parent
    if not re.fullmatch(r"v\d+", args.tag):
        print(f"warning: {args.tag} isn't a vN release tag; a brain built from this manifest "
              "has no release for /update-brain to compare against", file=sys.stderr)
    manifest = build_manifest(Factory(repo, args.tag), args.tag)
    out = Path(args.out)
    out.write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    size = out.stat().st_size
    print(f"scaffold-brain manifest {args.tag}: {len(manifest['tree'])} entries, "
          f"{size // 1024} KB -> {out}")
    return 0


# ---------------------------------------------------------------- push

def github_api(token: str, base: str = "https://api.github.com"):
    def call(method: str, path: str, body: dict | None = None):
        request = urllib.request.Request(
            base + path, method=method,
            data=json.dumps(body).encode() if body is not None else None,
            headers={"Authorization": f"Bearer {token}",
                     "Accept": "application/vnd.github+json",
                     "X-GitHub-Api-Version": "2022-11-28",
                     "Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                return response.status, json.loads(response.read() or b"null")
        except urllib.error.HTTPError as error:
            detail = error.read().decode("utf-8", "replace")
            return error.code, (json.loads(detail) if detail.startswith("{") else {"message": detail})
        except urllib.error.URLError as error:
            raise ScaffoldError(f"couldn't reach {base}: {error.reason}")
    return call


# Files GitHub may create on a new repo (auto_init, gitignore_template, license_template).
FRESH_REPO_FILES = {"README.md", ".gitignore", "LICENSE"}


def apply_manifest(manifest: dict, repo: str, values: dict[str, str], api) -> str:
    """The backend's three write calls, plus the reads it should make first.
    `api(method, path, body)` returns (status, json). Returns the new commit sha."""
    if manifest.get("format") != MANIFEST_FORMAT:
        raise ScaffoldError(f"manifest format {manifest.get('format')} isn't {MANIFEST_FORMAT}")
    status, info = api("GET", f"/repos/{repo}")
    if status != 200:
        raise ScaffoldError(f"can't read {repo}: {status} {info.get('message')}")
    branch = info["default_branch"]
    status, ref = api("GET", f"/repos/{repo}/git/ref/heads/{branch}")
    if status != 200:
        raise ScaffoldError(f"{repo} has no {branch} commit yet ({status} {ref.get('message')}). "
                            "Create it with auto_init: true; the tree API can't write to an empty repo.")
    head = ref["object"]["sha"]
    status, commit = api("GET", f"/repos/{repo}/git/commits/{head}")
    if status != 200:
        raise ScaffoldError(f"can't read {repo}@{head}: {status}")
    if commit.get("parents"):
        raise ScaffoldError(f"{repo} already has history beyond its first commit; refusing to scaffold over it")
    status, tree = api("GET", f"/repos/{repo}/git/trees/{commit['tree']['sha']}")
    names = {item["path"] for item in tree.get("tree", [])} if status == 200 else set()
    extra = sorted(names - FRESH_REPO_FILES)
    if status != 200 or extra:
        raise ScaffoldError(f"{repo} isn't fresh (found {', '.join(extra) or 'an unreadable tree'}); "
                            "refusing to scaffold over it")

    entries = []
    for item in manifest["tree"]:
        item = dict(item)
        if "content" in item:
            item["content"] = render(item["content"], values, item["path"])
        entries.append(item)
    # base_tree keeps a LICENSE or .gitignore the repo was created with; the
    # manifest's README.md replaces GitHub's starter one.
    status, new_tree = api("POST", f"/repos/{repo}/git/trees",
                           {"base_tree": commit["tree"]["sha"], "tree": entries})
    if status != 201:
        raise ScaffoldError(f"create tree failed: {status} {new_tree.get('message')}")
    tag = manifest["factory"]["tag"]
    status, new_commit = api("POST", f"/repos/{repo}/git/commits", {
        "message": f"Scaffold an empty brand brain (Parker method {tag})",
        "tree": new_tree["sha"], "parents": [head],
    })
    if status != 201:
        raise ScaffoldError(f"create commit failed: {status} {new_commit.get('message')}")
    status, moved = api("PATCH", f"/repos/{repo}/git/refs/heads/{branch}",
                        {"sha": new_commit["sha"], "force": False})
    if status != 200:
        raise ScaffoldError(f"moving {branch} failed: {status} {moved.get('message')}")
    return new_commit["sha"]


def cmd_push(args) -> int:
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        raise ScaffoldError("set GITHUB_TOKEN to a token that can write to the repo")
    if not re.fullmatch(r"[\w.-]+/[\w.-]+", args.repo):
        raise ScaffoldError("--repo must be owner/name")
    manifest = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    values = token_values(args.brand_name, args.brand_id,
                          args.repo_url or f"https://github.com/{args.repo}",
                          args.created_at or date.today().isoformat())
    sha = apply_manifest(manifest, args.repo, values, github_api(token, args.api))
    print(f"scaffold-brain push: {args.repo} now at {sha[:12]} "
          f"({len(manifest['tree'])} entries, method {manifest['factory']['tag']})")
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    sub = parser.add_subparsers(dest="command", required=True)

    def identity(p, repo_url_help, required=True):
        p.add_argument("--brand-name", required=required)
        p.add_argument("--brand-id", required=required)
        p.add_argument("--repo-url", help=repo_url_help)
        p.add_argument("--created-at", help="YYYY-MM-DD (default: today)")

    init = sub.add_parser("init", help="scaffold the brand folder this runs in")
    identity(init, "the brand repo URL (default: the folder's origin)", required=False)
    init.add_argument("--target", default=".", help="brand folder (default: current folder)")
    init.add_argument("--tag", help="release the mount is at (default: read from parker-system/)")
    init.add_argument("--dry-run", action="store_true")
    init.add_argument("--verbose", action="store_true", help="list every file")
    init.add_argument("--restore-copies", action="store_true",
                      help="put back the release's version of every method copy that is missing or "
                           "edited, on any brain; never touches brand files (for build repairs)")
    init.add_argument("--only", action="append", metavar="PATH",
                      help="with --restore-copies: restore just this copy (repeatable), so a "
                           "copy the team edited on purpose stays as it is")
    init.set_defaults(run=cmd_init)

    manifest = sub.add_parser("manifest", help="write the scaffold as GitHub tree entries")
    manifest.add_argument("--tag", required=True, help="release tag to build from, e.g. v23")
    manifest.add_argument("--factory", help="factory checkout (default: this script's repo)")
    manifest.add_argument("--out", default="brain-scaffold.json")
    manifest.set_defaults(run=cmd_manifest)

    push = sub.add_parser("push", help="test helper: apply a manifest to a fresh GitHub repo")
    identity(push, "the brand repo URL (default: https://github.com/<repo>)")
    push.add_argument("--manifest", required=True)
    push.add_argument("--repo", required=True, help="owner/name")
    push.add_argument("--api", default="https://api.github.com")
    push.set_defaults(run=cmd_push)

    args = parser.parse_args(argv)
    try:
        return args.run(args)
    except ScaffoldError as error:
        print(f"scaffold-brain: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
