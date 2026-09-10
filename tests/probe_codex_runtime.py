#!/usr/bin/env python3
"""Offline integration: real Codex, fixed local responses, temporary brand files.

Run with Codex 0.154.0+: python3 tests/probe_codex_runtime.py
No model inference, API key, customer account, or external server is used.
The probe explicitly trusts only the fixture's inspected hook definitions.
"""

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import tempfile
import threading

from test_runtime_hooks import make_brand


def probe(case, codex):
    with tempfile.TemporaryDirectory(prefix="parker-codex-probe-") as directory:
        root = Path(directory).resolve()
        brand = root / "brand"
        brand.mkdir()
        make_brand(brand)
        subprocess.run(["git", "init", "-q", str(brand)], check=True)
        requests = []
        nested = case == "nested-brand-edit"
        target = "parker-system/probe.md" if case != "nested-brand-edit" else "probe.md"
        patch = f"*** Begin Patch\n*** Add File: {target}\n+fixture\n*** End Patch\n"
        command = None
        if case == "shell-write":
            command = "printf fixture > parker-system/probe.md"
        elif case == "indirect-write":
            command = "python3 -c " + shlex.quote("from pathlib import Path; Path('parker-system/probe.md').write_text('fixture')")
        elif case == "read-mount":
            command = "cat parker-system/source.md"

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def do_POST(self):
                requests.append(json.loads(self.rfile.read(int(self.headers["Content-Length"]))))
                if len(requests) == 1:
                    if command:
                        item = {"id": "fc_fixture", "type": "function_call", "call_id": "call_fixture", "name": "exec_command", "arguments": json.dumps({"cmd": command, "login": False})}
                    else:
                        item = {"id": "fc_fixture", "type": "custom_tool_call", "call_id": "call_fixture", "name": "apply_patch", "input": patch}
                else:
                    item = {"id": "msg_fixture", "type": "message", "role": "assistant", "content": [{"type": "output_text", "text": "fixture complete", "annotations": []}]}
                item["status"] = "completed"
                response = {"id": f"resp_{len(requests)}", "object": "response", "created_at": 0, "status": "completed", "model": "gpt-5.5", "output": [item], "usage": {"input_tokens": 1, "output_tokens": 1, "total_tokens": 2}}
                events = [
                    {"type": "response.created", "response": {**response, "status": "in_progress", "output": []}},
                    {"type": "response.output_item.added", "output_index": 0, "item": item},
                    {"type": "response.output_item.done", "output_index": 0, "item": item},
                    {"type": "response.completed", "response": response},
                ]
                stream = "".join("event: " + e["type"] + "\ndata: " + json.dumps(e) + "\n\n" for e in events).encode()
                self.send_response(200)
                self.send_header("Content-Type", "text/event-stream")
                self.send_header("Content-Length", str(len(stream)))
                self.end_headers()
                self.wfile.write(stream)

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        threading.Thread(target=server.serve_forever, daemon=True).start()
        home = root / "runtime-home"
        home.mkdir()
        (home / "config.toml").write_text(
            'model = "gpt-5.5"\nmodel_provider = "fixture"\napproval_policy = "never"\n'
            '[model_providers.fixture]\nname = "Local fixture"\n'
            f'base_url = "http://127.0.0.1:{server.server_port}/v1"\n'
            'wire_api = "responses"\nrequires_openai_auth = false\n'
            f'[projects.{json.dumps(str(brand))}]\ntrust_level = "trusted"\n'
        )
        cwd = brand / "sub-context-docs" if nested else brand
        args = [codex, "-C", str(cwd), "--strict-config", "--dangerously-bypass-hook-trust", "exec", "--json", "--ephemeral", "Offline fixture test."]
        if case == "legacy-patch":
            args[1:1] = ["--sandbox", "workspace-write"]
        try:
            result = subprocess.run(args, env={**os.environ, "CODEX_HOME": str(home)}, input="", text=True, capture_output=True, timeout=40)
        finally:
            server.shutdown()
            server.server_close()
        assert result.returncode == 0, (case, result.stdout, result.stderr)
        assert len(requests) == 2, (case, requests, result.stderr)
        feedback = json.dumps([item for item in requests[1].get("input", []) if item.get("type") in {"function_call_output", "custom_tool_call_output"}])
        assert (cwd / target).exists() == nested, (case, result.stdout, result.stderr)
        # The entire generated table must be directly visible, not spilled.
        visible = json.dumps(requests[0].get("input", []), ensure_ascii=False)
        source = (brand / "parker-system/creative-strategy-context/expertise-routing.md").read_text()
        for row in source.splitlines():
            if row.startswith("|") and ".md" in row:
                assert json.dumps(row, ensure_ascii=False)[1:-1] in visible, (case, row)
        assert "hook_outputs/" not in visible, case
        if case == "indirect-write":
            # The shell heuristic does not parse Python; native permissions must deny it.
            assert "Operation not permitted" in feedback or "Permission denied" in feedback, (result.stdout, result.stderr, feedback)
        if case == "read-mount":
            assert "fixture method" in feedback, (result.stdout, feedback)
        if case in {"native-patch", "shell-write", "legacy-patch"}:
            assert "read-only factory method mount" in feedback, (case, feedback)
        print(f"PASS {case}: expected file effect; full catalog delivered")


if __name__ == "__main__":
    executable = shutil.which("codex")
    if not executable:
        raise SystemExit("Install Codex CLI 0.154.0+ to run this optional probe.")
    if os.name == "nt":
        raise SystemExit("The integration probe uses POSIX shell fixtures; Windows runs the unit suite.")
    print(subprocess.check_output([executable, "--version"], text=True).strip())
    for case in ("native-patch", "shell-write", "indirect-write", "nested-brand-edit", "read-mount", "legacy-patch"):
        probe(case, executable)
