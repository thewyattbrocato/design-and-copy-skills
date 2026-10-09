Here's one set of rules for every page. Articles, the front page, and pricing all sit on the same three-column frame. Prose is capped at a 68ch measure, and wide things like tables, code, and grids use a 1280px ceiling.

## The numbers

| Token | Value | Why |
|---|---|---|
| Breakpoints | 40rem (640), 64rem (1024), 80rem (1280) | Phone, tablet, desktop, wide monitor |
| Gutter | `clamp(1rem, 0.5rem + 2vw, 2rem)` | 16px on phones, 32px cap on large screens |
| Column gap | `clamp(1rem, 0.75rem + 1vw, 1.5rem)` | Keeps cards from crowding on phones |
| Reading measure | `68ch` | Inside the 60–75ch range; roughly 650px at 17px body |
| Wide max | `1280px` | Tables, code, and grids stop growing on big monitors |
| Body size | `1.0625rem` (17px), line-height 1.6 | Prose reads comfortably at that measure |
| Section spacing | `clamp(3rem, 2rem + 5vw, 6rem)` | Vertical rhythm scales with the viewport |
| Grid columns | 1 (phone), 2 (640+), 3 (1024+) for features; pricing 2 to 3 tiers → 1/2/N, 4 tiers → 1/2/2 then 4 at 1280+ | One pattern for every card grid |

Keep the pixel values out of the media queries. Custom properties can't be used in media queries, so the breakpoints are literals. Keep them in sync with the tokens.

## CSS

```css
:root {
  /* Breakpoints (literal values: custom properties can't be used in @media) */
  /* sm 40rem (640px) · lg 64rem (1024px) · xl 80rem (1280px) */

  --gutter: clamp(1rem, 0.5rem + 2vw, 2rem);
  --col-gap: clamp(1rem, 0.75rem + 1vw, 1.5rem);
  --content-max: 1280px;   /* wide: tables, code, grids */
  --measure: 68ch;         /* prose */
  --section-space: clamp(3rem, 2rem + 5vw, 6rem);
  --body-size: 1.0625rem;  /* 17px */
}

body {
  font-size: var(--body-size);
  line-height: 1.6;
}

/* One frame for every page: gutter | content | gutter */
.layout {
  display: grid;
  grid-template-columns:
    minmax(var(--gutter), 1fr)
    minmax(0, var(--content-max))
    minmax(var(--gutter), 1fr);
}
.layout > * {
  grid-column: 2;
  min-width: 0;
}

/* Articles: text capped at the measure, wide blocks opt in */
.article > * {
  width: 100%;
  max-width: var(--measure);
  justify-self: center;
}
.article > .wide {
  max-width: var(--content-max);
}

/* Code: scroll inside its own box, never the page */
pre {
  overflow-x: auto;
  white-space: pre;
  tab-size: 2;
}

/* Tables: scroll inside the wrapper, keep a minimum width so columns don't crush */
.table-wrap {
  overflow-x: auto;
}
.table-wrap table {
  width: 100%;
  min-width: 32rem;
  border-collapse: collapse;
}

/* Card grids: features and pricing share the same rules */
.card-grid {
  display: grid;
  gap: var(--col-gap);
  grid-template-columns: 1fr;
}
@media (min-width: 40rem) {
  .card-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (min-width: 64rem) {
  .card-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .card-grid--four { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (min-width: 80rem) {
  .card-grid--four { grid-template-columns: repeat(4, minmax(0, 1fr)); }
}

/* Sections */
.section {
  padding-block: var(--section-space);
}
```

Usage:

```html
<main class="layout article">
  <h1>Title</h1>
  <p>Prose is capped at 68ch and centered.</p>
  <div class="table-wrap wide"><table>…</table></div>
  <pre class="wide"><code>…</code></pre>
</main>

<section class="layout section">
  <div class="card-grid card-grid--four">…</div>
</section>
```

## Notes

- **Wide blocks** get `.wide` so they can use the full 1280px column. Everything else stays at the measure.
- **Pricing**: if you have 2 or 3 tiers, use `.card-grid` alone. Four tiers use `.card-grid--four`, which gives 2 columns at tablet and 4 at 1280px. That avoids a lone orphan card.
- **Test widths**: check 360, 768, 1024, 1280, and 2560. At 2560 the content should stay centered at 1280px, which is intentional.
- I didn't have Quillmark's stylesheet or markup in this environment, so these are standalone. Map the class names onto your existing components. If you share the current CSS, I can show you what to change.
