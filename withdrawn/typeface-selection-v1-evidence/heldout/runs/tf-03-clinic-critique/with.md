**The problem is that you have six font families doing jobs that one or two should do.**

Open Sans for body, Playfair Display for h1, Montserrat for h2, Lora for h3 and doctor names, Poppins for buttons and nav, and Courier New for phone numbers. Nothing ties them together, so the page reads as messy even if a patient can't say why.

**What fails, and the fix for each:**

1. **Too many families.** Four of the six are close to each other. Montserrat and Poppins are both geometric sans faces, and Open Sans is a third sans. Lora and Playfair are two different serifs. Pairs that nearly match look like a mistake. Use at most two families.
2. **Headings change face at every level.** An h1 in a high-contrast serif, an h2 in a geometric sans, and an h3 in a different serif means the eye has to re-adjust at each step. Give headings one face and let size and weight set the hierarchy.
3. **Courier New on phone numbers.** Monospace is for code and aligned columns. A typewriter face on the most important number on a clinic site looks out of place. It also has thin strokes that are hard to read for older eyes. Put phone numbers in the body face with tabular figures.
4. **Playfair Display is a poor fit here.** It has hairline strokes and extreme contrast, which hold up badly at small sizes and for older readers. If you want a serif, use it only at large sizes.
5. **No fallbacks beyond generics.** If a web font fails to load, patients get the browser's default `sans-serif` or `serif`, which differs from device to device. That may be part of why the site looks inconsistent. I can't tell from the CSS whether the fonts are actually loaded, so check that too.
6. **Weights and italics are unchecked.** If you load only one weight of each font, the browser fakes the bold and italic, and that looks rough. Check the font imports.

**Suggested replacement.** It uses one family, with a serif for headings only if you want warmth:

```css
:root {
  --font-text: 'Source Sans 3', 'Segoe UI', system-ui, -apple-system, Roboto, Arial, sans-serif;
  --font-head: 'Source Serif 4', Georgia, 'Times New Roman', serif;
}

body { font-family: var(--font-text); }
h1, h2, h3, .doctor-name { font-family: var(--font-head); font-weight: 600; }
.btn, nav a { font-family: var(--font-text); font-weight: 600; }
.phone-number { font-family: var(--font-text); font-weight: 600; font-variant-numeric: tabular-nums; }
```

- **Simplest option:** drop `--font-head` and use `--font-text` everywhere, with weight and size setting the hierarchy. That is the safest choice for a clinic.
- **Why these faces:** Source Sans 3 and Source Serif 4 were designed as a matched pair, and both have real bold and italic weights. They are open-licensed, but confirm that you load them with the weights you use. Any other humanist sans with a sturdy serif partner would also work.

**Two notes:**
- I assumed a screen-only, English-language site. If you need other scripts, the font choice changes.
- Body text should be at least 18px for older patients. Size and line spacing are a separate fix from the fonts.

If you share the page's `<link>` or `@font-face` imports, I can check what actually loads.
