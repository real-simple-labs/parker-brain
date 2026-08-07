# Growing the brain — the scaffold is a floor, not a ceiling

> Runtime system doc: reaches every brand brain inside the `parker-system/` mount, at `parker-system/system/growing-the-brain.md`. It governs how a standing brain expands when the org connects new tools or asks about domains the original build never covered.

The build hands a team the performance-marketing core: the ad account read, the personas, the voice of customer, the competitors, the strategy on top. That is the part Parker can construct cold from the brand's marketing data, and it is where most teams start. It is not where the brain ends. The brain is org-shaped, not channel-shaped: every connector the team adds and every domain they bring to it is a new part of the business the brain can learn, by the same rules the original build followed. The folder tree the build produced is the buildable core — the floor. Nothing about it is a cage.

The same principle that governs claims governs structure: taxonomies are lenses, not cages. Forcing email-lifecycle truth into `audits/` because that folder exists, or dropping the org's support-ticket themes into `running-notes/` because nothing better exists, is the structural version of forcing a gray claim into a rigid bucket. When the truth doesn't fit the shape, grow the shape.

## When to grow

Grow when real data arrives, never speculatively. Three triggers:

1. **A new connector comes online.** The team wires in a tool the brain hasn't seen — an email platform, a CRM, site analytics, a support desk, a podcast host, retail or wholesale data, anything with an API or MCP.
2. **A recurring ask has no surface.** The team keeps asking about a domain the brain has no home for, and the answers keep getting assembled from scratch instead of from a standing doc.
3. **A connected tool carries homeless truth.** A source the brain already reads keeps surfacing a kind of knowledge no existing doc captures.

Do not scaffold empty folders for domains nobody has connected and nobody asks about. An empty speculative surface is noise in the map and a false promise in the tree. The brain grows like an organization does: when the work shows up.

## How to grow

**1. Read what truth lives there.** Before creating anything, survey the new source the way Phase 0 surveys Parker MCP: what does this tool actually know? What in it would change a strategic answer? What of it does the brain already capture elsewhere, and what has no home? Say what you find in plain language before proposing structure.

**2. Give it a home, not a shoehorn.** Two honest outcomes:

- **It extends an existing surface.** Another review source feeds voice-of-customer. A second ad channel extends the audit layer with its own cuts. A project tracker folds into `running-notes/current-work.md`. When the truth is the same *kind*, fold it in and note the new source in the receiving doc's provenance.
- **It is a genuinely new domain.** Email lifecycle, SEO, PR and comms, partnerships, retail, customer support, recruiting — when the truth is a new kind, stand up a new first-class surface: its own top-level folder, its own sub-context doc or docs, and, when the domain has a moving present tense worth watching, its own audit cadence. A new domain is a sibling of the marketing core, never a tenant inside `audits/` or `running-notes/`.

**3. Hold every new surface to the same standards as the originals.** Growth does not relax the rules; the rules are what make a new surface trustworthy:

- every claim labeled stated, inferred, verified, or data-limited, with provenance per the attribution rules in `CLAUDE.md`;
- `generated_on` and `refresh_by` stamped, and a line added to `running-notes/refresh-schedule.md` so the freshness watch covers it;
- an `INDEX.md` once the folder grows past what the map can enumerate;
- open loops emitted in the canonical form when the new domain surfaces real unresolved questions.

**4. Wire it into the maps, in the same pass.** A surface the planner cannot see does not exist. The same rule the factory applies to its own canonical locations applies here: creating the surface and registering it are one change, not two.

- add it to `CLAUDE.md`'s "## The map" with one honest line on what it holds;
- add it to the vault index in `brand-profile.md` so the planning pass sees it on every question;
- add its docs to `running-notes/refresh-schedule.md`.

**5. Wire it into the loops.** The living layer has to know the new surface exists, or it will quietly go stale while everything else refreshes:

- `refresh-context` re-runs its docs on their cadence, same as any standing doc;
- `dream` reads it as part of the day's picture, and dreaming is also where growth usually starts — when a connected tool carries truth with no home, the right first move is a dreaming proposal for the new surface, disposed by `self-improve` with the human in the loop;
- if the domain needs its own generating prompt, author it in the brain's own `prompts/` folder at the repo root (create it on first use — the `parker-system/` mount is read-only, so brain-authored generators live beside it, following the same prompt standards it carries). The refresh routine treats both homes as generator sources: factory prompts under `parker-system/prompts/`, the brain's own under `prompts/`. The brain carries the method for writing its own generators; growing one is normal, not exceptional.

**6. Tell the user what grew.** A new surface is a real change to what the brain is. Name it plainly when it happens: what got created, what feeds it, what it will be watched for. The team should always be able to answer "what does our brain cover now?" from the map alone.

## Growing a skill, not just a surface

Everything above grows the brain sideways — new domains, new surfaces, new kinds of truth. A brain also grows *downward*, into how well it does the craft it already does. That happens when the team has a real body of their own work and the factory method never sees it.

The factory craft skills are deliberately general. They carry the method — how a hook earns attention, how a script sounds spoken, how an iteration is chosen — and they are written to work for a brand the factory has never met. A team that has produced three hundred scripts for one brand holds something the method cannot: the actual answer to "how do *we* write this." That corpus usually lives outside the brain, in Notion, Airtable, a Drive folder, a spreadsheet, or in Parker itself, which holds every script from every ad the brand has run.

**A fine-tuned skill is a brand-authored sibling of a factory skill, built from that corpus.** It does not replace the factory method; it specializes it. Build one when three things are true: the team has a real corpus (dozens of pieces, not a handful), the craft is one they have a distinct house style in, and the generic output keeps needing the same corrections.

**How to build one.**

1. **Read the whole corpus, not a sample.** Reach it through whatever tool holds it — the Notion or Airtable connection, the ad account through Parker MCP, the brain's own `sprints/`. Say how many pieces you read and where they came from; a fine-tune built on twelve scripts is a different object from one built on three hundred, and the doc should be honest about which it is.
2. **Extract the profile docs first, the skill second.** What comes out of a corpus read is usually a script-voice profile (the sound: cadence, sentence length, how the brand opens, what it never says) and a visual vocabulary (what the brand has actually filmed and can film again, per `creative-strategy-context/visual-vocabulary-method.md`). Those are brand docs and belong in the vault. The fine-tuned skill sits on top of them and encodes the *process* differences — the beats this team uses, the structures they return to, the moves they have rejected.
3. **Write it as a delta, not a fork.** The fine-tuned skill references the factory skill and states what is different for this brand. A full copy of the factory method with a few lines changed is the drift anti-pattern: the copy stops receiving factory improvements and nobody can see what was actually brand-specific.
4. **Keep the provenance.** Every rule in it carries what it was derived from — how many pieces, from which surface, over what window — per `system/attribution-principle.md`. A fine-tuned rule with no corpus behind it is just an opinion that outranks the method.

**Where it lives, and why that matters.** The fine-tuned skill goes in the brain's own `.claude/skills/`, alongside the copied factory skills but **under a distinct name** — `<brand>-scriptwriting`, not `scriptwriting`. This is not cosmetic. `scripts/sync-executable-layer.py` refreshes the copied executable layer on every pin bump against a bundle map of factory skill names; a brand-authored skill whose name is not in that map is invisible to the sync and survives every update untouched. A name that collides puts the team's work in the path of the refresh. Nothing is ever deleted by the sync, but a distinct name is what keeps a fine-tune permanently the team's own.

This is also why a fine-tuned sibling beats the alternative. Editing a copied factory skill in place works, but that file is then frozen at the team's version while the factory's moves on. A separately-named sibling takes factory updates through the skill it references *and* keeps the brand specialization. It is the third and best option on the adaptation ladder: put the adaptation in brand docs when it fits there, build a fine-tuned sibling when it is a real process difference backed by a corpus, and edit a copy in place only when neither works.

**Precedence.** Once a fine-tuned skill exists for a craft, it is the default for that craft, and the factory skill is the fallback and the underlying method it builds on. Register it in the brain's root `CLAUDE.md` — its "## The map" entry for `.claude/skills/`, and the execution-routing rule — so the planning pass routes to it rather than rediscovering it. A fine-tuned skill nobody routes to is the same as no fine-tune at all.

**Keep it current, or retire it.** A corpus grows. Put the refresh on the brain's own cadence — re-read the window since the last run, fold in what changed, re-stamp the dates, and add the doc to `running-notes/refresh-schedule.md` like any other standing surface. A fine-tune built on last year's work quietly teaches the brain to write like the brand used to.

**The same pattern generalizes past scripts.** Any craft the team has a real body of work in can carry one: the iterations they have run, the statics they have designed, the briefs they have written, the feedback they have given. And the corpus does not have to be finished work — a client channel's full feedback history, or every note a creative director has left, is a corpus about taste rather than output, and it fine-tunes the same way.

## Beyond marketing

Nothing above is scoped to marketing. A team that connects the org's whole stack — the CRM, the support desk, the product roadmap, the hiring pipeline — can grow the brain into a genuinely org-wide intelligence, one surface at a time, and the marketing core stays intact as the first and deepest region rather than the boundary. The constraint is never the folder tree. It is only whether real data has arrived and whether each new surface keeps the standards that make the brain worth trusting.
