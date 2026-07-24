---
trace_id: 2026-07-24-voice-output-style-layer
date_captured: 2026-07-24
source: chat
source_ref: Jimmy — "I want to make sure that this output style, however they're doing it, is in the PARKERBRAIN. I think right now we have ours in our claude.md, and I think we need to change this to make it in the actual system instructions... Overall, again, I think Claude code is so dense and hard to read. I want the experience to feel like Claude Chat, which is way better"
trigger_type: user_directive
scope: system
brand: global
team: product
confidence: strong
status: applied
target_surfaces:
  - .claude/output-styles/parker.md
  - .claude/settings.json
  - templates/brand-routines/claude/settings.json
  - prompts/onboarding-runner.md
  - scripts/propagate-to-brand-brains.sh
  - .claude/skills/propagate-craft/SKILL.md
  - prompts/_parker-voice-block.md
  - CLAUDE.md
  - system/master-file-structure.md
  - system/parker-system-map.md
  - README.md
  - templates/brand-routines/claude/README.md
promotion_condition: already applied — proposed and approved in the same session (2026-07-24); propagation to standing brains deliberately held until the factory tree is committed clean
---

**What happened:** Jimmy saw a tweet about Claude Code output styles (a user-authored file in `.claude/output-styles/` whose body is injected into the system prompt) and directed that Parker's voice move from CLAUDE.md text into that layer, product-wide. His framing: Claude Code's default register is dense and hard to read; the Parker experience should feel like Claude Chat — plain, warm, conversational — for marketers who have never touched a terminal.

**Decision context:** Verified against the official docs (code.claude.com/docs/en/output-styles.md) before building: project-level `.claude/output-styles/` is supported, a checked-in `.claude/settings.json` with `"outputStyle": "Parker"` activates it for everyone who opens the repo with no setup step (the old `/output-style` command was removed in v2.1.91; settings is the current path), and `keep-coding-instructions: true` keeps the harness's careful-engineering discipline while still replacing the terse CLI register. The style file's substance was lifted from `prompts/_parker-voice-block.md` (which stays canonical for voice rules), plus the Claude-Chat-feel rules Jimmy asked to import: prose over bullet walls, answer-first replies, reply size matched to question size, no flattery openers, no hedge stacks, one question per message — and the ELI5-tweet operator moves: "what I did, did it work, what's next," technical terms explained on first use, decisions as 2-3 options with a named pick. Shipping is structural at every surface: the factory carries the file and the switch; the onboarding runner copies the style dir and the stamped settings at build time; the propagate script copies it unconditionally (like the context hook) to standing brains. Known trade-off, accepted: the voice now lives in two factory files (voice block and output style) mirrored by hand, because a system prompt cannot reference other files at runtime; the pair is documented in both headers and the `system-of-records` audit is the drift backstop.

**Why it matters:** This is the enforcement-must-be-structural rule applied to the voice itself. CLAUDE.md is advisory context that competes with the harness's dense default system prompt; an output style replaces that section of the actual system prompt, so the plain-warm register stops depending on instruction text winning a tug-of-war. It also moves voice from "a thing each brain's CLAUDE.md says" to "a thing every session mechanically runs," which is the difference between describing the Claude Chat feel and shipping it.
