Go with **B**.

**Why B wins**

- **It respects user settings.** The `rem` part of the clamp scales with the browser's default font size, so readers who've bumped their default up still get larger text.
- **It passes zoom accessibility.** Pure `vw` (option A) doesn't grow when the user zooms, which fails WCAG 1.4.4 (Resize Text). Mixing in a `rem` term, as B does, keeps zoom working.
- **It has sane bounds.** The text never drops below 16px (1rem) or goes above 20px (1.25rem), and it scales smoothly between those limits. There are no jumps at breakpoints.
- **It limits line length.** `max-width: 68ch` keeps lines at a comfortable 60–75 characters, which matters a lot for people reading a recipe while cooking. Neither A nor C addresses this.

**Why not A**

`2.2vw` has no floor or ceiling. On a 375px phone it comes to about 8px, which is unreadable. On a 1920px monitor it's about 42px, which is huge. It also ignores zoom, as noted above.

**Why not C**

It works, but it has two drawbacks:

- `px` ignores the user's browser font-size preference.
- The jump from 16px to 20px at 1200px is abrupt, and there's nothing in between. It also has no line-length control.

If you'd rather use C, switch the values to `rem` (`1rem` and `1.25rem`). That fixes the preference problem.

**One tweak to B**

Some of the recipe's text (ingredient lists, notes, captions) may want to scale relative to the body size. Use `em` or `rem` for those so they follow the article's size and don't set their own.
