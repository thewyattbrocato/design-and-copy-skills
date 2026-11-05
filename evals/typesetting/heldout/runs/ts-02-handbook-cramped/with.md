```css
body { font: 1.0625rem/1.55 Arial, sans-serif; color: #2b2b2b; background: #fbfaf7; margin: 0; }
.page { padding: 24px 48px; }
h1 { font-size: 2rem; line-height: 1.15; margin: 0 0 1rem; text-wrap: balance; }
h2 { font-size: 1.375rem; line-height: 1.25; margin: 2.25rem 0 0.75rem; text-wrap: balance; }
p { margin: 0 0 1em; max-width: 65ch; text-wrap: pretty; }
.note { font-size: 0.8125rem; line-height: 1.5; color: #777; }
```

What changed and why:
- **Body:** 13px became 17px (1.0625rem), and line height went from 1.2 to 1.55. The tight leading was the main cause of the wall-of-text feel.
- **Line length:** paragraphs are capped at 65ch, about 65 characters. On a 1440px screen they now stop partway across the page and no longer run edge to edge. I capped the `p` element, not `.page`, so headings and other elements can still use the full width.
- **Headings:** h1 is 32px and h2 is 22px. Each h2 has about three times as much space above as below, so it sits with the section it introduces.
- **Paragraph gaps:** 6px became 1em, so paragraphs are visibly separate.
- **`.note`:** 10px became 13px (0.8125rem). I left its color as it was, as you asked.

Two notes:
- `.note` is `#777` on `#fbfaf7`, which is about 4.2:1 contrast and just under the 4.5:1 WCAG AA minimum. The size increase helps, but a slightly darker gray would fully fix it. That's a color change, so I didn't make it.
- If `.note` text is ever wider than 65ch, add the same `max-width` to it.
