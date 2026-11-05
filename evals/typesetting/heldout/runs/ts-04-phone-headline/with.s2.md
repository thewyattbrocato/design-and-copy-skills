Add this media query after your existing rules. Desktop is untouched.

```css
h1 { text-wrap: balance; }

@media (max-width: 600px) {
  h1 {
    font-size: clamp(2.25rem, 10vw, 3rem); /* 36–48px */
    line-height: 1.08;
    letter-spacing: -0.02em;
    font-weight: 700;
  }
}
```

**Why it was five lines:** 72px on a ~350px-wide phone fits about 8 characters per line. At 36–48px you get roughly 14–18 characters, so the headline should wrap to about three balanced lines.

- **Size:** `clamp()` scales the headline with the screen width and stops it from getting too small or too large.
- **Line height and tracking:** these are slightly looser than on desktop. Tight display settings that work at 72px feel cramped at phone sizes.
- **Weight:** 700 instead of 800 keeps the headline from looking heavy at the smaller size. Delete that line if you want to keep 800.
- **`text-wrap: balance`:** this evens out the line lengths on every screen. It can shift where the line breaks on desktop. If the desktop look must be exactly the same, move that declaration inside the media query.

I haven't rendered this in a browser, so check it on your phone.
