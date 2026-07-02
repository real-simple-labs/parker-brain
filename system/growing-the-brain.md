# Growing the brain — the scaffold is a floor, not a ceiling

> Runtime system doc: ships into every brand brain at `parker-system/system/growing-the-brain.md`. It governs how a standing brain expands when the org connects new tools or asks about domains the original build never covered.

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
- if the domain needs its own generating prompt, author it in the brain's `parker-system/prompts/` following the prompt standards that shipped with the brain, so the refresh routine can re-run it instead of improvising. The brain carries the method for writing its own generators; growing one is normal, not exceptional.

**6. Tell the user what grew.** A new surface is a real change to what the brain is. Name it plainly when it happens: what got created, what feeds it, what it will be watched for. The team should always be able to answer "what does our brain cover now?" from the map alone.

## Beyond marketing

Nothing above is scoped to marketing. A team that connects the org's whole stack — the CRM, the support desk, the product roadmap, the hiring pipeline — can grow the brain into a genuinely org-wide intelligence, one surface at a time, and the marketing core stays intact as the first and deepest region rather than the boundary. The constraint is never the folder tree. It is only whether real data has arrived and whether each new surface keeps the standards that make the brain worth trusting.
