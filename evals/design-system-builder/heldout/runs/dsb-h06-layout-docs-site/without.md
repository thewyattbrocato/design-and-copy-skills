# One layout system for docs and marketing

The same wrapper, gutter, and grid serve both. Docs and marketing differ only in what goes inside the wrapper. The big-monitor strategy is to stop growing the page. Everything is in `rem`, so the layout scales by bumping the root font size, not by getting wider.

## The numbers

| Token | Value | Why |
|---|---|---|
| Page wrapper | `80rem` (1280px) | Holds a 4-up pricing grid and the docs 3-column shell. It doesn't grow on a 27" or 32" display. |
| Gutter | `clamp(1rem, 4vw, 2rem)` | 16px on phones, 32px from about 800px up. |
| Breakpoints | 40em (640), 56.25em (900), 70em (1120), 112em (1792) | Four is enough. Use `em` so they respect user font size. |
| Prose size / leading | 17px (1.0625rem) / 1.65 | Comfortable for long reading. |
| Reading measure | `68ch` | Inside the 60–75 character range. It's set on the prose element so `ch` uses the prose font. |
| Docs shell | `15rem` sidebar, fluid article, `13rem` TOC, `2.5rem` gaps | At 1280px the article column is about 43rem (688px), which fits a 68ch measure with room for code. |
| Grid gap | `1.5rem` (`2rem` from 900px up) | |
| Section padding | `clamp(3rem, 8vw, 6rem)` | |
| Root size at ≥1792px | `112.5%` (18px) | The wrapper becomes 1440px effective and everything scales together. |

Behavior by breakpoint:

- **Below 900px:** the sidebar becomes a drawer (you'll need to build that) and the TOC is hidden.
- **900–1120px:** sidebar and article.
- **1120px and up:** sidebar, article, and TOC.
- **Pricing grid:** 1 column, then 2 from 640px, then 4 from 1120px (or 3 with `--3`).
- **Feature rows:** stacked below 900px, then a 2-column split with alternating sides.
- **Code blocks and tables:** they fill the article column, not the 68ch measure. They scroll horizontally inside their own box. On phones they bleed to the screen edges.

## CSS

```css
:root {
  --wrap: 80rem;
  --gutter: clamp(1rem, 4vw, 2rem);
  --gap: 1.5rem;
  --section-y: clamp(3rem, 8vw, 6rem);
  --measure: 68ch;
  --sidebar: 15rem;
  --toc: 13rem;
  --shell-gap: 2.5rem;
}

@media (min-width: 56.25em) { :root { --gap: 2rem; } }
@media (min-width: 112em)   { html { font-size: 112.5%; } }

/* ---------- Wrapper ---------- */
.wrap {
  width: 100%;
  max-width: calc(var(--wrap) + 2 * var(--gutter));
  margin-inline: auto;
  padding-inline: var(--gutter);
}
.section { padding-block: var(--section-y); }

/* Grid children must be allowed to shrink, or code/tables blow out the layout */
.wrap *, .docs-shell > * { min-width: 0; }

/* ---------- Generic grid (feature cards, etc.) ---------- */
.grid {
  display: grid;
  gap: var(--gap);
  grid-template-columns: 1fr;
}
@media (min-width: 40em)  { .grid--2, .grid--3, .grid--4 { grid-template-columns: repeat(2, 1fr); } }
@media (min-width: 70em)  {
  .grid--3 { grid-template-columns: repeat(3, 1fr); }
  .grid--4 { grid-template-columns: repeat(4, 1fr); }
}

/* ---------- Pricing: same grid, 1 → 2 → N columns ---------- */
.pricing { composes: grid; }              /* or add both classes in markup */
.pricing {
  display: grid; gap: var(--gap);
  grid-template-columns: 1fr;
}
@media (min-width: 40em) { .pricing { grid-template-columns: repeat(2, 1fr); } }
@media (min-width: 70em) { .pricing { grid-template-columns: repeat(4, 1fr); }
                           .pricing--3 { grid-template-columns: repeat(3, 1fr); } }

/* ---------- Feature rows: text + media, alternating ---------- */
.feature-row {
  display: grid; gap: var(--gap);
  grid-template-columns: 1fr;
  align-items: center;
}
.feature-row__text { max-width: 34rem; }
@media (min-width: 56.25em) {
  .feature-row { grid-template-columns: 1fr 1fr; gap: 4rem; }
  .feature-row:nth-child(even) .feature-row__media { order: -1; }
}

/* ---------- Docs shell ---------- */
.docs-shell { display: block; }
@media (min-width: 56.25em) {
  .docs-shell {
    display: grid;
    grid-template-columns: var(--sidebar) minmax(0, 1fr);
    column-gap: var(--shell-gap);
  }
}
@media (min-width: 70em) {
  .docs-shell {
    grid-template-columns: var(--sidebar) minmax(0, 1fr) var(--toc);
  }
}
.docs-sidebar, .docs-toc {
  position: sticky; top: 1rem;
  align-self: start;
  max-height: calc(100vh - 2rem);
  overflow-y: auto;
}
.docs-toc { display: none; }
@media (min-width: 70em) { .docs-toc { display: block; } }

/* ---------- Prose: the reading measure ---------- */
.prose {
  font-size: 1.0625rem;
  line-height: 1.65;
}
.prose > :where(p, ul, ol, blockquote, h1, h2, h3, h4, dl) {
  max-width: var(--measure);
}
.prose :where(h1, h2, h3, h4) { line-height: 1.2; scroll-margin-top: 5rem; }
.prose :where(h2) { margin-top: 2.5em; }
.prose :where(h3) { margin-top: 2em; }
.prose :where(p, ul, ol, pre, .table-scroll) { margin-block: 1em; }
.prose :where(code) { overflow-wrap: anywhere; }       /* long inline identifiers */

/* ---------- Code blocks: full column width, scroll inside ---------- */
.prose pre {
  max-width: 100%;
  overflow-x: auto;
  padding: 1rem 1.25rem;
  font-size: 0.875rem;
  line-height: 1.6;
  tab-size: 2;
  border-radius: 0.5rem;
  -webkit-overflow-scrolling: touch;
}
.prose pre code { overflow-wrap: normal; white-space: pre; }

/* ---------- Tables: wrap in .table-scroll ---------- */
.table-scroll {
  max-width: 100%;
  overflow-x: auto;
}
.table-scroll > table {
  width: max-content;      /* natural width, never squashed */
  min-width: 100%;         /* but fill the column when narrow */
  border-collapse: collapse;
  font-size: 0.9375rem;
}
.table-scroll :where(th, td) { padding: 0.5rem 0.75rem; text-align: left; vertical-align: top; }
.table-scroll td:not(:has(code)) { max-width: 28rem; }  /* stop one cell eating the table */

/* ---------- Phones: code and tables bleed to the screen edge ---------- */
@media (max-width: 39.99em) {
  .prose :where(pre, .table-scroll) {
    margin-inline: calc(-1 * var(--gutter));
    max-width: none;
    border-radius: 0;
  }
  .prose pre { padding-inline: var(--gutter); }
}
```

## Notes on the choices

- **Why 68ch and not a fixed pixel width:** the measure should follow the font. Put it on `.prose` children, because `ch` is computed from the element's own font size. If you set it on a wrapper with a different font size, the measure will be wrong.
- **Why code isn't capped at the measure:** at 0.875rem monospace, 68ch of prose is about 75 code characters, which is too tight. Letting `pre` use the full article column (about 688px, or 80+ characters) cuts horizontal scrolling a lot.
- **Why `minmax(0, 1fr)` and `min-width: 0`:** without them, one long `pre` or wide table makes the grid track grow to its content, and the whole page scrolls sideways. This is the most common bug in this kind of layout.
- **Marketing pages:** use `.wrap` and `.section` only, with no docs shell. Headlines and feature copy should be capped at `34rem` or `40ch`, not `68ch`.
- **Changes to the markup:** you need a `.table-scroll` wrapper around each `<table>`. A remark/rehype plugin or an MDX `table` component override can add it. The `.pricing { composes: grid; }` line is only a CSS-modules idiom, so delete it if you aren't using modules. The standalone block below it is complete on its own.
- **Not tested:** I haven't rendered this. Check it at 360, 768, 1024, 1280, and 2560px, with the longest code block and widest table you have.
