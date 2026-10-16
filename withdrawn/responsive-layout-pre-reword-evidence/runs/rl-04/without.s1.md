**Go with B.**

**Why B wins:**
- **It respects user settings.** The `rem` units in `clamp()` scale with the reader's browser font-size preference, so people who set larger default text still get it.
- **It scales smoothly.** The size grows with the viewport from 16px up to a 20px cap, with no jumps. The middle term (`0.92rem + 0.4vw`) includes a rem part, so zooming still works. Pure `vw` units don't have that property.
- **It has sane limits.** The floor of 1rem means text never gets too small on phones, and the 1.25rem ceiling stops it from getting oversized on big monitors.
- **It fixes line length too.** `max-width: 68ch` keeps lines at a readable 60–75 characters. That matters a lot for long-form text like recipe instructions, and neither of the other options addresses it.

**Why not the others:**
- **A (`2.2vw`)** has no minimum or maximum. On a 375px phone it comes out to about 8px, which is unreadable. On a 1920px monitor it's about 42px, which is huge. Because it's purely viewport-based, it also ignores the user's font preferences, and browser zoom may not enlarge the text, which is an accessibility failure (WCAG 1.4.4).
- **C (16px + media query)** is safe and predictable, but it has two problems. Pixel values override the user's default font size. And the text jumps from 16px to 20px at exactly 1200px instead of scaling gradually. If you like this approach, use `1rem` and `1.25rem` instead of px, but B does the same job with less code.

**One tweak to consider:** put the `max-width` on the article container, or keep it on `article` and add `margin-inline: auto` to center it. Since `ch` is relative to the element's own font size, it will track the text size as it scales.
