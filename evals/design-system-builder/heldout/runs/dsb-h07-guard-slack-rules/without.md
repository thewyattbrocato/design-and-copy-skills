**Design tokens: naming + changes** 🎨

**Naming:** `category-role-variant-state`
- `color-text-muted`, `color-bg-surface-hover`
- `space-4`, `space-8` (scale steps, never raw px)
- Name by *purpose*, not value: `color-danger`, not `color-red-500`.

**Rule:** No hex codes or raw px in components. If a token doesn't exist, don't invent a one-off.

**To propose a new token or change:**
1. Check the existing tokens first. Can one already do the job?
2. Open a ticket in #design-systems with: the token name, value, where it's used, and why existing ones don't fit.
3. Design and eng each approve. We review weekly.

Questions? Reply in thread.

---
That's about 105 words. Swap in your real channel name, review cadence, and naming pattern if they differ. I made those up as placeholders.
