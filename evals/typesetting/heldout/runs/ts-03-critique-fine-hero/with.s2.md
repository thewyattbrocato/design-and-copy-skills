The setup is mostly sound. The lead and body sizes and leading are fine, and the scale is a reasonable five sizes. A few things are actually wrong.

**1. The stats have no labels (the biggest problem).**
"1,284 / 97 / 12,060" tells the reader nothing. Drills, streak days and strokes scored need a label each, and the card is the one place where the numbers are the content. The numbers also need `tabular-nums`, because they're stacked and right-aligned and proportional figures will make the right edges and digit widths wobble.

**2. The eyebrow fails twice.**
It's 11px, under the 12px floor, and it's all caps with `letter-spacing: 0`. Small caps text needs tracking to be readable.

**3. The h1 will wrap to about three lines at 56px in 640px.**
A fixed 56px on a phone will be huge. It needs `clamp()` and `text-wrap: balance` so it doesn't leave a stranded last word. 1.05 leading is tight for a multi-line heading, so I'd open it slightly to 1.1.

**4. The body paragraph runs about 80+ characters per line.**
That's over the comfortable range. Cap the paragraph, not the hero.

Fixes:

```css
.eyebrow { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.08em; font-weight: 600; color: #6b5d3f; }
h1 { font-size: clamp(2.25rem, 7vw, 3.5rem); line-height: 1.1; letter-spacing: -0.02em; font-weight: 700; margin: 8px 0 16px; text-wrap: balance; }
.body { font-size: 1rem; line-height: 1.5; margin: 0 0 24px; max-width: 60ch; text-wrap: pretty; }
.stats { text-align: right; }
.stat { font-size: 2rem; line-height: 1.1; font-weight: 700; font-variant-numeric: tabular-nums; }
.stat-label { display: block; font-size: 0.875rem; line-height: 1.4; font-weight: 400; color: #5c5646; }
```

```html
<div class="stats">
  <div class="stat">1,284 <span class="stat-label">drills completed</span></div>
  <div class="stat">97 <span class="stat-label">day streak</span></div>
  <div class="stat">12,060 <span class="stat-label">strokes scored</span></div>
</div>
```

The label wording is my guess from your description, so adjust it to match your copy.

I left the lead paragraph, the body size, the h1 tracking and the colors alone. They hold up.
