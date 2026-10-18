# Decisions

Every decision that shapes this project, why it was made, and whether it still stands. Newest at the bottom.
**Never edit an old line.** To change a decision, add a new one and set the old one's status to "replaced by D-0xx" (the only edit allowed).

| # | Date | Decision | Why | Status |
|---|---|---|---|---|
| D-001 | 2026-10-01 | Customers order through a **Telegram bot**. | Most regulars already use it; bots are free; buttons for confirm/cancel. | ✅ |
| D-002 | 2026-10-01 | Orders go into **Mai's existing Google Sheet**, new tab "Orders". | She already lives in that sheet; no new app to learn. | ✅ |
| D-003 | 2026-10-01 | **n8n on a $5 VPS**, not a paid automation plan. | ~1,500 runs a month would cost more on per-task pricing. | ✅ |
| D-004 | 2026-10-03 | Pickup time is **required**; the bot asks once if it's missing. | Without a time, Mai can't plan the rush (3 of 20 test orders had none). | ✅ |
| D-005 | 2026-10-03 | The 7:30 summary goes to **Mai only**. | The customer group doesn't need to see everyone's orders. | ✅ |
