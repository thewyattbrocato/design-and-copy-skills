Use three layouts, switching at two widths. The ad column only exists where the recipe still gets a comfortable reading width. Everywhere else it moves into the flow.

## Behavior by width

| Viewport | Layout | Notes |
|---|---|---|
| **320 to 60em** (phones, small tablets, 960px) | One column: recipe, newsletter, related recipes, ad | Related cards wrap into 2 or 3 across on a tablet with no extra rules. |
| **60em to 80em** (960 to 1280px) | Two columns: recipe plus a rail. The rail holds the newsletter, related recipes and the ad. | The ad sits at the bottom of the rail and sticks while scrolling. |
| **80em and up** (laptop to 34-inch) | Three columns: recipe, rail, ad column. | The whole layout is capped at 100rem and centered. |

- **Recipe column:** it is the flexible one. Text never runs longer than about 68ch, however wide the column gets.
- **Rail:** a fixed 18rem.
- **Ad column:** a fixed 300px. This is a legitimate pixel size because ad creatives are fixed-size.
- **34-inch monitor:** a 3440px-wide screen gets the same 100rem layout with empty margins on both sides. The text isn't stretched and nothing feels tiny. If the empty margins look bare, give the page background a tint or texture. Don't add more columns.
- **Phone ad:** put it after the recipe ends, never between ingredients and steps. Reserve its height (`min-block-size`) so the page doesn't jump when it loads. At 320px the content width is 288px, so ask ad ops for a 300×250 that can shrink, or a 320×50 or 320×100. Otherwise it will overflow.

## CSS

```css
*, *::before, *::after { box-sizing: border-box; }
img { max-inline-size: 100%; block-size: auto; }

.page {
  display: grid;
  gap: 2rem;
  inline-size: min(100% - 2rem, 100rem);
  margin-inline: auto;
  grid-template-columns: minmax(0, 1fr);   /* minmax(0,…) stops long content blowing out the column */
  grid-template-areas: "recipe" "rail" "ad";
}
.recipe { grid-area: recipe; container-type: inline-size; }
.rail   { grid-area: rail; display: grid; gap: 2rem; align-content: start; }
.ad     { grid-area: ad; min-block-size: 15.625rem; /* 250px slot */ }

/* Related recipes: wraps on its own, 1 column in the rail, 2 to 3 on a tablet */
.related-list {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fill, minmax(min(14rem, 100%), 1fr));
}

/* Text measure: cap the text, not the layout */
.recipe :is(p, li, h1, h2) { max-inline-size: 68ch; }

/* Breakpoint 1: viewport question (is there room for a rail beside a 36rem+ recipe?) */
@media (min-width: 60em) {
  .page {
    grid-template-columns: minmax(0, 1fr) 18rem;
    grid-template-areas: "recipe rail" "recipe ad";
    grid-template-rows: auto 1fr;
  }
  .ad { position: sticky; inset-block-start: 1rem; align-self: start; }
}

/* Breakpoint 2: room for a third column */
@media (min-width: 80em) {
  .page {
    grid-template-columns: minmax(0, 1fr) 18rem 300px;
    grid-template-areas: "recipe rail ad";
    grid-template-rows: auto;
  }
}

/* Optional: ingredients beside steps when the recipe column itself is wide */
@container (min-width: 48rem) {
  .recipe-body {
    display: grid;
    grid-template-columns: minmax(14rem, 1fr) minmax(0, 2fr);
    gap: 2rem;
  }
  .ingredients { position: sticky; inset-block-start: 1rem; align-self: start; }
}
```

The ingredients/steps split uses a container query, not a media query. That way it responds to the recipe column's width, whichever of the three layouts it's in.

## Why these numbers

Recipe column widths, using the 1rem gutters and 2rem gaps from the CSS above:

- **960px:** 960 − 32 − 32 − 288 = 608px, about 38rem.
- **1280px:** 1280 − 32 − 64 − 288 − 300 = 596px, about 37rem.
- **Target:** at least about 36rem, which holds roughly 65ch of body text.

Dropping either breakpoint lower would push the recipe below that. Both are in `em`, so they follow the reader's text size.

## Checks for your developer

- At 320px there is no sideways scroll, and the ad doesn't overflow.
- Browser zoom at 200% collapses to the single column and stays readable.
- A very long recipe title or URL in the rail wraps instead of widening the page.
- At 3440px the layout stays centered and no line of text runs wider than about 68 characters.
- The ad doesn't push content down when it loads.

## Assumptions

- 320px is the narrowest screen, and you target current evergreen browsers (needed for container queries).
- You use plain CSS and left-to-right text. For right-to-left, swap `inset-block-start` and the like for logical properties, which this code already uses.
- On tablets between 768 and 960px the single column stays. If your analytics show many readers there, the next step would be a two-column layout at 52em with a narrower 15rem rail.
