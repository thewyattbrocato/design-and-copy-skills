The problem is mostly that the page uses five different families, and each one is a different style. Patients read that as visual noise, even if each choice looks fine alone.

**What's wrong**

1. **Too many families.** Open Sans, Playfair Display, Montserrat, Lora, Poppins, and Courier New are six faces. A clinic page needs one, at most two.
2. **Near-duplicate sans faces.** Montserrat (h2) and Poppins (buttons, nav) are both wide geometric sans. They are similar enough to look like a mistake, and different enough to look inconsistent.
3. **Two serifs that compete.** Playfair (h1) has high contrast and thin hairlines, and Lora (h3, doctor names) is a text serif. Headings and names end up in different voices.
4. **Courier New for phone numbers.** Monospace is for code and aligned columns. Courier New is spindly and light at small sizes, which is hard for older eyes. Phone numbers are the most important text on the page for this audience, and this makes them the hardest to read.
5. **Poppins in buttons and nav.** Poppins has round, closed shapes, so letters like I, l, and 1 look alike. Appointment and navigation labels need to be unambiguous.

**Suggested fix: one family for the whole site**

Pick a sturdy humanist sans with a real weight range, distinct I/l/1 and O/0, and tabular figures. Atkinson Hyperlegible is a good candidate because it was designed for low-vision readers. Check its license for web use before you ship it. Source Sans 3 is a solid alternative.

```css
:root {
  --font-main: 'Atkinson Hyperlegible', system-ui, -apple-system, 'Segoe UI', Arial, sans-serif;
}

body,
h1, h2, h3,
.doctor-name,
.btn,
nav a,
.phone-number {
  font-family: var(--font-main);
}

/* Keep digits aligned in phone numbers, times, and dates */
.phone-number,
.appointment-info {
  font-variant-numeric: tabular-nums;
}
```

Hierarchy then comes from size and weight inside the one family, not from mixing faces. Only use the weights you actually load, and don't rely on faux bold or italic.

If you want a serif for long reading, such as an about page or patient instructions, use one serif for that role only and keep headings and buttons in the sans.

**Two things I couldn't check from the CSS**

- Whether these fonts are actually loaded. If Playfair, Lora, or Poppins fail to load, the browser falls back to a default serif or sans, which can add to the mismatch. Check the Network tab.
- Text sizes and line spacing for older readers. Those are typesetting decisions and should be reviewed separately.
