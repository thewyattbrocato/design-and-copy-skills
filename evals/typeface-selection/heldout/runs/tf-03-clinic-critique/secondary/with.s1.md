The problem is the font count, not any single font. The CSS uses **five families plus monospace**, and three of them are nearly the same face.

**What's wrong**

1. **Montserrat and Poppins are near-twins.** Both are wide geometric sans, so the h2 headings and the nav/buttons look almost alike but not quite. That near-match reads as inconsistency.
2. **Open Sans is a third sans** doing body text. Three sans faces with similar shapes make the page look unsettled.
3. **Playfair Display and Lora are two serifs.** Playfair has very thin hairlines at display sizes, and it sits beside Lora, which has a different contrast and x-height. Two serifs that differ slightly look like a mistake.
4. **Courier New for phone numbers is the worst choice for this audience.** It's thin, has a small x-height, and its strokes break up at small sizes. Phone numbers are the most important text on a clinic site, and older patients need to read them easily.
5. **Mixed weights and styles add to the mess.** Each family has its own weight behavior, so the bold in one heading doesn't match the bold elsewhere.

**Recommended fix: one family, with a single serif only if you want a brand voice**

Keep Open Sans, which is already the body font and is a good choice for older readers: open apertures, distinct letterforms, and a generous x-height.

```css
body,
h1, h2, h3,
.doctor-name,
.btn, nav a,
.phone-number {
  font-family: 'Open Sans', system-ui, -apple-system, 'Segoe UI', Arial, sans-serif;
}

h1, h2, h3 { font-weight: 600; }

.phone-number {
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  font-size: 1.25em;
}
```

If you want a bit of personality in headings, you can keep **Lora for h1 and h3 only**, and make everything else Open Sans. That gives two families total, and the serif has a clear role. Drop Playfair, Montserrat, Poppins, and Courier.

**Things to check on the live site**

- **Are the fonts actually loading?** The CSS names fonts but doesn't show the `@font-face` or Google Fonts link. If they're missing, visitors see the fallback, which may explain the mismatch.
- **Body text size.** For older patients, body text should be about 18px or larger, with noticeably more line spacing than default. That may matter more than the font choice.
- **Phone numbers as links.** Make them `tel:` links so they're tappable on phones.

I haven't seen the rendered site, so I can't confirm which face is visibly off. If you send a screenshot or the page URL, I can point to the specific lines that cause the problem.
