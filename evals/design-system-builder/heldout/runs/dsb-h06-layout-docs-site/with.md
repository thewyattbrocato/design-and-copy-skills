I assumed one brand, plain CSS, no existing layout CSS to reconcile, and about three pricing tiers.

## The rules

| Decision | Value |
|---|---|
| Breakpoints (3, `min-width`) | 640px (`40rem`), 1024px (`64rem`), 1440px (`90rem`) |
| Columns | 4 below 640, 8 from 640, 12 from 1024 (feature rows only) |
| Page padding and gutter (one token) | 16px, then 24px at 640, then 32px at 1024. It does not change after that. |
| Reading measure | `65ch` (about 70–75 characters). It is the only width for running text. |
| Wide width | `75rem` (1200px). Marketing sections, code, tables and figures use it. |
| Shell cap | `90rem` (1440px). Beyond that, everything centers and stops growing. |
| Docs shell | sidebar 260px from 1024. TOC 220px from 1440. Below 1024 the sidebar is a drawer. |
| Pricing grid | cards at least 272px wide, 1 column on phone, 2 on tablet, 3 or 4 on desktop |
| Feature rows | stacked below 1024. At 1024 and up, text is 5 of 12 columns, media is 6, with 1 empty between. |

Docs and marketing use the same three-width system: **content** (65ch), **wide** (up to 1200px) and **full** (edge to edge). Articles put prose in content and let code, tables and figures break out to wide. Marketing puts sections in wide and keeps headlines and ledes to a narrower measure. In the docs the main column is already narrower than 1200px, so wide shrinks to fit it. Code and tables there get about 95–100 monospace characters at 1440px without a second set of rules.

## CSS

```css
/* ---- tokens ---- */
:root {
  --w-prose: 65ch;      /* reading measure */
  --w-wide: 75rem;      /* 1200px: code, tables, marketing sections */
  --w-shell: 90rem;     /* 1440px: docs shell cap */
  --space-page: 1rem;   /* page padding and gutter, one token */
  --measure-lede: 52ch;
  --measure-head: 18ch;
}
@media (min-width: 40rem) { :root { --space-page: 1.5rem; } }
@media (min-width: 64rem) { :root { --space-page: 2rem; } }

/* ---- the one grid: full / wide / content lines ---- */
.page-grid {
  font-size: 1rem; /* ch in the tracks resolves against this element's font */
  display: grid;
  grid-template-columns:
    [full-start] minmax(var(--space-page), 1fr)
    [wide-start] minmax(0, calc((var(--w-wide) - var(--w-prose)) / 2))
    [content-start] min(var(--w-prose), 100% - 2 * var(--space-page))
    [content-end] minmax(0, calc((var(--w-wide) - var(--w-prose)) / 2))
    [wide-end] minmax(var(--space-page), 1fr)
    [full-end];
}
.page-grid > *            { grid-column: content; }
.page-grid > .wide        { grid-column: wide; }
.page-grid > .full        { grid-column: full; }
.page-grid--wide > *      { grid-column: wide; }   /* marketing sections */

/* ---- articles ---- */
.prose { line-height: 1.65; }
.prose > pre,
.prose > .table-wrap,
.prose > figure { grid-column: wide; }
.prose pre,
.table-wrap { overflow-x: auto; max-width: 100%; }
.prose pre { tab-size: 2; }
.table-wrap { overscroll-behavior-x: contain; }
.table-wrap table { min-width: 100%; width: max-content; }

/* ---- docs shell ---- */
.docs-shell {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  max-width: var(--w-shell);
  margin-inline: auto;
}
@media (min-width: 64rem) {
  .docs-shell { grid-template-columns: 16.25rem minmax(0, 1fr); }   /* 260 */
}
@media (min-width: 90rem) {
  .docs-shell { grid-template-columns: 16.25rem minmax(0, 1fr) 13.75rem; } /* 260 / 220 */
}
.docs-shell > main { min-width: 0; } /* lets code and tables scroll instead of blowing out the grid */

/* ---- marketing ---- */
.lede { max-width: var(--measure-lede); }
.hero h1 { max-width: var(--measure-head); text-wrap: balance; }

.feature-row {
  display: grid;
  gap: var(--space-page);
  grid-template-columns: minmax(0, 1fr);
}
.feature-row > .copy { max-width: 52ch; }
@media (min-width: 64rem) {
  .feature-row {
    grid-template-columns: repeat(12, minmax(0, 1fr));
    align-items: center;
  }
  .feature-row > .copy  { grid-column: 1 / 6; }    /* 5 cols */
  .feature-row > .media { grid-column: 7 / 13; }   /* 6 cols, col 6 empty */
  .feature-row.is-reversed > .copy  { grid-column: 8 / 13; grid-row: 1; }
  .feature-row.is-reversed > .media { grid-column: 1 / 7;  grid-row: 1; }
}

.pricing-grid {
  display: grid;
  gap: var(--space-page);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 17rem), 1fr));
}
```

Usage:

```html
<!-- article -->
<main><article class="page-grid prose">
  <h1>…</h1><p>…</p>
  <pre><code>…</code></pre>
  <div class="table-wrap"><table>…</table></div>
</article></main>

<!-- marketing -->
<section class="page-grid page-grid--wide">
  <div class="pricing-grid">…</div>
</section>
```

## Notes

- **Pricing at tablet:** `auto-fit` gives 2 columns at tablet and 3 at desktop, so three tiers leave an orphan on a second row at 640–1023. If you have exactly three, add `@media (min-width:40rem){.pricing-grid{grid-template-columns:repeat(3,1fr)}}`. Cards then go to about 190px at 640. I'd keep the stacked 1 or 2 columns instead.
- **TOC at 1440:** it appears only at 1440. At 1280 the main column is 1020px, which leaves room for prose but not for a TOC without squeezing it. A fourth breakpoint at 1280 would show it sooner. I held to three.
- **Table wrappers:** tables need the `.table-wrap` div. Making `<table>` itself scroll breaks its table semantics.
