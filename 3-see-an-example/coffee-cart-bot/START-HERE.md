# 👋 START HERE

**Status:** ✅ Set up on 2026-10-01 as **automation-builder** for "Bean Cart Orders".

## New here? 2 steps
1. **Give this folder to your AI**
   - **Claude Cowork:** Projects → **+** → **Use an existing folder** → pick this folder. In **Instructions**, paste:
     `Read START-HERE.md in this folder and follow it.`
   - **Claude Code · Cursor · Codex:** just open this folder.
   - **A chat app (claude.ai, ChatGPT, Gemini):** attach `START-HERE.md` and `_system/SETUP.md`. (Chat apps can't create files: the AI writes the text for you to paste, or points you to a ready-made version with the folders already made.)
2. **Say "hi".** Your AI asks a few quick questions, shows you the setup that fits you, and builds it when you say yes. About 3 minutes.

## Every day after that
Just talk normally, and use these words at the edges of a session:

| Say | The AI will |
|---|---|
| **"continue"** | read where you stopped and tell you what's next |
| **"wrap up"** | save today's changes, decisions and next steps for next time |
| **"write a guide for …"** | write step-by-step instructions you can follow |
| **"tidy up"** | suggest where messy files should go (moves nothing without your OK) |

Your work goes in the folders you see. Each one has a short `README.md` saying what belongs there. `_system/` is the AI's memory and rules: you rarely need to open it.

---

## For the AI (read this every session)
1. **If the Status line starts with ⚪ or 🟡, run `_system/SETUP.md` now**, whatever the user's first message is, unless they clearly ask to skip it.
2. Otherwise read, in order: `README.md` → `_system/HOUSE-RULES.md` → `_system/HANDOFF.md` → the newest entries of `_system/CHANGELOG.md`. Check `_system/DECISIONS.md` before suggesting a change to anything already decided.
3. **"continue"** (or any start of a session): after reading, tell the user in 3 lines where things stand and what's next, then wait.
4. **"wrap up"** (or "end session", "that's it for today"): add today's changes to `_system/CHANGELOG.md` (newest on top), add decisions to `_system/DECISIONS.md` (replace, never edit, old ones), rewrite `_system/HANDOFF.md` (state, decisions, open questions, next steps, and the paste-line for the next chat), add a `_system/JOURNEY.md` entry if it's used, and check nothing you wrote contains a key or password. Then summarise in 3 lines.
5. **"write a guide for …"**: put it in `guides/` (create it if missing), following `_system/GUIDE-TEMPLATE.md`. Assume a non-developer: exact clicks and words. Tick its tracker as the user reports progress.
6. **"tidy up"**: compare the folder with `_system/HOUSE-RULES.md` §1, list misplaced files, duplicates and old versions with where each should go. Move nothing until the user says yes.
7. Always follow `_system/HOUSE-RULES.md`. Never delete: move to `_system/_to_delete/`.

<sub>Made with [ready-set-folder](https://github.com/itskhoamd/ready-set-folder) v1.0.</sub>
