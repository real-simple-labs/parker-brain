# Optional token usage logging

`scripts/usage-log.py` collects counters already written by Claude Code or Codex.
It makes no model calls, network requests, or Git commits. Both the factory and
new brand brains ship the hook wiring. Existing brains receive it through the
normal executable-layer sync; a retained settings override can prevent collection.

## Enable and save

Merge this option into the repository-root `parker_config.json`, preserving all
existing fields:

```json
{"usage_logging": {"enabled": true}}
```

Missing file, missing option, invalid config, or anything except literal `true`
means off. Off means no transcript reads, no `.usage` writes, and no context
injection. Onboarding and upgrades never enable it. Set it to `false` to stop
collection; existing records remain. Hooks still start a short Python process
when disabled, but do no accounting work. Approve the hook definitions in the
runtime before relying on them; Codex headless runs can skip unapproved hooks.

Hooks checkpoint at SessionStart, Stop, SubagentStop, and SessionEnd. While a turn
is running its counters can lag; export re-reads known transcripts to catch up.
Only transcripts explicitly supplied by hooks are registered. There is no scan
of the user's session history, and hidden internal runtime work is not assumed
to be covered. Ephemeral runs without transcripts cannot be counted this way.

From the repository root, before confirming a batch has synced (on Windows, use
`py -3` in place of `python3`):

```bash
python3 scripts/usage-log.py export
python3 scripts/usage-log.py report
python3 scripts/usage-log.py report --build BUILD_RUN_ID
```

When enabled, `save-brain` and the build's final sync check run export before
confirming the files synced. Parker Desktop saves those exported files through
its existing sync; it does not run the export command itself. The collector
never stages, commits, pulls, or pushes. Factory and self-managed saves export
before their normal staging step. Commands are no-ops when disabled. Export
failures report an error; finish the normal save and surface missing telemetry
instead of retrying the build or blocking a turn over accounting.

- `.usage/.local/`: ignored checkpoints, a lock, and local transcript locations.
  Its self-ignoring `.gitignore` is created only when enabled. Never force-add it.
- `.usage/YYYY-MM-DD/<runtime>-<parent-session>/<actor>.json`: commit-ready schema
  v1 records, one file per actor, updated idempotently on export. The date is
  fixed on the first checkpoint. Main actor is `main`; child actors keep their
  IDs. Parent totals contain only the parent's requests. The report adds child
  totals once and groups by runtime, model, stage, prompt, and actor type.

Each public record contains counters, request hashes, runtime/version, session
and actor IDs, timestamps, explicit build labels, and coverage diagnostics.
It contains no messages, tool results, raw transcripts, credentials, or absolute
source paths. Model and prompt identifiers are metadata; treat the records as
repo-visible. `.usage` is diagnostic data, never marketing context to load into
routine prompts. Never ask another model to calculate token counts.

Stop hooks only update ignored checkpoints, so they cannot dirty a just-saved
working tree or restart the assistant. Tokens incurred after the final export
are exported at the next save. Abrupt exits are reconciled from known transcripts
at the next SessionStart/export on that machine. A different machine cannot
recover another machine's unexported checkpoints.

## Accounting rules

| Counter | Claude Code | Codex |
|---|---|---|
| Input | fresh + cache read + cache creation | reported input, already including cache |
| Uncached input | `input_tokens` | input minus reported cache read/write |
| Cache read | `cache_read_input_tokens` | `cached_input_tokens` |
| Cache creation | `cache_creation_input_tokens` | `cache_write_input_tokens` |
| Output | `output_tokens`, including thinking | `output_tokens`, including reasoning |
| Reasoning | optional thinking subset | reasoning subset; never add again |
| Total | normalized input + output | reported total, checked against input + output |

Claude streaming/replayed frames are deduplicated by response ID; the largest
observed counters for each response survive. Cache-duration subdivisions and
iteration breakdowns are not added to their parent counters. Codex cumulative
snapshots are differenced; repeated rate-limit snapshots do not count as new
requests. Prior checkpoints survive compaction/resume. Counter resets, history
gaps, and unknown fork boundaries are marked partial. A child excludes inherited
Claude response IDs using its parent transcript, or inherited Codex counters
using its creation/turn boundary. If that boundary is missing, the ambiguous
first snapshot is not charged to the child. Own Stop and parent SubagentStop
callbacks for the same Codex child share one record.

Absent counters stay `null`, never a guessed zero. Unknown thinking detail alone
does not invalidate known output totals. Coverage `observed_transcript` means
all recognized records in the available transcript were parsed; it is not a
provider billing reconciliation or a guarantee that every worker emitted a hook.
Malformed/unflushed lines and unavailable sources produce `partial` with reason
codes. Hooks fail open without returning instructions or requesting another turn.

Reports show raw usage and cache hit rates, not dollars: prices depend on runtime,
model, cache policy, and account. Cached input is real processed context but must
not be priced as fresh input. Compare equivalent builds before claiming a
single-agent counterfactual; review/rerun tokens measure work actually performed,
not automatically avoidable waste. Hook gaps and unattributed work must remain
visible when making that comparison.

## Build attribution

When logging is enabled, append one literal line to each worker's task, outside
the quoted prompt instructions. Use the existing setup `run_id`:

```text
PARKER_USAGE {"build_run_id":"BUILD_RUN_ID","stage":"generation","prompt_path":"parker-system/prompts/example.md","output_path":"sub-context-docs/example.md","attempt":1}
```

Allowed stages: `coordinator`, `generation`, `fidelity_review`, `retry`, and
`build_verification`. A fidelity review keeps its writer's prompt/output paths
and attempt number. A rewritten output is `retry` with attempt 2; its review is
`fidelity_review` with attempt 2. Do not derive these labels from task prose or
store brand names, freeform notes, or absolute paths in them. Untagged everyday
work is still counted, with stage `unattributed`. No marker is needed when off.

A parent session does not acquire a build label merely by delegating labelled
work. For a dedicated build coordinator, explicitly label its collected session:

```bash
python3 scripts/usage-log.py label --runtime codex --session SESSION_ID --metadata '{"build_run_id":"BUILD_RUN_ID","stage":"coordinator"}'
python3 scripts/usage-log.py export
```

Use `--runtime claude` for Claude Code and `--agent AGENT_ID` to repair a missing
worker label. Session/actor IDs are in exported records. This override labels
that actor's whole history, so never use it to attribute a mixed-purpose parent
session to one build. Leave that parent unattributed and report it separately.
If hooks have not collected the actor, the label command fails rather than
inventing a run. In a runtime without workers, inline review costs remain in the
parent session; they cannot be separated by this marker convention.

## Verification

Run `python3 -m unittest discover -s tests -v`. Sanitized fixtures cover both
formats, caches, replay, forks, compaction, resumes, incomplete records, concurrent
writes, disabled mode, privacy, and actual committed hook commands. Run
`python3 tests/probe_codex_runtime.py` for the installed Codex CLI against a local
fixture server: no inference or API key. The usage case verifies cached and
reasoning counts from real hook dispatch. Baseline: Codex 0.154.0; transcript
formats are internal and must be checked when runtimes change. Claude parsing
also uses sanitized shapes checked against local Claude Code transcripts.

References: [Claude hook payloads](https://code.claude.com/docs/en/hooks),
[Claude usage semantics](https://code.claude.com/docs/en/monitoring-usage), and
[Codex hook payloads and transcript stability](https://learn.chatgpt.com/docs/hooks).
