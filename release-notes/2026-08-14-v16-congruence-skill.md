# v16 — Congruence

Parker can now audit whether one Meta ad journey feels intentionally made for the same person from impression through landing page.

## What shipped

- A new `.claude/skills/congruence/` skill that reads the full ad, actual ad-level age-and-gender delivery and outcomes, and the exact rendered landing page.
- A canonical `creative-strategy-context/congruence.md` method that keeps the ad's implied audience, the brief's stated audience, and Meta's delivered audience separate.
- A fixed 1-to-10 score built from four seams: ad message and person (20%), intended audience and delivery (30%), ad promise and page (25%), and delivered audience and page experience (25%).
- A deterministic scoring script, report template, regression tests, and three forward-test packets.
- A hard evidence gate: no complete creative, exact ad-level delivery, or rendered destination means no overall score.
- A required local landing-page mockup when either page seam scores 6.0 or lower, or a generic destination drops the ad's audience, product, promise, or promotion. The mockup studies the live brand, reuses owned assets, follows the user's available design skills, verifies mobile and desktop, and never changes the live site.

## Data connection order

The skill always prefers Parker MCP. If Parker cannot provide the complete joined evidence, it can use another authorized source or a fresh direct evidence packet. If no route supplies the required evidence, it stops and explains how to connect Parker or what to provide.

## How it reaches standing brains

The skill lives in the copied executable layer, so the normal `/update-brain` pin bump and re-sync adds it. The canonical method arrives through the read-only Parker mount. No brand-authored file needs to change.
