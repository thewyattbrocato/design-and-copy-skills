Most of this is sound. The scale (56/20/16) is clear, the h1 tracking and line-height are reasonable, and the body measure and leading are fine. These are the things that are actually wrong, most important first.

**1. The stats have no labels.**
Three bare numbers (1,284 / 97 / 12,060) don't tell anyone what they're looking at. A visitor can't tell drills from streak days from strokes. Right-aligning them in a stack also makes them look like a column of figures to add up. Each one needs a small label beneath or beside it. Also add `font-variant-numeric: tabular-nums` so the digits line up in the right-aligned column.

```html
<div class="stat"><span class="num">1,284</span><span class="label">drills completed</span></div>
```
```css
.stat { display: flex; flex-direction: column; align-items: flex-end; }
.num { font-size: 32px; font-weight: 700; font-variant-numeric: tabular-nums; line-height: 1.1; }
.label { font-size: 13px; color: #6b5d3f; }
```

**2. The eyebrow is uppercase with `letter-spacing: 0`.**
Small all-caps text needs positive tracking or the letters crowd together. At 11px it's also at the edge of comfortable reading. Use:
```css
.eyebrow { font-size: 12px; letter-spacing: 0.08em; }
```
Go to 13px if it sits near other small text.

**3. The h1 is a fixed 56px.**
In a 640px column it will wrap to about three lines even on desktop, and on a phone it will be far too big. Use a fluid size and balance the wrapping so you don't get a one-word last line:
```css
h1 { font-size: clamp(36px, 7vw, 56px); text-wrap: balance; }
```

**Optional, not a bug:** `system-ui` is perfectly legible, but it gives a handwriting app no personality. If you want one change that adds character, set the h1 only in a calligraphic or high-contrast serif and leave everything else as is. Skip this if the brand is meant to be plain.

I'd leave the rest alone. The lead and body sizes, colors and spacing don't need changes.
