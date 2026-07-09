# Reading level block

This file is the single source for the reading-level block embedded verbatim in every Phase 1 doc-generating prompt, synced by `scripts/sync-open-loops-core.py` between `reading-level` markers. It exists to override the one voice the runtime brings by default: Claude Code is built for developers, so its native register is clipped, dense, and jargon-packed. That register is wrong for a context doc a strategist reads. This block resets the output voice to plain, human, tenth-grade prose without touching the rigor the rest of the prompt demands.

Scope is deliberate. It rides only the Phase 1 audit-and-context prompts, not the Phase 2 strategy prompts and not the Phase 3 creative prompts, whose voice is governed by the brand's own profile. The registry of what syncs where is `system/system-of-records.md`.

Edit the block here, never in an individual prompt, then re-run the sync script.

Everything between the BLOCK markers is the block.

<!-- BLOCK-START -->
**Write the output at a tenth-grade reading level.** The thing this prompt produces is a document a person reads, so write it the way a sharp person talks, not the way a developer tool writes. The default machine voice is clipped, jargon-packed, and built to be skimmed by an engineer. That is the wrong voice here. Override it. Write like a smart colleague explaining the finding out loud to another smart colleague.

Aim for a tenth-grade reading level. Reach for short, common words over long or fancy ones: "use" over "utilize," "dig into" over "delve," "plain" over "comprehensive," "strong" over "robust." Write sentences a reader gets on the first pass; if a line needs a second read, rewrite it. Vary the sentence length so it moves like speech, not like a spec sheet.

This is about the words, not the substance. The doc stays exactly as dense, specific, and evidence-heavy as the rest of this prompt asks for. Every claim still carries its stated, inferred, or verified mark, its number with the window, its source, and its verbatim. Talking plain is not thinking small. You are making rigorous content easy to read, never cutting the content down to make it simple. The craft's real words stay, because people actually say them: hook, ROAS, thumb-stop, problem-solution. Invented words jammed together into terms nobody says out loud do not.
<!-- BLOCK-END -->
