Here's the revised stylesheet. Colors are untouched, and there are no HTML changes.

```css
body { font: 1.0625rem/1.55 Arial, sans-serif; color: #2b2b2b; background: #fbfaf7; margin: 0; }
.page { padding: 1.5rem 3rem; max-width: 46rem; margin: 0 auto; }
h1 { font-size: 2rem; line-height: 1.15; margin: 0 0 1rem; text-wrap: balance; }
h2 { font-size: 1.375rem; line-height: 1.25; margin: 2.25rem 0 0.75rem; text-wrap: balance; }
p { margin: 0 0 1em; text-wrap: pretty; }
.note { font-size: 0.875rem; line-height: 1.45; color: #777; }
```

What changed and why:
- **Body:** 13px became 17px (`1.0625rem`), and line height went from 1.2 to 1.55. The old setting was small and tight, which is what made it tiring.
- **Line length:** `.page` is now capped at `46rem`, about 70 characters per line, and centered. Text no longer runs edge to edge on a 1440px screen.
- **Headings:** Each `h2` has about three times as much space above as below, so it attaches to the section it introduces. The `h1` and `h2` have tighter line heights and balanced wrapping.
- **Paragraphs:** The gap is now one line (`1em`) instead of 6px.
- **`.note`:** It goes from 10px to 14px, since 10px is too small to read. I left its gray alone as you asked, but `#777` on `#fbfaf7` is about 4.3:1 contrast, just under the 4.5:1 target for small text. You may want to darken it slightly later.

I assumed the page is read on screen and that Arial stays.
