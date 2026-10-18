# HANDOFF

> Where the last session stopped. Read this right after `START-HERE.md`. Rewrite it at the end of every session.
> **Last updated:** 2026-10-03 · **Session:** pickup-time reading + morning summary

## Paste this to start the next chat
> Continue my project in this folder. Read `START-HERE.md`, then `_system/HANDOFF.md`, `_system/HOUSE-RULES.md` and the latest `_system/CHANGELOG.md` entries. Next I want to: run Part B of `guides/2026-10-02_SETUP.md` with Mai's real menu.

---

## 1. Where things stand
| Area | State | Where |
|---|---|---|
| Order bot workflow | v0.2 built, tested with fake orders (18/20 read right) | `workflows/current/beancart-orders.json` |
| Morning summary (7:30) | v0.1 built, not switched on | `workflows/current/beancart-summary.json` |
| Order-reading prompt | v3 | `ai-prompts/read-order.md` |
| Setup guide | Part A done by Mai, Part B next | `guides/2026-10-02_SETUP.md` |

## 2. Decided this session (don't re-ask)
- Pickup time is required; if missing, the bot asks once ("What time will you pick it up?") → D-004
- Summary goes to Mai only, not the group → D-005

## 3. Open questions for Mai
- Oat milk: extra charge or free?
- Last order time: 10:30 or 11:00?

## 4. Next steps (most valuable first)
1. Mai runs Part B of the setup guide with her real menu (B0–B1).
2. Fix the 2 misread orders from the test set (`code/tests/orders-v2.md`, #7 and #14: "half sugar" read as a size).
3. Switch on the morning summary after 3 good days.

## 5. Notes for the next AI
- The sheet's timezone was wrong once (see `docs/troubleshooting/CASEBOOK.md` #1). Check it if times look shifted.
- Raw exports are in `workflows/private/` (git-ignored). Clean before copying to `current/`.
