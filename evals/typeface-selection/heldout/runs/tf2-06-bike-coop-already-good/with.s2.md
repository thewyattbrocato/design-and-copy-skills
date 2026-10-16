This type setup is sound, so I'd change only one thing.

**What works**
- The system stack is a good fit for a volunteer-run portal. It loads instantly, needs no licensing, and looks native on each device.
- 17px body text with 1.55 line height is comfortable to read.
- Headings use tight leading and slight negative tracking, which suits bold text.
- `tabular-nums` with right alignment keeps number columns lined up.
- Monospace is used only for `code`, and `0.92em` stops it looking oversized next to the body text.

**What to change: the heading weight**

`650` only works on variable system fonts like San Francisco. Roboto, Segoe UI and Arial are mostly static files, so the browser rounds 650 to 600 or 700. Your headings will then look a little different on each device. Use a weight every font in the stack has:

```css
h1, h2, h3 { font-family: var(--font-body); font-weight: 700; line-height: 1.2; letter-spacing: -0.01em; }
```

I'd pick 700 because it exists in every font in your stack. 600 also looks good on Apple devices, but it often falls back to bold anyway on Windows and Android.

**Optional:** if members ever see the portal on Linux, add `"DejaVu Sans Mono"` before the final `monospace` in `--font-mono`. This is not needed for most members.

I made these notes from the CSS alone and haven't checked how it renders on any device.
