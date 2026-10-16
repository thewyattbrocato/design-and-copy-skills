Add a media query that scales the headline down on small screens. Desktop stays unchanged because the query only applies below the breakpoint.

```css
.wrap { max-width: 1100px; margin: 0 auto; padding: 0 20px; font-family: system-ui, sans-serif; }
h1 { font-size: 72px; line-height: 1.02; letter-spacing: -0.03em; font-weight: 800; margin: 0 0 20px; }
.lead { font-size: 18px; line-height: 1.5; margin: 0; }

@media (max-width: 600px) {
  h1 {
    font-size: clamp(32px, 10vw, 44px);
    line-height: 1.08;
    letter-spacing: -0.02em;
    overflow-wrap: break-word;
    text-wrap: balance;
  }
}
```

What this does:

- **`font-size: clamp(32px, 10vw, 44px)`** is the main fix. At 72px, a phone about 375px wide fits only one or two words per line. At that width this gives roughly 37px, which should wrap to 3 lines, and it scales smoothly across phone sizes.
- **`line-height: 1.08`** gives slightly more room than 1.02. Tight leading looks fine at 72px but cramped at small sizes.
- **`letter-spacing: -0.02em`** eases the tight tracking, which reads worse when the type is small.
- **`text-wrap: balance`** evens out the line lengths so you don't get a single orphaned word on the last line. Browsers that don't support it ignore it.
- **`overflow-wrap: break-word`** keeps a long word from overflowing the screen.

I haven't rendered this, so check it on your phone. If you want the headline bigger or smaller, change the `10vw` value. If tablets in portrait still look too large, raise the breakpoint to 768px.
