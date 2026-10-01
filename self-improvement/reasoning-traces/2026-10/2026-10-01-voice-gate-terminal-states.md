---
trace_id: 2026-10-01-voice-gate-terminal-states
date_captured: 2026-10-01
source: chat
source_ref: An audit of how the shipped skills behave on a scaffolded, unbuilt brain found the creative skills' voice gate could loop forever; Anton approved a fix with a pass cap
trigger_type: correction
scope: skill
brand: global
team: product
confidence: strong
status: applied
target_surfaces:
  - .claude/agents/creative-voice-review.md
  - .claude/skills/scriptwriting/SKILL.md
  - .claude/skills/hooks/SKILL.md
  - .claude/skills/headlines/SKILL.md
  - .claude/skills/iterations/SKILL.md
  - .claude/skills/ai-ad-generation/SKILL.md
  - creative-strategy-context/ai-writing-tells.md
promotion_condition: already applied — explicit approval in the same session
---

**What happened:** Reading every skill that ships into a brain against a scaffolded, unbuilt brain showed that the five creative skills re-ran the voice review "until the verdict is `ships`," while the reviewer's read-aloud pass forces `flagged` on copy that is clean but generic. The doctrine already said the cause is upstream (a thin voice profile) and that more scrubbing can't fix it, so with no voice corpus the loop had no exit.

**Decision context:** I proposed a third verdict owned by the independent reviewer and argued against a plain retry cap, because the v9 history shows the model treats any escape hatch as permission to skip a gate. Anton wanted a cap of about three passes as well, rather than an open-ended loop. Both landed, shaped so neither weakens the gate: `needs-corpus` can only be returned when no fixable line flag remains, and the three-pass cap ends with the open flags shown as unresolved in the receipt, never as a pass. Re-runs hand the reviewer its last return so it verifies its own rewrites instead of re-reviewing from scratch, and it is told to put every real flag in the first pass.

**Why it matters:** A gate that cannot terminate either hangs the run or teaches the model to abandon the gate. Both are worse than an honest "these lines are clean but generic, here is the corpus that would fix it."

**Inferred rule:** Every review loop needs an end state for problems the loop can't fix. Give that end state to the independent reviewer, with a precondition that keeps it from swallowing fixable issues, and back it with a pass cap whose exit is visible in the output contract rather than silent.

**Scope judgment:** The five creative skills and the voice reviewer. The grounding gate has the same kind of gap when a pull it asks for can't be made (no Parker MCP connected), so a bounce can repeat with no end; that needs its own change and was left out of this one.
