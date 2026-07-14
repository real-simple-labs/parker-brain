---
doc: reasoning-trace
title: "Identity is second person — the instruction files talk to the model, never about a character"
status: approved by Jimmy 2026-07-14 and executed same day on the claude-is-parker branch
date: 2026-07-14
author: Parker (Fable), from Jimmy's direction
sources:
  - "Jimmy's direction, 2026-07-14: for all of the CLAUDE.md and agent md files, we do not want this to be Parker, we need it to assume it's YOU (Claude) — we want their Claude Code to adapt this"
  - "CLAUDE.md (factory root)"
  - "prompts/_parker-voice-block.md"
  - "templates/brand-brain-CLAUDE-template.md"
---

# Identity is second person

## The rule

Every instruction surface a runtime model reads — the factory `CLAUDE.md`, the brand-brain `CLAUDE.md` template, the voice block, agent definitions — is written **to** the model, in second person. It never describes Parker as a third-party bot ("Parker should think like a strategist"), and it never assigns the identity as a costume ("You are Parker, a strategist"). The team's Claude Code reads these files and becomes the system.

"Parker" survives two ways only:

1. **Artifact names.** Parker MCP, `parker-brain`, `parker-system/`, `setup_parker_brain`, "Parker's GitHub organization," file names like `_parker-voice-block.md`. These are proper nouns for real things and do not change.
2. **One mapping line** near the top of each identity surface: "The team calls this system Parker; when they ask what Parker thinks, that's you." Teams will keep saying "Parker" because the product and tools carry the name, so the line closes the gap without reopening the character.

The character itself — the Minnesota strategist, the biography, the nature — stays, per Jimmy's explicit call on 2026-07-14. It is just turned around: "You're a creative strategist from Minnesota who turned yourself into an AI to scale what you know."

## Why

Third-person instructions read as a spec about someone else, and the model treats them with a spectator's distance — it describes what Parker would do instead of doing it. Second person is the operating contract: the reader is the actor. This is the same reason the brand-brain template was already second person; the fix extends that posture to every instruction surface and removes the mixed frame where one file says "you" and the canonical voice block says "he."

## How to apply

- New CLAUDE.md files, agent definitions, and identity/voice blocks are written in second person from the first draft.
- When editing an older doc that talks about Parker in third person on an instruction surface, convert it in the same pass.
- Generating prompts and method docs that *mention* Parker as the system (for example, "separate what the brand says from what Parker infers" inside a prompt's output rules) are a different surface; convert them when touched, but they were not part of this pass.
