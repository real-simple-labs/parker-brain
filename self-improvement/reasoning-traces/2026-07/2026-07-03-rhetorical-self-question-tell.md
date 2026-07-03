---
trace_id: 2026-07-03-rhetorical-self-question-tell
date_captured: 2026-07-03
source: chat
source_ref: Jimmy's correction of a voiced-verbatim example — "one of the biggest ai tells is the questions that you are not actually asking... Humans dont ask rhetorical questions in ad scripts (unless it's a question hook)"
trigger_type: correction
scope: system
brand: global
team: creative-strategy
confidence: strong
status: applied
target_surfaces:
  - global/knowledge/creative-strategy/spoken-script-voice.md
  - global/knowledge/creative-strategy/ai-writing-tells.md
  - scripts/voice-lint.py
  - .claude/agents/creative-voice-review.md
promotion_condition: already applied — explicit correction and approval in the same session
---

**What happened:** While reviewing the register-translation work, Jimmy corrected an example line: "And honestly? I like, forgot I was wearing them" should be "And guys I literally forgot I was wearing them." His rule, verbatim: one of the biggest AI tells is the questions you are not actually asking — humans don't ask rhetorical questions in ad scripts, unless it's a question hook.

**Decision context:** The doctrine half-covered this — "the rhetorical fragment" sat under the written-tics section of `spoken-script-voice.md` — but it was buried, unnamed on the main tells list, absent from the linter, and absent from the voice reviewer's judgment checklist, and the generated example proved it slips through. The example also broke a second doctrine rule its own doc states: an em-dash written as a spoken pause ("I just — I forgot"). Jimmy's version fixes both mechanisms the human way: emphasis carried by spoken words ("guys," "literally") rather than a question mark aimed at no one or punctuation standing in for a pause.

**Why it matters:** The self-question ("Honestly?" "Sound familiar?" "Crazy, right?" "The best part?") is writing wearing a conversational costume — a speaker interviewing themselves mid-thought. It feels conversational to a model, which is exactly why models overproduce it, and why it reads as generated to a human ear. The single legitimate home is the question hook: an opener deliberately built as a real question to the viewer, per the hook taxonomy.

**Inferred rule:** Emphasis in spoken copy is voiced with words said *to the listener*, never with a rhetorical question mark. Any mid-body question the speaker immediately answers is a tell; a question is only allowed when it is genuinely being asked of the viewer, which in ad scripts means the question hook position. Also meta: when a generated example illustrates a doctrine, audit the example against the full doctrine — a bad example teaches the tell it was meant to prevent.

**Scope judgment:** Applies to all creative deliverables, spoken and written (the question-as-header, "The result?", is the static-copy form). The question-hook exception is positional and deliberate, not a loophole for any line-one question mark: the linter flags mechanically everywhere and the judgment layer keeps only a real question hook.

**Routing:** Promoted to Tell 11 on the main list in `spoken-script-voice.md` (compound tell renumbered to 12; the "eleven tells" citations in `ai-writing-tells.md` and the voice agent updated to twelve; the buried written-tics entry now points at the named tell). Sign family 8 in `ai-writing-tells.md` renamed and expanded. New `rhetorical self-question` pattern in `voice-lint.py`, tested: flags "honestly? / Sound familiar? / Crazy, right?", passes a genuine question hook and Jimmy's corrected line. Voice reviewer's catch-what-regex-can't list updated. The voiced-verbatim example in the register section replaced with Jimmy's line, with a note that voicing must not introduce tells.
