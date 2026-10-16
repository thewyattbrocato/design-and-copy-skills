**What works:** The h1 is well set: 56px with 1.05 leading and -0.02em tracking suits a display headline, and it's the right size to dominate. The lead and body sizes (20px and 16px at 1.5) are comfortable, and 640px caps the measure at about 65–75 characters. Leave all of that alone.

**What's actually wrong**

1. **The eyebrow is tiny, capitalised and untracked.** `11px` with `text-transform: uppercase` and `letter-spacing: 0` is the weakest line in the section. Caps need tracking, and 12px is the floor. Fix: `font-size: 0.75rem; letter-spacing: 0.08em;`. The `#6b5d3f` colour is fine on a light ground.

2. **The stats are proportional figures in a stacked column.** 1,284, 97 and 12,060 are right-aligned, but without `tabular-nums` the digits have different widths, so the column won't line up. Add `font-variant-numeric: tabular-nums;` to `.stat`.

3. **The stats have no labels in the markup.** Three bare numbers don't tell anyone which is drills, streak days or strokes scored. This is a content problem more than a typographic one, and it's the most important fix. Give each stat a small label, at least 12px and in sentence case, set one step below the number. For example:
   ```html
   <div class="stat"><span class="num">1,284</span><span class="label">drills</span></div>
   ```
   Also drop the numbers from 32px to about 28px (1.75rem). In a narrow card, 32px bold competes with the 56px h1 for no gain, and 12,060 may crowd the card at that size.

4. **The type is in px, not rem.** Everything is in fixed px, so browser font-size preferences are ignored. Convert: 0.75rem, 3.5rem, 1.25rem, 1rem, 1.75rem. This changes nothing visually at default settings.

5. **The h1 will break badly on narrow screens.** 56px has no fallback, and "Beautiful handwriting in ten minutes a day" will wrap to 5–6 lines on a phone. Use `font-size: clamp(2.25rem, 8vw, 3.5rem);` and add `text-wrap: balance;`. Add `text-wrap: pretty;` to `.body`.

6. **The spacing around the h1 is slightly off.** The gap above is 8px and below is 16px, the reverse of the usual 2:1 above-to-below. That's acceptable for an eyebrow tied to its heading, so I'd leave it. The 16px gap between the lead and the body is fine too.

**Not worth changing:** the weight (700 at 56px is a bit heavy, but 600 is a taste call, not a flaw), the face (`system-ui` is a choice, not a typesetting error), and the lead/body size ratio.

**Fix summary**
```css
.eyebrow { font-size: 0.75rem; letter-spacing: 0.08em; }
h1       { font-size: clamp(2.25rem, 8vw, 3.5rem); text-wrap: balance; }
.body    { text-wrap: pretty; }
.stat    { font-size: 1.75rem; font-variant-numeric: tabular-nums; }
.stat .label { font-size: 0.75rem; font-weight: 400; }
```

I assumed the section is on a light background and viewed on screen. I haven't checked the stats card's own width or background, so the 28px size is a guess for that card.
