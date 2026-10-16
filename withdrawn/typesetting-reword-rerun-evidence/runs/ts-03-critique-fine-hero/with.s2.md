The type is mostly sound. The 56/20/16 sizes, the 1.5 body leading and the tight h1 leading all work. These are the real problems:

**1. The stats have no labels.** This is the biggest issue. "1,284 / 97 / 12,060" tells a reader nothing, and nobody can guess that 97 is streak days. They also need `tabular-nums`. They're right-aligned in a stack, so digits only line up if every figure has the same width.

**2. The eyebrow fails on both counts.** It's 11px, below the 12px floor, and all-caps with `letter-spacing: 0`. Untracked small caps look cramped and are hard to read. Its default `<p>` bottom margin (16px) also collapses with the h1's 8px top margin and wins, so the gap you wrote is ignored.

**3. The body paragraph runs about 80 characters per line.** At 16px in a 640px box, that's past the 75 limit. The lead is fine. Cap the paragraph, not the hero.

**4. The h1 is a fixed 56px.** On a phone it will break into 4–5 short lines. It needs `clamp()`, and `text-wrap: balance` will stop an orphaned last word. The 1.05 leading is fine at this size.

Fixes:

```css
.eyebrow { font-size: 0.8125rem; letter-spacing: 0.08em; text-transform: uppercase; font-weight: 600; color: #6b5d3f; margin: 0 0 8px; }
h1 { font-size: clamp(2.25rem, 7vw, 3.5rem); text-wrap: balance; /* rest unchanged */ }
.body { max-width: 65ch; text-wrap: pretty; /* rest unchanged */ }
.stat { font-size: 2rem; line-height: 1.1; font-weight: 700; font-variant-numeric: tabular-nums; }
.stat-label { display: block; font-size: 0.875rem; font-weight: 400; color: #6b5d3f; }
```

```html
<div class="stat">1,284 <span class="stat-label">drills</span></div>
<div class="stat">97 <span class="stat-label">day streak</span></div>
<div class="stat">12,060 <span class="stat-label">strokes scored</span></div>
```

Each stat's number and label sit together in one block. If you right-align the card, align the labels the same way.

I left the color, the lead and the h1 weight alone because they work.
