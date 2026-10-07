#!/usr/bin/env python3
"""The git steps of a cloud run that touch its key or Parker's git server.

A Claude cloud routine runs in auto mode. Its safety check never sees tool
results, so it stops a key step that only the Parker MCP tool's text asks
for; and the check in the session that creates a routine stops a routine
prompt that carries the key command itself ("Credential Exploration"). The
factory's .claude/settings.json allows exactly these commands, so neither
check has to judge them. A routine starts in a checkout of the
factory, where this script and that rule live; run it from that folder.

    scripts/cloud-run-git.py key <brand_id>
        Makes a key for Parker's git servers, hands it to git's credential
        cache (memory only, no file) under the user parker-<brand_id>, and
        prints only its SHA-256: the hash register_parker_brain_git_credential
        takes. The cache keeps it for a day, for both servers (production and
        dev); it opens only the one whose API registered its hash, and the
        server's one-hour registration decides when it stops working.

    scripts/cloud-run-git.py clone <git_url> <brand_id> [<folder>]
        Clones the brain from the git_url that tool returns, with the cache
        as the only credential helper for Parker's server and the brand's
        user in the URL, then sets up the brain's parker-system mount. The
        folder defaults to the brain's name next to this checkout. Prints the
        folder. A big brain clones for minutes: wait for the folder line, as
        a half-made copy ("No commits yet") is not an empty brain.

    scripts/cloud-run-git.py save <folder> [-m <message>]
        Saves a copy made by `clone` to Parker's git server: commits what
        changed (with the message), takes in what others saved meanwhile
        (pull --rebase), and pushes to main, trying again when someone saves
        in between. It never forces a push, pushes only to Parker's git
        server, and runs no git hook from the copy. When a change clashes with what
        someone else saved, it pushes nothing and names the files: combine
        them in the copy, then run save again, which finishes and pushes.
        Prints "saved <commit>" when the brain has it.

The key never reaches a command line, a file, or this script's output.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import secrets
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import urlsplit

HOSTS = ("git.heyparker.ai", "dev-git.heyparker.ai")
SECRET_PREFIX = "parker_git_"
CACHE_HELPER = f"cache --timeout={24 * 60 * 60}"
BRAND_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9-]{0,63}")
REPO_PATH = re.compile(r"^/([A-Za-z0-9._-]+)/([A-Za-z0-9._-]+)\.git$")
FACTORY = Path(__file__).resolve().parent.parent


def git_env() -> dict[str, str]:
    """Git may never stop to ask: no terminal prompt, no inherited askpass
    helper and no editor, so a missing key fails at once instead of holding
    a run."""
    return {**os.environ, "GIT_TERMINAL_PROMPT": "0", "GIT_ASKPASS": "", "SSH_ASKPASS": "",
            "GIT_EDITOR": "true"}


class UsageError(Exception):
    pass


def credential_user(brand_id: str) -> str:
    """One cache entry per brand: git's cache holds one secret per host and
    user, so two brains in one session each keep their own."""
    # fullmatch: `$` would also take a final newline, which ends git's
    # credential input early and caches no key at all.
    if not BRAND_ID.fullmatch(brand_id):
        raise UsageError(f"not a brand_id: {brand_id!r}")
    return f"parker-{brand_id}"


def make_key(brand_id: str, hosts: tuple[str, ...] = HOSTS, protocol: str = "https") -> str:
    """Puts a new secret in git's credential cache for each host and returns
    its SHA-256. The secret goes to git on stdin only."""
    user = credential_user(brand_id)
    secret = SECRET_PREFIX + secrets.token_hex(32)
    for host in hosts:
        subprocess.run(
            ["git", "-c", "credential.helper=", "-c", f"credential.helper={CACHE_HELPER}",
             "credential", "approve"],
            input=f"protocol={protocol}\nhost={host}\nusername={user}\npassword={secret}\n\n",
            text=True, check=True, env=git_env(),
        )
    return hashlib.sha256(secret.encode("utf-8")).hexdigest()


def clone_args(git_url: str, brand_id: str, folder: Path | None = None) -> list[str]:
    """The clone command for a gateway URL the tool returned. The empty
    helper first switches off every other one; the cache then answers
    Parker's server only."""
    parts = urlsplit(git_url)
    match = REPO_PATH.match(parts.path)
    if (parts.scheme != "https" or parts.hostname not in HOSTS or parts.port
            or parts.username or parts.password or parts.query or parts.fragment
            or not match):
        raise UsageError(f"not a Parker git server address: {git_url!r}")
    if folder is not None and (not str(folder) or str(folder).startswith("-")):
        raise UsageError(f"not a folder: {str(folder)!r}")
    origin = f"https://{parts.hostname}"
    url = f"https://{credential_user(brand_id)}@{parts.hostname}{parts.path}"
    target = folder if folder is not None else FACTORY.parent / match.group(2)
    # `--` ends git's options: nothing after it can become one, whatever the
    # folder says.
    return [
        "git", "clone",
        "-c", "credential.helper=",
        "-c", f"credential.{origin}.helper={CACHE_HELPER}",
        "-c", f"credential.{origin}.useHttpPath=false",
        "--", url, str(target),
    ]


SAVE_ATTEMPTS = 5
FALLBACK_IDENTITY = {"user.name": "Parker cloud run", "user.email": "routines@heyparker.ai"}
MARKER_LINE = re.compile(rb"^(<<<<<<<|\|\|\|\|\|\|\||>>>>>>>)( |$)", re.M)
# Plain markers whatever the machine's git config says (diff3 and zdiff3 add a
# ||||||| block with the old text), so the clash message and the check above
# describe what is really in the file.
CONFLICT_STYLE = ["-c", "merge.conflictStyle=merge"]
# A pull or push that moves no data for ten minutes has stalled: let git give
# up so save reports it, rather than hold the run forever. Parker's server can
# go quiet for a minute or more while it builds a big brain's answer.
STALL_LIMIT = {"GIT_HTTP_LOW_SPEED_LIMIT": "1", "GIT_HTTP_LOW_SPEED_TIME": "600"}


class SaveError(Exception):
    """A save that can't finish; the message says what to do."""

    def __init__(self, message: str, code: int):
        super().__init__(message)
        self.code = code


# The factory allows save without the safety check, so nothing in the copy
# may run code through it: no git hooks and no file-system monitor.
NO_CODE = ["-c", "core.hooksPath=/dev/null", "-c", "core.fsmonitor=false"]


def git(folder: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(folder), *NO_CODE, *args],
                          capture_output=True, text=True, env={**git_env(), **STALL_LIMIT})


def check_copy(folder: Path) -> None:
    """Only a copy `clone` made: its origin is Parker's git server, with the
    brand's user in the address. So this allowed command can push nowhere
    else."""
    if not str(folder) or str(folder).startswith("-") or not folder.is_dir():
        raise UsageError(f"not a folder: {str(folder)!r}")
    # Every address origin fetches from and pushes to, after any insteadOf or
    # pushInsteadOf rewrite: a pushurl is where the push really goes.
    fetch = git(folder, "remote", "get-url", "--all", "origin")
    push = git(folder, "remote", "get-url", "--push", "--all", "origin")
    urls = fetch.stdout.split() + push.stdout.split()
    if fetch.returncode != 0 or push.returncode != 0 or not urls or not all(map(parker_url, urls)):
        raise UsageError(f"{folder} is not a copy made by `clone`: its origin is not "
                         "Parker's git server")


def parker_url(url: str) -> bool:
    parts = urlsplit(url)
    return (parts.scheme == "https" and parts.hostname in HOSTS
            and not (parts.port or parts.password or parts.query or parts.fragment)
            and bool(parts.username) and parts.username.startswith("parker-")
            and bool(BRAND_ID.fullmatch(parts.username[len("parker-"):]))
            and bool(REPO_PATH.match(parts.path)))


def identity(folder: Path) -> list[str]:
    """Commits and the rebase need a name and an email; a fresh cloud machine
    has neither."""
    args: list[str] = []
    for key, value in FALLBACK_IDENTITY.items():
        if not git(folder, "config", key).stdout.strip():
            args += ["-c", f"{key}={value}"]
    return args


def rebase_open(folder: Path) -> bool:
    for name in ("rebase-merge", "rebase-apply"):
        path = git(folder, "rev-parse", "--git-path", name).stdout.strip()
        if path and (folder / path).is_dir():
            return True
    return False


def clash(folder: Path) -> SaveError:
    files = [f for f in git(folder, "diff", "--name-only", "-z", "--diff-filter=U").stdout.split("\0") if f]
    return SaveError(
        "what you changed clashes with what someone else saved, in: "
        + (", ".join(files) or "the same files")
        + f". Nothing was pushed. In {folder}, combine each of those files: keep what "
        "matters from both versions and delete every marker line (<<<<<<<, =======, "
        ">>>>>>>). Then run this save command again: it finishes and pushes.", 3)


def finish_rebase(folder: Path, ident: list[str]) -> None:
    """The last save stopped on a clash and left the rebase open; the files
    are combined now. Take them and finish it."""
    git(folder, "add", "-A")
    staged = [f for f in git(folder, "diff", "--cached", "--name-only", "-z", "HEAD").stdout.split("\0") if f]
    left = [f for f in staged
            if (folder / f).is_file() and MARKER_LINE.search((folder / f).read_bytes())]
    if left:
        raise SaveError(
            "these files still have marker lines (<<<<<<<, ||||||| or >>>>>>>): " + ", ".join(left)
            + ". Combine them, then run save again.", 3)
    # Kept only their version: this commit has nothing left to add.
    step = "--continue" if staged else "--skip"
    done = git(folder, *ident, *CONFLICT_STYLE, "rebase", step)
    if done.returncode != 0:
        if rebase_open(folder):
            raise clash(folder)
        raise SaveError(done.stderr.strip() or done.stdout.strip(), done.returncode)


def save(folder: Path, message: str | None, attempts: int = SAVE_ATTEMPTS) -> str:
    check_copy(folder)
    ident = identity(folder)
    if rebase_open(folder):
        finish_rebase(folder, ident)
    elif git(folder, "status", "--porcelain").stdout.strip():
        if not message:
            raise UsageError("the copy has changes: give a message with -m")
        add = git(folder, "add", "-A")
        if add.returncode != 0:
            raise SaveError(add.stderr.strip(), add.returncode)
        commit = git(folder, *ident, "commit", "-m", message)
        if commit.returncode != 0:
            raise SaveError(commit.stderr.strip() or commit.stdout.strip(), commit.returncode)
    for attempt in range(1, attempts + 1):
        pull = git(folder, *ident, *CONFLICT_STYLE, "pull", "--rebase", "origin", "main")
        if pull.returncode != 0:
            # The rebase stays open, so the next save can finish it once the
            # files are combined; no fetch or push is left for the agent to run.
            if rebase_open(folder):
                raise clash(folder)
            raise SaveError(pull.stderr.strip() or pull.stdout.strip(), pull.returncode)
        ahead = git(folder, "rev-list", "--count", "origin/main..HEAD").stdout.strip()
        if ahead == "0":
            return git(folder, "rev-parse", "--short", "HEAD").stdout.strip()
        push = git(folder, "push", "origin", "HEAD:main")
        if push.returncode == 0:
            return git(folder, "rev-parse", "--short", "HEAD").stdout.strip()
        # Someone saved between the pull and the push: take it in and go again.
        if not any(word in push.stderr for word in ("non-fast-forward", "fetch first", "[rejected]")):
            raise SaveError(push.stderr.strip(), push.returncode)
        time.sleep(2 * attempt)
    raise SaveError(f"main kept moving: tried {attempts} times. Run save again.", 4)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        prog="cloud-run-git.py", description=__doc__.split("\n\n")[0])
    sub = parser.add_subparsers(dest="step", required=True)
    key = sub.add_parser("key", help="make the key; prints only its hash")
    key.add_argument("brand_id")
    clone = sub.add_parser("clone", help="clone the brain with the key")
    clone.add_argument("git_url")
    clone.add_argument("brand_id")
    clone.add_argument("folder", nargs="?")
    save_step = sub.add_parser("save", help="commit, take in others' saves, and push to main")
    save_step.add_argument("folder")
    save_step.add_argument("-m", "--message")
    args = parser.parse_args(argv)
    try:
        if args.step == "key":
            print(make_key(args.brand_id))
        elif args.step == "save":
            print(f"saved {save(Path(args.folder), args.message)}")
        else:
            command = clone_args(
                args.git_url, args.brand_id,
                Path(args.folder) if args.folder is not None else None)
            folder = command[-1]
            # A cloud shell moves a command that runs past its timeout to the
            # background, and an agent once read the half-made copy as an
            # empty brain. Say so before the wait, where the shell shows it.
            # No folder in this line: the folder alone, on stdout, means done.
            print("cloud-run-git.py: cloning. A big Parker Brain takes several minutes: wait "
                  "until this command prints the folder. Until then git says \"No commits "
                  "yet\" there: that is the clone still running, not an empty brain.",
                  file=sys.stderr, flush=True)
            subprocess.run(command, check=True, env=git_env())
            # The method mount comes from the public factory. Without it the
            # copy still works, so a failure here is a warning, not a stop.
            mount = subprocess.run(
                ["git", "-C", folder, "submodule", "update", "--init"], env=git_env())
            if mount.returncode != 0:
                print("cloud-run-git.py: the copy is ready, but parker-system could not be "
                      "set up: it comes from github.com, which this environment may block. "
                      "The copy works without it.", file=sys.stderr)
            print(folder)
    except UsageError as err:
        print(f"cloud-run-git.py: {err}", file=sys.stderr)
        return 2
    except SaveError as err:
        print(f"cloud-run-git.py: {err}", file=sys.stderr)
        return err.code or 1
    except FileNotFoundError:
        print("cloud-run-git.py: git is not installed here", file=sys.stderr)
        return 127
    except subprocess.CalledProcessError as err:
        return err.returncode or 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
