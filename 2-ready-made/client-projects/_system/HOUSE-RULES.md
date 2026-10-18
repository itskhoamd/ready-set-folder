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

## 8. Rules for client work
1. **One folder per client**, copied from `clients/_CLIENT-TEMPLATE/`, named `<PREFIX>_<client-name>`. The prefix comes from the initials (clash → add a number). Use it in file names and codes.
2. **Client data stays in its own client folder.** Never copy one client's data into another client's folder or into `templates/`: turn it into placeholders first.
3. **Client keys live in the client's own accounts or a credential store.** The client card only says where they are.
4. **Client-facing documents are written in the client's language**, in your brand's look, and checked by the human.
5. **Nothing goes to a client** (message, file, invoice, price) without the human's OK.
6. **Each client folder has its own `HANDOFF.md` and `CHANGELOG.md`.** `_system/HANDOFF.md` sums up across clients.
7. **Leads live in `pipeline/LEADS.md`** until they say yes; then they get a client folder.
8. **Never share or publish this workspace with real client folders in it.** `.gitignore` keeps real client folders out of git, but `pipeline/LEADS.md` and your notes are still personal: keep any repo of this workspace **private**.
