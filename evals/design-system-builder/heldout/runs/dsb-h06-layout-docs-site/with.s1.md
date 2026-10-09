Assumptions: one brand, plain CSS, and a docs template (nav, article, TOC) alongside the marketing template. The numbers are starting points; I haven't tested them against your fonts or content.

## The rules

| Decision | Value | Why |
|---|---|---|
| Breakpoints (3) | 40rem (640), 64rem (1024), 80rem (1280) | Phone → tablet → laptop. Layouts change only at these. |
| Page gutter | `clamp(1rem, .5rem + 2.5vw, 2rem)` | 16px on phones, 32px on desktop. Fluid, so no breakpoint is needed. |
| Grid gap | `clamp(1rem, .5rem + 2vw, 1.5rem)` | One gap for every card grid. |
| Reading measure | `66ch` at body size (17px) | About 620px, which is 60–75 characters per line. |
| Content width | `72rem` (1152px) | Feature rows and the pricing grid. |
| Wide width | `80rem` (1280px) | Full-width code blocks and tables in marketing and long-form pages. Also the docs shell width. |
| Docs article column | `48rem` (768px) | Prose stays at 66ch inside it. Code and tables use the full column, about 88 monospace columns at 14px. |
| Docs nav / TOC | 15rem / 13rem | Nav appears at 64rem and above. TOC appears at 80rem and above. |
| Column counts | 1 below 40rem, 2 from 40rem, 3 or 4 from 64rem | Set per grid with `--cols-md` and `--cols-lg`. |
| Above 80rem | Nothing grows | Content stays centered, and only backgrounds go full-bleed. A big monitor gets margins. |

Only the reading measure is a text-width rule. Everything else is a container width, and prose never exceeds 66ch whichever page it is on.

## CSS

```css
:root {
  --measure: 66ch;
  --width-content: 72rem;
  --width-wide: 80rem;
  --width-docs-main: 48rem;
  --width-nav: 15rem;
  --width-toc: 13rem;

  --gutter: clamp(1rem, 0.5rem + 2.5vw, 2rem);
  --grid-gap: clamp(1rem, 0.5rem + 2vw, 1.5rem);
  --section-space: clamp(3rem, 2rem + 5vw, 6rem);

  --text-body: 1.0625rem;
}

/* ---------- Page grid: prose < content < wide < full ---------- */
.page {
  --content-extra: calc((var(--width-content) - var(--measure)) / 2);
  --wide-extra: calc((var(--width-wide) - var(--width-content)) / 2);

  font-size: var(--text-body); /* so ch resolves at body size */
  display: grid;
  grid-template-columns:
    [full-start] minmax(var(--gutter), 1fr)
    [wide-start] minmax(0, var(--wide-extra))
    [content-start] minmax(0, var(--content-extra))
    [prose-start] min(var(--measure), 100% - 2 * var(--gutter))
    [prose-end] minmax(0, var(--content-extra))
    [content-end] minmax(0, var(--wide-extra))
    [wide-end] minmax(var(--gutter), 1fr)
    [full-end];
}
.page > * { grid-column: prose; min-width: 0; }
.page > .content { grid-column: content; }
.page > .wide    { grid-column: wide; }
.page > .full    { grid-column: full; }

.prose { font-size: var(--text-body); line-height: 1.65; }
.prose > :where(p, ul, ol, blockquote) { max-width: var(--measure); }
.measure-narrow { max-width: 45ch; } /* hero subheads, feature copy */

.section { padding-block: var(--section-space); }

/* ---------- Card grid (pricing, features, logos) ---------- */
.grid {
  display: grid;
  gap: var(--grid-gap);
  grid-template-columns: repeat(var(--cols, 1), minmax(0, 1fr));
}
@media (min-width: 40rem) { .grid { --cols: var(--cols-md, 2); } }
@media (min-width: 64rem) { .grid { --cols: var(--cols-lg, 3); } }

/* 3 tiers: stack until 64rem (avoids a 2+1 orphan). 4 tiers: 2x2 then 4. */
.grid--pricing-3 { --cols-md: 1; --cols-lg: 3; }
.grid--pricing-4 { --cols-md: 2; --cols-lg: 4; }

/* ---------- Feature row ---------- */
.feature-row { display: grid; gap: var(--grid-gap); align-items: center; }
@media (min-width: 64rem) {
  .feature-row { grid-template-columns: 1fr 1fr; gap: calc(var(--grid-gap) * 2); }
  .feature-row--flip > :first-child { order: 2; }
}

/* ---------- Code and tables: scroll inside, never wrap or blow out ---------- */
pre {
  overflow-x: auto;
  white-space: pre;
  tab-size: 2;
  font-size: 0.875rem;
  max-width: 100%;
}
.table-scroll { overflow-x: auto; max-width: 100%; } /* add tabindex="0" in markup */
.table-scroll table { min-width: 100%; width: max-content; }

/* In .page layouts, opt long code and tables out to the wide column: */
.page > :is(pre, .table-scroll) { grid-column: wide; }

/* ---------- Docs shell: nav | article | TOC ---------- */
.docs {
  --docs-gap: 2rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: var(--docs-gap);
  padding-inline: var(--gutter);
  max-width: calc(var(--width-wide) + 2 * var(--gutter));
  margin-inline: auto;
}
.docs-nav, .docs-toc { display: none; }  /* nav becomes a disclosure under 64rem */

@media (min-width: 64rem) {
  .docs { grid-template-columns: var(--width-nav) minmax(0, var(--width-docs-main)); }
  .docs-nav { display: block; position: sticky; top: 1rem; align-self: start; }
}
@media (min-width: 80rem) {
  .docs { grid-template-columns: var(--width-nav) minmax(0, var(--width-docs-main)) var(--width-toc); }
  .docs-toc { display: block; position: sticky; top: 1rem; align-self: start; }
}
/* Docs article: prose keeps the measure, code and tables take the full column. */
.docs main { min-width: 0; }
```

## Markup

```html
<!-- Marketing -->
<main class="page">
  <h1>…</h1>
  <p class="measure-narrow">…</p>
  <section class="content section">
    <div class="grid grid--pricing-3">…cards…</div>
  </section>
  <div class="full" style="background: …">…</div>
</main>

<!-- Docs: nav, article, TOC -->
<div class="docs">
  <nav class="docs-nav">…</nav>
  <main class="prose">…</main>
  <aside class="docs-toc">…</aside>
</div>
```

## Notes

- Media queries can't read custom properties, so the three breakpoints appear as literals. Keep them identical everywhere.
- On long-form pages that use `.page`, code blocks and tables go out to the wide column. In docs they use the 48rem article column, and anything wider scrolls inside its own box. Check your widest real table against that column before shipping.
