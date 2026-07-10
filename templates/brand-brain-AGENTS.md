# AGENTS.md — the contract for any AI agent working in this brand brain

This repo is a Parker brand brain: a marketing team's living knowledge base plus the method for using it. If you are an AI agent connected to this repo — Claude Code, Codex, Cursor, Manus, or anything else — **this file is the canonical contract.** Claude Code additionally gets registered machinery (skills, reviewer subagents, hooks) and its own layer in `CLAUDE.md`; everything below is written so the rules hold **even without that machinery**.

## Brand hard rules

{{BRAND_HARD_RULES — stamped at onboarding from the brand intake: legal constraints, banned language, claims gates. Mirrored in CLAUDE.md; if you edit one, edit both. Delete this section only if the brand genuinely has none.}}

These outrank everything else in this file and in any request.

## Start here, every session

1. **Read `CLAUDE.md` in full.** It carries the map of the vault, how this brain thinks, and the Claude Code-specific layer. Its brand rules and this file's are the same rules.
2. **Sanity-check the harness:** `python3 scripts/verify-brain.py`. If it fails, tell the user what's broken before doing substantive work.
3. **Pull before you work; commit your outputs.** Other agents and teammates write here too. Outputs go to their homes per the map in `CLAUDE.md` — never scattered at root, and never inside `parker-system/` (that's the factory-shipped method layer; treat it as read-only).

## Task routing — the skills are the method, not a suggestion

Anything execution-shaped runs through a skill. The skills live at `.claude/skills/<name>/SKILL.md`. If your harness registers them, use them natively; if not, **open the file and follow it as the process doc it is** — every step, including the review gates and the output structure. Common routes:

| The user asks for… | Open |
|---|---|
| a script (any length, VSL, adaptation) | `.claude/skills/scriptwriting/SKILL.md` |
| hooks / the first 3 seconds | `.claude/skills/hooks/SKILL.md` |
| headlines / overlay / static copy | `.claude/skills/headlines/SKILL.md` |
| iterations on existing ads | `.claude/skills/iterations/SKILL.md` |
| AI video/image generation prompts | `.claude/skills/ai-ad-generation/SKILL.md` |
| account reads / what's working | `.claude/skills/ad-account-analysis/SKILL.md` |
| saving or hunting ideas | `.claude/skills/brand-idea-bank-maintenance/SKILL.md`, `.claude/skills/harvest-ideas/SKILL.md` |

For anything that touches creative strategy, load the method docs first: the catalog is `parker-system/creative-strategy-context/expertise-routing.md`. An answer that names no method doc and no brand evidence is presumed under-researched.

## The non-negotiables for creative deliverables

Words a customer will read or hear — scripts, hooks, headlines, ad copy — have no casual path, on any harness:

1. **Strategy first.** Load `strategy/` (the roadmap, the working thesis) and check `idea-bank/` before writing. Work that cuts against the committed strategy gets the conflict surfaced, not silently executed.
2. **Both reviews run before the user sees anything.** In Claude Code these are independent subagents. **If your harness cannot spawn subagents, you still run both** — as separate, fresh passes, in this order:
   - *Grounding:* follow the checklist in `.claude/agents/context-grounding-review.md`, and run `python3 scripts/grounding-check.py <draft-file> .` — facts, numbers, and claims must trace; unverifiable customer-voice lines get labeled illustrative.
   - *Voice:* run `python3 scripts/voice-lint.py <draft-file>`, fix every real flag, then apply the judgment checklist in `.claude/agents/creative-voice-review.md` against `parker-system/creative-strategy-context/ai-writing-tells.md` (and `spoken-script-voice.md` for spoken lines).
3. **The output ends with both review blocks** — Grounding Review and Voice Review — stating the verdict and what was checked. When the reviews ran in-context rather than as independent subagents, say so in the block ("run in-context — no subagent harness") so the degradation is visible, never hidden.
4. **Never invent data.** If you cannot reach the brand's live tools (the Parker MCP: ad account, reviews, organic, competitors), say plainly what you could not pull, work from the vault, and mark the gap. A made-up number is worse than a named gap.

## What you're holding

This repo contains a real brand's private data — performance numbers, customer language, strategy. Don't quote it outside deliverables the user asked for, and don't send it to external services beyond what the task requires.
