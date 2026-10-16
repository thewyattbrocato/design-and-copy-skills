Here's the revised stylesheet. Colors and HTML are untouched.

```css
body { font: 1.0625rem/1.55 Arial, sans-serif; color: #2b2b2b; background: #fbfaf7; margin: 0; }
.page { padding: 1.5rem 3rem; max-width: 70rem; }
h1 { font-size: 2rem; line-height: 1.15; margin: 0 0 1rem; text-wrap: balance; }
h2 { font-size: 1.375rem; line-height: 1.25; margin: 2.25rem 0 0.5rem; text-wrap: balance; }
p { margin: 0 0 1em; max-width: 65ch; text-wrap: pretty; }
.note { font-size: 0.8125rem; line-height: 1.45; color: #777; }
```

What changed and why:
- **Body:** 13px at 1.2 leading became 17px (`1.0625rem`) at 1.55. That's the main cause of the tiring read.
- **Line length:** paragraphs are capped at `65ch` (about 65 characters per line) instead of running 1440px wide. The cap is on `p`, so headings and the page wrapper keep their width. I also capped `.page` at 70rem so the content doesn't sit far from its headings on wide screens.
- **Headings:** h2 now has about 4× more space above (2.25rem) than below (0.5rem), so each heading groups with the text under it. Sizes are 32px for h1 and 22px for h2, which gives clear steps above the body.
- **Paragraph gap:** it's now a full line (`1em`) instead of 6px.
- **`.note`:** 10px was too small to read. It's now 13px, and I left its color as is.

One thing to check: `#777` on `#fbfaf7` is about 4.3:1 contrast, just under the 4.5:1 AA level for small text. You asked me not to touch colors, so I didn't. If any `.note` text is important, like deadlines or fees, a slightly darker gray such as `#6b6b6b` would pass.
