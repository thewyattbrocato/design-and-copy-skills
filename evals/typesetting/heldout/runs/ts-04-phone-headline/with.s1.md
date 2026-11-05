Replace the `h1` rule with this:

```css
h1 {
  font-size: clamp(2.25rem, 10vw, 4.5rem);
  line-height: 1.02;
  letter-spacing: -0.03em;
  font-weight: 800;
  margin: 0 0 20px;
  text-wrap: balance;
}
```

- **Cause:** the 72px headline was fixed, so on a ~350px-wide phone column only two or three short words fit per line.
- **Phones:** the size now scales with the viewport (`10vw`) and never drops below 36px (`2.25rem`). At 390px wide it's about 39px, so the headline should wrap to about three lines.
- **Desktop:** it reaches the full 72px (`4.5rem`) at a viewport width of 720px and stays there. Your desktop look is unchanged.
- **Line breaks:** `text-wrap: balance` evens out the line lengths, so you shouldn't get a last line with one orphaned word.

I haven't tested it in a browser, so check it on your phone. If three lines still feels heavy, lower the 36px floor (for example to `2rem`).
