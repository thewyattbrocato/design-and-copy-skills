## The rules

Three widths, one set of breakpoints, and one column rule for every grid.

| Token | Value | Used for |
|---|---|---|
| `--page-max` | 1280px | Outer container for marketing and docs, including gutters |
| `--wide-max` | 1080px | Code blocks, tables, figures, pricing and feature grids |
| `--measure` | 68ch (about 680px at 18px) | Running prose, headings, lists |
| `--gutter` | 16px / 24px / 40px / 48px | Side padding by breakpoint |

Breakpoints: **<640** phone, **640–1023** tablet, **1024–1439** laptop and desktop, **≥1440** large monitor. Above 1440 the layout stops growing: the container stays at 1280px and centers.

Grid: a 12-column grid with a 16px gap on phones and a 24px gap from 640px up. Items use `span 12` on phones, `span 6` on tablets, and `span 4` on desktop. Column counts are set per breakpoint, not with `auto-fit`, so rows never end with orphaned items.

Reading measure: prose is capped at 68ch. Code, tables and figures can extend to 1080px. Nothing in the page scrolls sideways except inside its own code or table box.

## CSS

```css
:root {
  /* Widths */
  --page-max: 1280px;
  --wide-max: 1080px;
  --measure: 68ch;

  /* Gutters and gaps: phone first */
  --gutter: 1rem;          /* 16px */
  --grid-gap: 1rem;        /* 16px */

  /* Type: body size steps up with the viewport */
  --text-body: 1.0625rem;  /* 17px */
  --leading-body: 1.6;
}

/* Tablet: 640px */
@media (min-width: 40rem) {
  :root {
    --gutter: 1.5rem;      /* 24px */
    --grid-gap: 1.5rem;    /* 24px */
  }
}

/* Desktop: 1024px */
@media (min-width: 64rem) {
  :root {
    --gutter: 2.5rem;      /* 40px */
    --text-body: 1.125rem; /* 18px */
    --leading-body: 1.65;
  }
}

/* Large monitor: 1440px. Container stops growing here. */
@media (min-width: 90rem) {
  :root {
    --gutter: 3rem;        /* 48px */
  }
}

*,
*::before,
*::after {
  box-sizing: border-box;
}

/* Page container: every page and section uses this */
.container {
  width: 100%;
  max-width: var(--page-max);
  margin-inline: auto;
  padding-inline: var(--gutter);
}

/* Articles: running text is capped at the measure */
.prose {
  max-width: var(--measure);
  margin-inline: auto;
  font-size: var(--text-body);
  line-height: var(--leading-body);
}

/* Wide blocks: code, tables, figures, grids */
.wide {
  width: 100%;
  max-width: var(--wide-max);
  margin-inline: auto;
}

/* Code and tables scroll inside their own box, never the page */
.wide pre,
.prose pre,
.table-scroll {
  overflow-x: auto;
}

.table-scroll {
  max-width: 100%;
}

.table-scroll table {
  width: 100%;
  min-width: 36rem; /* below this, the box scrolls */
  border-collapse: collapse;
}

/* 12-column grid */
.grid {
  display: grid;
  grid-template-columns: repeat(12, minmax(0, 1fr));
  gap: var(--grid-gap);
}

.grid > * {
  min-width: 0;          /* lets long code and text shrink instead of overflowing */
  grid-column: span 12;  /* phone: one per row */
}

@media (min-width: 40rem) {
  .grid > * { grid-column: span 6; }   /* tablet: two per row */
}

@media (min-width: 64rem) {
  .grid > * { grid-column: span 4; }   /* desktop: three per row */
}

/* Three-tier pricing and other 3-item sets: one column until desktop. */
.grid-tiers {
  max-width: var(--wide-max);
  margin-inline: auto;
}

.grid-tiers > * {
  grid-column: span 12;
}

@media (min-width: 64rem) {
  .grid-tiers > * { grid-column: span 4; }
}
```

## How the pieces fit

- **Marketing front page:** wrap sections in `.container`. Feature rows use `.grid` with 12, 6 or 4 spans. The pricing grid uses `.grid-tiers`, which is one column until 1024px and then three columns. Use `.wide` for the pricing block so the cards stop at 1080px on big monitors.
- **Articles:** body text goes in `.prose`. Code blocks, tables and figures go in `.wide`, which lets them be wider than the text column without breaking the page.
- **Tables:** wrap each table in `.table-scroll`. The 36rem `min-width` keeps columns readable, and the wrapper scrolls on phones.

## Caveats

- I haven't looked at your existing CSS, so the token names are placeholders. Map them onto whatever you already use.
- The breakpoints use `rem`, which assumes the default 16px root size. If your root size is changed, the breakpoints move with it, which is usually what you want for accessibility.
- The `span 6` rule for tablets fits feature rows well. If a row has an odd count on tablet, give the last item `grid-column: 1 / -1`.
