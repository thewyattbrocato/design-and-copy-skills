Your type setup is sound, so I'd change just one thing.

**What works**
- A system font stack suits a volunteer-run portal. It loads instantly, needs no licensing, and looks native on each device.
- Both stacks end in real generic fallbacks.
- 17px body text with 1.55 line height is comfortable to read.
- Tight headings with slightly negative tracking look right.
- `tabular-nums` with right-alignment keeps number columns lined up.
- Monospace is used only for `code`.

**The one change: heading weight**
`650` only renders as written on variable system fonts like San Francisco. Roboto and Segoe UI ship fixed weights, so the browser snaps `650` to a different real weight depending on the device. Headings would then look a little different from one member to the next. A named weight gives the same result everywhere:

```css
h1, h2, h3 { font-family: var(--font-body); font-weight: 600; line-height: 1.2; letter-spacing: -0.01em; }
```

I assumed screen use, an English-language audience, and no web fonts. If you ever want a more distinctive look, add one heading font and keep this stack for everything else. I wouldn't do that unless you want it, because the current setup is reliable.
