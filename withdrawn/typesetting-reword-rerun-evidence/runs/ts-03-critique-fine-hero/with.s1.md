Most of this is already well set. The lead and body sizes, the 1.5 leading, the tight leading and tracking on the 56px headline, and the text colors all hold up. Five things fail, and the first two matter most.

**1. The eyebrow breaks two rules at once.**
- At 11px it's under the 12px floor.
- Uppercase text with `letter-spacing: 0` looks cramped and reads slowly.
- Fix: `font-size: 0.8125rem; letter-spacing: 0.08em;`

**2. The stats use proportional figures.**
- You stack them and right-align them, so the digits won't line up in a column. The `1` in `1,284` and the `1` in `12,060` have different widths.
- Fix: `font-variant-numeric: tabular-nums;`

**3. The stats have no labels.**
- "1,284 / 97 / 12,060" means nothing on its own. Readers can't tell drills from streak days from strokes.
- Add a small label under each number, in sentence case at 0.8125rem, in a dimmer color (a lighter value, not opacity). Use the labels you gave me: drills, streak days, strokes scored.
- Put the number and its label in one element. Otherwise the number can wrap away from its label.

**4. The body text line is too long.**
- At 16px in a 640px container it runs about 80 characters. The target is 65 or fewer.
- Fix: cap the paragraph with `max-width: 65ch`, rather than narrowing the whole `.hero`.
- If the card sits beside the text and takes space from this column, this may already be solved. Check it once the layout is real.

**5. The headline can wrap badly.**
- At 640px it will probably break onto three lines, and the last line could be a single word.
- Fix: add `text-wrap: balance`. Optionally move the line height to 1.1, since 1.05 is at the tight limit for three lines containing `g` and `y`.

```css
.eyebrow { font-size: 0.8125rem; letter-spacing: 0.08em; /* rest unchanged */ }
h1       { text-wrap: balance; line-height: 1.1; /* rest unchanged */ }
.body    { max-width: 65ch; text-wrap: pretty; /* rest unchanged */ }
.stat    { font-variant-numeric: tabular-nums; font-size: 2rem; font-weight: 700; line-height: 1.1; }
.stat small { display: block; font-size: 0.8125rem; font-weight: 400; color: #6b5d3f; }
```

```html
<div class="stat">1,284<small>Drills</small></div>
```

I'd leave everything else alone. I'd also stay with `system-ui` for now, since choosing a typeface is a separate question.
