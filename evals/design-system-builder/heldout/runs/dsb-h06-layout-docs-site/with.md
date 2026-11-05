**Assumption:** this is a greenfield web site with one brand and no existing layout tokens. I haven't run the CSS in a browser.

## The rules

| Rule | Phone | Tablet | Desktop | Large |
|---|---|---|---|---|
| Breakpoint | base | ≥ 40rem (640) | ≥ 64rem (1024) | ≥ 80rem (1280) |
| Grid columns | 4 | 8 | 12 | 12 |
| Gutter | 16px | 24px | 32px | 32px |
| Page margin | `clamp(1rem, 4vw, 2rem)` (16 to 32px) | same | same | same |

- **Three breakpoints, no more.** They change the grid (4, 8, 12 columns) and the docs shell. At 80rem the docs page gains a table of contents. Nothing else changes after that.
- **Reading measure: `68ch`.**
  - It applies to article text, set at 17px with a 1.65 line height.
  - Marketing lead paragraphs use `56ch`. Card copy uses `45ch`.
  - Headings use `text-wrap: balance`.
- **Wide container: `72rem` (1152px) of content.** The front page uses it for feature rows and the pricing grid.
- **Docs shell:** a 16rem sidebar, the 68ch article, then a 14rem table of contents from 80rem up.
  - The shell is centered and stops growing.
  - At the 64rem boundary it needs about 1008px (256 sidebar + 48 gap + about 640 article + 64 margins), so it fits.
- **Large monitors:** nothing stretches. At ≥ 120rem (1920) the root font size goes to 18px, so every rem and ch width scales together.
- **Code blocks and tables** never exceed the article column. They scroll horizontally and don't wrap. On phones they run edge to edge.
- **One span default.** A column spans 4. That is the full row on a 4-column grid, half on 8, and a third on 12. So "a card" is 1, 2 or 3 across with no per-breakpoint code.

## CSS

```css
:root {
  /* measure and widths */
  --w-prose: 68ch;
  --w-wide: 72rem;
  --w-card-text: 45ch;
  --w-lead: 56ch;
  --w-sidebar: 16rem;
  --w-toc: 14rem;

  /* grid (values step up at the breakpoints below) */
  --cols: 4;
  --gutter: 1rem;
  --page-margin: clamp(1rem, 4vw, 2rem);

  /* section rhythm */
  --section-space: clamp(3rem, 8vw, 6rem);
}

/* Media queries can't read custom properties, so keep these literals in sync:
   40rem = tablet, 64rem = desktop, 80rem = large, 120rem = huge. */
@media (min-width: 40rem) { :root { --cols: 8;  --gutter: 1.5rem; } }
@media (min-width: 64rem) { :root { --cols: 12; --gutter: 2rem; } }
@media (min-width: 120rem) { html { font-size: 112.5%; } }

body { font-size: 1.0625rem; line-height: 1.65; }

/* ---------- containers ---------- */
.container,
.container--prose {
  width: 100%;
  margin-inline: auto;
  padding-inline: var(--page-margin);
  max-width: calc(var(--w-wide) + 2 * var(--page-margin));
}
.container--prose {
  max-width: calc(var(--w-prose) + 2 * var(--page-margin));
}
.section { padding-block: var(--section-space); }

h1, h2, h3 { text-wrap: balance; }
.lead { max-width: var(--w-lead); }
.card p { max-width: var(--w-card-text); }

/* ---------- grid ---------- */
.grid {
  display: grid;
  grid-template-columns: repeat(var(--cols), minmax(0, 1fr));
  gap: var(--gutter);
}
/* default span 4 = 1 / 2 / 3 across at 4 / 8 / 12 columns */
.col { grid-column: span var(--span, 4); }
@media (min-width: 40rem) {
  .col { grid-column: span var(--span-sm, var(--span, 4)); }
}
@media (min-width: 64rem) {
  .col { grid-column: span var(--span-md, var(--span-sm, var(--span, 4))); }
}

/* Usage
   Pricing, 3 tiers: <div class="grid"><div class="col">…</div> ×2
     <div class="col" style="--span-sm:8">…</div></div>   (no orphan on tablet)
   Feature row:   text  style="--span:4; --span-sm:8; --span-md:5"
                  media style="--span:4; --span-sm:8; --span-md:7"
   Alternate rows with order, not with different markup. */

/* ---------- docs shell ---------- */
.docs {
  display: grid;
  gap: var(--gutter);
  padding-inline: var(--page-margin);
  padding-block: 2rem;
}
.docs > * { min-width: 0; }              /* lets code and tables scroll, not blow out the grid */
.docs__sidebar, .docs__toc { display: none; }  /* sidebar becomes a drawer below 64rem */

@media (min-width: 64rem) {
  .docs {
    grid-template-columns: var(--w-sidebar) minmax(0, var(--w-prose));
    column-gap: 3rem;
    justify-content: center;
  }
  .docs__sidebar { display: block; position: sticky; top: 4rem; align-self: start; }
}
@media (min-width: 80rem) {
  .docs { grid-template-columns: var(--w-sidebar) minmax(0, var(--w-prose)) var(--w-toc); }
  .docs__toc { display: block; position: sticky; top: 4rem; align-self: start; }
}

/* ---------- article content ---------- */
.prose > * + * { margin-top: 1.25em; }
.prose :is(h2, h3) { scroll-margin-top: 5rem; }
.prose :not(pre) > code { overflow-wrap: anywhere; }

.prose pre,
.table-wrap {
  overflow-x: auto;
  max-width: 100%;
  -webkit-overflow-scrolling: touch;
}
.prose pre {
  font-size: 0.875rem;
  line-height: 1.6;
  tab-size: 2;
  white-space: pre;
}
.table-wrap table { width: max-content; min-width: 100%; }

/* phones: code and tables go edge to edge */
@media (max-width: 39.999rem) {
  .prose pre, .table-wrap {
    margin-inline: calc(-1 * var(--page-margin));
    border-radius: 0;
  }
  .prose pre { padding-inline: var(--page-margin); }
}
```

Wrap every wide table in `<div class="table-wrap">` in your markdown renderer.

- **Trade-off:** wide tables scroll inside the 68ch column instead of breaking out into the margins. That keeps one rule and no collision with the table of contents. If a few tables really need more room, add a `.table-wrap--bleed` that spans the full docs width. Do that only after a second real case turns up.
- **Next step:** check a long code line and a 6-column table at 360px, 1024px and 1440px. Those are the widths where the shell changes.
