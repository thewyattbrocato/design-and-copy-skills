**Go with B.**

**Why B wins**

- **It respects user preferences.** The `rem` floor and ceiling scale with the reader's browser font setting. The `vw` term only adds a gentle slope in between. The size never drops below 16px (at default settings) or goes above 20px.
- **It's still zoomable.** Pure `vw` units (option A) don't respond to browser zoom or text-size settings, which is an accessibility failure (WCAG 1.4.4). The `rem` component in `clamp()` keeps zoom working.
- **It sets line length.** `max-width: 68ch` keeps lines around 60–75 characters, which is the readability sweet spot. Recipe pages with ingredient lists and step-by-step instructions benefit from this, especially on wide monitors. Neither A nor C addresses it.
- **It scales smoothly.** There are no jumps at breakpoints. Size grows from 16px at about 400px wide to 20px at about 1050px wide.

**Why not the others**

- **A (`2.2vw`)** is the worst choice. On a 360px phone it's about 8px, which is unreadable. On a 1920px monitor it's about 42px, which is huge. It also ignores zoom and user font settings.
- **C (16px + media query)** is safe and predictable, but it has two problems. Pixel values override the user's default font size setting. It also jumps from 16px to 20px at 1200px instead of scaling, and it leaves line length uncontrolled. If you like this approach, use `1rem` and `1.25rem` instead of `px`. That fixes the biggest flaw.

**Small tweaks to consider**

- Add `line-height: 1.5` to `1.6` for body text.
- Put `margin-inline: auto` on `article` if you want the 68ch column centered.
- If the article has images or wide tables, let them break out of the `max-width` separately.
