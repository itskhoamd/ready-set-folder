# Changelog (the repo itself)

Newest first. `YYYY-MM-DD` · **[area]** change. Areas: `core` · `<setup name>` · `tools` · `docs`.

---

## 2026-10-17 · v1.0
- **[core]** Self-setting-up folder: give it to your AI, say "hi". `START-HERE.md` has a status line (⚪ starter · 🟡 ready-made · ✅ set up); while it isn't ✅, the AI runs `_system/SETUP.md`: ~6 questions → recommends a setup with a folder preview → builds it on "yes" → fills project card, handoff, decisions → hands over. Daily use by plain words: "continue", "wrap up", "write a guide for …", "tidy up".
- **[core]** Every download: `START-HERE.md`, `CLAUDE.md`, `AGENTS.md`, `.gitignore`, and `_system/` (SETUP, PROJECT-CARD, HOUSE-RULES with general rules + one section per setup, HANDOFF, CHANGELOG, DECISIONS, JOURNEY optional, GUIDE-TEMPLATE, blueprints, `_archive/`, `_to_delete/`).
- **[setups]** automation-builder · content-creator · client-projects · film-production · general (new: inbox / work / output / reference).
- **[repo]** `1-start-here/` (the universal starter) · `2-ready-made/` (folders already made, for chat apps) · `3-see-an-example/` (coffee-cart-bot) · `_system/` (contributors).
- **[tools]** `_system/tools/build.py` builds the starter, the ready-made workspaces and the zips (`ready-set-folder.zip` + one per setup). GitHub Actions: check on every push; zips attached to every published release.
- **[docs]** README, MIT licence.
