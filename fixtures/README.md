# Fixtures

Sanitized example artifacts used to anchor prompts and skills to a real shape without leaking private brand data. Every fixture here is illustrative — a worked example of a format, never a schema to impose and never live customer output. Each entry below names what it is, which prompt or skill it supports, and the behavior it illustrates.

## `creative-tracker-example.csv`

**Fixture data — illustrative, not a required schema.** A creative tracker's planning tab: one concept per row across 23 columns.

- **Supports:** `prompts/ideas-and-briefs/sprint-plan.md` (the concept map it emits) and `creative-strategy-context/ideation-and-brainstorming.md` (the concept-planning method).
- **Illustrates:** the seam between the **planning columns** a strategist fills at plan time — `Job #`, `Concept Name`, `Description`, `Sale/EG`, `Visuals`, `Content Type`, `Persona`, `Doorway`, `Emotion`, `Type`, `Page`, `Versions` — and the **execution columns** production fills downstream as briefs are written and assets move — `Brief Link`, `Review Link`, `Status`, `Strategist`, `Editor`, `Handle`, `Ad Text`, `Ad Text Approval`, `Landing Page`, `Upload Date`, `Source Assets`. That seam is the seam between the sprint plan and the briefs that follow it.
- **Expected behavior:** the sprint-plan concept map maps onto these column semantics, not these exact headers. When a brand has supplied its own tracker or brief format at intake (`briefs/_brief-template.md`, `running-notes/brand-rules.md`), that governs and this example yields to it.

## `weekly-creative-report-example.json`

**Fixture data — a fictional brand ("Juniper & Pine") with fictional numbers.** One week's report data file, every section filled.

- **Supports:** the `weekly-creative-report` skill (`.claude/skills/weekly-creative-report/`): it's the worked example `report-schema.md` points to, and the input to render when checking a change to `render_report.py`.
- **Illustrates:** the voice the shareable report is written in (an agency talking plainly to a brand's leadership), a "why" line that describes the ad so the reader can picture it, a watch list where every flag carries an action, `media_type` on every ad (a real run also carries each ad's public `media_url`, left out here because the ads are fictional), and the hidden `basis` and `sources` lines that keep each insight's source in the brain's copy without printing stated or inferred labels on the client's page.
- **Expected behavior:** `python3 .claude/skills/weekly-creative-report/render_report.py fixtures/weekly-creative-report-example.json out.html` renders with no warnings. A real run matches this shape and tone, not these numbers or sections; the brand's setup answers decide what leads and what's on the page.
