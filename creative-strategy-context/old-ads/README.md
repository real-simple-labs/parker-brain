---
summary: "The old-ads corpus — a growing swipe library of historical print advertising, organized by industry and by mechanic, with the capture method for adding entries; the historian lens of the weekly idea hunt digs here."
---

# The old-ads corpus

Old print ads are the strategist's gold mine, especially for statics. Nothing is new under the sun, and the past is the one inspiration source the rest of the market isn't mining — everyone else is scrolling the same feed. Print carried a different economics: a shoot cost so much that a brand spent hours getting one concept right, so the surviving headlines and visuals hold a density of craft most modern feed content never reaches. A vintage category-comparison line becomes a new product comparison. A grid layout becomes a Meta ad, because humans love choices. A matching-game visual becomes a creator swapping looks until she finds her favorite. The method for *using* these finds lives in `../ideation-and-brainstorming.md`; this corpus is where the finds live.

## What this is

A curated, continuously growing library of historical ad **entries** — one file per ad or per tightly related set — that the weekly idea hunt's historian lens digs through by the brand's industry and by mechanic. It ships into every brand brain at `parker-system/creative-strategy-context/old-ads/`, so a brain can mine the past offline; live web archives are the fallback when the corpus is thin on an industry.

## Where entries come from

Public-domain and openly archived material only. The richest veins:

- **Life magazine archives** (archive.org and Google Books carry decades) — where the long-form advertorials lived.
- **Industry-categorized collections** — the All-American Ads books organize by industry (beauty, appliances, autos, food), which is exactly the retrieval shape this corpus mirrors. Own copies can seed entries by description; the entry describes and links, it never reproduces a scanned page wholesale.
- **Public ad archives and museum collections** — the Smithsonian, Duke's Ad*Access, the Internet Archive's ephemera collections.

**Copyright posture: describe and link.** An entry carries a narrative reconstruction of the ad (per the source-capture standards — written so a reader can picture it without seeing it), the exact headline or line when short quotation is fair, and a link to where the ad can be viewed. It does not embed full scans of in-copyright work, and adaptation always translates the mechanism, never copies the surface.

## Organization

```
old-ads/
  README.md          ← this file
  INDEX.md           ← the searchable table: every entry, by industry and mechanic
  entries/
    [era]-[industry]-[slug].md
```

Every entry is tagged two ways, because retrieval happens two ways:

- **By industry** — beauty, food and drink, apparel, home and appliance, auto, travel, health, tobacco-era cautionary, and so on. A strategist concepting for a skincare brand opens the beauty page first.
- **By mechanic** — the reusable shape: comparison line, grid-of-choices, avatar callout, demonstration visual, before/after, matching game, testimonial, long-copy advertorial, mascot, fear-then-relief. The mechanic is what transfers across industries; the far-transfer lane hunts these.

## Entry shape

Per the idea-bank capture standards, adapted for historical sources: `concept_name` · `era` (decade) · `industry` · `mechanic` (one or more) · `headline_or_line` (verbatim when short quotation is fair) · `source_read` (the narrative reconstruction — what the ad shows, in order) · `source_link` (viewable archive link) · `craft_justification` (why this earned a place — the strength of the line, the visual, or the structure; old ads justify on craft and durability, not metrics) · `notes`. No `spark` here — the corpus is brand-agnostic; sparks happen at hunt time, in the brand's own idea bank, when the historian lens collides an entry with the brand.

## How it grows

- The **historian lens** of every weekly hunt adds what it finds while digging for its brand — the corpus compounds across every brand's hunts.
- **Expert-signal intake** routes here when a source teaches through a historical ad.
- **Deliberate mining sessions** — an hour in the archives on one industry fills a page. Any contributor can run one.

Update `INDEX.md` in the same pass as any entry — an unindexed entry is invisible to the historian lens.
