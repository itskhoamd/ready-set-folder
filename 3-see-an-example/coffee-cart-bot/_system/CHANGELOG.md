# Changelog

Newest first. Format: `YYYY-MM-DD` · **[area]** what changed. Rules: `_system/HOUSE-RULES.md` §3.

---

## 2026-10-03
- **[workflow]** Order bot v0.2: reads pickup times ("8:15", "quarter past 8", "in 20 min"), asks once if missing (D-004).
- **[prompt]** `read-order.md` v3: sizes vs sugar levels split into separate fields. Test set: 18/20 right (was 13/20).
- **[workflow]** Morning summary v0.1 built (`beancart-summary.json`), not switched on yet (D-005).
- **[docs]** Casebook #1: sheet timezone.

## 2026-10-02
- **[guide]** `guides/2026-10-02_SETUP.md` Parts A–B. Mai finished Part A (bot + sheet).
- **[tests]** `code/tests/orders-v2.md`: 20 fake orders with expected results.

## 2026-10-01
- **[setup]** Set up as automation-builder for "Bean Cart Orders" (ready-set-folder v1.0).
- **[decision]** D-001 to D-003 (Telegram, Google Sheets, n8n self-hosted).
