Go with **B**.

**Why B wins**

- **It respects user preferences.** The `rem` floor and ceiling scale with the reader's browser font setting, and the `0.92rem + 0.4vw` middle term keeps zoom working. That matters for a recipe blog, where people read from a phone or tablet propped up in the kitchen, often with larger text settings.
- **It's bounded.** The text never drops below 16px (1rem) or grows past 20px (1.25rem). It scales smoothly between those limits, with no jumps.
- **It sets line length.** `max-width: 68ch` keeps lines at roughly 60–75 characters, the readable range. This does as much for readability as the font size does. At 20px on a wide monitor, an uncapped column would be exhausting to read.

**Why not A**

`2.2vw` is purely viewport-based, so it has two problems:

- On a 375px phone it comes out around 8px, which is unreadably small.
- On a 1920px monitor it comes out around 42px, which is huge.

It also ignores the user's font-size preference, and because `vw` doesn't respond to browser zoom, it can fail WCAG 1.4.4 (resize text). Don't use it.

**Why not C**

C is safe and predictable, but it has these drawbacks:

- `px` ignores the user's default font-size setting, which is an accessibility regression.
- The size jumps from 16px to 20px at 1200px instead of scaling.
- It does nothing about line length.

If you used `rem` instead of `px` (`1rem` → `1.25rem`), it would be acceptable, but B does the same job more smoothly.

**One tweak to consider**

Put `max-width: 68ch` on a wrapper or on the paragraphs if your `article` also holds full-width images or ingredient tables. Otherwise those get squeezed too. For example, use `article > p, article > ul { max-width: 68ch; }`, or add `margin-inline: auto` to center the column.
