The rules below use one set of tokens and one page frame. Articles, the front page, and the pricing grid all cap at the same content width, and the prose column is set in `ch` so it scales with the type.

## The numbers

| Token | Phone `<600px` | Tablet `600–899` | Small desktop `900–1199` | Desktop `≥1200` |
|---|---|---|---|---|
| Columns | 4 | 8 | 12 | 12 |
| Gutter | 16px | 20px | 24px | 24px |
| Page margin | 16px | 24px | 32px | 40px |
| Prose measure | 65ch (capped by screen width) | 65ch | 65ch | 65ch |
| Max content width | fluid | fluid | fluid | 1120px |

- **Body text:** 17px (`1.0625rem`), line-height 1.6, the same at every size. Phones get no smaller type.
- **Reading measure:** `65ch` is about 70 characters of English prose, inside the 45–75 range.
- **Max content width:** 1120px for everything: code, tables, feature rows, pricing. A big monitor gets more whitespace, not wider columns.

## The CSS

```css
:root {
  /* Type */
  --font-body: 1.0625rem;   /* 17px at every size */
  --line-body: 1.6;

  /* Layout tokens: change here only */
  --cols: 4;
  --gutter: 16px;
  --margin: 16px;
  --measure: 65ch;          /* prose line length */
  --wide: 1120px;           /* max content width for every page */
  --tiers: 4;               /* pricing tiers */
}

@media (min-width: 600px) {
  :root { --cols: 8; --gutter: 20px; --margin: 24px; }
}
@media (min-width: 900px) {
  :root { --cols: 12; --gutter: 24px; --margin: 32px; }
}
@media (min-width: 1200px) {
  :root { --margin: 40px; }
}

body {
  font-size: var(--font-body);
  line-height: var(--line-body);
}

/* Page frame: every page wraps its content in this */
.page {
  width: 100%;
  max-width: calc(var(--wide) + 2 * var(--margin));
  margin-inline: auto;
  padding-inline: var(--margin);
}

/* Articles: prose in the middle column, blocks that need room span the full width */
.article {
  display: grid;
  grid-template-columns: minmax(0, 1fr) min(var(--measure), 100%) minmax(0, 1fr);
}
.article > * {
  grid-column: 2;
}
.article > :where(pre, table, figure, .table-wrap, .wide) {
  grid-column: 1 / -1;
  min-width: 0;
}

/* Long code and wide tables scroll inside their own box, never the page */
pre {
  overflow-x: auto;
  font-size: 0.875rem;
  line-height: 1.5;
}
.table-wrap {
  overflow-x: auto;
}
.table-wrap table {
  width: max-content;
  min-width: 100%;
}

/* Long unbroken strings (URLs, identifiers) must not push the measure wider */
.article p,
.article li {
  overflow-wrap: anywhere;
}

/* Media never exceeds its column */
img, video, svg {
  max-width: 100%;
  height: auto;
}

/* Marketing: 12-column (or 4/8-column) grid inside the same page frame */
.grid {
  display: grid;
  grid-template-columns: repeat(var(--cols), minmax(0, 1fr));
  gap: var(--gutter);
}

/* Feature rows: stacked on phone, split 5/6 on desktop */
.feature {
  display: grid;
  gap: var(--gutter);
  align-items: center;
}
@media (min-width: 900px) {
  .feature {
    grid-template-columns: repeat(12, minmax(0, 1fr));
  }
  .feature__text  { grid-column: 1 / span 5; }
  .feature__media { grid-column: 7 / span 6; }
}

/* Pricing: 1 column, then 2, then one column per tier */
.pricing {
  display: grid;
  gap: var(--gutter);
  grid-template-columns: minmax(0, 1fr);
}
@media (min-width: 600px) {
  .pricing { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (min-width: 1200px) {
  .pricing { grid-template-columns: repeat(var(--tiers), minmax(0, 1fr)); }
}
```

## Usage

```html
<main class="page">
  <article class="article">
    <h1>Title</h1>
    <p>Prose sits in the measured column.</p>
    <pre><code>long code scrolls inside this block</code></pre>
    <div class="table-wrap"><table>…</table></div>
  </article>
</main>

<main class="page">
  <section class="feature">
    <div class="feature__text">…</div>
    <div class="feature__media"><img src="…" alt=""></div>
  </section>
  <section class="pricing" style="--tiers: 3">…</section>
</main>
```

## Why these choices

- **One frame for everything.** Articles and the marketing page both use `.page`, so the left and right edges line up from one page to the next.
- **Measure in `ch`, not px.** `65ch` tracks the font. Set it on the element that holds the text.
- **Wide content is not wider prose.** Code and tables get the full 1120px. Prose stays at 65ch, so the reading column does not change between pages.
- **Scroll, don't squeeze.** Long code and wide tables scroll in their own box on phones. The page never scrolls sideways.
- **Pricing counts fixed.** I assumed 4 tiers. Pass `--tiers` for a different count. With 3 tiers, the 1200px step gives three even columns. If the grid has to step at 900px instead, move that rule.

I did not check for existing CSS in the working directory, since it has no project files and is not a git repo. If you already have stylesheets, the tokens in `:root` are the part to map onto them.
