I found one real problem and a few smaller ones.

**Real bug: the card is wider than 340px.**
- `.ticket` has `width: 340px` plus 20px padding and a 1px border, and no `box-sizing`. It renders at 382px.
- That overflows a 360px phone viewport and makes the button's right edge sit differently than you'd expect.
- Fix with `box-sizing: border-box` and `max-width: 100%`.

**Spacing tweaks**
- **`.meta` margins:** the rhythm is 16 above the rule, 16 below it, then 24 to the button. The 24 is defensible because it separates the action from the details, but the rule's padding and the margin are doing the same job in two places. I moved the spacing onto the margin and padding so the values read as 16 / 16 / 20.
- **`.meta` wrapping:** the three items have no wrap fallback. "1 adult / 2 children / Seat 12B" or a longer translation would overflow. I added `flex-wrap: wrap` with a `row-gap` so wrapped rows don't touch.
- **Gap between items:** I raised it from 12px to 16px so "1 adult" and "1 child" don't read as one run of text.

**Not spacing, but it affects how the button looks**
- Buttons don't inherit `font-family`, so the button falls back to the browser default instead of system-ui. I added `font-family: inherit`.

```css
.ticket { box-sizing: border-box; width: 340px; max-width: 100%; padding: 20px; border: 1px solid #d5d9de; border-radius: 12px; font: 15px/1.45 system-ui; }
.route { margin: 0; font-size: 18px; font-weight: 600; }
.time { margin: 4px 0 0; color: #4a5560; }
.meta { display: flex; flex-wrap: wrap; gap: 4px 16px; margin: 16px 0 20px; padding-top: 16px; border-top: 1px solid #e6e9ed; font-size: 14px; }
.ticket button { width: 100%; height: 44px; border: 0; border-radius: 8px; background: #0b5cad; color: #fff; font: inherit; font-size: 16px; }
```

I left these alone because they're fine:
- The 4px between route and time.
- The 44px button height, which is a good tap target.
- The 20px card padding.
- The 8px button radius nested inside the 12px card radius.

I haven't rendered this, so check it once at 320–360px wide before shipping.
