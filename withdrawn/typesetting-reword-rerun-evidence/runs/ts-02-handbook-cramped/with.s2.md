Here's the revised stylesheet. Colors and HTML are unchanged.

```css
body { font: 1.0625rem/1.55 Arial, sans-serif; color: #2b2b2b; background: #fbfaf7; margin: 0; }
.page { padding: 1.5rem 3rem; }
h1 { font-size: 2rem; line-height: 1.15; margin: 0 0 1rem; text-wrap: balance; }
h2 { font-size: 1.375rem; line-height: 1.25; margin: 2.25rem 0 0.75rem; text-wrap: balance; }
p { margin: 0 0 1rem; max-width: 65ch; text-wrap: pretty; }
.note { font-size: 0.8125rem; line-height: 1.45; color: #777; }
```

What changed and why:
- **Body:** 13px at 1.2 leading became 17px (`1.0625rem`) at 1.55. That fixes most of the tiring feel.
- **Line length:** `p` is capped at `65ch`, so paragraphs no longer run edge to edge on a 1440px screen. The cap is on the paragraphs, so the page padding and headings are unaffected.
- **Headings:** h1 is 32px and h2 is 22px, with tighter leading than the body. Each h2 has about 3× more space above than below (36px vs 12px), so it sits with the section it introduces.
- **Paragraph gaps:** the gap is now 1rem, roughly one line, up from 6px.
- **Notes:** `.note` goes from 10px to 13px. I kept its `#777` color as you asked. It's lighter than the body text, so it's the one place I'd consider a darker gray if you ever relax the no-color-changes rule.

The 65ch cap leaves the right side of the page empty on wide screens. If that bothers you, the usual fix is to put the text in a centered or two-column layout, but that would mean changing the HTML.
