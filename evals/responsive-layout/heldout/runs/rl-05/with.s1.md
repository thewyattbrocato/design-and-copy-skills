# Recipe page: column behavior from phone to ultrawide

**Principle:** the recipe text is the only region that matters at every size. Its line length stays fixed at about 65 characters. Narrow screens stack the other regions below it. Wide screens add side columns, and the very widest screens add margins instead of stretching anything.

## Behavior by width

| Viewport | Layout | Ad | Sidebar |
|---|---|---|---|
| **Under 50em** (about 800px: phones, small tablets) | 1 column | Inline banner slots between recipe sections, never a column | Below the recipe: newsletter first, then related recipes in a wrapping grid |
| **50em to 75em** (tablets, small laptops) | 2 columns: recipe plus sidebar | A horizontal banner below the recipe, or at the bottom of the sidebar | Right column, sticky |
| **75em and up** (laptops, desktops) | 3 columns: recipe, sidebar, ad | Right column, 300px wide, sticky | Middle column, about 18rem |
| **Beyond about 100em** (34-inch and larger) | Same 3 columns, **capped at 100rem and centered** | Same | Same |

Two rules cover the extremes:

- **Phone:** side padding is 1rem, and there is no horizontal scrolling at 320px.
- **Ultrawide:** the layout stops growing at 100rem and the extra width becomes empty margin. Do not widen the recipe text past about 65ch to fill it. If the design feels empty at that size, put ingredients and steps side by side inside the recipe column, with ingredients sticky on the left.

That makes **two breakpoints**, both in `em` so they follow the reader's text size. Each one is where a column is added. The ultrawide behavior is a `max-width`, so it needs no breakpoint.

## CSS the developer can start from

```css
*, *::before, *::after { box-sizing: border-box; }
img { max-inline-size: 100%; block-size: auto; }

.recipe-page {
  max-inline-size: 100rem;
  margin-inline: auto;
  padding-inline: 1rem;
  display: grid;
  gap: 2rem;
  grid-template-columns: minmax(0, 1fr);       /* phone: one column */
  grid-template-areas: "recipe" "side" "ad";
}

.recipe  { grid-area: recipe; }
.side    { grid-area: side; }
.ad-col  { grid-area: ad; }

/* Text measure: cap the text, not the column */
.recipe :is(p, li, h1, h2, h3) { max-inline-size: 65ch; overflow-wrap: anywhere; }

/* Related recipes wrap to however many fit */
.related {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fill, minmax(min(12rem, 100%), 1fr));
}

/* Breakpoint 1: add the sidebar */
@media (min-width: 50em) {
  .recipe-page {
    grid-template-columns: minmax(0, 1fr) 18rem;
    grid-template-areas: "recipe side" "ad side";
  }
  .side { position: sticky; top: 1rem; align-self: start; }
}

/* Breakpoint 2: add the ad column */
@media (min-width: 75em) {
  .recipe-page {
    grid-template-columns: minmax(0, 1fr) 18rem 300px;
    grid-template-areas: "recipe side ad";
    padding-inline: 2rem;
  }
  .ad-col { position: sticky; top: 1rem; align-self: start; }
}

/* Ad slots: reserve space so the page doesn't jump when the ad loads */
.ad-slot { min-block-size: 250px; display: grid; place-items: center; }
```

Notes for the developer:

- `minmax(0, 1fr)` on the recipe column stops long ingredient lines or URLs from pushing the grid wider than the screen.
- The ad column is the one place a fixed pixel width is correct, because ad units come in set sizes (300×250, 300×600).
- On phones, a 300px ad doesn't fit inside 1rem of padding on each side at 320px. Let the ad slot go edge to edge, or use 320×50 and 300×250 units centered in it.
- On the 50em to 75em layout, the ad sits under the recipe as a banner. Use a 728×90 or a responsive unit there.
- Keep the sticky sidebar and ad shorter than the viewport. A sticky element taller than the screen gets cut off.

## How I checked it

- **320px:** one column, no horizontal scroll, and related recipes drop to one per row (`min(12rem, 100%)`).
- **About 800px:** the sidebar appears next to the recipe, which is still wider than 65ch, so the text cap applies.
- **About 1200px:** all three columns fit. The recipe gets roughly 1200 − 288 − 300 − gaps ≈ 540px. That is a bit narrow, so test it. If it feels tight, raise breakpoint 2 to 80em.
- **34-inch (about 3440px wide, or about 1720 CSS px at typical scaling):** the layout is centered at 100rem, with the text at 65ch inside the recipe column.

## Assumptions

1. Evergreen browsers, plain CSS, left-to-right text.
2. The newsletter box comes before related recipes on phones. Swap the order if signups matter less than discovery.
3. The ad network supports the sizes above. Confirm that before committing to the 300px column.
