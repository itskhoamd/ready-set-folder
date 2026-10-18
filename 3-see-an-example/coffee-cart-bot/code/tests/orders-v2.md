# Test orders v2 (fake)

20 made-up orders and what the bot should read. Run after every prompt change; note the score in `_system/CHANGELOG.md`.

| # | Message | Expected | v3 result |
|---|---|---|---|
| 1 | `1 iced latte 8:15` | latte · iced · regular · 08:15 | ✅ |
| 2 | `2 flat whites, oat, quarter past 8` | flat white ×2 · oat · 08:15 | ✅ |
| 7 | `large mocha half sugar 8am` | mocha · large · sugar 50% · 08:00 | ❌ size read as medium |
| 14 | `cappu half sugar in 20 min` | cappuccino · sugar 50% · now+20 min | ❌ size read as small |
| … | (16 more) | | 18/20 ✅ |
