# SETUP (instructions for the AI)

Run this when the Status line in `START-HERE.md` starts with **⚪** (nothing set up) or **🟡** (folders ready, project not set up). Start as soon as the user says anything, even "hi". Don't wait to be asked.

**Goal:** the user answers a few questions, sees a plan, says yes, and is working within about 3 minutes.
**Tone:** short, friendly, plain words. No jargon, no long explanations, no file paths unless they help.

---

## Step 1 · Ask (one message)
Greet in one line, then ask everything at once. If your app can show clickable choices, use them; otherwise number the questions so the user can reply in one line ("1: a cooking channel, 2b, 3 solo…").

1. **What are you working on?** One line, e.g. "a cooking channel on TikTok" or "a booking bot for my spa".
2. **Which sounds most like it?** *(⚪ only. On 🟡 the workspace is already chosen: say which one instead and skip this.)*
   a) 🤖 Automations, AI agents or bots (n8n, Make, Zapier, scripts)
   b) 🎬 Content: videos, reels, podcasts
   c) 💼 Work for clients (freelance, agency, setups for customers)
   d) 🎥 Film, video or event production jobs
   e) 🗂️ Something else, or a mix
3. **Just you, or a team?**
4. **Which apps and tools do you use for it?** (Names only, never passwords or keys.)
5. **What does "done" or success look like? Any deadline?**
6. **Which language should your project files be in?** (Default: the language of this chat.)

## Step 2 · Recommend (one message)
Pick the blueprint from the table at the bottom that fits best. If the user clearly does two things (e.g. content *and* client work), you may combine two blueprints: keep it to **7 top-level folders at most** and say you combined them. When nothing fits, use **general**.

Show:
- **One line** on why this setup fits them.
- **A preview** of the top level, one line per folder (take the line from each folder's `README.md` in the blueprint), with `_system/` last. Use their words where it helps (e.g. "content/ ← your TikTok scripts").
- Anything you'd **add or rename** for them, if needed (max 2 suggestions).

End with: **"Build it? Reply yes, or tell me what to change."** Wait.

## Step 3 · Build (after yes, without more questions)
Paths are from the top of this folder. On 🟡 (ready-made), skip the steps marked ⚪.

1. ⚪ **Copy the folders** of the chosen blueprint from `_system/blueprints/<name>/` to the top of this folder, each with its `README.md` and any starter files inside. Don't copy `_blueprint/`. Combining two? Copy both; merge folders with the same name.
2. **Project card:** ⚪ replace the placeholder `README.md` with a copy of `_system/PROJECT-CARD.md`; 🟡 use the existing `README.md`. Fill in the project name, the one-line description, owner, status ("setting up"), what "done" looks like and the tools. Replace `<!-- FOLDER-MAP -->` with a table (`| Folder | What goes in it |`): one row per top-level folder and its sub-folders, text = the first line of that folder's `README.md`, `_system/` last. Replace `<workspace>` in the line at the bottom with the blueprint name.
3. ⚪ **House rules:** in `_system/HOUSE-RULES.md`, replace `<!-- NICHE-RULES -->` with the text of `_system/blueprints/<name>/_blueprint/rules.md`. Two blueprints: add both (number the second one §9).
4. ⚪ **.gitignore:** add the lines of `_system/blueprints/<name>/_blueprint/gitignore.txt` to the end of `.gitignore`.
5. **Decisions** (`_system/DECISIONS.md`): D-001 = the workspace chosen and why; then one decision per useful answer (team or solo, file language, deadline). Remove the placeholder row.
6. **Handoff** (`_system/HANDOFF.md`): fill it in. "Next steps" = the **3 most useful first tasks** for *their* project, concrete (e.g. "Write the first 5 video ideas in `content/ideas/INBOX.md`").
7. **Changelog** (`_system/CHANGELOG.md`): replace the placeholder date, add "**[setup]** Set up as <blueprint> for <project>."
8. **Language:** write everything you fill in the chosen language. Leave the template READMEs as they are unless the user asks you to translate them. Keep folder names as they are.
9. **Status:** in `START-HERE.md`, change the Status line to: `✅ Set up on <YYYY-MM-DD> as **<blueprint>** for "<project>".`
10. Leave `_system/blueprints/` in place. **Never delete anything.**

## Step 4 · Hand over (one message)
- **"✅ You're set."** and the top-level folder list.
- The **3 first next steps** (from the handoff). Offer to start the first one now.
- **How to use it from now on:** say **"continue"** at the start of a session and **"wrap up"** at the end. Everything else: just talk.
- **Claude Cowork only:** if the project's Instructions are empty, suggest pasting `Read START-HERE.md in this folder and follow it.` so every new session starts right.

## Special cases
- **"Skip setup":** set the Status line to `✅ Set up (setup skipped) on <date>.`, create `README.md` from `_system/PROJECT-CARD.md` with just the project name, and stop.
- **"Redo setup" or "change the setup":** ask what to change. Move folders that are no longer needed to `_system/_to_delete/` (never delete), add the new ones, update `README.md`, `DECISIONS.md` and `CHANGELOG.md`.
- **You can't create files or folders** (a plain chat app): say so in one line. On ⚪, recommend the matching **ready-made** workspace ({{REPO_URL}}/tree/main/2-ready-made): its folders are already made. On 🟡, or if the user prefers, do the setup anyway and give them the finished text of `README.md`, `_system/HANDOFF.md` and `_system/DECISIONS.md` to paste into those files.

---

## The blueprints
{{BLUEPRINT_TABLE}}
