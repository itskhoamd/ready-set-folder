# JOURNEY (optional)

> The story log of this project. `_system/CHANGELOG.md` says **what** changed; this file says **why**, what you tried, what broke, the real numbers, and the moments worth telling.

---

## 2026-10-03 · The "half sugar" problem
- What we set out to do: read pickup times and build the morning summary.
- What happened: the order prompt went from 13/20 to 18/20 on the test set after splitting size and sugar into separate fields.
- What broke: "half sugar" kept turning a large into a medium. The AI saw "half" as a size.
- The moment worth telling: Mai's reaction to the first summary: "So I can sleep 10 more minutes."
