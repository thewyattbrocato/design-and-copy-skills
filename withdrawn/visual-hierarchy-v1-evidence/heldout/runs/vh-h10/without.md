I'd recommend the third option: keep the table uniform and add a small "Special" label.

**Why:**

- **It's accessible.** A label is text, so screen readers announce it and colorblind users see it. Bold is subtle and easy to miss. A yellow box with a star depends on color and an icon, and the star needs alt text or an aria-label to be conveyed at all.
- **The page is tiny.** With only five rows and two columns, one row that stands out will already draw the eye. A bright yellow box would be too loud for a table this plain, and it would dominate the page.
- **It's unambiguous.** Bold on a single row can look like a rendering glitch or a "today" marker. The word "Special" says what it is.
- **It's robust.** The label survives printing in black and white, which matters for a school menu that parents may print or post on a fridge. It also survives text-only views and narrow mobile screens.

**Implementation tips:**

- Put the label next to the dish name, for example "Chicken Parmesan `Chef's special`", rather than in its own column. That way the table structure stays at main and side only.
- Make it a small pill or badge with enough contrast. Aim for at least 4.5:1 against its background.
- Use real text in the markup, not a CSS-only pseudo-element, so assistive tech and copy/paste pick it up.

**Optional tweak:** if the team wants a bit more visual pull, add a subtle tint to the label itself, or a light left border on the row. Keep the word "Special" as the main signal, so the highlight doesn't depend on the color.
