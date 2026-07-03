---
trace_id: 2026-07-03-bypass-hook-pull-log-bounce-traces
date_captured: 2026-07-03
source: chat
source_ref: Jimmy approved three of five proposed hardening ideas before his testing phase (fixtures deferred, script-coach-as-eval deferred)
trigger_type: product_rule
scope: system
brand: global
team: creative-strategy
confidence: strong
status: applied
target_surfaces:
  - templates/brand-routines/claude/hooks/craft-context.py
  - templates/brand-routines/claude/hooks/pull-log.py
  - templates/brand-routines/claude/settings.json
  - scripts/grounding-check.py
  - .claude/agents/context-grounding-review.md
  - .claude/skills/ (five creative skills, update-parker-skill)
promotion_condition: already applied — explicit approval in the same session
---

**What happened:** Before beginning his testing phase, Jimmy approved three hardening moves: closing the skill-bypass path, making bounce-learning real, and replacing self-reported pulls with a hook-written log. He deferred the red-team fixture set and the script-coach-as-gate-eval protocol.

**Decision context:** Three residual gaps in the gate system. (1) Skill bypass: the gates live inside skills, so a casual "write me a hook real quick" answered inline never fires them — the craft-context hook's injected instruction now states creative deliverables have no casual path and must route through their skill with both receipts, in both the script and the settings.json fallback string. (2) Bounce amnesia: bounces were used once and forgotten; each skill's gate step now captures every bounce through self-improvement-intake as a one-line trace (task shape + missed loads/pulls), and the birth principles carry it, so the routing layer learns instead of re-making the mistake for the gate to re-catch. (3) Self-reported pulls: the grounding reviewer trusted the skill's claim of which pulls it made — a model that fabricates a quote can fabricate a pull. New PostToolUse hook (pull-log.py, matcher mcp__.*) appends every MCP call to a JSONL log in the OS temp dir keyed by repo-path hash — never in the repo, never user-visible; grounding-check.py reads the last 24h back and the reviewer is instructed that the hook log outranks the skill's claims. Tested end to end: MCP calls logged with input hints, non-MCP calls ignored, grounding-check reads them back. Both hooks ship automatically: the runner stamps templates/brand-routines/claude/ wholesale and the propagate script rsyncs the hooks dir + settings.json as plain copies.

**Why it matters:** Each closes a spot where the system still depended on the model choosing to behave: the front door (skill routing), the memory (learning from catches), and the evidence chain (pull verification). The pull log is the pattern worth reusing: when the model's self-report is load-bearing, have the harness write the record instead.

**Inferred rule:** Trust boundaries in a gate system are only as strong as their evidence source. Prefer harness-written records over model self-reports for anything a reviewer must verify, and put the reminder that routes work into skills at the harness layer (hook injection) rather than hoping the skill triggers.

**Scope judgment:** The pull log records MCP calls only, with short input hints and no payloads, in the temp dir — invisible to users and outputs by design; it is reviewer plumbing. The bypass injection fires every turn as one added sentence, accepted as cheap. Deferred items (fixtures, script-coach-as-eval) remain open and good.

**Routing:** Hook script edited + new hook added + settings.json registration in templates/brand-routines/claude/; grounding-check session-pulls section; grounding agent pull-log precedence; bounce-trace sentence in the five creative skills' gate steps and the birth principles; propagate-craft's "context hook pair" wording updated to the hook bundle. Ship lists needed no change (hooks dir and settings ship wholesale).
