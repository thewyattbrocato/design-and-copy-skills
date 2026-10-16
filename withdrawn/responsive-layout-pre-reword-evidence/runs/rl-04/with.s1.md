**Go with B.**

**Why B wins**

- **It respects user settings.** The `rem` in the clamp means the size scales with the reader's browser default font size. Someone who has bumped their default up for readability still gets a larger size.
- **It scales smoothly but within limits.** The size ranges from 16px to 20px, growing gradually with viewport width. It never gets too small to read or too large to look odd.
- **It passes zoom accessibility.** The `0.92rem` part of the preferred value keeps a `rem` component, so pinch and browser zoom still enlarge the text. (WCAG 1.4.4 requires text to resize up to 200%.)
- **`max-width: 68ch` limits line length.** Around 60–75 characters per line is the comfortable reading range. Recipe pages, where people glance back and forth between the text and the kitchen, benefit from this.

**Why not A**

`2.2vw` is purely viewport-relative, so it has no floor or ceiling. On a 375px phone it comes out to about 8px, which is unreadable. On a 1920px monitor it comes to about 42px, which is huge. It also ignores the user's font preferences, and zoom barely affects it, which is an accessibility failure.

**Why not C**

It works, but the size jumps from 16px to 20px at 1200px with nothing in between. A hard-coded `px` value also overrides the user's browser default font size. It also does nothing to control line length, so you'd still need a `max-width`.

**Optional tweaks for B**

- Check that the max (1.25rem) is the size you want on desktop. At that size, 68ch is about 700–750px wide.
- If you want to double-check zoom behavior, zoom to 200% on a desktop browser. The text should visibly grow.
