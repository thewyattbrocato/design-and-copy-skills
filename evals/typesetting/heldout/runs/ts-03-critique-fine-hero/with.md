The hero is mostly sound. The h1 is set well (tight leading is correct at that size), and the lead and body sizes and leading are fine. A few things do fail.

**What's wrong**

1. **Eyebrow is 11px, uppercase, with `letter-spacing: 0`.** That breaks two rules at once. It's under the 12px floor, and untracked caps look cramped and read slowly. Use 12px and 0.08em tracking.
2. **The body paragraph runs too long.** At 16px in a 640px container, lines come out around 85 characters, past the 75 ceiling. Cap the paragraph itself at `max-width: 65ch`, not the wrapper. The lead (about 65–70 characters at 20px) is fine.
3. **The stats are three bare numbers.** Nothing says that 1,284 is drills, 97 is streak days or 12,060 is strokes scored. That's the biggest problem in the section. Each number needs a small label.
4. **The figures use proportional digits.** Right-aligned numbers of different lengths (`1,284`, `97`, `12,060`) won't line up digit-for-digit in a stacked card. Add `tabular-nums`.
5. **Minor: the h1 can wrap badly.** It's about 42 characters at 56px, so it will break to two or three lines in a 640px container. `text-wrap: balance` avoids a one-word last line.

**Fixes**

```css
.eyebrow { font-size: 0.75rem; letter-spacing: 0.08em; /* rest unchanged */ }
h1 { text-wrap: balance; /* rest unchanged */ }
.body { max-width: 65ch; text-wrap: pretty; /* rest unchanged */ }
.stat { font-size: 2rem; font-weight: 700; font-variant-numeric: tabular-nums; line-height: 1.1; }
.stat-label { display: block; font-size: 0.75rem; font-weight: 400; color: #6b5d3f; line-height: 1.3; }
```

```html
<div class="stat">1,284<span class="stat-label">Drills</span></div>
<div class="stat">97<span class="stat-label">Day streak</span></div>
<div class="stat">12,060<span class="stat-label">Strokes scored</span></div>
```

The label wording is mine, taken from your description of the stats, so change it to match your product copy.

I'd leave everything else as it is.
