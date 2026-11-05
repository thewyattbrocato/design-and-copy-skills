# Quillmark layout rules

I assumed one brand, a plain-CSS site, and a docs page with a sidebar on the left and a table of contents on the right. I haven't run this in a browser.

## The numbers

| Rule | Value |
|---|---|
| Breakpoints | 40em (640px), 60em (960px), 90em (1440px) |
| Columns | 4 below 40em, 8 from 40em, 12 from 60em |
| Page margin | `clamp(1rem, 4vw, 3rem)` (16–48px) |
| Gutter | 16px, then 24px from 40em, then 32px from 60em |
| Reading measure | 68ch target. It can shrink to about 45ch on a phone. It never goes above 75ch. |
| Article body | 17px, line-height 1.65. Code is 14px. |
| Wide width | 72rem (1152px). Code, tables and marketing sections use it. |
| Shell width | 90rem (1440px). This is the docs frame: sidebar, article and table of contents. |
| Docs sidebar | 15rem, from 60em |
| Docs table of contents | 14rem, from 90em |
| Beyond 1440px | Nothing grows. The page stays centered with empty margins. |

I used `em` for the breakpoints so they respond to user font-size settings. Media queries can't read CSS variables, so those three values are written out in each query.

- **Why the table of contents starts at 90em.** At 1280px, the sidebar, table of contents and margins leave the article about 656px. That's under the 68ch target. At 1440px it gets about 816px, which holds the full measure.
- **Why prices stack until 60em.** With 3 plans, a 2-column layout leaves one card alone on a row. Below 60em the cards stack at a capped width instead.

## CSS

```css
/* ---------- tokens ---------- */
:root {
  --layout-margin: clamp(1rem, 4vw, 3rem);
  --layout-gutter: 1rem;
  --layout-cols: 4;

  --measure-prose: 68ch;
  --width-wide: 72rem;
  --width-shell: 90rem;
  --size-sidebar: 15rem;
  --size-toc: 14rem;

  --space-section: 4rem;
}
@media (min-width: 40em) {
  :root { --layout-gutter: 1.5rem; --layout-cols: 8; }
}
@media (min-width: 60em) {
  :root { --layout-gutter: 2rem; --layout-cols: 12; --space-section: 6rem; }
}

/* ---------- page containers ---------- */
.container {                       /* marketing sections, header, footer */
  width: min(100% - 2 * var(--layout-margin), var(--width-wide));
  margin-inline: auto;
}
.container--shell {                /* docs frame */
  width: min(100% - 2 * var(--layout-margin), var(--width-shell));
}
.section { padding-block: var(--space-section); }

/* ---------- docs shell ---------- */
.docs-shell {
  display: grid;
  grid-template-columns: minmax(0, 1fr);        /* phone: article only, nav is a drawer */
  gap: var(--layout-gutter);
}
.docs-shell > * { min-width: 0; }               /* stops code/tables stretching the grid */
@media (min-width: 60em) {
  .docs-shell { grid-template-columns: var(--size-sidebar) minmax(0, 1fr); }
}
@media (min-width: 90em) {
  .docs-shell {
    grid-template-columns: var(--size-sidebar) minmax(0, 1fr) var(--size-toc);
  }
}

/* ---------- article: prose / wide breakout grid ---------- */
.article {
  --breakout: calc((var(--width-wide) - var(--measure-prose)) / 2);
  font-size: 1.0625rem;
  line-height: 1.65;
  display: grid;
  grid-template-columns:
    [full-start] minmax(0, 1fr)
    [wide-start] minmax(0, var(--breakout))
    [content-start] min(var(--measure-prose), 100%)
    [content-end] minmax(0, var(--breakout))
    [wide-end] minmax(0, 1fr)
    [full-end];
}
.article > * { grid-column: content; min-width: 0; }
.article > .wide,
.article > pre,
.article > .table-scroll { grid-column: full; }  /* phone: edge to edge */
@media (min-width: 40em) {
  .article > .wide,
  .article > pre,
  .article > .table-scroll { grid-column: wide; }
}

/* code and tables scroll inside themselves, never the page */
.article pre {
  font-size: 0.875rem;
  line-height: 1.5;
  overflow-x: auto;
  tab-size: 2;
  padding: 1rem var(--layout-margin);
}
.table-scroll { overflow-x: auto; }              /* <div class="table-scroll" tabindex="0" role="region" aria-label="…"> */
.table-scroll table { min-width: 100%; width: max-content; }

/* ---------- marketing: feature rows ---------- */
.feature {
  display: grid;
  gap: var(--layout-gutter);
  align-items: center;
}
@media (min-width: 60em) {
  .feature { grid-template-columns: repeat(12, minmax(0, 1fr)); }
  .feature__text  { grid-column: 1 / span 5; }
  .feature__media { grid-column: 6 / span 7; }
  .feature--flip .feature__text  { grid-column: 8 / span 5; grid-row: 1; }
  .feature--flip .feature__media { grid-column: 1 / span 7; grid-row: 1; }
}
.feature + .feature { margin-top: var(--space-section); }

/* ---------- marketing: pricing grid ---------- */
.pricing {
  --plans: 3;                                    /* set to 2–4 per page */
  display: grid;
  gap: var(--layout-gutter);
  grid-template-columns: minmax(0, 1fr);
}
@media (max-width: 59.999em) {
  .pricing { max-width: 30rem; margin-inline: auto; }
}
@media (min-width: 60em) {
  .pricing { grid-template-columns: repeat(var(--plans), minmax(0, 1fr)); }
}
```

## How to use it

- **Docs page.** Wrap it in `.container.container--shell > .docs-shell`, with the sidebar, then `<article class="article">`, then the table of contents. Anything in the article that should be wider than the text, like an image or diagram, gets class `wide`.
- **Front page.** Put each section in `.section > .container`. Feature rows use `.feature`, and the pricing cards sit inside `.pricing`.
- **Prose width.** The 68ch measure is in the `.article` font size, so it follows the 17px body text automatically.

Two limits to know about. On pages with the sidebar, the article column is usually too narrow for `wide` to add anything, so wide tables scroll inside their wrapper there. The `.table-scroll` wrapper has to be added in the markup. A Markdown pipeline will need a small plugin to insert it.
