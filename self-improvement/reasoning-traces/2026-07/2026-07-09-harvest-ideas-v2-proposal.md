---
doc: design-proposal
title: "Harvest v2 — closing the gap between the idea harvester and Hannah's actual process"
status: approved by Jimmy 2026-07-09 (one modification — no daily pulse; the trend lane runs inside the weekly hunt) and executed same day on the harvest-v2 branch
date: 2026-07-09
author: Parker (Fable), from Jimmy's direction
sources:
  - "Hannah Houg / Saalt research transcripts: May 29, Jun 2, Jun 3, Jun 5, Jun 9, Jun 11 2026, plus the two solo concepting recordings"
  - ".claude/skills/harvest-ideas/SKILL.md"
  - ".claude/skills/evaluate-ideas/SKILL.md"
  - ".claude/skills/brand-idea-bank-maintenance/SKILL.md"
  - "global/knowledge/creative-strategy/ideation-and-brainstorming.md"
  - "prompts/ideas-and-briefs/brand-idea-bank.md (schema spec, referenced)"
---

# Harvest v2 proposal

## What this is

Jimmy asked for an honest read: how strong is the idea harvesting today, measured against how Hannah actually does it, and what would make the whole thing feel magical — like Parker has her brain, her process, and her quality of ideas. The frame he gave is the four-phase system: the audit surfaces the opportunities (product, messaging, personas, creative/creator/talent), that becomes the strategy, and then we go out and find more ideas. He also wants the system to learn from how users use Parker, and he named the heart of it: creativity is combining unrelated things and making them make sense for the brand's strategy.

This doc is the gap analysis plus the proposed fixes. Every gap carries its transcript evidence so the claim can be checked. Every fix is structural — a gate, a schema field, a required artifact, a new pass — never a paragraph of instruction text asking the model to try harder. That's a standing rule on this project and it's the right one here, because the failure mode in every gap below is not "the model wasn't told." It's "the pipeline has no place for it to happen."

## The one-breath verdict

The bones are good. The capture contract, the capture/grade split, the source ranking, the articulation test — all of that is faithful to Hannah and should not move. But the current harvester is a librarian and Hannah is a magpie with a plan. She doesn't collect things. She collides them with the strategy in the second she sees them. The system currently has no place for that collision, and in one spot it actively forbids it.

## What's already right — do not touch

These parts of the current system match the transcripts and survive v2 unchanged:

- **Verbatim capture, never a summary.** Hannah pastes the actual hook text, the actual comment, the actual review line. The skill's "a tidy summary is the failure" contract is exactly her behavior. (Verified across every transcript.)
- **Capture separated from grading.** She logs liberally and judges later, in a different mindset. "Brainstorming and ideation and concepting are two separate things... one is playing, the other is serious business" (Jun 3). The harvest/evaluate split encodes this correctly.
- **The articulation test.** "I really like that hook... I don't care about anything else she's talking about" (Jun 3). Winning element named in a breath or the idea is skipped. Already canon in ideation-and-brainstorming.md.
- **Source ranking.** Customer language first ("for concepting, the bread and butter is the customer... what takes the cake," Jun 3), old ads as the gold mine, affinity brands over direct competitors, organic scraping as the format supply. All present and correctly ordered in the skill.
- **Provenance and the viewable link.** She links every logged idea back to the thing itself. The schema already requires this.

## The gaps

### Gap 1 — The spark is banned at capture time (the big one)

**What Hannah does.** Every entry in her icebox carries the source PLUS the one-breath spin for the brand, captured at the moment of noticing:

- "All sunglasses are alike until you try Ray-Ban. Okay, I love that. **All discs are alike until you try Saalt.**" (Jun 3, print ads)
- "Teaching grandma how to use period underwear and why... it will allow the very same moment that a woman like me receives from her mother." (Jun 3) — logged with the storyline spin attached.
- "You could turn this into a short form video like **what wellness girlies do to stay dry**... I don't like the hot girls specifically" (Jun 3) — source hook, brand recast, and the boundary, all in one entry.
- The rugs.com story (Jun 3): a vintage ad of a woman matching gowns to refrigerators became "a creator using her outfit to imagine what a rug would look like in her space... boom, top performer, over 200k in spend." The transfer happened at noticing time, in her head, years before the brief.

**What the system does today.** harvest-ideas hard rule 3: "Do not write how the brand should run a competitor / inspiration / affinity hook inside the entry. Adaptation belongs to concepting, later." brand-idea-bank-maintenance repeats it ("Keep adaptation separate").

**Why it matters.** That rule was borrowed from the competitor source-capture doctrine (attribution-principle), where it's correct: a competitor profile is a portrait and must stay descriptive. But the idea bank is a different surface. It's the strategist's own icebox, and Hannah's own icebox is full of sparks. Jimmy named the core of creativity as combining unrelated things for this brand's strategy — the combination IS the creative act, and it happens at noticing time. Deferring it to concepting loses it, because the spark doesn't keep. Three weeks later, "yapper ad, liked the format" is a dead entry; "yapper with floating topics → disc benefits floating around her head, or a lo-fi bathroom-mirror static with the USPs around her" (her actual Jun 3 logging) is a live one.

**Structural fix.** Add a `spark` field to the entry schema: the one-breath brand application, captured only when it comes naturally (the articulation test already defines "naturally" — if the fit has to be forced, leave the field empty and say so). The verbatim source block stays intact and untouched above it. Rewrite hard rule 3 to ban what Hannah also bans — full adaptations, variations, scripts, briefs inside an entry ("one idea, not a concept" already covers this) — while requiring the spark when it lands. The competitor-profile prompts keep their no-adaptation rule unchanged; this change is scoped to idea-bank entries only, and the propagation pass (via update-parker-skill) must draw that boundary explicitly so the doctrine doesn't leak either direction.

### Gap 2 — There's no notepad (cold generation is missing entirely)

**What Hannah does.** Her first favorite method has zero external inputs: "turning off all of your electronics... getting a notebook and a pen, and literally before your mind gets stuck in all these inspo videos, write down the most simplistic language hooks that can come from your human brain... **say goodbye to period prison**" (Jun 3). She's explicit that it needs personas locked first ("it's really hard for me to do that without personas, because I don't know who I'm speaking to") and that team versions of it outperform solo ("everyone has such different minds... the hooks that come out of those sessions can be really powerful").

**What the system does today.** Nothing. harvest-ideas is 100% external capture. There is no generation pass anywhere in the harvest pipeline.

**Structural fix.** A required cold pass as phase one of every harvest, before any feed or tool is opened: generate simplest-language hooks, lines, and storylines from the personas + voice-of-customer verbatim alone, run each through the articulation test, log survivors as `source_type: cold-brainstorm` with the persona and the customer language that seeded them as provenance. Order matters and is enforced by the run structure: cold pass first, exactly for the reason Hannah gives — before the mind gets polluted by the feed. (The multi-lens fan-out in Gap 8 is the team version of this same exercise.)

### Gap 3 — No far-transfer hunt (adjacent is listed, unrelated is where the magic lives)

**What Hannah does.** Her best finds are consistently from outside the category: swimwear (Pepper Mayo) and cotton dresses (Pact) feeding a period-underwear round (concepting recording 1); refrigerators feeding rugs (Jun 3); a hair-mask tutorial and a sardines ad logged as format fuel (concepting recording 1: "I know this is about sardines... there are so many things about this that are working"). "There's nothing new under the sun, so where do we go to find inspiration is in the past" and the deliberately-unpolluted lanes nobody else mines.

**What the system does today.** Source surface 4 is "affinity brand paid ads — close-but-not-direct rivals." Close is as far as the skill reaches. Nothing pushes the hunt into unrelated categories that share a mechanism.

**Structural fix.** A required far-transfer lane in every weekly run: two or three deliberately unrelated categories or domains, rotated week to week and logged in the run output so the rotation is auditable and doesn't repeat, hunted for *mechanisms* (a format, a visual device, a story shape) rather than messages. The spark field (Gap 1) is what makes this lane productive — a mechanism with no brand collision is a dead log; the entry ships as mechanism + spark. The lane picks its categories from the brand's persona world (where does this buyer actually spend attention beyond the category), which the hunt brief (Gap 4) supplies.

### Gap 4 — The hunt isn't primed with the live account read

**What Hannah does.** Before she scrolls one video she's holding: the diagnosis ("my head is really centered around the disc right now," Jun 3), the personas ranked by confidence, what's working right now ("it is working right now... we don't break something that is working," Jun 11, on Hanky Panky), and what's been tried and failed ("authority hooks, clinical language, polished studio aesthetics — yep... we want to stay away from those," concepting recording 1). And she re-hunts per lane after personas lock: "once we have the personas nailed down... I will likely have to do one more round of inspiration just in the lane of thinking of that persona" (Jun 3).

**What the system does today.** "Weekly, centered on the brand's Phase-2 priorities" — one line of orientation, no required artifact, nothing that stops a run from harvesting an angle the account already burned or ignoring what the bank is starving for.

**Structural fix.** A hunt brief as a gate: harvest cannot open a feed until it has assembled and emitted a short pre-hunt artifact containing (a) the roadmap's ranked priorities and personas by confidence, (b) a live what's-working-now pull from the ad account, (c) the tried-and-failed angle list per active SKU, (d) the last evaluation's "what the bank is starving for" read, and (e) the week's user-signal read (Gap 5). The brief appears in the run output or the run is invalid — an output contract, not an instruction. The lanes of the hunt (which personas, which SKUs, which far-transfer categories) are derived from the brief, which also gives every entry's `justification` something concrete to point at.

### Gap 5 — Nobody reads the room (the user-usage loop Jimmy asked for)

**What Hannah does.** She read Saalt's own Parker chats and immediately extracted signal: "Claire was like, write me five ads for my launch for organic cotton... and took the first pass" (Jun 5) — what the team is trying to make, what bar they're accepting, where Parker is being underused. Jimmy's ask is explicit: learn from how the users are using Parker to go out and find more ideas.

**What the system does today.** "User conversations, manual ideas-tab saves" sit in source surface 6, the bottom of the list, with no defined pass. Dream reads comms but for a different purpose (proposals, not hunt fuel).

**Structural fix.** A user-signal pass inside the hunt-brief assembly: read the week's chat history (`search_chat_history`) and ideas-tab saves for (a) creative asks — what the team tried to generate, launch, or brief this week, (b) ideas mentioned in passing that never got logged, (c) rejections and their reasons. Asks become hunt targets for this run's lanes; passing ideas get logged with conversation provenance; rejections feed the fit notes. This is bounded and cheap — it's a read of one week, not an archive crawl — and it's the piece that makes the harvest track what the team actually needs instead of what the roadmap said a month ago.

### Gap 6 — Weekly is too slow for trends

**What Hannah does / wants.** "This was just posted yesterday... **Parker can do this every single day**. Every single day can be sourcing these kinds of ideas and providing them to the end user — should I log this as an idea, and we say yep, and it goes straight into the icebox... or Parker could be like, I found this new trending video in the period space, here are three ways I could see it working for Saalt" (Jun 3). The best find of that whole session was a video from the day before.

**What the system does today.** Harvest is weekly. ideation-and-brainstorming.md names the daily-pulse idea in "What this means for Parker" but nothing implements it.

**Structural fix.** A daily trend pulse as a small scheduled routine (registered by setup-routines alongside the others): one bounded pull of what's trending in the brand's space today (organic first, `search_tiktok_videos` / organic social tools), articulation-test the top handful, and surface each keeper as a should-I-log-this with two or three sparks attached. Kept deliberately small — minutes of work, a handful of candidates, no grading — so it doesn't duplicate the weekly deep hunt. Yes-decisions land in the bank through the existing brand-idea-bank-maintenance path.

### Gap 7 — The old-ads gold mine has no mine

**What Hannah does.** "It's my secret sauce... if you could create a database of print ads like this... no one else is doing that" and "training Parker on old ads is really important to me, personally, because I just don't think any other LLM will be doing that — they're going to find shortcuts for today's way of thinking" (Jun 3). She names the sources: All-American Ads (categorized by industry), Life magazines (where the advertorials lived). She uses them for copy, visuals, and whole concepts, and her reasoning for why they're rich is craft economics: print shoots cost so much that every ad carried hours of confidence.

**What the system does today.** Old print ads are source surface 2 in the skill — but there's no archive, no corpus, no retrieval path. As shipped, that source line is a wish. A harvest run that "checks old ads" today has nowhere to look.

**Structural fix.** Stand up an old-ads swipe corpus as a real asset. Start scrappy and legal: public-domain and openly archived material (archive.org hosts decades of Life magazines; other public ad archives exist), organized by industry and by mechanic (grid ads, comparison lines, avatar callouts, demonstration visuals), each entry carrying the era, source, and a narrative read of the visual per the existing source-capture standards. Wire the retrieval path into harvest so the print-ads lane has a mine to dig in, with live web archive search as the fallback. This is the one proposal that's an asset build rather than a pipeline change, and it's also the most defensible moat — her words, not mine. Copyright care: capture describes and links; it doesn't reproduce whole creative works into brand outputs.

### Gap 8 — One brain, one pass

**What Hannah does.** Her process is soaked in other strategists: the creative-strategy hotline ("eight women telling me the same thing," May 29), Sarah Levinger's market read that reshaped the Saalt diagnosis (Jun 11), Alex Cooper as a sounding board ("Alex, okay, here's the — what do you think from your mindset... back up your thinking," Jun 5). And she named the design implication herself: "you can have the same account, two different brains on it, and completely different creative outcomes... to have that may be important for Parker in the long run" (Jun 5).

**What the system does today.** One harvest pass, one disposition.

**Structural fix.** The weekly hunt fans out as a small workflow: three or four hunter lenses with genuinely different dispositions — the customer-language purist (reviews, comments, Reddit), the format hunter (organic + affinity paid), the historian (old-ads corpus), the wildcard (far-transfer lanes) — each producing candidate entries against the same hunt brief, then a dedupe and articulation-test merge before anything is written to the bank. Diversity of disposition is enforced by the lens prompts' different source assignments and different tastes, not by asking one pass to "think diversely." Capture stays generous; the merge dedupes, it does not grade.

## The redesigned weekly run, end to end

1. **Assemble the hunt brief** (gate — Gap 4 + Gap 5). Roadmap priorities and personas by confidence; live what's-working pull; tried-and-failed per SKU; last evaluation's starving-for read; the week's user signals. Emit it.
2. **Cold pass** (Gap 2). Notepad first, feeds closed. Log survivors.
3. **Fan out the hunters** (Gap 8) across the lanes the brief set: persona/SKU lanes on organic, affinity paid, comments, Reddit; the historian on the old-ads corpus (Gap 7); the wildcard on this week's far-transfer categories (Gap 3).
4. **Merge**: dedupe, articulation-test, write entries — verbatim source intact, winning elements named, `spark` where it landed naturally (Gap 1), full provenance and viewable links per the existing contract.
5. **Emit the run summary**: what was hunted, which lanes, which far-transfer categories were used (for rotation), what was logged, what was seen and skipped and why in one line.
6. **Hand off to evaluate-ideas**, unchanged. The grading pass now also has the spark to grade, which should sharpen its "which lever does it pull" read.

Alongside the weekly run: the **daily trend pulse** (Gap 6) as its own small routine.

## Schema changes (prompts/ideas-and-briefs/brand-idea-bank.md + entry schema in the skill)

- Add `spark` — one breath, the brand collision, only when it comes naturally; empty with a note otherwise.
- Add `source_type` values: `cold-brainstorm`, `far-transfer`, `old-ad-corpus`, `user-conversation` (formalized), `trend-pulse`.
- Add `hunt_lane` — which lane of the run produced it (persona/SKU lane, far-transfer category, cold pass), so evaluate-ideas and the starving-for read can see coverage per lane, not just per source type.

## Doctrine boundary and propagation

The spark change touches a real doctrine seam. The rule "source capture never contains adaptation" stays fully intact for competitor-profile, inspiration, and affinity *source-capture docs* (attribution-principle territory). The idea bank is declared what it actually is — the strategist's own icebox — and gets the spark. The propagation pass (run through update-parker-skill) must touch, at minimum: harvest-ideas SKILL.md, brand-idea-bank-maintenance SKILL.md, prompts/ideas-and-briefs/brand-idea-bank.md, ideation-and-brainstorming.md (which already half-documents the spark in its articulation-test section — the method doc and the skill currently disagree, and v2 resolves it in the method doc's favor), evaluate-ideas (to read the new fields), and a sibling-check across the competitor-profile prompts to confirm the boundary language stays put. system/master-file-structure.md and the doc map regenerate if any doc moves or gains a summary.

## Build order

1. **Spark field + rule rewrite + schema** (Gap 1) — highest leverage, smallest diff, unlocks the value of everything else.
2. **Hunt brief gate + user-signal pass** (Gaps 4, 5) — makes every hunt strategy-true and team-true.
3. **Cold pass + far-transfer lane** (Gaps 2, 3) — the two missing methods; both depend on the brief for lanes.
4. **Daily trend pulse** (Gap 6) — small standalone routine.
5. **Multi-lens fan-out** (Gap 8) — pipeline upgrade of the weekly run once 1–3 are stable.
6. **Old-ads corpus** (Gap 7) — the asset build; start scrappy, grow continuously.

## Open questions for Jimmy

1. **Spark scope.** Comfortable with the spark being *required when it lands naturally* and *empty otherwise*, with the articulation test as the line? Or should it stay optional everywhere to keep capture friction at zero?
2. **Daily pulse surface.** Its own scheduled routine, or a bucket inside dream's morning suggestion so the team gets one daily touchpoint instead of two?
3. **Old-ads corpus home.** Global (factory ships it to every brand brain) or per-brand (each brain grows its own from its industry)? Global-with-industry-tags seems right, but it's a real storage and licensing decision.
4. **Chat-history consent.** The user-signal pass reads the team's Parker conversations weekly. Hannah did exactly this and found it valuable, but it should probably be named plainly to teams during onboarding. Where does that disclosure live?
5. **Multi-lens cost.** The fan-out multiplies harvest cost roughly by the lens count. Fine for the weekly cadence, or should lens count scale with account size?

## Execution record (2026-07-09)

Jimmy approved with one change: everything stays weekly — the daily trend pulse became a trend lane riding inside the weekly hunt's format-hunter lens. Defaults taken on the other open questions: spark is required-when-natural / empty-otherwise with the articulation test as the line; the old-ads corpus is global with industry tags; the chat-reading pass carries a one-line plain disclosure in the harvest skill; lens count is fixed at the four named lenses weekly.

The durable doctrine decision this trace records: **the no-adaptation rule is scoped by surface, not universal.** Competitor/inspiration/affinity source-capture docs stay purely descriptive (attribution-principle, unchanged); the idea bank is the strategist's own icebox and carries the spark — the one-breath brand collision — because deferring the combination to concepting loses it. The prior harvest rules had borrowed the source-capture boundary into the icebox, which contradicted both the transcripts and the articulation-test section of the canonical ideation doc; resolved in the method doc's favor.

Files changed: `global/knowledge/creative-strategy/ideation-and-brainstorming.md` (canonical: spark doctrine + structured weekly hunt + corpus pointer), `prompts/ideas-and-briefs/brand-idea-bank.md` (schema: spark, hunt_lane, new source types; rule 1 rescoped), `.claude/skills/harvest-ideas/SKILL.md` + template copy (full v2 rewrite), `.claude/skills/evaluate-ideas/SKILL.md` + template copy (spark/lane reads; also fixed pre-existing factory-vs-template drift by aligning to the template's sprint-plan language), `.claude/skills/brand-idea-bank-maintenance/SKILL.md` (alignment), `templates/brand-routines/schedules/ideas-weekly.md` (v2 run shape), new `global/knowledge/creative-strategy/old-ads/` (README + INDEX scaffold), `scripts/propagate-to-brand-brains.sh` (corpus seed-or-add in both layout branches), `system/parker-system-map.md` + `system/master-file-structure.md` (index updates), `expertise-routing.md` doc map regenerated. Standing brand brains need a propagate run after merge.
