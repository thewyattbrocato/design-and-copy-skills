Add this after your existing rules. Nothing changes above 600px, so desktop stays as it is.

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

**Why it was five lines:** 72px on a ~350px-wide screen leaves room for about 8 characters per line. At 36–48px the headline should fit in about three lines. The line height goes from 1.02 to 1.08 because multi-line display text with a heavy weight looks cramped at 1.02. The tracking is eased slightly because tight tracking at smaller sizes hurts legibility. `text-wrap: balance` evens out the line lengths so you don't get a one-word last line. It also applies on desktop, where it only changes the break points if the headline wraps there.

I haven't checked this in a browser. If you want the headline bigger or smaller on phones, change the `10vw` value.
