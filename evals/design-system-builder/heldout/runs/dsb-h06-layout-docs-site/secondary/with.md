Here's one system. Everything aligns to a single page container, text is capped by a measure, and wide things scroll inside themselves instead of stretching the page. I didn't have your site's source, so the class names are placeholders.

## The numbers

| Token | Value | Why |
|---|---|---|
| Body size | `clamp(1rem, 0.95rem + 0.25vw, 1.125rem)` (16 → 18px) | Grows slightly on big screens, never past 18px |
| Measure (`--measure`) | `68ch` | Roughly 65–75 characters per line, the readable range |
| Gutter | `clamp(1rem, 4vw, 2.5rem)` (16 → 40px) | Phone margin is 16px; the margin grows with the screen |
| Grid gap | `clamp(1rem, 2.5vw, 2rem)` (16 → 32px) | Matches the gutter's proportions |
| Page max (`--page-max`) | `1200px` | Marketing grid and pricing never widen past this |
| Article max (`--article-max`) | `1040px` | Code blocks and tables get this width; prose still stays at the measure |
| Breakpoints | `640px` (sm), `960px` (md) | Two breakpoints are enough for 1, 2, or 3 columns |

Custom properties can't be used inside `@media` conditions, so the breakpoints are literal values. Keep them in one comment block so they stay in sync.

## The CSS

```css
:root {
  /* Type */
  --body-size: clamp(1rem, 0.95rem + 0.25vw, 1.125rem);
  --measure: 68ch;

  /* Space */
  --gutter: clamp(1rem, 4vw, 2.5rem);
  --gap: clamp(1rem, 2.5vw, 2rem);

  /* Widths */
  --page-max: 1200px;     /* marketing + pricing */
  --article-max: 1040px;  /* docs: code, tables, figures */
}

/* Breakpoints (literal values, keep in sync with the tokens above):
   sm: 640px   md: 960px   */

body {
  font-size: var(--body-size);
}

/* Page container: every section aligns to this edge */
.container {
  width: min(100% - 2 * var(--gutter), var(--page-max));
  margin-inline: auto;
}

/* Article container: same gutter, wider cap */
.article {
  width: min(100% - 2 * var(--gutter), var(--article-max));
  margin-inline: auto;
}

/* Prose is capped at the measure and centered in the article */
.article > * {
  max-width: var(--measure);
  margin-inline: auto;
}

/* Wide blocks use the full article width */
.article > pre,
.article > .table-wrap,
.article > figure {
  max-width: var(--article-max);
}

/* Code scrolls inside its own box; it never widens the page */
pre {
  overflow-x: auto;
}

/* Tables scroll inside a wrapper instead of squashing */
.table-wrap {
  overflow-x: auto;
}
.table-wrap table {
  width: max-content;
  min-width: 100%;
  border-collapse: collapse;
}

/* Grid: feature rows and pricing share one rule.
   minmax(0, 1fr) stops a wide child (code, table) from forcing a column wider. */
.grid {
  display: grid;
  gap: var(--gap);
  grid-template-columns: minmax(0, 1fr);
}
@media (min-width: 640px) {
  .grid--features {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}
@media (min-width: 960px) {
  .grid--features,
  .grid--pricing {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}
/* Pricing stays one column below 960px. Two columns with three tiers leaves an orphan. */

/* Split sections (text + visual) */
.split {
  display: grid;
  gap: var(--gap);
  grid-template-columns: minmax(0, 1fr);
}
@media (min-width: 960px) {
  .split {
    grid-template-columns: 5fr 7fr;
  }
}
```

## Rules to follow

1. **Only the container sets page width.** Sections, grids, and images use `.container` or `.article`. Nothing else sets its own max width.
2. **Text is capped at `--measure`, never by the container.** On a phone the measure doesn't bind, because the gutter is narrower than 68ch. On a monitor it binds, and the text stays readable.
3. **Wide content scrolls inside its own box.** Code and tables use `overflow-x: auto`. The page never gets a horizontal scrollbar.
4. **Full-bleed is for hero backgrounds only.** Backgrounds can run edge to edge, but their content still uses `.container`.
5. **Grid columns use `minmax(0, 1fr)`.** Plain `1fr` lets a wide code block push the column past its share.

## Check at these widths

360, 390, 768, 1024, 1440, and 2560. At 360 and 390, nothing should scroll sideways except code and table wrappers. At 1440 and 2560, prose stays at about 680px and the page doesn't grow past 1200px for marketing or 1040px for docs.
