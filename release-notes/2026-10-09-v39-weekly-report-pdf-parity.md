# v39 — the weekly creative report's PDF matches the web page (2026-10-09)

The weekly creative report's PDF printed on letter-size pages with white margins and its own print-only styles, so sections got cut between pages and it looked different from the web page. Teams send the PDF to clients, so it has to look just like the HTML.

## What shipped

- **One long page, edge to edge.** `render_report.py --pdf` now prints the report as a single page exactly as wide and tall as the web layout (1,100 pixels wide), with no margins. The soft color washes run to the edges, and nothing is cut between pages. A small script in the page sizes the printed page to fit, so printing from a browser gives the same result.
- **No print-only look.** The print styles that shrank the text, tightened padding, and flattened the glass panels are gone. The PDF uses the same styles as the screen.
- **Every picture loads before printing.** Thumbnails no longer load lazily, so none can be missing from the PDF.
- **Past the PDF size limit** (about 200 inches tall, far longer than a weekly report runs), the page size is left alone and breaks fall between sections, never through a card or a table row.

Checked on `<a brand>`'s live Week 40 report: one page, 824.88 by 5,285.04 points, every thumbnail in place, matching the web page section for section.

## Migration

`migrations/v39.md`: no-op. Everything ships through the skill bundle.
