# Quillmark layout rules

## The rules

| Thing | Value | Why |
|---|---|---|
| Gutter | `clamp(1rem, 0.5rem + 2.5vw, 2rem)` (16px on phones, 32px from about 600px up) | One side padding for every page |
| Reading measure | `68ch` (about 620–700px) | Inside the 60–75 character range. Applies to prose on every page. |
| Wide track (code, tables, figures) | measure + 6rem each side (about 850px) | Code fits about 95 characters at 14px, so it rarely scrolls. |
| Page max | `80rem` (1280px), `90rem` (1440px) from 1600px up | Header, footer, feature rows, pricing and the docs shell |
| Docs shell | 15rem sidebar, article, 13rem TOC, 2rem gaps | Sidebar appears at 1024px, TOC at 1280px |
| Base font | 16px, then 17px from 768px, then 18px from 1600px | Big monitors get larger type, not longer lines |
| Line height | 1.65 prose, 1.2 headings | |
| Section spacing | `clamp(3rem, 2rem + 5vw, 7rem)` | |

**Breakpoints** (rem, so they follow user zoom):

| Width | What changes |
|---|---|
| 40rem (640px) | Pricing goes to 2 columns |
| 48rem (768px) | Feature rows go to 2 columns. Font goes to 17px. |
| 64rem (1024px) | Docs sidebar appears |
| 80rem (1280px) | Docs TOC appears. Pricing goes to its full column count. |
| 100rem (1600px) | Page max goes to 90rem. Font goes to 18px. |

Two choices matter most:

- **Prose never exceeds 68ch, on any page.** Marketing copy and docs share the same text column. Only code, tables, figures, grids and heroes are allowed to be wider.
- **Pricing responds to its container, not the viewport.** It lays out correctly with or without a sidebar.

## CSS

```css
:root {
  --gutter: clamp(1rem, 0.5rem + 2.5vw, 2rem);
  --measure: 68ch;
  --breakout: 6rem;            /* extra width each side for code/tables */
  --page: 80rem;
  --section-space: clamp(3rem, 2rem + 5vw, 7rem);
}
@media (min-width: 100rem) { :root { --page: 90rem; } }

html { font-size: 100%; }
@media (min-width: 48rem)  { html { font-size: 106.25%; } }  /* 17px */
@media (min-width: 100rem) { html { font-size: 112.5%; } }   /* 18px */

body { line-height: 1.65; }
h1, h2, h3, h4 { line-height: 1.2; text-wrap: balance; scroll-margin-top: 5rem; }

/* ---------- Page container (all pages) ---------- */
.page {
  max-width: var(--page);
  margin-inline: auto;
  padding-inline: var(--gutter);
}
.section { padding-block: var(--section-space); }   /* full-bleed bands: put bg on .section, content in .page */

/* ---------- Content flow: prose / wide / full ---------- */
.flow {
  display: grid;
  justify-content: center;
  grid-template-columns:
    [wide-start] minmax(0, var(--breakout))
    [prose-start] min(100%, var(--measure)) [prose-end]
    minmax(0, var(--breakout)) [wide-end];
}
.flow > *            { grid-column: prose; }
.flow > :is(pre, figure, .table-wrap, .wide) { grid-column: wide; }
.flow > * + *        { margin-top: 1.25em; }
.flow > :is(h2, h3) { margin-top: 2em; }

/* ---------- Code & tables ---------- */
pre {
  overflow-x: auto;
  font-size: 0.875rem;
  line-height: 1.55;
  tab-size: 2;
  padding: 1rem var(--gutter);
  border-radius: 0.5rem;
}
@media (max-width: 39.99rem) {
  pre { margin-inline: calc(var(--gutter) * -1); border-radius: 0; }  /* edge to edge on phones */
}
.table-wrap { overflow-x: auto; }     /* <div class="table-wrap" tabindex="0"> around every table */
.table-wrap table { min-width: 100%; width: max-content; max-width: none; }
td, th { padding: 0.5rem 0.75rem; }
img, video, svg { max-width: 100%; height: auto; }

/* ---------- Docs shell ---------- */
.docs { display: grid; gap: 2rem; padding-block: 2rem; }
.docs > article { min-width: 0; }                 /* lets pre/tables scroll instead of blowing out the grid */
.docs aside { display: none; }
@media (min-width: 64rem) {
  .docs { grid-template-columns: 15rem minmax(0, 1fr); }
  .docs .sidebar { display: block; position: sticky; top: 4.5rem; align-self: start;
                   max-height: calc(100vh - 5rem); overflow: auto; }
}
@media (min-width: 80rem) {
  .docs { grid-template-columns: 15rem minmax(0, 1fr) 13rem; }
  .docs .toc { display: block; position: sticky; top: 4.5rem; align-self: start; }
}

/* ---------- Marketing: hero ---------- */
.hero h1 { max-width: 20ch; font-size: clamp(2.25rem, 1.5rem + 3.5vw, 4rem); }
.hero p  { max-width: var(--measure); }

/* ---------- Marketing: feature rows ---------- */
.feature { display: grid; gap: 1.5rem; align-items: center; }
.feature + .feature { margin-top: var(--section-space); }
.feature p { max-width: 55ch; }
@media (min-width: 48rem) {
  .feature { grid-template-columns: minmax(0, 1fr) minmax(0, 1.1fr); gap: 3rem; }
  .feature:nth-child(even) > :first-child { order: 2; }
}

/* ---------- Marketing: pricing (set --plans: 3 or 4 on .pricing) ---------- */
.pricing-wrap { container-type: inline-size; }
.pricing { display: grid; gap: 1.5rem; grid-template-columns: 1fr; }
@container (min-width: 36rem) { .pricing { grid-template-columns: repeat(2, 1fr); } }
@container (min-width: 60rem) { .pricing { grid-template-columns: repeat(var(--plans, 3), 1fr); } }
```

## Markup shape

```html
<!-- docs -->
<div class="page docs">
  <nav class="sidebar">…</nav>
  <article class="flow">
    <h1>…</h1><p>…</p>
    <pre>…</pre>
    <div class="table-wrap" tabindex="0"><table>…</table></div>
  </article>
  <aside class="toc">…</aside>
</div>

<!-- marketing -->
<section class="section"><div class="page hero">…</div></section>
<section class="section"><div class="page">
  <div class="feature">…</div><div class="feature">…</div>
</div></section>
<section class="section"><div class="page pricing-wrap">
  <div class="pricing" style="--plans:3">…</div>
</div></section>
```

## Notes

- **Docs article width.** At exactly 1280px with sidebar and TOC, the article column is only about 700px, so the wide track barely exceeds the prose. That's intended: code and tables get the full column. If you want more room there, raise `--page` for docs only, for example `.docs { max-width: 90rem; }`.
- **Wide tables.** They scroll inside `.table-wrap` instead of stretching the page. Keep the `tabindex="0"` so keyboard users can scroll them. Make the first column sticky if tables get really wide.
- **Pricing columns.** Pricing uses explicit column counts rather than `auto-fit`. With 4 plans, `auto-fit` leaves an orphan card at mid widths.
- **`ch` units.** `ch` resolves against the font of the element it's used on. Keep `.flow` in the body font, not in a smaller-sized wrapper.
- **Untested.** I haven't rendered this. Check it at 360, 768, 1024, 1280 and 1920px before shipping, especially the docs shell with a long code line.
