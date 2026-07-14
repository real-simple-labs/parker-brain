---
trace_id: 2026-07-14-onboarding-existence-triage
date_captured: 2026-07-14
source: chat
source_ref: Anton flagged that onboarding asks "is this the right brand" and "ready for the multi-hour build" even when the brand's brain already exists fully built
trigger_type: correction
scope: system
brand: global
team: product
confidence: strong
status: applied
target_surfaces:
  - prompts/onboarding-runner.md
  - .claude/skills/set-up-brain/SKILL.md
promotion_condition: already applied — explicit approval in the same session
---

**What happened:** Anton hit the onboarding flow with a brand whose brain was already fully built and still got the two build-kickoff questions — confirm the brand, then the go/no-go with the multi-hour time expectation. The runner already had a "look at what you cloned before assuming a cold start" rule, but it sat in Phase 0 step 2, after the welcome pitch, the go-ahead gate, and the brand-confirm question had all fired.

**Decision context:** The detection machinery already existed — `setup_parker_brain` is idempotent and returns `reused_existing: true` — so the fix is ordering, not new capability. A new runner section ("Before anything — find out what already exists") now runs the triage before the orientation: resolve the brand without a confirmation question when it's unambiguous, call the tool, and route by repo state — fully built → retrieval straight to `/get-started`; mid-build → resume offer; new/empty → the normal build flow with the pitch and gate intact. The skill's step 0 grew from interrupted-only to the full triage, deferring mechanics to the runner. The skill description also gained a retrieval trigger so a frontend prompt like "Retrieve my existing Parker brain" routes to the same skill.

**Why it matters:** Telling someone a multi-hour build is coming when the work is already done is wrong on its face and costs trust at the exact moment the product is introducing itself. The go-ahead gate exists to be honest about cost; honesty cuts both ways.

**Inferred rule:** Any gate that pitches cost or asks for a commitment must run *after* the check that determines whether the cost is real. Detection before pitch, always. Same pattern as the resume rule: never make someone rebuild — or re-approve — finished work.

**Scope judgment:** Method-only; both files travel via the pin bump / copied bundle, so the next release's migration is a no-op one-liner. Complementary frontend change flagged to Anton (dashboard can swap the copiable prompt to "retrieve" once the backend sees a completed run), not part of this repo.
