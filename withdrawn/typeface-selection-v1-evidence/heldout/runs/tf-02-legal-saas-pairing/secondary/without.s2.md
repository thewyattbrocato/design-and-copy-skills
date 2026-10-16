I'd go with **Georgia for headings and the platform's native sans for body text.** Nothing ships with the site, so it doesn't need a license review.

No font is identical on Mac, Windows, iOS, and Android, so the goal is a stack where each platform gets a good match:

```css
/* Marketing headings: traditional serif, reads as "established firm" */
--font-display: Georgia, "Palatino Linotype", Palatino, "Times New Roman", serif;

/* Product UI and marketing body: native sans, so every platform looks like itself */
--font-body: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
```

- **Georgia** is on macOS, Windows, and iOS. Android doesn't ship it, so it falls back to the device serif, which is close enough in tone. Palatino is the second choice on Windows and Mac if you want a lighter feel.
- **system-ui** resolves to SF on Apple devices, Segoe UI on Windows, and Roboto on Android. That's the most honest "body font that's already installed," and users already read it all day.

Things to watch:

- **Georgia's numerals are old-style** (the 3s, 4s, 5s, and 7s drop below the baseline). That looks charming in a headline but wrong next to dollar amounts. Keep Georgia for headings only, and set invoice and balance figures in the sans with `font-variant-numeric: tabular-nums` so columns line up.
- **Don't use Charter, Iowan, Avenir, or Optima** even though they look good on Mac. They're missing on Windows, and the fallback will look like a mistake.
- **Test on a real Android phone.** That's where the fallback is most different from what you'll see on a Mac.

If you want the product UI to feel more like a legal document, you can also use Georgia for the invoice header and client names. Keep the body and table text in the sans.
