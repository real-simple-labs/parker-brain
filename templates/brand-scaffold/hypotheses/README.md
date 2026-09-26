# Hypotheses

Promoted open loops turned into something testable: a prediction that could come back wrong, plus the few data pulls that together would settle it. The `open-loops-advance` skill writes these; `open-loops-validate` runs them.

## What lives here

- `awaiting-user/[YYYY-MM]/[loop-slug].md`: hypotheses that need the team before the test runs, usually because only the brand can answer part of the question or the plan is high stakes.
- `tested/[YYYY-MM]/[loop-slug].md`: hypotheses whose test has run. The verdict itself is filed in `../validations/`.
- `denied/[YYYY-MM]/[loop-slug].md`: hypotheses the team said no to, with their reason.

Each one is a short page that leads with the prediction. The method is in `parker-system/system/open-loops-system.md` and `.claude/skills/open-loops-advance/`.

A new brain starts with this folder empty.
