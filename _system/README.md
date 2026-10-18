# _system/ (for contributors)

How the repo is made. **To use it you don't need anything in here**: go to [`1-start-here/`](../1-start-here/).

| Folder / file | What it is |
|---|---|
| `core/` | What every download gets: `START-HERE.md` (status line, 2-step guide, the daily words, instructions for the AI), `CLAUDE.md`, `AGENTS.md`, `.gitignore`, and the download's own `_system/` (SETUP.md = the first-run interview, PROJECT-CARD.md, house rules, handoff, changelog, decisions, journey, guide template, archive, trash). |
| `niches/<name>/` | One setup (blueprint): its folders, each with a `README.md`, plus `_niche/` = extra house rules, extra `.gitignore` lines, a one-line description (`about.md`) and an emoji (`card.json`). |
| `tools/build.py` | Builds `1-start-here/` (core + every blueprint), `2-ready-made/<name>/` (folders already applied) and the zips. Python 3, nothing to install. |
| `tools/config.json` | The repo's URL (used in links inside the downloads). |
| `VERSION` · `CHANGELOG.md` | The version (a release tag must match it) and the repo's own changelog. |

## How the first run works
`START-HERE.md` has a **Status** line: ⚪ (starter, nothing set up) or 🟡 (ready-made, folders done). `CLAUDE.md` / `AGENTS.md` (or the Cowork project instruction) send the AI to `START-HERE.md`, which sends it to `_system/SETUP.md` while the status isn't ✅. SETUP asks ~6 questions, recommends a blueprint with a preview, builds it on "yes", fills the project card, handoff and decisions, and flips the status to ✅.

## Change something
1. Edit `core/` (everything) or `niches/<name>/` (one setup). Never edit `1-start-here/` or `2-ready-made/` by hand.
2. From the repo folder run: `python3 _system/tools/build.py`
3. Commit everything, including the rebuilt folders. GitHub Actions runs `--check` on every push.

## Add a setup
Copy a folder in `niches/`, rename it, change its folders, READMEs and `_niche/` files, then build. It appears in the starter's blueprints, in SETUP's table and in `2-ready-made/` automatically. Please open a Discussion first.

## Release
1. Bump `VERSION` (e.g. `v1.1`), add a `CHANGELOG.md` entry, build, commit, push.
2. On GitHub: **Releases → Draft a new release** → tag = the same version → **Publish**.
3. The **Release zips** action attaches `ready-set-folder.zip` + one zip per ready-made workspace. The README links (`releases/latest/download/…`) always point at the newest release.
