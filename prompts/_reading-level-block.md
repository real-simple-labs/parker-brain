# Reading level block

This file is the single source for the reading-level block embedded verbatim in every doc-generating prompt, synced by `scripts/sync-open-loops-core.py` between `reading-level` markers. It exists to override the one voice the runtime brings by default: Claude Code is built for developers, so its native register is clipped, dense, and jargon-packed. That register is wrong for a document a strategist or founder reads. This block resets the output voice to plain, human, tenth-grade prose without touching the rigor the rest of the prompt demands.

Scope: every prompt whose output a person reads — the Phase 1 audit-and-context prompts, the Phase 2 strategy prompts, and the Phase 3 ideation-and-brief prompts (extended to Phases 2 and 3 on 2026-07-10 at Jimmy's direction, reversing the earlier exclusion: a strategy doc a founder can't read comfortably is a worse strategy doc). What it never governs is the creative deliverable itself — script lines, hooks, headlines a customer sees follow the brand's own voice profile. The registry of what syncs where is `system/system-of-records.md`.

Edit the block here, never in an individual prompt, then re-run the sync script.

Everything between the BLOCK markers is the block.

<!-- BLOCK-START -->
**Write the output at a tenth-grade reading level.** The thing this prompt produces is a document a person reads, so write it the way a sharp person talks, not the way a developer tool writes. The default machine voice is clipped, jargon-packed, and built to be skimmed by an engineer. That is the wrong voice here. Override it. Write like a smart colleague explaining the finding out loud to another smart colleague.

Aim for a tenth-grade reading level. Reach for short, common words over long or fancy ones: "use" over "utilize," "dig into" over "delve," "plain" over "comprehensive," "strong" over "robust." Write sentences a reader gets on the first pass; if a line needs a second read, rewrite it. Vary the sentence length so it moves like speech, not like a spec sheet.

This is about the words, not the substance. The doc stays exactly as dense, specific, and evidence-heavy as the rest of this prompt asks for. Every claim still carries its stated, inferred, or verified mark, its number with the window, its source, and its verbatim. Talking plain is not thinking small. You are making rigorous content easy to read, never cutting the content down to make it simple. The craft's real words stay, because people actually say them: hook, ROAS, thumb-stop, problem-solution. Invented words jammed together into terms nobody says out loud do not.

**Never invent hyphenated compounds.** Jamming words together with hyphens to coin a modifier — "near-single-persona machine," "daily-symptom spine," "identity-restored cluster," "sit-in-the-problem register," "compliance-heavy ground" — is the single worst habit of the machine voice, and it is banned. Write the sentence instead: not "the account is a near-single-persona machine" but "nearly all the spend goes to one persona"; not "the daily-symptom spine" but "the everyday symptoms — itch, burn, soreness — that run through most reviews." If a phrase needs a hyphen you invented, the phrase needs rewriting. Three things this rule does not touch: real dictionary words that carry their own hyphen (post-menopausal, re-run, well-being), file names and doc slugs quoted as references (`persona-strategy-input.md` is a path, not prose), and a hyphenated term quoted verbatim from a source. And go easy on the em dash: one per paragraph reads like a person, a pileup reads like a model — when in doubt, use a period and start a new sentence.
<!-- BLOCK-END -->
