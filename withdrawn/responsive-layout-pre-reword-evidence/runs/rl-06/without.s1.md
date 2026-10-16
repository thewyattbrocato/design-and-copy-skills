The CSS is already responsive, so your developer is mostly right. I read it but didn't render it, because I only have the CSS and no HTML.

**What's already good**
- `--gutter` uses `clamp()`, so the side padding scales smoothly with no breakpoints.
- The `h1` mixes `rem` and `vw`, so it scales with the viewport and still responds to browser zoom and text-size settings. It runs from 28px at 320px wide up to 52px at about 1310px wide.
- `.grid` uses `minmax(min(100%, 16rem), 1fr)`. The `min()` stops a single column from overflowing on screens narrower than 16rem, which is the usual bug in this pattern.
- `.prose` caps line length at 65ch.
- `img` is fluid and keeps its aspect ratio.

**Small gaps worth fixing**
1. **Grid blowout:** `1fr` has an implicit `min-width: auto`. A long URL, a `<pre>` or a wide table inside a card can push the grid past the screen on mobile. Adding `min-width: 0` to the children fixes it.
2. **No `box-sizing: border-box`:** with the default `content-box`, `.wrap` is 72rem plus padding. That works, but it's surprising and usually not what's intended.
3. **Headings:** long headings can wrap with a single word on the last line, and `text-wrap: balance` fixes that. The browser's default heading margins also scale with font size, so they're worth checking.
4. **Images:** `display: block` removes the small gap under inline images.

**Tidied version**
```css
*, *::before, *::after { box-sizing: border-box; }

:root {
  --gutter: clamp(1rem, 4vw, 2.5rem);
  --measure: 65ch;
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
  text-wrap: balance;
}

.prose { max-width: var(--measure); }

.grid {
  display: grid;
  gap: 1.5rem;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
}
.grid > * { min-width: 0; }

img { display: block; max-width: 100%; height: auto; }
```

`box-sizing: border-box` makes `.wrap` exactly 72rem wide including its padding, so the content area is slightly narrower than before. If the layout was signed off at the old width, bump `max-width` by twice the gutter, or leave `.wrap` as it was.

**Check these outside the CSS**
- The HTML `<head>` needs `<meta name="viewport" content="width=device-width, initial-scale=1">`. Without it, mobile browsers ignore all of this and render a zoomed-out desktop page. This is the most common reason "responsive" CSS fails in practice.
- Test at 320px, 768px and 1280px wide. Also zoom to 200% and look for horizontal scrolling.
- Give `img` explicit `width` and `height` attributes to avoid layout shift while images load.

If you paste the HTML or point me at the files, I can check those items and run it at those widths.
