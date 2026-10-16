Add this media query and clamp the desktop size. The desktop look stays at 72px.

```css
h1 {
  font-size: clamp(2.25rem, 9vw, 72px);
  text-wrap: balance;
}
```

If you'd rather leave the original `h1` rule untouched, use this instead:

```css
@media (max-width: 600px) {
  h1 {
    font-size: clamp(2.25rem, 10vw, 3rem); /* 36–48px */
    line-height: 1.08;
    letter-spacing: -0.02em;
  }
}
```

- **Cause:** 72px at 800 weight is about 5 words wide on a 360–400px screen, so each line holds only one or two words. On a phone, a headline at about half to two-thirds of the desktop size reads well, and this one lands at roughly 36–40px.
- **Leading and tracking:** I raised line-height slightly on the mobile version because 1.02 is too tight once the headline wraps to 3–4 lines. I also eased the tracking.
- **Balanced wrapping:** `text-wrap: balance` evens out the line lengths so you don't get a single orphaned word on the last line.

I haven't tested this on a device. Check it at around 360px wide, where the headline should fall on about three lines.
