"""The brain scaffold: local init, the release manifest, and the push helper agree.

Builds a small fixture factory from the working tree (the bundle-map sources and
the seed templates), tags it, and scaffolds brand folders from it both ways.
"""

import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

from test_runtime_hooks import FACTORY

SCRIPT = FACTORY / "scripts/scaffold-brain.py"
SYNC = FACTORY / "scripts/sync-executable-layer.py"
ENV = {**os.environ, "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"}
GIT_ID = ["-c", "user.name=Scaffold Test", "-c", "user.email=scaffold@example.invalid",
          "-c", "core.autocrlf=false", "-c", "commit.gpgsign=false",
          "-c", "protocol.file.allow=always"]
IDENTITY = {"brand_name": 'Acme "Quote" \\ Co', "brand_id": "42",
            "repo_url": "https://github.com/parker-brain/acme", "created_at": "2026-09-25"}

spec = importlib.util.spec_from_file_location("scaffold_brain", SCRIPT)
scaffold = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scaffold)


def git(cwd, *args, stdin=None):
    return subprocess.run(["git", *GIT_ID, *args], cwd=cwd, env=ENV, check=True,
                          capture_output=True, input=stdin).stdout


def values():
    return scaffold.token_values(IDENTITY["brand_name"], IDENTITY["brand_id"],
                                 IDENTITY["repo_url"], IDENTITY["created_at"])


def run_script(*args, cwd=None):
    return subprocess.run([sys.executable, str(SCRIPT), *args], cwd=cwd, env=ENV,
                          capture_output=True, text=True, timeout=120)


class Scaffold(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix="parker scaffold test ")
        cls.root = Path(cls.temp.name).resolve()
        cls.factory = cls.root / "factory"
        cls.factory.mkdir()
        tracked = subprocess.check_output(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
            cwd=FACTORY, text=True).splitlines()
        needed = set(scaffold.bundle_map(dict.fromkeys(tracked))) | {s.source for s in scaffold.SEEDS}
        for rel in sorted(needed):
            (cls.factory / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(FACTORY / rel, cls.factory / rel)
        git(cls.factory, "init", "-q")
        git(cls.factory, "add", "-A")
        git(cls.factory, "commit", "-qm", "Fixture factory")
        git(cls.factory, "tag", "v99")
        cls.commit = git(cls.factory, "rev-parse", "HEAD").decode().strip()
        cls.bundle = scaffold.bundle_map(dict.fromkeys(needed))
        out = cls.root / "brain-scaffold.json"
        result = run_script("manifest", "--tag", "v99", "--factory", str(cls.factory), "--out", str(out))
        assert result.returncode == 0, result.stderr
        cls.manifest = json.loads(out.read_text(encoding="utf-8"))

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def brand(self, name):
        brand = self.root / name
        brand.mkdir()
        git(brand, "init", "-q")
        git(brand, "submodule", "add", "-q", str(self.factory), "parker-system")
        return brand

    def init(self, brand, *extra):
        return run_script("init", "--target", str(brand), "--brand-name", IDENTITY["brand_name"],
                          "--brand-id", IDENTITY["brand_id"], "--repo-url", IDENTITY["repo_url"],
                          "--created-at", IDENTITY["created_at"], *extra)

    def assert_init_ok(self, result):
        if os.name == "nt" and result.returncode == 1:
            self.assertIn(".agents/skills", result.stdout)  # symlinks need Developer Mode
        else:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    # ------------------------------------------------------------ manifest

    def test_manifest_carries_every_piece(self):
        tree = {item["path"]: item for item in self.manifest["tree"]}
        self.assertEqual(self.manifest["factory"], {
            "remote": scaffold.FACTORY_REMOTE, "tag": "v99", "commit": self.commit})
        self.assertEqual(tree["parker-system"], {
            "path": "parker-system", "mode": "160000", "type": "commit", "sha": self.commit})
        self.assertEqual(tree[".agents/skills"]["mode"], "120000")
        self.assertEqual(tree[".agents/skills"]["content"], "../.claude/skills")
        self.assertIn(f"url = {scaffold.FACTORY_REMOTE}", tree[".gitmodules"]["content"])
        for dest in self.bundle.values():
            self.assertIn(dest, tree)
        for seed in scaffold.SEEDS:
            self.assertIn(seed.dest, tree)
        for path in ("parker_config.json", ".scaffolded", "CLAUDE.md", ".claude/settings.json",
                     ".claude/skills/save-brain/SKILL.md", ".claude/skills/scriptwriting/SKILL.md",
                     "AGENTS.md", ".codex/config.toml", "scripts/voice-lint.py"):
            self.assertIn(path, tree)
        self.assertEqual(tree["scripts/voice-lint.py"]["mode"], "100755")
        self.assertEqual(tree["CLAUDE.md"]["mode"], "100644")
        self.assertNotIn("BUILD-STATUS.md", tree)
        self.assertNotIn("running-notes/refresh-schedule.md", tree)
        # the routine dream wins the name clash with the craft dream
        self.assertEqual(tree[".claude/skills/dream/SKILL.md"]["content"],
                         (FACTORY / "templates/brand-routines/claude/skills/dream/SKILL.md").read_text(encoding="utf-8"))

    def test_bundle_files_ship_verbatim(self):
        tree = {item["path"]: item for item in self.manifest["tree"]}
        for src, dest in self.bundle.items():
            self.assertEqual(tree[dest]["content"].encode("utf-8"), (FACTORY / src).read_bytes(), dest)
            for token in scaffold.TOKENS:
                self.assertNotIn(token, tree[dest]["content"], dest)

    def test_seeds_are_clean(self):
        tree = {item["path"]: item["content"] for item in self.manifest["tree"] if "content" in item}
        rendered = {path: scaffold.render(text, values(), path) for path, text in tree.items()}
        claude = rendered["CLAUDE.md"]
        self.assertNotIn("{{", claude)
        self.assertTrue(claude.startswith(f"# Parker — {IDENTITY['brand_name']}\n"))
        self.assertIn("**Not built yet.**", claude)
        self.assertIn("scaffolded, not built", claude)
        self.assertNotIn("BRAND_HARD_RULES", claude)
        for path in ("brand-lens.md", "running-notes/brand-rules.md", "running-notes/success-definition.md",
                     "running-notes/standard-sync.md", "README.md", "running-notes/missing-context.md",
                     "running-notes/brand-notes-from-org.md"):
            self.assertNotIn("{{", rendered[path], path)
            self.assertNotIn("> Status", rendered[path], path)
            self.assertNotIn("> Template for", rendered[path], path)
        sync = rendered["running-notes/standard-sync.md"]
        self.assertIn("- **Posture:** `follow`\n", sync)
        self.assertIn("- **Pinned release:** v99\n", sync)
        self.assertIn("- **Migrations applied through:** v99\n", sync)
        self.assertIn(f"- **Factory remote:** {scaffold.FACTORY_REMOTE}\n", sync)
        self.assertNotIn("own-factory", sync)
        self.assertIn("- **Primary campaign objective:** Not captured yet.",
                      rendered["running-notes/brand-rules.md"])
        self.assertIn(f"brand: {IDENTITY['brand_name']}\n", rendered["running-notes/missing-context.md"])
        self.assertIn(f"# Brand notes from org — {IDENTITY['brand_name']}",
                      rendered["running-notes/brand-notes-from-org.md"])
        log = rendered["running-notes/routine-log.md"]
        self.assertTrue(log.startswith(f"# Routine log — {IDENTITY['brand_name']}"))
        self.assertIn("{{routine}}", log)  # the entry-shape example stays an example
        config = json.loads(rendered["parker_config.json"])
        self.assertEqual(config, {
            "brand_id": "42", "brand_name": IDENTITY["brand_name"],
            "github_repo_url": IDENTITY["repo_url"], "parker_brain_version": "v99",
            "created_at": "2026-09-25", "usage_logging": {"enabled": False}})
        self.assertIn("release v99", rendered[".scaffolded"])

    def test_render_is_one_pass(self):
        sneaky = scaffold.token_values("{{BRAND_ID}}", "7", "", "2026-01-01")
        self.assertEqual(scaffold.render("{{BRAND_NAME}}/{{BRAND_ID}}", sneaky, "x.md"), "{{BRAND_ID}}/7")

    # ------------------------------------------------------------ init

    def test_init_scaffolds_idempotently_and_update_sync_sees_clean_copies(self):
        brand = self.brand("init brand")
        result = self.init(brand)
        self.assert_init_ok(result)
        self.assertIn("scaffold-brain init (v99)", result.stdout)
        self.assertTrue((brand / ".scaffolded").is_file())
        self.assertTrue((brand / ".claude/skills/get-started/SKILL.md").is_file())
        self.assertEqual(json.loads((brand / "parker_config.json").read_text(encoding="utf-8"))["brand_name"],
                         IDENTITY["brand_name"])
        if os.name != "nt":
            self.assertEqual(os.readlink(brand / ".agents/skills"), "../.claude/skills")
            self.assertTrue(os.access(brand / "scripts/voice-lint.py", os.X_OK))

        again = self.init(brand)
        self.assert_init_ok(again)
        self.assertIn("wrote 0 files", again.stdout)

        # The update sync must read every copy as untouched: nothing edited, nothing to refresh.
        sync = subprocess.run([sys.executable, str(SYNC), "--dry-run"], cwd=brand, env=ENV,
                              capture_output=True, text=True, timeout=120)
        self.assertEqual(sync.returncode, 0, sync.stderr)
        self.assertIn("would refresh: 0   would add: 0", sync.stdout)
        self.assertNotIn("left alone", sync.stdout)

        # The session-start hook reports a scaffolded brain on the standard layout.
        hook = subprocess.run([sys.executable, str(brand / ".claude/hooks/run-hook.py"), "session-start"],
                              cwd=brand, env=ENV, capture_output=True, text=True, timeout=30)
        context = json.loads(hook.stdout)["hookSpecificOutput"]["additionalContext"]
        self.assertIn("scaffolded, not built", context)
        self.assertIn("pinned to factory release v99", context)
        self.assertNotIn("decoupled", context)

    def test_init_matches_the_manifest(self):
        brand = self.brand("match brand")
        self.assert_init_ok(self.init(brand))
        for item in self.manifest["tree"]:
            path = brand / item["path"]
            if item["mode"] == "160000":
                self.assertEqual(git(path, "rev-parse", "HEAD").decode().strip(), item["sha"])
            elif item["mode"] == "120000":
                if os.name != "nt":
                    self.assertEqual(os.readlink(path), item["content"])
            elif item["path"] == ".gitmodules":
                self.assertIn('[submodule "parker-system"]', path.read_text(encoding="utf-8"))
            else:
                expected = scaffold.render(item["content"], values(), item["path"])
                self.assertEqual(path.read_bytes(), expected.encode("utf-8"), item["path"])

    def test_init_merges_an_existing_config_without_overwriting(self):
        brand = self.brand("config brand")
        (brand / "parker_config.json").write_text(json.dumps({
            "run_id": "run-1", "brand_id": "42", "usage_logging": {"enabled": True}}))
        result = self.init(brand)
        self.assert_init_ok(result)
        self.assertIn("parker_config.json: added", result.stdout)
        config = json.loads((brand / "parker_config.json").read_text(encoding="utf-8"))
        self.assertEqual(config["run_id"], "run-1")
        self.assertEqual(config["usage_logging"], {"enabled": True})
        self.assertEqual(config["parker_brain_version"], "v99")

    def test_init_refuses_a_built_brain_and_a_missing_mount(self):
        built = self.brand("built brand")
        (built / "CLAUDE.md").write_text("# Parker — a built brain\n")
        result = self.init(built)
        self.assertEqual(result.returncode, 2)
        self.assertIn("already built", result.stderr)
        self.assertFalse((built / ".scaffolded").exists())

        bare = self.root / "bare brand"
        bare.mkdir()
        git(bare, "init", "-q")
        result = self.init(bare)
        self.assertEqual(result.returncode, 2)
        self.assertIn("isn't attached", result.stderr)

    def test_init_repairs_a_scaffolded_brain(self):
        brand = self.brand("repair brand")
        self.assert_init_ok(self.init(brand))
        (brand / "running-notes/brand-rules.md").write_text("team notes\n")
        (brand / ".claude/skills/hooks/SKILL.md").unlink()
        result = self.init(brand)
        self.assert_init_ok(result)
        self.assertIn("wrote 1 files", result.stdout)
        self.assertEqual((brand / "running-notes/brand-rules.md").read_text(), "team notes\n")

    def test_restore_copies_repairs_edited_method_files_only(self):
        brand = self.brand("restore brand")
        self.assert_init_ok(self.init(brand))
        skill = brand / ".claude/skills/dream/SKILL.md"
        pristine = skill.read_bytes()
        skill.write_bytes(pristine.replace(b"the brand", b"Acme", 1))
        schedule = brand / "schedules/dream.md"
        armed = "\n".join(line.replace(line, "- **Status:** active (armed 2026-09-25)")
                          if line.startswith("- **Status:**") else line
                          for line in schedule.read_text(encoding="utf-8").split("\n"))
        schedule.write_text(armed, encoding="utf-8")
        (brand / "running-notes/brand-rules.md").write_text("team notes\n")
        (brand / "BUILD-STATUS.md").write_text("mid-build\n")
        (brand / ".scaffolded").unlink()  # a build started before the scaffold existed
        self.assertEqual(self.init(brand).returncode, 2)  # a plain init refuses it

        result = run_script("init", "--target", str(brand), "--restore-copies")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("restored 1 method files", result.stdout)
        self.assertEqual(skill.read_bytes(), pristine)
        self.assertIn("- **Status:** active (armed 2026-09-25)", schedule.read_text(encoding="utf-8"))
        self.assertEqual((brand / "running-notes/brand-rules.md").read_text(), "team notes\n")

    def test_init_flags_a_pin_that_moved_after_scaffolding(self):
        brand = self.brand("moved pin brand")
        self.assert_init_ok(self.init(brand))
        config = brand / "parker_config.json"
        config.write_text(config.read_text(encoding="utf-8").replace('"v99"', '"v98"'), encoding="utf-8")
        result = self.init(brand)
        self.assertEqual(result.returncode, 1)
        self.assertIn("records v98 but parker-system/ is at v99", result.stdout)
        restore = run_script("init", "--target", str(brand), "--restore-copies")
        self.assertEqual(restore.returncode, 2)

    def test_init_rejects_a_tag_the_mount_is_not_at(self):
        brand = self.brand("tag brand")
        mount = brand / "parker-system"
        tree = git(mount, "rev-parse", "HEAD^{tree}").decode().strip()
        other = git(mount, "commit-tree", tree, "-m", "Another release").decode().strip()
        git(mount, "tag", "v98", other)  # a real tag, just not the commit the mount is at
        wrong = self.init(brand, "--tag", "v98")
        self.assertEqual(wrong.returncode, 2)
        self.assertIn("--tag v98 is", wrong.stderr)
        self.assertFalse((brand / ".scaffolded").exists())
        self.assert_init_ok(self.init(brand, "--tag", "v99"))

    @unittest.skipIf(os.name == "nt", "POSIX symlinks and modes")
    def test_writes_ignore_planted_symlinks_and_keep_modes(self):
        brand = self.brand("mode brand")
        victim = self.root / "victim.txt"
        victim.write_text("keep me\n")
        for name in (".CLAUDE.md.scaffold-tmp", ".scaffolded.scaffold-tmp"):
            (brand / name).symlink_to(victim)
        config = brand / "parker_config.json"
        config.write_text('{"brand_id": "42"}')
        config.chmod(0o600)
        self.assert_init_ok(self.init(brand))
        self.assertEqual(victim.read_text(), "keep me\n")
        self.assertEqual(config.stat().st_mode & 0o777, 0o600)  # merged, still private
        umask = os.umask(0)
        os.umask(umask)
        self.assertEqual((brand / "CLAUDE.md").stat().st_mode & 0o777, 0o666 & ~umask)
        self.assertEqual((brand / "scripts/voice-lint.py").stat().st_mode & 0o777, 0o777 & ~umask)
        self.assertEqual(list(brand.rglob("*.scaffold-tmp")),
                         sorted(brand / n for n in (".CLAUDE.md.scaffold-tmp", ".scaffolded.scaffold-tmp")))

    def test_origin_credentials_never_reach_the_config(self):
        brand = self.brand("token brand")
        git(brand, "remote", "add", "origin", "https://x-access-token:ghs_secret@github.com/parker-brain/acme.git")
        result = run_script("init", "--target", str(brand), "--brand-name", "Acme", "--brand-id", "42",
                            "--created-at", "2026-09-25")
        self.assert_init_ok(result)
        config = json.loads((brand / "parker_config.json").read_text(encoding="utf-8"))
        self.assertEqual(config["github_repo_url"], "https://github.com/parker-brain/acme.git")
        self.assertEqual(scaffold.without_credentials("git@github.com:parker-brain/acme.git"),
                         "git@github.com:parker-brain/acme.git")

    def test_a_run_that_dies_partway_is_finished_by_the_next(self):
        """The failure lands after the bytes are written, where a plain write would
        leave a short file behind that the next run would keep as done."""
        brand = self.brand("crash brand")
        real_replace = os.replace

        def failing_replace(src, dst, *args, **kwargs):
            if Path(dst).name in ("CLAUDE.md", "parker_config.json"):
                raise OSError(28, "No space left on device")
            return real_replace(src, dst, *args, **kwargs)

        cwd = os.getcwd()
        self.addCleanup(os.chdir, cwd)
        with mock.patch.object(scaffold.os, "replace", failing_replace):
            try:
                code = scaffold.main(["init", "--target", str(brand), "--brand-name", "Acme",
                                      "--brand-id", "42", "--created-at", "2026-09-25"])
            finally:
                os.chdir(cwd)
        self.assertEqual(code, 2)
        self.assertTrue((brand / ".scaffolded").exists())  # the marker landed first
        self.assertFalse((brand / "CLAUDE.md").exists())   # no short file left behind
        self.assertEqual(list(brand.rglob("*.scaffold-tmp")), [])
        self.assert_init_ok(self.init(brand))  # the next run finishes the job
        self.assertEqual((brand / "CLAUDE.md").read_bytes(),
                         self.rendered_seed("CLAUDE.md", brand_name=IDENTITY["brand_name"]))
        json.loads((brand / "parker_config.json").read_text(encoding="utf-8"))

    def rendered_seed(self, path, brand_name):
        item = next(i for i in self.manifest["tree"] if i["path"] == path)
        vals = scaffold.token_values(brand_name, "42", IDENTITY["repo_url"], "2026-09-25")
        return scaffold.render(item["content"], vals, path).encode("utf-8")

    def test_an_unreadable_config_needs_attention(self):
        brand = self.brand("broken config brand")
        (brand / "parker_config.json").write_text('{"brand_id": "42", "run_')
        result = self.init(brand)
        self.assertEqual(result.returncode, 1)
        self.assertIn("needs attention: parker_config.json: isn't readable JSON", result.stdout)
        self.assertEqual((brand / "parker_config.json").read_text(), '{"brand_id": "42", "run_')

    def test_session_start_tells_an_unfinished_build_from_an_empty_brain(self):
        brand = self.brand("underway brand")
        self.assert_init_ok(self.init(brand))
        (brand / "BUILD-STATUS.md").write_text("Phase 1: 12 of 40\n")

        def context():
            hook = subprocess.run([sys.executable, str(brand / ".claude/hooks/run-hook.py"), "session-start"],
                                  cwd=brand, env=ENV, capture_output=True, text=True, timeout=30)
            return json.loads(hook.stdout)["hookSpecificOutput"]["additionalContext"]

        underway = context()
        self.assertIn("stopped partway", underway)
        self.assertIn("resume", underway)
        self.assertNotIn("scaffolded, not built", underway)
        # Mid-build the hook has usually cleared the marker already; the status file still speaks.
        (brand / ".scaffolded").unlink()
        self.assertIn("stopped partway", context())
        (brand / "BUILD-STATUS.md").unlink()
        built = context()
        self.assertNotIn("stopped partway", built)
        self.assertNotIn("scaffolded, not built", built)
        (brand / ".scaffolded").write_text("marker\n")
        self.assertIn("scaffolded, not built", context())
        # A run_id alone is setup tracking that started before any build work.
        config = brand / "parker_config.json"
        config.write_text(json.dumps({**json.loads(config.read_text(encoding="utf-8")), "run_id": "run-1"}))
        only_run_id = context()
        self.assertIn("scaffolded, not built", only_run_id)
        self.assertNotIn("stopped partway", only_run_id)

    def test_pull_log_clears_the_marker_once_a_real_phase_completes(self):
        brand = self.brand("phase brand")
        self.assert_init_ok(self.init(brand))
        marker = brand / ".scaffolded"
        tool = "mcp__Parker__update_parker_brain_setup_status"
        temp = str(self.root)  # the pull log lands in the temp dir; keep it in the fixture
        env = {**ENV, "TMPDIR": temp, "TEMP": temp, "TMP": temp}

        def report(tool_name, tool_input, cwd=brand):
            payload = {"session_id": "s1", "tool_name": tool_name, "tool_input": tool_input}
            hook = subprocess.run([sys.executable, str(brand / ".claude/hooks/run-hook.py"), "pull-log"],
                                  cwd=cwd, env=env, input=json.dumps(payload), capture_output=True,
                                  text=True, timeout=30)
            self.assertEqual(hook.returncode, 0, hook.stderr)

        def phase(name, index, status):
            return {"mode": "update_phase", "brand_id": "42", "run_id": "run-1",
                    "phase_name": name, "phase_index": index, "phase_status": status}

        keeps = [
            (tool, {"mode": "start", "brand_id": "42"}),
            (tool, phase("Phase 0 — Repo & Scaffold", 1, "in_progress")),
            (tool, phase("Phase 0 — Repo & Scaffold", 1, "completed")),
            (tool, phase("phase 0: setup", 3, "completed")),
            (tool, phase("Repo & Scaffold", 1, "completed")),  # index 1 is Phase 0, whatever its name
            (tool, phase("Phase 1A — Brand Foundation", 2, "in_progress")),
            (tool, phase("Phase 1A — Brand Foundation", 2, "failed")),
            (tool, {"mode": "complete", "brand_id": "42", "run_status": "failed"}),
            ("mcp__Parker__search_facebook_ads_sql", phase("Phase 1A — Brand Foundation", 2, "completed")),
            ("Bash", phase("Phase 1A — Brand Foundation", 2, "completed")),
            (tool, "not a dict"),
        ]
        for tool_name, tool_input in keeps:
            report(tool_name, tool_input)
            self.assertTrue(marker.exists(), (tool_name, tool_input))

        # The hook runs from the brand root, so a call made from a subfolder still clears it.
        (brand / "running-notes").mkdir(exist_ok=True)
        report("mcp__claude_ai_Parker__update_parker_brain_setup_status",
               phase("Phase 1A — Brand Foundation", "2", "completed"), cwd=brand / "running-notes")
        self.assertFalse(marker.exists())
        report(tool, phase("Phase 1B — Competitor Profiles", 3, "completed"))  # already gone: no error
        self.assertFalse(marker.exists())

        marker.write_text("marker\n")
        report(tool, {"mode": "complete", "brand_id": "42", "run_id": "run-1", "run_status": "completed"})
        self.assertFalse(marker.exists())

    # ------------------------------------------------------------ the backend path

    def test_manifest_builds_a_real_repo(self):
        """Replays the GitHub tree call with git's own index, then clones the result."""
        built = self.root / "from manifest"
        built.mkdir()
        git(built, "init", "-q")
        rendered = []
        for item in self.manifest["tree"]:
            if item["type"] == "commit":
                sha = item["sha"]
            else:
                content = scaffold.render(item["content"], values(), item["path"])
                sha = git(built, "hash-object", "-w", "--stdin", stdin=content.encode("utf-8")).decode().strip()
            rendered.append(f"{item['mode']} {sha}\t{item['path']}\n")
        git(built, "update-index", "--add", "--index-info", stdin="".join(rendered).encode("utf-8"))
        tree = git(built, "write-tree").decode().strip()
        commit = git(built, "commit-tree", tree, "-m", "Scaffold").decode().strip()
        git(built, "update-ref", "refs/heads/main", commit)

        listing = git(built, "ls-tree", "-r", "main").decode()
        self.assertIn(f"160000 commit {self.commit}\tparker-system", listing)
        self.assertIn("120000 blob", listing)

        clone = self.root / "manifest clone"
        git(self.root, "clone", "-q", "--branch", "main", str(built), str(clone))
        git(clone, "config", "submodule.parker-system.url", str(self.factory))
        git(clone, "submodule", "update", "--init", "-q", "parker-system")
        self.assertEqual(git(clone / "parker-system", "describe", "--tags", "--exact-match").decode().strip(), "v99")
        self.assertTrue((clone / ".scaffolded").is_file())
        json.loads((clone / "parker_config.json").read_text(encoding="utf-8"))

    def fake_github(self, parents=(), files=("README.md",)):
        calls = []

        def api(method, path, body=None):
            calls.append((method, path, body))
            if path == "/repos/o/r" and method == "GET":
                return 200, {"default_branch": "main"}
            if path.endswith("/git/ref/heads/main"):
                return 200, {"object": {"sha": "head0"}}
            if path.endswith("/git/commits/head0"):
                return 200, {"tree": {"sha": "tree0"}, "parents": list(parents)}
            if path.endswith("/git/trees/tree0"):
                return 200, {"tree": [{"path": f} for f in files]}
            if path.endswith("/git/trees"):
                return 201, {"sha": "tree1"}
            if path.endswith("/git/commits"):
                return 201, {"sha": "commit1"}
            if path.endswith("/git/refs/heads/main"):
                return 200, {"object": {"sha": "commit1"}}
            raise AssertionError(f"unexpected call {method} {path}")
        return api, calls

    def test_push_makes_three_writes_on_a_fresh_repo(self):
        api, calls = self.fake_github()
        sha = scaffold.apply_manifest(self.manifest, "o/r", values(), api)
        self.assertEqual(sha, "commit1")
        writes = [(m, p) for m, p, _ in calls if m != "GET"]
        self.assertEqual(writes, [("POST", "/repos/o/r/git/trees"), ("POST", "/repos/o/r/git/commits"),
                                  ("PATCH", "/repos/o/r/git/refs/heads/main")])
        tree = {item["path"]: item for item in calls[4][2]["tree"]}
        self.assertEqual(json.loads(tree["parker_config.json"]["content"])["brand_name"], IDENTITY["brand_name"])
        self.assertNotIn("{{BRAND_NAME}}", tree["CLAUDE.md"]["content"])
        self.assertEqual(calls[5][2]["parents"], ["head0"])
        self.assertEqual(calls[6][2], {"sha": "commit1", "force": False})

    def test_push_refuses_a_repo_that_is_not_fresh(self):
        for parents, files in ((("p",), ("README.md",)), ((), ("README.md", "CLAUDE.md"))):
            api, calls = self.fake_github(parents, files)
            with self.assertRaises(scaffold.ScaffoldError):
                scaffold.apply_manifest(self.manifest, "o/r", values(), api)
            self.assertFalse([c for c in calls if c[0] != "GET"])


if __name__ == "__main__":
    unittest.main()
