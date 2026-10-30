#!/usr/bin/env python3
"""PostToolUse hook: append every MCP tool call to a session pull log.

The grounding gate needs to verify that the data pulls behind a creative
output actually happened — self-reporting is not evidence, because a model
that fabricated a quote can also fabricate having pulled it. This hook is
the record the model cannot write: the harness fires it after every MCP
tool call, and `scripts/grounding-check.py` reads the log back.

The log lives in the OS temp directory, keyed by a hash of the repo path —
never inside the repo, never committed, never visible in any output. It is
plumbing for the reviewer, not a surface for humans.

The same call also clears the `.scaffolded` marker. The build reports every
phase to Parker with `update_parker_brain_setup_status`; the first time it
reports a phase after Phase 0 as completed (or the whole run as completed), the
brain has real content, so the marker that tells Parker's apps "nothing built
yet" comes off right here, in code, instead of waiting for the model to
remember at the end of a multi-hour build. A report the tool answered with an
error leaves the marker alone.

During a brain build (v45) the same call saves every Parker read into the
build's data folder, so the model never types a result into a file: output
tokens cost several times what input tokens cost, and a typed copy of a big
pull costs more than pulling it again. The folder must already exist with its
own `.gitignore` (the runner creates both before the first pull), so raw ad data
and customer text never reach the sync. In Claude Code (`--runtime claude`) a
large result then reaches the model as a short note: where the file is, its
size, its fields, and its first records. The model reads the rest from the file
by slices. Codex gets the file too, and the full result as before.
"""

import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import time


def log_path() -> str:
    key = hashlib.sha256(os.getcwd().encode()).hexdigest()[:16]
    return os.path.join(tempfile.gettempdir(), f"parker-pull-log-{key}.jsonl")


MARKER = Path(".scaffolded")
STATUS_TOOL = "update_parker_brain_setup_status"


def as_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def clears_marker(tool: str, tool_input) -> bool:
    """A setup-status report that means the build has written real content:
    a phase other than Phase 0 reported completed, or the whole run completed."""
    if not tool.endswith("__" + STATUS_TOOL) or not isinstance(tool_input, dict):
        return False
    mode = str(tool_input.get("mode", "")).lower()
    if mode == "complete":
        return str(tool_input.get("run_status", "")).lower() == "completed"
    if mode != "update_phase" or str(tool_input.get("phase_status", "")).lower() != "completed":
        return False
    if re.match(r"\s*phase\s*0(?!\d)", str(tool_input.get("phase_name", "")), re.IGNORECASE):
        return False
    index = as_int(tool_input.get("phase_index"))
    return index is not None and index >= 2  # phase 1 of the run is Phase 0


def reported_failure(response) -> bool:
    """True when the tool's response says the call failed. Claude Code only runs
    PostToolUse after a call succeeds; this covers runtimes that also run it for
    failures, and responses that carry the error as JSON text."""
    if isinstance(response, str):
        try:
            response = json.loads(response)
        except ValueError:
            return False
    if isinstance(response, list):
        return any(reported_failure(block.get("text")) for block in response
                   if isinstance(block, dict) and block.get("type") == "text")
    if not isinstance(response, dict):
        return False
    if response.get("isError") or response.get("is_error") or response.get("success") is False:
        return True
    if response.get("error"):
        return True
    return reported_failure(response.get("content")) if "content" in response else False


BUILD_STATUS = Path("BUILD-STATUS.md")
BUILD_DATA = Path("build-data")
PULLS = BUILD_DATA / "pulls"
PULL_LIST = BUILD_DATA / "pulls.md"

# Parker's read tools. Only their results are saved: a build reads them again.
# Setup, credential, status, and write tools never are.
SAVED_TOOLS = {
    "analyze_video_from_url", "brand_discovery", "check_northbeam_connection",
    "check_triple_whale_connection", "get_brand_persona", "list_custom_metrics",
    "lookup_post_purchase_survey", "search_and_manage_organic_social",
    "search_chat_history", "search_competitor_facebook_ads",
    "search_customer_reviews_semantic", "search_customer_reviews_sql",
    "search_facebook_ad_comments_semantic", "search_facebook_ad_comments_sql",
    "search_facebook_ads_semantic", "search_facebook_ads_sql",
    "search_google_ads_sql", "search_northbeam_attribution",
    "search_reddit_posts_and_comments", "search_swipe_file",
    "search_tiktok_ads_sql", "search_tiktok_videos",
    "search_triple_whale_attribution", "semantic_search_post_purchase_survey",
}

# A result up to this many characters (about 8,000 tokens) reaches the model
# whole: a smaller one costs less to carry than the extra turn a file read takes.
INLINE_MAX = 32000
PREVIEW_RECORDS = 5
PREVIEW_RECORD_CHARS = 500
PREVIEW_TEXT_CHARS = 2500
INPUT_CHARS = 600


def build_running() -> bool:
    """A build is under way and its data folder is ready and kept out of the sync."""
    return (BUILD_STATUS.is_file() and BUILD_DATA.is_dir() and not BUILD_DATA.is_symlink()
            and (BUILD_DATA / ".gitignore").is_file())


def tool_base(tool: str) -> str:
    return tool.rsplit("__", 1)[-1]


def response_text(response):
    """The text of a tool result: a string, a list of content blocks, or an
    object with a `content` list."""
    if isinstance(response, str):
        return response
    if isinstance(response, list):
        parts = [block["text"] for block in response if isinstance(block, dict)
                 and block.get("type") == "text" and isinstance(block.get("text"), str)]
        return "\n".join(parts) if parts else None
    if isinstance(response, dict):
        if "content" in response:
            return response_text(response["content"])
        return json.dumps(response, ensure_ascii=False)
    return None


def record_list(value):
    """The result's records: the result itself when it is a list of objects, or
    its longest list of objects at most two levels down. (key or None, records or None)"""
    def is_records(item):
        return isinstance(item, list) and item and all(isinstance(x, dict) for x in item)
    if is_records(value):
        return None, value
    if not isinstance(value, dict):
        return None, None
    found = [(k, v) for k, v in value.items() if is_records(v)]
    if not found:
        found = [(f"{k}.{k2}", v2) for k, v in value.items() if isinstance(v, dict)
                 for k2, v2 in v.items() if is_records(v2)]
    return max(found, key=lambda kv: len(kv[1])) if found else (None, None)


def rest_of(parsed, key, count: int):
    """Everything in the result but its records, whole: the records' place holds
    a short marker, so no field (an author, a page offset, a total) is lost."""
    if not key or not isinstance(parsed, dict):
        return {}
    rest = dict(parsed)
    top, _, inner = key.partition(".")
    marker = f"<{count} records, one per line below>"
    if inner:
        rest[top] = {**rest[top], inner: marker}
    else:
        rest[top] = marker
    return rest


def one_line(value, limit: int) -> str:
    text = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    return text if len(text) <= limit else text[:limit] + "…"


def next_file(tool: str, suffix: str):
    """Claim the next numbered file; two calls at once never share one."""
    PULLS.mkdir(exist_ok=True)
    number = sum(1 for _ in PULLS.iterdir()) + 1
    for _ in range(1000):
        path = PULLS / f"{number:04d}-{tool}{suffix}"
        try:
            return path, open(path, "x", encoding="utf-8")
        except FileExistsError:
            number += 1
    raise OSError("no free pull file name")


def save_pull(tool: str, tool_input, text: str):
    """Write the result to its file and list it. Returns the note facts."""
    try:
        parsed = json.loads(text)
    except ValueError:
        parsed = None
    key, records = record_list(parsed)
    meta = {}
    stamp = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())
    if records is not None:
        meta = rest_of(parsed, key, len(records))
        header = {"_pull": {"tool": tool, "input": tool_input, "saved": stamp,
                            "records": len(records), "records_from": key}, "_meta": meta}
        path, f = next_file(tool, ".jsonl")
        with f:
            f.write(json.dumps(header, ensure_ascii=False) + "\n")
            for record in records:
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
    else:
        path, f = next_file(tool, ".json" if parsed is not None else ".txt")
        with f:
            # One value per line, so a search or a line range returns a slice.
            f.write(json.dumps(parsed, ensure_ascii=False, indent=1) if parsed is not None else text)
    size = path.stat().st_size
    count = f"{len(records):,} records, one per line after a header line" if records is not None else "not split into records"
    line = (f"- `{path.as_posix()}` · `{tool}` · {count} · {size / 1024:,.0f} KB · {stamp}"
            f" · input: `{one_line(tool_input, INPUT_CHARS).replace('`', chr(39))}`\n")
    new = not PULL_LIST.exists()
    with open(PULL_LIST, "a", encoding="utf-8") as f:
        if new:
            f.write("# Parker pulls of this build\n\nThe build's hook saves every Parker read here by itself, one line per file. "
                    "Check it before any pull.\n\n")
        f.write(line)
    return path, size, key, records, parsed, meta


def note_for(path, size, records, parsed, meta, text) -> str:
    where = (f"Parker's result was saved in full to `{path.as_posix()}` ({size / 1024:,.0f} KB"
             + (f", {len(records):,} records" if records is not None else "") + "; listed in "
             "`build-data/pulls.md`). Only its start is shown here, to save tokens. Read what this "
             "doc needs from the file: search it for ids, products, dates, or words, or read line "
             "ranges. Read all of it, part by part, only when the doc needs every record (a count, "
             "a classification, a corpus). Never type it into another file.")
    if records is not None:
        fields = sorted({k for r in records[:50] for k in r})
        lines = [where, "", "One record per line after the header line. Fields: " + ", ".join(fields) + "."]
        if meta:
            lines.append("The rest of the result (whole in the file's header line"
                         + (", cut here" if len(one_line(meta, 10**9)) > 1500 else "") + "): " + one_line(meta, 1500))
        lines.append(f"The first {min(PREVIEW_RECORDS, len(records))} records:")
        lines += [one_line(r, PREVIEW_RECORD_CHARS) for r in records[:PREVIEW_RECORDS]]
        return "\n".join(lines)
    return where + "\n\nThe start of the result:\n" + text[:PREVIEW_TEXT_CHARS]


def shaped(response, note: str):
    """The note in the shape the tool returned, or None to leave the result as it is."""
    if isinstance(response, str):
        return note
    if isinstance(response, list):
        return [{"type": "text", "text": note}]
    if isinstance(response, dict) and isinstance(response.get("content"), list):
        out = {k: v for k, v in response.items() if k != "structuredContent"}
        out["content"] = [{"type": "text", "text": note}]
        return out
    return None


def keep_for_build(tool: str, tool_input, response, rewrite: bool):
    """Save a Parker read during a build. Returns the replacement output or None."""
    if tool_base(tool) not in SAVED_TOOLS or not build_running() or reported_failure(response):
        return None
    text = response_text(response)
    if not text:
        return None
    path, size, _key, records, parsed, meta = save_pull(tool_base(tool), tool_input, text)
    if not rewrite or len(text) <= INLINE_MAX:
        return None
    return shaped(response, note_for(path, size, records, parsed, meta, text))


def clear_marker() -> None:
    try:
        if MARKER.is_symlink() or MARKER.is_file():
            MARKER.unlink()
    except OSError:
        pass


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        return
    tool = payload.get("tool_name", "")
    if not tool.startswith("mcp__"):
        return
    if clears_marker(tool, payload.get("tool_input")) \
            and not reported_failure(payload.get("tool_response")):
        clear_marker()
    entry = {
        "ts": int(time.time()),
        "session": payload.get("session_id", ""),
        "tool": tool,
    }
    # Keep a hint of what was pulled without storing full payloads: the
    # input's short string values name the query/brand/ad without bulk.
    tool_input = payload.get("tool_input") or {}
    if isinstance(tool_input, dict):
        hints = {
            k: v for k, v in tool_input.items()
            if isinstance(v, (str, int, float)) and len(str(v)) <= 120
        }
        if hints:
            entry["input"] = hints
    try:
        with open(log_path(), "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
    except OSError:
        pass
    # Saving is best effort: a failure here must never cost the person the result.
    try:
        rewrite = "--runtime" in sys.argv and sys.argv[sys.argv.index("--runtime") + 1:][:1] == ["claude"]
        replacement = keep_for_build(tool, payload.get("tool_input"), payload.get("tool_response"), rewrite)
    except Exception:
        replacement = None
    if replacement is not None:
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PostToolUse", "updatedMCPToolOutput": replacement}}))


if __name__ == "__main__":
    main()
