# <Project name>

<One line: what this project is and who it's for.>

> **Owner:** <your name> · **Status:** <idea / building / live / paused> · **Last update:** <YYYY-MM-DD>
> **First time here, or starting a new AI chat?** Open [`START-HERE.md`](START-HERE.md).

---

## What "done" looks like
- <the outcome, in one or two lines>

## Tools
- <apps and services this project uses (no keys here)>

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
