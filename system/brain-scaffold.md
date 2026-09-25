# Brain scaffold: what a new brand brain starts with, and how it gets there

A new brand brain starts as a **scaffold**: every method file the brain carries, plus the brand-owned starting files, with none of the brand's own knowledge yet. `scripts/scaffold-brain.py` builds it with no AI involved. This doc is the maintainer's contract for it: what goes in, the marker that says "not built yet," the three ways it gets applied, and what to change when you add a file every brain needs.

## Why it exists

Setting up a brain used to be the model's job: dozens of folder creations, 162 method file copies, template stamps, a symlink, and a config file, all before a single real prompt ran. That burned tokens and time on work with no judgment in it, and it went wrong in ways the build verification had to catch (skills dropped, both `dream` skills kept, the skills folder copied instead of linked, a brand name typed into a method file so it stopped updating). A script does it the same way every time, in seconds.

It also means a brain can exist before anyone builds it. Parker's backend scaffolds a brand's repo the moment the brand signs up, from a manifest this repo publishes on every release, with no git on the server. A team can start talking to Parker in that brain right away: Parker works from live pulls and saves what the team tells it into the running notes and the brand lens, and the full build (`/set-up-brain`) runs whenever they're ready.

## What an empty brain contains

Exactly two lists define it. A file every brain needs belongs in one of them, or it never reaches a new brain.

1. **The bundle map**, `bundle_map()` in `scripts/sync-executable-layer.py`. Method files copied in **verbatim**: the craft and routine skills, the review-gate agents, the output style, the hooks and settings, the Codex twin (`.codex/`, `AGENTS.md`), the schedule recipes, and the checker and usage scripts. `/update-brain` re-syncs these on every pin bump, refreshing a copy only while it still matches the release it came from. That is why **no method file ever gets the brand name or any other per-brand edit**: a changed copy reads as the team's own and stops updating for good. Write bundle files brand-neutral; they find the brand through the brain's `CLAUDE.md` and `parker_config.json`.
2. **`SEEDS`** in `scripts/scaffold-brain.py`. Brand-owned starting files, written once and never touched by the update sync: the brand `CLAUDE.md` (the template with the brand name filled in and the phase and build-status sections saying nothing is built yet), a short `README.md`, the six living-layer folder READMEs from `templates/brand-scaffold/`, `brand-lens.md`, and the running notes (`brand-rules.md`, `success-definition.md`, `missing-context.md`, `brand-notes-from-org.md`, `routine-log.md`, `standard-sync.md`). Template slots that need an answer become "Not captured yet." so an unanswered question reads as a named blank.

The script also generates `parker_config.json` (brand id and name, repo URL, the pinned `parker_brain_version`, `created_at`, usage logging off), the `.scaffolded` marker, the `.agents/skills` symlink to `../.claude/skills`, and, in the manifest only, `.gitmodules` plus the `parker-system` mount pointer at the release's commit.

Left out on purpose:

- **`BUILD-STATUS.md` and `prompts-run-log/`.** They mean a build is running or ran. The build creates them.
- **`running-notes/refresh-schedule.md`.** It aggregates real docs' `generated_on` and `refresh_by` dates, and there are none yet; `/refresh-context` builds it when it's missing.
- **Placeholder files in the data folders** (`sub-context-docs/`, `personas/`, `competitors/`, `audits/`, `strategy/`, and the rest). Git can't hold an empty folder, and a README sitting among the docs a synthesis prompt reads by folder is noise in its input. The brand `CLAUDE.md`'s map says where each doc goes, and writing a doc creates its folder.
- **Binary files.** The manifest carries text only (GitHub's tree API takes inline text content). The script fails the release if a bundle file isn't UTF-8.

## The `.scaffolded` marker

A file at the brain's root that says "set up, not built." The scaffold writes it; the build deletes it once its verification passes (`prompts/onboarding-runner.md`, "Verify the build"), and nothing else touches it. It stays for as long as the brain isn't built, including a brain the team has been filling by conversation for weeks.

What reads it:

- **The runner and `/set-up-brain`** route a folder with the marker and no build started as "scaffolded": a cold start with the setup already done.
- **The session-start hook** tells the model the brain is scaffolded, so it doesn't go hunting for docs that don't exist.
- **Parker's apps.** Any "is this brain built?" check should treat the marker's presence as **not built**. Checking presence costs nothing extra: the root listing the check already reads (`GET /repos/{owner}/{repo}/contents/`) includes dotfiles, so it's one more name to look for in data already fetched. Don't read `parker_config.json` for this; that's a second API call per check, and the marker is the one source of truth.

Heads-up for the web app: its current check calls a brain built once the root holds any file outside a short ignore list. A scaffolded brain has dozens of files (`CLAUDE.md`, `.claude/`, `running-notes/`, and more), so that check reads it as built. **The marker check has to ship before the backend starts scaffolding.** It also changes one thing for the better: a brain now shows as not built for the whole length of a build, instead of flipping to built when the first file lands.

## Three ways it gets applied

### 1. Locally, inside the brand folder (the runner's Phase 0 step 3)

```
python3 parker-system/scripts/scaffold-brain.py init --brand-name "Acme" --brand-id 123
```

Needs the `parker-system/` mount attached and checked out at a release tag; it reads every file from the mount's git objects at that commit, so the scaffold always matches the pinned method. It never overwrites a file (an existing `parker_config.json` only gains the keys it lacks, and one that isn't valid JSON is flagged, not trusted), so running it on a scaffolded brain fills gaps and nothing else. The `.scaffolded` marker is written first, and every file goes through a temp file and a swap, so a run that dies partway leaves whole files or none, and the next run finishes the job. It refuses a brain that's already built or mid-build without the marker, and a folder with no mount. `--dry-run` shows the plan; `--verbose` lists every file. It also flags a mount that moved after scaffolding (the release in `parker_config.json` no longer matches the mount's tag): the copies came from the recorded release, so that move gets finished the `/update-brain` way, and on a scaffolded folder the pin shouldn't move before the build at all.

`init --restore-copies` is the repair tool the build verification uses: on any brain with the mount, it puts back the pinned release's version of every bundle-map copy that is missing or differs (keeping a schedule's armed Status line) and touches nothing else. On a standing brain it would overwrite the team's own edits, which is why `/update-brain`, not this, is the update tool there. The report is one line plus anything that needs attention; the likely one is the `.agents/skills` symlink on Windows without Developer Mode, which only matters for Codex.

### 2. The release manifest (CI)

`.github/workflows/release-scaffold.yml` runs when a release is published. It runs the scaffold tests, builds the manifest at the release tag, and attaches it to the release as `brain-scaffold.json`:

```
python3 scripts/scaffold-brain.py manifest --tag v23 --out brain-scaffold.json
```

The manifest is the scaffold as GitHub tree entries:

```json
{
  "format": 1,
  "factory": {"remote": "https://github.com/real-simple-labs/parker-brain", "tag": "v23", "commit": "<sha>"},
  "placeholders": {"{{BRAND_NAME}}": "...", "{{BRAND_ID}}": "...", "{{GITHUB_REPO_URL}}": "...", "{{CREATED_AT}}": "..."},
  "json_escaped_paths": ["parker_config.json"],
  "marker": ".scaffolded",
  "tree": [
    {"path": "CLAUDE.md", "mode": "100644", "type": "blob", "content": "# Parker — {{BRAND_NAME}}\n..."},
    {"path": "scripts/voice-lint.py", "mode": "100755", "type": "blob", "content": "..."},
    {"path": ".agents/skills", "mode": "120000", "type": "blob", "content": "../.claude/skills"},
    {"path": "parker-system", "mode": "160000", "type": "commit", "sha": "<the release commit>"}
  ]
}
```

As of this change it's 182 entries and about 950 KB. The four placeholders are the only ones; the script fails the release if any bundle file contains one, so filling them everywhere is safe. Run the workflow by hand (`workflow_dispatch` with a tag) to rebuild the file for a release; only releases that contain `scripts/scaffold-brain.py` can build one, so the first manifest ships with the release that carries this change.

### 3. The backend, when a brand signs up

No git and no disk. Four steps, three of them writes:

1. **Fetch the manifest** from `https://github.com/real-simple-labs/parker-brain/releases/latest/download/brain-scaffold.json` (public, no auth). For the minute after a release is published, before CI attaches the file, that URL returns 404; fall back to the newest release that has the asset (`GET /repos/real-simple-labs/parker-brain/releases`). Check `format` is `1`.
2. **Create the repo with `auto_init: true`.** GitHub's tree API refuses an empty repo, so it needs the one starting commit. If the repo already existed (the provisioning service is create-or-reuse), scaffold only when it's still fresh: exactly one commit, holding nothing but GitHub's own `README.md`, `.gitignore`, or `LICENSE`. Anything else is someone's brain; leave it alone.
3. **Fill the placeholders** in every entry's `content`, in a single pass (so a value can never introduce another placeholder), JSON-string-escaping the values for the paths in `json_escaped_paths`.
4. **Create the tree, create the commit, move the branch.** No `base_tree` (the scaffold replaces GitHub's starter README), the starter commit as the parent, and `force: false` so the branch only moves forward.

A reference in TypeScript with Octokit:

```ts
const res = await fetch("https://github.com/real-simple-labs/parker-brain/releases/latest/download/brain-scaffold.json");
const manifest = await res.json();
if (manifest.format !== 1) throw new Error(`unknown scaffold format ${manifest.format}`);

const values: Record<string, string> = {
  "{{BRAND_NAME}}": brand.name,
  "{{BRAND_ID}}": String(brand.id),
  "{{GITHUB_REPO_URL}}": `https://github.com/${owner}/${repo}`,
  "{{CREATED_AT}}": new Date().toISOString().slice(0, 10),
};
const fill = (text: string, path: string) =>
  text.replace(/\{\{(?:BRAND_NAME|BRAND_ID|GITHUB_REPO_URL|CREATED_AT)\}\}/g, (token) =>
    manifest.json_escaped_paths.includes(path) ? JSON.stringify(values[token]).slice(1, -1) : values[token]);

const { data: info } = await octokit.rest.repos.get({ owner, repo });
const branch = info.default_branch;
const { data: ref } = await octokit.rest.git.getRef({ owner, repo, ref: `heads/${branch}` });
// (fresh-repo check from step 2 goes here)
const { data: tree } = await octokit.rest.git.createTree({
  owner, repo,
  tree: manifest.tree.map((entry: any) => ("content" in entry ? { ...entry, content: fill(entry.content, entry.path) } : entry)),
});
const { data: commit } = await octokit.rest.git.createCommit({
  owner, repo, tree: tree.sha, parents: [ref.object.sha],
  message: `Scaffold an empty brand brain (Parker method ${manifest.factory.tag})`,
});
await octokit.rest.git.updateRef({ owner, repo, ref: `heads/${branch}`, sha: commit.sha, force: false });
```

`apply_manifest()` in `scripts/scaffold-brain.py` is the same sequence in Python, fresh-repo check included, and it is what the tests exercise.

What happens next on a machine: Parker Desktop downloads the repo. Because the repo already has tracked files, the app's "attach the mount to a brand new brain" step doesn't fire; its regular submodule step sees the recorded `parker-system` pointer uninitialized and initializes it at the pinned release. A cloud session that clones the brain gets the same fix from the session-start hook (`git submodule update --init parker-system`).

## Testing it against a sample repo

```
python3 scripts/scaffold-brain.py manifest --tag v23 --out /tmp/brain-scaffold.json
# create an empty private repo with "Add a README" ticked (that's auto_init), then:
GITHUB_TOKEN=<a token that can write to it> python3 scripts/scaffold-brain.py push \
    --manifest /tmp/brain-scaffold.json --repo you/sample-brain --brand-name "Sample" --brand-id 1
git clone --recurse-submodules https://github.com/you/sample-brain
```

`push` refuses any repo that isn't fresh, so a mistyped repo name can't overwrite a real brain. Building the manifest from an untagged ref works for testing (it warns), but the mount then points at a commit that isn't a release, so `/update-brain` has nothing to compare against.

## When you add, move, or change a file a brain needs

- **A method file** (skill, agent, hook, checker script, schedule recipe, Codex config): make sure `bundle_map()` covers its path. Most do already by folder; a new top-level script needs an explicit line. Standing brains get it from `/update-brain` on the next pin bump, no migration step.
- **A brand-owned starting file**: add a `Seed` to `SEEDS`, with its template under `templates/`. Standing brains don't get seeds, so if they need the file too, the release's `migrations/vN.md` carries a step that creates it (`migrations/README.md`).
- **A template a seed reads** (`templates/brand-brain-CLAUDE-template.md`, the running-notes templates, `templates/brand-scaffold/`): the seed's slot patterns must still match. If one doesn't, the scaffold fails loudly and names the slot; update the `Seed` in the same PR.
- Run `python3 -m unittest discover -s tests -p "test_scaffold_brain.py" -v`. It builds a fixture factory from your working tree, scaffolds a brand both ways, and checks they match, that the update sync reads every copy as untouched, and that nothing leaked a placeholder.
- Update the description of what ships in `prompts/onboarding-runner.md` (Phase 0 steps 3 and 5) and the brand tree in `system/master-file-structure.md`.
