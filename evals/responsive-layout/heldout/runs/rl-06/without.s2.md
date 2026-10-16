The CSS is already responsive. I didn't find anything broken, so the developer was right. I only read it. I didn't render it, and I haven't seen the HTML.

**What's already right**
- `--gutter` uses `clamp()`, so side padding scales smoothly.
- `.wrap` caps at 72rem and centres with `margin-inline: auto`.
- The `h1` uses `clamp()` with a `rem` term in the middle value, so it still responds to browser zoom and font-size settings.
- `.prose` at 65ch keeps line lengths readable.
- The grid uses `minmax(min(100%, 16rem), 1fr)`. The `min(100%, …)` stops overflow on screens narrower than 16rem, which is the detail people usually miss.
- `img { max-width: 100%; height: auto }` is correct.

**Small gaps worth closing**
1. There's no `box-sizing: border-box` reset, which causes surprise overflow once anyone adds padding and borders to sized elements.
2. `video`, `svg` and `iframe` aren't covered like `img` is.
3. Grid children can blow out the layout with long words, URLs or `<pre>` blocks unless they have `min-width: 0`.
4. Long unbroken strings can overflow on narrow screens.

**Tidied version**
```css
:root {
  --gutter: clamp(1rem, 4vw, 2.5rem);
}

*,
*::before,
*::after {
  box-sizing: border-box;
}

body {
  margin: 0;
  font: 1rem/1.6 system-ui, sans-serif;
  overflow-wrap: break-word;
}

.wrap {
  max-width: 72rem;
  margin-inline: auto;
  padding-inline: var(--gutter);
}

h1 {
  font-size: clamp(1.75rem, 1.2rem + 2.5vw, 3.25rem);
  line-height: 1.15;
}

.prose {
  max-width: 65ch;
}

.grid {
  display: grid;
  gap: 1.5rem;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
}

.grid > * {
  min-width: 0;
}

img,
video,
svg {
  max-width: 100%;
  height: auto;
}
```

**Things the CSS can't tell me**
- The page needs `<meta name="viewport" content="width=device-width, initial-scale=1">` in the `<head>`. Without it, mobile browsers ignore all of this and render a zoomed-out desktop layout. This is the first thing I'd check.
- Wide tables and code blocks need `overflow-x: auto` on a wrapper if the page has them.
- Any fixed `width` or `px` values in other stylesheets could undo this.

If you share the HTML or the other stylesheets, or point me to the project files, I can check those and test it at real breakpoints (320, 768 and 1280px).
