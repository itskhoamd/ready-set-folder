# Casebook

Known problems and their fixes. Newest at the bottom. The AI checks here before debugging.

| # | Date | What happened | Why | Fix |
|---|---|---|---|---|
| 1 | 2026-10-03 | Pickup times in the sheet were 7 hours early. | The Google Sheet's timezone was set to the default, not the cart's local time. | Sheet → File → Settings → Time zone → local time. Also set the n8n workflow's timezone. |
