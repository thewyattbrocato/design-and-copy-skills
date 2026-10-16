Add this after your existing rules. It only applies at 600px and below, so desktop is unchanged.

```css
@media (max-width: 600px) {
  h1 {
    font-size: clamp(2.25rem, 9.5vw, 4.5rem); /* 36px floor, 72px cap */
    line-height: 1.08;
    margin-bottom: 16px;
    text-wrap: balance;
  }
}
```

- **Size:** on a typical 375px phone the headline is 36px, half its desktop size. It should wrap to about three even lines instead of five ragged ones. `4.5rem` equals your 72px, so the clamp never exceeds the desktop size.
- **Line height:** `1.08` is slightly looser than the desktop `1.02`. The headline now wraps to several lines, and the tight desktop value starts to crowd them at the smaller size.
- **Wrapping:** `text-wrap: balance` is inside the media query so desktop line breaks stay as they are.

I haven't run this in a browser, so check it on your phone. If a very narrow phone (320px) still breaks awkwardly, lower the `2.25rem` floor to `2rem`.
