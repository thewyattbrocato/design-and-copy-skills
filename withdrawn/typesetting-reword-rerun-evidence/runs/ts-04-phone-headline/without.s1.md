Add a media query that scales the headline down on narrow screens. Desktop stays untouched because the rule only applies below the breakpoint.

```css
.wrap { max-width: 1100px; margin: 0 auto; padding: 0 20px; font-family: system-ui, sans-serif; }
h1 { font-size: 72px; line-height: 1.02; letter-spacing: -0.03em; font-weight: 800; margin: 0 0 20px; }
.lead { font-size: 18px; line-height: 1.5; margin: 0; }

@media (max-width: 600px) {
  h1 {
    font-size: clamp(32px, 9.5vw, 44px);
    line-height: 1.1;
    letter-spacing: -0.02em;
    text-wrap: balance;
  }
}
```

**Why it was breaking:** 72px is fixed, and a phone is about 360–430px wide. After the 20px side padding, that leaves roughly 320–390px of text width, which fits only a word or two per line at that size.

**What each change does:**
- `font-size: clamp(32px, 9.5vw, 44px)` scales with the screen width. It's about 34px on a 360px phone and caps at 44px. The headline should come out at 3 lines instead of 5.
- `line-height: 1.1` loosens the leading slightly. At 1.02, tight lines look cramped at small sizes.
- `letter-spacing: -0.02em` eases the tracking. Very tight tracking hurts legibility on small screens.
- `text-wrap: balance` evens out the line lengths so you don't get a stray single word on the last line. Browsers that don't support it ignore it, so nothing breaks.

If it still feels too big or small on your phone, adjust the middle value (`9.5vw`). The 600px breakpoint leaves tablets and desktops on the original 72px. If you'd like the headline to scale down smoothly on tablets too, raise the breakpoint to about 900px and change the `clamp` max to a larger value, but that changes the in-between look.
