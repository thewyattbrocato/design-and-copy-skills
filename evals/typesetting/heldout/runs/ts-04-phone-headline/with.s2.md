Add this media query. Nothing outside it changes, so the desktop look stays the same.

```css
@media (max-width: 600px) {
  h1 {
    font-size: clamp(2.25rem, 10vw, 3rem); /* 36–48px */
    line-height: 1.08;
    letter-spacing: -0.02em;
    text-wrap: balance;
  }
}
```

- **Size:** 72px on a phone about 375px wide leaves room for only one or two words per line. The headline now runs about 36–42px there. That's roughly half the desktop size, so it should wrap to about three lines.
- **Line height:** At 1.02 a headline that wraps to several lines gets cramped. 1.08 gives it a little room.
- **Letter-spacing:** I eased the tracking from -0.03em to -0.02em. Tight tracking at a smaller size makes the letters look squeezed.
- **`text-wrap: balance`:** This evens out the line lengths, so you don't get a last line with one orphaned word.

I left the `.lead` paragraph alone. At 18px with a 1.5 line height it already reads well on a phone.

I haven't rendered this on a device. If three lines still feels too tall, lower the `3rem` cap or the `10vw` value.
