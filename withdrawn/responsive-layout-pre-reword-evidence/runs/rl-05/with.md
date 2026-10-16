# Recipe page: column behavior from phone to 34-inch monitor

The page shell is the one place a viewport media query is the right tool, because the question is how the whole page is arranged. It needs two breakpoints, written in `em` so they follow the reader's text size. Everything inside the columns stays fluid.

## Behavior by width

| Width | Layout | Why |
|---|---|---|
| **Under 48em** (phones, about 768px at default text size) | **One column**, in this order: recipe, newsletter, related recipes, ad. | Readers came for the recipe, so it comes first. Ads become in-flow slots, not a column. |
| **48em to 75em** (tablets, small laptops) | **Two columns**: recipe (flexible) and sidebar (about 20rem). The sidebar holds related recipes and the newsletter. The ad drops to a full-width slot below the recipe, or into the sidebar. | There isn't room for three columns without squeezing the recipe below a comfortable line length. |
| **75em and up** (laptops and desktops) | **Three columns**: recipe, sidebar (about 18rem), ad column (about 19rem). | This is your current design, so the laptop view is unchanged. |
| **Very wide** (34-inch and up) | The same three columns, in a wrapper capped at about 90rem and centered. The extra space becomes side margins. | Past that width, stretching the columns makes lines of text too long to read and spreads the content too far apart. |

Two rules hold at every width:
- **The recipe text is capped at about 65ch.** Ingredients and method steps never run edge to edge, even if the column is wider.
- **The sidebar and ad columns have fixed widths, and the recipe takes the remaining space.** Only the recipe column flexes.

## CSS to build from

```css
/* Global */
*, *::before, *::after { box-sizing: border-box; }
html { font-size: 100%; }            /* leave the reader's default alone */
img { max-inline-size: 100%; block-size: auto; }

.recipe-page {
  display: grid;
  grid-template-columns: minmax(0, 1fr);   /* minmax(0,…) lets long words/URLs shrink */
  grid-template-areas:
    "recipe"
    "newsletter"
    "related"
    "ad";
  gap: 2rem;
  max-inline-size: 90rem;                  /* the 34-inch cap */
  margin-inline: auto;
  padding-inline: max(1rem, env(safe-area-inset-left));
}

.recipe     { grid-area: recipe; }
.newsletter { grid-area: newsletter; }
.related    { grid-area: related; }
.ad         { grid-area: ad; }

/* Text measure: cap the text, not the column */
.recipe :is(p, li, h1, h2, h3) {
  max-inline-size: 65ch;
  overflow-wrap: anywhere;
}

/* Two columns: the sidebar appears */
@media (min-width: 48em) {
  .recipe-page {
    grid-template-columns: minmax(0, 1fr) 20rem;
    grid-template-areas:
      "recipe     newsletter"
      "recipe     related"
      "ad         ad";
    align-items: start;
  }
}

/* Three columns: the ad column appears */
@media (min-width: 75em) {
  .recipe-page {
    grid-template-columns: minmax(0, 1fr) 18rem 19rem;
    grid-template-areas:
      "recipe newsletter ad"
      "recipe related    ad";
  }
  .ad { position: sticky; inset-block-start: 1rem; }
}
```

The newsletter and related-recipes boxes are separate grid items, so each can be reordered on its own. If your developer would rather have one sidebar element, nest them in a wrapper and use a single `sidebar` area.

## Notes for your developer

- **Ads:** reserve each slot's height with `min-block-size` so the page doesn't jump when the ad loads. Under 48em, use a mobile ad size (about 300×250) in the in-flow slot. Don't load the desktop ad unit into a hidden column.
- **Newsletter:** under 48em it sits directly after the recipe. Nothing should cover the recipe on first load, so no sticky banner or pop-up there.
- **Related recipes:** use a wrapping grid, `grid-template-columns: repeat(auto-fill, minmax(min(12rem, 100%), 1fr))`. It then gives one column in the sidebar and a row of cards when it is full width in the stacked layout.
- **Type:** keep sizes in `rem`, not `px`. Don't block zoom in the viewport meta tag.

## What to check
- **320px wide:** no sideways scroll, and nothing clipped.
- **200% text size:** nothing overlaps or hides.
- **Long strings:** paste a very long URL into the ingredient notes to confirm it wraps.
- **Boundary widths:** look at 47em and 49em, and at 74em and 76em, to see that each column change looks right.
- **Very wide:** test a window wider than 90rem to confirm the content stays centered.

## Assumptions
1. The narrowest supported width is 320px, and the page is read left to right.
2. Evergreen browsers only, so `grid` and `sticky` need no fallbacks.
3. The breakpoints use your content and ad sizes (20rem, 18rem and 19rem columns). Resize in the browser and adjust the two `em` values if the recipe column looks cramped before they trigger.
