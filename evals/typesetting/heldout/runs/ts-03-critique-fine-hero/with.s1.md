The body, lead and headline are mostly fine. The real problems are in the eyebrow and the stats.

**What works**
- The h1 at 56px with 1.05 leading and -0.02em tracking is right for display type.
- The lead is 20px at 1.5 and the body is 16px at 1.5. The two sizes have clear roles.
- The color is a warm near-black, and the five sizes are a sensible count.

**What's wrong**
1. **The stats have no labels.** This is the biggest problem. "1,284 / 97 / 12,060" tells nobody anything. Nobody can tell they are drills, streak days and strokes scored. Big bare numbers in a card read as decoration, so the numbers need captions.
2. **The stat figures are proportional.** Stacked and right-aligned, "97" and "12,060" won't line up digit for digit. Use `tabular-nums`.
3. **The eyebrow is 11px, uppercase, with `letter-spacing: 0`.** That fails twice. Caps need tracking of about 0.05–0.1em, and 11px is below the 12px floor.
4. **The body paragraph runs about 80+ characters per line** at 16px in a 640px box. That's a little long. Cap the paragraph, not the wrapper.
5. **The h1 can leave a stranded last word** when it wraps. It's a short heading, so `text-wrap: balance` fixes it for free.

**Fixes (changed rules only)**
```css
.eyebrow { font-size: 0.75rem; letter-spacing: 0.08em; }
h1       { text-wrap: balance; }
.body    { max-width: 62ch; text-wrap: pretty; }

.stat       { font-size: 2rem; line-height: 1.1; font-weight: 700;
              font-variant-numeric: tabular-nums; }
.stat-label { display: block; font-size: 0.875rem; line-height: 1.3;
              font-weight: 400; color: #6b5d3f; margin-top: 2px; }
.stat + .stat { margin-top: 16px; }
```
```html
<div class="stat">1,284 <span class="stat-label">drills completed</span></div>
<div class="stat">97 <span class="stat-label">day streak</span></div>
<div class="stat">12,060 <span class="stat-label">strokes scored</span></div>
```

I wrote the label wording from your description, so change it to match your product copy. Because the label is `display: block`, it sits under each number. I left the h1 spacing and the lead alone.
