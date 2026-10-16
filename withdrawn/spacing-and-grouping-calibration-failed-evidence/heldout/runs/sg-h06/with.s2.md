The spacing is nearly done. I'd change one thing.

**What already works**
- **Grouping:** The route and time sit 4px apart as one header. The meta row and the button are separate groups with larger gaps (16px, then 24px), so the card reads in three clear tiers.
- **Rule:** The divider has 16px on each side, which is balanced.
- **Button:** It's 44px tall, which is a good touch target, and it's full width.
- **Gaps:** Every gap is a 4px-scale step (4, 12, 16, 24).

**What I'd change**
- **Padding:** The `20px` card padding is the only off-scale value. It's also bigger than the 16px gaps inside the card, so the border looks looser than the content. Snapping it to `16px` tightens the card and lines the outer edge up with the internal rhythm.

```css
.ticket { width: 340px; padding: 16px; border: 1px solid #d5d9de; border-radius: 12px; font: 15px/1.45 system-ui; }
```

I left the rest alone. The `.meta` margins (`16px 0 24px`) put the last bit of space on the child, while the parent could own it. That only matters if you add more children, so it isn't worth changing for a card this small.

I couldn't see the card rendered, so check that 16px doesn't feel cramped around the 8px-radius button. If it does, go to `24px` instead of keeping `20px`.
