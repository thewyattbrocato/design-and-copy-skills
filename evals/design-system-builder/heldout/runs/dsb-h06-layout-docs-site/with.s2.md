I've assumed one brand and a small team, and I couldn't check this against your current CSS. If your existing widths and breakpoints differ, merge them into these values instead of adding new ones.

## The numbers

| Token | Value | Why |
|---|---|---|
| `--w-prose` | `38rem` (608px) | At 17px body text this gives about 70 characters per line. It is the only reading measure, used for articles and marketing copy. |
| `--w-wide` | `64rem` (1024px) | Code blocks, tables, screenshots and feature rows. It is a maximum and shrinks to fit the space. |
| `--w-page` | `80rem` (1280px) | Outer limit for everything. On bigger monitors the content stays centered and the page doesn't stretch. |
| `--margin` | `clamp(1rem, 5vw, 2.5rem)` | Side padding. About 19px on a phone, 40px from 800px up. |
| `--gap` | `clamp(1rem, 2.5vw, 1.5rem)` | Gutter between grid columns and cards. |
| `--space-section` | `clamp(3rem, 8vw, 6rem)` | Vertical space between marketing sections. |
| Breakpoints | `40em` (640), `64em` (1024), `80em` (1280) | Media queries can't read variables, so these are literals. They are the only three allowed. |
| Docs shell | sidebar `15rem` at ≥64em, TOC `13rem` at ≥80em | Both fit inside `--w-page`. |
| Body text | `1.0625rem` / 1.65 | The prose measure depends on this. If you change the body size, re-derive `--w-prose`. |

The widths are 38, 64 and 80rem. Each is at least 25% larger than the one before, so none are close enough to confuse.

## How the pages share rules

Every page uses one grid with named column lines. Children default to the prose column, and a child can opt into `wide`, `page` or `full` with a single class. Docs articles and the marketing page use the same grid and differ only in which column each block picks.

- **Phone:** the wide and page tracks collapse to zero, so everything is prose width minus the margin. Code and tables scroll sideways inside their own box.
- **Big monitor:** content stops at 80rem and stays centered.

## CSS

```css
:root {
  --w-prose: 38rem;
  --w-wide: 64rem;
  --w-page: 80rem;
  --margin: clamp(1rem, 5vw, 2.5rem);
  --gap: clamp(1rem, 2.5vw, 1.5rem);
  --space-section: clamp(3rem, 8vw, 6rem);
}

body { font-size: 1.0625rem; line-height: 1.65; }

/* One grid for every page. Children default to the prose column. */
.l-grid {
  display: grid;
  grid-template-columns:
    [full-start] minmax(var(--margin), 1fr)
    [page-start] minmax(0, calc((var(--w-page) - var(--w-wide)) / 2))
    [wide-start] minmax(0, calc((var(--w-wide) - var(--w-prose)) / 2))
    [prose-start] min(100% - 2 * var(--margin), var(--w-prose))
    [prose-end] minmax(0, calc((var(--w-wide) - var(--w-prose)) / 2))
    [wide-end] minmax(0, calc((var(--w-page) - var(--w-wide)) / 2))
    [page-end] minmax(var(--margin), 1fr)
    [full-end];
}
.l-grid > *       { grid-column: prose; }
.l-grid > .wide   { grid-column: wide; }
.l-grid > .page   { grid-column: page; }
.l-grid > .full   { grid-column: full; }

/* Long-form content */
.prose > * + * { margin-block-start: 1.25em; }
.prose :is(h1, h2, h3) { text-wrap: balance; line-height: 1.2; }
.prose :is(h2, h3) { margin-block-start: 2em; scroll-margin-block-start: 5rem; }

/* Code and wide tables: wide column, scroll inside the box, never the page */
.prose pre,
.table-wrap {
  grid-column: wide;
  overflow-x: auto;
  overscroll-behavior-x: contain;
  max-width: 100%;
}
.prose pre { font-size: 0.875rem; line-height: 1.55; padding: 1rem 1.25rem; tab-size: 2; }
.table-wrap table { min-width: 100%; border-collapse: collapse; font-size: 0.9375rem; font-variant-numeric: tabular-nums; }
.table-wrap :is(th, td) { padding: 0.5rem 0.75rem; text-align: start; white-space: nowrap; }
.table-wrap td.wrap { white-space: normal; min-width: 16rem; }

/* 12-column grid inside the page column, for feature rows and similar */
.cols {
  grid-column: page;
  display: grid;
  gap: var(--gap);
  grid-template-columns: 1fr;
  padding-inline: 0;
}
@media (min-width: 64em) {
  .cols { grid-template-columns: repeat(12, 1fr); align-items: center; }
  .feature > .text  { grid-column: span 5; }
  .feature > .media { grid-column: span 7; }
  .feature:nth-of-type(even) > .text  { order: 2; }
}

/* Marketing sections */
.section { padding-block: var(--space-section); }

/* Pricing: 1 column, then 2, then 3. 4+ tiers wrap at the same steps. */
.pricing {
  grid-column: page;
  display: grid;
  gap: var(--gap);
  grid-template-columns: 1fr;
}
@media (min-width: 40em) { .pricing { grid-template-columns: repeat(2, 1fr); } }
@media (min-width: 64em) { .pricing { grid-template-columns: repeat(3, 1fr); } }
.pricing > * { min-width: 0; }

/* Docs shell */
.docs-shell { max-width: var(--w-page); margin-inline: auto; }
.docs-shell > nav, .docs-shell > aside { display: none; }
@media (min-width: 64em) {
  .docs-shell { display: grid; grid-template-columns: 15rem minmax(0, 1fr); column-gap: 2rem; }
  .docs-shell > nav { display: block; position: sticky; top: 0; height: 100dvh; overflow-y: auto; }
}
@media (min-width: 80em) {
  .docs-shell { grid-template-columns: 15rem minmax(0, 1fr) 13rem; }
  .docs-shell > aside { display: block; position: sticky; top: 0; height: 100dvh; overflow-y: auto; }
}
```

## Usage

```html
<main class="l-grid prose">          <!-- article -->
  <h1>…</h1><p>…</p>
  <pre>…</pre>                       <!-- wide column -->
  <div class="table-wrap"><table>…</table></div>
</main>

<div class="l-grid">                 <!-- marketing -->
  <section class="section"><h1>…</h1><p>…</p></section>   <!-- prose width -->
  <section class="cols feature">…</section>
  <section class="pricing">…</section>
</div>
```

## Trade-offs

- With the sidebar and TOC both showing (≥80em), the article area is about 48rem. The wide column then barely exceeds prose width. Between 64em and 80em, with only the sidebar, code gets more room. I accepted this because the sidebar and TOC matter more than extra code width.
- I used `rem` for the measure instead of `ch`. That makes it predictable, but it won't follow a later change in body font size. Adjust `--w-prose` whenever the body size changes.
