**Go with B.**

**Why B wins:**
- **Respects user settings.** The `rem` base means it scales with the reader's browser font-size preference. The `0.92rem` part also keeps a `vw`-driven zoom response, so pinch/browser zoom still enlarges text (WCAG 1.4.4).
- **Fluid but bounded.** `clamp(1rem, …, 1.25rem)` goes from 16px on phones to 20px on wide screens, with no sudden jumps and no extreme sizes.
- **Line length is handled.** `max-width: 68ch` keeps lines at about 60–75 characters, which is the readable range for long text like recipe instructions. A and C don't address this at all.

**Why not A:** Pure `vw` sizing is the worst option. It ignores the user's font preference and can fail zoom accessibility, because zooming doesn't reliably enlarge the text. It's also too small on phones (2.2vw is about 8px at 375px wide) and huge on big monitors (about 42px at 1920px).

**Why not C:** It's accessible and simple, but it has a hard jump at 1200px. It also uses `px`, which can override the user's browser font-size setting. If you prefer this approach, use `1rem` and `1.25rem` instead of pixels, and add a `max-width` in `ch`.

**One tweak to consider:** If you want a clearer step up on large screens, adjust the middle term (for example `0.9rem + 0.5vw`). The current values reach the 20px cap at roughly 1250px wide, which is fine for most blogs.
