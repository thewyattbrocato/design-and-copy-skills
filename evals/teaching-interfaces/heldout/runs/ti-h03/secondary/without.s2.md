**Recommendation: (c), the interactive setup.**

**Why:** The mistake new users make is misjudging how the settings interact with real conditions. A carousel or video can explain that "wind limit 15 kt" means alerts are suppressed above 15 kt, but it can't show whether that setting would fire today at their beach. A live preview can: "With these settings, you'd have gotten 0 alerts today. Wind was 18 kt, and your limit is 15." That turns each setting into a concrete consequence, which is the understanding the other two options only describe.

**Why not the others:**
- **(a) Video:** Passive, and people skip or forget 90-second videos. It's also expensive to produce and goes stale as the setup UI changes.
- **(b) Carousel:** Cheap and quick, and it's the right fallback. But it explains settings in the abstract, and abstract explanations are what new users already fail to apply.

**Risks of (c):**
- It's the most expensive to build, and it depends on a live conditions feed working during onboarding. If the feed is down, the preview breaks at the moment of first impression.
- Multi-step flows lose people. Keep it to the four settings, let users accept sensible defaults, and make it skippable.
- If the preview shows "0 alerts," users may want to adjust immediately. Make that a suggestion ("loosen wind to 20 kt to see 3 alerts this week") rather than a dead end.

**Since you have no data, I'd ship (c) with these measurements so you learn quickly:**
1. Setup completion rate (started → first alert saved).
2. Share of users who edit the defaults before saving.
3. Whether a first alert actually fires within 7 days. This is the real success metric, since a saved alert that never triggers usually means the settings were wrong.

If you can't build (c) in the sprint, ship (b) and track the same three metrics. That gives you a baseline to compare against when you do build the interactive version.
