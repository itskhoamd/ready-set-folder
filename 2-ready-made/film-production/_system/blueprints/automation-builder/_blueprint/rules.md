## 8. Rules for automation projects
1. **One live version per workflow** in `workflows/current/`, with a stable file name. The old version moves to `workflows/archive/` before the new one goes live.
2. **Raw exports go to `workflows/private/` first.** Before a copy goes anywhere else: remove keys and tokens, sample or pinned data (it can hold real messages and orders) and real webhook URLs.
3. **Change live workflows in place** when the tool allows it. Re-importing usually creates a new copy with a new ID, which can break links (error handlers, webhooks, schedules). If a re-import can't be avoided, say so first.
4. **Test with fake data before switching anything on** (`code/tests/`). Never test on real customers or real money.
5. **Code and prompts live as files** (`code/`, `ai-prompts/`) and match what's in the tool. A change in one is a change in both, with a `_system/CHANGELOG.md` line.
6. **Database changes are numbered migrations.** Never edit one that has run; add the next number.
7. **Every error and its fix goes into `docs/troubleshooting/`.** Check there first next time.
8. **Costs:** list every paid service and its price in `README.md` → Tools. Ask before adding a new paid one.
