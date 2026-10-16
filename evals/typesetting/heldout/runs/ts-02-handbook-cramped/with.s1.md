Here's the revised stylesheet. Colors and HTML are untouched.

```css
body { font: 1rem/1.5 Arial, sans-serif; color: #2b2b2b; background: #fbfaf7; margin: 0; }
.page { padding: 24px 48px; }
h1 { font-size: 2rem; line-height: 1.2; margin: 0 0 1rem; text-wrap: balance; }
h2 { font-size: 1.375rem; line-height: 1.25; margin: 2.5rem 0 0.75rem; text-wrap: balance; }
p { margin: 0 0 1em; max-width: 65ch; text-wrap: pretty; }
.note { font-size: 0.875rem; color: #777; }
```

What changed and why:
- **Body size:** 13px became 1rem (16px). Small type was a big part of the tiring feel.
- **Line height:** 1.2 became 1.5. Lines had almost no air between them.
- **Line length:** `p` is capped at 65ch, so paragraphs no longer run edge to edge on a 1440px screen. The text sits at the left, and the right side of the page will be empty. If you want it centered, wrap the content in a centered container, but that needs an HTML change.
- **Headings:** h2 has about 2.5rem above and 0.75rem below, so each heading groups with the text that follows it. Sizes are 2rem for h1, 1.375rem for h2 and 1rem for body, which gives clear steps.
- **Paragraph spacing:** the gap between paragraphs went from 6px to one line.
- **`.note`:** it goes from 10px to 14px. Your `#777` on `#fbfaf7` is about 4.1:1 contrast, which is below the 4.5:1 accessibility threshold for small text. I left it as you asked. Darkening it slightly, to `#6b6b6b`, would fix that if you ever want to.
