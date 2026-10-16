**Honest verdict: the fonts suit a kids' museum, but the way they're set up will make the most important information hard to read on a phone.**

**Problems, most serious first**

1. **The body text is too thin and too small.** `font-weight: 100` is Josefin Sans Thin, and it's set at 13px. On a phone, especially outdoors or in a car park, hairline strokes at that size are hard to read. Ticket prices and details will be the hardest things to read on the page.
2. **The opening hours are the hardest text to read.** They're in Pacifico, a decorative script, at 11px. Script fonts are fine for a headline, but they're hard to read in small sizes, and with numbers like "10:00–4:30" they get worse. This is the thing parents came for.
3. **There are too many display fonts.** Bangers (comic-book), Pacifico (retro script) and Lobster (bold script) each have a strong personality, and they clash. Lobster and Pacifico are so similar that using both looks like a mistake, not a choice.
4. **There are no fallback fonts.** If the Google Fonts request is slow or blocked, the browser falls back to a default serif. Each rule should end with something like `, sans-serif`.
5. **It loads more than it needs.** Four font families on a mobile connection slows the page for little visual gain.

**What's fine:** the playful feel suits the audience, and Josefin Sans is a good friendly body font at a normal weight.

**What I'd suggest**

- Use one playful display font for headings and the tagline. Pacifico or Bangers would both work, but not both.
- Use Josefin Sans at regular weight (400) at 16px or larger for everything parents need to read.
- Set opening hours and prices in the body font, ideally slightly bigger or bolder, so they stand out.

```css
@import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Josefin+Sans:wght@400;700&display=swap');

body { font-family: 'Josefin Sans', sans-serif; font-weight: 400; font-size: 16px; line-height: 1.5; }
h1, h2, .tagline { font-family: 'Pacifico', cursive; font-weight: 400; }
.opening-hours { font-family: 'Josefin Sans', sans-serif; font-weight: 700; font-size: 18px; }
```

If your friend wants to keep Bangers for the main title, that's reasonable. Use it only on the `h1`, and keep everything else to the two fonts above.
