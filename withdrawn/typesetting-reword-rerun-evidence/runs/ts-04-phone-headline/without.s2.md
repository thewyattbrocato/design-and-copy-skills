Add this to the end of your CSS. It only applies at 600px wide and below, so desktop is unchanged:

```css
@media (max-width: 600px) {
  h1 {
    font-size: clamp(32px, 10vw, 44px);
    line-height: 1.08;
    text-wrap: balance;
  }
  .lead { font-size: 17px; }
}
```

- **Why it broke:** 72px type is about 290px wide for the word "weekend" alone. A phone's content area is only about 335px, so almost every word wraps onto its own line.
- **Font size:** `clamp(32px, 10vw, 44px)` scales with the screen. A 375px phone gets about 37px, which should put the headline on 2 or 3 lines. It never goes below 32px or above 44px.
- **Line height:** I raised it slightly to 1.08. Tight leading looks fine on a big single block but cramped across several short lines.
- **`text-wrap: balance`:** This evens out line lengths so you don't get a single orphaned word on the last line. Browsers that don't support it ignore it, and the headline still wraps normally.
- **Lead text:** The 17px size is optional. Delete that line if you want it to stay at 18px.

Make sure your `<head>` has `<meta name="viewport" content="width=device-width, initial-scale=1">`. Without it, phones render the page at desktop width and shrink it, and the media query won't fire.
