"""Sanitized accounting, hook, and Git regressions for optional usage logging."""
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import tomllib
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/usage-log.py"
spec = importlib.util.spec_from_file_location("usage_log", SCRIPT)
usage = importlib.util.module_from_spec(spec)
spec.loader.exec_module(usage)


def write_rows(path, rows):
    path.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")


def claude(mid="response1", output=10, **extra):
    return {"type": "assistant", "timestamp": "2026-09-10T10:00:00Z",
            "message": {"id": mid, "model": "fixture-model", "usage": {
                "input_tokens": 20, "cache_read_input_tokens": 60,
                "cache_creation_input_tokens": 30, "output_tokens": output,
                "output_tokens_details": {"thinking_tokens": 4},
                # These are subdivisions, not additional input.
                "cache_creation": {"ephemeral_1h_input_tokens": 30},
                "iterations": [{"input_tokens": 20, "output_tokens": output}],
                **extra}}}


def counts(inp=100, cached=60, output=10):
    return {"input_tokens": inp, "cached_input_tokens": cached,
            "cache_write_input_tokens": 0, "output_tokens": output,
            "reasoning_output_tokens": 4, "total_tokens": inp + output}


def codex(total=None, last=None, stamp="2026-09-10T10:00:00Z"):
    return {"type": "event_msg", "timestamp": stamp, "payload": {
        "type": "token_count", "info": {"total_token_usage": total or counts(),
                                          "last_token_usage": last or counts()}}}


class UsageLogging(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="parker usage ")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.source = self.root / "transcript.jsonl"
        self.config = self.root / "parker_config.json"
        self.config.write_text('{"usage_logging":{"enabled":true}}')
        write_rows(self.source, [claude()])
        self.payload = {"hook_event_name": "Stop", "session_id": "session1",
                        "transcript_path": str(self.source)}

    def run_cli(self, *args, payload=None):
        return subprocess.run([sys.executable, str(SCRIPT), "--root", str(self.root), *args],
                              input=json.dumps(payload if payload is not None else self.payload),
                              text=True, capture_output=True, timeout=15)

    def hook(self, runtime="claude", payload=None):
        result = self.run_cli("hook", "--runtime", runtime, payload=payload)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "")

    def exported(self):
        result = self.run_cli("export")
        self.assertEqual(result.returncode, 0, result.stderr)
        return [json.loads(p.read_text()) for p in (self.root / ".usage").glob("*/*/*.json")]

    def publish_from_other_machine(self, rows, day, runtime="claude", agent=None):
        with tempfile.TemporaryDirectory(prefix="usage remote fixture ") as tmp:
            root = Path(tmp).resolve()
            source = root / "transcript.jsonl"
            write_rows(source, rows)
            payload = {**self.payload, "transcript_path": str(source)}
            if agent:
                payload.update(hook_event_name="SubagentStop", agent_id=agent,
                               agent_transcript_path=str(source))
            snapshot = usage.collect(root, runtime, payload, root / ".usage/.local")
            snapshot["log_date"] = day
            usage.export(self.root, [snapshot])
            return snapshot

    def test_disabled_is_strict_and_does_not_read_transcript(self):
        variants = [None, "{bad", "[]", "{}", '{"usage_logging":true}',
                    '{"usage_logging":{"enabled":"true"}}',
                    '{"usage_logging":{"enabled":1}}',
                    '{"usage_logging":{"enabled":false}}']
        for body in variants:
            if body is None:
                self.config.unlink(missing_ok=True)
            else:
                self.config.write_text(body)
            self.source.unlink(missing_ok=True)
            self.hook(payload={"transcript_path": "/does/not/exist"})
            self.assertFalse((self.root / ".usage").exists())

    def test_claude_cache_and_streaming_deduplication(self):
        write_rows(self.source, [claude(output=2), claude(), claude(), claude(output=2)])
        self.hook()
        record, = self.exported()
        self.assertEqual(record["request_count"], 1)
        self.assertEqual(record["tokens"], dict(zip(usage.FIELDS, (110, 20, 60, 30, 10, 4, 120))))
        self.assertEqual(record["coverage"], "observed_transcript")

    def test_codex_cumulative_deltas_and_cache_subsets(self):
        write_rows(self.source, [codex(), codex(), codex(counts(250, 180, 25)), codex(counts(250, 180, 25))])
        self.hook("codex")
        record, = self.exported()
        self.assertEqual(record["request_count"], 2)
        self.assertEqual(record["tokens"]["input_tokens"], 250)
        self.assertEqual(record["tokens"]["uncached_input_tokens"], 70)
        self.assertEqual(record["tokens"]["total_tokens"], 275)
        self.assertEqual(record["tokens"]["reasoning_output_tokens"], 4)

    def test_codex_fork_excludes_inherited_events_and_counter_baseline(self):
        write_rows(self.source, [
            {"type": "session_meta", "payload": {"timestamp": "2026-09-10T09:00:00Z", "parent_thread_id": "parent"}},
            codex(counts(1000, 800, 100), stamp="2026-09-10T08:00:00Z"),
            codex(counts(1100, 860, 110)), codex(counts(1200, 920, 120))])
        result, issues = usage.parse_codex(self.source)
        self.assertFalse(issues)
        self.assertEqual(usage.totals(result)["total_tokens"], 220)

    def test_codex_fork_without_copied_events_uses_first_request(self):
        write_rows(self.source, [
            {"type": "session_meta", "payload": {"parent_thread_id": "parent", "timestamp": "2026-09-10T09:00:00Z"}},
            {"type": "turn_context", "timestamp": "2026-09-10T10:00:00Z", "payload": {"turn_id": "child-turn"}},
            codex(counts(1100, 860, 110), counts())])
        result, issues = usage.parse_codex(self.source)
        self.assertFalse(issues)
        self.assertEqual(usage.totals(result)["total_tokens"], 110)

    def test_codex_unknown_fork_does_not_count_inherited_snapshot(self):
        write_rows(self.source, [
            {"type": "session_meta", "payload": {"parent_thread_id": "parent"}}, codex()])
        result, issues = usage.parse_codex(self.source)
        self.assertEqual(result, [])
        self.assertIn("unknown_fork_or_reset_baseline", issues)

    def test_codex_own_stop_and_parent_stop_have_one_actor(self):
        write_rows(self.source, [
            {"type": "session_meta", "payload": {"id": "child1", "parent_thread_id": "session1",
             "timestamp": "2026-09-10T09:00:00Z", "cli_version": "0.154.0"}},
            {"type": "turn_context", "timestamp": "2026-09-10T10:00:00Z", "payload": {}}, codex()])
        self.hook("codex", {**self.payload, "session_id": "child1"})
        self.hook("codex", {**self.payload, "hook_event_name": "SubagentStop", "agent_id": "child1",
                            "agent_type": "review", "agent_transcript_path": str(self.source)})
        record, = self.exported()
        self.assertEqual(record["tokens"]["total_tokens"], 110)
        self.assertEqual((record["session_id"], record["agent_id"]), ("session1", "child1"))

    def test_codex_compacted_cumulative_history_is_not_added_twice(self):
        write_rows(self.source, [codex(), codex(counts(200, 120, 20))])
        self.hook("codex")
        for rows in ([codex(counts(200, 120, 20))], [codex(counts(300, 180, 30))]):
            write_rows(self.source, rows)
            record, = self.exported()
            self.assertEqual(record["tokens"]["total_tokens"], rows[-1]["payload"]["info"]["total_token_usage"]["total_tokens"])

    def test_placeholder_export_keeps_one_stable_filename(self):
        self.source.write_text("")
        self.hook()
        self.exported()
        write_rows(self.source, [claude()])
        record, = self.exported()
        self.assertEqual(record["tokens"]["total_tokens"], 120)

    def test_public_snapshot_survives_loss_of_local_state(self):
        self.hook()
        self.run_cli("label", "--runtime", "claude", "--session", "session1",
                     "--metadata", '{"stage":"coordinator","build_run_id":"build1"}')
        initial, = self.exported()
        for path in (self.root / ".usage/.local").glob("*.json"):
            path.unlink()
        write_rows(self.source, [claude("later")])
        self.hook()
        resumed, = self.exported()
        self.assertEqual(resumed["log_date"], initial["log_date"])
        self.assertEqual(resumed["request_count"], 2)
        self.assertEqual(resumed["attribution_override"]["build_run_id"], "build1")

    def test_recovery_unions_divergent_exports_without_a_transcript(self):
        self.publish_from_other_machine([claude("one"), claude("shared")], "2026-09-10")
        later = claude("three")
        later["timestamp"] = "2026-09-11T10:00:00Z"
        self.publish_from_other_machine([claude("shared"), later], "2026-09-11")
        self.source.unlink()
        for _ in range(2):
            self.hook()
            self.exported()
            state = json.loads((self.root / ".usage/.local/claude-session1-main.json").read_text())
            self.assertEqual(state["snapshot"]["request_count"], 3)
            self.assertEqual(state["snapshot"]["tokens"]["total_tokens"], 360)
            self.assertEqual(state["snapshot"]["log_date"], "2026-09-10")
            summary = json.loads(self.run_cli("report").stdout)
            self.assertEqual(summary["request_count"], 3)
            self.assertEqual(summary["tokens"]["total_tokens"], 360)
            self.assertEqual(summary["partial_runs"], 1)

    def test_synced_history_is_merged_with_existing_local_state(self):
        self.hook()
        remote = claude("remote")
        remote["timestamp"] = "2026-09-11T10:00:00Z"
        self.publish_from_other_machine([remote], "2026-09-11")
        self.source.unlink()
        self.hook()
        self.exported()
        state = json.loads((self.root / ".usage/.local/claude-session1-main.json").read_text())
        self.assertEqual(state["snapshot"]["request_count"], 2)
        summary = json.loads(self.run_cli("report").stdout)
        self.assertEqual(summary["request_count"], 2)
        self.assertEqual(summary["tokens"]["total_tokens"], 240)

    def test_duplicate_exports_preserve_streaming_maxima_cache_and_build_labels(self):
        marker = {"type": "user", "message": {"content":
            'PARKER_USAGE {"stage":"fidelity_review","build_run_id":"build1"}'}}
        # The older path has the fuller streaming frame, including an unlabeled
        # copy. Neither date nor label alone determines the best token counters.
        self.publish_from_other_machine([claude()], "2026-09-10", agent="child")
        self.publish_from_other_machine([marker, claude(output=5)], "2026-09-11", agent="child")
        summary = json.loads(self.run_cli("report", "--build", "build1").stdout)
        self.assertEqual(summary["request_count"], 1)
        self.assertEqual(summary["tokens"], dict(zip(usage.FIELDS, (110, 20, 60, 30, 10, 4, 120))))
        self.assertEqual(summary["by_role"]["subagent"]["total_tokens"], 120)
        self.assertEqual(summary["groups"][0]["cache_hit_percent"], 54.55)
        self.assertEqual(summary["unattributed_requests_all_runs"], 0)

    def test_codex_exports_with_overlapping_cumulative_intervals_count_once(self):
        first = codex()
        second = codex(counts(200, 120, 20), stamp="2026-09-10T11:00:00Z")
        third = codex(counts(300, 180, 30), stamp="2026-09-10T12:00:00Z")
        self.publish_from_other_machine([first, third], "2026-09-10", runtime="codex")
        # This machine missed the first cumulative event altogether.
        self.publish_from_other_machine([second, third], "2026-09-11", runtime="codex")
        self.source.unlink()
        for _ in range(2):
            self.hook("codex")
            self.exported()
            summary = json.loads(self.run_cli("report").stdout)
            self.assertEqual(summary["request_count"], 3)
            self.assertEqual(summary["tokens"], dict(zip(usage.FIELDS, (300, 120, 180, 0, 30, 4, 330))))
            self.assertEqual(summary["groups"][0]["cache_hit_percent"], 60)

    def test_codex_overlapping_exports_can_share_event_timestamps(self):
        first, second, third = codex(), codex(counts(200, 120, 20)), codex(counts(300, 180, 30))
        self.publish_from_other_machine([first, third], "2026-09-10", runtime="codex")
        self.publish_from_other_machine([second, third], "2026-09-11", runtime="codex")
        self.source.unlink()
        self.hook("codex")
        self.exported()
        summary = json.loads(self.run_cli("report").stdout)
        self.assertEqual(summary["request_count"], 3)
        self.assertEqual(summary["tokens"]["total_tokens"], 330)
        self.assertEqual(summary["tokens"]["cache_read_input_tokens"], 180)

    def test_duplicate_empty_exports_count_as_one_unknown_run(self):
        for day in ("2026-09-10", "2026-09-11"):
            self.publish_from_other_machine([], day)
        summary = json.loads(self.run_cli("report").stdout)
        self.assertEqual(summary["runs_without_usage"], 1)
        self.assertEqual(summary["partial_runs"], 1)
        self.assertIsNone(summary["tokens"]["total_tokens"])

    def test_terminal_checkpoint_still_recovers_late_streaming_counts(self):
        write_rows(self.source, [claude(output=5)])
        self.hook(payload={**self.payload, "hook_event_name": "SessionEnd"})
        self.exported()
        write_rows(self.source, [claude()])
        record, = self.exported()
        self.assertEqual(record["tokens"]["total_tokens"], 120)
        self.assertEqual(record["coverage"], "observed_transcript")

    def test_report_adds_parent_and_child_once_and_exposes_unknown_runs(self):
        self.hook()
        parent = self.source
        child = self.root / "child.jsonl"
        write_rows(child, [{"type":"user", "message":{"content":
            'PARKER_USAGE {"stage":"fidelity_review","build_run_id":"build1"}'}}, claude("child")])
        self.hook(payload={**self.payload, "hook_event_name": "SubagentStop", "agent_id": "child",
                           "agent_transcript_path": str(child), "transcript_path": str(parent)})
        self.hook(payload={"session_id": "missing"})
        self.exported()
        report = json.loads(self.run_cli("report").stdout)
        self.assertEqual(report["tokens"]["total_tokens"], 240)
        self.assertEqual(report["by_role"]["main"]["total_tokens"], 120)
        self.assertEqual(report["by_role"]["subagent"]["total_tokens"], 120)
        self.assertEqual(report["partial_runs"], 1)
        self.assertEqual(report["runs_without_usage"], 1)
        filtered = json.loads(self.run_cli("report", "--build", "build1").stdout)
        self.assertEqual(filtered["tokens"]["total_tokens"], 120)
        self.assertEqual(filtered["unattributed_requests_all_runs"], 1)

    def test_claude_fork_excludes_parent_response_ids(self):
        parent = self.root / "parent.jsonl"
        write_rows(parent, [claude("inherited")])
        write_rows(self.source, [claude("inherited"), claude("child")])
        self.hook(payload={**self.payload, "hook_event_name": "SubagentStop", "agent_id": "child",
                           "agent_type": "context-grounding-review", "transcript_path": str(parent),
                           "agent_transcript_path": str(self.source)})
        record, = self.exported()
        self.assertEqual(record["agent_id"], "child")
        self.assertEqual(record["parent_session_id"], "session1")
        self.assertEqual(record["request_count"], 1)

    def test_missing_cache_fields_are_unknown(self):
        row = claude()
        del row["message"]["usage"]["cache_read_input_tokens"]
        write_rows(self.source, [row])
        self.hook()
        record, = self.exported()
        self.assertIsNone(record["tokens"]["total_tokens"])
        self.assertEqual(record["coverage"], "partial")

    def test_unavailable_source_preserves_observed_counts(self):
        self.hook()
        self.source.unlink()
        record, = self.exported()
        self.assertEqual(record["tokens"]["total_tokens"], 120)
        self.assertIn("transcript_unavailable", record["issues"])

    def test_partial_line_recovers_after_flush(self):
        self.source.write_text(self.source.read_text() + '{"partial"')
        self.hook()
        record, = self.exported()
        self.assertIn("invalid_or_unflushed_json", record["issues"])
        write_rows(self.source, [claude()])
        record, = self.exported()
        self.assertEqual(record["coverage"], "observed_transcript")

    def test_compaction_keeps_prior_observed_requests(self):
        self.hook()
        write_rows(self.source, [claude("after-compaction")])
        record, = self.exported()
        self.assertEqual(record["request_count"], 2)

    def test_codex_reset_is_reported_and_does_not_subtract_usage(self):
        write_rows(self.source, [codex(counts(1000, 600, 100)), codex()])
        result, issues = usage.parse_codex(self.source)
        self.assertIn("counter_reset", issues)
        self.assertEqual(usage.totals(result)["total_tokens"], 1210)

    def test_codex_reset_can_revisit_an_old_counter_value(self):
        write_rows(self.source, [codex(), codex(counts(200, 120, 20)), codex()])
        self.hook("codex")
        for _ in range(2):
            record, = self.exported()
            self.assertEqual(record["tokens"]["total_tokens"], 330)
            self.assertIn("counter_reset", record["issues"])

    def test_resumed_actor_and_replayed_hook_are_idempotent(self):
        self.hook()
        first = self.exported()
        self.hook()
        self.assertEqual(first, self.exported())
        write_rows(self.source, [claude(), claude("resumed")])
        record, = self.exported()
        self.assertEqual(record["request_count"], 2)

    def test_marker_attributes_only_explicit_user_task(self):
        tag = {"build_run_id": "build1", "stage": "fidelity_review", "attempt": 2,
               "prompt_path": "parker-system/prompts/brand-profile/brand-identity-analysis.md",
               "output_path": "sub-context-docs/brand-identity.md"}
        write_rows(self.source, [{"type": "user", "message": {"content": "PARKER_USAGE " + json.dumps(tag)}}, claude()])
        self.hook()
        record, = self.exported()
        self.assertEqual(record["requests"][0]["attribution"], tag)
        self.assertEqual(self.run_cli("report", "--build", "build1").returncode, 0)

    def test_replayed_response_keeps_its_original_build_label(self):
        def marker(build):
            return {"type":"user", "message":{"content":
                "PARKER_USAGE " + json.dumps({"stage":"generation", "build_run_id":build})}}
        write_rows(self.source, [marker("first"), claude("one"), marker("second"), claude("one"), claude("two")])
        self.hook()
        record, = self.exported()
        self.assertEqual([r["attribution"]["build_run_id"] for r in record["requests"]], ["first", "second"])

    def test_export_contains_no_source_text_or_absolute_paths(self):
        row = claude()
        row["message"]["content"] = [{"type": "text", "text": "private-fixture-content"}]
        row["cwd"] = str(self.root)
        write_rows(self.source, [row])
        self.hook()
        body = json.dumps(self.exported())
        self.assertNotIn("private-fixture-content", body)
        self.assertNotIn(str(self.root), body)
        self.assertNotIn("transcript_path", body)

    def test_label_rejects_prose_and_escaping_paths(self):
        for invalid in ({"stage": "fidelity_review", "secret": "private"},
                        {"stage": "generation", "output_path": "../other.md"},
                        {"stage": "generation", "attempt": True},
                        {"stage": "not-a-stage"}):
            self.assertIsNone(usage.label(invalid))

    def test_concurrent_agents_and_exports_do_not_lose_records(self):
        processes = []
        for i in range(6):
            p = subprocess.Popen([sys.executable, str(SCRIPT), "--root", str(self.root), "hook", "--runtime", "claude"],
                                 stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            p.stdin.write(json.dumps({**self.payload, "session_id": f"session{i}"}))
            p.stdin.close()
            p.stdin = None
            processes.append(p)
        for p in processes:
            stdout, stderr = p.communicate(timeout=15)
            self.assertEqual((p.returncode, stdout, stderr), (0, "", ""))
        self.assertEqual(len(self.exported()), 6)

    def test_live_checkpoints_do_not_dirty_git(self):
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        (self.root / ".gitignore").write_text("parker_config.json\ntranscript.jsonl\n")
        subprocess.run(["git", "-C", str(self.root), "add", ".gitignore"], check=True)
        self.hook()
        status = subprocess.check_output(["git", "-C", str(self.root), "status", "--porcelain"], text=True)
        self.assertNotIn(".usage", status)
        self.exported()
        status = subprocess.check_output(["git", "-C", str(self.root), "status", "--porcelain"], text=True)
        self.assertIn(".usage", status)

    def test_desktop_style_sync_commits_only_exports_and_stays_clean_after_stop(self):
        fixture_env = {**os.environ, "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"}

        def git(*args):
            return subprocess.check_output([
                "git", "-C", str(self.root), "-c", "user.name=Usage Fixture",
                "-c", "user.email=usage@example.invalid", "-c", "commit.gpgsign=false",
                *args], text=True, env=fixture_env)

        git("init", "-q")
        git("remote", "add", "origin", "https://github.com/parker-brain/fixture")
        (self.root / ".gitignore").write_text("parker_config.json\ntranscript.jsonl\n")
        self.hook()
        self.exported()
        git("add", "-A")  # Simulate the app's own sync, not the collector.
        staged = git("diff", "--cached", "--name-only")
        self.assertIn(".usage/", staged)
        self.assertNotIn(".local", staged)
        git("commit", "-qm", "Fixture app sync")
        self.assertEqual(git("status", "--porcelain"), "")
        write_rows(self.source, [claude(), claude("after-save")])
        self.hook()
        self.assertEqual(git("status", "--porcelain"), "")
        record, = self.exported()
        self.assertEqual(record["tokens"]["total_tokens"], 240)
        self.assertIn(".usage/", git("diff", "--name-only"))
        self.assertEqual(git("diff", "--cached", "--name-only"), "")

    def test_actual_hook_commands_are_silent_and_do_not_read_payload_when_off(self):
        import shutil
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        (self.root / "scripts").mkdir()
        shutil.copyfile(SCRIPT, self.root / "scripts/usage-log.py")
        factory = SCRIPT.parents[1]
        for preference in (None, '{"usage_logging":{"enabled":false}}'):
            if preference is None:
                self.config.unlink(missing_ok=True)
            else:
                self.config.write_text(preference)
            for base in (factory, factory / "templates/brand-routines"):
                for runtime in ("claude", "codex"):
                    path = base / (("." if base == factory else "") + runtime)
                    config = (json.loads((path / "settings.json").read_text()) if runtime == "claude"
                              else tomllib.loads((path / "config.toml").read_text()))
                    for groups in config["hooks"].values():
                        for group in groups:
                            for hook in group["hooks"]:
                                if "usage-log.py" not in hook["command"]:
                                    continue
                                command = hook.get("commandWindows", hook["command"]) if os.name == "nt" else hook["command"]
                                result = subprocess.run(command, shell=True, cwd=self.root,
                                    input="invalid JSON: must not be read when disabled", text=True,
                                    capture_output=True, timeout=10)
                                self.assertEqual((result.returncode, result.stdout, result.stderr), (0, "", ""))
                                self.assertFalse((self.root / ".usage").exists())

    def test_committed_hook_commands_collect_from_nested_cwd(self):
        import shutil
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        (self.root / "scripts").mkdir()
        shutil.copyfile(SCRIPT, self.root / "scripts/usage-log.py")
        nested = self.root / "nested"
        nested.mkdir()
        factory = SCRIPT.parents[1]
        for base in (factory, factory / "templates/brand-routines"):
            claude_path = base / (".claude/settings.json" if base == factory else "claude/settings.json")
            codex_path = base / (".codex/config.toml" if base == factory else "codex/config.toml")
            for runtime, config in (("claude", json.loads(claude_path.read_text())),
                                    ("codex", tomllib.loads(codex_path.read_text()))):
                write_rows(self.source, [claude()] if runtime == "claude" else [codex()])
                for event in ("SessionStart", "Stop", "SubagentStop", "SessionEnd"):
                    hooks = [h for g in config["hooks"][event] for h in g["hooks"] if "usage-log.py" in h["command"]]
                    self.assertEqual(len(hooks), 1)
                    hook = hooks[0]
                    command = hook.get("commandWindows", hook["command"]) if os.name == "nt" else hook["command"]
                    payload = {**self.payload, "hook_event_name": event, "agent_id": "child",
                               "agent_transcript_path": str(self.source)}
                    result = subprocess.run(command, shell=True, cwd=nested, input=json.dumps(payload),
                                            capture_output=True, text=True, timeout=10)
                    self.assertEqual((result.returncode, result.stdout, result.stderr), (0, "", ""))
        records = self.exported()
        self.assertEqual({r["runtime"] for r in records}, {"claude", "codex"})

    def test_disabled_preserves_existing_records(self):
        self.hook()
        self.exported()
        files = {p: p.read_bytes() for p in (self.root / ".usage").rglob("*.json")}
        self.config.write_text('{"usage_logging":{"enabled":false}}')
        self.hook()
        self.run_cli("export")
        self.assertEqual(files, {p: p.read_bytes() for p in files})

    def test_usage_directory_symlink_cannot_escape_repo(self):
        other = self.root / "other"
        other.mkdir()
        root = self.root / "repo"
        root.mkdir()
        (root / "parker_config.json").write_text(self.config.read_text())
        try:
            (root / ".usage").symlink_to(other, target_is_directory=True)
        except OSError as error:
            self.skipTest(str(error))
        self.root = root
        result = self.run_cli("hook", "--runtime", "claude")
        self.assertEqual(result.returncode, 0)
        self.assertFalse(list(other.iterdir()))


if __name__ == "__main__":
    unittest.main()
