## What's happening

Two separate behaviors, both caused by the browser rendering text before the font file arrives:

- **Invisible headline (FOIT).** With no `font-display` set, or with `block`, browsers hide text for up to about 3 seconds while they wait for the font. That's your blank headline.
- **Different font, then a jump (FOUT plus layout shift).** If text is shown in a fallback first, the swap changes glyph widths and line heights when the real font lands. Headings wrap differently, so everything below them moves. This counts against your CLS score.

Your body text is the system font, so it's fine. Only the headings are affected, but a large headline moving is very noticeable.

## What to do

1. **Never hide the text.** Add `font-display: swap`, or `optional` if you'd rather skip the swap than shift the layout.
2. **Preload the one critical file** so the swap happens sooner. Use `crossorigin`, even for same-origin fonts.
3. **Tune a fallback to match your font's metrics.** This is the fix for the jump. Without it, `swap` only trades the invisible text for a layout shift.
4. **Self-host and subset to WOFF2** for the scripts you actually use. A smaller file arrives sooner and shrinks the window in which any of this is visible.

```html
<link rel="preload" href="/fonts/heading-var.woff2" as="font" type="font/woff2" crossorigin>
```

```css
@font-face {
  font-family: "Heading";
  src: url("/fonts/heading-var.woff2") format("woff2");
  font-weight: 100 900;      /* match the file's real wght range */
  font-display: swap;
}

/* Local fallback tuned to the web font's metrics */
@font-face {
  font-family: "Heading Fallback";
  src: local("Arial");
  size-adjust: 104%;         /* placeholder values, see below */
  ascent-override: 92%;
  descent-override: 24%;
  line-gap-override: 0%;
}

h1, h2, h3 {
  font-family: "Heading", "Heading Fallback", system-ui, sans-serif;
  font-synthesis: none;
}
```

The override numbers above are placeholders. Compute them from your font's actual metrics. Tools like Capsize, or the `fontaine` plugin if you use a bundler, will generate them. Frameworks such as Next.js (`next/font`) do this automatically.

## Choosing swap or optional

- **`swap`**: the heading always ends up in your font. With tuned fallback metrics, the visible change is small.
- **`optional`**: the browser gives the font a very short window (about 100ms). If it misses that, it uses the fallback for that page view and caches the font for the next one. This means no shift at all, but some first-time visitors never see your heading font. Because the heading is a brand element, I'd start with `swap` plus the metric-matched fallback.

## Variable font notes

- Set the `font-weight` range in `@font-face` to what the file actually contains. A mismatch can cause synthesized weights.
- Keep `font-synthesis: none` so a missing weight or italic doesn't get faked.
- Use named weight tokens in your CSS rather than raw axis values.

## Check it

Test in DevTools with network throttling (Slow 4G), with the cache disabled, and once with the font file blocked. The page should always show readable text. The heading shouldn't visibly move when the font arrives, and you can confirm that in Lighthouse or the Performance panel's layout shift markers.

I haven't seen your code, so I can't say which of these you already have. If you point me to the CSS or the framework you use, I can check what's set and compute the real fallback values.
