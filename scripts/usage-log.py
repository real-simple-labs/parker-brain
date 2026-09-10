#!/usr/bin/env python3
"""Opt-in local token accounting. No inference, networking, or Git mutations.

Enable with usage_logging.enabled = true in the repository's parker_config.json.
Hooks collect ignored checkpoints; `export` publishes metadata-only .usage records.
See system/usage-logging.md for accounting semantics and coverage limits.
"""
import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import time


FIELDS = ("input_tokens", "uncached_input_tokens", "cache_read_input_tokens",
          "cache_creation_input_tokens", "output_tokens", "reasoning_output_tokens",
          "total_tokens")
STAGES = {"coordinator", "generation", "fidelity_review", "retry", "build_verification"}
LABEL_KEYS = {"build_run_id", "stage", "prompt_path", "output_path", "attempt"}
ID = re.compile(r"[A-Za-z0-9_-]{1,160}\Z")
NAME = re.compile(r"[A-Za-z0-9_.:/-]{1,180}\Z")


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()[:24]


def identifier(value):
    return value if isinstance(value, str) and ID.fullmatch(value) else digest(str(value))


def name(value):
    return value if isinstance(value, str) and NAME.fullmatch(value) else None


def number(value):
    return value if type(value) is int and value >= 0 else None


def add(values):
    values = list(values)
    return sum(values) if all(v is not None for v in values) else None


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def configuration(root):
    try:
        config = read_json(root / "parker_config.json")
    except (OSError, ValueError):
        return {}
    return config if isinstance(config, dict) else {}


def enabled(root):
    option = configuration(root).get("usage_logging")
    return isinstance(option, dict) and option.get("enabled") is True


def safe_path(root, relative):
    """Keep generated files in this worktree, including through existing symlinks."""
    path = root / relative
    if not path.resolve().is_relative_to(root):
        raise ValueError("usage path escapes repository")
    return path


def atomic_json(path, value):
    body = json.dumps(value, ensure_ascii=True, sort_keys=True, indent=2) + "\n"
    if path.exists() and path.read_text(encoding="utf-8") == body:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".usage-write-", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            stream.write(body)
        os.replace(temporary, path)
    finally:
        Path(temporary).unlink(missing_ok=True)


@contextmanager
def locked(root):
    local = safe_path(root, ".usage/.local")
    local.mkdir(parents=True, exist_ok=True)
    # This file ignores itself too, so collecting alone leaves Git clean.
    safe_path(root, ".usage/.local/.gitignore").write_text("*\n", encoding="utf-8")
    with safe_path(root, ".usage/.local/lock").open("a+b") as stream:
        stream.seek(0)
        if not stream.read(1):
            stream.write(b"0")
            stream.flush()
        deadline = time.monotonic() + 5
        while True:
            try:
                if os.name == "nt":
                    import msvcrt
                    stream.seek(0)
                    msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except OSError:
                if time.monotonic() >= deadline:
                    raise TimeoutError("usage collector busy")
                time.sleep(0.02)
        try:
            yield local
        finally:
            if os.name == "nt":
                stream.seek(0)
                msvcrt.locking(stream.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(stream.fileno(), fcntl.LOCK_UN)


def rows(path, issues):
    try:
        with Path(path).open(encoding="utf-8") as stream:
            for line in stream:
                try:
                    row = json.loads(line)
                except ValueError:
                    issues.add("invalid_or_unflushed_json")
                    continue
                if isinstance(row, dict):
                    yield row
    except (OSError, UnicodeError):
        issues.add("transcript_unavailable")


def label(value):
    """Only explicit structured attribution is retained, never task prose."""
    if not isinstance(value, dict) or set(value) - LABEL_KEYS:
        return None
    if value.get("stage") not in STAGES:
        return None
    result = {"stage": value["stage"]}
    if "build_run_id" in value:
        if not isinstance(value["build_run_id"], str) or not ID.fullmatch(value["build_run_id"]):
            return None
        result["build_run_id"] = value["build_run_id"]
    for key in ("prompt_path", "output_path"):
        if key in value:
            p = value[key]
            if (not isinstance(p, str) or not NAME.fullmatch(p) or
                    p.startswith(("/", ".")) or ".." in p.split("/") or
                    ":" in p or not p.endswith(".md")):
                return None
            result[key] = p
    if "attempt" in value:
        if number(value["attempt"]) is None or value["attempt"] < 1:
            return None
        result["attempt"] = value["attempt"]
    return result


def message_label(content):
    texts = [content] if isinstance(content, str) else [
        part.get("text", "") for part in content or [] if isinstance(part, dict)]
    for text in texts:
        if not isinstance(text, str):
            continue
        for line in text.splitlines():
            if line.startswith("PARKER_USAGE "):
                try:
                    found = label(json.loads(line[len("PARKER_USAGE "):]))
                except ValueError:
                    continue
                if found:
                    return found
    return None


def claude_tokens(usage):
    fresh, read, write, output = (number(usage.get(k)) for k in
        ("input_tokens", "cache_read_input_tokens", "cache_creation_input_tokens", "output_tokens"))
    total_input = add((fresh, read, write))
    details = usage.get("output_tokens_details")
    if not isinstance(details, dict):
        details = {}
    return dict(zip(FIELDS, (total_input, fresh, read, write, output,
                            number(details.get("thinking_tokens")), add((total_input, output)))))


def codex_tokens(usage):
    inp, read, write, output, reasoning, total = (number(usage.get(k)) for k in
        ("input_tokens", "cached_input_tokens", "cache_write_input_tokens",
         "output_tokens", "reasoning_output_tokens", "total_tokens"))
    fresh = inp - read - write if None not in (inp, read, write) else None
    if fresh is not None and fresh < 0:
        fresh = None
    return dict(zip(FIELDS, (inp, fresh, read, write, output, reasoning,
                            total if total is not None else add((inp, output)))))


def validate_tokens(tokens, issues):
    if any(tokens[k] is None for k in FIELDS if k != "reasoning_output_tokens"):
        issues.add("missing_token_fields")
    inp, out = tokens["input_tokens"], tokens["output_tokens"]
    if inp is not None:
        cached = add((tokens["cache_read_input_tokens"], tokens["cache_creation_input_tokens"]))
        if cached is not None and cached > inp:
            issues.add("inconsistent_cache_counts")
        components = add((tokens["uncached_input_tokens"], tokens["cache_read_input_tokens"],
                          tokens["cache_creation_input_tokens"]))
        if components is not None and components != inp:
            issues.add("inconsistent_input_components")
    if out is not None and tokens["reasoning_output_tokens"] is not None:
        if tokens["reasoning_output_tokens"] > out:
            issues.add("inconsistent_reasoning_counts")
    if inp is not None and out is not None and tokens["total_tokens"] != inp + out:
        issues.add("inconsistent_total")


def request(key, timestamp, model, turn, tokens, attribution):
    try:
        timestamp = datetime.fromisoformat(timestamp.replace("Z", "+00:00")).astimezone(timezone.utc).isoformat()
    except (AttributeError, ValueError):
        timestamp = None
    return {"request_id": digest(key), "timestamp": timestamp, "model": name(model),
            "turn_id": identifier(turn) if turn else None,
            "tokens": tokens, "attribution": attribution}


def parse_claude(path, parent_path=None):
    issues, requests, attribution = set(), {}, None
    inherited = set()
    if parent_path:
        for row in rows(parent_path, issues):
            msg = row.get("message") or {}
            if row.get("type") == "assistant" and isinstance(msg, dict) and msg.get("id"):
                inherited.add(msg["id"])
    for row in rows(path, issues):
        msg = row.get("message") or {}
        if not isinstance(msg, dict):
            continue
        if row.get("type") == "user":
            attribution = message_label(msg.get("content")) or attribution
        if row.get("type") != "assistant" or not isinstance(msg.get("usage"), dict):
            continue
        mid = msg.get("id")
        if not isinstance(mid, str) or not mid:
            issues.add("missing_response_identity")
            continue
        if mid in inherited:
            continue
        tokens = claude_tokens(msg["usage"])
        item = request(mid, row.get("timestamp"), msg.get("model"),
                       row.get("turnId"), tokens, attribution)
        prior = requests.get(item["request_id"])
        # Streaming frames and replayed chunks can repeat one API response.
        if prior:
            for key in FIELDS:
                values = [v for v in (prior["tokens"][key], tokens[key]) if v is not None]
                item["tokens"][key] = max(values) if values else None
            item["timestamp"] = prior["timestamp"]
            item["attribution"] = prior["attribution"] or attribution
        requests[item["request_id"]] = item
    for item in requests.values():
        validate_tokens(item["tokens"], issues)
    return list(requests.values()), issues


def parse_codex(path, prior_requests=()):
    issues, requests = set(), []
    previous, created, turn, model, attribution = None, None, None, None, None
    child, epoch, own_turn = False, 0, False
    known = {r["request_id"]: r for r in prior_requests}
    for row in rows(path, issues):
        p = row.get("payload") or {}
        if not isinstance(p, dict):
            continue
        if row.get("type") == "session_meta":
            created = p.get("timestamp") or row.get("timestamp")
            child = bool(p.get("parent_thread_id") or
                         isinstance(p.get("source"), dict) and p["source"].get("subagent"))
        elif row.get("type") == "turn_context":
            model, turn = p.get("model"), p.get("turn_id")
            own_turn = bool(created and row.get("timestamp") and row["timestamp"] >= created)
        elif row.get("type") == "response_item" and p.get("role") == "user":
            attribution = message_label(p.get("content")) or attribution
        if row.get("type") != "event_msg" or p.get("type") != "token_count":
            continue
        info = p.get("info")
        if not isinstance(info, dict) or not isinstance(info.get("total_token_usage"), dict):
            continue
        current = info["total_token_usage"]
        stamp = row.get("timestamp")
        # Forks can retain earlier transcript events and cumulative counters.
        if child and created and stamp and stamp < created:
            previous = current
            continue
        if current == previous:
            continue
        if child and previous is None and not own_turn:
            previous = current
            issues.add("unknown_fork_or_reset_baseline")
            continue
        reset = previous is not None and any(number(value) is not None and
            number(previous.get(k)) is not None and value < previous[k] for k, value in current.items())
        if reset:
            epoch += 1
            issues.add("counter_reset")
        key = json.dumps([epoch, stamp, current], sort_keys=True)
        prior = known.get(digest(key))
        if prior:
            requests.append(prior)
            previous = current
            continue
        if previous is None and prior_requests:
            checkpoint = prior_requests[-1].get("source_totals")
            if checkpoint and all(number(current.get(k)) is not None and current[k] >= v
                                  for k, v in checkpoint.items()):
                previous = checkpoint
                issues.add("transcript_history_gap")
                if current == previous:
                    continue
            elif checkpoint:
                issues.add("counter_reset")
        if previous is None:
            delta = info.get("last_token_usage") if child else current
        else:
            delta = {key: number(value) - number(previous[key])
                     if number(value) is not None and number(previous.get(key)) is not None
                     else None for key, value in current.items()}
            if any(value is not None and value < 0 for value in delta.values()):
                delta = info.get("last_token_usage")
                issues.add("counter_reset")
        previous = current
        if not isinstance(delta, dict):
            issues.add("unknown_fork_or_reset_baseline")
            continue
        tokens = codex_tokens(delta)
        validate_tokens(tokens, issues)
        key = json.dumps([epoch, stamp, current], sort_keys=True)
        item = request(key, stamp, model, turn, tokens, attribution)
        item["source_totals"] = {k: v for k, v in current.items() if k in (
            "input_tokens", "cached_input_tokens", "cache_write_input_tokens", "output_tokens",
            "reasoning_output_tokens", "total_tokens") and number(v) is not None}
        requests.append(item)
    return requests, issues


def totals(requests):
    return {key: add(r["tokens"][key] for r in requests) if requests else None for key in FIELDS}


def session_info(path, runtime):
    if not path:
        return {}
    for index, row in enumerate(rows(path, set())):
        if runtime == "codex" and row.get("type") == "session_meta":
            return row["payload"] if isinstance(row.get("payload"), dict) else {}
        if runtime == "claude" and row.get("version"):
            return {"cli_version": row["version"]}
        if index >= 40:
            break
    return {}


def collect(root, runtime, payload, local):
    child = payload.get("hook_event_name") == "SubagentStop"
    source = payload.get("agent_transcript_path") if child else payload.get("transcript_path")
    info = session_info(source, runtime)
    # Some harnesses deliver both an own Stop and a parent's SubagentStop.
    # They must resolve to the same actor, regardless of delivery order.
    if runtime == "codex" and info.get("parent_thread_id") and info.get("id"):
        payload = {**payload, "session_id": info["parent_thread_id"], "agent_id": info["id"],
                   "agent_transcript_path": source, "hook_event_name": "SubagentStop"}
        child = True
    session = identifier(payload.get("session_id") or "unknown")
    agent = identifier(payload.get("agent_id")) if child else "main"
    key = f"{runtime}-{session}-{agent}"
    state_path = safe_path(root, f".usage/.local/{key}.json")
    previous = read_json(state_path) if state_path.exists() else {}
    old_snapshot = previous.get("snapshot", {})
    if not old_snapshot:
        # A resumed transcript may arrive on another machine without local state.
        published = sorted((root / ".usage").glob(f"*/{runtime}-{session}/{agent}.json"))
        if published:
            old_snapshot = read_json(published[0])
    parent = payload.get("transcript_path") if child else None
    issues = set()
    if source:
        if runtime == "claude":
            requests, issues = parse_claude(source, parent if parent != source else None)
        else:
            requests, issues = parse_codex(source, old_snapshot.get("requests", []))
    else:
        requests = []
        issues.add("transcript_unavailable")
    merged = {r["request_id"]: r for r in old_snapshot.get("requests", [])}
    for r in requests:
        if runtime == "claude" and r["request_id"] in merged:
            prior = merged[r["request_id"]]
            r["attribution"] = prior["attribution"] or r["attribution"]
            for field in FIELDS:
                values = [v for v in (r["tokens"][field], prior["tokens"][field]) if v is not None]
                r["tokens"][field] = max(values) if values else None
        merged[r["request_id"]] = r
    # Preserve transcript order when multiple snapshots share a timestamp.
    requests = sorted(merged.values(), key=lambda r: r["timestamp"] or "")
    issues.update(set(old_snapshot.get("issues", [])) & {
        "counter_reset", "unknown_fork_or_reset_baseline", "transcript_history_gap"})
    # A later checkpoint can repair a provisional streaming frame.
    issues.difference_update({"missing_token_fields", "inconsistent_cache_counts",
                              "inconsistent_reasoning_counts", "inconsistent_total",
                              "inconsistent_input_components"})
    for r in requests:
        validate_tokens(r["tokens"], issues)
    if not requests:
        issues.add("no_usage_observed")
    override = previous.get("attribution") or old_snapshot.get("attribution_override")
    if override:
        for r in requests:
            r["attribution"] = override
    observed = [r["timestamp"] for r in requests if r["timestamp"]]
    now = datetime.now(timezone.utc).isoformat()
    started = min(observed) if observed else None
    snapshot = {
        "schema_version": 1, "runtime": runtime, "session_id": session,
        "agent_id": agent, "agent_type": (name(payload.get("agent_type")) or old_snapshot.get("agent_type")) if child else "main",
        "runtime_version": name(info.get("cli_version")) or old_snapshot.get("runtime_version"),
        "parent_session_id": session if child else None,
        "started_at": started, "last_usage_at": max(observed) if observed else None,
        "log_date": old_snapshot.get("log_date") or (started or now)[:10],
        "coverage": "partial" if issues else "observed_transcript",
        "issues": sorted(issues), "request_count": len(requests),
        "tokens": totals(requests), "requests": requests,
        "attribution_override": override,
    }
    state = {"runtime": runtime, "payload": {
        k: payload[k] for k in ("hook_event_name", "session_id", "agent_id", "agent_type",
                               "transcript_path", "agent_transcript_path") if k in payload},
        "snapshot": snapshot}
    if override:
        state["attribution"] = override
    atomic_json(state_path, state)
    return snapshot


def reconcile(root, local):
    snapshots = []
    for path in sorted(local.glob("*.json")):
        state = read_json(path)
        snapshots.append(collect(root, state["runtime"], state["payload"], local))
    return snapshots


def export(root, snapshots):
    for snapshot in snapshots:
        day = snapshot["log_date"]
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", day):
            day = "undated"
        path = f".usage/{day}/{snapshot['runtime']}-{snapshot['session_id']}/{snapshot['agent_id']}.json"
        atomic_json(safe_path(root, path), snapshot)


def report(root, build):
    snapshots = [read_json(p) for p in sorted((root / ".usage").glob("*/*/*.json"))
                 if ".local" not in p.parts]
    groups, included, actors = {}, [], set()
    roles = {"main": [], "subagent": []}
    for snapshot in snapshots:
        if not build:
            actors.add((snapshot["runtime"], snapshot["session_id"], snapshot["agent_id"]))
        for r in snapshot["requests"]:
            attribution = r.get("attribution") or {}
            if build and attribution.get("build_run_id") != build:
                continue
            included.append(r)
            actors.add((snapshot["runtime"], snapshot["session_id"], snapshot["agent_id"]))
            roles["main" if snapshot["agent_id"] == "main" else "subagent"].append(r)
            key = (snapshot["runtime"], r["model"] or "unknown",
                   attribution.get("stage", "unattributed"),
                   attribution.get("prompt_path", ""), snapshot["agent_type"] or "subagent")
            groups.setdefault(key, []).append(r)
    result = []
    for key, requests in sorted(groups.items()):
        counts = totals(requests)
        inp, cached = counts["input_tokens"], counts["cache_read_input_tokens"]
        result.append(dict(zip(("runtime", "model", "stage", "prompt_path", "agent_type"), key),
                           request_count=len(requests), tokens=counts,
                           cache_hit_percent=round(100 * cached / inp, 2) if inp and cached is not None else None))
    print(json.dumps({"tokens": totals(included), "request_count": len(included),
                      "by_role": {role: totals(rs) for role, rs in roles.items()},
                      "unattributed_requests": sum(not r.get("attribution") for r in included),
                      "unattributed_requests_all_runs": sum(not r.get("attribution") for s in snapshots for r in s["requests"]),
                      "runs_without_usage": sum(not s["requests"] for s in snapshots),
                      "groups": result, "partial_runs": sum(s["coverage"] == "partial" for s in snapshots
                          if (s["runtime"], s["session_id"], s["agent_id"]) in actors)}, indent=2))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, help="repository root; defaults to nearest Git worktree")
    sub = ap.add_subparsers(dest="command", required=True)
    hook = sub.add_parser("hook")
    hook.add_argument("--runtime", choices=("claude", "codex"), required=True)
    sub.add_parser("export")
    summary = sub.add_parser("report")
    summary.add_argument("--build")
    annotate = sub.add_parser("label", help="attach explicit attribution to an already collected actor")
    annotate.add_argument("--runtime", choices=("claude", "codex"), required=True)
    annotate.add_argument("--session", required=True)
    annotate.add_argument("--agent", default="main")
    annotate.add_argument("--metadata", required=True, help="JSON containing only build attribution")
    args = ap.parse_args()
    if args.root:
        root = args.root.resolve()
    else:
        found = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True)
        if found.returncode:
            return 0
        root = Path(found.stdout.strip()).resolve()
    # Check before reading stdin, transcripts, or creating even a lock file.
    if not enabled(root):
        return 0
    try:
        if args.command == "report":
            report(root, args.build)
            return 0
        with locked(root) as local:
            if args.command == "hook":
                payload = json.load(sys.stdin)
                if not isinstance(payload, dict):
                    raise ValueError("invalid hook payload")
                if payload.get("hook_event_name") == "SessionStart":
                    reconcile(root, local)
                collect(root, args.runtime, payload, local)
            elif args.command == "export":
                export(root, reconcile(root, local))
            elif args.command == "label":
                attribution = label(json.loads(args.metadata))
                if not attribution:
                    raise ValueError("invalid attribution")
                path = safe_path(root, f".usage/.local/{args.runtime}-{identifier(args.session)}-{identifier(args.agent)}.json")
                state = read_json(path)
                state["attribution"] = attribution
                atomic_json(path, state)
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        # Never feed source text or exception payloads back into the conversation.
        print(f"usage-log: unavailable ({type(error).__name__})", file=sys.stderr)
        return 0 if args.command == "hook" else 1


if __name__ == "__main__":
    sys.exit(main())
