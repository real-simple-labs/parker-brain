# v45 — the customer anchor check skill (2026-10-30)

A strategist training Parker's creative skills on an internal brain ran every concept through an end-of-concept "anchor check" before it went to a creator: how much of this already sounds like the customer, and where would the customer's own words do better? This release ships that check as a public skill with everything brand-specific taken out, so any team can run it on any brand. The design decisions (lens, not gate; one concept at a time; only when asked; swaps picked for the exact avatar) were confirmed by the person who built it on 2026-10-27.

## What shipped

- **`.claude/skills/customer-anchor-check/SKILL.md`.** Takes one concept in any state (a hook, a script, static copy, a concept in progress) and the person it's built for. Pulls the brand's reviews, ad comments, and post-purchase survey for that angle and avatar, tags each non-functional line Verbatim (1), Echo (0.5), Composed (0), or Off-customer (0), and returns a customer-language match percentage plus three to six swaps. Each swap keeps the concept's meaning and speaker, says it the customer's way, and shows the verbatim customer line it's anchored in. Functional lines (CTA, offer, price, product mechanics, legal) are left out of the score. The full line-by-line read comes only on request.
- **`references/closeness-scale.md`** (the four tags, how to test a line, the scoring), **`references/avatar-matching.md`** (the avatar fields, reading who's speaking in a record, strong, partial, and cross-voice matches), and **`references/brand-overlay-template.md`** (brand rules for running the skill without a brain).
- **Index docs** name the new skill: `README.md`, `system/parker-system-map.md` (skill library and update log), `system/master-file-structure.md`, `prompts/onboarding-runner.md` (Phase 0's list of what ships), the brand `CLAUDE.md` template, and the routine bundle README.

## Guardrails worth knowing

- **A lens, not a gate.** The percentage measures wording only and is never a performance prediction. A composed hook over a verbatim body is a strong build that scores lower, and the skill says that's fine.
- **Quotes are exact; swaps are not quotes.** The anchor line is the customer's words untouched, with the full review under it when it's a fragment. The swap is the customer's meaning fitted to the concept and is never shown in quotation marks as something a customer said.
- **Survey answers are private.** They can anchor a swap, cited by date, segment, and question, never by name or email. Reviews and public comments can be quoted on screen.
- **Counts come from the keyword tool.** A semantic pull that returns exactly topK has hit the cap and is never read as a count.
- **A dark survey tool has a fallback.** When `semantic_search_post_purchase_survey` returns nothing, the skill looks for a survey export in the brain (usually `brand-context/`) or asks for one.

## Brand rules live in the brand lens

In a brain, the skill reads `brand-lens.md` as the brand's overlay, alongside the brand profile, identity analysis, rules, personas, and voice-of-customer docs. That keeps brand rules in the one file factory updates never touch, instead of a second overlay inside a copied skill folder. The overlay template is only for running the skill without a brain.

## No review gates, on purpose

Like `recreate`, this skill doesn't spawn `context-grounding-review` and `creative-voice-review`. It hands back notes on someone's concept, not finished copy, and a voice rewrite would pull the swaps off the customer's wording. Each swap gets its own claims and voice check inside the skill. The brain's `craft-context` hook and the ship-gates rule in `update-parker-skill` now name both exceptions, so nothing reads the missing receipts as a skipped gate.

## Not in this release

- **The worked example.** The internal run behind this skill (a six-line script that scored 67%: three verbatim, two echo, one composed) quotes real customer reviews, so it stays out of the public repo. A sanitized fixture of the same shape is the planned first eval.
- **Product notes** from the internal run (a brand whose survey tool returned no rows while a large survey export sat in its brain, and a policy check on quoting survey answers) went to the product team rather than into the skill.

## How it reaches brains

The bundle map in `scripts/sync-executable-layer.py` already copies every folder under `.claude/skills/`, so new brains get the skill from the scaffold and standing brains get it, and the updated `craft-context` hook, from `/update-brain` on the pin bump. The brand `CLAUDE.md` template now names the skill; that file is a seed, so only new brains get the new wording. Standing brains don't need it: the skill registers and triggers from its own description.

## Migration

`migrations/v45.md`: no-op. Everything ships through the bundle.
