Assumptions: one brand, a plain CSS stack, and a docs shell with a left nav and a right table of contents. Treat the numbers as starting points and check them against your real articles.

## The rules

| Decision | Value | Why |
|---|---|---|
| Breakpoints (3) | 40rem (640), 64rem (1024), 80rem (1280) | Phone to tablet, the point where the docs sidebar fits, and the point where the table of contents fits. |
| Page max width | 80rem (1280) | Marketing and docs share it, so the header and footer line up. The page is centered above that and nothing scales up. |
| Page margin | `clamp(1rem, 5vw, 2rem)` | 16px on small phones, 32px from about 640px up. |
| Grid columns | 4, then 8 at 40rem, then 12 at 64rem | Marketing layouts snap to this grid. |
| Column gap | 1rem, then 1.5rem at 64rem | |
| Reading measure | 66ch for body prose | Applies in docs and marketing. |
| Lead paragraph measure | 52ch | Shorter for large intro text. |
| Heading measure | 24ch | Keeps headings from running into one long line. |
| Body text | 1.0625rem (17px), line-height 1.6 | At 17px, 66ch is about 600px, which fits the narrowest docs column. |
| Docs sidebar and TOC | 16rem and 14rem | Sidebar appears at 64rem, TOC at 80rem. Below that the TOC collapses to a block above the article. |
| Code and tables | Fill the column up to its full width | Only text lines are held to the measure. Code and tables scroll horizontally inside their own wrapper and never wrap or shrink the page. |

Doc content column width at the breakpoints: at 1024px it is about 664px, and at 1280px it is about 656px. Both are wider than the prose measure, so code and tables get the full column.

## CSS

```css
:root {
  /* widths and measure */
  --width-page: 80rem;
  --page-margin: clamp(1rem, 5vw, 2rem);
  --measure: 66ch;
  --measure-lead: 52ch;
  --measure-heading: 24ch;

  /* grid */
  --grid-cols: 4;
  --grid-gap: 1rem;

  /* docs shell */
  --docs-nav: 16rem;
  --docs-toc: 14rem;
  --docs-gap: 2.5rem;

  --font-size-body: 1.0625rem;
  --line-height-body: 1.6;
}

/* Media queries can't read custom properties, so these are literals:
   40rem / 64rem / 80rem. Keep them in sync with this file only. */
@media (min-width: 40rem) { :root { --grid-cols: 8; } }
@media (min-width: 64rem) { :root { --grid-cols: 12; --grid-gap: 1.5rem; } }

body {
  font-size: var(--font-size-body);
  line-height: var(--line-height-body);
}

/* page container: every page, every section */
.page {
  inline-size: min(100% - 2 * var(--page-margin), var(--width-page));
  margin-inline: auto;
}

/* the grid */
.grid {
  display: grid;
  grid-template-columns: repeat(var(--grid-cols), minmax(0, 1fr));
  gap: var(--grid-gap);
}
.grid > * { grid-column: 1 / -1; }  /* default: full width; spans below */

/* reading measure: text is capped, wide content is not */
.prose > * { max-inline-size: var(--measure); }
.prose > pre,
.prose > .table-wrap,
.prose > figure,
.prose > .callout { max-inline-size: none; }
.lead { max-inline-size: var(--measure-lead); }
h1, h2 { max-inline-size: var(--measure-heading); text-wrap: balance; }

/* code and wide tables scroll in place */
pre {
  overflow-x: auto;
  font-size: 0.875rem;
  line-height: 1.5;
  tab-size: 2;
  white-space: pre;
}
.table-wrap { overflow-x: auto; }        /* add tabindex="0" in markup so it's keyboard-scrollable */
.table-wrap > table { min-inline-size: 100%; }
.prose :not(pre) > code { overflow-wrap: anywhere; }  /* long identifiers don't push the page wide */

/* docs shell */
.docs {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: var(--docs-gap);
}
.docs-nav { display: none; }             /* drawer below 64rem */
@media (min-width: 64rem) {
  .docs { grid-template-columns: var(--docs-nav) minmax(0, 1fr); }
  .docs-nav { display: block; position: sticky; top: 1rem; align-self: start; }
}
@media (min-width: 80rem) {
  .docs { grid-template-columns: var(--docs-nav) minmax(0, 1fr) var(--docs-toc); }
  .docs-toc { position: sticky; top: 1rem; align-self: start; }
}
@media (max-width: 79.999rem) {
  .docs-toc { order: -1; }               /* collapsed block above the article */
}

/* marketing: feature rows on the 12-col grid */
@media (min-width: 64rem) {
  .feature-row > .feature-text  { grid-column: 1 / span 5; align-self: center; }
  .feature-row > .feature-media { grid-column: 6 / span 7; }
  .feature-row.is-reversed > .feature-text  { grid-column: 8 / span 5; grid-row: 1; }
  .feature-row.is-reversed > .feature-media { grid-column: 1 / span 7; grid-row: 1; }
}

/* marketing: pricing grid (stacked below 64rem, three across above) */
.pricing {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: var(--grid-gap);
  max-inline-size: 36rem;
  margin-inline: auto;
}
@media (min-width: 64rem) {
  .pricing {
    grid-template-columns: repeat(3, minmax(0, 1fr));
    max-inline-size: none;
  }
}
```

## How to use it

- Wrap every page section in `.page`. Docs articles use `.docs` inside it, with the article body in `.prose`. Marketing text blocks also use `.prose`, so both agree on the measure.
- Make new layouts span the 12 columns (5 and 7, 4 and 4 and 4, 6 and 6) instead of adding widths.
- Always give grid and flex children `minmax(0, 1fr)` or `min-width: 0`. Otherwise one wide table or code block stretches the whole page.
- If you have more than three pricing tiers, move the 36rem cap to the 40rem breakpoint and use two columns between 40rem and 64rem.
