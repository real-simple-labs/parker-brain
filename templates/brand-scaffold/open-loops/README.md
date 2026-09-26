# Open loops

The brand's open strategic questions: the things Parker can't answer yet that would change the strategy if it could. Every context doc ends with its own open loops; this folder is where they get collected, graded, and routed.

## What lives here

- `[YYYY-MM-DD]-consolidated-roll-up.md`: the current agenda. The roll-up prompt (`parker-system/prompts/open-loops/open-loops-roll-up.md`) gathers every doc's loops, drops the ones not worth researching, scores the rest, and writes this file. Each new roll-up supersedes the last one by name.
- `promoted/[YYYY-MM]/[loop-slug].md`: one file per loop that made the cut, carrying everything the next step needs to turn it into a hypothesis.
- `archived/[YYYY-MM]/[loop-slug].md`: one file per loop that didn't, with the reason, so nobody re-argues it blind.

## Where a loop goes next

Promoted loop, then a hypothesis in `../hypotheses/`, then a verdict in `../validations/`, then a scheduled re-check in `../re-validations/` if the finding can go stale. The weekly `/research-loops` routine runs that whole chain. The rules for every stage are in `parker-system/system/open-loops-system.md`.

A new brain starts with this folder empty. The first roll-up runs at the end of the build's first phase, once the context docs exist to feed it.
