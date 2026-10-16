This setup is sound, so I'd change only one thing.

**What works**
- The system font stack needs no downloads, loads instantly, and looks native on every device. That suits a volunteer-run portal.
- Body text at 17px with 1.55 line height reads comfortably.
- Headings use the same family at a heavier weight with tighter line height and spacing. That's all the hierarchy you need.
- `tabular-nums` on right-aligned number columns keeps digits lined up.
- Monospace is only used for `code`, and the `0.92em` size stops it looking oversized next to body text.

**The one fix: change the heading weight from 650 to 600 or 700**
Most system fonts (Segoe UI, Roboto, Helvetica Neue, Arial) come in fixed weights, not a continuous range. A 650 weight gets rounded to whichever weight each device has, so headings will look slightly different from machine to machine. Use `600` if you want a softer heading, or `700` if you want a firmer one. I'd pick 600:

```css
h1, h2, h3 { font-family: var(--font-body); font-weight: 600; line-height: 1.2; letter-spacing: -0.01em; }
```

You could also delete `font-family: var(--font-body)` from the heading rule, since headings inherit it from `body`. It's harmless, so leave it if you prefer.

I'd skip adding a web font. It would add loading and licensing work for little gain here. If the portal later needs a more distinct look, one open-licensed sans with a real semibold would be the upgrade, but nothing is broken now.

I assumed Latin-script text on screens, with no brand font mandated.
