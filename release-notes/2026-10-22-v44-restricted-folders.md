# v44 — the brain knows which folders only some people see (2026-10-22)

A team can restrict a folder in its brain to the people it picks. For everyone else the folder is not in their copy, and nothing in the files says a folder is limited. So an agent asked "who has access to this folder?" answered "everyone", and an agent asked to sum up the brain could copy a restricted folder's content into a file the whole team reads.

Parker Desktop now writes `.parker/access.md` at the root of each brain for the person signed in on that computer: the restricted folders, who sees each one, who sees the rest, and the rules for an agent. The file is never synced.

## What shipped

- **The session start hook passes the file in.** Every session in a brain (Claude Code and Codex both run the hook) starts with the file's text. A long file is named instead of pasted. With no file on a computer that has Parker Desktop, the hook tells the agent to say it doesn't know who sees a folder, and never "everyone". A cloud run has no app and gets nothing.
- **`AGENTS.md` (copied bundle) and the brand `CLAUDE.md` template** carry the rule for a session whose hooks didn't run: content from a restricted folder stays in it unless the person says yes after hearing who will then see it; answer access questions from the file; no file means "don't know".
- **`system/brain-sync.md`** says where the file comes from and why.

Standing brains get the hook and `AGENTS.md` through the re-sync. The `CLAUDE.md` line reaches new brains only; standing brains already get the same rule from the hook.

## Migration

`migrations/v44.md` is a no-op.
