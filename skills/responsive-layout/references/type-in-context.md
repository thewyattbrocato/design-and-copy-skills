# Type in context

Size and measure depend on the screen's shape and the reading distance, not only its width. Load when a headline, text block or text-heavy layout must hold on short, tall, huge or far-away screens.

## Size by context

- Body text starts at the reader's default (`1rem`) on phones, laptops and desktops. Do not shrink it for density or enlarge it to fill a big monitor; a bigger screen is usually farther away, not more readable.
- Something read from across a room (wall display, kiosk, TV) needs a larger base, set once on a wrapper with a custom property, with the same rem-based components inside. Say the assumed distance.
- Tablets are held close, propped up at laptop distance, and rotated. Test both orientations; do not file them under "phone" or "desktop".
- Honor the reader's text-size setting at every context: nothing sized in px, breakpoints in em.

## Display type needs a height guard

A width-only `clamp()` fails on screens that are wide but short: a landscape phone gets a headline that fills the screen, an ultrawide short window gets an enormous one.

```css
h1 { font-size: clamp(2rem, 1.2rem + 3vmin, 3.5rem); line-height: 1.1; }
@media (max-height: 30em) { h1 { font-size: clamp(1.5rem, 1rem + 4vh, 2.5rem); } }
```

- `vmin` follows the shorter side, so the size stays stable when the device rotates. Keep a rem term in the sum and a ceiling.
- Cap the heading's width in `ch` and add `text-wrap: balance` so it breaks evenly instead of leaving one word on the last line.
- Large type takes tight leading (about 1.0 to 1.2) and a smaller block gap than body text.
- Check a landscape phone (about 40em by 20em) and a wide, short desktop window before calling it done. A hero must not push its call to action below the fold there.

## Measure guard rails

- Cap running text at `ch` (about 45 to 75). A text column that cannot reach 45ch on a narrow screen is fine; let it fill the width with `inline-size: min(100%, 65ch)` and a side padding instead of a minimum width.
- Do not set the cap on grids and wrappers, only on text elements; a card grid should still use the full width.

## Margin notes

Notes, captions and pull quotes can sit in a side margin only where the margin exists: a grid with a text track, a gap and a notes track, enabled by a container or `min-width` query. Below that, the same elements flow inline between paragraphs, visually set apart (smaller type, a rule or tint), in source order directly after the line they annotate. Do not float notes into a margin that can vanish; a note outside the viewport is lost.

## Columns

Newspaper-style columns (`column-width: 20em`, not a fixed `column-count`) only when the column height fits the viewport. On a screen shorter than the text, the reader scrolls down one column and back up to the next. Gate them with a query on both width and height, or leave one column. Never use columns on phones.

## Test matrix

Landscape phone; short desktop window; ultrawide; tablet in both orientations; browser font set to 24px (or equivalent 150%) with page zoom at 200%; 320 CSS pixels wide. For each, headline, call to action and first paragraph are visible and nothing overlaps.
