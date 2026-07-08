---
trace_id: 2026-07-03-register-translation-and-skill-birth-principles
date_captured: 2026-07-03
source: chat
source_ref: Jimmy's follow-up after the two gates landed — carry these principles into future skills, and voice written customer language when it crosses into spoken scripts
trigger_type: context_rule
scope: system
brand: global
team: creative-strategy
confidence: strong
status: applied
target_surfaces:
  - global/knowledge/creative-strategy/spoken-script-voice.md
  - global/knowledge/creative-strategy/ai-writing-tells.md
  - .claude/agents/creative-voice-review.md
  - .claude/agents/context-grounding-review.md
  - .claude/skills/scriptwriting/SKILL.md
  - .claude/skills/hooks/SKILL.md
  - .claude/skills/update-parker-skill/SKILL.md
promotion_condition: already applied — explicit approval in the same session
---

**What happened:** Two directives in one message. First: as new skills get created, the principles just built (the two ship gates, structural enforcement) must carry over automatically rather than being retrofitted per skill. Second: customer language is register-specific — a written review is perfect verbatim for written deliverables (static headlines, review headlines), but carried into a spoken script it must gain "the human components of speaking: the likes, the ums, the you know-es" — Jimmy's words — because typed sentences are not how people talk.

**Decision context:** The subtle problem surfaced before editing: voicing a verbatim breaks the grounding gate's grep-trace, since the spoken line no longer matches the vault text. So the rule was designed as a provenance shape, not just a writing instruction: the exact written verbatim lands in the Script Brief's key VoC phrases (where it traces), and the script line is presented as its voiced adaptation. The voice gate flags pasted written cadence in spoken work (the fix is voicing, preserving the customer's vocabulary); the grounding gate resolves an untraced spoken line through its paired brief verbatim before calling it invented. The verbatim exemption in ai-writing-tells.md became register-aware: it protects the customer's words everywhere, and their typed cadence only in written deliverables. For the future-skills half, the canonical enforcement point is `update-parker-skill` — the required path for skill creation — which gained a "Principles every new skill is born with" checklist: both gates for creative deliverables, the structural stack (deterministic check, independent reviewer, output contract), canonical-doc-plus-reference, the register rule, provenance, and the ship-list check for files outside `.claude/skills/`.

**Why it matters:** Both halves are drift prevention. Skills created next quarter by someone else (or by Parker) would otherwise miss the gates, and the gates would slowly become a five-skill island. And the register rule closes a failure the voice doctrine implied but never named: "use customer language" executed naively pastes typed sentences into mouths, producing scripts that are perfectly grounded and perfectly unsayable.

**Inferred rule:** When two rules collide (use exact customer language / sound spoken), the resolution is a two-artifact shape that satisfies both — exact source preserved where provenance lives, adapted form where the register lives, explicitly paired. And any new standard worth enforcing gets written into the creation path, not appended to existing instances.

**Scope judgment:** The register rule governs the crossing from written sources into spoken deliverables anywhere it happens — scripts, spoken hook lines, ad-prompt dialogue. It does not license inventing fake stumbles: disfluencies are placed where thought turns, in the brand's register, per the existing keep-the-mess rule. The birth principles apply to skill creation and material reshaping, not to every small skill edit.

**Routing:** Applied to the voice doctrine (new section: written customer language is not spoken customer language), the tells doc's false-positive discipline, both reviewer agents, the scriptwriting and hooks hard rules, update-parker-skill's new principles section, and the system map (skill-library intro + changelog). No new files, so ship lists unchanged — every edit lands in files that already ship.
