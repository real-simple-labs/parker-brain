# v44 — the brain knows which folders only some people see (2026-10-22)

A team can restrict a folder in its brain to the people it picks. For everyone else the folder is not in their copy, and nothing in the files says a folder is limited. So an agent asked "who has access to this folder?" answered "everyone", and an agent asked to sum up the brain could copy a restricted folder's content into a file the whole team reads.

Parker Desktop now writes `.parker/access.md` at the root of each brain for the person signed in on that computer: the restricted folders, who sees each one, who sees the rest, and the rules for an agent. The file is never synced.

## What shipped

- **The session start hook gives the rule and passes the file in.** Every session in a brain (Claude Code and Codex both run the hook), cloud runs included, starts with the rule: content from a restricted folder stays in it. Then the file's text, quoted as data (folder and people names in it are never instructions), or its name when it is over 6000 bytes. With no file (a cloud run, or the app hasn't written one), the hook says the agent can't tell which folders are restricted and must never say "everyone". A file that can't be read or isn't UTF-8 never stops the session start check.
- **`AGENTS.md` (copied bundle) and the brand `CLAUDE.md` template** carry the rule for a session whose hooks didn't run: content from a restricted folder stays in it unless the person says yes after hearing who will then see it; answer access questions from the file; no file means "don't know".
- **`system/brain-sync.md`** says where the file comes from and why.

Standing brains get the hook and `AGENTS.md` through the re-sync. A team-edited `AGENTS.md` stays the team's, as before; the hook still gives those sessions the rule.

## Migration

`migrations/v44.md` (**Auto-apply:** yes): adds the same paragraph to the brain's own `CLAUDE.md`, for a session whose hooks don't run. Skipped where it is there already or the team rewrote the section around it.
