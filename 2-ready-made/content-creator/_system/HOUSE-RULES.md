# House rules

The working agreement for this project, for the human, for the AI, and for anyone who joins later.
If a rule is broken, it's usually because someone once got burned by it. Change a rule by recording a decision in `_system/DECISIONS.md` and then updating this file. (All paths here are from the project folder.)

> **Short version:** one folder = the truth · nothing gets deleted · no secrets in files · every change gets a CHANGELOG line · decisions are replaced, never edited · end every session with a handoff · ask before anything that can't be undone.

---

## 1. Where things live
1. **This folder is the single source of truth.** Copies elsewhere (a Claude Project, Google Drive, a chat) are mirrors. If they differ, this folder wins.
2. **Keep the top level clean:** `START-HERE.md`, `README.md`, `CLAUDE.md`, `AGENTS.md`, the work folders and `_system/`. Nothing else goes at the top level without the human's OK.
3. **Every folder has a `README.md`** saying what goes in it. Put each new file where it belongs. If no folder fits, create one, give it a `README.md`, and log it in `_system/CHANGELOG.md`.
4. **Nothing is deleted by the AI.** Files to remove go to `_system/_to_delete/`. Only the human empties it.
5. **One current version of every doc.** When a doc is replaced, the old version moves to `_system/_archive/` (named `<file>_<version>_<YYYY-MM-DD>`).
6. **File names:** lowercase-with-dashes or UPPER-CASE.md for key docs, no spaces, dates as `YYYY-MM-DD_` at the start for one-off files (handoffs, reports).

## 2. Secrets and safety
1. **Passwords, API keys and tokens never go into chat, docs, code or commits.** They live only in the tool's own credential store (the app's settings, a password manager, `.env` files that are git-ignored).
2. Use `.env.example` with fake values to show which keys are needed.
3. Before sharing or publishing anything, check it for keys, private data and other people's personal details.
4. **Ask before anything that can't be undone:** deleting data, sending messages or emails to real people, spending money, publishing, changing something that's live.

## 3. Changes and versions
1. **Every change gets a line in `_system/CHANGELOG.md`**: newest on top, `YYYY-MM-DD` · **[area]** what changed.
2. Things that get released or installed get a version (`v1.0`, `v1.1`…): first number = new behaviour, second = fixes.
3. **Fix it in files, not in prompts.** If two AI models would do something differently (a design, a rule, a number), write it down in a file so the result is the same every time.
4. **Preview before locking.** New looks, formats or big changes are shown to the human first. They approve, then it becomes the standard.

## 4. Decisions
1. **Every decision that shapes the project goes into `_system/DECISIONS.md`** with the date and the why.
2. **Decisions are never edited.** To change one, add a new decision that replaces it and mark the old one "replaced by D-0xx". This stops anyone (human or AI) from quietly undoing a choice.
3. The AI doesn't re-ask questions that `_system/DECISIONS.md` already answers.

## 5. Sessions and handoffs
1. **Every session starts** with `START-HERE.md` and `_system/HANDOFF.md`.
2. **Every session ends** with the "wrap up" routine in `START-HERE.md`: `CHANGELOG.md`, `HANDOFF.md`, `DECISIONS.md` (and `JOURNEY.md` if used) in `_system/` are updated.
3. `_system/HANDOFF.md` always holds a ready-to-paste line for the next chat.

## 6. Guides and instructions for the human
1. Step-by-step guides go in `guides/` and follow `_system/GUIDE-TEMPLATE.md`: Parts (A, B, C…), lettered steps (A0, A1…), a **✅ You should see** check after each step, and a tracker at the end.
2. The AI keeps the tracker up to date as the human reports progress.

## 7. Roles
- **Human:** ideas, decisions, taste, approvals. Tests and publishes.
- **AI:** builds, writes, checks, documents. Proposes; doesn't decide alone on anything in §2.4.

## 8. Rules for content projects
1. **Every piece gets an episode code** (`E001`, `E002`…), used in the script, footage, work and export names.
2. **Footage is read-only.** Originals in `footage/` are never edited, renamed or deleted.
3. **The editor writes only inside `work/E###/`.** Only approved finals go to `exports/`.
4. **After filming, the script is updated to what was actually said**, so captions, cuts and cue words match the audio.
5. **Brand rules in `brand/` win over the taste of the day.** Change them through `_system/DECISIONS.md`.
6. **Every post is logged in `content/SCHEDULE.md`** with date and link.
7. **Big media stays out of git.** Back up `footage/` and `exports/` to a drive or cloud.
8. **Rights:** only music, clips and images you're allowed to use. Note the source in the episode's script file.
