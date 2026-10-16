Add this below your existing rules. The desktop styles stay as they are.

```css
h1 {
  font-size: clamp(2.25rem, 9vw, 4.5rem); /* 36px on phones, 72px on desktop */
  text-wrap: balance;
}

@media (max-width: 600px) {
  h1 { line-height: 1.1; letter-spacing: -0.02em; }
}
```

- **Size:** At 72px, a 350px-wide phone fits only 5 to 8 characters per line. That is why you get one or two words per line. The `clamp()` caps at 4.5rem, which is 72px. The cap is reached at about 800px viewport width, so desktop is unchanged. Phones drop to about half size, with a 36px floor.
- **Line height and tracking:** On phones the headline now wraps to about three lines. 1.02 is too tight for that, so it goes to 1.1. The tracking is also eased slightly. Both changes apply under 600px only.
- **Balance:** `text-wrap: balance` evens out the line lengths. It also stops a single word from sitting alone on the last line.

If 36px feels too big or too small on your phone, change the `2.25rem` floor. The `9vw` value controls how fast the size grows between phone and desktop widths.
