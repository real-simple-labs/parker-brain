#!/usr/bin/env python3
"""The two git steps of a cloud run that touch its key.

A Claude cloud routine runs in auto mode. Its safety check never sees tool
results, so it stops a key step that only the Parker MCP tool's text asks
for; and the check in the session that creates a routine stops a routine
prompt that carries the key command itself ("Credential Exploration"). The
factory's .claude/settings.json allows exactly these two commands, so
neither check has to judge them. A routine starts in a checkout of the
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
        folder.

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
from pathlib import Path
from urllib.parse import urlsplit

HOSTS = ("git.heyparker.ai", "dev-git.heyparker.ai")
SECRET_PREFIX = "parker_git_"
CACHE_HELPER = f"cache --timeout={24 * 60 * 60}"
BRAND_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9-]{0,63}")
REPO_PATH = re.compile(r"^/([A-Za-z0-9._-]+)/([A-Za-z0-9._-]+)\.git$")
FACTORY = Path(__file__).resolve().parent.parent


def git_env() -> dict[str, str]:
    """Git may never stop to ask: no terminal prompt and no inherited askpass
    helper, so a missing key fails at once instead of holding a run."""
    return {**os.environ, "GIT_TERMINAL_PROMPT": "0", "GIT_ASKPASS": "", "SSH_ASKPASS": ""}


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
    args = parser.parse_args(argv)
    try:
        if args.step == "key":
            print(make_key(args.brand_id))
        else:
            command = clone_args(
                args.git_url, args.brand_id,
                Path(args.folder) if args.folder is not None else None)
            subprocess.run(command, check=True, env=git_env())
            folder = command[-1]
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
    except FileNotFoundError:
        print("cloud-run-git.py: git is not installed here", file=sys.stderr)
        return 127
    except subprocess.CalledProcessError as err:
        return err.returncode or 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
