# Creative Strategy Parker Taste Idea Bank

This is Parker's cross-brand creative idea bank: the place where reusable creative ideas worth stealing live, regardless of which brand they came from.

## Why the idea bank exists

An idea bank is not a list of ads Parker liked. It is a working library of ideas Parker has actually learned. The test for an entry is not "is this a good ad" — it is "does Parker understand this idea well enough to apply it the way a strategist who studied it would."

That is why every entry carries its reasoning. An idea saved without the why behind it is a screenshot; nobody can trust it or build on it later. The reasoning is what makes the idea reusable: it explains the mechanism that makes the idea work, so Parker can run the idea in a new context instead of copying a surface. When Parker reaches into the idea bank during concepting, it should be pulling a principle it owns, not a template it is mimicking.

So Parker embraces each idea and makes it its own. The standard is the same as a person watching a great breakdown video and walking away able to apply the lesson — not able to recite the example, able to use the idea. The example is how the idea is taught; the principle is what gets reused.

## What belongs here, and what does not

- Cross-brand creative taste belongs here — an idea reusable across many brands.
- Brand-specific ideas belong at `z-brands/[brand]/idea-bank/`, where the same per-idea standard applies.
- Expert-sourced signals start in `creative-strategy-context/expert-insights/`, then route here only once they have become a reusable creative pattern rather than a raw signal.

## The idea must be new to Parker

This is the precondition for everything below. The idea bank is a library of ideas that are new to Parker — things it did not already know how to do. Its whole value is that it captures what Jimmy is teaching Parker, not what Parker already has.

So before an idea can be proposed, Parker verifies it is actually new. It searches what it already knows — the skills and their processes, the creative-strategy context docs, the knowledge docs, the existing idea-bank entries — and asks whether this idea is already covered. If Parker already has it, it is not an idea-bank idea, no matter how good it is.

When an idea is already covered, route it to where it lives instead of duplicating it. A re-framing-a-winner idea is an iteration move and belongs in the iterations skill, not the idea bank. A hook structure already in the hooks doc belongs there. Sharpen the existing surface if the source adds something; do not mint a redundant idea-bank entry. An idea-bank entry is reserved for the genuinely new.

Every proposed entry states what Parker checked and why the idea cleared the bar — the surfaces searched and the closest existing thing it is not a duplicate of. An idea that cannot clear that check is not proposed.

## Folder structure

The idea bank is a folder system, not one running list. A single growing list bloats and rots; folders keep each idea legible and let an idea grow without crowding the others.

- Each idea gets its own folder, named with a short kebab-case slug.
- Inside the folder, `idea.md` holds the idea, its reasoning, and the examples that teach it.
- An idea folder is a parent that can hold children: child folders for variations of the idea, brand-specific instances, or saved example assets. Nest when an idea spawns enough material to deserve its own sub-structure; keep it flat when it does not.
- `INDEX.md` is a thin pointer list to every idea folder. It is a table of contents, never the content.

## The per-idea standard

Every `idea.md` should carry, in narrative prose:

- **What the idea is** — the idea named and described in Parker's own words.
- **New to Parker** — the novelty check. What surfaces Parker searched and the closest existing thing this is not a duplicate of, so the entry shows on its face that it cleared the new-to-Parker bar.
- **Why it's in the idea bank** — the reasoning. The mechanism that makes it work, what makes it durable, and why it is reusable across brands. This is the part that earns trust.
- **Why it works now** — the timing. What changed in the platform, the market, or the tooling that makes this idea work today, and whether it is a durable shift or a cyclical window that will close. An idea without its moment is half-learned; a strategist knows not just why a move works but why it works right now, and when it will stop.
- **How it runs, from the source** — the actual examples discussed in the source, narrated so a reader who never saw them can replay them. This is how the idea gets taught.
- **Making it our own** — the reusable atom, stated as a principle Parker can apply to a new brand. Not how one specific brand should run it; the generalizable move underneath.

Each entry also carries lightweight metadata: source and source type, confidence, the winning elements at play, the stage of awareness it tends to serve, its approval status, when it was last reviewed, and when to monitor it again.

Confidence is honest. An idea sourced only from one expert's claim stays mixed-confidence until Parker sees it work in account data. Saving an idea is not endorsing it as proven; it is committing to understanding it.

## The approval gate

Parker does not fill its own idea bank. It proposes; Jimmy approves. An idea Parker finds — from a knowledge source, an ad-library walk, or anywhere else — enters as a proposal and is not a trusted, active idea-bank idea until Jimmy approves it. This keeps the idea bank a curated library Parker can lean on, not a junk drawer of whatever Parker happened to notice.

The gate uses the same convention as the rest of the system:

- **`[~]` proposed** — Parker drafted the entry, with full reasoning, why-now, and examples, and is asking Jimmy to approve it. It lives in the idea bank but in the pending set, and Parker should not treat it as endorsed taste when concepting.
- **`[x]` approved** — Jimmy reviewed it and approved it into the active set, dated. Now Parker may reach for it as trusted taste.

The status line carries the state and, once approved, the date. Approval is about whether the idea belongs in Parker's taste at all; it is separate from confidence and from whether the idea is later proven in account data. The `INDEX.md` keeps active and pending ideas in separate sections so Jimmy has one place to approve and Parker can tell at a glance what it is allowed to trust.

## Review cadence and archiving

Approval gets an idea in. It does not keep it there. Creative ideas decay: a format saturates as the field copies it, a platform behavior changes, a wrapper that felt native last quarter now reads as an ad. The idea bank has to reflect what is true now, or it quietly turns into a museum that Parker trusts as if it were current.

Rather than carry a live status label, every idea simply records two dates: **when it was last reviewed** and **when to monitor it again**. The interval between them is set by the idea's why-now read — a durable shift gets a long interval, a cyclical window or a fast-saturating format gets a short one. When the monitor date arrives, Parker checks whether the idea still holds and either refreshes it, updating the dates and the why-now, or retires it.

Retiring an idea means archiving it, not deleting it. Ideas are never deleted from the idea bank, because creative formats are cyclical — the green-screen reaction layer is the standing proof, an idea that went quiet and came back. An archived idea is moved to the `_archive/` folder, keeping its full doc, with an added header that records the date archived, the reason, and what would have to be true for it to revive. The why-now read is what tells Parker which archived ideas to expect back.

Parker can re-review and update an idea's dates on its own. **Archiving** an idea and **reviving** an archived idea both cross the trusted-taste line, so both need Jimmy's approval, the same gate as the original approval. Review prompts come from three places: an idea's own monitor-again date, any ad-library walk or audit that observes the field saturating the pattern, and account results when the idea has been tried.
