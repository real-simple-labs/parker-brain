# 2026-07-08 — Why the brand brain mounts the factory instead of copying it

**Type:** product rule / architecture decision. **Source:** Anton, planning session 2026-07-08, converged over a long back-and-forth and approved explicitly.

**The decision.** A brand brain gets the factory method as a git submodule at `parker-system/`, pinned to a plain release tag (`v1`, `v2` — manual, no semver). Brand data flat at root; `brand-lens.md` and `expert-insights/` at root (brand property never inside the mirrored/mounted method tree); the `.claude/` executable layer copied out because Claude Code only loads skills from the project root; deny rules + a SessionStart check keep the mount read-only and catch un-initialized clones.

**Alternatives rejected, and why — keep these; they will come up again:**
- **Two sibling folders (`factory/` + `<brand>-brain/` + top-level orientation file):** skills only load from the opened project's `.claude/`, so it forced a duplicated top-level `.claude/` with a permanent sync problem; cloud routines clone one repo, so the sibling doesn't exist there; nothing recorded which factory version a brain ran. Anton shipped this briefly (#24) and reverted it himself before converging here.
- **npm/npx packaging:** wrong ecosystem for marketers; agents consume the docs by path and grep, a registry layer only obscures; git tags already give versioned releases.
- **GitHub forks:** forks of a public repo cannot be made private — dead for brand data and for private team factories both; also mixes method and brand data into one merge-prone history.
- **AGENTS.md as the orientation file:** Claude Code doesn't read it natively; CLAUDE.md (optionally containing `@AGENTS.md`) is the pattern.

**The load-bearing trick:** renaming `global/knowledge/creative-strategy/` → `creative-strategy-context/` at the factory root made the factory's own tree match the brain's view minus the `parker-system/` prefix, which let ~330 existing references survive unchanged and deleted the entire ship-time copy/rename/rewrite machinery. When choosing between "sweep every reference" and "reshape the source tree once," reshaping won.

**Standing doctrine this reinforced:** updates are offers, never overrides — the submodule pin makes that structural (nothing changes until `/update-brain` moves the pin with a yes); structural changes ship `migrations/vN.md` in the same PR (CLAUDE.md "Releases And Migrations"); decoupling is a deliberate, confirmation-gated act (`/disconnect-factory`), never a side effect of hitting the read-only wall.
