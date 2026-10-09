The main problem is that the page uses six font families, and several of them do the same job. Most of the mess comes from that, not from any one font.

**What's wrong**

1. **Too many families.** Open Sans, Playfair Display, Montserrat, Lora, Poppins, and Courier New all appear. Each one adds a different x-height, stroke weight, and width, so the page looks busy even when each element looks fine alone.
2. **Two near-identical sans faces.** Montserrat (h2) and Poppins (buttons and nav) are both wide geometric sans. They differ slightly, which reads as a mistake rather than a deliberate contrast. Open Sans is a third sans for body text.
3. **Two serifs with no clear roles.** Playfair Display (h1) is a high-contrast display face with very thin hairlines, which are hard to read for older eyes at small sizes. Lora (h3, doctor names) is a text serif. Headings and names end up in different serif styles.
4. **Courier New for phone numbers.** Monospace is for code. It makes numbers look like a typewriter printout, and Courier's thin strokes are hard to read for older patients. It also isn't a web font, so it renders differently on Mac and Windows.
5. **Light weights for headings.** Playfair and Montserrat are heavy and wide at h2 size, which competes with the appointment details under them.

**Fix: one family, set by weight and size**

Open Sans is already the best choice here. It has a large x-height, open letterforms, and a full weight range, and it works well for older readers. Use it everywhere and drop the rest.

```css
body,
h1, h2, h3, .doctor-name,
.btn, nav a,
.phone-number {
  font-family: 'Open Sans', system-ui, -apple-system, 'Segoe UI', Arial, sans-serif;
}

h1, h2, h3, .doctor-name { font-weight: 700; }

.phone-number {
  font-weight: 700;
  font-size: 1.2em;
  font-variant-numeric: tabular-nums;
  white-space: nowrap;
}
```

- Headings keep their hierarchy through size and weight, not a different face.
- Phone numbers get tabular figures so they line up and are easy to scan, and `nowrap` keeps them from breaking across lines.
- The system fallbacks mean the page still looks consistent if the web font fails to load.

**Things I couldn't check**

- I only have the CSS, not the HTML or the font loading code. If you load these fonts from Google Fonts, removing the unused families also cuts six font requests down to one.
- I haven't checked Open Sans's current license terms. It's generally available under an open license, but confirm the terms for your use.

If the site needs a serif for long-form content like a "about us" page, Lora is the one to keep, and it should be the only serif on the site.
