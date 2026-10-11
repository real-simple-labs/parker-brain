"""Automatic updates: what scripts/update-brain.py lets a brain take on its
own, how it keeps the ledger honest through a full update, and how a brain
recovers when a migration stops partway."""

import json
import os
from pathlib import Path
import re
import runpy
import subprocess
import sys
import tempfile
import unittest

from test_runtime_hooks import FACTORY

PLAN = FACTORY / "scripts/update-brain.py"
SYNC = FACTORY / "scripts/sync-executable-layer.py"
SKILL = "templates/brand-routines/claude/skills/demo/SKILL.md"
NO_OP = "# {v} — fixture\n\nNothing to do; the pin bump's re-sync delivers everything. Record `{v}`.\n"
SAFE = ("# {v} — fixture with steps\n\n**Auto-apply:** yes\n\n## Step 1 — add a file\n\n"
        "If `notes/{v}.md` is missing, create it.\n")
NEEDS_PERSON = ("# {v} — fixture that edits CLAUDE.md\n\n## Step 1 — show the team, then edit\n\n"
                "Show the team the new sentence before adding it to `CLAUDE.md`.\n")
LEDGER = """# Standard sync — the update ledger

## Where this brain stands

- **Factory remote:** https://example.invalid/parker-brain.git
- **Posture:** `{posture}`
- **Pinned release:** {pinned}
- **Migrations applied through:** {applied}
- **Last compared:** 2026-10-01 against {pinned}

## Offer history

No offers yet.
"""


class Brain:
    """A brand brain with a parker-system/ mount holding fixture releases."""

    def __init__(self, root: Path):
        self.root = root / "brain"
        self.factory = root / "factory"
        self.mount = self.root / "parker-system"
        self.factory.mkdir(parents=True)
        self.root.mkdir()
        self.env = {**os.environ, "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"}
        self.git("init", "-q", cwd=self.factory)
        self.migrations: dict[str, str] = {}

    def git(self, *args: str, cwd: Path | None = None) -> str:
        return subprocess.run(
            ["git", "-c", "user.name=Runtime Test", "-c", "user.email=runtime@example.invalid",
             "-c", "core.autocrlf=false", "-c", "commit.gpgsign=false",
             "-c", "advice.detachedHead=false", "-c", "protocol.file.allow=always", *args],
            cwd=cwd or self.mount, env=self.env, check=True, capture_output=True, text=True,
        ).stdout

    def release(self, version: str, migration: str) -> None:
        """Cut a factory release; the brain sees it once it fetches the tags."""
        self.migrations[version] = migration.format(v=version)
        for name, text in self.migrations.items():
            path = self.factory / "migrations" / f"{name}.md"
            path.parent.mkdir(exist_ok=True)
            path.write_text(text, encoding="utf-8")
        skill = self.factory / SKILL
        skill.parent.mkdir(parents=True, exist_ok=True)
        skill.write_text(f"demo skill {version}\n", encoding="utf-8")
        self.git("add", "-A", cwd=self.factory)
        self.git("commit", "-qm", f"Fixture {version}", cwd=self.factory)
        self.git("tag", version, cwd=self.factory)
        if self.mount.exists():
            self.git("fetch", "-q", "origin", "--prune", "--prune-tags", "--tags")

    def install(self, version: str, posture: str = "follow") -> None:
        """Pin the brain at `version`, as a build at that release leaves it."""
        if not self.mount.exists():
            self.git("clone", "-q", str(self.factory), str(self.mount), cwd=self.root)
        self.git("checkout", "-q", version)
        (self.root / "running-notes").mkdir(exist_ok=True)
        self.ledger.write_text(LEDGER.format(posture=posture, pinned=version, applied=version),
                               encoding="utf-8")
        (self.root / "parker_config.json").write_text(
            json.dumps({"brand_id": "42", "parker_brain_version": version}, indent=2) + "\n")
        skill = self.root / ".claude/skills/demo/SKILL.md"
        skill.parent.mkdir(parents=True, exist_ok=True)
        skill.write_text(f"demo skill {version}\n", encoding="utf-8")

    @property
    def ledger(self) -> Path:
        return self.root / "running-notes/standard-sync.md"

    def run(self, script: Path, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run([sys.executable, str(script), *args], cwd=self.root, env=self.env,
                              capture_output=True, text=True, timeout=60)

    def tool(self, *args: str) -> str:
        result = self.run(PLAN, *args)
        if result.returncode != 0:
            raise AssertionError(f"update-brain.py {' '.join(args)}: {result.stderr}")
        return result.stdout

    def plan(self) -> dict:
        return json.loads(self.tool("plan"))

    def field(self, name: str) -> str:
        return re.search(rf"\*\*{name}:\*\* (.*)", self.ledger.read_text(encoding="utf-8")).group(1)

    def update(self, to: str, migrations: list[str], stop_at: str | None = None) -> None:
        """Do what /update-brain does on a yes: move the pin, run and record
        each migration in order (stopping where one stops), re-sync, record the pin."""
        old = self.field("Pinned release")
        self.git("checkout", "-q", to)
        for version in migrations:
            if version == stop_at:
                break  # the migration stopped partway: it is not recorded
            self.tool("record-migration", version)
        synced = self.run(SYNC, "--from", old)
        if synced.returncode != 0:
            raise AssertionError(synced.stderr)
        self.tool("record-pin", to)


class UpdateBrain(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="parker update test ")
        self.brain = Brain(Path(self.tmp.name).resolve())

    def tearDown(self):
        self.tmp.cleanup()

    def test_a_safe_release_installs_on_its_own_and_keeps_team_edits(self):
        brain = self.brain
        brain.release("v1", NO_OP)
        brain.install("v1")
        brain.release("v2", NO_OP)
        brain.release("v3", SAFE)
        team_skill = brain.root / ".claude/skills/demo/SKILL.md"

        plan = brain.plan()
        self.assertEqual(plan["auto_target"], "v3", plan)
        self.assertEqual(plan["offer_target"], "v3")
        self.assertEqual(plan["why_not_auto"], [])
        self.assertIsNone(plan["stopped_at"])

        brain.update("v3", ["v2", "v3"])
        self.assertEqual(brain.field("Pinned release"), "v3")
        self.assertEqual(brain.field("Migrations applied through"), "v3")
        config = json.loads((brain.root / "parker_config.json").read_text())
        self.assertEqual(config, {"brand_id": "42", "parker_brain_version": "v3"})
        self.assertEqual(team_skill.read_text(encoding="utf-8"), "demo skill v3\n")
        settled = brain.plan()
        self.assertIsNone(settled["auto_target"])
        self.assertEqual(settled["mount_at"], "v3")
        self.assertEqual(settled["unfinished_migrations"], [])

        # A team edit survives the next automatic update untouched.
        team_skill.write_text("Fixture team edit\n", encoding="utf-8")
        brain.release("v4", NO_OP)
        self.assertEqual(brain.plan()["auto_target"], "v4")
        brain.update("v4", ["v4"])
        self.assertEqual(team_skill.read_text(encoding="utf-8"), "Fixture team edit\n")
        self.assertEqual(brain.field("Pinned release"), "v4")

    def test_it_stops_before_a_migration_that_needs_a_person(self):
        brain = self.brain
        brain.release("v1", NO_OP)
        brain.install("v1")
        brain.release("v2", NO_OP)
        brain.release("v3", NEEDS_PERSON)
        brain.release("v4", NO_OP)
        plan = brain.plan()
        self.assertEqual(plan["auto_target"], "v2")
        self.assertEqual(plan["offer_target"], "v4")
        self.assertEqual(plan["stopped_at"]["release"], "v3")
        self.assertEqual(plan["stopped_at"]["reason"], "its migration needs a person")

        brain.update("v2", ["v2"])
        after = brain.plan()
        self.assertIsNone(after["auto_target"])  # v3 waits for a person
        self.assertEqual(after["offer_target"], "v4")

    def test_an_interrupted_migration_blocks_the_next_update_until_it_finishes(self):
        brain = self.brain
        brain.release("v1", NO_OP)
        brain.install("v1")
        brain.release("v2", NO_OP)
        brain.release("v3", SAFE)
        # v3's migration stops partway: the pin and the sync still go ahead.
        brain.update("v3", ["v2", "v3"], stop_at="v3")
        self.assertEqual(brain.field("Pinned release"), "v3")
        self.assertEqual(brain.field("Migrations applied through"), "v2")

        brain.release("v4", NO_OP)
        plan = brain.plan()
        self.assertIsNone(plan["auto_target"])
        self.assertEqual([m["release"] for m in plan["unfinished_migrations"]], ["v3"])
        self.assertTrue(plan["unfinished_migrations"][0]["auto_apply"])
        self.assertTrue(any("didn't finish its migrations" in w for w in plan["why_not_auto"]))

        # No skipping: v4 can't be recorded while v3 is open, nor before the
        # mount reaches v4, even when someone moves the pin by hand.
        early = brain.run(PLAN, "record-migration", "v4")
        self.assertEqual(early.returncode, 3)
        self.assertIn("isn't part of it yet", early.stderr)
        brain.git("checkout", "-q", "v4")
        skipped = brain.run(PLAN, "record-migration", "v4")
        self.assertEqual(skipped.returncode, 3)
        self.assertIn("record v3 first", skipped.stderr)
        brain.git("checkout", "-q", "v3")
        self.assertEqual(brain.field("Migrations applied through"), "v2")

        # The next run finishes v3, then takes v4 on its own.
        brain.tool("record-migration", "v3")
        self.assertEqual(brain.plan()["auto_target"], "v4")
        brain.update("v4", ["v4"])
        self.assertEqual(brain.field("Migrations applied through"), "v4")

    def test_a_pin_moved_but_never_recorded_resumes_the_sync(self):
        brain = self.brain
        brain.release("v1", NO_OP)
        brain.install("v1")
        brain.release("v2", NO_OP)
        brain.git("checkout", "-q", "v2")  # the session died right after the checkout
        plan = brain.plan()
        self.assertEqual(plan["resume_sync_from"], "v1")
        self.assertEqual([m["release"] for m in plan["unfinished_migrations"]], ["v2"])
        self.assertIsNone(plan["auto_target"])

        brain.git("checkout", "-q", "v1")
        brain.ledger.write_text(brain.ledger.read_text().replace("**Pinned release:** v1",
                                                                 "**Pinned release:** v2"))
        behind = brain.plan()
        self.assertTrue(any("behind the recorded v2" in w for w in behind["why_not_auto"]))
        self.assertIsNone(behind["auto_target"])

    def test_record_pin_refuses_a_release_the_mount_is_not_on(self):
        brain = self.brain
        brain.release("v1", NO_OP)
        brain.install("v1")
        brain.release("v2", NO_OP)
        refused = brain.run(PLAN, "record-pin", "v2")
        self.assertEqual(refused.returncode, 3)
        self.assertIn("not checked out at v2", refused.stderr)
        self.assertEqual(brain.field("Pinned release"), "v1")
        self.assertEqual(json.loads((brain.root / "parker_config.json").read_text())
                         ["parker_brain_version"], "v1")

    def test_decoupled_opted_out_and_mid_build_brains_are_never_updated_on_their_own(self):
        brain = self.brain
        brain.release("v1", NO_OP)
        brain.install("v1", posture="own-factory")
        brain.release("v2", NO_OP)
        decoupled = brain.plan()
        self.assertEqual(decoupled["mode"], "own-factory")
        self.assertIsNone(decoupled["auto_target"])
        self.assertIn("decoupled", decoupled["why_not_auto"][0])

        brain.install("v1")
        self.assertEqual(brain.plan()["auto_target"], "v2")
        self.assertEqual(brain.tool("auto-update", "off").strip(), "automatic updates: off")
        self.assertIn("- **Posture:** `follow`\n- **Auto-update:** off\n",
                      brain.ledger.read_text(encoding="utf-8"))
        opted_out = brain.plan()
        self.assertFalse(opted_out["auto_update"])
        self.assertIsNone(opted_out["auto_target"])
        self.assertEqual(opted_out["offer_target"], "v2")
        brain.tool("auto-update", "on")
        self.assertEqual(brain.ledger.read_text(encoding="utf-8").count("Auto-update"), 1)
        self.assertEqual(brain.plan()["auto_target"], "v2")

        (brain.root / "BUILD-STATUS.md").write_text("# Build status\n")
        mid_build = brain.plan()
        self.assertIsNone(mid_build["auto_target"])
        self.assertTrue(any("BUILD-STATUS.md" in w for w in mid_build["why_not_auto"]))


class MigrationMarkers(unittest.TestCase):
    def test_every_shipped_migration_classifies_as_its_author_meant(self):
        auto_apply = runpy.run_path(str(PLAN))["auto_apply"]
        for path in sorted((FACTORY / "migrations").glob("v*.md")):
            text = path.read_text(encoding="utf-8")
            if re.search(r"(?im)^\**\s*Auto-apply:", text):
                continue  # an explicit marker says it all
            no_op = re.search(r"(?im)^\**\s*Nothing to do\b", text)
            steps = re.search(r"(?m)^(?:#{2,} |\d+\. )", text)
            self.assertEqual(auto_apply(text), bool(no_op and not steps), path.name)
        self.assertFalse(auto_apply((FACTORY / "migrations/v1.md").read_text(encoding="utf-8")))
        self.assertTrue(auto_apply((FACTORY / "migrations/v39.md").read_text(encoding="utf-8")))
        # v40 turns automatic updates on, so every team says yes to it first.
        self.assertFalse(auto_apply((FACTORY / "migrations/v40.md").read_text(encoding="utf-8")))
        self.assertFalse(auto_apply(NO_OP.format(v="v9") + "\n**Auto-apply:** no\n"))
        self.assertTrue(auto_apply(SAFE.format(v="v9")))
        self.assertFalse(auto_apply(NEEDS_PERSON.format(v="v9")))


if __name__ == "__main__":
    unittest.main()
