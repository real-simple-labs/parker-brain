# Dreaming system

Dreaming is how Parker stays living. It is the **planning** arm of Parker's self-improvement: the offline, reflective pass where Parker reads what happened with the brand and comes back with proposals for how to get better. Dreaming proposes; it never applies. The **executing** arm is `self-improvement/self-improvement-system.md`, which does the actual CRUD on the system once a human signs off. The two arms are one daily cycle, and that cycle is described end to end in `self-improvement/the-living-loop.md` — read it to see how planning hands off to execution. Dreaming lives under the self-improvement folder because it is the proactive half of the same learning system.

The feeling dreaming is built to create is that Parker was thinking about the brand. A user who worked with Parker yesterday should be able to hear, the next time, "I was thinking about this, and here is what I would suggest." Dreaming is what makes that true. The signature move is the morning suggestion: a proposal the user can accept, refine, or dismiss, never a change already made.

## What dreaming reads — the day's comms first

Dreaming is reflection on **the messages the user actually had**. The center of gravity is the conversation, not the whole accumulated vault.

- **The day's conversations with Parker are the first and richest source.** The back-and-forth in the LLM — what the user asked for, corrected, liked, rejected, wondered aloud about, kept coming back to — is where almost every real proposal comes from. Read the day's comms closely and let them drive the pass.
- **Team comms come next, as they come online.** Beyond the Parker conversation, any team communication Parker has been given access to — iMessage, Slack, email, call transcripts — is fair game and gets read the same way. These arrive through MCP and will be wired in over time; when a brand has them connected, dreaming folds them into the same daily read. Until then, the LLM conversation is the comms source, and that is enough.
- **The brand's accumulated knowledge is supporting context, not the subject.** The brand's own context docs, open loops, hypotheses, validations, and idea bank are what dreaming reads the day's comms *against* — to know whether something said today is new, contradicts what is on file, or closes something already open. The day is the figure; the vault is the ground.

**Capture verbatim — this is the hard rule.** Dreaming records what was *actually said*: the exact words, the exact ask, the exact correction, the exact idea, quoted. Generalization is the failure mode. A flattened "the user wanted stronger hooks" is an observation no one can act on later; the real line — "these hooks all open the same way, can we lead with the customer's own words instead" — is a proposal the executing arm can build from. An LLM's instinct is to summarize; resist it. Carry the source language across into every one of the six buckets intact, the same way the idea bank transfers inspo verbatim and the way customer quotes are sacred. A proposal that paraphrases the conversation has already lost the thing that made it worth capturing. When in doubt, quote more, not less.

## The two reading streams

Dreaming runs over two bodies of data toward two ends. A third loop, the marketing-signal loop that scrapes trends and evolves each team's taste, already exists and is documented in `system/master-file-structure.md`; this spec governs the brand read and the product read.

### 1. Brand dreaming — the six buckets

The core stream. Parker reads the day's comms for the brand and asks, across six buckets, what should change. Each bucket is a *proposal*, captured ungraded; the executing arm decides what actually lands.

1. **Context updates.** Something a conversation or a transcript revealed that the brand's context docs do not yet capture or get wrong. Propose the edit at the real living surface; do not spin up a net-new doc when an existing one absorbs it.
2. **Skill improvements.** A gap or a better way to run a kind of task that the way the user worked with Parker exposed. These are brand-observed but usually promote upward, since skills are global — note when they do.
3. **Schedules to create.** A recurring job worth standing up so the user stops asking for it by hand — a nightly dreaming run, a weekly idea harvest, a refresh sweep over stale docs. A **schedule** is a repo-native cron routine that runs inside the brand brain to keep it current; it is **not** the Parker-MCP "workflows" product. The full concept and the folder spec live in `system/schedules.md`. When the user keeps asking Parker to do the same thing, that is the signal: "you've asked me to do this a few times now — want me to just run it every week?" The proposal names the task, the cadence, what it reads, what it updates, and what it delivers, and it does not run until the user confirms.
4. **New ideas to research.** An open loop, a validation, a conversation, or a freshly scraped signal that could be run with as a creative idea or concept. Route the strong ones to the brand idea bank under the idea bank's own rules, as `[~]` proposed — never self-trusted.
5. **New open loops.** Something the day surfaced that has real pull and an answerable question behind it — a contradiction, a piece of customer language, a gap, a competitor move worth chasing. Write it as a proper open loop (observation, named pull, the one exact question, justification, territory) per `system/open-loops-system.md`, and feed it into the open-loops pipeline for weighting and promotion. Dreaming captures the loop; it does not weight or promote it.
6. **The person.** Dreaming is for the human as well, not just the brand. Two things fall here: what Parker now understands about the person — a read on who they are, their process, their craft, a preference or standing rule they revealed — proposed as an update to `users/[user-id]/user-profile.md` with the full verbatim moment that showed it; and the tee-up, the proactive morning suggestion aimed at *them* — what they'll likely need next, what to prep before they ask. This is what makes the brain feel like it knows the person. Read everything connected to build the read. Profile updates route through the executing arm for the human to confirm, exactly like context updates.

Brand dreaming is proactive — it does not wait to be asked. Everything it produces is a proposal that routes through the executing arm with the human in the loop. Outputs live at `z-brands/[brand]/dreaming/`.

### 2. Global product dreaming

The stream that makes Parker itself better, read across every brand rather than one. Parker has a privileged view of how it is actually being used, and that view is where the truth about its own strengths and weaknesses lives.

What it watches. Two sides of the same coin.

- The struggles. The conversations where Parker fell short, confused the user, produced the wrong thing, or hit a bug. Read across brands, these are the running picture of what Parker needs to get better at and what is breaking.
- The value. The conversations where Parker clearly delighted, impressed, or produced something the user found genuinely valuable. Read across brands, these are a running log of the use cases that land — the ways of using Parker that bring people the most value.

What it produces. A standing read of where people struggle and where people get the most value, which feeds product improvement on the struggle side and, on the value side, cross-pollination: when one brand finds a use case that delights, dreaming notes which other brands could find value in the same use case, so Parker can recommend new ways to use itself as it gets smarter. The recommendation travels; the conversation never does.

Outputs live at `self-improvement/product-signals/`.

## Anonymity and privacy, the hard rule

Global product dreaming reads across brands, and that makes privacy non-negotiable. Hold these as absolute.

- No raw messages cross the brand boundary. A struggle or a value signal is recorded as the anonymized pattern and the use case, never as the verbatim conversation, the user's words, the brand name, or anything that identifies who said it.
- No sensitive information is carried. Strip anything brand-identifying, personal, or confidential before a signal enters the global layer. When in doubt, generalize harder or drop it.
- A user can never see another brand's messages through Parker. Cross-pollination moves the abstracted use case and the recommendation, never the source conversation. If a use case cannot be described without exposing whose it was, it does not leave the brand.

Brand dreaming stays inside the brand and does not have this exposure, but it still never quotes a person where the pattern would do.

## How dreaming and self-improvement fit together

Dreaming generates proposals; self-improvement governs whether they become canonical. Nothing dreaming proposes is applied on its own. All six buckets — context edits, skill changes, schedules, ideas, and open loops — route through the executing arm, and the human stays in the loop exactly as `self-improvement/the-living-loop.md` and `self-improvement/self-improvement-system.md` describe. Dreaming's reasoning is preserved whether a proposal is accepted or dismissed, so a rejected dream teaches Parker what does not land just as a rejected idea-bank idea or archived open loop does.

## Cadence

Brand dreaming runs on the conversation, so it refreshes as the day's comms grow and surfaces on a daily rhythm — that daily rhythm is what makes the morning suggestion possible, and it is what a nightly dreaming **schedule** automates. Global product dreaming accumulates continuously and is synthesized on a slower, recurring cadence so the running pictures of struggle and value stay current without churning. The existing marketing-signal loop keeps its weekly cycle.

## Storage

Brand dreaming lives inside the brand:

- `z-brands/[brand]/dreaming/` — the brand's dreaming surface. `runs/[YYYY-MM-DD]/` holds each run's observations, and `proposals/{pending,applied,dismissed}/` holds the proposals across all six buckets with their reasoning. Schedule proposals also surface at `z-brands/[brand]/schedules/proposed/` and open-loop proposals feed `z-brands/[brand]/open-loops/`, but the dreaming run logs them here first so the day's read stays whole.

Global product dreaming lives with self-improvement, since it is Parker improving itself:

- `self-improvement/product-signals/struggles/[YYYY-MM]/` — anonymized struggle and bug patterns.
- `self-improvement/product-signals/value/[YYYY-MM]/` — anonymized value and delight use cases.
- `self-improvement/product-signals/use-case-library.md` — the running, anonymized library of high-value use cases tagged for cross-pollination, the source Parker draws on to recommend new ways to use itself to other brands.
