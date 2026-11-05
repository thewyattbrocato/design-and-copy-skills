Here's the revised stylesheet. Colors are unchanged, and so is the HTML. I kept your selectors.

```css
body { font: 1.0625rem/1.55 Arial, sans-serif; color: #2b2b2b; background: #fbfaf7; margin: 0; }
.page { padding: 1.5rem 3rem; max-width: 70rem; }
h1 { font-size: 2rem; line-height: 1.15; margin: 0 0 1rem; text-wrap: balance; }
h2 { font-size: 1.375rem; line-height: 1.25; margin: 2.25rem 0 0.5rem; text-wrap: balance; }
p { margin: 0 0 1em; max-width: 65ch; text-wrap: pretty; }
.note { font-size: 0.875rem; line-height: 1.5; color: #777; }
```

What changed and why:
- **Body size:** 13px became 17px (1.0625rem). 13px is too small for reading across a full-width page.
- **Line height:** 1.2 became 1.55. The tight leading was the main cause of the wall-of-text feel.
- **Line length:** paragraphs are capped at 65ch, so they no longer run edge to edge on a 1440px screen. The `.page` wrapper is capped at 70rem so headings don't sit far from the text. It's left-aligned. Add `margin: 0 auto` if you want it centered.
- **Headings:** h2 now has about 2.25rem above and 0.5rem below, so each heading groups with the text that follows it. Headings have tighter leading than body and wrap evenly.
- **Paragraph gap:** 6px became 1em, so paragraphs separate clearly.
- **`.note`:** 10px became 14px. It's still secondary, but readable.

One thing I left alone: `.note` uses `#777` on `#fbfaf7`, which is about 4.2:1 contrast. That's a bit under the 4.5:1 recommended for small text. You asked me not to touch colors, so I didn't. If you ever relax that, `#6b6b6b` would pass.
