"""The cloud-run key script and the factory rule that allows it."""

import contextlib
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

from test_runtime_hooks import FACTORY

SCRIPT = FACTORY / "scripts/cloud-run-git.py"
_spec = importlib.util.spec_from_file_location("cloud_run_git", SCRIPT)
crg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(crg)

BRAND = "e608c8a7-141b-4154-9881-c131c8e78ebf"
URL = "https://git.heyparker.ai/parker-brain/admin-laura-geller.git"


class CloneCommand(unittest.TestCase):
    def test_clones_with_the_cache_for_parkers_server_and_the_brands_user(self):
        args = crg.clone_args(URL, BRAND, Path("/work/brain"))
        self.assertEqual(args, [
            "git", "clone",
            "-c", "credential.helper=",
            "-c", "credential.https://git.heyparker.ai.helper=cache --timeout=86400",
            "-c", "credential.https://git.heyparker.ai.useHttpPath=false",
            f"https://parker-{BRAND}@git.heyparker.ai/parker-brain/admin-laura-geller.git",
            "/work/brain",
        ])

    def test_clones_next_to_the_factory_checkout_by_default(self):
        args = crg.clone_args(URL, BRAND)
        self.assertEqual(Path(args[-1]), FACTORY.parent / "admin-laura-geller")

    def test_takes_only_a_parker_git_server_address(self):
        for url in [
            "http://git.heyparker.ai/parker-brain/a.git",
            "https://github.com/parker-brain/a.git",
            "https://git.heyparker.ai.evil.example/parker-brain/a.git",
            "https://git.heyparker.ai:8443/parker-brain/a.git",
            "https://someone@git.heyparker.ai/parker-brain/a.git",
            "https://git.heyparker.ai/parker-brain/a.git?x=1",
            "https://git.heyparker.ai/parker-brain/a",
            "https://git.heyparker.ai/a/b/c.git",
        ]:
            with self.subTest(url=url), self.assertRaises(crg.UsageError):
                crg.clone_args(url, BRAND)
        crg.clone_args("https://dev-git.heyparker.ai/parker-brain/a.git", BRAND)

    def test_takes_only_a_brand_id_a_shell_cannot_read(self):
        for brand in ["", "a b", "$(id)", "a;b", "x" * 65]:
            with self.subTest(brand=brand), self.assertRaises(crg.UsageError):
                crg.credential_user(brand)

    def test_refuses_bad_input_with_exit_code_2_and_runs_nothing(self):
        with mock.patch.object(crg.subprocess, "run") as run, \
                contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(crg.main(["clone", "https://github.com/a/b.git", BRAND]), 2)
            self.assertEqual(crg.main(["key", "not a brand"]), 2)
        run.assert_not_called()


@unittest.skipIf(sys.platform == "win32", "git's credential cache needs Unix sockets")
class KeyInGitsMemory(unittest.TestCase):
    def setUp(self):
        self.home = tempfile.mkdtemp(prefix="crg-")
        self.env = {**os.environ, "HOME": self.home, "XDG_CACHE_HOME": os.path.join(self.home, ".cache"),
                    "GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull,
                    "GIT_TERMINAL_PROMPT": "0", "GIT_ASKPASS": "", "SSH_ASKPASS": ""}
        patcher = mock.patch.dict(os.environ, self.env, clear=True)
        patcher.start()
        self.addCleanup(patcher.stop)
        self.addCleanup(lambda: subprocess.run(
            ["git", "credential-cache", "exit"], env=self.env, capture_output=True))

    def fill(self, user):
        out = subprocess.run(
            ["git", "-c", f"credential.helper={crg.CACHE_HELPER}", "credential", "fill"],
            input=f"protocol=http\nhost=127.0.0.1:9\nusername={user}\n\n",
            env=self.env, text=True, capture_output=True, check=True).stdout
        return dict(line.split("=", 1) for line in out.splitlines() if "=" in line)["password"]

    def test_keeps_the_key_in_memory_and_prints_only_its_hash(self):
        printed = crg.make_key(BRAND, host="127.0.0.1:9", protocol="http")
        self.assertRegex(printed, r"^[0-9a-f]{64}$")
        secret = self.fill(f"parker-{BRAND}")
        self.assertRegex(secret, r"^parker_git_[0-9a-f]{64}$")
        self.assertEqual(hashlib.sha256(secret.encode()).hexdigest(), printed)
        self.assertEqual([p.name for p in Path(self.home).iterdir()], [".cache"])

    def test_a_second_brands_key_leaves_the_first_one_in_place(self):
        crg.make_key("brand-1", host="127.0.0.1:9", protocol="http")
        first = self.fill("parker-brand-1")
        crg.make_key("brand-2", host="127.0.0.1:9", protocol="http")
        self.assertEqual(self.fill("parker-brand-1"), first)
        self.assertNotEqual(self.fill("parker-brand-2"), first)


class FactoryRule(unittest.TestCase):
    def test_allows_these_two_steps_of_this_script_and_nothing_else(self):
        settings = json.loads((FACTORY / ".claude/settings.json").read_text())
        self.assertEqual(settings["permissions"], {"allow": [
            "Bash(scripts/cloud-run-git.py key *)",
            "Bash(scripts/cloud-run-git.py clone *)",
            "Bash(python3 scripts/cloud-run-git.py key *)",
            "Bash(python3 scripts/cloud-run-git.py clone *)",
        ]})

    def test_routine_prompts_name_the_script_and_carry_no_key_command(self):
        for path in [".claude/skills/setup-routines/SKILL.md",
                     "templates/brand-routines/claude/skills/setup-routines/SKILL.md"]:
            with self.subTest(path=path):
                text = (FACTORY / path).read_text()
                self.assertIn("1. Run `scripts/cloud-run-git.py key [brand_id]`.", text)
                self.assertIn("3. Run `scripts/cloud-run-git.py clone <git_url> [brand_id]`", text)
                self.assertNotIn("credential approve", text)
                self.assertNotIn("openssl rand", text)

    @unittest.skipIf(sys.platform == "win32", "no execute bit on Windows")
    def test_the_script_runs_as_written_in_the_rule(self):
        self.assertTrue(os.access(SCRIPT, os.X_OK))
        self.assertTrue(SCRIPT.read_text().startswith("#!/usr/bin/env python3\n"))


if __name__ == "__main__":
    unittest.main()
