Most of this is sound. The scale from 56px to 20px to 16px is clear, and the line lengths and line-heights are fine. Four things are actually wrong, listed from most to least important.

**1. The stats have no labels.**
Three bare numbers (1,284 / 97 / 12,060) don't tell the reader anything. Nobody can tell which one is drills, which is streak days and which is strokes scored. Fixing the type won't help until each number has a label. Right-aligning also suggests the numbers can be compared by width, but they're different units, so it only adds visual noise. Put a small label under or beside each number. Add `tabular-nums` so digits line up if the values change.

```html
<dl class="stats">
  <div class="stat"><dd>1,284</dd><dt>drills completed</dt></div>
  <div class="stat"><dd>97</dd><dt>day streak</dt></div>
  <div class="stat"><dd>12,060</dd><dt>strokes scored</dt></div>
</dl>
```
```css
.stat dd { margin: 0; font-size: 32px; font-weight: 700; font-variant-numeric: tabular-nums; line-height: 1.1; }
.stat dt { font-size: 13px; color: #6b5d3f; }
.stats { text-align: left; }
```

**2. The eyebrow has `letter-spacing: 0`.**
Small uppercase text with no tracking looks cramped and is harder to read. It's also only 11px. Use about 12–13px with `letter-spacing: 0.08em`.

**3. The h1 is a fixed 56px.**
In a 640px column it will wrap to about three lines even on desktop. On a phone, 56px will break mid-phrase or overflow. Use a fluid size and balance the wrapping:
```css
h1 { font-size: clamp(36px, 7vw, 56px); text-wrap: balance; }
```

**4. `system-ui` is a weak choice for this product.**
This is a judgment call, not a bug. A handwriting app that sets its headline in the same font as the OS settings screen misses an easy chance to show its character. A calligraphic or high-contrast serif for the h1 only (keep the sans for body text) would suit the product. If you don't have a brand face yet, this can wait.

I'd leave everything else alone. Changing the lead and body colors or margins would only be busywork.
