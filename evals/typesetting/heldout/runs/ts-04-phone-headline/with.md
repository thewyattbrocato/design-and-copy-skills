Add this to the end of your CSS. The media query means nothing changes above 600px, so desktop stays as it is.

```css
@media (max-width: 600px) {
  h1 {
    font-size: clamp(32px, 9.5vw, 44px);
    line-height: 1.1;
    letter-spacing: -0.02em;
    text-wrap: balance;
  }
}
```

**Why it was breaking:** at 72px, a 375px phone with 20px padding leaves about 335px of text width. That fits only 7–8 characters per line, so every word ended up on its own line.

**What each change does:**
- **`font-size: clamp(32px, 9.5vw, 44px)`** scales the headline with the screen width. It's about 36px on a 375px phone, which gives roughly 3 lines. The 32px floor and 44px ceiling keep it sensible on very small and very large phones.
- **`line-height: 1.1`** is a little looser than your desktop 1.02. Tight leading looks fine on one or two big lines, but it feels cramped once the headline wraps to three.
- **`letter-spacing: -0.02em`** eases the tight tracking slightly, since smaller type needs less tightening.
- **`text-wrap: balance`** evens out the line lengths so you don't get a short orphan line like "weekend". Browsers that don't support it ignore it and wrap normally.

I haven't tested this on a device. If 3 lines still feels too big, lower the `9.5vw` to about `8.5vw`.
