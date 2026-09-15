"""Sanitized runtime regressions. Run: python3 -m unittest discover -s tests -v."""

import hashlib
import json
import os
from pathlib import Path
import runpy
import shutil
import subprocess
import sys
import tempfile
import tomllib
import unittest

FACTORY = Path(__file__).resolve().parents[1]
BUNDLE = FACTORY / "templates/brand-routines"


def make_brand(root):
    shutil.copytree(BUNDLE / "claude", root / ".claude")
    shutil.copytree(BUNDLE / "codex", root / ".codex")
    shutil.copyfile(BUNDLE / "AGENTS.md", root / "AGENTS.md")
    (root / "scripts").mkdir(exist_ok=True)
    shutil.copyfile(FACTORY / "scripts/usage-log.py", root / "scripts/usage-log.py")
    mount = root / "parker-system"
    (mount / "creative-strategy-context").mkdir(parents=True)
    shutil.copyfile(FACTORY / "creative-strategy-context/expertise-routing.md",
                    mount / "creative-strategy-context/expertise-routing.md")
    (mount / "source.md").write_text("fixture method\n")
    (root / "sub-context-docs").mkdir()


class RuntimeHooks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="parker runtime test ")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        make_brand(self.root)
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        self.config = tomllib.loads((self.root / ".codex/config.toml").read_text(encoding="utf-8"))

    def invoke(self, name, payload=None, cwd=None):
        command = [sys.executable, str(self.root / ".claude/hooks/run-hook.py"), name]
        if name == "git-guard":
            command.append("--codex")
        return subprocess.run(command, cwd=cwd or self.root,
                              input=json.dumps(payload or {}), text=True,
                              capture_output=True, timeout=10)

    def decision(self, inputs, tool="apply_patch", cwd=None):
        result = self.invoke("mount-guard", {"tool_name": tool,
                             "tool_input": inputs, "cwd": str(cwd or self.root)})
        self.assertEqual(result.returncode, 0, result.stderr)
        return bool(result.stdout and json.loads(result.stdout)["hookSpecificOutput"]["permissionDecision"] == "deny")

    def patch(self, header, key="command", cwd=None):
        return self.decision({key: f"*** Begin Patch\n{header}\n+fixture\n*** End Patch\n"}, cwd=cwd)

    def test_native_patch_operations_and_legacy_keys(self):
        for action in ("Add", "Update", "Delete"):
            for key in ("command", "input", "patch"):
                with self.subTest(action=action, key=key):
                    self.assertTrue(self.patch(f"*** {action} File: parker-system/source.md", key))
        self.assertTrue(self.patch("*** Update File: brand-lens.md\n*** Move to: parker-system/source.md"))
        self.assertFalse(self.patch("*** Add File: brand-lens.md"))

    def test_real_paths_and_nested_sessions(self):
        self.assertTrue(self.patch(f"*** Add File: {self.root}/parker-system/file.md"))
        self.assertFalse(self.patch("*** Add File: parker-system/../brand-lens.md"))
        self.assertTrue(self.patch("*** Add File: ../parker-system/file.md", cwd=self.root / "sub-context-docs"))
        self.assertFalse(self.patch("*** Add File: local.md", cwd=self.root / "sub-context-docs"))
        for tool, key in (("Write", "file_path"), ("NotebookEdit", "notebook_path")):
            self.assertTrue(self.decision({key: "parker-system/source.md"}, tool))

    def test_symlink_target_and_unrelated_same_name(self):
        alias = self.root / "method-alias"
        try:
            alias.symlink_to(self.root / "parker-system", target_is_directory=True)
        except OSError as error:
            self.skipTest(f"Symlinks unavailable: {error}")
        self.assertTrue(self.patch("*** Add File: method-alias/file.md"))
        self.assertFalse(self.patch("*** Add File: examples/parker-system/file.md"))

    def test_direct_shell_writes(self):
        if os.name == "nt":
            self.skipTest("POSIX shell syntax; Windows command startup is tested separately")
        for command in (
            "printf fixture > parker-system/file.md",
            "printf fixture >> parker-system/file.md",
            "rm parker-system/source.md", "mv parker-system/source.md brand.md",
            "cp brand.md parker-system/source.md", "cp -t parker-system brand.md",
            "tee parker-system/file.md", "sed -i s/a/b/ parker-system/source.md",
            "cd parker-system && touch file.md", 'touch "parker-system/file with spaces.md"',
        ):
            with self.subTest(command=command):
                self.assertTrue(self.decision({"command": command}, "Bash"))
        for command in (
            "cat parker-system/source.md", "rg fixture parker-system",
            "cp parker-system/source.md brand.md", "git -C parker-system fetch origin",
            "git -C parker-system checkout v17", "printf fixture > brand.md",
        ):
            with self.subTest(command=command):
                self.assertFalse(self.decision({"command": command}, "Bash"))

    def test_launcher_from_nested_directory(self):
        # Execute the actual committed command, not a reconstructed test command.
        nested = self.root / "sub-context-docs"
        for event, groups in self.config["hooks"].items():
            for group in groups:
                for hook in group["hooks"]:
                    command = hook["commandWindows"] if os.name == "nt" else hook["command"]
                    result = subprocess.run(command, shell=True, cwd=nested, input="{}",
                                            text=True, capture_output=True, timeout=10)
                    self.assertEqual(result.returncode, 0, (event, result.stderr))
                    if event in {"UserPromptSubmit", "SessionStart"} and "usage-log.py" not in command:
                        self.assertTrue(json.loads(result.stdout)["hookSpecificOutput"]["additionalContext"])

    def test_launcher_does_not_cross_repository_boundaries(self):
        nested_repo = self.root / "nested-repo"
        nested_repo.mkdir()
        subprocess.run(["git", "init", "-q", str(nested_repo)], check=True)
        self.assert_hooks_skipped(nested_repo)

    def test_missing_dispatcher_is_a_successful_noop(self):
        (self.root / ".claude/hooks/run-hook.py").unlink()
        self.assert_hooks_skipped(self.root / "sub-context-docs")

    def test_launcher_outside_a_repository_is_a_successful_noop(self):
        with tempfile.TemporaryDirectory(prefix="parker no repository ") as directory:
            self.assert_hooks_skipped(Path(directory))

    def assert_hooks_skipped(self, cwd):
        for groups in self.config["hooks"].values():
            for group in groups:
                for hook in group["hooks"]:
                    command = hook["commandWindows"] if os.name == "nt" else hook["command"]
                    result = subprocess.run(command, shell=True, cwd=cwd, input="{}",
                                            text=True, capture_output=True, timeout=10)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertEqual(result.stdout, "")

    def test_windows_shell_targets(self):
        inspect = runpy.run_path(str(BUNDLE / "claude/hooks/mount-guard.py"))["shell_targets"]
        cases = {
            r"copy brand.md parker-system\file.md /A": r"parker-system\file.md",
            r"copy /B brand.md parker-system\file.md /b /Y": r"parker-system\file.md",
            r"move /Y brand.md parker-system\file.md": r"parker-system\file.md",
            r"del /F /Q parker-system\file.md": r"parker-system\file.md",
            r"erase /Q parker-system\file.md": r"parker-system\file.md",
            r"rd /S /Q parker-system\folder": r"parker-system\folder",
        }
        for command, target in cases.items():
            with self.subTest(command=command):
                targets = [path for path, cwd in inspect(command, self.root, windows=True)]
                self.assertIn(target, targets)
                if os.name == "nt":
                    self.assertTrue(self.decision({"command": command}, "Bash"))
        command = r"copy parker-system\source.md brand.md /A"
        self.assertEqual(list(inspect(command, self.root, windows=True)), [("brand.md", self.root)])
        if os.name == "nt":
            self.assertFalse(self.decision({"command": command}, "Bash"))

    def test_full_catalog_and_profile_budget(self):
        result = self.invoke("craft-context")
        context = json.loads(result.stdout)["hookSpecificOutput"]["additionalContext"]
        source = (self.root / "parker-system/creative-strategy-context/expertise-routing.md").read_text(encoding="utf-8")
        for row in source.splitlines():
            if row.startswith("|") and ".md" in row:
                self.assertIn(row, context)
        limit = self.config["hooks"]["UserPromptSubmit"][0]["hooks"][0]["additionalContextLimit"]
        self.assertLessEqual(len(context.encode("utf-8")), limit)
        profile = self.root / "users/fixture/user-profile.md"
        profile.parent.mkdir(parents=True)
        profile.write_text("文" * 2500, encoding="utf-8")
        context = json.loads(self.invoke("craft-context").stdout)["hookSpecificOutput"]["additionalContext"]
        self.assertIn("Read users/fixture/user-profile.md in full", context)
        for row in source.splitlines():
            if row.startswith("|") and ".md" in row:
                self.assertIn(row, context)
        self.assertLessEqual(len(context.encode("utf-8")), limit)
        profile.write_text("Fixture rule. " * 20000)
        context = json.loads(self.invoke("craft-context").stdout)["hookSpecificOutput"]["additionalContext"]
        self.assertIn("Read users/fixture/user-profile.md in full", context)
        self.assertLessEqual(len(context.encode("utf-8")), limit)
        catalog = self.root / "parker-system/creative-strategy-context/expertise-routing.md"
        catalog.write_text("<!-- DOC-MAP:START -->\n" + "fixture " * 10000 + "\n<!-- DOC-MAP:END -->")
        context = json.loads(self.invoke("craft-context").stdout)["hookSpecificOutput"]["additionalContext"]
        self.assertIn("catalog has not been injected", context)
        self.assertIn("in full before answering", context)
        self.assertLessEqual(len(context.encode("utf-8")), limit)

    def test_multibyte_context_uses_a_conservative_token_bound(self):
        catalog = self.root / "parker-system/creative-strategy-context/expertise-routing.md"
        catalog.write_text("<!-- DOC-MAP:START -->\n" + "文" * 6000 + "\n<!-- DOC-MAP:END -->", encoding="utf-8")
        context = json.loads(self.invoke("craft-context").stdout)["hookSpecificOutput"]["additionalContext"]
        limit = self.config["hooks"]["UserPromptSubmit"][0]["hooks"][0]["additionalContextLimit"]
        self.assertLessEqual(len(context.encode("utf-8")), limit)
        self.assertIn("catalog has not been injected", context)

    def test_pull_log_uses_brand_root_from_nested_directory(self):
        key = hashlib.sha256(str(self.root).encode()).hexdigest()[:16]
        log = Path(tempfile.gettempdir()) / f"parker-pull-log-{key}.jsonl"
        self.addCleanup(lambda: log.unlink(missing_ok=True))
        result = self.invoke("pull-log", {"tool_name": "mcp__fixture__read", "session_id": "fixture"}, self.root / "sub-context-docs")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(log.read_text(encoding="utf-8"))["tool"], "mcp__fixture__read")

    def test_git_guard_retains_both_envelopes(self):
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        subprocess.run(["git", "-C", str(self.root), "remote", "add", "origin", "https://github.com/parker-brain/fixture"], check=True)
        for command in ("git push --force origin main", ["git", "push", "--force", "origin", "main"]):
            result = self.invoke("git-guard", {"tool_name": "Bash", "tool_input": {"command": command}}, self.root / "sub-context-docs")
            self.assertEqual(json.loads(result.stdout)["hookSpecificOutput"]["permissionDecision"], "deny")
        result = subprocess.run([sys.executable, str(self.root / ".claude/hooks/run-hook.py"), "git-guard"], input=json.dumps({"tool_name": "Bash", "tool_input": {"command": "git push --force origin main"}}), text=True, capture_output=True)
        self.assertEqual(result.returncode, 2)

    def test_git_guard_leaves_brand_sync_to_parker_desktop(self):
        subprocess.run(["git", "-C", str(self.root), "remote", "add", "origin", "https://git.example.test/parker-brain/fixture.git"], check=True)
        def denied(command):
            result = self.invoke("git-guard", {"tool_name": "Bash", "tool_input": {"command": command}})
            self.assertEqual(result.returncode, 0, result.stderr)
            return bool(result.stdout and json.loads(result.stdout)["hookSpecificOutput"]["permissionDecision"] == "deny")
        for command in ("git push origin main", "git commit -am fixture", "git pull --rebase", "git stash", "git switch --discard-changes main", "git submodule deinit -f parker-system", "git -C parker-system fetch --tags; git push origin main", "gh pr create", "git clone https://github.com/parker-brain/other.git", "git submodule add https://github.com/parker-brain/other.git other", "git clone --depth 1 https://github.com/real-simple-labs/parker-brain.git factory-compare; git push origin main", "git submodule add https://github.com/real-simple-labs/parker-brain parker-system && git push origin main", "git -C parker-system reset --hard", "git -C parker-system clean -fdx", "git -C parker-system push origin main", "git rm -r .", "git submodule update --remote parker-system"):
            with self.subTest(blocked=command):
                self.assertTrue(denied(command))
        for command in ("git status --short --branch", "git -C parker-system fetch origin --prune --prune-tags", "git -C parker-system checkout v18", "git submodule update --init parker-system", "git rm --cached parker-system && rm parker-system/.git && git add -- parker-system/", "git clone --depth 1 https://github.com/real-simple-labs/parker-brain.git factory-compare", "git submodule add https://github.com/real-simple-labs/parker-brain parker-system", "git -C parker-system describe --tags", "git -C parker-system rev-parse HEAD && git -C parker-system ls-files"):
            with self.subTest(allowed=command):
                self.assertFalse(denied(command))
        subprocess.run(["git", "-C", str(self.root), "remote", "set-url", "origin", "https://github.com/fixture-team/brain.git"], check=True)
        self.assertFalse(denied("git push origin main"))

    def test_native_permission_profile_and_shared_commands(self):
        self.assertEqual(self.config["default_permissions"], "parker-brain")
        profile = self.config["permissions"]["parker-brain"]
        self.assertEqual(profile["extends"], ":workspace")
        self.assertEqual(profile["filesystem"][":workspace_roots"]["parker-system"], "read")
        claude = json.loads((self.root / ".claude/settings.json").read_text(encoding="utf-8"))
        for event, groups in claude["hooks"].items():
            actual = groups[0]["hooks"][0]["command"]
            expected = self.config["hooks"][event][0]["hooks"][0]["command"]
            self.assertEqual(actual, expected.removesuffix(" --codex").replace("--runtime codex", "--runtime claude"))
        for groups in self.config["hooks"].values():
            for group in groups:
                for hook in group["hooks"]:
                    self.assertEqual(hook["commandWindows"], hook["command"].replace("python3 ", "py -3 ", 1))
                    self.assertNotIn("/dev/null", hook["commandWindows"])


if __name__ == "__main__":
    unittest.main()
