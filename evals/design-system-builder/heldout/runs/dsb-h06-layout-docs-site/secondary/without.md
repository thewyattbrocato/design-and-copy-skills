Use three widths: a 68ch reading column for prose, a 75rem container for grids and the pricing table, and a bleed rule that lets code and wide tables stretch to the container. Breakpoints sit at 40rem and 60rem. I haven't checked for existing site CSS, since this directory isn't a repo, so treat these as a starting point.

## The numbers

| Token | Value | Px at 16px root | Used for |
|---|---|---|---|
| `--gutter` | `clamp(1rem, 4vw, 3rem)` | 16 → 48 | Side padding on every page |
| `--prose` | `68ch` | ~680 at body size | Article text, hero copy, any running text |
| `--wide` | `75rem` | 1200 | Outer container: feature rows, pricing, bleed blocks |
| `--gap` | `clamp(1rem, 2.5vw, 2rem)` | 16 → 32 | Grid gutters |
| Breakpoint A | `40rem` | 640 | Pricing goes to 2 columns |
| Breakpoint B | `60rem` | 960 | Pricing goes to 3 columns; feature rows go side by side |

Reserve `80rem` (1280) for a four-tier pricing grid. Nothing should grow past 1200px on a big monitor; the extra width becomes margin.

Body text is 17px with a 1.7 line height. Code is 14px. Those two sizes keep the 68ch measure close to 70 characters.

## The CSS

```css
:root {
  --gutter: clamp(1rem, 4vw, 3rem);
  --prose: 68ch;
  --wide: 75rem;
  --gap: clamp(1rem, 2.5vw, 2rem);
  --body-size: 1.0625rem;
  --code-size: 0.875rem;
}

/* Outer frame for every section, article or marketing */
.container {
  width: min(100% - 2 * var(--gutter), var(--wide));
  margin-inline: auto;
}

/* Running text: capped measure, centered in the container */
.prose {
  max-width: var(--prose);
  margin-inline: auto;
  font-size: var(--body-size);
  line-height: 1.7;
}

/* Code blocks, wide tables, wide images: stretch to the container,
   not the reading column. Works on phones too (full width minus gutters). */
.bleed {
  width: min(var(--wide), 100vw - 2 * var(--gutter));
  position: relative;
  left: 50%;
  translate: -50% 0;
}

/* Horizontal scroll instead of breaking the layout */
.bleed.scroll,
.bleed:is(pre) {
  overflow-x: auto;
}

pre {
  font-size: var(--code-size);
  line-height: 1.6;
  padding: 1rem 1.25rem;
  white-space: pre;
}

table {
  min-width: 36rem;
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  padding: 0.5em 0.75em;
  text-align: left;
  vertical-align: top;
}

/* Pricing: 1 → 2 → 3 columns */
.pricing {
  display: grid;
  gap: var(--gap);
  grid-template-columns: minmax(0, 1fr);
}

@media (min-width: 40rem) {
  .pricing { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}

@media (min-width: 60rem) {
  .pricing { grid-template-columns: repeat(3, minmax(0, 1fr)); }
}

/* Feature rows: stacked, then side-by-side */
.feature {
  display: grid;
  gap: var(--gap);
  align-items: center;
}

@media (min-width: 60rem) {
  .feature {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 4rem;
  }
  .feature.reverse > :first-child { order: 2; }
}
```

## Usage

```html
<section class="container">
  <div class="prose">
    <h1>Article title</h1>
    <p>Body text stays at the measure.</p>
    <div class="bleed"><pre><code>long code line here</code></pre></div>
    <div class="bleed scroll"><table>…</table></div>
  </div>
</section>

<section class="container">
  <div class="pricing">…three tier cards…</div>
</section>

<section class="container">
  <div class="feature">
    <img src="…" alt="">
    <div><h2>Feature</h2><p>…</p></div>
  </div>
</section>
```

## Notes

- Front page and articles share the same `.container`, so the pricing grid and the article code blocks line up on the same outer edges.
- `.bleed` relies on the `.prose` parent not having `overflow: hidden`. Don't put `overflow: hidden` on the article wrapper.
- `100vw` includes the scrollbar on desktop, so bleed blocks can be about 15px wider than the visible area there. If that shows, switch to a grid-based full-bleed layout.
- The pricing rules assume three tiers. If you have four, use `repeat(4, …)` at `80rem`.
- Media queries can't read custom properties, so the breakpoints are literal values. Keep them in sync if you change them.

If you paste the existing stylesheet or the front-page markup, I can map these onto your current class names.
