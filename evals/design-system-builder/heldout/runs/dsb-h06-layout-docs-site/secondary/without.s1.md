Use one outer frame, two content widths, and fixed breakpoints for the grids. Every page then shares the same centre line. Prose stays at reading measure, and code, tables, figures, and the grids fill a wider column that is capped on big screens.

## The numbers

| Token | Value | Applies to |
|---|---|---|
| `--frame` | 1360px | Outer max width, gutters included. Everything sits inside it. |
| `--gutter` | clamp(16px, 4vw, 48px) | Side padding inside the frame |
| `--gap` | clamp(16px, 2.5vw, 32px) | Grid and card gaps |
| `--measure` | 68ch (~680px at 18px) | Prose: paragraphs, lists, headings |
| `--wide` | 1120px | Code blocks, tables, figures, feature rows, pricing |
| Body size | 16px phone, 18px from 768px | Line height 1.65 |

Breakpoints: 640px (2 columns), 768px (body size up, feature rows go side by side), 1024px (3 columns), 1280px (4-tier pricing goes to 4 columns). Use these four and no others.

## CSS

```css
/* ---------- tokens ---------- */
:root {
  --font-size-body: 1rem;                       /* 16px on phones */
  --line-height-body: 1.65;
  --frame: 1360px;                              /* outer max, incl. gutters */
  --gutter: clamp(1rem, 4vw, 3rem);             /* 16px → 48px */
  --gap: clamp(1rem, 2.5vw, 2rem);              /* 16px → 32px */
  --measure: 68ch;                              /* prose column */
  --wide: 1120px;                               /* code, tables, grids */
}

@media (min-width: 48rem) {                     /* 768px */
  :root { --font-size-body: 1.125rem; }         /* 18px */
}

*, *::before, *::after { box-sizing: border-box; }

body {
  font-size: var(--font-size-body);
  line-height: var(--line-height-body);
}

/* ---------- frame: every page uses this ---------- */
.frame {
  width: 100%;
  max-width: var(--frame);
  margin-inline: auto;
  padding-inline: var(--gutter);
}

/* ---------- two content widths, one centre line ---------- */
.prose {                                        /* reading column */
  max-width: var(--measure);
  margin-inline: auto;
}

.wide {                                         /* code, tables, grids */
  max-width: var(--wide);
  margin-inline: auto;
}

/* ---------- things that must not widen the page ---------- */
.wide > *,
.prose > * { min-width: 0; }

pre {
  max-width: 100%;
  overflow-x: auto;                             /* code scrolls, page doesn't */
}

.table-scroll {                                 /* wrap every wide table */
  max-width: 100%;
  overflow-x: auto;
}

.table-scroll table {
  width: 100%;
  min-width: 36rem;                             /* below this, scroll inside the wrapper */
  border-collapse: collapse;
}

/* ---------- card grids (pricing, feature cards) ---------- */
/* Fixed steps, not auto-fit, so the layout is predictable at every width. */
.cards {
  display: grid;
  gap: var(--gap);
  grid-template-columns: minmax(0, 1fr);        /* phone: 1 column */
}

@media (min-width: 40rem) {                     /* 640px */
  .cards { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}

@media (min-width: 64rem) {                     /* 1024px */
  .cards { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .cards--4 { grid-template-columns: repeat(2, minmax(0, 1fr)); } /* 4 tiers stay 2×2 */
}

@media (min-width: 80rem) {                     /* 1280px */
  .cards--4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
}

/* ---------- feature rows: text beside media ---------- */
.feature {
  display: grid;
  gap: var(--gap);
  align-items: center;
}

@media (min-width: 48rem) {                     /* 768px */
  .feature { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .feature--reverse .feature__media { order: -1; }
}

.feature img,
.feature video { display: block; width: 100%; height: auto; }
```

## Usage

```html
<header class="frame">
  <div class="prose"><h1>Quillmark</h1><p>Intro…</p></div>
</header>

<main class="frame">
  <article class="prose">
    <h2>Setup</h2>
    <p>Body text…</p>
    <pre><code>npm install quillmark</code></pre>   <!-- breaks out to --wide -->
  </article>
</main>
```

Put wide blocks outside `.prose`, or give them `.wide` inside it. Use `.prose` for text and `.wide` for code, tables, and grids. Pricing is `<section class="frame"><div class="wide cards cards--4">…</div></section>`.

## Notes

- Prose stays at 68ch on a 27-inch monitor. The frame caps at 1360px, so the page never stretches. Wide blocks top out at 1120px, which leaves a visible step between text and code on large screens. That step is intended.
- `68ch` depends on the font. If your body font is much wider or narrower than average, check that prose lands at 60–75 characters per line.
- I didn't look at your existing stylesheet, so these class names are new and will need to be mapped onto whatever is already there.
- To check it, load a long article and the front page at 360, 390, 768, 1024, 1280, 1440, and 2560px. At each width, confirm `document.documentElement.scrollWidth === document.documentElement.clientWidth` (no page-level horizontal scroll), that tables and code scroll inside their own boxes, and that the pricing grid has no single orphaned card.
