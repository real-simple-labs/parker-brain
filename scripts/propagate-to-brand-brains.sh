#!/usr/bin/env bash
#
# propagate-to-brand-brains.sh — re-ship the factory methodology bundle into
# standing brand brains, so factory improvements reach brains that were stood
# up earlier. This is the *update-time* counterpart to the onboarding-runner's
# build-time "ship the craft" step (Phase 0). See .claude/skills/propagate-craft/SKILL.md.
#
# It auto-detects the brain's layout and mirrors accordingly.
#
# NESTED brains (current onboarding-runner layout, method bundled under parker-system/,
# all skills in .claude/skills/ where Claude Code loads them):
#   prompts/  -> parker-system/prompts/   (the generating prompts; the brain refreshes itself with these)
#   system/   -> parker-system/system/
#   templates/-> parker-system/templates/
#   global/knowledge/creative-strategy/ -> parker-system/creative-strategy-context/
#   .claude/skills/ (factory craft skills, minus dream) -> .claude/skills/
#   templates/brand-routines/claude/skills/ (routine skills) -> .claude/skills/
#   templates/brand-routines/claude/{hooks/,settings.json} -> .claude/  (added if missing,
#                                          not update-only: the context hook is factory-owned
#                                          machinery and settings.json requires the script)
#
# FLAT standalone brains (legacy layout, craft + system at root, no factory prompts):
#   global/knowledge/creative-strategy/ -> creative-strategy-context/
#   system/                             -> system/  (runtime subset only; --existing
#                                          never adds the factory-internal docs)
#   templates/brand-routines/claude/skills/ -> .claude/skills/
#   templates/brand-routines/claude/{hooks/,settings.json} -> .claude/  (same as nested)
#
# DELIBERATE ADDS: --existing never adds files, so genuinely-new runtime system docs,
# routine skills, and schedule recipes a standing brain should gain are named explicitly
# in each branch (currently: system/growing-the-brain.md, the research-loops and
# update-brain skills and their schedule recipes, and the creative review gates —
# creative-strategy-context/ai-writing-tells.md, .claude/agents/creative-voice-review.md
# + context-grounding-review.md, and scripts/voice-lint.py + grounding-check.py).
# Add new ones there when the runtime ship list grows.
#   (legacy flat brains do not carry factory prompts/ or templates/, so those are skipped;
#    shipped system docs get their global/knowledge/creative-strategy/ refs rewritten
#    to creative-strategy-context/)
#
# After mirroring, it runs scripts/sync-open-loops-core.py against the brain to
# refresh the marker-delimited shared blocks from factory canon — notably the
# parker-voice block in the brain's root CLAUDE.md, which lives outside
# parker-system/ and is never rsynced.
#
# What it PRESERVES (never overwritten or deleted) in each brand brain:
#   - parker-system/creative-strategy-context/_*-lens.md   (brand lens overlays)
#   - parker-system/creative-strategy-context/expert-insights/ (brand intake)
#   - everything OUTSIDE parker-system/ (brand-profile, personas, strategy,
#     audits, competitors, open-loops, running-notes, sub-context-docs,
#     CLAUDE.md, README.md, .claude/, schedules/, prompts-run-log, ...)
#
# Sync semantics: UPDATE-ONLY (rsync --existing, no --delete). It refreshes
# every file the brain ALREADY has to match the factory, but it does NOT add
# factory-only files (so product-internal docs like product-brain-CLAUDE.md,
# repo-boundary-and-promotion-model.md, or the propagate-craft skill never leak
# into a brand brain) and does NOT delete anything (brand-specific files and
# anything the brain intentionally keeps are preserved). Genuinely-new
# methodology docs a brain SHOULD gain are added deliberately, not by this
# sweep — see the skill doc. Brand brains are git repos, so changes are
# recoverable from history.
#
# Usage: scripts/propagate-to-brand-brains.sh [brand-repo ...]
#   If no arguments are passed, set PARKER_BRAND_BRAIN_REPOS to a space-separated
#   local default list.
# Requires: gh (authenticated), rsync, git.

set -euo pipefail

FACTORY="$(cd "$(dirname "$0")/.." && pwd)"
SHA="$(git -C "$FACTORY" rev-parse --short HEAD)"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

REPOS=("$@")
if [ ${#REPOS[@]} -eq 0 ]; then
  if [ -n "${PARKER_BRAND_BRAIN_REPOS:-}" ]; then
    read -r -a REPOS <<< "$PARKER_BRAND_BRAIN_REPOS"
  else
    echo "Usage: $0 [brand-repo ...]"
    echo "Or set PARKER_BRAND_BRAIN_REPOS to a space-separated local default list."
    exit 2
  fi
fi

for repo in "${REPOS[@]}"; do
  echo "============================================================"
  echo "Propagating factory @ $SHA  ->  $repo"
  echo "============================================================"
  dir="$WORK/$repo"
  gh repo clone "jimmyslagle/$repo" "$dir" -- --depth 1 >/dev/null 2>&1
  # Detect layout. Nested brains keep the bundle under parker-system/; flat
  # standalone brains (what the current onboarding-runner produces) keep the
  # craft + system layers at the repo root and the runtime skills under .claude/.
  if [ -d "$dir/parker-system" ]; then
    ps="$dir/parker-system"
    layout=nested
    echo "  Layout: nested (parker-system/)"
    # update-only: refresh files the brain already has; add nothing, delete nothing
    rsync -a --existing "$FACTORY/prompts/"   "$ps/prompts/"
    rsync -a --existing "$FACTORY/system/"    "$ps/system/"
    rsync -a --existing "$FACTORY/templates/" "$ps/templates/"
    rsync -a --existing \
      --exclude '_*-lens.md' \
      --exclude 'expert-insights' \
      "$FACTORY/global/knowledge/creative-strategy/" "$ps/creative-strategy-context/"
    # All skills live in .claude/skills/ — the only place Claude Code loads them on clone.
    # Refresh both the craft skills (from the factory's own .claude/skills/) and the
    # routine bundle (from templates/), update-only so nothing brand-specific is added/lost.
    # Exclude the factory craft `dream` so it never clobbers the brand's canonical routine
    # `dream` (the scheduled dreaming run); the routine bundle below owns that one.
    rsync -a --existing --exclude 'dream' "$FACTORY/.claude/skills/"        "$dir/.claude/skills/"
    rsync -a --existing "$FACTORY/templates/brand-routines/claude/skills/"  "$dir/.claude/skills/"
    # The context hook (settings.json + hooks/) is factory-owned runtime machinery with
    # no brand-specific content, and settings.json requires hooks/craft-context.py to
    # exist — so these two ship together, added if missing, NOT update-only.
    # Per-instance overrides live in settings.local.json (gitignored), never here.
    mkdir -p "$dir/.claude/hooks"
    rsync -a "$FACTORY/templates/brand-routines/claude/hooks/"    "$dir/.claude/hooks/"
    rsync -a "$FACTORY/templates/brand-routines/claude/settings.json" "$dir/.claude/settings.json"
    # Deliberate adds: genuinely-new runtime docs and routine skills a standing brain
    # SHOULD gain. --existing above never adds files, so each is named here once.
    cp -n "$FACTORY/system/growing-the-brain.md" "$ps/system/" 2>/dev/null || true
    # New synced-block source: --existing refreshes the 67 embeds inline but never
    # creates this source file, so name it here to keep the brain's prompts/ a mirror.
    cp -n "$FACTORY/prompts/_reading-level-block.md" "$ps/prompts/" 2>/dev/null || true
    cp -n "$FACTORY/templates/routine-log-template.md" "$ps/templates/" 2>/dev/null || true
    cp -n "$FACTORY/templates/user-profile-template.md" "$ps/templates/" 2>/dev/null || true
    # Routine-bundle seeding: any routine skill the brain is missing (checked by
    # SKILL.md, not the dir — rsync --existing leaves empty dirs) is seeded whole,
    # including the canonical routine dream, plus every schedule recipe.
    for sk in "$FACTORY"/templates/brand-routines/claude/skills/*/; do
      name="$(basename "$sk")"
      if [ ! -f "$dir/.claude/skills/$name/SKILL.md" ]; then
        mkdir -p "$dir/.claude/skills/$name"
        cp -R "$sk". "$dir/.claude/skills/$name/"
        echo "  seeded routine skill: $name"
      fi
    done
    mkdir -p "$dir/schedules"
    cp -n "$FACTORY"/templates/brand-routines/schedules/*.md "$dir/schedules/" 2>/dev/null || true
    mkdir -p "$ps/fixtures" 2>/dev/null; cp -n "$FACTORY/fixtures/creative-tracker-example.csv" "$ps/fixtures/" 2>/dev/null || true
    # The creative review gates ship as a bundle: the written-tells doctrine, the two
    # reviewer agents (voice + grounding), and the two deterministic checkers they run.
    # The creative skills' SKILL.md gates reference all of them by name, so they land together.
    cp -n "$FACTORY/global/knowledge/creative-strategy/ai-writing-tells.md" "$ps/creative-strategy-context/" 2>/dev/null || true
    mkdir -p "$dir/.claude/agents" "$dir/scripts"
    cp -n "$FACTORY/.claude/agents/creative-voice-review.md" "$dir/.claude/agents/" 2>/dev/null || true
    cp -n "$FACTORY/.claude/agents/context-grounding-review.md" "$dir/.claude/agents/" 2>/dev/null || true
    cp -n "$FACTORY/scripts/voice-lint.py" "$dir/scripts/" 2>/dev/null || true
    cp -n "$FACTORY/scripts/grounding-check.py" "$dir/scripts/" 2>/dev/null || true
    # The old-ads corpus (harvest v2): a new directory --existing never creates, and
    # whose entries/ grows at the factory — seed it whole if missing, else add the
    # new entry files (README/INDEX refresh via the --existing sweep above).
    if [ -d "$ps/creative-strategy-context/old-ads" ]; then
      mkdir -p "$ps/creative-strategy-context/old-ads/entries"
      cp -n "$FACTORY"/global/knowledge/creative-strategy/old-ads/entries/*.md "$ps/creative-strategy-context/old-ads/entries/" 2>/dev/null || true
    else
      cp -R "$FACTORY/global/knowledge/creative-strategy/old-ads" "$ps/creative-strategy-context/"
    fi
    # Skill/agent path normalization (always ship the tool, then run it): the factory
    # copies rsynced above carry factory doc paths that don't resolve in the brain's
    # layout. The rewrite is deterministic and idempotent.
    # Craft-skill seeding: brains built before the all-skills-in-.claude/ convention
    # carry the craft set in an inert top-level skills/ (which Claude Code never
    # loads) or not at all, so "write me a script" has no skill to route through.
    # Seed any missing craft skill from the factory set; ones already present were
    # refreshed by the --existing sweep above. The routine `dream` stays canonical.
    for sk in "$FACTORY"/.claude/skills/*/; do
      name="$(basename "$sk")"
      [ "$name" = "dream" ] && continue
      # Check for SKILL.md, not the directory: the --existing rsync above creates
      # empty skill dirs (it only skips files), and git never ships an empty dir.
      if [ ! -f "$dir/.claude/skills/$name/SKILL.md" ]; then
        mkdir -p "$dir/.claude/skills/$name"
        cp -R "$sk". "$dir/.claude/skills/$name/"
        echo "  seeded craft skill: $name"
      fi
    done
    cp -f "$FACTORY/scripts/normalize-brain-paths.py" "$dir/scripts/" 2>/dev/null || true
    cp -f "$FACTORY/scripts/verify-brain.py" "$dir/scripts/" 2>/dev/null || true
    python3 "$FACTORY/scripts/normalize-brain-paths.py" "$dir" nested
  elif [ -d "$dir/creative-strategy-context" ]; then
    layout=flat
    echo "  Layout: flat (standalone)"
    # update-only: refresh only what the brain already has. The flat brain carries
    # the craft layer at root, the runtime system subset at system/ (--existing
    # naturally limits to the docs the brain has, never the factory-internal ones),
    # and the runtime routine skills under .claude/skills/. It does NOT carry the
    # factory prompts/ or templates/, so those are not mirrored. Flat path
    # normalization runs after the canon sync below — so it also catches the
    # nested parker-system/ paths the synced CLAUDE.md blocks carry.
    rsync -a --existing \
      --exclude '_*-lens.md' \
      --exclude 'expert-insights' \
      "$FACTORY/global/knowledge/creative-strategy/" "$dir/creative-strategy-context/"
    rsync -a --existing "$FACTORY/system/"                                  "$dir/system/"
    rsync -a --existing "$FACTORY/templates/brand-routines/claude/skills/"  "$dir/.claude/skills/"
    # Context hook + settings ship together, added if missing (see the nested branch's
    # note). The hook script finds the flat craft path on its own, so no rewrite needed.
    mkdir -p "$dir/.claude/hooks"
    rsync -a "$FACTORY/templates/brand-routines/claude/hooks/"    "$dir/.claude/hooks/"
    rsync -a "$FACTORY/templates/brand-routines/claude/settings.json" "$dir/.claude/settings.json"
    # Deliberate adds (same list as the nested branch). Flat path normalization below
    # rewrites the system docs' nested-layout references.
    cp -n "$FACTORY/system/growing-the-brain.md" "$dir/system/" 2>/dev/null || true
    # Routine-bundle seeding: any routine skill the brain is missing (checked by
    # SKILL.md, not the dir — rsync --existing leaves empty dirs) is seeded whole,
    # including the canonical routine dream, plus every schedule recipe.
    for sk in "$FACTORY"/templates/brand-routines/claude/skills/*/; do
      name="$(basename "$sk")"
      if [ ! -f "$dir/.claude/skills/$name/SKILL.md" ]; then
        mkdir -p "$dir/.claude/skills/$name"
        cp -R "$sk". "$dir/.claude/skills/$name/"
        echo "  seeded routine skill: $name"
      fi
    done
    mkdir -p "$dir/schedules"
    cp -n "$FACTORY"/templates/brand-routines/schedules/*.md "$dir/schedules/" 2>/dev/null || true
    mkdir -p "$dir/fixtures" 2>/dev/null; cp -n "$FACTORY/fixtures/creative-tracker-example.csv" "$dir/fixtures/" 2>/dev/null || true
    # Craft skills refresh (update-only): flat brains built with the craft set in
    # .claude/skills/ get the same SKILL.md updates nested brains get from the factory
    # sweep; brains without a given skill gain nothing (--existing adds no files).
    rsync -a --existing --exclude 'dream' "$FACTORY/.claude/skills/" "$dir/.claude/skills/"
    # The creative review-gate bundle (see the nested branch's note).
    cp -n "$FACTORY/global/knowledge/creative-strategy/ai-writing-tells.md" "$dir/creative-strategy-context/" 2>/dev/null || true
    mkdir -p "$dir/.claude/agents" "$dir/scripts"
    cp -n "$FACTORY/.claude/agents/creative-voice-review.md" "$dir/.claude/agents/" 2>/dev/null || true
    cp -n "$FACTORY/.claude/agents/context-grounding-review.md" "$dir/.claude/agents/" 2>/dev/null || true
    cp -n "$FACTORY/scripts/voice-lint.py" "$dir/scripts/" 2>/dev/null || true
    cp -n "$FACTORY/scripts/grounding-check.py" "$dir/scripts/" 2>/dev/null || true
    # The old-ads corpus (harvest v2) — same seed-or-add as the nested branch.
    if [ -d "$dir/creative-strategy-context/old-ads" ]; then
      mkdir -p "$dir/creative-strategy-context/old-ads/entries"
      cp -n "$FACTORY"/global/knowledge/creative-strategy/old-ads/entries/*.md "$dir/creative-strategy-context/old-ads/entries/" 2>/dev/null || true
    else
      cp -R "$FACTORY/global/knowledge/creative-strategy/old-ads" "$dir/creative-strategy-context/"
    fi
    # Skill/agent path normalization for the flat layout (see the nested branch's note).
    # Runtime system docs: some flat brains were built without a system/ dir, so
    # the skills' system/<doc>.md references resolve to nothing and update-only
    # can never add them. Seed the six runtime docs the brains actually read.
    mkdir -p "$dir/system"
    for doc in parker-tools.md three-phase-operating-model.md open-loops-system.md refresh-cadence.md schedules.md growing-the-brain.md; do
      cp -n "$FACTORY/system/$doc" "$dir/system/" 2>/dev/null || true
    done
    # Craft-skill seeding: brains built before the all-skills-in-.claude/ convention
    # carry the craft set in an inert top-level skills/ (which Claude Code never
    # loads) or not at all, so "write me a script" has no skill to route through.
    # Seed any missing craft skill from the factory set; ones already present were
    # refreshed by the --existing sweep above. The routine `dream` stays canonical.
    for sk in "$FACTORY"/.claude/skills/*/; do
      name="$(basename "$sk")"
      [ "$name" = "dream" ] && continue
      # Check for SKILL.md, not the directory: the --existing rsync above creates
      # empty skill dirs (it only skips files), and git never ships an empty dir.
      if [ ! -f "$dir/.claude/skills/$name/SKILL.md" ]; then
        mkdir -p "$dir/.claude/skills/$name"
        cp -R "$sk". "$dir/.claude/skills/$name/"
        echo "  seeded craft skill: $name"
      fi
    done
    cp -f "$FACTORY/scripts/normalize-brain-paths.py" "$dir/scripts/" 2>/dev/null || true
    cp -f "$FACTORY/scripts/verify-brain.py" "$dir/scripts/" 2>/dev/null || true
    python3 "$FACTORY/scripts/normalize-brain-paths.py" "$dir" flat
  else
    echo "  SKIP: $repo has neither parker-system/ nor creative-strategy-context/ (unrecognized layout)"; continue
  fi

  # Refresh the marker-delimited shared blocks from the factory canon. The rsync
  # above already carried the prompt embeds inside parker-system/, but the brain's
  # root CLAUDE.md lives OUTSIDE parker-system/ and is never rsynced, so its
  # parker-voice block goes stale on its own. Sync scans the whole brain clone
  # with the factory as the source of truth; it is idempotent and only touches
  # files whose block has actually drifted.
  python3 "$FACTORY/scripts/sync-open-loops-core.py" --scan "$dir"

  # Flat-layout path normalization. Factory canon carries nested-layout paths:
  # the rsync'd system docs reference the craft layer as global/knowledge/creative-strategy/,
  # and the marker blocks the sync just refreshed into the brain's root CLAUDE.md
  # carry parker-system/ paths. Rewrite both to the flat repo's shape so every
  # reference resolves. (Nested brains keep parker-system/ as-is, so this is flat-only.)
  if [ "$layout" = flat ]; then
    LC_ALL=C find "$dir/system" -name '*.md' -type f \
      -exec sed -i '' \
        -e 's#global/knowledge/creative-strategy/#creative-strategy-context/#g' \
        -e 's#parker-system/creative-strategy-context/#creative-strategy-context/#g' \
        -e 's#parker-system/system/#system/#g' \
        {} + 2>/dev/null || true
    if [ -f "$dir/CLAUDE.md" ]; then
      # Skills live in .claude/skills/ in the current template (the only dir Claude Code
      # loads from), so the template's .claude/skills/<skill>/ path needs no rewrite here.
      LC_ALL=C sed -i '' \
        -e 's#parker-system/creative-strategy-context/#creative-strategy-context/#g' \
        -e 's#parker-system/system/#system/#g' \
        "$dir/CLAUDE.md"
    fi
  fi

  if git -C "$dir" diff --quiet && git -C "$dir" diff --cached --quiet && [ -z "$(git -C "$dir" status --porcelain)" ]; then
    echo "  No changes — already current."
    continue
  fi

  echo "  Changed files:"; git -C "$dir" status --porcelain | sed 's/^/    /' | head -40
  git -C "$dir" add -A
  git -C "$dir" commit -q -m "Re-ship parker-system methodology bundle from parker-brain factory @ $SHA

Mirrors factory prompts/skills/system/templates and the creative-strategy
craft layer into parker-system/, then syncs the marker-delimited shared blocks
(including the parker-voice block in the root CLAUDE.md) from factory canon.
Brand lens overlays, expert-insights, and all brand outputs outside
parker-system/ are preserved.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
  git -C "$dir" push origin HEAD >/dev/null 2>&1
  echo "  Pushed: $(git -C "$dir" rev-parse --short HEAD)"
done

echo "Done."
