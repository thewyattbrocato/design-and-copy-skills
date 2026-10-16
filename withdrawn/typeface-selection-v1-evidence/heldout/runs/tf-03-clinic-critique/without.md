The mess comes from using **six different font families** on one site. Each element type has its own typeface, so the eye gets no consistent rhythm. Most of the families are also decorative or geometric designs that compete with each other.

**What's wrong**

1. **Too many typefaces.** Open Sans, Playfair Display, Montserrat, Lora, Poppins, and Courier New. A good rule is two, or three at most. Here every level of the hierarchy looks like it came from a different site.
2. **Three sans-serifs that nearly match.** Open Sans, Montserrat, and Poppins are all sans-serifs but differ in width, letter shape, and weight. They are close enough to look like a mistake and different enough to clash. Most visitors can't name the problem, but they feel it as "messy".
3. **Serifs mixed in without a system.** Playfair Display (high-contrast, dramatic) is used for h1, and Lora (a softer, bookish serif) for h3 and doctor names. That gives two unrelated serifs, with a sans-serif h2 sitting between them. The heading levels jump serif → sans → serif.
4. **Courier New for phone numbers.** This is probably the most jarring choice. It's a typewriter font that looks out of place next to the others. It also renders thin and light, which is hard to read for older patients, and the phone number is one of the most important things on the page.
5. **Buttons and nav in a different font from the body.** Poppins on buttons and nav links means the main interactive elements don't match the text around them.

**Why it matters for your patients**

Older readers are more sensitive to thin strokes, tight letterforms, and inconsistent text. Playfair Display's hairline strokes and Courier New's thin strokes are the worst for this. Appointment details need to be scanned quickly and trusted, and a mix of fonts makes the page feel less credible.

**A simpler setup**

Use one sans-serif for everything, with an optional serif for headings only:

```css
body, h2, h3, .btn, nav a, .doctor-name, .phone-number {
  font-family: 'Open Sans', sans-serif;
}
h1 {
  font-family: 'Lora', serif; /* optional: one serif for the main title only */
}

body { font-size: 18px; line-height: 1.6; }
h1, h2, h3 { font-weight: 700; line-height: 1.3; }
.btn, nav a { font-weight: 600; }
.phone-number { font-weight: 600; font-variant-numeric: tabular-nums; }
```

Things to note about this version:

- **Open Sans is already your body font**, so you only need to remove the others, and you load fewer font files, so pages load faster.
- **Hierarchy comes from size and weight**, not from switching typefaces.
- **18px body text or larger** helps older readers a lot. Check that your current size isn't smaller.
- **The phone number matches the rest of the text**, but is bold enough to stand out. You could also make it a tap-to-call link on mobile.

If you want a warmer feel, the Lora h1 gives it some character without adding clutter. If you want the simplest option, drop it and use Open Sans throughout.

I can only see the CSS you pasted, so I haven't checked font sizes, colors, or contrast. Those could also contribute to the messy look. If you share the rest of the stylesheet or a screenshot, I can check those too.
