The main problem is that the page uses six typefaces across three styles (sans, serif, and monospace), so nothing looks like it belongs to the same system. Each rule looks reasonable alone, but together they make the page feel busy:

- **Six font families for a small site.** Open Sans, Playfair Display, Montserrat, Lora, Poppins, and Courier New all compete. Most sites need one or two.
- **Headings alternate styles.** `h1` is a high-contrast serif, `h2` is a sans, and `h3` is a serif again. Scanning a page of appointment info, the hierarchy jumps back and forth instead of reading as one system.
- **Montserrat and Poppins are both wide geometric sans fonts.** They're close enough to look like a near-miss, not a deliberate choice. Poppins on nav and buttons also differs from the Open Sans body text.
- **Playfair Display is a display serif.** Its thin hairlines and sharp contrast are meant for large headings. Older eyes often struggle with it, especially at smaller sizes or on lower-resolution screens.
- **Courier New for phone numbers is the biggest issue for this audience.** It's a typewriter face with thin strokes and uneven digit widths. Phone numbers are the most important text on a clinic site, and this makes them the hardest to read and the most out of place.
- **Possible missing font loading.** The CSS names Google Fonts but doesn't load them. If the `<link>` or `@import` is missing from the HTML, browsers fall back to system defaults, which vary by device and would explain why it looks inconsistent. Check the page head and the Network tab in DevTools for those font files.

For a clinic with older patients, I'd suggest:

```css
body, h1, h2, h3, .btn, nav a, .doctor-name {
  font-family: 'Open Sans', sans-serif;
}
body { font-size: 18px; line-height: 1.6; }   /* larger base text */
h1, h2, h3 { font-weight: 700; }
.phone-number {
  font-weight: 700;
  font-variant-numeric: tabular-nums;   /* even digit widths */
  letter-spacing: 0.02em;
}
```

If you want a bit of personality in headings, keep a single serif (Lora is the friendliest choice here) for `h1` and `h2` only, and drop Playfair, Montserrat, and Poppins. Then check that the Open Sans and Lora files are actually loaded.

I haven't tested this on the live site. If you can share the HTML head or a screenshot, I can confirm whether the fonts are loading and point out any other layout issues.
