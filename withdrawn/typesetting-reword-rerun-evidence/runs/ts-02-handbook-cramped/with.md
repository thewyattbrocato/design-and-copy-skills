Here's the revised stylesheet. Colors and HTML are unchanged.

```css
body { font: 1.0625rem/1.55 Arial, sans-serif; color: #2b2b2b; background: #fbfaf7; margin: 0; }
.page { padding: 24px 48px; }
h1 { font-size: 2rem; line-height: 1.15; margin: 0 0 1rem; text-wrap: balance; }
h2 { font-size: 1.375rem; line-height: 1.25; margin: 2rem 0 0.5rem; text-wrap: balance; }
p { margin: 0 0 0.9rem; max-width: 65ch; text-wrap: pretty; }
.note { font-size: 0.8125rem; color: #777; }
```

- **Body text:** It was 13px with 1.2 line height. It's now about 17px with 1.55 line height, which is the main fix for the tiring, wall-of-text feel.
- **Line length:** Paragraphs are capped at `65ch`, so they stop running across the 1440px screen. Headings and notes aren't capped.
- **Heading spacing:** Each heading now has about 4× more space above than below, so it groups with the paragraphs under it instead of floating. Paragraphs are separated by a gap of about one line.
- **Notes:** `.note` goes from 10px to 13px. I left its color alone as you asked, but `#777` on `#fbfaf7` is only about 4.2:1 contrast, just under the 4.5:1 target for small text. If the notes carry anything tenants need to act on, consider darkening it to around `#6b6b6b`.
