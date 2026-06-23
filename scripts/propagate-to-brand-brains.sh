#!/usr/bin/env bash
#
# propagate-to-brand-brains.sh — re-ship the factory methodology bundle into
# standing brand brains, so factory improvements reach brains that were stood
# up earlier. This is the *update-time* counterpart to the onboarding-runner's
# build-time "ship the craft" step (Phase 0). See skills/propagate-craft/SKILL.md.
#
# It auto-detects the brain's layout and mirrors accordingly.
#
# NESTED brains (older layout, bundle under parker-system/):
#   prompts/  -> parker-system/prompts/
#   skills/   -> parker-system/skills/
#   system/   -> parker-system/system/
#   templates/-> parker-system/templates/
#   global/knowledge/creative-strategy/ -> parker-system/creative-strategy-context/
#
# FLAT standalone brains (current onboarding-runner layout, layers at root):
#   global/knowledge/creative-strategy/ -> creative-strategy-context/
#   system/                             -> system/  (runtime subset only; --existing
#                                          never adds the factory-internal docs)
#   templates/brand-routines/claude/skills/ -> .claude/skills/
#   (flat brains do not carry factory prompts/ or templates/, so those are skipped;
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
#   default brand repos: the three full brand brains.
# Requires: gh (authenticated), rsync, git.

set -euo pipefail

FACTORY="$(cd "$(dirname "$0")/.." && pwd)"
SHA="$(git -C "$FACTORY" rev-parse --short HEAD)"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

REPOS=("$@")
if [ ${#REPOS[@]} -eq 0 ]; then
  REPOS=(the-perfect-jean-brand-brain liquid-iv-brand-brain nutrafol-brand-brain)
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
    rsync -a --existing "$FACTORY/skills/"    "$ps/skills/"
    rsync -a --existing "$FACTORY/system/"    "$ps/system/"
    rsync -a --existing "$FACTORY/templates/" "$ps/templates/"
    rsync -a --existing \
      --exclude '_*-lens.md' \
      --exclude 'expert-insights' \
      "$FACTORY/global/knowledge/creative-strategy/" "$ps/creative-strategy-context/"
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
      -exec sed -i '' 's#global/knowledge/creative-strategy/#creative-strategy-context/#g' {} + 2>/dev/null || true
    if [ -f "$dir/CLAUDE.md" ]; then
      LC_ALL=C sed -i '' \
        -e 's#parker-system/creative-strategy-context/#creative-strategy-context/#g' \
        -e 's#parker-system/system/#system/#g' \
        -e 's#parker-system/skills/#.claude/skills/#g' \
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
