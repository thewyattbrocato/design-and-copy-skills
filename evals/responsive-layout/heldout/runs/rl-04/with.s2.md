Go with **B**.

**Why B works**
- **It respects user settings.** `rem` follows the browser's default font size, so people who've set a larger size get it. The `vw` part is only a small nudge on top.
- **It stays zoomable.** The `rem` term scales when users zoom, so it meets WCAG 1.4.4 (resize text).
- **It's fluid but bounded.** With those numbers it runs from 16px on phones to 20px at about 1320px viewport width, then stops. There's no jump and no extreme at either end.
- **It controls line length.** `max-width: 68ch` keeps lines in the readable 60–75 character range, and since `ch` is tied to the font size, the measure stays right as the text scales. Add `margin-inline: auto` if you want the column centered.

**Why not A**
- Pure `vw` ignores the user's font preference.
- It can fail zoom: browser zoom doesn't enlarge `vw`-only text, which is an accessibility failure.
- It's too small on phones (about 8px at 375px wide) and too big on desktops (about 42px at 1920px wide).

**Why not C**
- `px` ignores the user's default font size setting.
- The jump from 16px to 20px at 1200px is abrupt.
- It does nothing about line length, so lines get very long on wide screens.
- It's fine and accessible enough if you want maximum simplicity. If you do use it, write it in `rem` (`1rem` and `1.25rem`).

On a recipe blog, people often read on a phone in the kitchen, so the 16px floor matters. Keep `line-height` around 1.5–1.6 for body text.
