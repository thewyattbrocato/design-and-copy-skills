Use three breakpoints, one page frame, and two content widths. Every page uses the same tokens, so the front page and the articles line up.

## The numbers

| Token | Value | Used for |
|---|---|---|
| Breakpoints | 600px, 900px, 1200px | Layout changes only. Typography also steps at 900px. |
| Page padding | 16px → 24px (600) → 32px (900) | Side margin of the page frame |
| Column gap | 16px → 24px (600) | Gap between grid columns and cards |
| Page frame | 1200px max | Marketing grid and front page |
| Article frame | 960px max | Article body, code blocks, wide tables |
| Reading measure | 68ch max | Paragraphs, lists, headings in articles and feature copy |
| Body text | 16px → 18px (900) | Line-height 1.65 → 1.6 |
| Grid | 12 columns, `minmax(0, 1fr)` | Marketing sections |
| Pricing | 1 col → 2 col (600) → 3 col (900) | Up to 3 tiers; see note below |

Why these values:
- **68ch** is in the 45–75 character range that most readers handle comfortably. Phones never reach it because the viewport is narrower, which is correct.
- **960px** holds about 68ch of prose with room for a code block or table beside it, without making lines longer than the prose.
- **1200px** caps the marketing grid so a 2560px monitor shows centered content, not stretched cards. Don't scale text up on big screens. Center the frame and stop there.
- **`minmax(0, 1fr)`** keeps a wide `<pre>` or table from forcing its column wider than the grid.

## CSS

```css
:root {
  /* Breakpoints (documented here; repeated in the @media rules below) */
  /* sm 600px · md 900px · lg 1200px */

  --page-pad: 16px;
  --col-gap: 16px;
  --body-size: 1rem;      /* 16px */
  --body-lh: 1.65;

  --w-prose: 68ch;        /* reading measure */
  --w-article: 960px;     /* article frame: code, tables, figures */
  --w-page: 1200px;       /* marketing frame */
}

@media (min-width: 600px) {
  :root { --page-pad: 24px; --col-gap: 24px; }
}

@media (min-width: 900px) {
  :root { --page-pad: 32px; --body-size: 1.125rem; /* 18px */ --body-lh: 1.6; }
}

/* ---------- Frames ---------- */

.page {                               /* marketing: front page, pricing, feature rows */
  width: min(100% - 2 * var(--page-pad), var(--w-page));
  margin-inline: auto;
}

.article {                            /* documentation articles */
  width: min(100% - 2 * var(--page-pad), var(--w-article));
  margin-inline: auto;
  font-size: var(--body-size);
  line-height: var(--body-lh);
}

/* Prose is capped at the reading measure and centered in the article frame. */
.article > * {
  max-width: var(--w-prose);
  margin-inline: auto;
}

/* Things that need room sit at the full article width. */
.article > .wide,
.article > pre,
.article > .table-scroll,
.article > figure {
  max-width: 100%;
}

/* ---------- Code and tables ---------- */

pre {
  overflow-x: auto;                   /* scroll code, never wrap it */
  white-space: pre;
  font-size: 0.875rem;
  padding: 1rem;
}

.table-scroll {                       /* wrap every table in a markdown article */
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

.table-scroll table {
  width: max-content;                 /* keep natural width, scroll the wrapper */
  min-width: 100%;
  border-collapse: collapse;
}

/* ---------- Marketing grid ---------- */

.grid-12 {
  display: grid;
  grid-template-columns: repeat(12, minmax(0, 1fr));
  column-gap: var(--col-gap);
  row-gap: var(--col-gap);
}

.grid-12 > * {
  grid-column: 1 / -1;                /* full width on phones */
}

/* Feature rows: stacked on phones, copy and media side by side from 900px. */
.feature-row {
  display: grid;
  gap: var(--col-gap);
}

@media (min-width: 900px) {
  .feature-row {
    grid-template-columns: repeat(12, minmax(0, 1fr));
    align-items: center;
  }
  .feature-row > .copy   { grid-column: 1 / span 5; }
  .feature-row > .media  { grid-column: 7 / span 6; }
  .feature-row.reverse > .copy  { grid-column: 8 / span 5; }
  .feature-row.reverse > .media { grid-column: 1 / span 6; }
}

.feature-row .copy {
  max-width: var(--w-prose);
}

/* Pricing: 1 → 2 → 3 columns. */
.pricing {
  display: grid;
  gap: var(--col-gap);
  grid-template-columns: minmax(0, 1fr);
}

@media (min-width: 600px) {
  .pricing { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}

@media (min-width: 1200px) {
  .pricing { grid-template-columns: repeat(3, minmax(0, 1fr)); }
}
```

## How to use it

- Wrap the front page sections in `.page`, and articles in `.article`. Use `.grid-12` or `.feature-row` inside `.page`.
- The markdown renderer should wrap every `<table>` in `<div class="table-scroll">`. Without that, a wide table pushes the whole page sideways on phones.
- Pricing with more than 3 tiers: go to 4 columns at 1200px, or use a 2×2 layout at 900px. Don't add a fourth column below 1200px, because the cards get too narrow.
- The `.wide` class is available for article content that should use the full 960px and not the prose measure.

I haven't checked this against your existing site's CSS, because this directory isn't a git repository and I didn't find any site source here. If your current stylesheet uses different breakpoints or a different frame width, change the custom properties in `:root` first. Most of the rest should follow from them. Tell me where the stylesheet lives and I can map it onto these tokens.
