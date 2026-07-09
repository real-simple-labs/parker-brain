# Fixtures

Sanitized example artifacts used to anchor prompts and skills to a real shape without leaking private brand data. Every fixture here is illustrative — a worked example of a format, never a schema to impose and never live customer output. Each entry below names what it is, which prompt or skill it supports, and the behavior it illustrates.

## `creative-tracker-example.csv`

**Fixture data — illustrative, not a required schema.** A creative tracker's planning tab: one concept per row across 23 columns.

- **Supports:** `prompts/ideas-and-briefs/sprint-plan.md` (the concept map it emits) and `creative-strategy-context/ideation-and-brainstorming.md` (the concept-planning method).
- **Illustrates:** the seam between the **planning columns** a strategist fills at plan time — `Job #`, `Concept Name`, `Description`, `Sale/EG`, `Visuals`, `Content Type`, `Persona`, `Doorway`, `Emotion`, `Type`, `Page`, `Versions` — and the **execution columns** production fills downstream as briefs are written and assets move — `Brief Link`, `Review Link`, `Status`, `Strategist`, `Editor`, `Handle`, `Ad Text`, `Ad Text Approval`, `Landing Page`, `Upload Date`, `Source Assets`. That seam is the seam between the sprint plan and the briefs that follow it.
- **Expected behavior:** the sprint-plan concept map maps onto these column semantics, not these exact headers. When a brand has supplied its own tracker or brief format at intake (`briefs/_brief-template.md`, `running-notes/brand-rules.md`), that governs and this example yields to it.
