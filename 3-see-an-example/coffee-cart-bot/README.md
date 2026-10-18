# Bean Cart Orders (example)

A Telegram bot that takes pre-orders for a small coffee cart and writes them to a Google Sheet, so the owner can prep drinks before the morning rush.

> 🧪 **This is a fictional example** showing a ready-set-folder workspace a few days into a real project. Bean Cart, its people and its numbers are made up.

> **Owner:** Mai (cart owner) · **Builder:** Sam · **Status:** building (v0.2 in testing) · **Last update:** 2026-10-03
> **First time here, or starting a new AI chat?** Open [`START-HERE.md`](START-HERE.md).

---

## What "done" looks like
- Customers send "1 iced latte, 8:15" to the bot → the order appears in the sheet with a pickup time → Mai gets a 7:30 summary of the morning's orders.
- Works for 30–60 orders a day, costs under $5 a month.

## Tools
- **n8n** (self-hosted, $5/month VPS): the workflows
- **Telegram bot** (free): where customers order
- **Google Sheets** (free): the order book Mai already uses
- **AI model** (pay per use, ~$1/month at this volume): reads free-text orders

## Where things live
| Folder | What goes in it |
|---|---|
| `ai-prompts/` | The AI prompts the system uses: one file per prompt (`<step>.md`), with the model it's written for. |
| `code/` | Code that runs inside or around the workflows: code-step scripts, helper tools (clean an export, deploy, back up) and `tests/`. |
| `code/tests/` | Test inputs and expected outputs: sample messages, sample webhooks, what the workflow should return. Fake data only, never real customers. |
| `database/` | Database structure and data changes (Supabase, Postgres, Airtable schema notes…). |
| `database/migrations/` | Numbered changes: `001_<what>.sql`, `002_<what>.sql`… |
| `docs/` | Background docs: how the system works, diagrams, costs, notes that aren't step-by-step guides. |
| `docs/troubleshooting/` | Known errors and their fixes: what happened, why, the fix, the date. One file per problem or one running `CASEBOOK.md`. |
| `guides/` | Step-by-step guides for the human: setups, installs, how-tos. Follow `_system/GUIDE-TEMPLATE.md`; name them `YYYY-MM-DD_<WHAT>.md`. |
| `workflows/` | The automation workflows themselves (exported JSON or the tool's own format). |
| `workflows/archive/` | Old versions of workflows, named `<workflow>_v<version>_<YYYY-MM-DD>.json`. Not live, kept for rollback. |
| `workflows/current/` | Exactly one file per workflow: the version that's live now, with a stable name (`<project>-<workflow>.json`). |
| `workflows/private/` | Raw exports straight from the tool. They can contain keys, tokens and real customer data. |
| `_system/` | The AI's memory and rules for this project. You rarely need to open this folder: the AI reads and updates it. |

---
<sub>Workspace: **automation-builder** from [ready-set-folder](https://github.com/itskhoamd/ready-set-folder) v1.0.</sub>
