# Quillmark layout rules

## The numbers

| Token | Value | Why |
|---|---|---|
| Reading measure | `65ch` (about 640px at 18px) | Gives 60–75 characters per line. Docs prose and long marketing copy both use it. |
| Short copy measure | `50ch` | Hero text and feature-row copy. Short lines read better there. |
| Wide column | measure + 16rem (about 900px) | Code blocks, tables and figures. At 14px mono this fits about 105 columns, so most code lines don't scroll. |
| Page max width | `80rem` (1280px) marketing, `90rem` (1440px) docs shell | Past this, extra monitor width becomes margin. Text never scales up further. |
| Page margin | `clamp(1rem, 4vw, 4rem)` | 16px on a phone, 64px on a big screen. |
| Gutter | `clamp(1rem, 2vw, 2rem)` | |
| Body size | `clamp(1rem, 0.95rem + 0.25vw, 1.125rem)` | 16px on a phone, capped at 18px. |
| Body line-height | `1.65` prose, `1.5` code | |
| Breakpoints | `40rem` (640), `64rem` (1024), `80rem` (1280) | Only three, used by every page. |
| Docs sidebar / TOC | `16rem` / `14rem` | The sidebar is a drawer below 64rem. The TOC appears at 80rem. |
| Pricing cards | `minmax(min(100%, 17rem), 1fr)`, grid max `72rem` | Gives 1, 2, 3 or 4 columns without extra breakpoints. |

**Why these breakpoints:** at 64rem the docs sidebar (256px) plus a 640px measure plus margins just fits. At 80rem the TOC fits too. Media queries can't read custom properties, so the three values are repeated literally.

## How it fits together

Every page uses one named-line grid with three widths: `content` (the measure), `wide`, and `full`. A child picks its width with a class, and nothing sets its own `max-width`. Marketing sections use the same grid. Their backgrounds go full-bleed on the section, and the content inside still aligns with the docs.

## CSS

```css
:root {
  --measure: 65ch;
  --measure-short: 50ch;
  --wide-extra: 8rem;               /* each side; wide = measure + 16rem */
  --page-max: 80rem;
  --margin: clamp(1rem, 4vw, 4rem);
  --gutter: clamp(1rem, 2vw, 2rem);
  --sidebar: 16rem;
  --toc: 14rem;
}

html { -webkit-text-size-adjust: 100%; }
body {
  font-size: clamp(1rem, 0.95rem + 0.25vw, 1.125rem);
  line-height: 1.65;
}
h1 { font-size: clamp(2rem, 1.4rem + 2.5vw, 3.5rem); line-height: 1.1; }
h2 { font-size: clamp(1.5rem, 1.2rem + 1.2vw, 2.25rem); line-height: 1.2; }
h3 { font-size: clamp(1.2rem, 1.1rem + 0.5vw, 1.5rem); line-height: 1.3; }

/* One grid for every page: full / wide / content */
.layout {
  display: grid;
  grid-template-columns:
    [full-start]    minmax(var(--margin), 1fr)
    [wide-start]    minmax(0, var(--wide-extra))
    [content-start] min(var(--measure), 100% - 2 * var(--margin))
    [content-end]   minmax(0, var(--wide-extra))
    [wide-end]      minmax(var(--margin), 1fr)
    [full-end];
}
.layout > *      { grid-column: content; min-width: 0; }
.layout > .wide  { grid-column: wide; }
.layout > .full  { grid-column: full; }
.layout > .short { max-width: var(--measure-short); }

/* Cap marketing width without losing full-bleed backgrounds */
.layout.capped {
  grid-template-columns:
    [full-start] minmax(var(--margin), 1fr)
    [wide-start content-start]
      minmax(0, calc(var(--page-max) - 2 * var(--margin)))
    [wide-end content-end] minmax(var(--margin), 1fr)
    [full-end];
}

/* Prose */
.prose p, .prose li { max-width: var(--measure); }
.prose :is(h2, h3) { scroll-margin-top: 5rem; margin-block: 2em 0.5em; }

/* Code and tables: break out to wide, scroll inside, never wrap the page */
.prose pre {
  grid-column: wide;
  overflow-x: auto;
  font-size: 0.875rem;
  line-height: 1.5;
  tab-size: 2;
  padding: 1rem;
  border-radius: 0.5rem;
}
.prose :not(pre) > code { font-size: 0.9em; overflow-wrap: anywhere; }

.table-wrap {                 /* wrap every <table> in this */
  grid-column: wide;
  overflow-x: auto;
  overscroll-behavior-x: contain;
}
.table-wrap table { min-width: 100%; width: max-content; max-width: none; border-collapse: collapse; }
.table-wrap :is(th, td) { padding: 0.5rem 0.75rem; text-align: left; vertical-align: top; }
.table-wrap td:first-child, .table-wrap th:first-child { position: sticky; left: 0; background: var(--bg, #fff); }

img, video, svg { max-width: 100%; height: auto; }

/* Docs shell: article reuses the same grid with no side margins */
.docs { display: grid; grid-template-columns: minmax(0, 1fr); max-width: 90rem; margin-inline: auto;
        padding-inline: var(--margin); column-gap: var(--gutter); }
.docs .sidebar, .docs .toc { display: none; }
.docs article.layout { --margin: 0px; }

@media (min-width: 64rem) {
  .docs { grid-template-columns: var(--sidebar) minmax(0, 1fr); }
  .docs .sidebar { display: block; position: sticky; top: 4rem; align-self: start;
                   max-height: calc(100dvh - 4rem); overflow-y: auto; }
}
@media (min-width: 80rem) {
  .docs { grid-template-columns: var(--sidebar) minmax(0, 1fr) var(--toc); }
  .docs .toc { display: block; position: sticky; top: 4rem; align-self: start; }
}

/* Marketing: feature rows */
.feature-row { display: grid; gap: var(--gutter); align-items: center; }
@media (min-width: 64rem) {
  .feature-row { grid-template-columns: 1fr 1fr; gap: calc(var(--gutter) * 2); }
  .feature-row:nth-child(even) > :first-child { order: 2; }
}
.feature-row p { max-width: var(--measure-short); }

/* Marketing: pricing grid */
.pricing {
  display: grid;
  gap: var(--gutter);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 17rem), 1fr));
  max-width: 72rem;
  margin-inline: auto;
}
.pricing > * { display: flex; flex-direction: column; }  /* equal-height cards */
```

## Markup

```html
<!-- Docs page -->
<div class="docs">
  <nav class="sidebar">…</nav>
  <article class="layout prose">
    <h1>…</h1>
    <p>…</p>
    <pre class="wide"><code>…</code></pre>
    <div class="table-wrap"><table>…</table></div>
  </article>
  <aside class="toc">…</aside>
</div>

<!-- Marketing section -->
<section class="layout capped" style="background: var(--tint)">
  <div class="feature-row">…</div>
</section>
```

## Things to know

- **Sticky first table column:** it needs an opaque background, or scrolled text shows through. That's the `--bg` variable above. Drop that rule if your tables have a short first column.
- **Docs article on mid-size screens:** it uses the same `wide` rule, but the middle column is only about 700px at 1280px. So `wide` and `content` nearly match there, and code scrolls sooner. That's intentional. Widening the article would mean dropping the TOC.
- **Pricing with five or more tiers:** `auto-fit` wraps them unevenly. With a fixed set of 3–4 tiers it's fine.
- **Big monitors (2560px and up):** nothing scales, and the page centers with margins. If it looks sparse, raise `--page-max` for marketing only. Don't raise `--measure`.

I haven't rendered this in a browser. Check it at 360px, 768px, 1024px, 1280px and 1920px, with the longest table and the widest code block you have.
