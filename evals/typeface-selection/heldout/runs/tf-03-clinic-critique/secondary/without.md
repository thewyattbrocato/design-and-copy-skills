The CSS shows the main problem: the site uses **six typefaces across five style categories**, and they're all close to each other in style. Your patients are likely seeing that as visual noise.

**What's clashing**

- **Six families:** Open Sans, Playfair Display, Montserrat, Lora, Poppins, and Courier New.
- **Two geometric sans-serifs that look almost alike:** Montserrat (h2) and Poppins (buttons and nav). Their differences are too small to read as intentional, so they look like a mistake.
- **Serif and sans-serif alternate down the page:** h1 is serif, h2 is sans, h3 is serif. Each heading level switches style, which makes the hierarchy feel jumbled.
- **Nav and buttons don't match the body:** Poppins in the nav and buttons vs. Open Sans in the body text.
- **Courier New for phone numbers:** a typewriter-style monospace is the hardest face to read for many people, and it doesn't match anything else on the page. Phone numbers are some of the most important text for your patients.
- **Playfair Display for h1:** its thin hairline strokes are hard to read at smaller sizes and for older eyes.

For a clinic with mostly older patients and lots of appointment details, readability matters more than variety. Use one family for almost everything and get hierarchy from size and weight.

**Suggested fix**

```css
body,
h1, h2, h3,
.doctor-name,
.btn, nav a,
.phone-number {
  font-family: 'Open Sans', sans-serif;
}

h1, h2, h3 { font-weight: 700; }
.phone-number { font-weight: 600; font-variant-numeric: tabular-nums; }
```

If you want a bit of personality in the header, keep one serif for h1 only and drop the rest. Also check that Open Sans is actually loaded (a Google Fonts link or `@font-face`). If it isn't, each device falls back to its own system font, which would make the page look inconsistent across phones and computers even with clean CSS.

I only had the CSS, not the HTML or the rendered page, so I can't see font sizes, weights, or line spacing. Those matter a lot for older readers. If you share the stylesheet's sizes or a screenshot, I can check those too.
