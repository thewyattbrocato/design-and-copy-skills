The type mostly holds up. The scale, the h1 tracking and leading, and the lead-to-body step are all fine, so I'd leave them alone. Four things do fail.

**1. Eyebrow: 11px, all caps, `letter-spacing: 0`.**
This is the worst offender. Untracked caps at 11px look cramped and sit below the 12px floor.
```css
.eyebrow { font-size: 0.75rem; letter-spacing: 0.08em; }
```

**2. Stats: three bare numbers with no labels.**
"1,284 / 97 / 12,060" means nothing without "drills", "streak days" and "strokes scored". That's a content failure, not a typographic one. The figures are also proportional, so in a right-aligned stack the digits won't line up.
```html
<dl class="stats">
  <div class="stat"><dd>1,284</dd><dt>drills</dt></div>
  <div class="stat"><dd>97</dd><dt>streak days</dt></div>
  <div class="stat"><dd>12,060</dd><dt>strokes scored</dt></div>
</dl>
```
```css
.stats { text-align: right; margin: 0; }
.stat { margin: 0 0 16px; }
.stat dd { margin: 0; font-size: 2rem; line-height: 1.1; font-weight: 700;
           font-variant-numeric: tabular-nums lining-nums; }
.stat dt { font-size: 0.8125rem; color: #6b5d3f; }
```
I put the `dd` before the `dt` in the markup so the number reads first. Strictly, `dt` should come first in a `dl`. If that bothers you, use plain `div`/`span` and keep the same CSS.

**3. h1 is a fixed 56px.**
In a 640px column it already wraps to about three lines. On a phone it will run to four or five lines with ragged breaks.
```css
h1 { font-size: clamp(2.25rem, 8vw, 3.5rem); text-wrap: balance; }
```
The 1.05 leading is correct for display size. Keep it.

**4. `.body` runs about 75–80 characters per line at 16px in 640px.**
That's the top edge of comfortable, and the lead above it is shorter, so the two blocks don't match. Cap the text element, not the section.
```css
.body { max-width: 65ch; }
```
Add `text-wrap: pretty` if you like.

**Optional:** 700 weight at 56px is heavy. Trying 600 is a matter of taste, not a fault.

I assumed a light background. `#6b5d3f` is fine on white or cream, but check it if the hero sits on a tinted ground.
