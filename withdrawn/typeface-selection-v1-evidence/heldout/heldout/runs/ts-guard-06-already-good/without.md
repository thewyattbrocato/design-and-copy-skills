I found a few real problems and one judgment call. The corrected CSS is below.

```css
:root {
  --font-body: Georgia, Cambria, 'Times New Roman', serif;
  --font-ui: system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  --font-mono: ui-monospace, Menlo, Consolas, 'Courier New', monospace;
}

html { -webkit-text-size-adjust: 100%; text-size-adjust: 100%; }

body {
  font-family: var(--font-body);
  font-size: 1.125rem;
  line-height: 1.6;
  max-width: 65ch;
  margin-inline: auto;
  padding-inline: 1rem;
}

nav, .meta { font-family: var(--font-ui); }
button, input, select, textarea, label { font-family: var(--font-ui); }
button, input, select, textarea { font-size: inherit; }

code, pre { font-family: var(--font-mono); font-size: 0.9em; }
pre code { font-size: inherit; }

h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-ui);
  font-weight: 600;
  line-height: 1.2;
  letter-spacing: -0.01em;
}
```

**What I changed**
- **`font-weight: 650`:** Most system fonts (Georgia, Segoe UI, Arial, Helvetica Neue) aren't variable fonts. Browsers snap 650 to 700 or 600 depending on the font, so headings would look different from one platform to the next. I used 600, which snaps predictably. Use 700 if you want it bolder.
- **Nested `code` in `pre`:** `code, pre` both set `0.9em`, so code blocks rendered at about 0.81em. `pre code { font-size: inherit }` fixes that.
- **Heading `line-height`:** Headings inherited the body's 1.6, which looks loose at heading sizes. I set 1.2.
- **Form controls:** `textarea` and `select` weren't covered, and form controls don't inherit font size by default. I added both and set `font-size: inherit` on the controls.
- **Measure:** There was no line-length limit, which matters most for long-form essays. `max-width: 65ch` keeps lines readable. Skip it if your layout wrapper already sets a width.
- **`h4`–`h6`:** I added them so they don't fall back to the serif body font.
- **`text-size-adjust`:** This stops iOS from inflating text in landscape.

**Judgment call**
Your headings use sans-serif over a serif body. That's a legitimate pairing, but for a site called *Slow Harbour Notes* with essays, serif headings (`var(--font-body)`) might suit the tone better. I left it as you had it. Check it against the client's brand direction.

I didn't touch any files, since you pasted the CSS inline.
