Your type setup is already sound, so I'd make one small change.

**What works**
- It uses one family with real range. Headings and body share the system UI stack, and the weight and size do the hierarchy.
- The body text is 17px with 1.55 line height, which is comfortable for reading.
- Mono is used only for `code`.
- `tabular-nums` and right alignment on number cells keep dues and counts lined up.
- Every stack ends in a real fallback, and nothing depends on a web font loading. That's a good choice for a volunteer-run site.

**The one change**
- `font-weight: 650` only works on variable system fonts like San Francisco on Apple devices. Segoe UI and static Roboto only have 400, 600 and 700, so headings will render differently on different machines. Using `600` makes them match across platforms.
- Headings already inherit the body font, so the `font-family` line on `h1, h2, h3` is redundant. It's harmless, but I removed it.

```css
h1, h2, h3 { font-weight: 600; line-height: 1.2; letter-spacing: -0.01em; }
```

**Optional**
- If you ever use `<em>` or `<strong>` in a font that lacks that style, add `font-synthesis: none;` to `body` so the browser doesn't fake it. The system fonts you're using have real italics and bolds, so this isn't needed now.

I assumed a screen-only, English-language portal with no custom fonts installed. If you later want a distinct brand look, that would be the point to add a second font for headings. For a member portal, I'd leave it as is.
