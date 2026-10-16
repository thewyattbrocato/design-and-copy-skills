Add this media query below your existing rules. Nothing above 600px changes, so the desktop look stays as it is.

```css
h1 { text-wrap: balance; }

@media (max-width: 600px) {
  h1 {
    font-size: clamp(2.25rem, 10vw, 3rem); /* 36–48px */
    line-height: 1.08;
    letter-spacing: -0.02em;
  }
}
```

**Why it was five lines:** at 72px and weight 800, a 390px phone has about 350px of text width. That fits roughly 8 characters per line. The headline now runs about 40px on a typical phone, so it should take 3 lines instead of 5.

**What I changed:**
- **Size:** `clamp()` scales the headline with the screen width. It stays between 36px and 48px.
- **Line height and tracking:** I loosened both slightly from your desktop values. The -0.03em tracking is tuned for huge type, and it gets cramped at phone sizes.
- **Wrapping:** `text-wrap: balance` evens out the line lengths, so you don't get a last line with one word on it. It sits outside the media query, so it also applies on desktop. It only changes where lines break, and your 72px headline probably already fits on one or two lines there. If you want desktop untouched, move that rule inside the media query.

I left `.lead` at 18px, which reads fine on a phone.

I haven't viewed it on a device, so check it at about 360px and 390px wide. If it still feels big, lower the `10vw` to `9vw`.
