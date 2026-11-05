```css
body { font: 1.0625rem/1.55 Arial, sans-serif; color: #2b2b2b; background: #fbfaf7; margin: 0; }
.page { padding: 24px 48px; }
h1 { font-size: 2rem; line-height: 1.15; margin: 0 0 1rem; text-wrap: balance; }
h2 { font-size: 1.375rem; line-height: 1.25; margin: 2.25rem 0 0.75rem; text-wrap: balance; }
p { margin: 0 0 1em; max-width: 65ch; text-wrap: pretty; }
.note { font-size: 0.8125rem; line-height: 1.45; color: #777; }
```

What changed and why:
- **Body:** 13px at 1.2 became 17px (1.0625rem) at 1.55. That's the main cause of the tiring wall of text.
- **Line length:** `p` is capped at `65ch`, so paragraphs stop running edge to edge on a 1440px screen. I capped the paragraphs and left `.page` alone, so headings and the layout still use the full width.
- **Headings:** h1 and h2 now have about twice as much space above as below, so each one attaches to the section it introduces. Paragraph gaps went from 6px to a full line.
- **Notes:** `.note` went from 10px to 13px. It stays smaller than body, but it's now readable. I left the color as is.

The HTML and colors are untouched. `#777` on `#fbfaf7` is about 4.2:1 contrast, a little under the 4.5:1 AA threshold for small text. If you ever decide to relax the color rule, `#6b6b6b` would pass.
