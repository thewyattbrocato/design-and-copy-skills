Your site uses six font families, each with a different job. Nothing is wrong with any single font. The mix is what looks messy.

**What works**
- Open Sans for body text is a good choice. It's a humanist sans with open shapes and clear letterforms, and it reads well for older patients.

**What fails**
1. **Six families with no shared logic.** You have three sans fonts (Open Sans, Montserrat, Poppins), two serifs (Playfair Display, Lora) and a monospace. Montserrat and Poppins are both round geometric sans fonts, and they sit next to Open Sans, so the differences look like mistakes. Every heading level and the nav and buttons each have a different personality.
2. **Playfair Display for the h1.** Its thin hairline strokes are hard to read for older eyes, especially on lower-quality screens.
3. **Courier New for phone numbers.** Typewriter styling on your most important contact detail looks dated and thin. It's also unrelated to the rest of the page, and monospace is meant for code, not for clinic phone numbers.
4. **Two serifs (Playfair and Lora) for different roles.** h1 and h3/doctor names use serifs, but h2 switches to a sans. The reader gets sans, serif, sans, serif as they move down the page.
5. **Poppins on the nav and buttons.** Different letterforms for the actions people need most make the interface feel inconsistent with the content around it.

**Fix: use one family and build hierarchy with weight and size.**

```css
body {
  font-family: 'Open Sans', system-ui, -apple-system, 'Segoe UI', Roboto, Arial, sans-serif;
  font-size: 18px;
  line-height: 1.6;
}
h1, h2, h3, .doctor-name { font-family: inherit; font-weight: 700; line-height: 1.25; }
h2 { font-weight: 600; }
h3, .doctor-name { font-weight: 600; }
.btn, nav a { font-family: inherit; font-weight: 600; }
.phone-number { font-family: inherit; font-weight: 700; font-variant-numeric: tabular-nums; }
```

Load Open Sans at weights 400, 600 and 700, plus the italic if you use it. Without the 600 and 700 files, the browser fakes bold, which looks blurry.

**Optional:** if you want some warmth, keep a single serif (Lora) for the h1 and doctor names only. Drop Playfair, Montserrat, Poppins and Courier either way.

I assumed the fonts load from Google Fonts or a similar service, and that patients mostly use phones and tablets. I also didn't check your site's font sizes. 18px or larger body text matters as much as the font choice for this audience.
