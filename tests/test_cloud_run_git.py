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
# The folder as this system writes it (Windows turns the slashes around).
FOLDER = str(Path("/work/brain"))


class CloneCommand(unittest.TestCase):
    def test_clones_with_the_cache_for_parkers_server_and_the_brands_user(self):
        args = crg.clone_args(URL, BRAND, Path("/work/brain"))
        self.assertEqual(args, [
            "git", "clone",
            "-c", "credential.helper=",
            "-c", "credential.https://git.heyparker.ai.helper=cache --timeout=86400",
            "-c", "credential.https://git.heyparker.ai.useHttpPath=false",
            "--",
            f"https://parker-{BRAND}@git.heyparker.ai/parker-brain/admin-laura-geller.git",
            FOLDER,
        ])

    def test_a_folder_can_never_become_a_git_option(self):
        # `clone <url> <brand> -- '--config=credential.helper=!cmd'` would have
        # let the allowed command run any shell command through git.
        for folder in ["--config=credential.helper=!id", "-c", "-"]:
            with self.subTest(folder=folder), self.assertRaises(crg.UsageError):
                crg.clone_args(URL, BRAND, Path(folder))
        with mock.patch.object(crg.subprocess, "run") as run, \
                contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(crg.main(
                ["clone", URL, BRAND, "--", "--config=credential.helper=!id"]), 2)
        run.assert_not_called()

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
        for brand in ["", "a b", "$(id)", "a;b", "-x", "a\nb", "brand\n", "x" * 65]:
            with self.subTest(brand=brand), self.assertRaises(crg.UsageError):
                crg.credential_user(brand)

    def test_refuses_bad_input_with_exit_code_2_and_runs_nothing(self):
        with mock.patch.object(crg.subprocess, "run") as run, \
                contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(crg.main(["clone", "https://github.com/a/b.git", BRAND]), 2)
            self.assertEqual(crg.main(["key", "not a brand"]), 2)
        run.assert_not_called()


class Main(unittest.TestCase):
    """The two steps as the allowed command runs them, git mocked."""

    def run_main(self, argv, side_effect=None):
        out, err = io.StringIO(), io.StringIO()
        with mock.patch.object(crg.subprocess, "run", side_effect=side_effect) as run, \
                contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = crg.main(argv)
        return code, out.getvalue(), err.getvalue(), run

    def test_key_caches_one_secret_for_both_servers_and_prints_only_its_hash(self):
        code, out, _, run = self.run_main(["key", BRAND])
        self.assertEqual(code, 0)
        printed = out.strip()
        self.assertRegex(printed, r"^[0-9a-f]{64}$")
        inputs = [call.kwargs["input"] for call in run.call_args_list]
        self.assertEqual([i.split("\n")[1] for i in inputs],
                         ["host=git.heyparker.ai", "host=dev-git.heyparker.ai"])
        secrets_sent = {i.split("password=")[1].split("\n")[0] for i in inputs}
        self.assertEqual(len(secrets_sent), 1)
        secret = secrets_sent.pop()
        self.assertEqual(hashlib.sha256(secret.encode()).hexdigest(), printed)
        self.assertNotIn(secret, out)
        for call in run.call_args_list:
            self.assertNotIn(secret, " ".join(call.args[0]))
            self.assertIn(f"username=parker-{BRAND}", call.kwargs["input"])

    def test_clone_never_prompts_sets_up_the_mount_and_prints_the_folder(self):
        code, out, err, run = self.run_main(["clone", URL, BRAND, "/work/brain"])
        self.assertEqual(code, 0)
        self.assertEqual(out.strip(), FOLDER)
        clone, mount = run.call_args_list
        self.assertEqual(clone.args[0][:2], ["git", "clone"])
        self.assertEqual(mount.args[0], ["git", "-C", FOLDER, "submodule", "update", "--init"])
        for call in (clone, mount):
            env = call.kwargs["env"]
            self.assertEqual((env["GIT_TERMINAL_PROMPT"], env["GIT_ASKPASS"], env["SSH_ASKPASS"]),
                             ("0", "", ""))
            self.assertIn("PATH", env)

    def test_says_to_wait_before_the_clone_starts(self):
        # The shell shows this line when it moves a long clone to the
        # background, so it has to be out before git starts.
        err, seen = io.StringIO(), []

        def fake(cmd, **kwargs):
            if cmd[:2] == ["git", "clone"]:
                seen.append(err.getvalue())
            return subprocess.CompletedProcess(cmd, 0)
        with mock.patch.object(crg.subprocess, "run", side_effect=fake), \
                contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(err):
            self.assertEqual(crg.main(["clone", URL, BRAND, "/work/brain"]), 0)
        self.assertEqual(len(seen), 1)
        self.assertIn("cloud-run-git.py: cloning. A big Parker Brain takes several minutes",
                      seen[0])
        self.assertIn('"No commits yet" there: that is the clone still running', seen[0])
        # The folder means done, so it shows up nowhere before the clone.
        self.assertNotIn(FOLDER, seen[0])

    def test_a_failed_mount_warns_but_keeps_the_copy(self):
        def fake(cmd, **kwargs):
            return subprocess.CompletedProcess(cmd, 1 if "submodule" in cmd else 0)
        code, out, err, _ = self.run_main(["clone", URL, BRAND, "/work/brain"], side_effect=fake)
        self.assertEqual(code, 0)
        self.assertEqual(out.strip(), FOLDER)
        self.assertIn("parker-system could not be set up", err)

    def test_a_failed_clone_prints_no_folder_and_passes_gits_exit_code(self):
        def fake(cmd, **kwargs):
            raise subprocess.CalledProcessError(
                128, cmd, stderr="fatal: Authentication failed for 'https://git.heyparker.ai/...'")
        code, out, _, run = self.run_main(["clone", URL, BRAND, "/work/brain"], side_effect=fake)
        self.assertEqual((code, out), (128, ""))
        self.assertEqual(run.call_count, 1)

    def test_no_git_is_a_plain_error(self):
        code, out, err, _ = self.run_main(["clone", URL, BRAND], side_effect=FileNotFoundError("git"))
        self.assertEqual((code, out), (127, ""))
        self.assertIn("git is not installed", err)


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
        printed = crg.make_key(BRAND, hosts=("127.0.0.1:9",), protocol="http")
        self.assertRegex(printed, r"^[0-9a-f]{64}$")
        secret = self.fill(f"parker-{BRAND}")
        self.assertRegex(secret, r"^parker_git_[0-9a-f]{64}$")
        self.assertEqual(hashlib.sha256(secret.encode()).hexdigest(), printed)
        self.assertEqual([p.name for p in Path(self.home).iterdir()], [".cache"])

    def test_a_second_brands_key_leaves_the_first_one_in_place(self):
        crg.make_key("brand-1", hosts=("127.0.0.1:9",), protocol="http")
        first = self.fill("parker-brand-1")
        crg.make_key("brand-2", hosts=("127.0.0.1:9",), protocol="http")
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
                self.assertIn("give the command a long timeout (10 minutes) and wait until it "
                              "prints the folder", text)
                self.assertNotIn("credential approve", text)
                self.assertNotIn("openssl rand", text)

    @unittest.skipIf(sys.platform == "win32", "no execute bit on Windows")
    def test_the_script_runs_as_written_in_the_rule(self):
        self.assertTrue(os.access(SCRIPT, os.X_OK))
        self.assertTrue(SCRIPT.read_text().startswith("#!/usr/bin/env python3\n"))


if __name__ == "__main__":
    unittest.main()
