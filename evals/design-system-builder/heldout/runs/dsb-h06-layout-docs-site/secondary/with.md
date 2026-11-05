Here's one set of rules. Every page uses the same outer container, gutter, and grid. Prose is narrower than code, tables, and figures, and both are centered on the same axis.

## The numbers

| Token | Value | Where it lands |
|---|---|---|
| Container max | 1280px | Outer edge stops growing above this |
| Gutter | 16px → 32px, fluid (`clamp(1rem, 4vw, 2rem)`) | Side padding |
| Grid gap | 16 / 24 / 32px | Phone / ≥640 / ≥1024 |
| Section padding | 48px → 120px, fluid | Vertical rhythm |
| Prose measure | 68ch | About 65–75 characters per line |
| Wide blocks | 1056px | Code, tables, figures, wide images |
| Prose size | 16px → 18px, fluid | Body text |
| Prose line-height | 1.65 | Body text |

Breakpoints are 40rem (640), 48rem (768), 64rem (1024), and 80rem (1280). Use only these. Media queries can't read CSS variables, so the values are repeated in the queries.

## CSS

```css
/* layout.css: one set of rules for every page */

:root {
  --container: 80rem;                                   /* 1280px outer max */
  --gutter: clamp(1rem, 4vw, 2rem);                     /* 16px → 32px */
  --gap: 1rem;                                          /* 16px phone */
  --section-y: clamp(3rem, 2rem + 6vw, 7.5rem);         /* 48px → 120px */

  --measure: 68ch;                                      /* prose column */
  --wide: 66rem;                                        /* 1056px: code, tables, figures */

  --prose-size: clamp(1rem, 0.95rem + 0.25vw, 1.125rem); /* 16px → 18px */
  --prose-leading: 1.65;
}

@media (min-width: 40rem) { :root { --gap: 1.5rem; } }  /* 640px */
@media (min-width: 64rem) { :root { --gap: 2rem; } }    /* 1024px */

*, *::before, *::after { box-sizing: border-box; }

/* Outer container: shared by front page and articles */
.container {
  max-width: var(--container);
  margin-inline: auto;
  padding-inline: var(--gutter);
}

/* Full-bleed backgrounds go on <section>, content goes inside .container */
.section { padding-block: var(--section-y); }

/* Grids. minmax(0, 1fr) stops wide children from forcing a track wider */
.grid {
  display: grid;
  gap: var(--gap);
  grid-template-columns: minmax(0, 1fr);
}

/* Feature rows: 1 → 2 → 3 columns */
@media (min-width: 48rem) {
  .grid--feature { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (min-width: 64rem) {
  .grid--feature { grid-template-columns: repeat(3, minmax(0, 1fr)); }
}

/* Pricing, 3 tiers: 1 → 3 columns (never 2, which orphans a card) */
@media (min-width: 64rem) {
  .grid--pricing-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
}

/* Pricing, 4 tiers: 1 → 2 → 4 columns */
@media (min-width: 48rem) {
  .grid--pricing-4 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (min-width: 80rem) {
  .grid--pricing-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
}

/* Prose: text is capped at the measure; wide blocks get the wider column */
.prose {
  font-size: var(--prose-size);
  line-height: var(--prose-leading);
}
.prose > * {
  max-width: var(--measure);
  margin-inline: auto;
}
.prose > :is(pre, figure, .table-scroll, .wide) {
  max-width: var(--wide);
}

/* Code never wraps; it scrolls inside its own box */
.prose pre {
  overflow-x: auto;
  white-space: pre;
  font-size: 0.875em;
  line-height: 1.5;
  padding: 1rem;
}

/* Tables scroll inside a wrapper instead of squeezing columns */
.table-scroll { overflow-x: auto; }
.table-scroll table {
  width: 100%;
  min-width: 36rem;
  border-collapse: collapse;
}
```

Wrap every article table in `<div class="table-scroll">`. If your markdown renderer produces the tables, have it add the wrapper.

## Rules

1. **One container.** Front page and articles both use `.container`. Only the inner content changes.
2. **Prose never exceeds 68ch.** Paragraphs, lists, and headings are capped at the measure.
3. **Code, tables, and figures can reach 1056px.** They're centered on the same axis as the text, so the column edges stay aligned.
4. **Code doesn't wrap.** Long lines scroll inside the block.
5. **Tables scroll below their min-width** (36rem) rather than crushing columns.
6. **Grid tracks are `minmax(0, 1fr)`.** Any child can then shrink without breaking the layout.
7. **Column counts are fixed per breakpoint.** Feature rows go 1 → 2 → 3. Pricing goes 1 → 3 for three tiers, or 1 → 2 → 4 for four. Don't use auto-fit for pricing, because it produces uneven counts.
8. **Nothing widens past 1280px.** On large monitors the extra width becomes margin, and text stays at the same measure.

## Check before you ship

- Load an article and the front page at 320, 768, 1024, 1440, and 2560px.
- At each width, confirm `document.documentElement.scrollWidth` equals `window.innerWidth`. If it doesn't, a wide element is escaping its container.
- Confirm a long code line scrolls inside its box and doesn't widen the page.
- Measure a paragraph's characters per line in the browser. If the average is well above 75 or below 60, adjust `--measure`.

I didn't look at your existing stylesheet, so the variable names may need to map onto your current tokens.
