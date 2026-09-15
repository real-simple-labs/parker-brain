"""Exercise the actual v16 bundle upgrade, including team-owned overrides."""

import io
import os
from pathlib import Path
import runpy
import subprocess
import sys
import tarfile
import tempfile
import unittest

from test_runtime_hooks import FACTORY

SYNC = FACTORY / "scripts/sync-executable-layer.py"


class ReleaseSync(unittest.TestCase):
    def test_absorb_preserves_files_and_can_reconnect(self):
        with tempfile.TemporaryDirectory(prefix="parker absorb test ") as directory:
            root = Path(directory).resolve()
            source, brand = root / "factory", root / "brand"
            source.mkdir()
            brand.mkdir()
            env = {**os.environ, "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"}

            def git(cwd, *args):
                return subprocess.check_output(
                    ["git", "-c", "user.name=Runtime Test", "-c", "user.email=runtime@example.invalid",
                     "-c", "core.autocrlf=false", "-c", "commit.gpgsign=false",
                     "-c", "protocol.file.allow=always", *args],
                    cwd=cwd, env=env, text=True, stderr=subprocess.STDOUT,
                )

            git(source, "init", "-q")
            (source / "method.md").write_bytes(b"Fixture method\n")
            git(source, "add", "--", "method.md")
            git(source, "commit", "-qm", "Fixture method")
            git(brand, "init", "-q")
            git(brand, "submodule", "add", str(source), "parker-system")
            git(brand, "commit", "-qm", "Fixture pinned method")
            mount = brand / "parker-system"
            method = (mount / "method.md").read_bytes()

            unrelated = brand / "unrelated.md"
            unrelated.write_bytes(b"Fixture user work\n")
            git(brand, "add", "--", "unrelated.md")
            with self.assertRaises(subprocess.CalledProcessError):
                git(brand, "diff", "--cached", "--quiet")
            self.assertTrue((mount / ".git").is_file())
            self.assertIn("unrelated.md", git(brand, "diff", "--cached", "--name-only"))
            # Simulate the user separating their work before approving the absorb.
            git(brand, "restore", "--staged", "--", "unrelated.md")
            git(brand, "diff", "--cached", "--quiet")
            git(brand, "rm", "--cached", "parker-system")
            (brand / ".gitmodules").unlink()
            self.assertTrue((mount / ".git").is_file())
            (mount / ".git").unlink()
            git(brand, "add", "--", "parker-system/")
            git(brand, "add", "-u", "--", ".gitmodules")
            self.assertEqual((mount / "method.md").read_bytes(), method)
            self.assertIn("parker-system/method.md", git(brand, "ls-files"))
            self.assertNotIn("160000", git(brand, "ls-files", "--stage"))
            self.assertTrue((brand / ".git/modules/parker-system").is_dir())
            self.assertEqual(set(git(brand, "diff", "--cached", "--name-only").splitlines()),
                             {".gitmodules", "parker-system", "parker-system/method.md"})
            git(brand, "commit", "-qm", "Fixture absorb")
            self.assertNotIn("unrelated.md", git(brand, "ls-files"))
            self.assertEqual(unrelated.read_bytes(), b"Fixture user work\n")
            git(brand, "revert", "--no-edit", "HEAD")
            git(brand, "submodule", "update", "--init", "parker-system")
            self.assertTrue((mount / ".git").is_file())
            self.assertEqual((mount / "method.md").read_bytes(), method)

    def test_v16_upgrade_is_complete_idempotent_and_preserves_overrides(self):
        helpers = runpy.run_path(str(SYNC))
        bundle_map = helpers["bundle_map"]
        old_paths = subprocess.check_output(
            ["git", "ls-tree", "-r", "--name-only", "v16"], cwd=FACTORY, text=True,
        ).splitlines()
        current_paths = subprocess.check_output(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
            cwd=FACTORY, text=True,
        ).splitlines()
        old_map = bundle_map(dict.fromkeys(old_paths))
        new_map = bundle_map(dict.fromkeys(current_paths))
        archive = subprocess.check_output(["git", "archive", "v16"], cwd=FACTORY)
        with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
            old_files = {src: tar.extractfile(src).read() for src in old_map}

        with tempfile.TemporaryDirectory(prefix="parker upgrade test ") as directory:
            root = Path(directory).resolve()
            mount = root / "parker-system"
            mount.mkdir()
            env = {**os.environ, "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"}

            def git(*args):
                return subprocess.run(
                    ["git", "-c", "user.name=Runtime Test", "-c", "user.email=runtime@example.invalid",
                     "-c", "core.autocrlf=false", "-c", "commit.gpgsign=false", *args],
                    cwd=mount, env=env, check=True, capture_output=True, text=True,
                )

            def write(path, content):
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content)

            git("init", "-q")
            for src, dest in old_map.items():
                write(mount / src, old_files[src])
                write(root / dest, old_files[src])
            git("add", "--", *old_map)
            git("commit", "-qm", "Fixture old bundle")
            git("tag", "v16")
            for src in new_map:
                write(mount / src, (FACTORY / src).read_bytes())
            git("add", "--", *new_map)
            git("commit", "-qm", "Fixture updated bundle")

            schedule = next(dest for dest in new_map.values()
                            if dest.startswith("schedules/") and b"- **Status:**" in (root / dest).read_bytes())
            status = "- **Status:** active — fixture registration"
            recipe = (root / schedule).read_text(encoding="utf-8")
            (root / schedule).write_text("\n".join(status if line.startswith("- **Status:**") else line
                                                    for line in recipe.splitlines()) + "\n", encoding="utf-8")

            skills = root / ".agents/skills"
            skills.parent.mkdir()
            try:
                skills.symlink_to("../.claude/skills", target_is_directory=True)
            except OSError:
                pass  # Windows without symlink privileges still tests all copied files.

            def sync():
                result = subprocess.run([sys.executable, str(SYNC), "--from", "v16"],
                                        cwd=root, env=env, capture_output=True, text=True, timeout=60)
                self.assertEqual(result.returncode, 0, result.stderr)
                return result.stdout

            first = sync()
            self.assertIn("added: .claude/hooks/run-hook.py", first)
            self.assertIn("added: scripts/usage-log.py", first)
            self.assertFalse((root / "parker_config.json").exists())
            self.assertFalse((root / ".usage").exists())
            for src, dest in new_map.items():
                expected = (FACTORY / src).read_bytes()
                actual = (root / dest).read_bytes()
                if dest == schedule:
                    self.assertIn(status, actual.decode("utf-8"))
                    self.assertEqual(helpers["normalized"](expected), helpers["normalized"](actual))
                else:
                    self.assertEqual(actual, expected, dest)
            second = sync()
            self.assertIn("refreshed: 0   added: 0", second)
            self.assertNotIn("left alone", second)
            if skills.is_symlink():
                self.assertEqual(skills.resolve(), root / ".claude/skills")

            override = root / ".codex/config.toml"
            override.write_text("# Fixture team override\n", encoding="utf-8")
            deleted = root / ".claude/hooks/git-guard.py"
            deleted.unlink()
            preference = '{"run_id":"fixture","usage_logging":{"enabled":true}}'
            (root / "parker_config.json").write_text(preference)
            third = sync()
            self.assertEqual((root / "parker_config.json").read_text(), preference)
            self.assertEqual(override.read_text(), "# Fixture team override\n")
            self.assertFalse(deleted.exists())
            self.assertIn("left alone", third)
            self.assertIn(".codex/config.toml", third)
            self.assertIn("left deleted", third)
            self.assertIn(".claude/hooks/git-guard.py", third)


if __name__ == "__main__":
    unittest.main()
