**Go with B.**

**Why B wins**

- **It respects user settings.** The `rem` floor and ceiling scale with the reader's browser font size. The `0.92rem` base in the preferred value means the `vw` part is only a small adjustment, so zooming and larger default font sizes still work.
- **It's bounded.** The text never drops below 16px (at default settings) and never grows past 20px. The size ramps smoothly between those limits, from about 320px to 720px wide, and stays at 20px on wider screens. There are no sudden jumps.
- **It sets line length.** `max-width: 68ch` keeps lines near 60–75 characters, which is the readable range for long text like recipe instructions. Neither A nor C addresses this, and on a wide screen it matters as much as font size.

**Why not A**

Pure `vw` sizing is the one to avoid. At 375px wide, `2.2vw` is about 8px, which is unreadably small. At 1440px it's about 32px, which is far too big. It also ignores the reader's font settings. Because the size is tied only to viewport width, browser zoom doesn't enlarge the text properly, which is an accessibility failure (WCAG 1.4.4).

**Why not C**

It's safe and predictable, but weaker than B:

- `px` values ignore the user's default font size setting.
- The text size jumps from 16px to 20px at 1200px, so it's too small just below that width and too large just above.
- It has no line-length control.

If you prefer breakpoints, the better version of C uses `rem` (`1rem`, then `1.25rem`). B still gives you the smoother result with less CSS.

**Two small tweaks to consider**

- Add `line-height: 1.5` to `1.6` on `article`. It helps readability about as much as the font size does.
- Use `margin-inline: auto` with the `max-width`, or the 68ch column will sit on the left of wide screens.
