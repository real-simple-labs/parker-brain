#!/usr/bin/env python3
"""Run a shared brand hook from the brand root, preserving stdin and exit status."""

import os
from pathlib import Path
import runpy
import sys

HOOKS = {"session-start", "craft-context", "git-guard", "mount-guard", "pull-log"}


def main() -> None:
    name = sys.argv[1]
    if name not in HOOKS:
        raise ValueError(f"Unknown brand hook: {name}")
    directory = Path(__file__).resolve().parent
    os.chdir(directory.parent.parent)
    sys.argv = [str(directory / f"{name}.py"), *sys.argv[2:]]
    runpy.run_path(sys.argv[0], run_name="__main__")


if __name__ == "__main__":
    main()
