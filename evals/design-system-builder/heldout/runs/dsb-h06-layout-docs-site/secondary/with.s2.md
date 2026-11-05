**Recommendation:** one shell (1280px max), one gutter and gap scale that grows with the viewport, one reading measure (68ch), and three breakpoints (40rem, 64rem, 80rem). Wide blocks (code, tables, wide figures) break out to 960px. Big monitors get more whitespace, not wider lines.

## Numbers

| Token | Value | Notes |
|---|---|---|
| `--page-max` | 1280px | Outer container. Never wider, on any screen. |
| `--wide-max` | 960px | Code blocks, tables, wide figures. |
| `--measure` | 68ch | About 66–72 characters per line at 17px body text. |
| `--body-size` | 17px (1.0625rem) | Body text at every width. Leading 1.6. |
| `--gutter` | 16px → 48px (`4vw`, clamped) | Side padding. |
| `--gap` | 16px → 32px (`2.5vw`, clamped) | Grid and column gap. |
| `--card-min` | 256px | Minimum card width for auto grids. Gives at most 4 columns at 1280. |
| `--sidebar` | 240px | Docs nav, shown at 1024px and up. |

Breakpoints (rem, so they respond to browser text zoom):

| Range | Layout |
|---|---|
| < 40rem (<640px), phone | One column. Docs nav becomes a drawer. |
| 40rem–64rem (640–1023px), tablet | Grids 2 columns. Text stays at measure. |
| 64rem–80rem (1024–1279px), laptop | Docs sidebar appears. Feature rows go 2-up. Grids 3 columns. |
| ≥ 80rem (≥1280px), desktop and monitors | Container capped at 1280. Grids 4 columns. |

## CSS

```css
/* 1. Tokens */
:root {
  --page-max: 80rem;                      /* 1280px */
  --wide-max: 60rem;                      /* 960px: code, tables, wide figures */
  --measure: 68ch;                        /* reading column */
  --sidebar: 15rem;                       /* 240px docs nav */
  --gutter: clamp(1rem, 4vw, 3rem);       /* 16px → 48px */
  --gap: clamp(1rem, 2.5vw, 2rem);        /* 16px → 32px */
  --card-min: 16rem;                      /* 256px */
  --body-size: 1.0625rem;                 /* 17px */
  --body-leading: 1.6;
}

/* 2. Page shell: every page uses this */
.container {
  box-sizing: border-box;
  width: 100%;
  max-width: var(--page-max);
  margin-inline: auto;
  padding-inline: var(--gutter);
}

/* 3. Card grids (features, pricing) */
.grid {
  display: grid;
  gap: var(--gap);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, var(--card-min)), 1fr));
}

/* Pricing with a fixed tier count: explicit columns so the 4th tier never orphans */
.grid--tiers {
  grid-template-columns: 1fr;
}
@media (min-width: 40rem) {
  .grid--tiers { grid-template-columns: repeat(2, 1fr); }
}
@media (min-width: 80rem) {
  .grid--tiers { grid-template-columns: repeat(4, 1fr); }
}

/* 4. Feature rows: stacked, then side by side */
.feature {
  display: grid;
  gap: var(--gap);
  align-items: center;
}
@media (min-width: 64rem) {
  .feature { grid-template-columns: 1fr 1fr; }
}

/* 5. Article: text at measure, blocks that need room break out to wide-max */
.article {
  display: grid;
  grid-template-columns:
    minmax(0, 1fr)
    min(var(--measure), 100%)
    minmax(0, 1fr);
  font-size: var(--body-size);
  line-height: var(--body-leading);
}
.article > * {
  grid-column: 2;
}
.article > pre,
.article > table,
.article > figure,
.article > .wide {
  grid-column: 1 / -1;
  justify-self: center;
  width: min(var(--wide-max), 100%);
}
.article pre,
.article table {
  overflow-x: auto;          /* scroll inside the block, never the page */
  max-width: 100%;
}
.article table {
  display: block;
}

/* 6. Docs shell: sidebar + main, sidebar from 1024px */
.docs {
  display: grid;
  gap: var(--gap);
}
@media (min-width: 64rem) {
  .docs {
    grid-template-columns: var(--sidebar) minmax(0, 1fr);
  }
}
.docs-main {
  min-width: 0;              /* lets wide blocks scroll instead of pushing the layout */
}
```

Usage: wrap each page in `.container`. Put marketing grids in `.grid` (or `.grid--tiers` for a fixed tier count). Put article HTML in `.article`, and docs pages in `.docs` with `.docs-main` holding the `.article`.

## Notes

- **Measure:** 68ch depends on the body font. If you change the font or `--body-size`, check that the line length still lands around 66–72 characters.
- **Big monitors:** the container stays at 1280px, so the page doesn't widen past it. If the marketing hero needs a full-bleed background, bleed the background color, not the content.
- **Docs main column:** on a wide screen the 68ch article sits centered inside the remaining space. If you want it left-aligned next to the sidebar, that's a one-line change to `.docs-main .article`.
- **Not verified:** I haven't seen your existing stylesheet or markup, so the class names here may need to match what you already use. I haven't rendered any of this. Check it at 375, 768, 1024, 1440 and 1920px, and confirm that no page scrolls horizontally and the pricing grid never shows 3 tiers plus an orphan.
