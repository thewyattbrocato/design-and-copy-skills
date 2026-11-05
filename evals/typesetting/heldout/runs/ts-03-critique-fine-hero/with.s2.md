The hierarchy is sound. The sizes (11, 16, 20, 32 and 56px) each have a role, and the lead and body leading are right. The 1.05 leading on the h1 and its -0.02em tracking are correct for display size. There are four real problems.

**1. The eyebrow is tiny, capitalised and untracked.**
It's 11px uppercase with `letter-spacing: 0`, so the capitals look cramped and the size is below the 12px floor.
```css
.eyebrow { font-size: 0.75rem; letter-spacing: 0.08em; }
```

**2. The stats are bare numbers.**
Nothing in the markup says what 1,284, 97 and 12,060 are. Without the labels (drills, streak days, strokes scored) they're decoration. The figures also use proportional digits, so in a stacked right-aligned column the digits won't line up.
```html
<div class="stat"><span class="stat-label">Drills</span><span class="stat-num">1,284</span></div>
<div class="stat"><span class="stat-label">Streak days</span><span class="stat-num">97</span></div>
<div class="stat"><span class="stat-label">Strokes scored</span><span class="stat-num">12,060</span></div>
```
```css
.stat { display: flex; justify-content: space-between; align-items: baseline; }
.stat-num { font-size: 2rem; font-weight: 700; font-variant-numeric: tabular-nums; }
.stat-label { font-size: 0.875rem; }
```
The label and number sit on one baseline. The label should be a small, dimmer shade of your text colour, not an opacity change. Drop the `text-align: right` on `.stats` once the labels are in.

**3. The h1 is fixed at 56px.**
On a phone, "Beautiful handwriting in ten minutes a day" will wrap to four or five lines and some words may break badly. Use a fluid size with a floor, and balance the wrap.
```css
h1 { font-size: clamp(2.25rem, 7vw, 3.5rem); text-wrap: balance; }
```

**4. The body measure is a little long.**
At 16px inside a 640px container, lines run about 80 characters. Cap the paragraph itself, not the wrapper.
```css
.body { max-width: 65ch; text-wrap: pretty; }
```
This matters less if the text column is already narrowed by the stats card beside it.

I left everything else alone, including the lead and body sizes, the margins and the colours.
