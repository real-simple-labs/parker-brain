---
trace_id: 2026-07-03-team-conversations-phase1-source
date_captured: 2026-07-03
source: chat
source_ref: Jimmy — a new tool (search_chat_history) pulls the team's past Parker web-app conversations; make it a first-class source for the Phase-1 cold-start build
trigger_type: product_rule
scope: prompt_family
brand: global
team: global
confidence: strong
status: applied
target_surfaces:
  - prompts/_team-conversations-source-block.md
  - scripts/sync-open-loops-core.py
  - 16 Phase-1 prompts (brand-profile, market-synthesis, open-loops, strategic-roadmap, ideas-and-briefs)
  - prompts/onboarding-runner.md
  - system/parker-tools.md
  - system/system-of-records.md
promotion_condition: already applied — Jimmy directed it and confirmed the exact prompt subset
---

**What happened:** Jimmy pointed out that `search_chat_history` now reaches the team's past Parker web-app conversations, and it should become a first-class source for the cold-start build, not just the audit tool for reading prior audits. His clarification reframed the scope: "This is more so for the prompts for the initial context generation for phase one. A lot of these are going to be impacted." So it is an evidence source for the Phase-1 context-generation prompts.

**Decision context:** Not every Phase-1 prompt should get it. Jimmy: "I don't know if every phase one prompt needs it or only the ones that are necessary. Brand reputation does not need this." That gave the rule: chat history is a source only where the truth is what the team knows and says, not where it is observed from outside. Team-knowledge prompts get it (brand identity, ops-and-team, targets, calendar, customer-journey, competitive-landscape, visual-vocabulary, the brand-profile narrative, gaps-and-opportunities, the open-loops roll-up, the strategic roadmap and its four inputs, the idea bank). Externally-observed reads do not (reputation, community, category/market research, organic inventory, the ad-account reads, all competitor library pulls, the persona source-pulls, the VoC extractions, the audits) because a past conversation does not make those truer. Jimmy confirmed the core set and picked the three borderline adds (customer-journey, competitive-landscape, visual-vocabulary), leaving website-and-product-audit out. The mechanism reused the existing synced-block infrastructure exactly like `brand-intake` (a targeted subset, not universal): a new `team-conversations` block written once, its markers inserted into the 16 confirmed prompts, filled by `scripts/sync-open-loops-core.py`. The block honors attribution (a chat claim is stated-until-verified, quoted with author and date; a contradiction with live data is the finding; team words never substitute for voice-of-customer) and is never a gate. Onboarding gained a Phase-0 step: once the brand is locked, check with `listThreads` whether the team already has web history, and if so read it into the build and seed each teammate's future `user-profile.md`. Tool doc and the system-of-records registry updated. The block was rewritten to drop em-dashes, since prompts carry the no-em-dash rule.

**Why it matters:** Teams say an enormous amount about their brand in the Parker web app that never lands in a formal doc. Ignoring it at cold start means rebuilding knowledge the team already handed over. This wires that history in where it is real evidence and keeps it out where it would be noise, and it is the connector between a team's prior Parker life and the brain being built for them.

**Inferred rule:** A new source is added selectively, by the nature of the truth each doc rests on, not blanket-applied. Team-stated knowledge is a source for the team-on-the-brand reads; it is not a source for externally-observed reads or for customer-language evidence. Reuse the synced-block subset mechanism for a selective add rather than editing prompts one by one or forcing a universal block.

**Scope judgment:** 16 Phase-1 prompts, named in the system-of-records registry. Deliberately excluded from the observed reads and the audits (which already use the tool for prior-audit trajectory, a different purpose). The user-profile seed from this history is noted as a downstream benefit, built later.

**Routing:** New synced block + sync-map entry + markers in 16 prompts (synced), onboarding Phase-0 check, `parker-tools.md` expanded, `system-of-records.md` registry entry. On its own branch for a separate PR.
