**What's wrong:** the site uses six font families, and each one has a different job from the others. That's why it looks messy.

- **Six families, no system.** Open Sans, Playfair Display, Montserrat, Lora, Poppins and Courier New each have different proportions and stroke contrast. The page shifts voice at every heading level.
- **Three sans faces that look alike.** Open Sans (body), Montserrat (h2) and Poppins (buttons and nav) are all clean sans-serifs. They differ just enough to look like a mistake, not a choice.
- **Two serifs doing different jobs.** Playfair Display on h1 is a high-contrast display serif. Lora on h3 and doctor names is a text serif. Neither has a clear role.
- **Courier New on phone numbers.** Monospace is for code. On a medical site it looks like a typewriter or a technical error, and it's the one thing patients most need to find quickly. Courier is also thin, which is hard to read for older eyes.
- **Thin hairline strokes in Playfair and Courier.** At small sizes and on low-quality screens, these are the hardest to read for older patients.
- **No fallbacks beyond the generic family.** If a web font fails to load, the browser drops to its default sans or serif, and the mismatch gets worse. I can't tell from the CSS whether these fonts are actually loaded.

**Fix:** use one family with real weight range, and add one serif only if you want a distinct heading voice. Here's the simplest option.

```css
body, h2, h3, .doctor-name, .btn, nav a, .phone-number {
  font-family: 'Source Sans 3', 'Segoe UI', system-ui, -apple-system, sans-serif;
}
h1 {
  font-family: 'Source Serif 4', Georgia, 'Times New Roman', serif;
}

h1 { font-weight: 600; }
h2, h3, .doctor-name { font-weight: 600; }
.btn, nav a { font-weight: 600; }
.phone-number { font-variant-numeric: tabular-nums; font-weight: 600; }
```

- **Body, h2, h3, buttons, nav, phone numbers:** one sturdy humanist sans in different weights. Hierarchy comes from size and weight, not from switching families.
- **h1 only:** a text serif gives the clinic some warmth. The sans and serif differ plainly in category, so they read as a deliberate pair.
- **Phone numbers:** the same sans, semibold, with tabular figures so digits line up. They stay easy to find and read.

If you'd rather have no serif at all, drop the h1 rule. One family is a perfectly good answer here.

Two assumptions: the site is read on screens in Latin script, and you can load web fonts. Source Sans 3 and Source Serif 4 are open-licensed, but confirm that before you self-host them. If you can't load fonts, the `Segoe UI` / `system-ui` fallbacks above still render cleanly.
