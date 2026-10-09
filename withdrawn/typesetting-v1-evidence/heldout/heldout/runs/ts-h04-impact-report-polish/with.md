Anchor: a calm printed annual report. Selectors and markup are kept, with one small addition: a wrapper pair so the two stats sit side by side.

```html
<div class="card">
  <div class="stats">
    <div class="stat">
      <div class="label">Meals served in 2025</div>
      <div class="big">184,300</div>
    </div>
    <div class="stat">
      <div class="label">Households helped</div>
      <div class="big">6,912</div>
    </div>
  </div>
  <p>Thanks to 412 volunteers and 38 partner farms, we served more meals this year than in any year since we opened in 2009. Most of the growth came from our new Saturday mobile pantry, which reached three rural counties for the first time. Next year we plan to add a second refrigerated truck so fresh produce can reach every route.</p>
</div>
<style>
  .card { width: 900px; max-width: 100%; margin: 0 auto; padding: 2.5rem; background: #fffdf8; color: #2b2b2b; font-family: Helvetica, Arial, sans-serif; box-sizing: border-box; }
  .stats { display: flex; gap: 3rem; margin-bottom: 2rem; padding-bottom: 1.5rem; border-bottom: 1px solid #e4dfd2; }
  .label { font-size: 0.8125rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #5f5f5f; }
  .big { font-size: 3rem; font-weight: 700; line-height: 1.1; margin-top: 0.25rem; color: #1f1f1f; font-variant-numeric: tabular-nums lining-nums; }
  p { max-width: 65ch; margin: 0; font-size: 1.0625rem; line-height: 1.6; color: #3d3d3d; }
</style>
```

What changed and why:
- **Body text:** it was 13px, pale gray `#999`, with a line height of 1.2, across a 900px card. It is now 17px (`1.0625rem`) in dark gray, with a line height of 1.6 and a 65-character line length. That is the biggest single fix for the amateur look.
- **Stats:** the numbers are now 48px, so they lead the card. They were 28px and barely stood out from the body. The labels sit close above their numbers, and the stats are separated from the paragraph by a rule and more space.
- **Labels:** they were 11px caps with no letter-spacing and pale `#888`. They are now 13px with 0.08em tracking and a darker gray (`#5f5f5f`) that is easier to read.
- **Numerals:** they use tabular lining figures, so they line up if you add more stats later.
- **Layout:** padding is larger, and `max-width: 100%` keeps the card from overflowing on narrow screens.

I kept your colors, font and cream background, and only darkened the grays for legibility.
